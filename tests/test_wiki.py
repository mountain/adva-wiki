import contextlib
from http.client import HTTPConnection
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import threading
import unittest
from urllib.parse import urlsplit

from adva_wiki.config import load_config
from adva_wiki.render import MetadataError, UnknownLanguage, parse_page, render_markdown, render_page
from adva_wiki.revisions import Revisions
from adva_wiki.wikify import wikify
from adva_wiki.server import content_path, create_server


class RenderingTests(unittest.TestCase):
    def test_red_link_for_unresolved_wiki_target(self):
        exists = {"torsor.md", "README.md"}.__contains__
        html = parse_page(
            "see [[torsor]] and [[missing concept]]", page_exists=exists
        ).render().html
        self.assertIn('href="/wiki/torsor.md"', html)
        self.assertIn('href="/wiki/missing%20concept.md" class="red-link"', html)

    def test_no_red_link_without_page_exists_callback(self):
        html = parse_page("see [[missing concept]]").render().html
        self.assertNotIn('class="red-link"', html)

    def test_gfm(self):
        html = render_markdown(
            "| A | B |\n| --- | --- |\n| 1 | 2 |\n\n"
            "~~old~~\n\n- [x] Done\n\nhttps://example.com\n\n```python\nprint(1)\n```"
        )
        for expected in ("<table>", "<s>old</s>", 'type="checkbox"',
                         'href="https://example.com"', 'class="language-python"'):
            self.assertIn(expected, html)

    def test_wiki_links_anchors_and_images(self):
        html = render_markdown(
            "# Some heading\n\n[[guides/Some page#some-heading|Read more]]\n\n"
            "[[#some-heading|Here]]\n\n![Diagram](images/diagram.png)"
        )
        self.assertIn('id="some-heading"', html)
        self.assertIn('href="/wiki/guides/Some%20page.md#some-heading">Read more', html)
        self.assertIn('href="#some-heading">Here', html)
        self.assertIn('src="images/diagram.png"', html)

    def test_math_and_code(self):
        html = render_markdown(
            "$x^2$\n\n$$\ny = 2\n$$\n\n```math\nz^2\n```\n\n"
            "`[[Not a link]] $not_math$`\n\n```text\n[[Not a link]]\n```"
        )
        self.assertIn('class="math inline">x^2', html)
        self.assertEqual(html.count('class="math block"'), 2)
        self.assertNotIn("/wiki/", html)
        self.assertIn("<code>[[Not a link]] $not_math$</code>", html)

    def test_untrusted_markup(self):
        html = render_markdown(
            '<script>alert(1)</script>\n\n[x](javascript:alert(1))\n\n'
            '[[javascript:alert(1)|<img onerror=alert(1)>]]\n\n'
            '$<script>alert(1)</script>$'
        )
        self.assertNotIn("<script>", html)
        self.assertNotIn("<img", html)
        self.assertNotIn('href="javascript:', html)


class MultilingualRenderingTests(unittest.TestCase):
    SOURCE = """---
languages:
  en: Torsor
  zh: "挠子（Torsor）"
default: en
---

# Torsor

English body with [[README|home]] and $x$.

## Definition

A $G$-torsor.

# 挠子（Torsor）

中文正文，包含 $x$。

## 定义

一个 $G$-挠子。

# References

Shared references.
"""

    def test_default_language_and_shared_sections(self):
        page = render_page(self.SOURCE)
        self.assertEqual((page.language, page.default, page.title), ("en", "en", "Torsor"))
        self.assertEqual([language.code for language in page.languages], ["en", "zh"])
        self.assertIn("English body", page.html)
        self.assertNotIn("中文正文", page.html)
        self.assertIn("Shared references", page.html)
        self.assertNotIn("languages:", page.html)

    def test_selected_language(self):
        page = render_page(self.SOURCE, "zh")
        self.assertEqual((page.language, page.title), ("zh", "挠子（Torsor）"))
        self.assertIn("中文正文", page.html)
        self.assertNotIn("English body", page.html)
        self.assertIn('id="挠子torsor"', page.html)

    def test_default_falls_back_to_first_language(self):
        source = self.SOURCE.replace("default: en\n", "")
        page = render_page(source)
        self.assertEqual((page.language, page.default), ("en", "en"))
        source = self.SOURCE.replace("default: en\n", "").replace(
            "languages:\n  en: Torsor\n  zh:", "languages:\n  zh:"
        )
        page = render_page(source)
        self.assertEqual((page.language, page.default), ("zh", "zh"))

    def test_unknown_language_and_bad_metadata(self):
        with self.assertRaises(UnknownLanguage):
            render_page(self.SOURCE, "fr")
        for broken in (
            self.SOURCE.replace("  zh: \"挠子（Torsor）\"", "  zh: Missing"),
            self.SOURCE.replace("  en: Torsor", "  e: Torsor"),
            self.SOURCE.replace("  en: Torsor", "  en: Torsor\n  e: Other"),
            self.SOURCE.replace("default: en", "default: fr"),
            self.SOURCE.replace("  zh: \"挠子（Torsor）\"", "  zh: Torsor"),
            self.SOURCE.replace("  zh: \"挠子（Torsor）\"", "  zh: \"\""),
        ):
            with self.subTest(metadata=broken.splitlines()[1:4]), self.assertRaises(MetadataError):
                render_page(broken)

    def test_plain_markdown_is_unchanged(self):
        self.assertIn("<h1 id=\"title\">Title</h1>", render_markdown("# Title"))
        self.assertIn("<hr />", render_markdown("---\n\n# Title"))


class WikiTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.docs = self.root / "docs"
        self.docs.mkdir()
        self.page = self.docs / "README.md"
        self.page.write_text("# First\n\nOriginal $x$.\n", encoding="utf-8")
        (self.docs / "nested").mkdir()
        (self.docs / "nested" / "Page name.md").write_text(
            "# Nested\n\n![Image](pixel.png)\n\n[[README|Home]]", encoding="utf-8",
        )
        (self.docs / "nested" / "pixel.png").write_bytes(b"\x89PNG\r\n\x1a\n")
        self.config_path = self.root / "wiki.toml"
        self.config_path.write_text(
            '[wiki]\ncontent_dir = "docs"\ntitle = "<Wiki>"\n'
            '[server]\nport = 0\n'
            '[[projects]]\nname = "related"\npath = "../related"\n'
            '[[feeds]]\nname = "News"\nurl = "https://example.com/feed.xml"\n',
            encoding="utf-8",
        )
        self.config = load_config(self.config_path)

    def git(self, *args):
        return subprocess.check_output(
            ["git", "-C", str(self.root), *args], stderr=subprocess.PIPE, text=True,
        ).strip()

    def commit(self, message):
        self.git("add", "docs")
        self.git("-c", "user.name=Test Author", "-c", "user.email=test@example.com",
                 "commit", "-m", message)
        return self.git("rev-parse", "HEAD")

    @contextlib.contextmanager
    def serving(self):
        with create_server(self.config) as server:
            worker = threading.Thread(target=server.serve_forever, daemon=True)
            worker.start()
            try:
                yield server.server_port
            finally:
                server.shutdown()
                worker.join()

    def request(self, port, path, method="GET"):
        with contextlib.closing(HTTPConnection("127.0.0.1", port, timeout=5)) as connection:
            connection.request(method, path)
            response = connection.getresponse()
            return response.status, dict(response.getheaders()), response.read()

    def backlinks(self, port, path):
        status, _, body = self.request(port, path)
        self.assertEqual(status, 200)
        section = body.partition(b'<section class="backlinks">')[2].partition(b"</section>")[0]
        return re.findall(r'<li><a href="([^"]+)">', section.decode())

    def test_config_paths_and_manifest_cli(self):
        self.assertEqual(self.config.content_dir, self.docs)
        self.assertEqual(self.config.projects[0]["path"], str((self.root.parent / "related").resolve()))
        output = subprocess.check_output(
            [sys.executable, "-m", "adva_wiki", "sources",
             "--config", str(self.config_path)], text=True,
        )
        manifest = json.loads(output)
        self.assertEqual(manifest["content_dir"], str(self.docs))
        self.assertEqual(manifest["feeds"][0]["url"], "https://example.com/feed.xml")

    def test_invalid_configuration(self):
        for text in ('[server]\nport = -1', '[[feeds]]\nname = "Bad"\nurl = "file:///etc/passwd"',
                     '[[projects]]\nname = "Missing path"'):
            with self.subTest(text=text):
                self.config_path.write_text(text, encoding="utf-8")
                with self.assertRaises(ValueError):
                    load_config(self.config_path)

    def test_content_path_safety(self):
        (self.docs / "outside.md").symlink_to(self.config_path)
        (self.docs / "loop.md").symlink_to("loop.md")
        for name in ("../wiki.toml", ".git/config", "/etc/passwd", "nested/../../wiki.toml",
                     "nested\\..\\README.md", "outside.md", "loop.md", ".secret.md"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                content_path(self.docs, name)

    def test_page_routes_and_headers(self):
        with self.serving() as port:
            status, headers, body = self.request(port, "/")
            self.assertEqual((status, headers["Location"]), (302, "/wiki/README.md"))
            status, headers, body = self.request(port, "/wiki/README.md")
            self.assertEqual(status, 200)
            self.assertIn(b'<h1 id="first">First</h1>', body)
            self.assertIn(b"&lt;Wiki&gt;", body)
            self.assertIn(b"katex@0.16.22", body)
            self.assertEqual(headers["X-Content-Type-Options"], "nosniff")
            self.assertIn("frame-ancestors 'none'", headers["Content-Security-Policy"])
            status, headers, body = self.request(port, "/wiki/README.md", "HEAD")
            self.assertEqual((status, body), (200, b""))
            status, _, body = self.request(port, "/wiki/nested/Page%20name.md")
            self.assertEqual(status, 200)
            self.assertIn(b'src="pixel.png"', body)
            self.assertIn(b'href="/wiki/README.md"', body)
            self.page.write_text("# Updated live", encoding="utf-8")
            self.assertIn(b"Updated live", self.request(port, "/wiki/README.md")[2])

    def test_backlinks_match_forward_links_and_allow_cycles(self):
        source = self.docs / "nested" / "Page name.md"
        source.write_text(
            "# Nested\n\n## Wiki link\n\n[[README#first|First]]\n\n"
            "## Markdown reference link\n\n[First][home]\n\n[home]: ../README.md#first\n",
            encoding="utf-8",
        )
        (self.docs / "nested" / "Other.md").write_text(
            "# Other\n\n[First][home]\n\n[home]: ../README.md#first\n", encoding="utf-8",
        )
        self.page.write_text("# First\n\n[[nested/Page name#nested|Nested]]\n", encoding="utf-8")

        with self.serving() as port:
            home_url, source_url = "/wiki/README.md", "/wiki/nested/Page%20name.md"
            incoming = self.backlinks(port, home_url)
            self.assertEqual([urlsplit(link).path for link in incoming], [
                "/wiki/nested/Other.md", source_url,
            ])
            for backlink, forward in zip(incoming, ("../README.md#first", home_url + "#first")):
                origin = urlsplit(backlink)
                source_html = self.request(port, origin.path)[2]
                self.assertIn(f'id="{origin.fragment}" href="{forward}"'.encode(), source_html)

            home_html = self.request(port, home_url)[2]
            self.assertIn("nested/Page name · Wiki link".encode(), home_html)
            (return_link,) = self.backlinks(port, source_url)
            origin = urlsplit(return_link)
            self.assertEqual(origin.path, home_url)
            self.assertIn(f'id="{origin.fragment}" href="{source_url}#nested"'.encode(), home_html)

    def test_backlinks_update_after_edits_renames_and_removal(self):
        target = self.docs / "Concept.md"
        target.write_text("# Concept\n\n## Detail\n", encoding="utf-8")
        self.page.write_text("# First\n\n[[Concept#detail]]", encoding="utf-8")
        with self.serving() as port:
            self.assertEqual(len(self.backlinks(port, "/wiki/Concept.md")), 1)
            target.write_text("# Concept\n\n## Renamed heading\n", encoding="utf-8")
            self.assertEqual(self.backlinks(port, "/wiki/Concept.md"), [])
            self.page.write_text("# First\n\n[[Concept#renamed-heading]]", encoding="utf-8")
            self.assertEqual(len(self.backlinks(port, "/wiki/Concept.md")), 1)

            target.rename(self.docs / "Renamed.md")
            self.assertEqual(self.request(port, "/wiki/Concept.md")[0], 404)
            self.assertEqual(self.backlinks(port, "/wiki/Renamed.md"), [])
            self.page.write_text("# First\n\n[[Renamed]]", encoding="utf-8")
            moved = self.page.rename(self.docs / "Moved source.md")
            (backlink,) = self.backlinks(port, "/wiki/Renamed.md")
            self.assertEqual(urlsplit(backlink).path, "/wiki/Moved%20source.md")
            moved.unlink()
            self.assertEqual(self.backlinks(port, "/wiki/Renamed.md"), [])

    def test_backlinks_exclude_unresolved_targets_and_unservable_sources(self):
        (self.docs / "Invalid links.md").write_text(
            "[[Missing]] [[README#absent]] [[README.xx]]\n\n"
            "[Unknown language](README.md?lang=xx) [History](README.md?history=1)\n\n"
            "[External](https://example.com/wiki/README.md) [External](//example.com/wiki/README.md)\n\n"
            "[Invalid path](/wiki/nested/%2e%2e/README.md) ![Image](README.md)\n\n"
            "`[[README]]` $[[README]]$\n\n```markdown\n[[README]]\n```\n",
            encoding="utf-8",
        )
        (self.docs / ".private.md").write_text("[[README]]", encoding="utf-8")
        (self.docs / "symlink.md").symlink_to(self.docs / "nested" / "Page name.md")
        (self.docs / "invalid-utf8.md").write_bytes(b"[[README]]\xff")
        (self.docs / "invalid-metadata.md").write_text(
            "---\nlanguages:\n  en: Declared\n---\n\n# Other\n\n[[README]]", encoding="utf-8",
        )
        with self.serving() as port:
            (backlink,) = self.backlinks(port, "/wiki/README.md")
            self.assertEqual(urlsplit(backlink).path, "/wiki/nested/Page%20name.md")
            self.assertEqual(self.request(port, "/wiki/Invalid%20links.md")[0], 200)

    def test_backlinks_follow_the_selected_language_and_shared_sections(self):
        (self.docs / "nested" / "Concept.md").write_text(
            "---\nlanguages:\n  en: Concept\n  zh: 概念\n---\n\n"
            "# Concept\n\n## Definition\n\n# 概念\n\n## Definition\n\n## 定义\n",
            encoding="utf-8",
        )
        (self.docs / "Source.md").write_text(
            "---\nlanguages:\n  en: English source\n  zh: 中文来源\n---\n\n"
            "# English source\n\n[[nested/Concept#definition]]\n\n"
            "# 中文来源\n\n## 中文引用\n\n[[nested/Concept.zh#definition-1]]\n\n"
            "[定义](nested/Concept.md?lang=zh#定义) [[nested/Concept#定义]] [[#中文引用]]\n\n"
            "# Shared\n\n[[nested/Concept#definition]]\n",
            encoding="utf-8",
        )
        with self.serving() as port:
            en = self.backlinks(port, "/wiki/nested/Concept.md")
            self.assertEqual(en, self.backlinks(port, "/wiki/nested/Concept.en.md"))
            self.assertEqual([urlsplit(link).path for link in en], [
                "/wiki/Source.md", "/wiki/Source.zh.md",
            ])
            shared = urlsplit(en[1]).fragment
            self.assertIn(f'id="{shared}"'.encode(), self.request(port, "/wiki/Source.md")[2])
            zh = self.backlinks(port, "/wiki/nested/Concept.zh.md")
            self.assertEqual(zh, self.backlinks(port, "/wiki/nested/Concept.md?lang=zh"))
            self.assertEqual([urlsplit(link).path for link in zh], ["/wiki/Source.zh.md"])
            source = self.request(port, "/wiki/Source.zh.md")[2]
            for current in zh:
                self.assertIn(f'id="{urlsplit(current).fragment}"'.encode(), source)
            self.assertEqual(self.backlinks(port, "/wiki/Source.zh.md"), [])

    def test_backlinks_distinguish_a_real_file_from_a_shadowed_language_alias(self):
        (self.docs / "Topic.md").write_text(
            "---\nlanguages:\n  en: Topic\n  zh: 主题\n---\n\n"
            "# Topic\n\n# 主题\n\n[[README]]\n", encoding="utf-8",
        )
        (self.docs / "Topic.zh.md").write_text("# Physical page\n", encoding="utf-8")
        self.page.write_text(
            "# First\n\n[[Topic.zh]] [Translation](Topic.md?lang=zh)\n", encoding="utf-8",
        )
        with self.serving() as port:
            self.assertEqual(self.backlinks(port, "/wiki/Topic.md"), [])
            (physical,) = self.backlinks(port, "/wiki/Topic.zh.md")
            (translation,) = self.backlinks(port, "/wiki/Topic.md?lang=zh")
            self.assertNotEqual(physical, translation)
            home = self.backlinks(port, "/wiki/README.md")
            (backlink,) = [link for link in home if urlsplit(link).path == "/wiki/Topic.md"]
            self.assertEqual(urlsplit(backlink).query, "lang=zh")
            source = self.request(port, "/wiki/Topic.md?lang=zh")[2]
            self.assertIn(f'id="{urlsplit(backlink).fragment}" href="/wiki/README.md"'.encode(), source)

    def test_automatic_links_choose_longest_and_first_eligible_mention(self):
        for title in ("A", "AB"):
            (self.docs / f"{title}.md").write_text(f"# {title}\n", encoding="utf-8")
        self.page.write_text(
            "# Before A and AB\n\nABC and `A` and $AB$. [AB](https://example.com/).\n\n"
            "A[**B**](https://example.com/), then **AB**, then A, AB and A.\n",
            encoding="utf-8",
        )
        with self.serving() as port:
            source = self.request(port, "/wiki/README.md")[2]
            self.assertIn(b"<code>A</code>", source)
            self.assertIn(b'A<a href="https://example.com/"><strong>B</strong></a>', source)
            self.assertIn(b'<strong><a id="wiki-ref:auto-1" href="/wiki/AB.md">AB</a></strong>', source)
            self.assertIn(b'then <a id="wiki-ref:auto-2" href="/wiki/A.md">A</a>, AB and A.', source)
            self.assertEqual(source.count(b'href="/wiki/A.md"'), 1)
            self.assertEqual(source.count(b'href="/wiki/AB.md"'), 1)
            self.assertEqual(self.backlinks(port, "/wiki/AB.md"), ["/wiki/README.md#wiki-ref:auto-1"])
            self.assertEqual(self.backlinks(port, "/wiki/A.md"), ["/wiki/README.md#wiki-ref:auto-2"])

    def test_automatic_links_handle_chinese_overlaps_and_ambiguous_names(self):
        (self.docs / "Geometry.md").write_text("# 几何\n", encoding="utf-8")
        (self.docs / "Principles.md").write_text("# 几何原理\n", encoding="utf-8")
        self.page.write_text(
            "# 学习笔记\n\n先读几何[原理](https://example.com/)，再读几何原理和几何。\n",
            encoding="utf-8",
        )
        with self.serving() as port:
            source = self.request(port, "/wiki/README.md")[2].decode()
            self.assertIn('先读几何<a href="https://example.com/">原理</a>', source)
            self.assertIn('再读<a id="wiki-ref:auto-1" href="/wiki/Principles.md">几何原理</a>', source)
            self.assertIn('和<a id="wiki-ref:auto-2" href="/wiki/Geometry.md">几何</a>', source)

            (self.docs / "Duplicate.md").write_text("# 几何原理\n", encoding="utf-8")
            source = self.request(port, "/wiki/README.md")[2].decode()
            self.assertIn('再读几何原理和<a id="wiki-ref:auto-1" href="/wiki/Geometry.md">几何</a>', source)
            self.assertEqual(self.backlinks(port, "/wiki/Principles.md"), [])
            self.assertEqual(self.backlinks(port, "/wiki/Duplicate.md"), [])

    def test_first_valid_authored_link_takes_precedence_over_automatic_links(self):
        (self.docs / "AB.md").write_text("# AB\n\n## Definition\n", encoding="utf-8")
        self.page.write_text(
            "# Source\n\nAB first as text. [[AB#missing|Old AB]]\n\n"
            "[AB](AB.md#definition) and [[AB|AB again]]. AB.\n",
            encoding="utf-8",
        )
        with self.serving() as port:
            (backlink,) = self.backlinks(port, "/wiki/AB.md")
            source = self.request(port, "/wiki/README.md")[2]
            self.assertIn(b"AB first as text.", source)
            self.assertNotIn(b'wiki-ref:auto-', source)
            self.assertIn(f'id="{urlsplit(backlink).fragment}" href="AB.md#definition"'.encode(), source)
            self.assertIn(b'href="/wiki/AB.md">AB again</a>', source)

    def test_automatic_links_use_the_recognized_language_view(self):
        (self.docs / "Algebra.md").write_text(
            "---\nlanguages:\n  en: Algebra\n  zh: 代数\n---\n\n# Algebra\n\n# 代数\n",
            encoding="utf-8",
        )
        (self.docs / "Source.md").write_text(
            "---\nlanguages:\n  en: English source\n  zh: 中文来源\n---\n\n"
            "# English source\n\nAlgebra and 代数.\n\n"
            "# 中文来源\n\n先看代数，再看 Algebra。\n\n# Shared\n\nAlgebra and 代数.\n",
            encoding="utf-8",
        )
        with self.serving() as port:
            self.assertEqual(self.backlinks(port, "/wiki/Algebra.md"), ["/wiki/Source.md#wiki-ref:auto-1"])
            self.assertEqual(self.backlinks(port, "/wiki/Algebra.zh.md"), ["/wiki/Source.zh.md#wiki-ref:auto-1"])
            for source_url, target_url in (("/wiki/Source.md", "/wiki/Algebra.md"),
                                           ("/wiki/Source.md?lang=zh", "/wiki/Algebra.zh.md")):
                source = self.request(port, source_url)[2]
                self.assertIn(f'id="wiki-ref:auto-1" href="{target_url}"'.encode(), source)
                self.assertEqual(source.count(b"wiki-ref:auto-"), 1)

    def test_multilingual_language_subpages(self):
        (self.docs / "images").mkdir()
        (self.docs / "images" / "pixel.png").write_bytes(b"\x89PNG\r\n\x1a\n")
        self.git("init")
        (self.docs / "torsor.md").write_text("# Torsor\n\nOld body.\n", encoding="utf-8")
        old = self.commit("Old torsor")
        (self.docs / "torsor.md").write_text(
            '---\n'
            'languages:\n'
            '  en: Torsor\n'
            '  zh: "挠子（Torsor）"\n'
            'default: en\n'
            '---\n\n'
            '# Torsor\n\nEnglish body.\n\n![Image](images/pixel.png)\n\n'
            '# 挠子（Torsor）\n\n中文正文。\n\n![图像](images/pixel.png)\n\n'
            '# References\n\nShared references.\n',
            encoding="utf-8",
        )
        sha = self.commit("Add torsor")
        with self.serving() as port:
            status, _, body = self.request(port, "/wiki/torsor.md")
            self.assertEqual(status, 200)
            self.assertIn(b'<html lang="en">', body)
            self.assertIn(b"English body", body)
            self.assertNotIn("中文正文".encode(), body)
            self.assertIn(b'href="/wiki/torsor.zh.md"', body)
            self.assertIn(b'src="images/pixel.png"', body)
            self.assertIn(b"Shared references", body)
            self.assertNotIn(b"languages:", body)

            status, _, body = self.request(port, "/wiki/torsor.zh.md")
            self.assertEqual(status, 200)
            self.assertIn(b'<html lang="zh">', body)
            self.assertIn("中文正文".encode(), body)
            self.assertNotIn(b"English body", body)
            self.assertIn(b'href="/wiki/torsor.md"', body)
            self.assertIn(b'src="images/pixel.png"', body)
            self.assertIn(b'aria-current="page"', body)

            status, _, body = self.request(port, "/wiki/torsor.md?lang=zh")
            self.assertEqual(status, 200)
            self.assertIn("中文正文".encode(), body)

            self.assertEqual(self.request(port, "/wiki/torsor.xx.md")[0], 404)
            self.assertEqual(self.request(port, "/wiki/torsor.md?lang=xx")[0], 404)

            status, _, body = self.request(port, f"/wiki/torsor.zh.md?rev={sha}")
            self.assertEqual(status, 200)
            self.assertIn("中文正文".encode(), body)
            self.assertIn(b"Shared references", body)
            self.assertIn(f"rev={sha}".encode(), body)

            status, _, body = self.request(port, f"/wiki/torsor.zh.md?rev={old}")
            self.assertEqual(status, 200)
            self.assertIn(b"Old body", body)
            self.assertIn(b"not available in this revision", body)

            status, _, history = self.request(port, "/wiki/torsor.zh.md?history=1")
            self.assertEqual(status, 200)
            self.assertIn(sha.encode(), history)

            status, _, pages = self.request(port, "/pages")
            self.assertEqual(status, 200)
            self.assertIn(b"torsor.md", pages)
            self.assertNotIn(b"torsor.zh.md", pages)

    def test_invalid_page_metadata_is_a_server_error(self):
        (self.docs / "broken.md").write_text(
            '---\nlanguages:\n  en: Declared title\n---\n\n# Another title\n',
            encoding="utf-8",
        )
        with self.serving() as port:
            status, _, body = self.request(port, "/wiki/broken.md")
            self.assertEqual(status, 500)
            self.assertIn(b"Invalid page metadata", body)

    def test_images_static_assets_and_index(self):
        (self.docs / ".hidden.md").write_text("Private", encoding="utf-8")
        (self.docs / "leak.md").symlink_to(self.config_path)
        with self.serving() as port:
            status, headers, image = self.request(port, "/wiki/nested/pixel.png")
            self.assertEqual(status, 200)
            self.assertEqual(headers["Content-Type"], "image/png")
            self.assertTrue(image.startswith(b"\x89PNG"))
            status, _, pages = self.request(port, "/pages")
            self.assertEqual(status, 200)
            self.assertIn(b"nested/Page%20name.md", pages)
            self.assertNotIn(b".hidden", pages)
            self.assertNotIn(b"leak", pages)
            for name in ("wiki.js", "wiki.css"):
                self.assertEqual(self.request(port, "/static/" + name)[0], 200)

    def test_http_rejects_unsafe_paths_and_non_content(self):
        with self.serving() as port:
            for path in ("/wiki/%2e%2e/wiki.toml", "/wiki/.git/config", "/wiki/.secret.md"):
                self.assertEqual(self.request(port, path)[0], 400)
            for path in ("/wiki/missing.md", "/wiki/config.toml", "/wiki/image.svg",
                         "/static/../wiki.toml", "/unknown"):
                self.assertEqual(self.request(port, path)[0], 404)
            self.assertEqual(self.request(port, "/wiki/README.md", "POST")[0], 501)

    def test_git_history_revision_and_diff(self):
        self.git("init")
        first = self.commit("First revision")
        self.page.write_text("# Second\n\nNew content", encoding="utf-8")
        second = self.commit("<script>Second</script>")
        revisions = Revisions(self.docs)
        self.assertEqual([item["sha"] for item in revisions.history(self.page)], [second, first])
        self.assertIn("# First", revisions.read(self.page, first))
        self.assertIn("+New content", revisions.diff(self.page, second))
        self.assertIn("+# First", revisions.diff(self.page, first))
        with self.serving() as port:
            status, _, history = self.request(port, "/wiki/README.md?history=1")
            self.assertEqual(status, 200)
            self.assertIn(first.encode(), history)
            self.assertNotIn(b"<script>Second", history)
            self.assertIn(b"&lt;script&gt;Second", history)
            archived = self.request(port, f"/wiki/README.md?rev={first}")[2]
            self.assertIn(b">First</h1>", archived)
            self.assertNotIn(b'class="backlinks"', archived)
            self.assertIn(b"+New content", self.request(port, f"/wiki/README.md?diff={second}")[2])
            self.page.unlink()
            self.assertEqual(self.request(port, f"/wiki/README.md?rev={first}")[0], 200)
            self.assertEqual(self.request(port, "/wiki/README.md?rev=--help")[0], 400)
            self.assertEqual(self.request(port, "/wiki/README.md?rev=" + "0" * 40)[0], 404)

    def test_no_git_and_untracked_pages(self):
        with self.serving() as port:
            self.assertEqual(self.request(port, "/wiki/README.md")[0], 200)
            self.assertEqual(self.request(port, "/wiki/README.md?history=1")[0], 404)
        self.git("init")
        self.commit("Initial")
        (self.docs / "new.md").write_text("# New", encoding="utf-8")
        self.assertEqual(Revisions(self.docs).history(self.docs / "new.md"), [])


class WikifyTests(unittest.TestCase):
    def test_direct_replacement_and_longest_first(self):
        self.assertEqual(
            wikify("the basic hyperbolic model and hyperbolic model",
                   ["basic hyperbolic model", "hyperbolic model"]),
            "the [[basic hyperbolic model]] and [[hyperbolic model]]",
        )

    def test_first_mention_only(self):
        self.assertEqual(
            wikify("dependency order then dependency order", ["dependency order"]),
            "[[dependency order]] then dependency order",
        )

    def test_protected_spans_untouched(self):
        source = (
            "use `dependency order` and $dependency order$ and [[dependency order]]\n"
            "and [dependency order](x.md)\n\n```\ndependency order\n```"
        )
        self.assertEqual(wikify(source, ["dependency order"]), source)

    def test_chinese_overlap(self):
        self.assertEqual(
            wikify("先读几何原理和几何", ["几何原理", "几何"]),
            "先读[[几何原理]]和[[几何]]",
        )

    def test_fence_and_prose_split(self):
        source = "a ```\ndependency order\n``` and dependency order"
        self.assertEqual(
            wikify(source, ["dependency order"]),
            "a ```\ndependency order\n``` and [[dependency order]]",
        )


if __name__ == "__main__":
    unittest.main()

    unittest.main()

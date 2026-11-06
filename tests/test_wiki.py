import contextlib
from http.client import HTTPConnection
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest

from adva_wiki.config import load_config
from adva_wiki.render import render_markdown
from adva_wiki.revisions import Revisions
from adva_wiki.server import content_path, create_server


class RenderingTests(unittest.TestCase):
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


class WikiTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
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
            self.assertIn(b">First</h1>", self.request(port, f"/wiki/README.md?rev={first}")[2])
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


if __name__ == "__main__":
    unittest.main()

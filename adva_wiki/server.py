from functools import partial
from html import escape
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlsplit

from .backlinks import Backlink, render_with_backlinks
from .config import Config
from .content import content_path, language_href, markdown_files, page_href, split_language_alias
from .render import MetadataError, RenderedPage, UnknownLanguage, parse_page
from .revisions import GitError, Revisions


IMAGES = {
    ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
    ".gif": "image/gif", ".webp": "image/webp", ".avif": "image/avif",
    ".ico": "image/x-icon",
}
STATIC = Path(__file__).parent / "static"


def language_nav(root: Path, name: str, rendered: RenderedPage, revision: str | None) -> str:
    if len(rendered.languages) < 2:
        return ""
    links = []
    for language in rendered.languages:
        href = language_href(root, name, language.code, rendered.default)
        if revision:
            href += ("&" if "?" in href else "?") + "rev=" + quote(revision, safe="")
        current = ' aria-current="page"' if language.code == rendered.language else ""
        links.append(
            f'<a href="{escape(href)}" hreflang="{escape(language.code)}" '
            f'lang="{escape(language.code)}"{current}>{escape(language.title)}</a>'
        )
    return '<nav class="language-nav" aria-label="Page languages">' + "".join(links) + "</nav>"


def backlinks_section(backlinks: list[Backlink]) -> str:
    if not backlinks:
        return ""
    rows = []
    for backlink in backlinks:
        label = backlink.title
        if backlink.heading and backlink.heading != label:
            label += " · " + backlink.heading
        rows.append(f'<li><a href="{escape(backlink.href)}">{escape(label)}</a></li>')
    return '<section class="backlinks"><h2>Backlinks</h2><ul>' + "".join(rows) + "</ul></section>"


def layout(title: str, body: str, wiki_title: str, lang: str = "en") -> str:
    return f"""<!doctype html>
<html lang="{escape(lang)}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} — {escape(wiki_title)}</title>
<link rel="stylesheet" href="/static/wiki.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.js"></script>
<script defer src="/static/wiki.js"></script>
</head><body><nav><a href="/wiki/README.md">{escape(wiki_title)}</a>
 · <a href="/pages">All pages</a></nav><main>{body}</main></body></html>"""


class WikiHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, config: Config, **kwargs):
        self.config = config
        super().__init__(*args, **kwargs)

    def respond(self, status: int, body: str | bytes, content_type="text/html; charset=utf-8"):
        payload = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", (
            "default-src 'none'; script-src 'self' https://cdn.jsdelivr.net; "
            "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
            "font-src https://cdn.jsdelivr.net; img-src 'self' https: http:; "
            "base-uri 'none'; frame-ancestors 'none'; form-action 'none'"
        ))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(payload)

    def page(self, title: str, body: str, status=200, lang="en"):
        self.respond(status, layout(title, body, self.config.title, lang))

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        try:
            self.route()
        except UnknownLanguage:
            self.page("Language not found", "<h1>Language not found</h1>", 404)
        except MetadataError as error:
            self.page(
                "Invalid page metadata",
                "<h1>Invalid page metadata</h1><p>" + escape(str(error)) + "</p>",
                500,
            )
        except (ValueError, UnicodeError):
            self.page("Bad request", "<h1>Invalid path or revision</h1>", 400)
        except (FileNotFoundError, IsADirectoryError, NotADirectoryError):
            self.page("Not found", "<h1>Page not found</h1>", 404)
        except GitError:
            self.page("History unavailable", "<h1>Git revision not found or history unavailable</h1>", 404)
        except OSError:
            self.page("Unavailable", "<h1>Unable to read content</h1>", 500)

    def route(self):
        root = self.config.content_dir
        url = urlsplit(self.path)
        path = unquote(url.path, errors="strict")
        query = parse_qs(url.query)
        if path == "/":
            self.send_response(302)
            self.send_header("Location", "/wiki/README.md")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        if path in {"/static/wiki.css", "/static/wiki.js"}:
            mime = "text/css" if path.endswith(".css") else "text/javascript"
            self.respond(200, (STATIC / path.rsplit("/", 1)[1]).read_bytes(), mime)
            return
        if path == "/pages":
            links = [
                f'<li><a href="{page_href(name)}">{escape(name[:-3])}</a></li>'
                for name, _ in markdown_files(root)
            ]
            self.page("All pages", "<h1>All pages</h1><ul>" + "".join(links) + "</ul>")
            return
        if not path.startswith("/wiki/"):
            raise FileNotFoundError
        requested_name = path.removeprefix("/wiki/") or "README.md"
        name, alias_language = split_language_alias(root, requested_name)
        requested_language = alias_language or (query.get("lang", [None])[0] or None)
        file = content_path(root, name)
        if file.suffix.lower() in IMAGES:
            self.respond(200, file.read_bytes(), IMAGES[file.suffix.lower()])
            return
        if file.suffix != ".md":
            raise FileNotFoundError
        revisions = Revisions(root)
        name = file.relative_to(root).as_posix()
        view_url = page_href(requested_name)
        if alias_language is None and "lang" in query and requested_language:
            view_url += "?lang=" + quote(requested_language, safe="")
        title = name[:-3]
        if "history" in query:
            rows = []
            for item in revisions.history(file):
                sha = item["sha"]
                separator = "&" if "?" in view_url else "?"
                rows.append(
                    f'<li><a href="{view_url}{separator}rev={sha}">{sha[:10]}</a> '
                    f'{escape(item["date"])} — {escape(item["author"])}: '
                    f'{escape(item["subject"])} '
                    f'<a href="{view_url}{separator}diff={sha}">diff</a></li>'
                )
            self.page(title, "<h1>Revision history</h1><ul>" + "".join(rows) + "</ul>"
                      + ("" if rows else "<p>No committed revisions yet.</p>"))
            return
        if "diff" in query:
            diff = revisions.diff(file, query["diff"][0])
            self.page(title, "<h1>Revision diff</h1><pre>" + escape(diff) + "</pre>")
            return
        revision = query.get("rev", [None])[0]
        source = revisions.read(file, revision) if revision else file.read_text(encoding="utf-8")
        parsed = parse_page(source)
        fallback = False
        backlinks = []
        if revision is None:
            rendered, backlinks = render_with_backlinks(root, name, parsed, requested_language)
        else:
            try:
                rendered = parsed.render(requested_language)
            except UnknownLanguage:
                rendered = parsed.render()
                fallback = True
        title = rendered.title or title
        separator = "&" if "?" in view_url else "?"
        toolbar = f'<p><a href="{view_url}{separator}history=1">Revision history</a>'
        if revision:
            toolbar += f' · Revision {escape(revision[:10])} · <a href="{view_url}">Current page</a>'
        body = language_nav(root, name, rendered, revision) + toolbar + "</p>" + rendered.html
        body += backlinks_section(backlinks)
        if fallback:
            body += (
                '<p class="note">Language <code>' + escape(requested_language or "")
                + "</code> is not available in this revision; showing the default language.</p>"
            )
        self.page(title, body, lang=rendered.language or "en")


def create_server(config: Config) -> ThreadingHTTPServer:
    return ThreadingHTTPServer(
        (config.host, config.port), partial(WikiHandler, config=config),
    )

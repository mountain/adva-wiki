from dataclasses import dataclass
from html import escape
import re
from urllib.parse import quote

from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.dollarmath import dollarmath_plugin
from mdit_py_plugins.tasklists import tasklists_plugin


LANGUAGE_CODE = re.compile(r"[A-Za-z]{2,8}(?:[-_][A-Za-z0-9]{1,8})*")
FRONT_MATTER = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.DOTALL)


class MetadataError(ValueError):
    """The language metadata at the top of a page is malformed."""


class UnknownLanguage(ValueError):
    """A requested language is not declared by the page."""


@dataclass(frozen=True)
class Language:
    code: str
    title: str


@dataclass(frozen=True)
class RenderedPage:
    html: str
    languages: tuple[Language, ...] = ()
    language: str | None = None
    default: str | None = None
    title: str | None = None


def wiki_link(state, silent):
    start = state.pos
    if state.linkLevel or not state.src.startswith("[[", start):
        return False
    end = state.src.find("]]", start + 2, state.posMax)
    if end == -1:
        return False
    target, separator, label = state.src[start + 2:end].partition("|")
    target = target.strip()
    if not target or "\n" in target:
        return False
    page, fragment_separator, fragment = target.partition("#")
    if page and not page.endswith(".md"):
        page += ".md"
    href = "/wiki/" + quote(page.lstrip("/"), safe="/") if page else ""
    if fragment_separator:
        href += "#" + quote(fragment, safe="")
    if not silent:
        token = state.push("link_open", "a", 1)
        token.attrSet("href", href)
        token = state.push("text", "", 0)
        token.content = label.strip() if separator else target
        state.push("link_close", "a", -1)
    state.pos = end + 2
    return True


def markdown_renderer() -> MarkdownIt:
    md = (
        MarkdownIt("gfm-like", {"html": False})
        .use(tasklists_plugin)
        .use(dollarmath_plugin)
        .use(anchors_plugin, min_level=1, max_level=6)
    )
    md.inline.ruler.before("link", "wiki_link", wiki_link)
    default_fence = md.renderer.rules["fence"]

    def fence(tokens, index, options, env):
        token = tokens[index]
        if token.info.strip() in {"math", "latex"}:
            return f'<div class="math block">{escape(token.content)}</div>\n'
        return default_fence(tokens, index, options, env)

    md.renderer.rules["fence"] = fence
    return md


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def _parse_meta(header: str) -> tuple[dict[str, str], str | None]:
    languages: dict[str, str] = {}
    default: str | None = None
    in_languages = False
    for raw_line in header.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if not raw_line[0].isspace():
            key, separator, value = line.partition(":")
            key = _unquote(key)
            value = _unquote(value)
            if key == "languages":
                if value:
                    raise MetadataError("languages must be a mapping of language codes to H1 titles")
                in_languages = True
            elif key == "default":
                default = value
                in_languages = False
            else:
                in_languages = False
            continue
        if not in_languages:
            continue
        code, separator, title = line.partition(":")
        if not separator:
            raise MetadataError(f"Invalid language entry: {line!r}")
        code = _unquote(code)
        title = _unquote(title)
        if not LANGUAGE_CODE.fullmatch(code):
            raise MetadataError(f"Invalid language code: {code!r}")
        if code in {"default", "languages"}:
            raise MetadataError(f"Reserved language code: {code!r}")
        if not title:
            raise MetadataError(f"Language {code!r} needs an H1 title")
        if code in languages:
            raise MetadataError(f"Duplicate language code: {code!r}")
        languages[code] = title
    if not languages:
        return {}, None
    if default is not None and default not in languages:
        raise MetadataError(f"Default language {default!r} is not declared")
    return languages, default


def parse_languages(source: str) -> tuple[dict[str, str], str | None, str]:
    """Return (language -> H1 title, default language, Markdown body).

    A front-matter block is only treated as language metadata when it declares
    a ``languages`` mapping; otherwise the source is returned unchanged.
    """
    if source.startswith("\ufeff"):
        source = source[1:]
    match = FRONT_MATTER.match(source)
    if not match:
        return {}, None, source
    header = match.group(1)
    if not re.search(r"(?m)^languages\s*:", header):
        return {}, None, source
    languages, default = _parse_meta(header)
    if not languages:
        raise MetadataError("A languages mapping must declare at least one language")
    return languages, default, source[match.end():]


def _normalize_title(title: str) -> str:
    return " ".join(title.split())


def _split_sections(tokens) -> tuple[list, list[tuple[str, list]]]:
    preamble: list = []
    sections: list[tuple[str, list]] = []
    current: list | None = None
    for token in tokens:
        if token.type == "heading_open" and token.tag == "h1":
            if current is None:
                current = []
            else:
                sections.append(current)
                current = []
        if current is None:
            preamble.append(token)
        else:
            current.append(token)
    if current is not None:
        sections.append(current)

    titled: list[tuple[str, list]] = []
    for section in sections:
        title = ""
        for index, token in enumerate(section):
            if token.type == "heading_open" and token.tag == "h1":
                if index + 1 < len(section) and section[index + 1].type == "inline":
                    title = section[index + 1].content
                break
        titled.append((title, section))
    return preamble, titled


def render_page(source: str, language: str | None = None) -> RenderedPage:
    """Render a page, selecting one language section when metadata is present."""
    languages, default, body = parse_languages(source)
    if not languages:
        if language is not None:
            raise UnknownLanguage(f"Page does not declare language {language!r}")
        return RenderedPage(markdown_renderer().render(body))

    if language is None:
        language = default or next(iter(languages))
    if language not in languages:
        raise UnknownLanguage(f"Page does not declare language {language!r}")

    normalized = {code: _normalize_title(title) for code, title in languages.items()}
    if len(set(normalized.values())) != len(normalized):
        raise MetadataError("Each language must point at a distinct H1 title")

    md = markdown_renderer()
    env: dict = {}
    tokens = md.parse(body, env)
    preamble, sections = _split_sections(tokens)
    selected: dict[str, list] = {code: [] for code in languages}
    shared: list = []
    for title, section in sections:
        match = next(
            (code for code, expected in normalized.items() if _normalize_title(title) == expected),
            None,
        )
        if match is None:
            shared.extend(section)
        else:
            selected[match].extend(section)

    missing = [code for code, tokens_for_code in selected.items() if not tokens_for_code]
    if missing:
        raise MetadataError(
            "No H1 section matches the declared title for: " + ", ".join(missing)
        )

    ordered = [*preamble, *selected[language], *shared]
    html = md.renderer.render(ordered, md.options, env)
    return RenderedPage(
        html=html,
        languages=tuple(Language(code, title) for code, title in languages.items()),
        language=language,
        default=default or next(iter(languages)),
        title=languages[language],
    )


def render_markdown(source: str) -> str:
    return render_page(source).html

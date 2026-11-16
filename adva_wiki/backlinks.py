from collections import defaultdict
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qs, unquote, urljoin, urlsplit

from markdown_it.token import Token

from .autolinks import Concepts, add_concept_links, term_pattern
from .content import content_path, language_href, markdown_files, split_language_alias
from .render import MetadataError, ParsedPage, RenderedPage, heading_text, parse_page


PageKey = tuple[str, str | None]


@dataclass(frozen=True)
class Backlink:
    href: str
    title: str
    heading: str | None


def _references(tokens: list[Token]) -> Iterator[tuple[str, str, str | None]]:
    heading = None
    for position, block in enumerate(tokens):
        if block.type == "heading_open":
            heading = heading_text(tokens[position + 1]) or None
        for token in block.children or ():
            if token.type == "link_open":
                href, anchor = token.attrGet("href"), token.attrGet("id")
                if isinstance(href, str) and isinstance(anchor, str):
                    yield href, anchor, heading


def _target(
    root: Path, source_url: str, href: str, pages: dict[str, ParsedPage],
) -> tuple[PageKey, str] | None:
    try:
        url = urlsplit(urljoin(source_url, href))
        if url.scheme or url.netloc:
            return None
        path = unquote(url.path, errors="strict")
        query = parse_qs(url.query)
        if path == "/":
            path, query = "/wiki/README.md", {}
        if not path.startswith("/wiki/") or query.keys() & {"history", "rev", "diff"}:
            return None
        name = path.removeprefix("/wiki/") or "README.md"
        name, alias = split_language_alias(root, name)
        name = content_path(root, name).relative_to(root).as_posix()
        if name not in pages:
            return None
        language = alias or query.get("lang", [None])[0] or pages[name].default
        return (name, language), unquote(url.fragment, errors="strict")
    except (OSError, ValueError):
        return None


def _first_references(
    root: Path, pages: dict[str, ParsedPage], headings: dict[PageKey, set[str]],
    source_key: PageKey, source_url: str, tokens: list[Token],
) -> dict[PageKey, tuple[str, str | None]]:
    references: dict[PageKey, tuple[str, str | None]] = {}
    for href, anchor, heading in _references(tokens):
        target = _target(root, source_url, href, pages)
        if target is None:
            continue
        key, fragment = target
        if key == source_key or key not in headings:
            continue
        if fragment and fragment not in headings[key]:
            continue
        references.setdefault(key, (anchor, heading))
    return references


def render_with_backlinks(
    root: Path, current_name: str, current: ParsedPage, requested_language: str | None,
) -> tuple[RenderedPage, list[Backlink]]:
    """Use the same current page views to render both directions of each link."""
    current_language = current.view_language(requested_language)
    current_key = (current_name, current_language)
    current_tokens = current.views[current_language]
    pages = {current_name: current}
    for name, file in markdown_files(root):
        if name == current_name:
            continue
        try:
            pages[name] = parse_page(file.read_text(encoding="utf-8"), current.markdown)
        except (OSError, UnicodeError, MetadataError):
            continue

    headings: dict[PageKey, set[str]] = {}
    urls: dict[PageKey, str] = {}
    concepts: Concepts = {}
    for name, page in sorted(pages.items()):
        for language, tokens in page.views.items():
            key = (name, language)
            url = language_href(root, name, language, page.default)
            urls[key] = url
            headings[key] = {
                anchor for token in tokens if token.type == "heading_open"
                if isinstance(anchor := token.attrGet("id"), str)
            }
            title = next((
                heading_text(tokens[index + 1]) for index, token in enumerate(tokens)
                if token.type == "heading_open" and token.tag == "h1"
            ), "")
            if title:
                concepts[title] = None if title in concepts else (name, url)

    pattern = term_pattern(concepts)
    inbound: dict[PageKey, list[Backlink]] = defaultdict(list)
    for source_key, source_url in urls.items():
        name, language = source_key
        page = pages[name]
        tokens = page.views[language]
        title = page.titles[language] if language is not None else name[:-3]
        references = _first_references(root, pages, headings, source_key, source_url, tokens)
        if pattern is not None:
            linked = {target_name for target_name, _ in references}
            linked.add(name)
            linked_tokens = add_concept_links(tokens, pattern, concepts, linked)
            if linked_tokens is not tokens:
                tokens = linked_tokens
                references = _first_references(root, pages, headings, source_key, source_url, tokens)
        if source_key == current_key:
            current_tokens = tokens
        for target_key, (anchor, heading) in references.items():
            inbound[target_key].append(Backlink(f"{source_url}#{anchor}", title, heading))
    return current.render(current_language, tokens=current_tokens), inbound[current_key]

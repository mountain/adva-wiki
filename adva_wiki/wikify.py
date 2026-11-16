"""Source-level wikification: insert ``[[phrase]]`` wiki links into Markdown prose.

This is the cheap "direct text replacement" counterpart to the render-time
concept links in :mod:`adva_wiki.autolinks`.  It rewrites the Markdown *source*
(``dependency order`` -> ``[[dependency order]]``) so the result can be saved and
served by the existing ``[[...]]`` wiki-link rule.

Design points
-------------
* Longest-first matching resolves overlap: if both ``basic hyperbolic model``
  and ``hyperbolic model`` are in the table, the longer phrase wins first.
* Code fences, inline code, math, and existing links are left untouched.
* By default only the *first* mention of each phrase is linked (Wikipedia style);
  pass ``link_all=True`` to link every eligible mention.
"""

from collections.abc import Iterable
import re

from .autolinks import term_pattern


# A phrase longer than this many characters is almost never a concept; skip it so
# path-like fragments ("check path library root") do not pollute the matcher.
_MAX_PHRASE_LENGTH = 48


def _protected_regex() -> re.Pattern[str]:
    """One regex that matches every span that must not be wikified."""
    fence = r"(?ms:^[ \t]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ \t]{0,3}\1[ \t]*$)"
    inline_code = r"(?s:`+[^`]*?`+)"
    display_math = r"(?s:\$\$.*?\$\$)"
    inline_math = r"(?<!\\)\$[^$\n]+?\$(?!\$)"
    wiki_link = r"\[\[[^\]]*\]\]"
    md_link = r"(?s:\[[^\]]*\]\([^)]*\))"
    autolink = r"<[A-Za-z][^>\n]*>"
    html = r"(?s:<!--.*?-->|</?[A-Za-z][^>]*>)"
    return re.compile(
        "|".join((fence, inline_code, display_math, inline_math, wiki_link, md_link, autolink, html))
    )


_PROTECTED = _protected_regex()


def _walk_prose(source: str):
    """Yield ``(is_prose, text)`` chunks of the source."""
    position = 0
    for match in _PROTECTED.finditer(source):
        if match.start() > position:
            yield True, source[position:match.start()]
        yield False, match.group()
        position = match.end()
    if position < len(source):
        yield True, source[position:]


def wikify(
    source: str,
    phrases: Iterable[str],
    *,
    link_all: bool = False,
) -> str:
    """Insert ``[[phrase]]`` wiki links for concept phrases.

    ``phrases`` is any iterable of concept phrases (the wikify table).  Matching
    is longest-first, so overlapping phrases are resolved toward the longer one.
    Protected spans (code, math, links, HTML) are copied through unchanged.

    >>> wikify("the dependency order", ["dependency order"])
    'the [[dependency order]]'
    """
    terms = sorted({p.strip() for p in phrases if p.strip() and len(p.strip()) <= _MAX_PHRASE_LENGTH})
    pattern = term_pattern(terms)
    if pattern is None:
        return source

    linked: set[str] = set()

    def replace(text: str) -> str:
        output: list[str] = []
        position = 0
        for match in pattern.finditer(text):
            phrase = match.group()
            if not link_all and phrase in linked:
                continue
            output.append(text[position:match.start()])
            output.append(f"[[{phrase}]]")
            position = match.end()
            linked.add(phrase)
        output.append(text[position:])
        return "".join(output)

    chunks = []
    for is_prose, text in _walk_prose(source):
        chunks.append(replace(text) if is_prose else text)
    return "".join(chunks)

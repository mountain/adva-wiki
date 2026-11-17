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
from pathlib import Path
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
    skip: Iterable[str] = (),
) -> str:
    """Insert ``[[phrase]]`` wiki links for concept phrases.

    ``phrases`` is any iterable of concept phrases (the wikify table).  Matching
    is longest-first and case-insensitive, so overlapping phrases are resolved
    toward the longer one and ``Flow equation`` links the same concept as
    ``flow equation``; the replacement preserves the original case.

    ``skip`` lists phrases to leave unlinked even if present — pass the page's
    own title(s) there to avoid self-links.

    Protected spans (code, math, links, HTML) are copied through unchanged.

    >>> wikify("the dependency order", ["dependency order"])
    'the [[dependency order]]'
    """
    terms = sorted({p.strip() for p in phrases if p.strip() and len(p.strip()) <= _MAX_PHRASE_LENGTH})
    pattern = term_pattern(terms, case_sensitive=False)
    if pattern is None:
        return source

    skip_lower = {s.strip().lower() for s in skip if s and s.strip()}
    linked: set[str] = set()

    def replace(text: str) -> str:
        output: list[str] = []
        position = 0
        for match in pattern.finditer(text):
            phrase = match.group()
            key = phrase.lower()
            if key in skip_lower:
                continue
            if not link_all and key in linked:
                continue
            output.append(text[position:match.start()])
            output.append(f"[[{phrase}]]")
            position = match.end()
            linked.add(key)
        output.append(text[position:])
        return "".join(output)

    chunks = []
    for is_prose, text in _walk_prose(source):
        chunks.append(replace(text) if is_prose else text)
    return "".join(chunks)


def load_concept_table(path: str | Path) -> list[str]:
    """Read a concept table and return its phrases, longest-first.

    Accepts both table shapes produced by the AEG pipeline:

    * ``wikify-replacement-table.tsv``: ``phrase<TAB>[[phrase]]`` (phrase in
      column 1, link in column 2);
    * ``generic-word-concepts.tsv``: ``word<TAB>phrase<TAB>count<TAB>repos``
      (phrase in column 2).

    Lines starting with ``#`` and the first header row are ignored.  Duplicate
    phrases are collapsed, and phrases longer than :data:`_MAX_PHRASE_LENGTH`
    are dropped.
    """
    phrases: set[str] = set()
    with open(path, encoding="utf-8") as stream:
        first = True
        for line in stream:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            columns = line.split("\t")
            if first:
                first = False
                if columns and columns[0].strip().lower() in {"phrase", "word"}:
                    continue
            if len(columns) >= 2 and columns[1].startswith("[["):
                phrase = columns[0]
            elif len(columns) >= 2:
                phrase = columns[1]
            elif columns:
                phrase = columns[0]
            else:
                continue
            phrase = phrase.strip()
            if phrase and len(phrase) <= _MAX_PHRASE_LENGTH:
                phrases.add(phrase)
    return sorted(phrases, key=lambda p: (-len(p), p))

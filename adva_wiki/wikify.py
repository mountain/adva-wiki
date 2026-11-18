"""Source-level wikification: insert ``[[phrase]]`` wiki links into Markdown prose.

This is the cheap "direct text replacement" counterpart to the render-time
concept links in :mod:`adva_wiki.autolinks`.  It rewrites the Markdown *source*
(``dependency order`` -> ``[[dependency order]]``) so the result can be saved and
served by the existing ``[[...]]`` wiki-link rule.

Design points
-------------
* Longest-first matching resolves overlap: if both ``basic hyperbolic model``
  and ``hyperbolic model`` are in the table, the longer phrase wins first.
* Language metadata, headings, code fences, inline code, math, and existing
  links are left untouched.
* By default only the *first* mention of each phrase is linked (Wikipedia style);
  pass ``link_all=True`` to link every eligible mention.
"""

from collections.abc import Iterable
from pathlib import Path
import re

from .autolinks import term_pattern
from .render import heading_text, markdown_renderer, parse_languages


# A phrase longer than this many characters is almost never a concept; skip it so
# path-like fragments ("check path library root") do not pollute the matcher.
_MAX_PHRASE_LENGTH = 48

_PLURAL_IRREGULAR = {
    "matrix": "matrices", "index": "indices", "vertex": "vertices",
    "analysis": "analyses", "basis": "bases", "criterion": "criteria",
}


def _plural(word: str) -> str:
    """Return the English plural of a (normally singular) word."""
    if word in _PLURAL_IRREGULAR:
        return _PLURAL_IRREGULAR[word]
    if word.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"
    if word.endswith("y") and len(word) > 1 and word[-2] not in "aeiou":
        return word[:-1] + "ies"
    return word + "s"


def _looks_plural(word: str) -> bool:
    """A cheap heuristic: does this word already look plural?"""
    return word.endswith("s") and not word.endswith(("ss", "us", "is"))


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


def _page_structure(source: str) -> tuple[set[str], list[tuple[int, int]]]:
    """Find the page's own titles and source ranges reserved for page structure."""
    languages, _, body = parse_languages(source)
    titles = set(languages.values())
    offset = len(source) - len(body)  # Includes the original BOM and language header.
    protected = [(0, offset)]
    lines = [offset, *(offset + m.end() for m in re.finditer("\n", body)), len(source)]
    declared = {" ".join(title.split()) for title in titles}
    tokens = markdown_renderer().parse(body)
    for index, token in enumerate(tokens):
        if token.type != "heading_open" or token.map is None:
            continue
        start, end = token.map
        protected.append((lines[start], lines[end]))
        if token.tag == "h1":
            inline = tokens[index + 1]
            if not titles or " ".join(inline.content.split()) in declared:
                titles.add(heading_text(inline))
    return titles, protected


def _walk_prose(source: str, protected: list[tuple[int, int]]):
    """Yield ``(is_prose, text)`` chunks of the source."""
    position = 0
    for start, end in [*protected, (len(source), len(source))]:
        for match in _PROTECTED.finditer(source, position, start):
            yield True, source[position:match.start()]
            yield False, match.group()
            position = match.end()
        yield True, source[position:start]
        yield False, source[start:end]
        position = end


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

    Page titles are excluded automatically. Pass additional names (such as
    the wiki path without its extension) in ``skip``.

    Plural forms of each phrase's last word are recognised and link to the
    singular canonical form, e.g. ``arithmetic motions`` becomes
    ``[[arithmetic motion|arithmetic motions]]``.

    Protected spans (code, math, links, HTML) are copied through unchanged.

    >>> wikify("the dependency order", ["dependency order"])
    'the [[dependency order]]'
    """
    terms = sorted({p.strip() for p in phrases if p.strip() and len(p.strip()) <= _MAX_PHRASE_LENGTH})

    # Map each matched form (lowercased) to its canonical phrase.  Besides the
    # exact phrases, register the plural of each phrase's last word so that
    # "arithmetic motions" links to "arithmetic motion" as
    # [[arithmetic motion|arithmetic motions]].
    forms: dict[str, str] = {}
    for phrase in terms:
        forms.setdefault(phrase.lower(), phrase)
        words = phrase.split()
        last = words[-1]
        if not _looks_plural(last):
            plural = _plural(last)
            if plural != last:
                forms.setdefault(" ".join(words[:-1] + [plural]).lower(), phrase)

    pattern = term_pattern(forms.keys(), case_sensitive=False)
    if pattern is None:
        return source

    # Match on the same line breaks as the reader, retaining each original
    # separator for writeback. Wiki links inserted from a TSV are single-line.
    original_lines = re.split(r"(\r\n?|\n)", source) if "\r" in source else None
    if original_lines is not None:
        source = "\n".join(original_lines[::2])
    titles, protected = _page_structure(source)
    titles.update(skip)
    skip_lower = {s.strip().lower() for s in titles if s and s.strip()}
    linked: set[str] = set()

    def replace(text: str) -> str:
        output: list[str] = []
        position = 0
        for match in pattern.finditer(text):
            matched = match.group()
            matched_lower = matched.lower()
            canonical = forms.get(matched_lower)
            if canonical is None:  # IGNORECASE also matches Unicode forms absent from the table.
                continue
            key = canonical.lower()
            if key in skip_lower:
                continue
            if not link_all and key in linked:
                continue
            output.append(text[position:match.start()])
            if canonical != matched_lower:
                output.append(f"[[{canonical}|{matched}]]")
            else:
                output.append(f"[[{matched}]]")
            position = match.end()
            linked.add(key)
        output.append(text[position:])
        return "".join(output)

    chunks = []
    for is_prose, text in _walk_prose(source, protected):
        chunks.append(replace(text) if is_prose else text)
    result = "".join(chunks)
    if original_lines is not None:
        original_lines[::2] = result.split("\n")
        return "".join(original_lines)
    return result


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

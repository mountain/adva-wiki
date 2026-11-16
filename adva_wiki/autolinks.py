from collections import defaultdict
from collections.abc import Iterable
from dataclasses import replace
import re

from markdown_it.token import Token


Concepts = dict[str, tuple[str, str] | None]
WORD_CHARACTER = r"[A-Za-z0-9_]"


def term_pattern(terms: Iterable[str]) -> re.Pattern[str] | None:
    choices = []
    for term in sorted(terms, key=lambda term: (-len(term), term)):
        pattern = re.escape(term)
        if re.fullmatch(WORD_CHARACTER, term[0]):
            pattern = rf"(?<!{WORD_CHARACTER})" + pattern
        if re.fullmatch(WORD_CHARACTER, term[-1]):
            pattern += rf"(?!{WORD_CHARACTER})"
        choices.append(pattern)
    return re.compile("|".join(choices)) if choices else None


def _inline_text(tokens: list[Token]) -> tuple[str, list[tuple[int, int, int]]]:
    parts = []
    spans = []
    position = 0
    link_depth = 0
    for index, token in enumerate(tokens):
        if token.type == "link_open":
            link_depth += 1
        elif token.type == "link_close":
            link_depth -= 1
        elif token.type in {"text", "code_inline"}:
            end = position + len(token.content)
            if token.type == "text" and not link_depth and end > position:
                spans.append((position, end, index))
            parts.append(token.content)
            position = end
        elif token.type in {"softbreak", "hardbreak", "image", "html_inline", "math_inline", "math_inline_double"}:
            parts.append("\n")
            position += 1
    return "".join(parts), spans


def add_concept_links(
    tokens: list[Token], pattern: re.Pattern[str], concepts: Concepts, linked: set[str],
) -> list[Token]:
    """Link the first eligible mention of each concept in this language view."""
    result = tokens
    number = 0
    for position, block in enumerate(tokens):
        if block.type != "inline" or not block.children:
            continue
        if position and tokens[position - 1].type == "heading_open":
            continue
        text, spans = _inline_text(block.children)
        eligible = iter(spans)
        span = next(eligible, None)
        matches: dict[int, list[tuple[int, int, str]]] = defaultdict(list)
        for match in pattern.finditer(text):
            while span is not None and match.start() >= span[1]:
                span = next(eligible, None)
            if span is None:
                break
            start, end, index = span
            # A match crossing markup or an existing link still occupies its full name.
            if match.start() < start or match.end() > end:
                continue
            target = concepts[match.group()]
            if target is not None and target[0] not in linked:
                name, href = target
                linked.add(name)
                matches[index].append((match.start() - start, match.end() - start, href))
        if not matches:
            continue

        children = []
        for index, token in enumerate(block.children):
            if index not in matches:
                children.append(token)
                continue
            start = 0
            for left, right, href in matches[index]:
                if left > start:
                    children.append(replace(token, content=token.content[start:left]))
                number += 1
                children.append(Token("link_open", "a", 1, attrs={
                    "id": f"wiki-ref:auto-{number}", "href": href,
                }))
                children.append(replace(token, content=token.content[left:right]))
                children.append(Token("link_close", "a", -1))
                start = right
            if start < len(token.content):
                children.append(replace(token, content=token.content[start:]))
        if result is tokens:
            result = tokens.copy()
        result[position] = replace(block, children=children)
    return result

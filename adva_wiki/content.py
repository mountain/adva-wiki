from collections.abc import Iterator
import os
from pathlib import Path, PurePosixPath
from urllib.parse import quote

from .render import LANGUAGE_CODE


def content_path(root: Path, name: str) -> Path:
    parts = PurePosixPath(name).parts
    if not parts or name.startswith("/") or "\\" in name:
        raise ValueError("Invalid content path")
    if any(part.startswith(".") for part in parts):
        raise ValueError("Hidden paths and parent traversal are not allowed")
    path = root.joinpath(*parts)
    if any(parent.is_symlink() for parent in (path, *path.parents) if parent != root):
        raise ValueError("Symlinks are not served")
    if not path.resolve().is_relative_to(root):
        raise ValueError("Content must remain inside the wiki directory")
    return path


def split_language_alias(root: Path, name: str) -> tuple[str, str | None]:
    """Map ``page.zh.md`` to ``page.md`` plus language ``zh`` if no such file exists."""
    if not name.endswith(".md"):
        return name, None
    stem = name[:-3]
    base, separator, code = stem.rpartition(".")
    if not separator or not base or not LANGUAGE_CODE.fullmatch(code):
        return name, None
    if content_path(root, name).exists():
        return name, None
    base_name = base + ".md"
    if not content_path(root, base_name).is_file():
        return name, None
    return base_name, code


def markdown_files(root: Path) -> Iterator[tuple[str, Path]]:
    for directory, dirs, files in os.walk(root):
        folder = Path(directory)
        dirs[:] = sorted(
            name for name in dirs
            if not name.startswith(".") and not (folder / name).is_symlink()
        )
        for filename in sorted(files):
            if not filename.endswith(".md"):
                continue
            name = (folder / filename).relative_to(root).as_posix()
            try:
                file = content_path(root, name)
                if file.is_file():
                    yield name, file
            except (OSError, ValueError):
                continue


def page_href(name: str) -> str:
    return "/wiki/" + quote(name)


def language_href(root: Path, name: str, code: str | None, default: str | None) -> str:
    href = page_href(name)
    if code is None or code == default:
        return href
    alias = name[:-3] + "." + code + ".md"
    try:
        if split_language_alias(root, alias) == (name, code):
            return page_href(alias)
    except (OSError, ValueError):
        pass
    return href + "?lang=" + quote(code, safe="")

from dataclasses import dataclass
from pathlib import Path
import tomllib
from urllib.parse import urlsplit


@dataclass(frozen=True)
class Config:
    content_dir: Path
    title: str
    host: str
    port: int
    projects: tuple[dict, ...]
    feeds: tuple[dict, ...]


def load_config(path: Path) -> Config:
    path = path.resolve()
    with path.open("rb") as stream:
        data = tomllib.load(stream)
    wiki = data.get("wiki", {})
    server = data.get("server", {})
    content = (path.parent / wiki.get("content_dir", ".")).resolve()
    title = wiki.get("title", "adva-wiki")
    host = server.get("host", "127.0.0.1")
    port = server.get("port", 8000)
    if not isinstance(title, str) or not isinstance(host, str):
        raise ValueError("Wiki title and server host must be strings")
    if type(port) is not int or not 0 <= port <= 65535:
        raise ValueError("Server port must be between 0 and 65535")
    if not content.is_dir():
        raise ValueError(f"Content directory does not exist: {content}")
    projects = []
    for project in data.get("projects", []):
        if not isinstance(project.get("name"), str) or not isinstance(project.get("path"), str):
            raise ValueError("Each project requires a name and path")
        projects.append({
            "name": project["name"],
            "path": str((path.parent / project["path"]).resolve()),
        })
    feeds = []
    for feed in data.get("feeds", []):
        if not isinstance(feed.get("name"), str) or not isinstance(feed.get("url"), str):
            raise ValueError("Each feed requires a name and URL")
        url = urlsplit(feed["url"])
        if url.scheme not in {"http", "https"} or not url.hostname or url.username or url.password:
            raise ValueError("Feed URLs must be HTTP(S) URLs without credentials")
        feeds.append({"name": feed["name"], "url": feed["url"]})
    return Config(content, title, host, port, tuple(projects), tuple(feeds))

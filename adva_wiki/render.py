from html import escape
from urllib.parse import quote

from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.dollarmath import dollarmath_plugin
from mdit_py_plugins.tasklists import tasklists_plugin


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


def render_markdown(source: str) -> str:
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
    return md.render(source)

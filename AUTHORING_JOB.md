# adva-wiki 自动撰写作业

每 3 小时由定时任务触发一次，每次完成一篇双语词条。本文件是撰写作业的自包含说明，
供定时任务调起的 AI 会话照此执行。

## 数据文件

- 任务单：`tasks.json`（`[{en, word, zh, priority}]`，已按优先级升序）。
- 进度：`state.json`（`{done, pending, current, last_run}`，gitignored，仅落盘）。
- 大词表（wikify 用）：`/Users/mingli/AEG/wikify-replacement-table.tsv`。

## 执行步骤（一次一篇）

### 1. 读任务与状态

```sh
cd /Users/mingli/AEG/adva-wiki
python3 -c "import json; s=json.load(open('state.json')); print(s['pending'][0])"
```

取 `state.json` 里 `pending` 的第一个英文名（如 `process history`），并从 `tasks.json`
查出它的中文名（如 `过程历史`）。

若 `pending` 为空：所有任务完成，本词条无需撰写，直接退出（不提交、不推送）。

### 2. 撰写双语词条

写文件 `<英文名>.md`（保留空格，放在仓库根目录），格式参照 `torsor.md`：

```markdown
---
languages:
  en: <英文名>
  zh: <中文名>
default: en
---

# <英文名>

英文正文：数学概念的定义与说明，准确克制，可含 LaTeX 与 [[其它概念]] 链接。

# <中文名>

中文正文。
```

要点：

- 正文以 paper-0 的权威定义为准，保持「定义 / 命题 / 猜想 / 开放问题」的区分，
  不把猜想写成定理、不把类比写成等价。
- 可主动写 `[[依赖偏序]]` 这类 wiki 链接（wikify 步骤会补全漏掉的名词）。
- 篇幅以「说清概念」为度，不强求长度。

### 3. wikify 源级替换

对刚写的文件做源级替换（跳过自身标题，避免自链接；大小写不敏感、替换保留原文大小写）：

```sh
cd /Users/mingli/AEG/adva-wiki
UV_CACHE_DIR=/Users/mingli/AEG/.uv-cache uv run python - <<'PY'
from pathlib import Path
from adva_wiki.wikify import load_concept_table, wikify
name = "<英文名>"          # 本次概念英文名，如 "flow equation"
zh   = "<中文名>"          # 本次概念中文名，如 "流方程"
path = Path(name + ".md")
phrases = load_concept_table('/Users/mingli/AEG/wikify-replacement-table.tsv')
path.write_text(wikify(path.read_text(encoding='utf-8'), phrases, skip=[name, zh]),
                encoding='utf-8')
PY
```

批量处理时，先用 `python -m adva_wiki wikify --config wiki.toml --table /Users/mingli/AEG/wikify-replacement-table.tsv --diff` 查看逐行差异。确认后将 `--diff` 换为 `--write` 写入。

每次运行只给每个词条的首个可替换位置加链接。已有链接会原样保留，重跑时同一词条在后文的另一次出现仍可能被加链。

### 4. 提交并推送（直接推 main）

```sh
cd /Users/mingli/AEG/adva-wiki
git add "<英文名>.md"
git commit -m "add <英文名>"
git push origin main
```

推送失败（如 main 前进）时：`git pull --rebase origin main` 后重推；仍失败则本次放弃，
不更新 `state.json`（下次调度重试）。

### 5. 更新状态

```sh
cd /Users/mingli/AEG/adva-wiki
python3 - <<'PY'
import json, datetime
s = json.load(open('state.json'))
name = s['pending'].pop(0)
s['done'].append(name)
s['current'] = None
s['last_run'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
json.dump(s, open('state.json','w'), ensure_ascii=False, indent=2)
PY
```

## 恢复语义

- `state.json` 落盘即持久：调度重启后，下次运行读它，从下一个 `pending` 继续，不重写已完成。
- 若某步失败且未更新 `state.json`，当前概念仍在 `pending`，下次重试。
- 若提交成功但状态更新前崩溃：下次会把同一概念再写一遍（幂等性差）——为降低重复概率，
  **先 push 成功再更新 state**；确需更严时可在 commit message 里带概念名做去重判断。

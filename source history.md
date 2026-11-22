---
languages:
  en: Source history
  zh: 源历史
default: en
---

# Source history

**Source history** is the history of the sources of a program — the source
objects with their own identifiers — as distinct from the [[occurrence history]]
of their uses.  Information is carried by source, occurrence, and history, never
by value, and several distinct occurrences may retain the same source; source
history is correspondingly coarser than occurrence history.

Source and occurrence identifiers must be explicit and stable under
serialization, and a source history is retained separately from the values, the
costs, and the residual.  Composition and [[transport]] must preserve source
history, together with the finer occurrence history.

# 源历史

**源历史**是程序各源的历史——各带自身标识的源对象——区别于其使用的出现历史。信息由源、出现与
历史承载，绝不只由值承载，多个不同出现可保留同一源；源历史相应地比出现历史更粗。

源与出现标识必须显式且在序列化下稳定，源历史与值、成本、残差分开保留。复合与传输必须保留源
历史，连同更细的出现历史。

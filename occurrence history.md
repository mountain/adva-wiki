---
languages:
  en: Occurrence history
  zh: 出现历史
default: en
---

# Occurrence history

**Occurrence history** is the ordered record of the occurrences of a program —
each distinct use of a source, carrying its own occurrence identifier — as
distinct from the [[source history]] (the sources) and the [[process history]] (the
process).  Several distinct occurrences may retain the same source, so occurrence
history is finer than source history.

Each initial occurrence must be allocated exactly once, and an unknown, missing,
or repeated occurrence fails; reuse proceeds by fresh occurrence bindings, with
no implicit sharing or collapse of history.  The [[occurrence order]] is part of
the [[retained history]], which must be preserved across [[transport]] and
normalization.

# 出现历史

**出现历史**是程序各出现的有序记录——源的每一次不同使用，各带其出现标识——区别于源历史（源）与
过程历史（过程）。多个不同出现可保留同一源，故出现历史比源历史更细。

每个初始出现必须恰好分配一次，未知、缺失或重复的出现都失败；复用经全新出现绑定进行，无隐式
共享或历史坍缩。出现序是保留历史的一部分，必须在传输与归一化中保留。

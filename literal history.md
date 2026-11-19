---
languages:
  en: Literal history
  zh: 字面历史
default: en
---

# Literal history

A **literal history** is the raw, uninterpreted word of primitive operations
$h=X_{i_1}\cdots X_{i_n}$: the process as it literally happened, before any
semantic interpretation, relation, or compression.  Its unweighted depth is its
length $d(h)=n$, and with caller-declared primitive costs $c(X_i)\ge0$ its
weighted depth is $d_c(h)=\sum_j c(X_{i_j})$; this is process depth, not
physical clock time.

In the process layer, a [[process history]] is stored as a literal word
(`ProcessWord`) with no built-in physical interpretation, and a separate
interpretation step supplies caller-defined finite semantics.  The literal
history is the base layer: exact relations, task sufficiency, [[history geometry]],
and presentation search all act on it or on derived objects.

# 字面历史

**字面历史**是原始运算的字面词 $h=X_{i_1}\cdots X_{i_n}$：过程如字面发生的那样，在任何语义
解释、关系或压缩之前。其无权重深度即其长度 $d(h)=n$，而带调用方声明的原始成本
$c(X_i)\ge0$ 时，其有权重深度为 $d_c(h)=\sum_j c(X_{i_j})$；这是过程深度，而非物理时钟时间。

在过程层，过程历史以字面词（`ProcessWord`）存储，无内置物理解释，另由解释步骤提供调用方
声明的有限语义。字面历史是底层：精确关系、任务充分性、历史几何与展示搜索都在它或其派生对象
上作用。

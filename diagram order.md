---
languages:
  en: Diagram order
  zh: 图表序
default: en
---

# Diagram order

The **diagram order** is the [[original diagram order]] — the order of events or
nodes in a checked program diagram.  Slice composition uses the original diagram
order, not the slice concatenation order; two adjacent event vectors need not
concatenate into diagram order, so they are canonically reordered.

The diagram order is distinct from the [[event order]], the [[composition order]],
and the [[schedule order]]; it is the [[canonical order]] of the checked diagram,
from which slices rebuild the outer view.

# 图表序

**图表序**是原始图序——经检验程序图中事件或节点的次序。切片复合使用原始图序而非切片拼接序；两个
相邻事件向量不必拼接成图序，故被规范重排。

图序区别于事件序、复合序与调度序；它是经检验图的规范序，切片从中重建外视图。

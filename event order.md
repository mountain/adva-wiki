---
languages:
  en: Event order
  zh: 事件序
default: en
---

# Event order

The **event order** of a checked program diagram $D$ is the temporal partial
order on its operation nodes: for events $e,f\in E_D$, write $e\preceq_D f$ when
a directed wire path runs from $e$ to $f$ (including equality).  Acyclic
validation makes this a finite [[partial order]]; it is the temporal reading, in
which an event can occur only after its causal predecessors.

No scalar evaluation is used to construct it, and two programs realizing the
same numerical function may have different event orders.  Its downward-closed
subsets are the completed pasts, an Alexandrov topology, and the event order is
recovered from them.  The event order is one of several dependency-flavoured
partial orders in the series, alongside the [[causal order]], the [[temporal order]],
the [[occurrence order]], and the [[dependency order]].

# 事件序

经检验程序图 $D$ 的**事件序**是其运算节点上的时间偏序：对事件 $e,f\in E_D$，当从 $e$ 到 $f$
存在有向线路径（含相等）时记 $e\preceq_D f$。无环校验使之成为有限偏序；它是时间解读——一个
事件只能在其因果前驱之后发生。

构造它不使用标量求值，实现同一数值函数的两个程序可有不同的事件序。其向下封闭子集即完成过去，
构成 Alexandrov 拓扑，事件序可由它们恢复。事件序是系列中若干依赖型偏序之一，与因果序、时间
序、出现序、依赖偏序并列。

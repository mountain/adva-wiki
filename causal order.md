---
languages:
  en: Causal order
  zh: 因果序
default: en
---

# Causal order

The **causal order** of a checked program diagram is the causal-dependence
[[partial order]] on its events: $e\preceq_D f$ when a directed wire path runs from
$e$ to $f$, so $f$ can occur only after its causal predecessor $e$.  It is the
causal reading of the [[event order]], and its downward-closed subsets are the
completed causal pasts (the completed pasts of the Alexandrov topology).

The raw topology remembers causal order, while source sharing is a decoration on
the open frontier.  The program causal order is kept distinct from any physical
causal order, and it is one of several dependency-flavoured partial orders in
the series, alongside the [[temporal order]], the [[occurrence order]], and the
[[dependency order]].

# 因果序

经检验程序图的**因果序**是事件上的因果依赖偏序：当从 $e$ 到 $f$ 存在有向线路径时
$e\preceq_D f$，故 $f$ 只能在其因果前驱 $e$ 之后发生。它是事件序的因果解读，其向下封闭子集即
完成因果过去（Alexandrov 拓扑的完成过去）。

原始拓扑记住因果序，而源共享只是开边界上的装饰。程序因果序与任何物理因果序相互区分，它是
系列中若干依赖型偏序之一，与时间序、出现序、依赖偏序并列。

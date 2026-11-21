---
languages:
  en: Upper cut
  zh: 上切割
default: en
---

# Upper cut

The **upper cut** of a program slice is its upper frontier — the certified set
of wires leaving the slice at the top.  For downward-closed event sets
$U\subseteq V$, the slice $\operatorname{Slice}(P,U,V)$ has [[lower cut]]
$\operatorname{cut}(P,U)$ and upper cut $\operatorname{cut}(P,V)$.

Every upper-cut wire is either produced by an interval event (an event in
$V\setminus U$) or is a through wire, unchanged from the lower cut; an interval
event is internal when none of its produced wires reaches the upper cut.  Equal
lower and upper [[cut frontier|cut frontiers]] do not imply an empty slice, so the
upper cut alone does not determine the slice content.

# 上切割

程序切片的**上切割**是其上前沿——在顶部离开切片的经认证线集。对向下封闭事件集 $U\subseteq V$，
切片 $\operatorname{Slice}(P,U,V)$ 有下切割 $\operatorname{cut}(P,U)$ 与上切割
$\operatorname{cut}(P,V)$。

每条上切割线要么由区间事件（$V\setminus U$ 中的事件）产生，要么是自下切割不变的通线；区间事件
当其任何产出线都不到达上切割时为内部事件。相等的下/上切割前沿不蕴含空切片，故上切割单独不
决定切片内容。

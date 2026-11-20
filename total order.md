---
languages:
  en: Total order
  zh: 全序
default: en
---

# Total order

A **total order** (linear order) on a set $P$ is a [[partial order]] in which
every two elements are comparable: for all $x,y\in P$, either $x\le y$ or
$y\le x$.  A chain is a totally ordered subset, and a linear extension of a
poset is a total order extending it; a finite poset has a unique linear
extension if and only if it is already a total order (a chain).

In the AEG series the total order is the sequential case: the [[chronological order]]
$1,2,\ldots,n$ of a comb, the [[evaluation order]] of a sequential tree, and the
[[dependency order]] of a single-spine tree are all total orders.  They contrast
with the branching case, whose dependency poset is only a partial order with
several linear extensions.

# 全序

集合 $P$ 上的**全序**（线性序）是每两个元素都可比较的偏序：对所有 $x,y\in P$，$x\le y$ 或
$y\le x$。链是全序子集，偏序集的线性扩张是扩展它的全序；有限偏序集有唯一线性扩张当且仅当它
已经是全序（链）。

在 AEG 系列中，全序是顺序情形：梳形的时间顺序 $1,2,\ldots,n$、顺序树的求值序、单脊柱树的
依赖偏序都是全序。它们与分支情形相对，后者的依赖偏序集只是有多个线性扩张的偏序。

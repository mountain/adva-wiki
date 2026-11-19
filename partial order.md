---
languages:
  en: Partial order
  zh: 偏序
default: en
---

# Partial order

A **partial order** on a set $P$ is a binary relation $\le$ that is reflexive,
antisymmetric, and transitive: $x\le x$; $x\le y$ and $y\le x$ imply $x=y$; and
$x\le y$ and $y\le z$ imply $x\le z$.  A set carrying a partial order is a
poset.  Elements $x,y$ are comparable when $x\le y$ or $y\le x$, and
incomparable otherwise; a chain is a totally ordered subset, and an antichain a
set of pairwise incomparable elements.

A [[total order]] is a partial order in which every two elements are comparable;
a linear extension of a poset is a total order extending it.  A down-set (order
ideal) is a subset closed under predecessors: $y\in U$ and $x\le y$ imply
$x\in U$.  A finite poset has a unique linear extension if and only if it is a
chain.

In the AEG series the partial order is the intrinsic form of data dependency:
the [[dependency order]] of an expression tree, the [[prefix order]] on marked
[[spinal history|spinal histories]], the down-set order on computation DAGs, and the
[[causal order]], [[temporal order]], and [[occurrence order]] of a program
diagram are all partial orders, and their legal [[evaluation order|evaluation orders]] are their
linear extensions.

# 偏序

集合 $P$ 上的**偏序**是自反、反对称且传递的二元关系 $\le$：$x\le x$；$x\le y$ 且
$y\le x$ 蕴含 $x=y$；$x\le y$ 且 $y\le z$ 蕴含 $x\le z$。带偏序的集合称为偏序集。元素
$x,y$ 当 $x\le y$ 或 $y\le x$ 时可比较，否则不可比较；链是全序子集，反链是两两不可比较的
元素集。

全序是每两个元素都可比较的偏序；偏序集的线性扩张是扩展它的全序。下集（序理想）是对前驱
封闭的子集：$y\in U$ 且 $x\le y$ 蕴含 $x\in U$。有限偏序集有唯一线性扩张当且仅当它是链。

在 AEG 系列中，偏序是数据依赖的内蕴形式：表达式树的依赖偏序、标记脊历史上的前缀序、计算
DAG 上的下集序，以及程序图的因果序、时间序与出现序，都是偏序，其合法求值序即其线性扩张。

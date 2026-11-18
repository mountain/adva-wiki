---
languages:
  en: Dependency order
  zh: 依赖偏序
default: en
---

# Dependency order

The **dependency order** of an [[arithmetic expression]] tree $T$ is the partial
order on its internal vertices given by data flow: for $u,v\in I(T)$, write
$u\preccurlyeq_T v$ when either $u=v$ or the value produced at $u$ is required
as an input at $v$ — equivalently, $v$ lies on the path from $u$ to the root.
A legal [[internal evaluation order]] is a linear extension of this finite poset.

The order is the intrinsic record of which operations must precede which: the
planar tree does not by itself order operations on disjoint subtrees.  A
finite poset has a unique linear extension if and only if it is a chain, and
for a binary expression tree this is equivalent to every internal vertex
having at most one internal child, and to the internal vertices forming a
single spine.  This is the sequential-tree classification.

For a comb the dependency order is the chain $v_1<v_2<\cdots<v_n$, so the only
legal internal evaluation order is the [[chronological order]] $1,2,\ldots,n$.  The
dependency order is the intrinsic notion that replaces informal "left/right"
language; the resulting marked object is a [[marked spinal history]].

# 依赖偏序

算术表达式树 $T$ 的**依赖偏序**是其内部顶点上由数据流给出的偏序：对
$u,v\in I(T)$，当 $u=v$，或 $u$ 处产生的值被要求作为 $v$ 的输入（等价地，$v$ 位于从
$u$ 到根的路径上）时，记 $u\preccurlyeq_T v$。合法的内部求值序就是这个有限偏序集的
线性扩张。

该偏序是"哪些运算必须先于哪些"的内蕴记录：平面树本身并不给不相交子树上的运算定序。
有限偏序集有唯一线性扩张当且仅当它是链；对二叉表达式树，这等价于每个内部顶点至多有
一个内部子顶点，也等价于内部顶点形成单脊柱。这就是顺序树分类。

对梳形，依赖偏序就是链 $v_1<v_2<\cdots<v_n$，故唯一合法的内部求值序是时间顺序
$1,2,\ldots,n$。依赖偏序是取代非正式"左/右"语言的内蕴概念；所得的标记对象是标记脊历史。

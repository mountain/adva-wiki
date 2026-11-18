---
languages:
  en: Arithmetic rank
  zh: 算术秩
default: en
---

# Arithmetic rank

The **arithmetic rank** is the level of an operation in the arithmetic tower:
rank one is addition, rank two is multiplication, and rank three is
exponentiation (the power maps), each rank iterating the previous one.  On the
positive [[assignment]] line $a>0$ the three are generated respectively by
$A=\partial_a$, $M=a\partial_a$, and $P=a\log a\,\partial_a$; the flow of $P$
is $a(t)=a(0)^{e^t}$, which moves the exponent and is the infinitesimal form
of the [[third rank]].

The ranks do not close under the Lie bracket: $[A,M]=A$, $[M,P]=M$, and
$[A,P]=(1+\log a)\partial_a$.  Hence the [[arithmetic generators]] generate an
[[infinite-dimensional Lie algebra]], and no finite-dimensional Lie group action
realizes all three ranks simultaneously.

"Third rank" is used here as a name for this calibration only; Paper 0 does
not attempt a classification of arithmetic ranks.  The same hierarchy appears
elsewhere as the [[hyperoperation rank]], read as a measure of process-compression.

# 算术秩

**算术秩**是算术塔中运算的层级：秩一为加法，秩二为乘法，秩三为幂运算（幂映射），每一级
迭代上一级。在正赋值线 $a>0$ 上三者分别由 $A=\partial_a$、$M=a\partial_a$、
$P=a\log a\,\partial_a$ 生成；$P$ 的流为 $a(t)=a(0)^{e^t}$，它移动指数，是第三秩的
无穷小形式。

这些秩在 Lie 括号下不封闭：$[A,M]=A$、$[M,P]=M$、$[A,P]=(1+\log a)\partial_a$。故
算术生成元生成无穷维 Lie 代数，没有任何有限维 Lie 群作用能同时实现这三个秩。

"第三秩"在此仅作为这一校准的名字使用；Paper 0 并未尝试对算术秩作分类。同样的层级在
别处作为超运算秩出现，被解读为过程压缩的一种度量。

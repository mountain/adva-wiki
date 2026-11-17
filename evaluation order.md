---
languages:
  en: Evaluation order
  zh: 求值序
default: en
---

# Evaluation order

The **evaluation order** of an [[arithmetic expression]] is the [[chronological order]]
in which its operations are evaluated.  An arithmetic expression is a planar
binary tree over $\Omega=\{+,-,\times,/\}$; the index of an operation is its
evaluation time, with the innermost operation evaluated first.  For a comb — an
expression whose internal vertices form a single chain — the order is unique:
the internal vertices form one dependency chain $v_1<v_2<\cdots<v_n$, and a
finite chain has a unique linear extension, so the only legal [[internal evaluation order]]
is $1,2,\ldots,n$.

The two extreme ways of writing a comb are the left- and right-expanded forms
$L_n[z]=\omega_n(\cdots\omega_2(\omega_1(z,c_1),c_2)\cdots,c_n)$ and
$R_n[z]=\omega_n(c_n,\cdots\omega_1(c_1,z)\cdots)$, in which the active subtree
occupies operand slot $(1)$ or $(2)$.  Both are chronological chains; the
planar direction in which the tree is drawn is not part of the [[convention]], and
the [[temporal order]] must not be identified with the planar orientation.

Paper 0 establishes uniqueness for combs given by explicit grammars.  The
intrinsic statement — that every binary expression tree with a unique internal
evaluation order has one such spine once operand slots are recorded — is
proved in Paper I.

# 求值序

算术表达式的**求值序**是其各运算被执行的时间顺序。算术表达式是
$\Omega=\{+,-,\times,/\}$ 上的平面二叉树；运算的下标即其求值时刻，最内层运算最先求值。
对梳形——即内部顶点构成单链的表达式——该顺序唯一：内部顶点形成一条依赖链
$v_1<v_2<\cdots<v_n$，而有限链有唯一的线性扩张，故唯一的合法内部求值序是
$1,2,\ldots,n$。

书写梳形的两种极端方式是左展开与右展开形式
$L_n[z]=\omega_n(\cdots\omega_2(\omega_1(z,c_1),c_2)\cdots,c_n)$ 与
$R_n[z]=\omega_n(c_n,\cdots\omega_1(c_1,z)\cdots)$，其中活动子树占据操作数槽 $(1)$ 或
$(2)$。两者都是时间链；树的平面画法不属于该约定，且时间顺序不得与平面朝向混同。

Paper 0 对由显式文法给出的梳形建立了唯一性。内蕴陈述——每个具有唯一内部求值序的二叉
表达式树在记录操作数槽之后都有这样一条脊柱——是在 Paper I 中证明的。

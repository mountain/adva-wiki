---
languages:
  en: Marked history
  zh: 标记历史
default: en
---

# Marked history

A **marked history** is a history whose evolving value is tracked explicitly: it
is a chronological word of elementary one-hole contexts
$C_{\omega,c}^{(1)}[z]=\omega(z,c)$ and $C_{\omega,c}^{(2)}[z]=\omega(c,z)$,
where the superscript marks which operand slot carries the evolving value.  A
bounded marked history adds an initial accumulator, written $(x_0;\gamma)$; the
empty word represents the marked single-leaf tree.

The marking resolves an ambiguity the [[dependency order]] alone does not: a
sequential tree determines which operation is performed first, but not which of
its two leaf inputs is carried forward along the spine.  Choosing that leaf as
the initial accumulator is the mark, and the slot superscripts form the
chirality word $\varepsilon(\gamma)$.

A marked sequential tree and a bounded marked history determine each other
uniquely, provided operation labels, constants, operand slots, and the initial
mark are retained.  The precise sequential form is the [[marked spinal history]];
earlier drafts called certain pure-chirality cases threadlike expressions, and
the present definition includes mixed chirality and makes the marking part of
the data.

# 标记历史

**标记历史**是显式追踪演化值的历史：它是初等单孔语境
$C_{\omega,c}^{(1)}[z]=\omega(z,c)$ 与 $C_{\omega,c}^{(2)}[z]=\omega(c,z)$ 的时间顺序词，
其上标标记哪个操作数槽承载演化值。有界标记历史另加一个初始累加器，记作 $(x_0;\gamma)$；
空词表示被标记的单叶树。

标记解决了依赖偏序本身无法确定的歧义：顺序树决定了哪个运算先执行，却不决定其两个叶输入中
哪个沿脊柱被携带。选择该叶为初始累加器就是标记，而上标构成的字就是手性词
$\varepsilon(\gamma)$。

被标记的顺序树与有界标记历史彼此唯一确定，只要保留运算标号、常量、操作数槽与初始标记。
精确的顺序形式是标记脊历史；早期草稿把某些纯手性情形称为线状表达式，现行定义包含混合手性
并把标记作为数据的一部分。

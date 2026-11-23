---
languages:
  en: Cut elimination
  zh: 切割消去
default: en
---

# Cut elimination

**Cut elimination** is the proof-theoretic property that the cut rule of a
sequent calculus is eliminable: every proof that uses cuts can be transformed
into a cut-free proof.  It is a strengthening of [[cut admissibility]] — the
admissible rule may be discarded from the calculus, whereas elimination also
gives an effective rewrite to a cut-free derivation.

The bounded-logic work asserts only conditional fresh-cut admissibility, not a
general cut-elimination theorem, and the statement is deliberately not inflated
into one.  This proof-theoretic cut is distinct from the program-level
[[causal cut]], which is a downward-closed event frontier in a diagram.

# 切割消去

**切割消去**是证明论性质：序列演算的切割规则可消去——每个使用切割的证明都可变换为无切割证明。
它是切割可容许性的加强——可容许规则可从演算中丢弃，而消去还给出到无切割推导的有效重写。

有界逻辑工作只断言有条件的全新切割可容许性，而非一般切割消去定理，且该陈述被有意地不夸大为
消去定理。此证明论切割区别于程序级的因果切割，后者是图中向下封闭的事件前沿。

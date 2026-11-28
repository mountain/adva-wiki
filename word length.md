---
languages:
  en: Word length
  zh: 字长
default: en
---

# Word length

The **word length** $|w|$ of a history is the number of its steps — the
unweighted depth of a [[literal history]].  It is the process/representation
depth of [[history geometry]]: a history $h=X_{i_1}\cdots X_{i_n}$ has word length
$n$, and this is the depth measured before any weighting.

Word length is a declared budget parameter (a finite checker works over words of
bounded length), and it grows with the history; the weighted [[history depth]]
replaces each step by its cost.

# 字长

历史的**字长** $|w|$ 是其步数——字面历史的无权深度。它是历史几何的过程/表示深度：历史
$h=X_{i_1}\cdots X_{i_n}$ 有字长 $n$，这是在加权之前度量的深度。

字长是声明的预算参数（有限检查器在有界长度词上工作），且随历史增长；有权历史深度把每步换成其
成本。

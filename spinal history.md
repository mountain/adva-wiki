---
languages:
  en: Spinal history
  zh: 脊历史
default: en
---

# Spinal history

A **spinal history** is the history of a sequential tree — a tree whose internal
vertices form a single spine, equivalently whose [[dependency order]] is a chain.
It is the chronological word of elementary one-hole contexts along that spine;
the sequential case contrasts with branching histories, whose dependency poset
is not a chain.

The syntactic passage is: an unmarked sequential tree, together with a choice of
initial accumulator, determines a marked planar sequential tree, which is in
bijection with a bounded [[marked spinal history]]; only the later evaluation
steps to an operator and an endpoint forget process data.  The marking resolves
which leaf is carried along the spine.

The free marked spinal histories form a monoid under chronological
concatenation, and the [[prefix order]] — $\gamma\sqsubseteq\gamma'$ when
$\gamma'=\gamma\delta$ — records earlier truncations; its ideal completion is
the dcpo of finite and countably infinite words.  The prefix order is exactly
the [[information order]] for a chain dependency poset.

# 脊历史

**脊历史**是顺序树的历史——即内部顶点形成单脊柱的树，等价地其依赖偏序是链。它是沿该脊柱
的初等单孔语境的时间顺序词；顺序情形与分支历史相对，后者的依赖偏序集不是链。

句法通道为：未标记的顺序树，连同初始累加器的选择，确定一个标记平面顺序树，它与有界标记脊
历史一一对应；只有后来的求值步骤到算子与端点才遗忘过程数据。标记解决了哪个叶沿脊柱被携带。

自由标记脊历史在时间顺序拼接下构成幺半群，前缀序 $\gamma\sqsubseteq\gamma'$（当
$\gamma'=\gamma\delta$）记录较早的截断；其理想完备化是有限与可数无穷词的有向完全偏序。
前缀序正是链依赖偏序集的信息序。

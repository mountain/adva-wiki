---
languages:
  en: History geometry
  zh: 历史几何
default: en
---

# History geometry

**History geometry** is the depth-and-width shape of the prefix representation
of a process's histories, read after the exact relations and the task
sufficiency have been fixed.  The depth of a [[literal history]]
$h=X_{i_1}\cdots X_{i_n}$ is its length $d(h)=n$, or the weighted
$d_c(h)=\sum c(X_{i_j})$ with primitive costs; this is process depth, not
physical clock time.

The width is the boundary or frontier complexity: for a family of histories, the
number $W(n)=|B_n|$ of distinct prefixes at depth $n$.  History geometry is a
useful entropy shadow — it is not topological entropy, and it is not process
equality.  Huffman coding sits at this layer and the next (presentation search);
it selects a cheaper representation, and does not decide which histories are
semantically or task equivalent.

# 历史几何

**历史几何**是过程历史前缀表示的深度与宽度形状，在精确关系与任务充分性固定之后读出。字面历史
$h=X_{i_1}\cdots X_{i_n}$ 的深度是其长度 $d(h)=n$，或带原始成本的有权深度
$d_c(h)=\sum c(X_{i_j})$；这是过程深度，而非物理时钟时间。

宽度是边界或前沿复杂度：对一族历史，深度 $n$ 处不同前缀的数目 $W(n)=|B_n|$。历史几何是有用
的熵影子——它不是拓扑熵，也不是过程相等。Huffman 编码位于此层及下一层（展示搜索）；它选择更
便宜的表示，而不决定哪些历史在语义或任务上等价。

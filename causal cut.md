---
languages:
  en: Causal cut
  zh: 因果切割
default: en
---

# Causal cut

A **causal cut** is the open frontier of a completed past in the [[causal order]] of
a checked program diagram.  For a Rust-checked finite shared program diagram
$D$ with operation nodes $E_D$, the [[temporal order]] is $e\preceq_D f$ (a directed
wire path from $e$ to $f$), and a completed past is a downward-closed subset
$U\subseteq E_D$.  The wires that cross from producers already available (program
inputs or events in $U$) to consumers still waiting (events outside $U$ or the
program output) form the causal cut of $U$.

The completed pasts form the opens of an Alexandrov topology — a finite
distributive lattice — and the temporal order is recovered from them:
$e\preceq_D f$ if and only if $f\in U\Rightarrow e\in U$ for every completed
past $U$.  This is a bounded space–time duality.  The cut carries occurrence
data on its frontier: two wires crossing the same cut may share a source
identifier while carrying distinct occurrence identifiers.

A causal cut is a derived reading of a checked shared program diagram, reusing
exact wire, source, and occurrence data; it is not the full program geometry on
its own.

# 因果切割

**因果切割**是经检验程序图的因果序中某个完成过去的开边界。对 Rust 检验的有限共享程序图
$D$（运算节点集 $E_D$），时间序为 $e\preceq_D f$（从 $e$ 到 $f$ 的有向线路径）；完成过去是
向下封闭子集 $U\subseteq E_D$。从已可用生产者（程序输入或 $U$ 中事件）跨到仍在等待的消费者
（$U$ 外事件或程序输出）的线，构成 $U$ 的因果切割。

完成过去构成 Alexandrov 拓扑的开集——即有限分配格——时间序可由它们恢复：
$e\preceq_D f$ 当且仅当对每个完成过去 $U$，$f\in U\Rightarrow e\in U$。这是有界的时空对偶。
切割在其边界上携带出现数据：跨越同一切割的两条线可共享源标识，却携带不同的出现标识。

因果切割是经检验共享程序图的导出解读，复用精确的线、源与出现数据；它本身不是完整的程序几何。

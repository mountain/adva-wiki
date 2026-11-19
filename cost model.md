---
languages:
  en: Cost model
  zh: 成本模型
default: en
---

# Cost model

A **cost model** is a declared pricing functional that orders or compares
representations of a process for a stated task.  In the costed process
presentation
$\Pi=(\mathcal A,\Sigma,\mathcal H,\mathcal R,\llbracket\cdot\rrbracket,T,c)$,
the cost component $c$ prices the grammar, the relations, the history, the
decoding, and the task error.

The model is declared and task-relative, not canonical or universal: there is no
universal cost model, and "cheaper" or "efficient" is meaningful only against a
declared baseline, workload, cost model, and scope.  A shorter history may
require a more expensive dictionary or decoder, so [[word length]] is only one cost
axis; the caller supplies the relevant model rather than inheriting a global
one.

# 成本模型

**成本模型**是声明的定价泛函，对某个既定任务对过程的表示进行排序或比较。在带成本的过程展示
$\Pi=(\mathcal A,\Sigma,\mathcal H,\mathcal R,\llbracket\cdot\rrbracket,T,c)$ 中，成本分量
$c$ 定价文法、关系、历史、解码与任务误差。

该模型是声明的、相对任务的，而非典范或普适的：不存在普适成本模型，"更便宜"或"高效"只有在
声明的基线、工作量、成本模型与范围内才有意义。较短的历史可能需要更昂贵的词典或解码器，故词
长只是成本的一个轴；调用方提供相关模型，而非继承一个全局模型。

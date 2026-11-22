---
languages:
  en: Matrix product
  zh: 矩阵积
default: en
---

# Matrix product

The **matrix product** of a chronological [[affine history]] is the product, in
order, of the [[affine matrix|affine matrices]] $\begin{pmatrix}\alpha_i&\beta_i\\0&1\end{pmatrix}$
representing its operations.  It gives the prefix recursion
$A_i=\alpha_i A_{i-1}$, $B_i=\alpha_i B_{i-1}+\beta_i$ with $(A_0,B_0)=(1,0)$, so
the accumulated scale and translation are read off

$$\begin{pmatrix}A_i&B_i\\0&1\end{pmatrix}.$$

The lower-left entry remains zero at every stage (the affine/Borel slice), so
projectively all prefixes stabilize the same point $\infty$; a right-slot
division makes that entry nonzero.  The matrix product condenses a history to
its [[affine cocycle]] coordinates $(A_n,B_n)$, and it is the affine-sector
instance of the [[projective matrix]] composition.

# 矩阵积

时间顺序仿射历史的**矩阵积**是其各运算的仿射矩阵
$\begin{pmatrix}\alpha_i&\beta_i\\0&1\end{pmatrix}$ 按顺序的乘积。它给出前缀递归
$A_i=\alpha_i A_{i-1}$、$B_i=\alpha_i B_{i-1}+\beta_i$（$(A_0,B_0)=(1,0)$），故累积尺度与平移由

$$\begin{pmatrix}A_i&B_i\\0&1\end{pmatrix}$$

读出。左下角项在每一阶段保持为零（仿射/Borel 切片），故射影地所有前缀稳定于同一点 $\infty$；
右槽除法使该项非零。矩阵积把历史压缩为其仿射余循环坐标 $(A_n,B_n)$，是射影矩阵复合的仿射扇形
实例。

---
languages:
  en: Matrix multiplication
  zh: 矩阵乘法
default: en
---

# Matrix multiplication

**Matrix multiplication** is the composition operation on matrices; for the
[[affine matrix|affine matrices]] $\begin{pmatrix}\Phi&a\\0&1\end{pmatrix}$ representing motions
$x\mapsto\Phi x+a$, it is exactly the affine group law.  Multiplication
composes in the same [[chronological order]] as the motions: applying
$\begin{pmatrix}\Phi_1&a_1\\0&1\end{pmatrix}$ then
$\begin{pmatrix}\Phi_2&a_2\\0&1\end{pmatrix}$ gives
$\begin{pmatrix}\Phi_2\Phi_1&\Phi_2a_1+a_2\\0&1\end{pmatrix}$.

In the projective sector, matrix multiplication composes the [[projective matrix]]
representatives, with the central sign of the [[linear lift]] tracking the chosen
lift.  A chronological history evaluates by multiplying its operation matrices
in order.

# 矩阵乘法

**矩阵乘法**是矩阵的复合运算；对表示运动 $x\mapsto\Phi x+a$ 的仿射矩阵
$\begin{pmatrix}\Phi&a\\0&1\end{pmatrix}$，它正是仿射群律。乘法按与运动相同的时间顺序复合：
先作用 $\begin{pmatrix}\Phi_1&a_1\\0&1\end{pmatrix}$ 再
$\begin{pmatrix}\Phi_2&a_2\\0&1\end{pmatrix}$ 得
$\begin{pmatrix}\Phi_2\Phi_1&\Phi_2a_1+a_2\\0&1\end{pmatrix}$。

在射影扇形中，矩阵乘法复合射影矩阵代表，线性提升的中心符号追踪所选的提升。时间顺序历史按其
运算矩阵按顺序相乘求值。

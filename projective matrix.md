---
languages:
  en: Projective matrix
  zh: 射影矩阵
default: en
---

# Projective matrix

A **projective matrix** is the homogeneous-coordinate matrix of a projective
motion, an element of $\operatorname{PGL}_2$ (or a lift in
$\operatorname{SL}_2$).  The affine sector is its Borel slice: an [[affine motion]]
$\varphi(z)=\Phi z+\xi$ with $\Phi>0$ has the homogeneous matrix
$\begin{pmatrix}\Phi&\xi\\0&1\end{pmatrix}$, and its normalised lift
$\Phi^{-1/2}\begin{pmatrix}\Phi&\xi\\0&1\end{pmatrix}\in\operatorname{SL}_2$ has
eigenvalues $e^{\pm M/2}$, where $M=\ln\Phi$ is the [[multiplicative charge]].

The trace of a lift is well defined up to sign, and its square classifies the
motion: $\tau^2>4$ is hyperbolic, $\tau^2=4$ parabolic, $\tau^2<4$ elliptic.  On
the affine slice the [[hyperbolic length]] is $\lvert\ln\Phi\rvert$.  Second-slot
division $z\mapsto c/z$ is not an affine motion; it is realised only as a
projective matrix, an element of $\operatorname{PGL}_2$.

# 射影矩阵

**射影矩阵**是射影运动的齐次坐标矩阵，即 $\operatorname{PGL}_2$ 的元素（或 $\operatorname{SL}_2$
中的提升）。仿射扇形是其 Borel 切片：仿射运动 $\varphi(z)=\Phi z+\xi$（$\Phi>0$）有齐次矩阵
$\begin{pmatrix}\Phi&\xi\\0&1\end{pmatrix}$，其归一化提升
$\Phi^{-1/2}\begin{pmatrix}\Phi&\xi\\0&1\end{pmatrix}\in\operatorname{SL}_2$ 有特征值
$e^{\pm M/2}$，其中 $M=\ln\Phi$ 是乘法荷。

提升的迹到符号有定义，其平方分类运动：$\tau^2>4$ 为双曲、$\tau^2=4$ 为抛物、$\tau^2<4$ 为椭圆。
在仿射切片上双曲长度为 $\lvert\ln\Phi\rvert$。第二槽除法 $z\mapsto c/z$ 不是仿射运动；它只能作为
射影矩阵（$\operatorname{PGL}_2$ 的元素）实现。

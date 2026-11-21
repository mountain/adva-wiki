---
languages:
  en: Riemannian metric
  zh: 黎曼度量
default: en
---

# Riemannian metric

A **Riemannian metric** on a smooth manifold $M$ is a smooth, positive-definite,
symmetric $(0,2)$-tensor field $g$, giving each tangent space $T_pM$ an inner
product.  It determines lengths, angles, distances, and [[curvature]] on $M$.

In the AEG series the metric is part of the data of a [[regular arithmetic expression space]]
$(M,g,a;\mu,\lambda)$: it measures the infinitesimal cost of moving and is
constrained by the [[eikonal]] identity $|\nabla a|_g^2=\mu^2+\lambda^2a^2$, while
the motions record arithmetic propagation and need not preserve $g$.  The
standard instances are the [[euclidean metric]], the [[hyperbolic metric]] of the
[[basic model]], and the [[horizontal metric]] of the [[contact model]].

# 黎曼度量

光滑流形 $M$ 上的**黎曼度量**是光滑、正定、对称的 $(0,2)$-张量场 $g$，给每个切空间 $T_pM$ 一个
内积。它决定 $M$ 上的长度、角度、距离与曲率。

在 AEG 系列中，度量是正则算术表达式空间 $(M,g,a;\mu,\lambda)$ 数据的一部分：它度量移动的无穷小
成本，并受程函恒等式 $|\nabla a|_g^2=\mu^2+\lambda^2a^2$ 约束，而运动记录算术传播、不必保持 $g$。
标准实例是欧氏度量、基本模型的双曲度量与接触模型的水平度量。

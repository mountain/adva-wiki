---
languages:
  en: Flow equation
  zh: 流方程
default: en
---

# Flow equation

In a regular arithmetic expression space (AES) $\mathfrak E=(M,g,a;\mu,\lambda)$
with its [[canonical arithmetic frame]], the **flow equation** is the first-order
[[ordinary differential equation]] satisfied by the assignment $a$ along a
unit-speed curve $\gamma$ whose tangent is
$\dot\gamma=\cos\theta\,X_u+\sin\theta\,X_v$:

$$\frac{d}{ds}(a\circ\gamma)=\mu\cos\theta+\lambda(a\circ\gamma)\sin\theta.$$

For constant $\theta$, its solutions are the directional affine solutions.  The
[[arithmetic flow]] is the [[horizontal lift]] of an Ehresmann connection over the
direction plane, and the constant $\mu\lambda$ is its curvature; the same
bracket is computed intrinsically in the [[canonical frame]] and gives the
[[hyperbolic area form]] of the [[basic model]].

# 流方程

在正则算术表达式空间（AES）$\mathfrak E=(M,g,a;\mu,\lambda)$ 及其规范算术框架中，
**流方程**是赋值 $a$ 沿单位速率曲线 $\gamma$ 满足的一阶常微分方程，其中
$\dot\gamma=\cos\theta\,X_u+\sin\theta\,X_v$：

$$\frac{d}{ds}(a\circ\gamma)=\mu\cos\theta+\lambda(a\circ\gamma)\sin\theta.$$

对常数 $\theta$，其解为方向仿射解。算术流是方向平面上一个 Ehresmann 联络的水平提升，
常数 $\mu\lambda$ 是其曲率；同一括号在规范框架中的内蕴计算给出基本模型的双曲面积形式。

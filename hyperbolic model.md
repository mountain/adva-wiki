---
languages:
  en: Hyperbolic model
  zh: 双曲模型
default: en
---

# Hyperbolic model

The **[[basic hyperbolic model]]** is the [[regular arithmetic expression space]] ([[AES]])

$$\mathfrak E_0(\mu,\lambda)=(\mathbb H^2,g_{\mu,\lambda},a;\mu,\lambda)$$

on the upper half-plane $\mathbb H^2=\{(x,y)\in\mathbb R^2:y>0\}$, with metric

$$g_{\mu,\lambda}=\frac1{y^2}\left(\frac{dx^2}{\mu^2}+\frac{dy^2}{\lambda^2}\right)$$

and [[assignment]] $a(x,y)=-x/y$.  It has constant Gaussian [[curvature]]
$K=-\lambda^2$, no [[puncture]], and its assignment vanishes along one complete
[[geodesic]].  In earlier drafts it was written $\mathfrak E_{\mathrm{hyp}}(\mu,\lambda)$.

The metric admits a group-theoretic description: writing
$G=\operatorname{Aff}^+(1,\mathbb R)$ for the positive affine group, the
left-invariant vector fields $X_u=-\mu y\,\partial_x$ and $X_v=-\lambda y\,\partial_y$
form the [[canonical arithmetic frame]], whose bracket is the constant $\mu\lambda$,
the curvature of the [[arithmetic flow]].  The [[basic model]] is complete with constant
curvature, and it is the model in which the [[arithmetic motion|arithmetic motions]] are read as point
paths.

# 双曲模型

**基本双曲模型**是上半平面 $\mathbb H^2=\{(x,y)\in\mathbb R^2:y>0\}$ 上的正则算术表达式空间（AES）

$$\mathfrak E_0(\mu,\lambda)=(\mathbb H^2,g_{\mu,\lambda},a;\mu,\lambda),$$

其度量为

$$g_{\mu,\lambda}=\frac1{y^2}\left(\frac{dx^2}{\mu^2}+\frac{dy^2}{\lambda^2}\right),$$

赋值为 $a(x,y)=-x/y$。它有常高斯曲率 $K=-\lambda^2$，无穿孔，赋值沿一条完整测地线消失。
早期草稿中它记为 $\mathfrak E_{\mathrm{hyp}}(\mu,\lambda)$。

该度量有群论描述：以 $G=\operatorname{Aff}^+(1,\mathbb R)$ 记正仿射群，左不变向量场
$X_u=-\mu y\,\partial_x$ 与 $X_v=-\lambda y\,\partial_y$ 构成规范算术框架，其括号是常数
$\mu\lambda$，即算术流的曲率。基本模型完备且曲率恒定，算术运动在此模型中读作点路径。

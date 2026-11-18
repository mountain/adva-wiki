---
languages:
  en: Arithmetic frame
  zh: 算术框架
default: en
---

# Arithmetic frame

The **arithmetic frame** of a [[regular arithmetic expression space]] is the
unique positively [[oriented orthonormal frame]] $(X_u,X_v)$ satisfying
$X_u a=\mu$ and $X_v a=\lambda a$, where $a$ is the [[assignment]] and
$\mu\ne0$, $\lambda$ are the two arithmetic parameters.  Its existence is
equivalent to the [[eikonal equation]] $|\nabla a|_g^2=\mu^2+\lambda^2a^2$;
writing $q=\sqrt{\mu^2+\lambda^2a^2}$ and $E_a=\nabla a/q$, it is

$$X_u=\frac{\mu}{q}E_a-\frac{\lambda a}{q}JE_a,\qquad
X_v=\frac{\lambda a}{q}E_a+\frac{\mu}{q}JE_a,$$

where $J$ is rotation by $+\pi/2$.  Thus $X_u$ is the additive direction
(along it $a$ changes at the constant rate $\mu$) and $X_v$ the multiplicative
direction ($a$ changes at rate $\lambda a$); the frame is the [[canonical arithmetic frame]].

The frame is generally non-coordinate.  Its bracket on the assignment is
$[X_u,X_v]a=\mu\lambda$, so for $\lambda\ne0$ the two directions do not
commute; this constant is the [[curvature]] density that returns in the [[ACS]] and
the [[contact model]].

# 算术框架

正则算术表达式空间的**算术框架**是满足 $X_u a=\mu$ 与 $X_v a=\lambda a$ 的唯一正定向
正交归一标架 $(X_u,X_v)$，其中 $a$ 是赋值，$\mu\ne0$、$\lambda$ 是两个算术参数。其存在
等价于程函方程 $|\nabla a|_g^2=\mu^2+\lambda^2a^2$；令 $q=\sqrt{\mu^2+\lambda^2a^2}$、
$E_a=\nabla a/q$，则

$$X_u=\frac{\mu}{q}E_a-\frac{\lambda a}{q}JE_a,\qquad
X_v=\frac{\lambda a}{q}E_a+\frac{\mu}{q}JE_a,$$

其中 $J$ 是旋转 $+\pi/2$。故 $X_u$ 是加法方向（沿它以常速率 $\mu$ 改变 $a$），$X_v$ 是
乘法方向（以速率 $\lambda a$ 改变 $a$）；该框架即规范算术框架。

框架一般不是坐标标架。它对赋值的括号为 $[X_u,X_v]a=\mu\lambda$，故当 $\lambda\ne0$ 时
两个方向不可交换；这一常数就是 ACS 与接触模型中再次出现的曲率密度。

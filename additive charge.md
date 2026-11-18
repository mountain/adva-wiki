---
languages:
  en: Additive charge
  zh: 加法荷
default: en
---

# Additive charge

For an add–scale history $\gamma$ — a finite word in the additive steps
$\mathsf A_p(x)=x+p$ and the scaling steps $\mathsf M_q(x)=e^q x$ — the
**additive charge** $A_\gamma$ is the [[accumulated additive charge]]: the sum of
the increments $p$ over its additive steps,

$$A_\gamma=\sum_{g_i=\mathsf A_{p_i}} p_i.$$

It is the first coordinate of the [[charge endpoint]] $(A_\gamma,M_\gamma)$ of the
[[charge path]] $C_\gamma$ in the [[accumulative commutative space]] ([[ACS]]).  On the
[[history group]] $G$, the [[charge map]] $c:G\to\mathbb R^2$ is the abelianization,
and the additive charge is its first coordinate $\mathsf A=\mathrm{pr}_1\circ c$,
with $c(\mathsf A_p)=(p,0)$ and $c(\mathsf M_q)=(0,q)$.

Unlike the [[multiplicative charge]], the additive charge does not descend to the
[[motion group]]: there is no homomorphism factoring it through the evaluation
$\nu:G\to\operatorname{Aff}^+(1,\mathbb R)$.  It is a property of the history,
not of the induced [[affine motion]].  Distributivity makes this visible: adding
$1$ and then multiplying by $e^q$ induces the same motion $z\mapsto e^qz+e^q$
as multiplying by $e^q$ and then adding $e^q$, yet the two histories carry
additive charges $1$ and $e^q$.

# 加法荷

对加乘历史 $\gamma$——即由加法步 $\mathsf A_p(x)=x+p$ 与缩放步
$\mathsf M_q(x)=e^q x$ 组成的有限词——，**加法荷** $A_\gamma$ 是累积的加法荷：
各加法步增量 $p$ 之和，

$$A_\gamma=\sum_{g_i=\mathsf A_{p_i}} p_i.$$

它是荷路径 $C_\gamma$ 的荷端点 $(A_\gamma,M_\gamma)$ 在累积交换空间（ACS）中的第一坐标。
在历史群 $G$ 上，荷映射 $c:G\to\mathbb R^2$ 即阿贝尔化，加法荷是其第一坐标
$\mathsf A=\mathrm{pr}_1\circ c$，满足 $c(\mathsf A_p)=(p,0)$、$c(\mathsf M_q)=(0,q)$。

与乘法荷不同，加法荷不下降到运动群：不存在使它经求值
$\nu:G\to\operatorname{Aff}^+(1,\mathbb R)$ 分解的同态。它是历史的属性，而非诱导仿射运动的
属性。分配律使这一点可见：先加 $1$ 再乘 $e^q$，与先乘 $e^q$ 再加 $e^q$，诱导同一运动
$z\mapsto e^qz+e^q$，但两条历史分别携带加法荷 $1$ 与 $e^q$。

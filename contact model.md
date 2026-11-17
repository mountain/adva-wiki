---
languages:
  en: Contact model
  zh: 接触模型
default: en
---

# Contact model

The **contact model** is the three-dimensional state space
$\mathcal C=\mathbb R^3_{(u,v,a)}$, where $a$ is the current [[assignment]] value
and $u,v$ parametrize additive and [[multiplicative motion]], equipped with the
arithmetic contact form

$$\alpha=da-\mu\,du-\lambda a\,dv$$

and the orientation $du\wedge da\wedge dv$.  It is a [[contact structure]] exactly
when $\mu\lambda\ne0$, since $\alpha\wedge d\alpha=\mu\lambda\,du\wedge da\wedge dv$.

The horizontal fields $D_u=\partial_u+\mu\partial_a$ and
$D_v=\partial_v+\lambda a\partial_a$ span $\mathcal D=\ker\alpha$, which is an
[[ehresmann|Ehresmann]] connection for the [[charge projection]]
$\pi(u,v,a)=(u,v)$; their [[horizontal lift]]s reproduce the
[[continuous affine flow]] $\frac{da}{ds}=\mu\cos\theta+\lambda a\sin\theta$.  The
[[curvature]] of this connection is $[D_u,D_v]=\mu\lambda\partial_a$: the
[[contact curvature]] is the constant $\mu\lambda$, the same density that
measures [[tearing]] in the [[ACS]].

For the [[basic model]] the correspondence is exact: the [[basic model]] is the
[[reeb quotient|Reeb quotient]] of the contact model under
$Q(u,v,a)=(-ae^{-\lambda v},e^{-\lambda v})=(x,y)$, with
$Q_*D_u=X_u$, $Q_*D_v=X_v$ and
$d\alpha=-\mu\lambda\,Q^*\bigl(d\mathrm{vol}_{g_{\mu,\lambda}}\bigr)$.  The
[[charge projection]] forgets the [[assignment]], while $Q$ forgets the [[Reeb]] direction;
the two quotients are complementary, and neither factors through the other.

# 接触模型

**接触模型**是三维状态空间 $\mathcal C=\mathbb R^3_{(u,v,a)}$——其中 $a$ 是当前赋值，
$u,v$ 参数化加法与乘法运动——配以算术接触形式

$$\alpha=da-\mu\,du-\lambda a\,dv$$

与定向 $du\wedge da\wedge dv$。当且仅当 $\mu\lambda\ne0$ 时它是接触结构，因为
$\alpha\wedge d\alpha=\mu\lambda\,du\wedge da\wedge dv$。

水平场 $D_u=\partial_u+\mu\partial_a$ 与 $D_v=\partial_v+\lambda a\partial_a$ 张成
$\mathcal D=\ker\alpha$，它是荷投影 $\pi(u,v,a)=(u,v)$ 上的 Ehresmann 联络；其水平提升
重现连续仿射流 $\frac{da}{ds}=\mu\cos\theta+\lambda a\sin\theta$。该联络的曲率为
$[D_u,D_v]=\mu\lambda\partial_a$：接触曲率即常数 $\mu\lambda$，与在 ACS 中度量撕裂的
密度相同。

对基本模型而言该对应是精确的：基本模型是接触模型在映射
$Q(u,v,a)=(-ae^{-\lambda v},e^{-\lambda v})=(x,y)$ 下的 Reeb 商，满足
$Q_*D_u=X_u$、$Q_*D_v=X_v$ 与
$d\alpha=-\mu\lambda\,Q^*\bigl(d\mathrm{vol}_{g_{\mu,\lambda}}\bigr)$。
荷投影遗忘赋值，而 $Q$ 遗忘 Reeb 方向；这两个商互补，且互不经过对方。

---
languages:
  en: Horizontal differential
  zh: 水平微分
default: en
---

# Horizontal differential

The **horizontal differential** $\delta_H$ of the [[contact model]] is, for a
smooth scalar field $F\in C^\infty(\mathcal C)$ on the carrier
$\mathcal C=\mathbb R^3_{(u,v,a)}$,

$$\delta_HF:=dF-(\partial_aF)\alpha=(D_uF)\,du+(D_vF)\,dv,$$

where $\alpha$ is the contact form and $D_u,D_v$ the horizontal fields.  It is
the [[ordinary differential]] restricted to horizontal directions, written on the
base coframe; for the [[assignment]] it is $\delta_Ha=\mu\,du+\lambda a\,dv$.  The
same operator is also called the [[scalar horizontal differential]] or the
[[horizontal covariant differential]].

For scalar fields only, the antisymmetrized second horizontal derivative is
$\mathcal R_H(F):=(D_uD_vF-D_vD_uF)\,du\wedge dv=\mu\lambda(\partial_aF)\,du\wedge dv$,
so $\mathcal R_H(a)=\mu\lambda\,du\wedge dv$ is the [[contact curvature]].  Writing
$\delta_H^2F$ for $\mathcal R_H(F)$ is only a shorthand: $\delta_H$ is not
extended to horizontal forms, and no nilpotent graded complex is asserted — the
operator is curvature-sensitive, and $\delta_H^2\ne0$ in general.

# 水平微分

接触模型的**水平微分** $\delta_H$，对载体 $\mathcal C=\mathbb R^3_{(u,v,a)}$ 上的光滑标量场
$F\in C^\infty(\mathcal C)$ 定义为

$$\delta_HF:=dF-(\partial_aF)\alpha=(D_uF)\,du+(D_vF)\,dv,$$

其中 $\alpha$ 是接触形式，$D_u,D_v$ 是水平场。它是限制到水平方向的普通微分，写在底余标架
上；对赋值有 $\delta_Ha=\mu\,du+\lambda a\,dv$。该算子也称为标量水平微分或水平共变微分。

仅对标量场，反对称化的二阶水平导数为
$\mathcal R_H(F):=(D_uD_vF-D_vD_uF)\,du\wedge dv=\mu\lambda(\partial_aF)\,du\wedge dv$，
故 $\mathcal R_H(a)=\mu\lambda\,du\wedge dv$ 即接触曲率。把 $\delta_H^2F$ 写成
$\mathcal R_H(F)$ 只是简写：$\delta_H$ 不扩展到水平形式，也不断言存在幂零的分次复形——
该算子是曲率敏感的，一般 $\delta_H^2\ne0$。

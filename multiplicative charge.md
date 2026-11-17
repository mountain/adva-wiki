---
languages:
  en: Multiplicative charge
  zh: 乘法荷
default: en
---

# Multiplicative charge

For an add–scale history $\gamma$ — a finite word in the additive steps
$\mathsf A_p(x)=x+p$ and the scaling steps $\mathsf M_q(x)=e^q x$ — the
**multiplicative charge** $M_\gamma$ is the accumulated [[logarithmic multiplicative charge]]:
the sum of the logarithmic increments $q$ over its
scaling steps,

$$M_\gamma=\sum_{g_i=\mathsf M_{q_i}} q_i.$$

It is the second coordinate of the [[charge endpoint]] $(A_\gamma,M_\gamma)$ of
the [[charge path]] $C_\gamma$ in the [[accumulative commutative space]] ([[ACS]]).  On
the [[history group]] $G$, the [[charge map]] $c:G\to\mathbb R^2$ is the
abelianization, and the multiplicative charge is the second coordinate
$\mathsf M=\mathrm{pr}_2\circ c$, with $c(\mathsf A_p)=(p,0)$ and
$c(\mathsf M_q)=(0,q)$.  Since $q=\ln e^q$, the charge is logarithmic: the
multipliers compose by multiplication while their charges add.

The multiplicative charge is the charge that survives evaluation.  By the
theorem that only the multiplicative charge descends, $\mathsf M$ factors
through the evaluation $\nu:G\to\operatorname{Aff}^+(1,\mathbb R)$ as
$\mathsf M=\log\circ L\circ\nu$, where $L$ is the linear part; hence
$M_\gamma=\ln\Phi$ whenever the induced [[affine motion]] is
$z\mapsto\Phi z+\xi$.  The [[additive charge]] admits no such factorization.
Consequently the [[translation length]] of an affine motion is this charge up to
sign, $\ell(\varphi)=\lvert\ln\Phi\rvert=\lvert M_\gamma\rvert$.

# 乘法荷

对加乘历史 $\gamma$——即由加法步 $\mathsf A_p(x)=x+p$ 与缩放步
$\mathsf M_q(x)=e^q x$ 组成的有限词——，**乘法荷** $M_\gamma$ 是累积的对数乘法荷：
各缩放步对数增量 $q$ 之和，

$$M_\gamma=\sum_{g_i=\mathsf M_{q_i}} q_i.$$

它是荷路径 $C_\gamma$ 的荷端点 $(A_\gamma,M_\gamma)$ 在累积交换空间（ACS）中的第二坐标。
在历史群 $G$ 上，荷映射 $c:G\to\mathbb R^2$ 即阿贝尔化，乘法荷是其第二坐标
$\mathsf M=\mathrm{pr}_2\circ c$，满足 $c(\mathsf A_p)=(p,0)$、$c(\mathsf M_q)=(0,q)$。
因 $q=\ln e^q$，该荷是对数的：乘子以乘法复合，而其荷以加法累加。

乘法荷是唯一能下降到求值的荷。按"只有乘法荷下降"定理，$\mathsf M$ 经求值
$\nu:G\to\operatorname{Aff}^+(1,\mathbb R)$ 分解为 $\mathsf M=\log\circ L\circ\nu$，
其中 $L$ 是线性部分；故当诱导仿射运动为 $z\mapsto\Phi z+\xi$ 时 $M_\gamma=\ln\Phi$。
加法荷不存在这样的分解。因此仿射运动的平移长度正是此荷到符号：
$\ell(\varphi)=\lvert\ln\Phi\rvert=\lvert M_\gamma\rvert$。

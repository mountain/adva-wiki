---
languages:
  en: Weighted area
  zh: 加权面积
default: en
---

# Weighted area

In the [[accumulative commutative space]] ([[ACS]]) — the oriented plane
$\mathcal A=\mathbb R^2_{(A,M)}$ with orientation $dA\wedge dM$ — a
**weighted area** is the integral of the target-normalized density
$e^{M_*-M}$ over an oriented two-chain $\Sigma$,

$$\iint_\Sigma e^{M_*-M}\,dA\wedge dM,$$

where $M_*$ is a fixed reference height, usually the common terminal
[[multiplicative charge]] of two histories.  The weight equals $1$ at the
terminal level $M=M_*$ and rescales the Euclidean [[area form]], so the [[additive charge]]
coordinate $A$ and the multiplicative coordinate $M$ do not enter the
area symmetrically.

The weighted area is the geometric value of [[relative torsion]].  By the
[[torsion Stokes theorem]], for two charge-compatible add–scale histories
$\gamma,\delta$ with common terminal charge $(A_*,M_*)$,

$$\tau(\gamma,\delta)=\oint_{C_\gamma-C_\delta}\eta_*=\iint_{\Sigma_{\gamma,\delta}} e^{M_*-M}\,dA\wedge dM,$$

where $\eta_*=e^{M_*-M}\,dA$ and $\Sigma_{\gamma,\delta}$ is any oriented
piecewise smooth two-chain with $\partial\Sigma_{\gamma,\delta}=C_\gamma-C_\delta$;
the value is independent of the filling.  The elementary rectangle
$\gamma=(\mathsf A_p,\mathsf M_q)$, $\delta=(\mathsf M_q,\mathsf A_p)$ has

$$\tau(\gamma,\delta)=p(e^q-1)=\int_0^p\!\int_0^q e^{q-M}\,dM\,dA.$$

The adjective is substantive.  In the staircase examples the integers
$1,6,21$ are values of the weighted area $n(e^{n\lambda}-1)$ at
$\lambda=\ln 2$, not of the unweighted area $n^2\lambda$ nor of the cell
count $n^2$; they carry no separate combinatorial meaning.  In Paper 0 the
[[order defect]] measured by this weighted area is named [[tearing]].

# 加权面积

在累积交换空间（ACS）——即按 $dA\wedge dM$ 定向的平面
$\mathcal A=\mathbb R^2_{(A,M)}$——中，**加权面积**是目标归一化密度
$e^{M_*-M}$ 在定向二维链 $\Sigma$ 上的积分

$$\iint_\Sigma e^{M_*-M}\,dA\wedge dM,$$

其中 $M_*$ 是固定参考高度，通常取两条历史的公共终末乘法荷。该权在终末高度
$M=M_*$ 处取 $1$，并以 $e^{M_*-M}$ 缩放欧氏面积形式，因此加法荷坐标 $A$ 与乘法荷坐标
$M$ 并不对称地进入面积。

加权面积是相对挠率的几何值。按挠率–Stokes 定理，对两条具有相同终末荷的加乘历史
$\gamma,\delta$（终末荷记为 $(A_*,M_*)$），有

$$\tau(\gamma,\delta)=\oint_{C_\gamma-C_\delta}\eta_*=\iint_{\Sigma_{\gamma,\delta}} e^{M_*-M}\,dA\wedge dM,$$

其中 $\eta_*=e^{M_*-M}\,dA$，$\Sigma_{\gamma,\delta}$ 是满足
$\partial\Sigma_{\gamma,\delta}=C_\gamma-C_\delta$ 的任一有向分片光滑二维链；该值不依赖于填充的选取。
基本矩形 $\gamma=(\mathsf A_p,\mathsf M_q)$、$\delta=(\mathsf M_q,\mathsf A_p)$ 给出

$$\tau(\gamma,\delta)=p(e^q-1)=\int_0^p\!\int_0^q e^{q-M}\,dM\,dA.$$

"加权"一词是实质性的：阶梯示例中的整数 $1,6,21$ 是加权面积
$n(e^{n\lambda}-1)$ 在 $\lambda=\ln 2$ 处的值，既非未加权面积 $n^2\lambda$，也非胞腔计数
$n^2$；它们不携带任何独立的组合意义。Paper 0 中这一加权面积所度量的次序缺陷被命名为撕裂。

---
languages:
  en: Order defect
  zh: 序缺陷
default: en
---

# Order defect

An **order defect** is the value by which two histories of the same elementary
operations differ when the operations are performed in different orders.  The
[[elementary order defect]] is "add, then scale" against "scale, then add": if
$\gamma$ first adds $\mu$ and then scales by $q$, while $\delta$ first scales
by $q$ and then adds $\mu$, then

$$\nu_x(\gamma)-\nu_x(\delta)=\mu(q-1),$$

which over the positive reals, with $q=e^M$, reads $\mu(e^M-1)$.  For small
increments $\mu h$ and $\lambda k$ the same value expands as
$\mu h(e^{\lambda k}-1)=\mu\lambda\,hk+O(\lVert(h,k)\rVert^3)$, so the
infinitesimal density of the order defect is the constant $\mu\lambda$.

The order defect is an open comparison of two chronological histories; it is
not a closed commutator-loop [[holonomy]], not a comparison with the [[path inverse]],
and not a mirror invariant.  It is the discrete root of [[tearing]]: for
charge-compatible pairs it is measured exactly as the [[ACS weighted area]], and
its density $\mu\lambda$ is the [[contact curvature]], the coefficient of
$[D_u,D_v]=\mu\lambda\partial_a$.

# 序缺陷

**序缺陷**是指同一组初等运算以不同次序执行时，两条历史取值之差。初等序缺陷即
"先加后乘"对"先乘后加"：以 $\gamma$ 记先加 $\mu$ 再乘 $q$，$\delta$ 记先乘 $q$
再加 $\mu$，则

$$\nu_x(\gamma)-\nu_x(\delta)=\mu(q-1),$$

在正实数上令 $q=e^M$，即得 $\mu(e^M-1)$。对微小增量 $\mu h$ 与 $\lambda k$，
同一值展开为 $\mu h(e^{\lambda k}-1)=\mu\lambda\,hk+O(\lVert(h,k)\rVert^3)$，
故序缺陷的无穷小密度是常数 $\mu\lambda$。

序缺陷是两条时间顺序历史的开比较；它不是闭交换子回路的和乐，不是与路径逆的比较，
也不是镜像不变量。它是撕裂的离散根源：对荷相容的对，它被精确地量度为 ACS 加权面积，
而其密度 $\mu\lambda$ 即接触曲率，也就是 $[D_u,D_v]=\mu\lambda\partial_a$ 的系数。

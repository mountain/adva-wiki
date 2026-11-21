---
languages:
  en: Forward differential
  zh: 前向微分
default: en
---

# Forward differential

The **forward differential** is the structural forward-mode differential of a
checked program, computed natively by Rust: the exact sensitivity of the
program's output to its inputs.  For a scalar program $\mathcal L(x,s,\kappa)$
it returns

$$d\mathcal L=(1-3\kappa)\,dx+3\,ds-3x\,d\kappa,$$

and in particular $\partial_\kappa\mathcal L=-3x$.  The certificate records the
checked diagram plus the versioned [[differential rule|differential rules]] (constant, copy, mul,
neg, add, scale).

The forward differential is the forward side of the [[differential calculus]],
paired against the [[backward transport]] (the contravariant side).  It is
distinct from the paper's [[horizontal differential]] $\delta$, which is the
contact-geometric differential restricted to horizontal directions.

# 前向微分

**前向微分**是经检验程序的结构化前向模式微分，由 Rust 原生计算：程序输出对其输入的精确敏感性。
对标量程序 $\mathcal L(x,s,\kappa)$ 它返回

$$d\mathcal L=(1-3\kappa)\,dx+3\,ds-3x\,d\kappa,$$

特别地 $\partial_\kappa\mathcal L=-3x$。证书记录经检验图与版本化微分规则（constant、copy、mul、
neg、add、scale）。

前向微分是微分演算的前向一侧，与后向传输（反变一侧）相配。它区别于论文的水平微分 $\delta$，
后者是限制到水平方向的接触几何微分。

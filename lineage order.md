---
languages:
  en: Lineage order
  zh: 谱系序
default: en
---

# Lineage order

The **lineage order** is the exact order of the occurrence lineage, owned by the
Rust upper `WireRef`.  It records the ordered occurrence lineage, and it is
distinct from a display order: the Rust lineage order $(t,K)$ may be sorted by an
observer display policy into $(K,t)$, and a bracket display is not exact lineage
order.

The lineage order is part of the ordered occurrence data, alongside the
[[occurrence order]], and it is distinct from the [[diagram order]].

# 谱系序

**谱系序**是出现谱系的精确次序，由 Rust 上层 `WireRef` 拥有。它记录有序出现谱系，区别于显示序：
Rust 谱系序 $(t,K)$ 可被观察者显示策略排序为 $(K,t)$，括号显示不是精确谱系序。

谱系序是有序出现数据的一部分，与出现序并列，且区别于图序。

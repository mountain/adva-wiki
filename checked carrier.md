---
languages:
  en: Checked carrier
  zh: 检查载体
default: en
---

# Checked carrier

A **checked carrier** is a carrier that has passed the Rust check — a validated
slice of a checked diagram, such as `TriadicObserverTransitionV0::slice`, a
checked program slice.  An observer transition supplies an exact checked carrier
between two diagrams, and Python audits the already checked [[local carrier]].

A checked carrier is typically both declared and [[exact carrier|exact]]: it is a
[[declared carrier]] whose directions are fixed, and it may be the [[common carrier]]
shared by several mechanisms.  It is built from a [[checked cut]], and it is the
basis on which downstream judgments are made.

# 检查载体

**检查载体**是通过 Rust 检查的载体——经检验图的已检验切片，如
`TriadicObserverTransitionV0::slice`（经检验程序切片）。观察者转移在两图之间供应精确检查载体，Python
审计已检查的局部载体。

检查载体通常是声明的且精确的：它是方向已固定的声明载体，且可为多个机制共享的公共载体。它由
经检验切割构建，是下游判断的依据。

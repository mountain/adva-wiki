---
languages:
  en: Process history
  zh: 过程历史
default: en
---

# Process history

A **process history** is the ordered, chronological record of a process — the
literal sequence of primitive operations performed — kept as a first-class
object, independent of and not reducible to its endpoint value.  It records the
order in which the operations were applied, and replacing it by a commutative
summary or a bare state forgets exactly that order.

The term records the "process before result" discipline of the AEG series: an
expression tree yields a [[marked history]], then an operator, then an endpoint
value, and two histories are not identified merely because they evaluate to the
same value.  A process history is an ordered word in a primitive grammar — the
[[history language]] and the [[history group]] carry this ordered data before any
evaluation — and it is the long form $a+a+\cdots+a$, only later compressed to
$na$.

Because it is ordered, a process history retains information that is invisible
after quotienting to a state or value; a [[lifted history]] keeps the order data
that the base quotient loses.

# 过程历史

**过程历史**是某个过程的有序时间记录——实际执行的原始运算的字面序列——作为一等对象保留，
独立于且不可约化为其端点值。它记录运算被执行的次序，用交换摘要或裸状态取代它恰好遗忘了
这次序。

该词记录 AEG 系列的"过程先于结果"纪律：表达式树先给出标记历史，再给出算子，最后是端点
值；两条历史不能仅仅因为求值相同就被等同。过程历史是原始文法中的有序词——历史语言与
历史群在求值之前就承载这份有序数据——它是长形式 $a+a+\cdots+a$，只是后来被压缩为 $na$。

因为它是有序的，过程历史保留着商到状态或值之后不可见的信息；提升历史保留了底商所丢失
的次序数据。

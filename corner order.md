---
languages:
  en: Corner order
  zh: 角序
default: en
---

# Corner order

The **corner order** of a plane binary tree is the order of its vertices
("corners") given by the left standard traversal, that is, the preorder:
root first, then the left subtree, then the right subtree.  The corners are
classified as SR (son of the root), LL (left leaves), RL (right leaves), and
LN, RN (left and right nonleaves).

The corner order is the preorder position, while the [[evaluation order]] is the
postorder; the two agree on leaves and are inverted on nonleaves.  For every
plane binary tree, the left-first postorder is the unique linear extension of
the [[dependency order]] minimizing inversions against the corner order.

# 角序

平面二叉树的**角序**是其顶点（"角"）按左标准遍历（即先序）给出的次序：先根、再左子树、后右
子树。角按 SR（根之子）、LL（左叶）、RL（右叶）、LN/RN（左/右非叶）分类。

角序是先序位置，而求值序是后序；二者在叶上一致、在非叶上反转。对每个平面二叉树，左先的后序
是依赖偏序的唯一线性扩张，使相对角序的反转数最小。

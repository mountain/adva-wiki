---
languages:
  en: Torsor
  zh: "挠子（Torsor）"
default: en
---

# Torsor

In mathematics, a **torsor** for a group $G$ — also called a **principal homogeneous space** — is a set $X$ on which $G$ acts freely and transitively. The action is so regular that $X$ looks exactly like $G$ once a point is chosen, but no point is part of the data. A torsor is therefore a group with its identity forgotten, or a ruler with no zero mark. Two points can be compared — their difference is an element of $G$ — but they cannot be added, and no point can be called the origin, until a reference point is chosen. The choice is not canonical, and the set of possible choices is itself the torsor.

The simplest picture is a clock face with no marked 12. The group $\mathbb{Z}/12\mathbb{Z}$ rotates the dial; any position can be moved to any other by a unique rotation, so the action is free and transitive. One can say that two positions differ by four hours, but not that a position is "three o'clock" until one decides where 12 is. Choosing 12 is a *trivialization*; a different choice changes every label by a rotation. The dial is a $\mathbb{Z}/12\mathbb{Z}$-torsor.

Torsors are central in algebra, geometry, topology, arithmetic, and gauge theory. They are also the precise shape of many statements in the AEG/Adva corpus, where "frame torsor," "resolution torsor," "parabolic torsor," and "torsor decomposition" look different but share the same structure: a group action that is free and transitive, with no canonical basepoint.

## Definition

Let $G$ be a group and $X$ a nonempty set with a left action

$$
G\times X\longrightarrow X,\qquad (g,x)\longmapsto g\cdot x .
$$

The action is **free** if $g\cdot x=x$ for some $x$ implies $g=e$; equivalently, every stabilizer is trivial. It is **transitive** if for every $x,y\in X$ there is some $g\in G$ with $g\cdot x=y$. A **$G$-torsor** is a nonempty $G$-set whose action is free and transitive. Equivalently, for every $x\in X$ the map

$$
G\longrightarrow X,\qquad g\longmapsto g\cdot x
$$

is a bijection. A morphism of $G$-torsors is a $G$-equivariant bijection; every such morphism is an isomorphism.

Choosing a point $x_0\in X$ gives a bijection $\varphi_{x_0}:G\to X$, $g\mapsto g\cdot x_0$. If $x_1=h\cdot x_0$ is another point, then

$$
\varphi_{x_1}(g)=g\cdot h\cdot x_0=\varphi_{x_0}(gh),
$$

so the two trivializations differ by right multiplication by $h$. In this sense a torsor is a group whose identity has been forgotten: a point restores the identity, but the restoration depends on the point.

The canonical operation on a torsor is not addition but *difference*. For $x,y\in X$ there is a unique $g\in G$ with $g\cdot x=y$; write $g=y-x$ in additive notation. The difference is independent of any basepoint. A sum requires a basepoint: after choosing $x_0$, one may define

$$
x+_{x_0}y=x_0+(x-x_0)+(y-x_0),
$$

but changing $x_0$ changes the sum. In affine notation this is the familiar statement that points of an affine space can be subtracted but not added until an origin is chosen. Algebraically, the same structure is a **heap**: a set with a ternary operation $[x,y,z]=x-y+z$ that generalizes the group law without selecting an identity.

### Trivial, noncanonical, and nontrivial

A $G$-torsor is **trivial** if it is isomorphic to $G$ with the left action. A point $x\in X$ is a trivialization, so a torsor over a point is always trivial as an abstract torsor: it is nonempty by definition, and any point gives an isomorphism with $G$. What may fail is a **canonical** trivialization. This distinction is the source of much confusion:

> A torsor over a point always has points. The issue is not existence but canonicity.

A torsor over a base $B$ is a family of $G$-torsors, one for each point of $B$. It is trivial if it has a global section, i.e. a consistent choice of a point in every fibre. Local sections always exist by local triviality, but a global section may not. Then the torsor is nontrivial in the stronger sense: there is no global point (no section) at all, although each fibre has points; this is stronger than merely having no canonical point. For a sheaf of groups $G$ on a site, isomorphism classes of $G$-torsors on $B$ are classified by the nonabelian cohomology set $H^1(B,G)$; a torsor is a 1-cocycle, and a trivialization is a coboundary.

The corpus usually speaks of the first kind of failure: a set of choices is nonempty, but no choice is canonical. For example, the set of resolutions of a through-crossing is nonempty and is isomorphic to $\mathbb{Z}$ after a resolution is chosen; the point is that the choice is the mathematical content, not that resolutions fail to exist. In the frame case, set-theoretic sections of $G\to G/H$ exist; what does not exist is a $G$-equivariant section. This is a naturality obstruction, not an existence obstruction.

## Torsor, homogeneous space, and principal bundle

Let $H\le G$. The quotient $G/H$ is a left $G$-set with a canonical point, the coset $H$. It is a **homogeneous space**. It is a $G$-torsor only when $H$ is trivial, because the stabilizer of $H$ is $H$. The projection

$$
\pi:G\longrightarrow G/H
$$

is a principal $H$-bundle; each fibre $\pi^{-1}(x)$ is an $H$-torsor under right multiplication. In the corpus, the sentence "$G\to G/H$ is an $H$-torsor" is shorthand for exactly this: the map is a principal $H$-bundle, and its fibres are $H$-torsors. The quotient $G/H$ itself is not an $H$-torsor; it is the base.

More generally, a **$G$-torsor over a base $B$** is a principal $G$-bundle $P\to B$; each fibre is a $G$-torsor. A $G$-torsor over a point is a single fibre. A global section of $P\to B$ trivializes the bundle; local sections are local trivializations, or gauge choices. A connection is additional data that lets one compare nearby fibres; it is not part of the torsor structure. For a Lie group, a torsor may carry a connection, but over an arbitrary field there is no canonical connection.

A single theorem can contain two different torsors. In the frame theorem below, the total space of framed bivaluations is a $G$-torsor, while the fibre of the projection to unframed bivaluations is an $H$-torsor. Keeping the group and the base straight is half the battle.

## Why torsors are everywhere

Many classification problems ask for a structure on a space, and the set of structures is often a torsor. A $GL_n$-torsor is the frame bundle of a rank-$n$ vector bundle; an $O_n$-torsor is a quadratic structure; a $\mathbb{G}_m$-torsor is a line bundle with its zero section removed; a $\mathbb{Z}/2$-torsor is a two-element set, or a double cover over a base, and an orientation is the two-element example; a $PGL_2$-torsor is a conic, i.e. a Severi–Brauer variety of dimension one, and more generally a $PGL_{n+1}$-torsor is a Severi–Brauer variety of dimension $n$. In topology, $H^1(B,G)$ classifies $G$-torsors; in gauge theory, a gauge field is a connection on a principal $G$-bundle, and a gauge choice is a local section.

Category-theoretically, the action groupoid $X/\!/G$ of a $G$-torsor is a connected groupoid equivalent to $BG$, the one-object groupoid of $G$. Choosing an object of $X/\!/G$ gives the equivalence; without a chosen object, the groupoid is equivalent to $BG$ but not canonically pointed. The "no canonical identity" of a torsor is the same statement as "no canonical object" of this groupoid.

## Examples

### Affine space: a ruler without a zero

Let $V$ be a vector space and $A$ a set on which $V$ acts simply transitively by translations. Then $A$ is an affine space, and $A$ is a $V$-torsor. The difference $y-x$ of two points is a vector; the sum $x+y$ is not defined. Choose an origin $0\in A$; then $A\cong V$, and one may define $x+y$ relative to $0$. Changing the origin by $a$ changes the sum by $a$. A vector space is an affine space with a canonical origin; it is a trivial $V$-torsor with a preferred point.

The solution set of a linear equation is the cleanest algebraic example. If $Ax=b$ is consistent, its solutions form a torsor for $\ker A$: the kernel acts by translation, freely and transitively, and the difference of two solutions lies in the kernel. If $b=0$, the zero vector is a canonical solution, so the solution set is a group. If $b\ne0$, there is no canonical solution, and the solution set is a nontrivial affine torsor.

### Bases, orientations, and isomorphisms

Let $V$ be an $n$-dimensional vector space. The set of ordered bases of $V$ is a $GL(V)$-torsor: $GL(V)$ acts simply transitively, and a reference basis gives an isomorphism with $GL(V)$. For a real vector space of positive dimension, the set of orientations is a $\mathbb{Z}/2$-torsor: there are two orientations, and no canonical one; choosing one identifies the set with $\mathbb{Z}/2$. The set of isomorphisms between two vector spaces is a $GL(V)$-torsor as well.

### Frames and gauge choices

The frame bundle of a vector bundle is a $GL_n$-torsor over the base; a frame is a local section. In gauge theory, a principal $G$-bundle over spacetime is a $G$-torsor over spacetime; a gauge is a local section, and a gauge transformation is a change of section. A connection is a rule for parallel transport, not a choice of section. The frame torsor in the corpus is exactly this kind of object for projective frames.

## Torsors in the AEG/Adva corpus

The corpus uses the word in several settings. The following table is a map; the subsections explain each row.

| Name in the corpus | Torsor | Acting group | What has no canonical choice | Source |
| --- | --- | --- | --- | --- |
| Frame torsor | third projective points over an ordered pair | $H=\operatorname{Stab}_G(q^+,q^-)$ | the third point, i.e. the frame | Paper IV, `thm:frame-torsor` |
| Resolution torsor | resolutions of a nodal through-crossing | $\langle T_\delta\rangle\cong\mathbb{Z}$ | which smoothing/resolution | Paper V, §8 |
| Parabolic torsor | conjugacy class of a nontrivial translation of a fixed sign | $\mathbb{R}_{>0}$ or $\mathbb{F}_q^\times$ | the representative of the class | Paper 0, `prop:p0-affine-two-layers` |
| Coset torsor | a coset $wK_{\mathrm{op}}$ or $gH$ | $K_{\mathrm{op}}$ or $H$ | the basepoint of the coset | `concept-ideal-point-naming`, §9.8 |
| Norm-fibre torsor | a nonzero norm fibre (an $8$-point conic) | $SO_2(\mathbb{F}_7)\cong\mathbb{Z}/8$ | the angle basepoint | `48-finite-field-trigonometry` |
| Ordering torsor | the two orderings of an unordered pair | $\mathbb{Z}/2$ | which point is first | `concept-ideal-point-naming`, §5.3 |
| Basepoint correction | carrier points of the pendulum | period lattice / clock group | the basepoint $P(0)$ | `54-pendulum-elliptic-group-rank-lowering` |

### The frame torsor: a third projective point

Let $K$ be a field, $G=PGL_2(K)$, and let $H$ be the stabilizer of an ordered pair $(q^+,q^-)$ of distinct points of $\mathbb{P}^1(K)$. A regular bivaluation is an ordered pair of distinct projective points, equivalently a rank-one idempotent on $K^2$. The first two points determine the projector. A third point $q^\infty$ selects a projective frame above it:

$$
(q^+,q^-,q^\infty)\longmapsto(q^+,q^-).
$$

The theorem `thm:frame-torsor` states that the set of framed regular bivaluations is a $G$-torsor; a reference triple is a point of it, so the theorem's phrase "after a reference triple has been chosen" is the trivialization step. The projection has fibres on which $H$ acts freely and transitively. Equivalently, $G\to G/H$ is an $H$-torsor.

Over $\mathbb{F}_q$ the numbers are explicit:

$$
\lvert G\rvert=q(q^2-1),\qquad
\lvert G/H\rvert=q(q+1),\qquad
\lvert H\rvert=q-1.
$$

The fibre over an ordered pair is the set of allowed third points, of size $q-1=|H|$; $H$ acts on it simply transitively. The third point is the frame: the first two points determine the *concept*, and the third selects a *coordinate* or *gauge*.

There is no $G$-equivariant section $G/H\to G$ unless $H$ is trivial. Indeed, if $s$ were such a section and $s(H)=g_0$, then equivariance would give $s(hH)=h g_0=s(H)=g_0$ for every $h\in H$, hence $h g_0=g_0$ and $h=e$ for all $h\in H$. Set-theoretic sections exist — choose a representative in each coset — but no natural one does. This is the precise content of the "framework failure" (N2) in the corpus: the concept is an unordered pair, while ordering it is a $\mathbb{Z}/2$-torsor, and a name requires a local section. The atlas language in the corpus is the same idea: local charts exist, but there is no global chart.

Two torsors live in this theorem. The total space of framed bivaluations is a $G$-torsor; the fibre of the projection is an $H$-torsor. The quotient $G/H$ is not the torsor; it is the base. The sentence "$G\to G/H$ is an $H$-torsor" means that the map is a principal $H$-bundle and its fibres are $H$-torsors.

For a Lie group the frame torsor may be equipped with a connection, but over an arbitrary field there is no canonical connection. A coordinate in $H$ requires a reference lift or a local section. This is the same statement as "the frame has no canonical origin," translated into differential geometry.

### The resolution torsor: a smoothing without a canonical choice

Consider a nodal through-crossing written as a cospan

$$
F_-\xrightarrow{\ \pi_-\ }F_0\xleftarrow{\ \pi_+\ }F_+ ,
$$

with through relation $R_c=F_-\times_{F_0}F_+$. A *resolution* chooses, for each point of the critical fibre, which smooth point on the negative side is joined to which smooth point on the positive side. The set $\operatorname{Res}(R_c)$ of resolutions is a torsor under the monodromy group generated by the vanishing transvection:

$$
\operatorname{Res}(R_c)\ \text{is a torsor under}\ \langle T_\delta\rangle\cong\mathbb{Z}.
$$

Any two resolutions differ by a power of the transvection, and no resolution is singled out by the geometry of the cospan. Monodromy is the *difference* of two resolutions:

$$
\bigl(P^{\downarrow}\bigr)^{-1}P^{\uparrow}=T_\delta .
$$

A single resolution determines nothing, because the torsor has no origin. This is the precise sense in which the monodromy operators are not intrinsic to a single fibre.

The finite model replaces the infinite cyclic torsor by a cyclic quotient; the group changes, but the shape does not. The affine instance is a torsor under $\mathbb{R}_{>0}$, not under $\mathbb{Z}$; it calibrates the shape without identifying the objects. The heading "Why the torsor language is not decoration" in Paper V makes the point: the absence of a canonical origin is not a rhetorical flourish, but the reason monodromy cannot be read off from one fibre.

Again, the set of resolutions is nonempty. Choosing one gives an isomorphism with $\mathbb{Z}$. The choice is the mathematical content, not a defect.

### The parabolic torsor: when the invariant vanishes

In $\operatorname{Aff}^+(1,\mathbb{R})$, write $D_\Phi(z)=\Phi z$ and $T_c(z)=z+c$. Then

$$
D_\Phi T_c D_\Phi^{-1}=T_{\Phi c}.
$$

The conjugacy class of a nontrivial translation $T_c$ of a fixed sign is

$$
\{T_{\Phi c}:\Phi>0\},
$$

a torsor under the dilations $\mathbb{R}_{>0}$. The stabilizer is the translation subgroup, and the orbit carries no continuous invariant; only the sign survives. Over $\mathbb{F}_q$ with $q$ odd, the class is a torsor under $\mathbb{F}_q^\times\cong\mathbb{Z}/(q-1)$, and there are exactly two sign classes. The shape is field-independent; only the group and its cardinality change.

This is the parabolic layer $\ell=0$: the continuous invariant (length) vanishes, and the torsor takes over. The corpus's phrase is apt: the layer is not empty; it is the layer in which the only datum is the choice of conjugate. The torsor is not a failed invariant; it is what remains when the invariant has nothing left to say.

### Cosets, basepoints, and groupoids

In the affine group over $\mathbb{F}_q$, the translation subgroup $[G,G]$ acts simply transitively on $\mathbb{F}_q$: no nonzero translation has a fixed point, and translations are transitive. Hence $\mathbb{F}_q$ is a $[G,G]$-torsor. A coset $wK_{\mathrm{op}}$ is a $K_{\mathrm{op}}$-torsor; a coset $gH$ is an $H$-torsor. A coset has no canonical basepoint. The corpus's sentence is exact:

> A torsor is a group only after choosing a point; the choice is not canonical.

This is also why the transformation group on the fibres is a groupoid rather than a group. Conjugation gives an outer action $BG\to B\,\mathrm{Out}(K_{\mathrm{op}})$; a strict action would require a splitting of the extension, i.e. a section, and no such splitting exists in the finite case. The outer action and the missing basepoint are two languages for the same obstruction.

### Norm fibres: a family of finite torsors

Over $\mathbb{F}_7$, the norm $N:\mathbb{F}_{49}\to\mathbb{F}_7$ has fibres

$$
N^{-1}(0)=\{0\},\qquad N^{-1}(a)\cong C\quad(a\in\mathbb{F}_7^\times),
$$

where $C$ is an $8$-point conic. Each nonzero fibre is a $G$-torsor under

$$
G=SO_2(\mathbb{F}_7)\cong\mathbb{Z}/8,\qquad z\longmapsto \alpha^k z.
$$

The decomposition is a torsor decomposition, not a canonical group product: the exact sequence

$$
1\longrightarrow\mathbb{Z}/8\longrightarrow\mathbb{F}_{49}^\times\longrightarrow\mathbb{F}_7^\times\longrightarrow1
$$

does not split, and choosing a basepoint in each fibre is a noncanonical section. This is a family of torsors: each fibre is trivial as an abstract torsor, but there is no consistent global choice. It is a finite analogue of polar coordinates — radius and angle, but no canonical angle zero.

### The pendulum: a basepoint correction

The pendulum note records the addition law

$$
P(t_1)\oplus P(t_2)=P(t_1+t_2)\oplus P(0).
$$

The group law on the carrier is defined only after choosing the basepoint $P(0)$. The lifted clock $t$ has a group structure, while the geometric action retains only $[t]$ modulo the period lattice; the period group is the kernel of the projection from lifted clocks to geometric actions. The correction term is the basepoint. This is the affine-space pattern again: a group law on a homogeneous object needs a marked origin. The note calls it a "base-point/torsor correction"; the structure is the same even though the setting is not a principal bundle.

## What the corpus usages have in common

These are not metaphors. In each of the first six rows the set is literally a torsor under the named group; the pendulum row is the same basepoint pattern in a group-law computation.

The rows of the table play five recurring roles:

1. **Fibre role.** A principal bundle has a base with points and fibres without canonical points. The frame torsor, the coset torsor, and the norm-fibre torsor are fibres. The total space may be a torsor too, but under a different group and over a different base.
2. **Choice role.** A construction needs a choice — a third point, a resolution, an ordering, a representative — and the set of choices is a torsor. The choice is the mathematical content, not an embarrassment.
3. **Orbit role.** A conjugacy class or orbit under a group action is a torsor when the action is free and transitive. The parabolic torsor is an orbit; the invariant labels the orbit, not the point.
4. **Diagnostic role.** When an invariant degenerates, the remaining structure is often a torsor. The parabolic layer $\ell=0$ is the model case: the length disappears, and the choice of conjugate remains.
5. **Groupoid role.** If a basepoint is needed to turn a fibre into a group, automorphisms are only defined up to conjugation; the structure is a groupoid or an outer action. The coset example is the model case.

The common checklist is short. A set $X$ is a $G$-torsor when:

- $G$ acts on $X$;
- the action is free;
- the action is transitive;
- $X$ is nonempty.

Then $X$ is isomorphic to $G$, but not canonically. To use the isomorphism, choose a point; to compare two choices, use the unique group element between them; to compare two points, use the difference; never add points without a basepoint.

## Torsion, tearing, and the observer's hole

The AEG and Adva uses of "invisible difference" meet at the torsor, but the meeting is precise and involves two different senses of "free." In AEG, the free object is the free product of additive and scaling histories; in a torsor, "free" refers to the action. Keeping these apart makes the bridge exact.

### The charge fibre is a torsor

In Paper 0 §8 the history group is the free product

$$
G=(\mathbb{R},+)*(\mathbb{R},+),
$$

with generators the additive steps $\mathsf A_p$ and the scaling steps $\mathsf M_q$. The charge map

$$
c:G\longrightarrow\mathbb{R}^2,\qquad \mathsf A_p\mapsto(p,0),\quad \mathsf M_q\mapsto(0,q)
$$

is the abelianization of $G$: `prop:p0-acs-is-abelianization` proves

$$
\ker c=[G,G].
$$

Fix a charge $b\in\mathbb{R}^2$ and choose a history $\gamma$ with $c(\gamma)=b$. Then the fibre is the right coset

$$
c^{-1}(b)=\gamma[G,G].
$$

The subgroup $[G,G]$ acts on this coset by left multiplication. The action is free: if $h\gamma h'=\gamma h'$, then $h\gamma=\gamma$, so $h=e$. It is transitive: given $\gamma h_1$ and $\gamma h_2$, the element $h=\gamma h_2h_1^{-1}\gamma^{-1}$ lies in $[G,G]$ because $[G,G]$ is normal, and $h\gamma h_1=\gamma h_2$. Hence **each charge fibre is a $[G,G]$-torsor**. This is a direct reading of the abelianization proposition; the paper does not use the word "torsor" here, but the structure is immediate.

The relative torsion of two histories in the same fibre is

$$
\tau(\gamma,\delta)=\xi_\gamma-\xi_\delta,
$$

the difference of their target-frame translations. The underlying torsor difference is the group element $\gamma^{-1}\delta\in[G,G]$; $\tau$ is one coordinate of the affine difference between the two evaluations. Tearing is the geometric name for this relative torsion: same linear part, different additive content. `prop:p0-characters-cannot-see-tearing` makes the observer statement exact: every function of the charge endpoint is constant on the fibre, while $\tau$ need not vanish. The observer sees the base $b$, not the torsor fibre over it. This is the AEG form of "the finite observer cannot see the difference" — the difference is the hole.

Two caveats. The "free" in $G$ is a free product, not a free group; the paper explicitly refuses to identify the history space with a free group without chosen generators and relations. And "torsion" here is relative arithmetic torsion, not group-theoretic torsion; it lives in the commutator subgroup $[G,G]$, which is exactly what the abelianization forgets.

### The hole is a filling fibre

Adva's finite observer is a bounded, versioned observation policy $Q$; it sees a quotient $q(h)$, not the history $h$, and a global finite observer need not exist (`0037` §5.14). The residual is not nothing. The typed-hole note `0079` states the shape:

> The hole is syntactically empty and semantically a family.

A hole is a filling fibre: the open bracket is the aperture, and the admissible fillings are the family. A torsor is the case where the forgotten differences form a group acting freely and transitively on that family. In that sense, **every torsor is a hole, but not every hole is a torsor**: if the stabilizer is nontrivial the family is a homogeneous space, and if there is no group action it is just a fibre.

The through-form note `0070` gives a literal instance. The unmarked relation $\langle F_-\mid_N F_+\rangle$ is the carrier of all marked resolutions; a chosen resolution selects one graph inside it. The set of resolutions is a torsor under the monodromy group $\langle T_\delta\rangle\cong\mathbb{Z}$ (Paper V §8). The observer who does not choose sees the relation, i.e. the hole; the observer who chooses sees a function. The singularity does not erase the ambiguity; it changes its representation into a node plus its resolution fibre.

The surreal tear note `0223` gives the cleanest value/presentation example. The state $q$ is the value of a form, and the presentation-day clock is $c_2$. The order clock descends to the value; the day clock does not. The witness is

$$
q(\ \mid\ )=q(\ \mid 1)=0,\qquad \mathrm{day}(\ \mid\ )=0,\quad \mathrm{day}(\ \mid 1)=2.
$$

There is a canonical section for surreal numbers — choose the simplest presentation — and it makes the day a function of the value; the tear is harmless there. AES has no such canonical section, so the defect is carried. This is the same dichotomy, in a different guise, as a torsor with a canonical trivialization versus one without: a section exists or it does not, and the tear is the witness that the chosen section is not canonical. `0021` adds the naturality failure: objectification chooses the simplest form, but the choice does not commute with scaling; the ordered holes and the surgery history are the residual. The pattern is the frame torsor's: set-theoretic sections exist, no equivariant section does.

### Two directions of invisibility

There is a second, opposite sense in which a finite observer "cannot see the hole." The frame analysis in `concept-ideal-point-naming` §7 states it:

> Visible $\leftrightarrow$ needs a frame; invisible $\leftrightarrow$ needs no frame.

The ordered carrier counts split concepts twice, because ordering the two points is a $\mathbb{Z}/2$-torsor; it misses non-split concepts entirely, because Frobenius swaps the two points and no ordering is available. Here the torsor is the visible side — the thing that needs a frame — and the hole is the canonical object that needs no frame. Visibility is not the same as canonicity.

Thus the corpus has two dual configurations:

1. **Base observer.** The observer sees the quotient and misses the fibre. The torsor is the invisible fibre: AEG's charge fibre, the resolution relation of `0047`/`0070`, the filling family of `0079`.
2. **Framed carrier.** The carrier sees the torsor (the need for a frame) and misses the canonical object: the ordered bivaluation carrier sees split concepts twice and non-split concepts not at all.

The same torsor can sit on either side of the visibility cut. Which side depends on what the observer's state space is, not on the torsor alone.

### Summary

**A torsor is the shape of a hole when the forgotten differences form a free transitive group action. The group element between two points of the fibre is the torsor difference; tearing is its geometric measure, and arithmetic torsion is its translation-coordinate shadow in the commutative quotient.**

The bridge is exact in the AEG charge fibre and in the resolution fibre. In the surreal and frame examples it is a structural reading: the same dichotomy between a canonical section and a noncanonical one, rather than a claim that every presentation fibre is a group torsor.

## Common confusions

**A torsor is not a group.** It becomes a group only after a point is chosen, and the group law depends on the point. The ternary difference is canonical; the binary sum is not.

**A torsor is not a homogeneous space.** $G/H$ has a canonical point $H$ and is a homogeneous space. It is a $G$-torsor only when $H$ is trivial. The fibre of $G\to G/H$ is an $H$-torsor; the quotient is the base.

**A torsor over a point is not the same as a torsor over a base.** Every nonempty torsor over a point is trivial as an abstract torsor; it may still have no canonical trivialization. A torsor over a base may have no global section at all. The corpus's "no origin" usually means the former; "no section" may mean the latter.

**No equivariant section is not the same as no section.** In the frame case, set-theoretic sections exist; no $G$-equivariant section does. The obstruction is naturality, not existence.

**A torsor is not torsion.** "Torsion" in group theory refers to elements of finite order, and the corpus also uses "torsion" for the commutator subgroup $[G,G]$. A torsor is a different notion: a free transitive action without a basepoint. The sentence "torsion is the basepoint-free part" is a local identification in the affine group, not a general definition. In the AEG charge fibre, the fibre is a $[G,G]$-torsor, but the relative torsion is a difference between two of its points, not the fibre itself.

**The group is part of the data.** The affine instance is a torsor under $\mathbb{R}_{>0}$, not under $\mathbb{Z}$; the resolution torsor is under $\mathbb{Z}$. The same shape with a different group is a different torsor. Always ask: which group acts, and over what base?

**"Noncanonical" does not mean "arbitrary."** The set of choices is itself a torsor, with a precise group action. A different choice changes the computation by a unique group element; that element is the interesting invariant.

## A practical checklist

- **To prove** that $X$ is a $G$-torsor: define the action, prove it is free, prove it is transitive, and prove $X$ is nonempty.
- **To compute** with a torsor: choose a point, do the computation in $G$, and record how the answer changes when the point changes. The change is an element of $G$.
- **To compare** two points: use the difference $y-x\in G$. Do not add points unless a basepoint has been chosen.
- **To trivialize** a torsor over a base: look for a global section. If none exists, the torsor is nontrivial in the strong sense; if one exists but is not natural, the torsor is trivial but not canonically trivialized.
- **To classify** torsors over a base: use $H^1(B,G)$; a torsor is a 1-cocycle, a trivialization is a coboundary.
- **To read the corpus**: identify the group, the base, and the fibre; distinguish the total space from the fibre; ask whether the section is set-theoretic or equivariant.

## See also

- [Principal homogeneous space](https://en.wikipedia.org/wiki/Principal_homogeneous_space)
- [Principal bundle](https://en.wikipedia.org/wiki/Principal_bundle)
- [Homogeneous space](https://en.wikipedia.org/wiki/Homogeneous_space)
- [Heap (mathematics)](https://en.wikipedia.org/wiki/Heap_(mathematics))
- [Groupoid](https://en.wikipedia.org/wiki/Groupoid)
- [Nonabelian cohomology](https://en.wikipedia.org/wiki/Nonabelian_cohomology)
- [Gauge theory](https://en.wikipedia.org/wiki/Gauge_theory)
- [Affine space](https://en.wikipedia.org/wiki/Affine_space)
- [Frame bundle](https://en.wikipedia.org/wiki/Frame_bundle)

## References

### Standard references

1. [Principal homogeneous space](https://en.wikipedia.org/wiki/Principal_homogeneous_space), Wikipedia.
2. [Torsor](https://ncatlab.org/nlab/show/torsor), nLab.
3. [Torsors made easy](https://math.ucr.edu/home/baez/torsors.html), John Baez.
4. [Definition 39.11.1 (0498)](https://stacks.math.columbia.edu/tag/0498), The Stacks Project.
5. [主齐性空间](https://zh.wikipedia.org/wiki/%E4%B8%BB%E9%BD%90%E6%80%A7%E7%A9%BA%E9%97%B4), 维基百科.

### Corpus sources

The line references are to the commits named below.

- **aeg-paper** `402e0e7`
  - [`paper-4/sections/03-projective-quotients.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/paper-4/sections/03-projective-quotients.tex#L138-L160), `thm:frame-torsor` and the frame discussion.
  - [`paper-5/sections/08-through-crossings.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/paper-5/sections/08-through-crossings.tex#L33-L97), `def:resolution-torsor`, `thm:monodromy-difference`, and the affine instance.
  - [`paper-0/sections/03-aes-and-motion.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/paper-0/sections/03-aes-and-motion.tex#L745-L805), `prop:p0-affine-two-layers`.
  - [`notes/analysis-and-calculus/48-finite-field-trigonometry.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/notes/analysis-and-calculus/48-finite-field-trigonometry.tex#L180-L190), norm fibres as torsors.
  - [`paper-4/sections/04-condensation-and-continuation.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/paper-4/sections/04-condensation-and-continuation.tex#L40-L140), continuation and the normalizer criterion.
  - [`paper-0/sections/08-acs-tearing.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/paper-0/sections/08-acs-tearing.tex#L142-L340), `conv:p0-history-group`, `prop:p0-acs-is-abelianization`, and `def:relative-torsion`.
  - [`paper-0/sections/08-acs-tearing.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/paper-0/sections/08-acs-tearing.tex#L593-L649), `def:p0-tearing`.
  - [`paper-0/sections/10-beyond-linear.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/paper-0/sections/10-beyond-linear.tex#L132-L150), `prop:p0-characters-cannot-see-tearing`.
- **pcrg-paper** `c59ab6f`
  - [`references/developing/09-capacity-layers-and-the-torsor.md`](https://github.com/mountain/pcrg-paper/blob/c59ab6f/references/developing/09-capacity-layers-and-the-torsor.md#L30-L48), the torsor layer.
  - [`references/developing/10-the-trichotomy-and-what-changes-over-fq.md`](https://github.com/mountain/pcrg-paper/blob/c59ab6f/references/developing/10-the-trichotomy-and-what-changes-over-fq.md#L30-L45), the finite-field torsor.
  - [`notes/2026-10-11-descent-proposition.md`](https://github.com/mountain/pcrg-paper/blob/c59ab6f/notes/2026-10-11-descent-proposition.md#L71-L90), the third point and the no-equivariant-section proof.
  - [`notes/2026-10-11-concept-ideal-point-naming.md`](https://github.com/mountain/pcrg-paper/blob/c59ab6f/notes/2026-10-11-concept-ideal-point-naming.md#L690-L750), cosets, basepoints, and groupoids.
  - [`notes/2026-10-11-concept-ideal-point-naming.md`](https://github.com/mountain/pcrg-paper/blob/c59ab6f/notes/2026-10-11-concept-ideal-point-naming.md#L225-L270), ordering as a $\mathbb{Z}/2$-torsor.
  - [`notes/2026-10-11-concept-ideal-point-naming.md`](https://github.com/mountain/pcrg-paper/blob/c59ab6f/notes/2026-10-11-concept-ideal-point-naming.md#L278-L353), visibility versus the need for a frame.
  - [`notes/2026-10-12-operator-kernel-transformation-groupoid-witness.py`](https://github.com/mountain/pcrg-paper/blob/c59ab6f/notes/2026-10-12-operator-kernel-transformation-groupoid-witness.py#L108-L120), the executable witness.
- **process-geometry** `c47c96f`
  - [`docs/54-pendulum-elliptic-group-rank-lowering.md`](https://github.com/mountain/process-geometry/blob/c47c96f/docs/54-pendulum-elliptic-group-rank-lowering.md#L30-L40), the basepoint/torsor correction.
- **adva** `17e1842a`
  - [`docs/research/0047-a1-nodal-through-crossing-geometry.md`](https://github.com/mountain/adva/blob/17e1842a/docs/research/0047-a1-nodal-through-crossing-geometry.md#L670-L710), phase torsor.
  - [`docs/research/0048-cellular-annulus-nodal-torus-dehn-twist.md`](https://github.com/mountain/adva/blob/17e1842a/docs/research/0048-cellular-annulus-nodal-torus-dehn-twist.md#L438-L450), the infinite cyclic torsor.
  - [`docs/research/0223-surreal-order-and-the-tear.md`](https://github.com/mountain/adva/blob/17e1842a/docs/research/0223-surreal-order-and-the-tear.md#L1-L110), the value/presentation-day tear and the canonical-section reading.
- **adva-machine** `51ee989`
  - [`docs/research/0079-typed-hole-open-close-calibration-v0.md`](https://github.com/mountain/adva-machine/blob/51ee989/docs/research/0079-typed-hole-open-close-calibration-v0.md#L15-L40), the hole as a filling fibre; see also [the one-sentence form](https://github.com/mountain/adva-machine/blob/51ee989/docs/research/0079-typed-hole-open-close-calibration-v0.md#L157-L167).
  - [`docs/research/0070-typed-surreal-through-forms.md`](https://github.com/mountain/adva-machine/blob/51ee989/docs/research/0070-typed-surreal-through-forms.md#L300-L325), the unmarked through relation and its resolution fibre.
  - [`docs/research/0021-surreal-cut-objectification-no-go.md`](https://github.com/mountain/adva-machine/blob/51ee989/docs/research/0021-surreal-cut-objectification-no-go.md#L26-L50), non-injective and non-natural objectification.
  - [`docs/research/0037-finite-observer-tricusp-surreal-reduction.md`](https://github.com/mountain/adva-machine/blob/51ee989/docs/research/0037-finite-observer-tricusp-surreal-reduction.md#L1040-L1060), the finite observer and the failure of a global section.

# 挠子（Torsor）

在数学中，群 $G$ 的**挠子**（torsor），又称**主齐性空间**（principal homogeneous space），是一个带有 $G$ 作用的集合 $X$，并且这个作用是自由且传递的。只要选定一个点，$X$ 就与 $G$ 完全同构；但“选哪个点”并不在数据之中。因此，挠子可以理解为“忘了单位元的群”，或者“没有零刻度的尺子”：两点可以比较——它们的差是 $G$ 的一个元素——但在选定参照点之前，不能相加，也不能说哪一点是原点。这个选择不是典范的，而“所有可能的选择”本身构成一个挠子。

最直观的图景是一个没有标出 12 点的钟面。群 $\mathbb{Z}/12\mathbb{Z}$ 让表盘旋转；任意两个位置之间都有唯一的旋转把一个送到另一个，所以作用是自由且传递的。我们可以说两个位置相差四小时，但在决定 12 点在哪里之前，不能说某个位置是“三点钟”。选定 12 点就是一次**平凡化**；换一个 12 点，所有标签都整体旋转。这个表盘就是一个 $\mathbb{Z}/12\mathbb{Z}$-挠子。

挠子在代数、几何、拓扑、算术和规范场论中都很基本。在 AEG/Adva 语料里，它同样以多种面貌出现：“框架挠子”“消解挠子”“抛物挠子”“挠子分解”看起来不同，但共享同一个结构：自由且传递的群作用，加上一个不典范的基点。

## 定义

设 $G$ 是群，$X$ 是非空集合，带有左作用

$$
G\times X\longrightarrow X,\qquad (g,x)\longmapsto g\cdot x .
$$

若 $g\cdot x=x$ 对某个 $x$ 成立就推出 $g=e$，则称作用是**自由**的；等价地，每个稳定子都是平凡的。若对任意 $x,y\in X$ 都存在 $g\in G$ 使 $g\cdot x=y$，则称作用是**传递**的。一个**$G$-挠子**就是作用自由且传递的非空 $G$-集合。等价地，对每个 $x\in X$，映射

$$
G\longrightarrow X,\qquad g\longmapsto g\cdot x
$$

都是双射。两个 $G$-挠子之间的态射就是 $G$-等变双射；任何这样的态射都是同构。

选定 $x_0\in X$ 给出双射 $\varphi_{x_0}:G\to X$，$g\mapsto g\cdot x_0$。若 $x_1=h\cdot x_0$ 是另一点，则

$$
\varphi_{x_1}(g)=g\cdot h\cdot x_0=\varphi_{x_0}(gh),
$$

所以两次平凡化相差一个右乘 $h$。在这个意义上，挠子是“单位元被忘掉”的群：一个点可以把单位元找回来，但找回来的方式依赖这个点。

挠子上典范的运算不是加法，而是**差**。对 $x,y\in X$，存在唯一的 $g\in G$ 使 $g\cdot x=y$；用加法记号写成 $g=y-x$。这个差不依赖任何基点。加法则需要基点：选定 $x_0$ 后，可以定义

$$
x+_{x_0}y=x_0+(x-x_0)+(y-x_0),
$$

但换一个 $x_0$，加法就变了。用仿射几何的话说：仿射空间的点可以相减，但在选定原点之前不能相加。代数上，同样的结构叫作**堆**（heap）：一个带有三元运算 $[x,y,z]=x-y+z$ 的集合，它不需要选定单位元就能推广群律。

### 平凡、非典范与非平凡

若一个 $G$-挠子与带左作用的 $G$ 同构，则称它是**平凡**的。$X$ 中的一个点就是一次平凡化，所以“点上的挠子”作为抽象挠子总是平凡的：它按定义非空，任取一点就给出与 $G$ 的同构。可能失效的是**典范**的平凡化。这个区别是许多混淆的根源：

> 点上的挠子总是有点。问题不是存在性，而是典范性。

底空间 $B$ 上的 $G$-挠子是一族 $G$-挠子，每个 $B$ 的点上有一根纤维。若它有一个整体截面，即每一根纤维中一致地选出一个点，则它是平凡的。局部截面由局部平凡性保证存在，但整体截面可能不存在。这时挠子在更强的意义下非平凡：不是“没有典范的点”，而是“没有整体点（整体截面）”，尽管每根纤维都有点。对于景上的群层 $G$，$B$ 上 $G$-挠子的同构类由非交换上同调集 $H^1(B,G)$ 分类；挠子就是 1-余循环，平凡化就是上边缘。

语料里大多数时候说的是第一种失效：选择集非空，但没有典范选择。例如，穿越的消解集合非空；选定一个消解后，它与 $\mathbb{Z}$ 同构；要点在于“选哪一个”就是数学内容，而不是消解不存在。在框架情形中，$G\to G/H$ 的集合论截面存在；不存在的只是 $G$-等变截面。这是自然性障碍，不是存在性障碍。

## 挠子、齐性空间与主丛

设 $H\le G$。商 $G/H$ 是一个左 $G$-集合，并且有一个典范点，即陪集 $H$。它是**齐性空间**。只有当 $H$ 平凡时，它才是 $G$-挠子，因为 $H$ 的稳定子正是 $H$。投影

$$
\pi:G\longrightarrow G/H
$$

是主 $H$-丛；每根纤维 $\pi^{-1}(x)$ 在右乘作用下是一个 $H$-挠子。语料中的句子“$G\to G/H$ 是 $H$-挠子”是这句话的简写：映射是主 $H$-丛，它的纤维是 $H$-挠子。商 $G/H$ 本身不是 $H$-挠子；它是底空间。

更一般地，**底空间 $B$ 上的 $G$-挠子**就是主 $G$-丛 $P\to B$；每根纤维是一个 $G$-挠子。点上的 $G$-挠子就是单根纤维。$P\to B$ 的整体截面把丛平凡化；局部截面就是局部平凡化，或者说规范选择。联络是额外的数据，用来比较邻近的纤维；它不属于挠子结构本身。对 Lie 群，挠子上可以赋予联络；在任意域上则没有典范联络。

同一个定理里可以同时出现两个不同的挠子。下面的框架定理中，带框架的赋值整体空间是 $G$-挠子，而投影到无框架赋值的纤维是 $H$-挠子。把“群”和“底空间”分清，是理解这类陈述的一半。

## 为什么挠子无处不在

许多分类问题问的是“在空间上选一个结构”，而所有结构的集合往往就是一个挠子。$GL_n$-挠子就是秩 $n$ 向量丛的标架丛；$O_n$-挠子就是二次结构；$\mathbb{G}_m$-挠子就是去掉零截面的线丛；$\mathbb{Z}/2$-挠子就是二点集，或底空间上的二重覆盖，定向是二点集的例子；$PGL_2$-挠子就是圆锥曲线，即一维 Severi–Brauer 簇；更一般地，$PGL_{n+1}$-挠子是 $n$ 维 Severi–Brauer 簇。在拓扑中，$H^1(B,G)$ 分类 $G$-挠子；在规范场论中，规范场是主 $G$-丛上的联络，规范选择是局部截面。

用范畴的语言说，$G$-挠子 $X$ 的作用群胚 $X/\!/G$ 是一个连通的群胚，等价于 $BG$，即 $G$ 的单对象群胚。选定 $X/\!/G$ 的一个对象就给出这个等价；没有选定对象时，它虽然等价于 $BG$，却没有典范的基点。挠子的“没有典范单位元”，和这个群胚的“没有典范对象”，是同一句话。

## 例子

### 仿射空间：没有零点的尺子

设 $V$ 是向量空间，$A$ 是一个带有 $V$ 平移作用的集合，作用是单可迁的。那么 $A$ 是仿射空间，$A$ 是 $V$-挠子。两点的差 $y-x$ 是向量；和 $x+y$ 没有定义。选定原点 $0\in A$ 后，$A\cong V$，可以相对 $0$ 定义 $x+y$；把原点换成 $a$，和就整体改变 $a$。向量空间就是带典范原点的仿射空间；它是带首选点的平凡 $V$-挠子。

线性方程组的解集是最干净的代数例子。若 $Ax=b$ 有解，解集是 $\ker A$ 的挠子：核通过平移作用，自由且传递，两个解的差落在核里。若 $b=0$，零向量是典范解，解集是群。若 $b\ne0$，没有典范解，解集是非平凡的仿射挠子。

### 基、定向与同构

设 $V$ 是 $n$ 维向量空间。$V$ 的有序基集合是 $GL(V)$-挠子：$GL(V)$ 单可迁地作用，选定一组参照基就给出与 $GL(V)$ 的同构。对正维数实向量空间，定向集合是 $\mathbb{Z}/2$-挠子：只有两个定向，没有典范的那一个；选定一个就把集合等同于 $\mathbb{Z}/2$。两个向量空间之间的同构集合也是 $GL(V)$-挠子。

### 框架与规范选择

向量丛的标架丛是底空间上的 $GL_n$-挠子；一个标架就是局部截面。在规范场论中，时空上的主 $G$-丛是时空上的 $G$-挠子；一个规范就是局部截面，规范变换就是截面的改变。联络是平行移动的规则，不是截面的选择。语料中的框架挠子，正是射影框架版本的这种对象。

## AEG/Adva 语料中的挠子

语料在多种场景中使用这个词。下表是一张地图，后面的小节逐行解释。

| 语料中的名称 | 挠子 | 作用群 | 没有典范选择的东西 | 出处 |
| --- | --- | --- | --- | --- |
| 框架挠子 | 有序对之上的第三个射影点 | $H=\operatorname{Stab}_G(q^+,q^-)$ | 第三点，即框架 | Paper IV，`thm:frame-torsor` |
| 消解挠子 | 节点穿越的消解 | $\langle T_\delta\rangle\cong\mathbb{Z}$ | 选哪一个光滑化/消解 | Paper V，§8 |
| 抛物挠子 | 固定符号的非平凡平移的共轭类 | $\mathbb{R}_{>0}$ 或 $\mathbb{F}_q^\times$ | 类的代表元 | Paper 0，`prop:p0-affine-two-layers` |
| 陪集挠子 | 陪集 $wK_{\mathrm{op}}$ 或 $gH$ | $K_{\mathrm{op}}$ 或 $H$ | 陪集的基点 | `concept-ideal-point-naming`，§9.8 |
| 范数纤维挠子 | 非零范数纤维（8 点圆锥曲线） | $SO_2(\mathbb{F}_7)\cong\mathbb{Z}/8$ | 角度基点 | `48-finite-field-trigonometry` |
| 排序挠子 | 无序对的两种排序 | $\mathbb{Z}/2$ | 哪个点在前 | `concept-ideal-point-naming`，§5.3 |
| 基点修正 | 摆的载体点 | 周期格 / 时钟群 | 基点 $P(0)$ | `54-pendulum-elliptic-group-rank-lowering` |

### 框架挠子：第三个射影点

设 $K$ 是域，$G=PGL_2(K)$，$H$ 是有序不同点对 $(q^+,q^-)$ 的稳定子，其中 $q^\pm\in\mathbb{P}^1(K)$。正则赋值（bivaluation）是有序的不同射影点对，等价于 $K^2$ 上的秩一幂等元。前两个点决定投影子；第三个点 $q^\infty$ 在它上面选出一个射影框架：

$$
(q^+,q^-,q^\infty)\longmapsto(q^+,q^-).
$$

定理 `thm:frame-torsor` 说：带框架的正则赋值集合是 $G$-挠子；一个参照三元组就是它的一个点，所以定理中“选定一个参照三元组之后”正是平凡化这一步。投影的纤维上，$H$ 自由且传递地作用。等价地，$G\to G/H$ 是 $H$-挠子。

在 $\mathbb{F}_q$ 上，数字是明确的：

$$
\lvert G\rvert=q(q^2-1),\qquad
\lvert G/H\rvert=q(q+1),\qquad
\lvert H\rvert=q-1.
$$

有序对之上的纤维就是允许的第三点集合，大小 $q-1=|H|$；$H$ 在其上单可迁地作用。第三点就是框架：前两个点决定**概念**，第三个点选择**坐标**或**规范**。

除非 $H$ 平凡，否则不存在 $G$-等变截面 $G/H\to G$。证明很短：若 $s$ 是这样的截面且 $s(H)=g_0$，则等变性给出 $s(hH)=h g_0=s(H)=g_0$ 对一切 $h\in H$ 成立，于是 $h g_0=g_0$，从而 $h=e$ 对一切 $h\in H$ 成立。集合论截面是存在的——在每个陪集里选一个代表元即可——但没有自然的截面。这正是语料中“框架失败”（N2）的精确内容：概念是无序对，而给它排序是一个 $\mathbb{Z}/2$-挠子；命名需要一个局部截面。语料里的 atlas 语言说的是同一件事：局部 chart 存在，但没有整体 chart。

这个定理里有两个挠子。带框架赋值的整个集合是 $G$-挠子；投影的纤维是 $H$-挠子。商 $G/H$ 不是挠子；它是底空间。“$G\to G/H$ 是 $H$-挠子”的意思是：映射是主 $H$-丛，它的纤维是 $H$-挠子。

对 Lie 群，框架挠子可以赋予联络；在任意域上则没有典范联络。$H$-坐标需要一个参照提升或局部截面。这与“框架没有典范原点”是同一句话的微分几何版本。

### 消解挠子：没有典范光滑化

把节点穿越写成余跨（cospan）

$$
F_-\xrightarrow{\ \pi_-\ }F_0\xleftarrow{\ \pi_+\ }F_+ ,
$$

其穿越关系为 $R_c=F_-\times_{F_0}F_+$。一个**消解**对临界纤维的每个点，选择负侧哪一个光滑点与正侧哪一个光滑点相连。消解集合 $\operatorname{Res}(R_c)$ 是单值群 $\langle T_\delta\rangle\cong\mathbb{Z}$ 下的挠子，其中 $T_\delta$ 是消没平延（vanishing transvection）：

$$
\operatorname{Res}(R_c)\ \text{is a torsor under}\ \langle T_\delta\rangle\cong\mathbb{Z}.
$$

任意两个消解相差一个消没平延的幂，而余跨的几何不挑出任何一个消解。单值性（monodromy）是两个消解之**差**：

$$
\bigl(P^{\downarrow}\bigr)^{-1}P^{\uparrow}=T_\delta .
$$

单个消解不决定任何东西，因为挠子没有原点。这就是“单值算子并不内在于单根纤维”的精确含义。

有限模型把无限循环挠子换成循环商；群变了，形状没变。仿射实例是 $\mathbb{R}_{>0}$ 下的挠子，而不是 $\mathbb{Z}$ 下的挠子；它校准的是形状，不是对象之间的等同。Paper V 中“为什么挠子语言不是装饰”这一标题说的正是：没有典范原点不是修辞，而是单值不能从单根纤维读出的原因。

再说一次，消解集合非空。选定一个消解就给出与 $\mathbb{Z}$ 的同构。选择本身就是数学内容，不是缺陷。

### 抛物挠子：不变量消失之时

在 $\operatorname{Aff}^+(1,\mathbb{R})$ 中，记 $D_\Phi(z)=\Phi z$，$T_c(z)=z+c$。则

$$
D_\Phi T_c D_\Phi^{-1}=T_{\Phi c}.
$$

固定符号的非平凡平移 $T_c$ 的共轭类是

$$
\{T_{\Phi c}:\Phi>0\},
$$

它是伸缩群 $\mathbb{R}_{>0}$ 下的挠子。稳定子是平移子群，轨道不带任何连续不变量；只剩符号。在奇素 $q$ 的 $\mathbb{F}_q$ 上，这个类是 $\mathbb{F}_q^\times\cong\mathbb{Z}/(q-1)$ 下的挠子，并且恰好有两个符号类。形状与域无关；变的只是群及其基数。

这就是抛物层 $\ell=0$：连续不变量（长度）消失，挠子接管。语料的说法很贴切：这一层不是空层；它是“唯一的 datum 就是共轭元的选择”的那一层。挠子不是失败的不变量；它是不变量已经无话可说之后剩下的东西。

### 陪集、基点与群胚

在 $\mathbb{F}_q$ 上的仿射群中，平移子群 $[G,G]$ 单可迁地作用在 $\mathbb{F}_q$ 上：非零平移没有不动点，而平移整体是传递的。因此 $\mathbb{F}_q$ 是 $[G,G]$-挠子。陪集 $wK_{\mathrm{op}}$ 是 $K_{\mathrm{op}}$-挠子；陪集 $gH$ 是 $H$-挠子。陪集没有典范基点。语料中的句子是精确的：

> 挠子只有在选定一个点之后才是群；这个选择不是典范的。

这也解释了为什么纤维上的变换群是群胚而不是群。共轭给出外作用 $BG\to B\,\mathrm{Out}(K_{\mathrm{op}})$；严格的群作用需要扩张的分裂，也就是一个截面，而有限情形下这样的分裂不存在。外作用和缺失的基点，是同一个障碍的两种语言。

### 范数纤维：有限域上的一族挠子

在 $\mathbb{F}_7$ 上，范数 $N:\mathbb{F}_{49}\to\mathbb{F}_7$ 的纤维是

$$
N^{-1}(0)=\{0\},\qquad N^{-1}(a)\cong C\quad(a\in\mathbb{F}_7^\times),
$$

其中 $C$ 是 8 点圆锥曲线。每个非零纤维都是 $G$-挠子，作用是

$$
G=SO_2(\mathbb{F}_7)\cong\mathbb{Z}/8,\qquad z\longmapsto \alpha^k z.
$$

这个分解是挠子分解，不是典范的群直积：正合列

$$
1\longrightarrow\mathbb{Z}/8\longrightarrow\mathbb{F}_{49}^\times\longrightarrow\mathbb{F}_7^\times\longrightarrow1
$$

不分裂，而在每根纤维中选一个基点是一个不典范的截面。这是一族挠子：每根纤维作为抽象挠子都是平凡的，但没有一致的整体选择。它是极坐标的有限类比——有半径和角度，但没有典范的角度零点。

### 摆：基点修正

摆的笔记记下加法律

$$
P(t_1)\oplus P(t_2)=P(t_1+t_2)\oplus P(0).
$$

载体上的群律只有在选定基点 $P(0)$ 之后才有定义。提升的时钟 $t$ 有群结构，而几何作用只保留 $[t]$ 模周期格；周期群是“提升时钟到几何作用”的投影的核。修正项就是基点。这又是仿射空间的模式：齐性对象上的群律需要一个标出的原点。笔记称之为“基点/挠子修正”；尽管这里的场景不是主丛，结构是相同的。

## 这些用法的共同点

这些都不是比喻。前六行中的集合在字面意义上就是所指群下的挠子；摆的那一行是群律计算中同一个基点模式。

上表的各行扮演五种反复出现的角色：

1. **纤维角色。** 主丛的底空间有点，纤维没有典范点。框架挠子、陪集挠子、范数纤维挠子都是纤维。整体空间本身也可能是挠子，但那是在另一个群、另一个底空间之下。
2. **选择角色。** 一个构造需要选择——第三点、消解、排序、代表元——而选择集就是挠子。选择是数学内容，不是尴尬。
3. **轨道角色。** 群作用的共轭类或轨道，在作用自由且传递时就是挠子。抛物挠子是轨道；不变量标记的是轨道，不是点。
4. **诊断角色。** 当不变量退化时，剩下的结构往往是挠子。抛物层 $\ell=0$ 是模型情形：长度消失了，共轭元的选择留下了。
5. **群胚角色。** 如果必须选一个基点才能把纤维变成群，那么自同构只能在共轭意义下定义；结构就是群胚或外作用。陪集例子是模型情形。

共同的检查表很短。一个集合 $X$ 是 $G$-挠子，当且仅当：

- $G$ 作用在 $X$ 上；
- 作用自由；
- 作用传递；
- $X$ 非空。

于是 $X$ 与 $G$ 同构，但不是典范同构。要使用这个同构，就选一个点；要比较两个选择，就用它们之间唯一的群元素；要比较两个点，就用差；没有基点时，不要相加。

## 挠、撕裂与观察者的洞

AEG 与 Adva 的“看不见的差异”在挠子这里相遇，但相遇是精确的，而且涉及两个不同的“自由”。AEG 里自由的是加法史与乘法史的自由乘积；挠子里自由的是作用。把这两个 free 分开，桥才是精确的。

### 电荷纤维是挠子

Paper 0 §8 的 history group 是自由乘积

$$
G=(\mathbb{R},+)*(\mathbb{R},+),
$$

生成元是加法步 $\mathsf A_p$ 与乘法步 $\mathsf M_q$。电荷映射

$$
c:G\longrightarrow\mathbb{R}^2,\qquad \mathsf A_p\mapsto(p,0),\quad \mathsf M_q\mapsto(0,q)
$$

是 $G$ 的交换化：`prop:p0-acs-is-abelianization` 证明

$$
\ker c=[G,G].
$$

固定电荷 $b\in\mathbb{R}^2$，取历史 $\gamma$ 使 $c(\gamma)=b$。纤维是右陪集

$$
c^{-1}(b)=\gamma[G,G].
$$

子群 $[G,G]$ 通过左乘作用在这个陪集上。作用是自由的：若 $h\gamma h'=\gamma h'$，则 $h\gamma=\gamma$，故 $h=e$。作用是传递的：给定 $\gamma h_1$ 与 $\gamma h_2$，元素 $h=\gamma h_2h_1^{-1}\gamma^{-1}$ 落在 $[G,G]$ 中（因为 $[G,G]$ 正规），且 $h\gamma h_1=\gamma h_2$。所以**每根电荷纤维都是一个 $[G,G]$-挠子**。这是交换化命题的直接读法；论文没有在这里使用“挠子”一词，但结构是直接的。

同一根纤维中两个历史的相对算术挠率（relative arithmetic torsion）是

$$
\tau(\gamma,\delta)=\xi_\gamma-\xi_\delta,
$$

即两个目标框架平移项之差。底层的挠子差是群元素 $\gamma^{-1}\delta\in[G,G]$；$\tau$ 是两次求值之仿射差的一个坐标。tearing（撕裂）是这个相对挠率的几何名字：线性部分相同，加法内容不同。`prop:p0-characters-cannot-see-tearing` 把观察者陈述说得很精确：电荷端点的任意函数在纤维上是常数，而 $\tau$ 不必为零。观察者看到的是底空间 $b$，不是它上面的挠子纤维。这是 AEG 版的“有限观察者看不到差异”——差异就是洞。

两个 caveat。$G$ 里的 free 是自由乘积，不是自由群；论文明确拒绝在没有选定生成元与关系时把历史空间等同于自由群。这里的 torsion 是相对算术挠率，不是群论 torsion；它住在交换子群 $[G,G]$ 里，而 $[G,G]$ 正是交换化忘掉的部分。

### 洞是填充纤维

Adva 的有限观察者是一个有界、带版本的观察策略 $Q$；它看到商 $q(h)$，而不是历史 $h$，而且全局有限观察者不必存在（`0037` §5.14）。残差不等于无。typed-hole 笔记 `0079` 把形状说清楚了：

> The hole is syntactically empty and semantically a family.
>
> 洞在句法上是空的，在语义上是一个族。

洞是一个填充纤维：空括号是开口，允许的填充是族。若被遗忘的差异构成一个群在族上的自由传递作用，这个洞就是挠子。在这个意义上，**每个挠子都是洞，但不是每个洞都是挠子**：稳定子非平凡时，族是齐性空间；没有群作用时，它只是纤维。

through-form 笔记 `0070` 给了一个字面实例。未标记关系 $\langle F_-\mid_N F_+\rangle$ 是全部标记消解的载体；选一个消解，就是在其中选一个图。消解集合是单值群 $\langle T_\delta\rangle\cong\mathbb{Z}$ 下的挠子（Paper V §8）。不选的观察者看到关系，也就是洞；选了的观察者看到函数。奇点不是把歧义擦掉，而是把它的表示换成“一个节点加它的消解纤维”。

Surreal tear 笔记 `0223` 给出最干净的值/呈现例子。状态 $q$ 是形式的数值，呈现日 clock 是 $c_2$。序 clock 下降到值；呈现日 clock 不下降。见证是

$$
q(\ \mid\ )=q(\ \mid 1)=0,\qquad \mathrm{day}(\ \mid\ )=0,\quad \mathrm{day}(\ \mid 1)=2.
$$

Surreal 数有规范截面——取最简呈现——它使呈现日成为值的函数；那里的 tear 无害。AES 没有这样的规范截面，所以缺陷被携带。这与“有典范平凡化的挠子 vs 没有的挠子”是同一组二分，只是换了外衣：截面存在或不存在，而 tear 是所选截面不典范的见证。`0021` 补上自然性失败：对象化取最简形式，但这个选择不与缩放交换；ordered holes 与 surgery history 是残差。这个模式与框架挠子相同：集合论截面存在，等变截面不存在。

### 两个方向的不可见

还有第二种、方向相反的“看不到洞”。`concept-ideal-point-naming` §7 的框架分析说：

> 可见 $\leftrightarrow$ 需要框架；不可见 $\leftrightarrow$ 不需要框架。

有序载体把 split 概念数了两遍，因为给两点排序是一个 $\mathbb{Z}/2$-挠子；它完全看不见 non-split 概念，因为 Frobenius 交换两点，没有排序可用。这里挠子是可见的那一侧——需要框架的东西——而洞是不需要框架的典范对象。可见性不等于典范性。

于是语料有两种对偶配置：

1. **底空间观察者。** 观察者看到商，看不到纤维。挠子是看不见的纤维：AEG 的电荷纤维、`0047`/`0070` 的消解关系、`0079` 的填充族。
2. **框架化载体。** 载体看到挠子（需要框架），看不到典范对象：有序 bivaluation 载体把 split 概念数两遍，把 non-split 概念数零遍。

同一个挠子可以落在可见性切口的任一侧。落在哪一侧，取决于观察者的状态空间是什么，而不只取决于挠子本身。

### 小结

**挠子是“洞”在遗忘的差异构成自由传递作用时的形状。纤维中两点之差是挠子的群元素；tearing 是它的几何度量，算术 torsion 是它在交换化商里的平移坐标影子。**

在 AEG 的电荷纤维与消解纤维中，这座桥是精确的。在 surreal 与框架例子中，它是一种结构读法：相同的“有/无典范截面”二分，而不是“每个呈现纤维都是群挠子”的断言。

## 常见混淆

**挠子不是群。** 只有在选点之后它才是群，而且群律依赖这个点。三元的差是典范的，二元的和不是。

**挠子不是齐性空间。** $G/H$ 有典范点 $H$，是齐性空间。只有当 $H$ 平凡时，它才是 $G$-挠子。$G\to G/H$ 的纤维是 $H$-挠子；商是底空间。

**点上的挠子不同于底空间上的挠子。** 点上的挠子只要非空，作为抽象挠子就是平凡的；它仍可能没有典范平凡化。底空间上的挠子可能根本没有整体截面。语料的“没有原点”通常指前者；“没有截面”可能指后者。

**没有等变截面不等于没有截面。** 在框架情形中，集合论截面存在；$G$-等变截面不存在。障碍是自然性，不是存在性。

**挠子不是挠（torsion）。** 群论中的“挠”指有限阶元素；语料还用“torsion”指交换子群 $[G,G]$。挠子是另一个概念：没有基点的自由传递作用。“torsion 是无基点的那一部分”是仿射群中的局部等同，不是一般定义。在 AEG 的电荷纤维中，纤维是 $[G,G]$-挠子，而相对挠率是纤维中两点之差，不是纤维本身。

**群是数据的一部分。** 仿射实例是 $\mathbb{R}_{>0}$ 下的挠子，不是 $\mathbb{Z}$ 下的挠子；消解挠子是 $\mathbb{Z}$ 下的挠子。同样的形状配上不同的群，就是不同的挠子。总要问：哪个群在作用？底空间是什么？

**“不典范”不等于“任意”。** 选择集本身就是一个挠子，带有精确的群作用。换一个选择，计算会差一个唯一的群元素；这个元素才是有意思的不变量。

## 实用检查表

- **要证明** $X$ 是 $G$-挠子：定义作用，证明自由，证明传递，证明 $X$ 非空。
- **要计算**：选一个点，在 $G$ 中计算，并记录换点时答案如何变化。变化量是 $G$ 的一个元素。
- **要比较**两个点：用差 $y-x\in G$。没有基点时不要相加。
- **要平凡化**底空间上的挠子：找整体截面。若不存在，则挠子在强意义下非平凡；若存在但不自然，则挠子平凡但没有典范平凡化。
- **要分类**底空间上的挠子：用 $H^1(B,G)$；挠子是 1-余循环，平凡化是上边缘。
- **要读语料**：先找群、底空间、纤维；区分整体空间与纤维；问截面是集合论的还是等变的。

## 参见

- [主齐性空间](https://zh.wikipedia.org/wiki/%E4%B8%BB%E9%BD%90%E6%80%A7%E7%A9%BA%E9%97%B4)
- [主丛](https://zh.wikipedia.org/wiki/%E4%B8%BB%E4%B8%9B)
- [齐性空间](https://zh.wikipedia.org/wiki/%E9%BD%90%E6%80%A7%E7%A9%BA%E9%97%B4)
- [堆（数学）](https://en.wikipedia.org/wiki/Heap_(mathematics))
- [群胚](https://zh.wikipedia.org/wiki/%E7%BE%A4%E8%83%9A)
- [非交换上同调](https://en.wikipedia.org/wiki/Nonabelian_cohomology)
- [规范场论](https://zh.wikipedia.org/wiki/%E8%A7%84%E8%8C%83%E5%A0%B4%E8%AE%BA)
- [仿射空间](https://zh.wikipedia.org/wiki/%E4%BB%BF%E5%B0%84%E7%A9%BA%E9%97%B4)
- [标架丛](https://zh.wikipedia.org/wiki/%E6%A0%87%E6%9E%B6%E4%B8%9B)

## 参考文献

### 标准文献

1. [Principal homogeneous space](https://en.wikipedia.org/wiki/Principal_homogeneous_space), Wikipedia.
2. [Torsor](https://ncatlab.org/nlab/show/torsor), nLab.
3. [Torsors made easy](https://math.ucr.edu/home/baez/torsors.html), John Baez.
4. [Definition 39.11.1 (0498)](https://stacks.math.columbia.edu/tag/0498), The Stacks Project.
5. [主齐性空间](https://zh.wikipedia.org/wiki/%E4%B8%BB%E9%BD%90%E6%80%A7%E7%A9%BA%E9%97%B4), 维基百科.

### 语料来源

行号对应下列提交。

- **aeg-paper** `402e0e7`
  - [`paper-4/sections/03-projective-quotients.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/paper-4/sections/03-projective-quotients.tex#L138-L160)，`thm:frame-torsor` 与框架讨论。
  - [`paper-5/sections/08-through-crossings.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/paper-5/sections/08-through-crossings.tex#L33-L97)，`def:resolution-torsor`、`thm:monodromy-difference` 与仿射实例。
  - [`paper-0/sections/03-aes-and-motion.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/paper-0/sections/03-aes-and-motion.tex#L745-L805)，`prop:p0-affine-two-layers`。
  - [`notes/analysis-and-calculus/48-finite-field-trigonometry.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/notes/analysis-and-calculus/48-finite-field-trigonometry.tex#L180-L190)，范数纤维作为挠子。
  - [`paper-4/sections/04-condensation-and-continuation.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/paper-4/sections/04-condensation-and-continuation.tex#L40-L140)，延拓与正规化子判据。
  - [`paper-0/sections/08-acs-tearing.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/paper-0/sections/08-acs-tearing.tex#L142-L340)，`conv:p0-history-group`、`prop:p0-acs-is-abelianization` 与 `def:relative-torsion`。
  - [`paper-0/sections/08-acs-tearing.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/paper-0/sections/08-acs-tearing.tex#L593-L649)，`def:p0-tearing`。
  - [`paper-0/sections/10-beyond-linear.tex`](https://github.com/mountain/aeg-paper/blob/402e0e7/paper-0/sections/10-beyond-linear.tex#L132-L150)，`prop:p0-characters-cannot-see-tearing`。
- **pcrg-paper** `c59ab6f`
  - [`references/developing/09-capacity-layers-and-the-torsor.md`](https://github.com/mountain/pcrg-paper/blob/c59ab6f/references/developing/09-capacity-layers-and-the-torsor.md#L30-L48)，挠子层。
  - [`references/developing/10-the-trichotomy-and-what-changes-over-fq.md`](https://github.com/mountain/pcrg-paper/blob/c59ab6f/references/developing/10-the-trichotomy-and-what-changes-over-fq.md#L30-L45)，有限域挠子。
  - [`notes/2026-10-11-descent-proposition.md`](https://github.com/mountain/pcrg-paper/blob/c59ab6f/notes/2026-10-11-descent-proposition.md#L71-L90)，第三点与无等变截面的证明。
  - [`notes/2026-10-11-concept-ideal-point-naming.md`](https://github.com/mountain/pcrg-paper/blob/c59ab6f/notes/2026-10-11-concept-ideal-point-naming.md#L690-L750)，陪集、基点与群胚。
  - [`notes/2026-10-11-concept-ideal-point-naming.md`](https://github.com/mountain/pcrg-paper/blob/c59ab6f/notes/2026-10-11-concept-ideal-point-naming.md#L225-L270)，排序作为 $\mathbb{Z}/2$-挠子。
  - [`notes/2026-10-11-concept-ideal-point-naming.md`](https://github.com/mountain/pcrg-paper/blob/c59ab6f/notes/2026-10-11-concept-ideal-point-naming.md#L278-L353)，可见性与“需要框架”的对偶。
  - [`notes/2026-10-12-operator-kernel-transformation-groupoid-witness.py`](https://github.com/mountain/pcrg-paper/blob/c59ab6f/notes/2026-10-12-operator-kernel-transformation-groupoid-witness.py#L108-L120)，可执行见证。
- **process-geometry** `c47c96f`
  - [`docs/54-pendulum-elliptic-group-rank-lowering.md`](https://github.com/mountain/process-geometry/blob/c47c96f/docs/54-pendulum-elliptic-group-rank-lowering.md#L30-L40)，基点/挠子修正。
- **adva** `17e1842a`
  - [`docs/research/0047-a1-nodal-through-crossing-geometry.md`](https://github.com/mountain/adva/blob/17e1842a/docs/research/0047-a1-nodal-through-crossing-geometry.md#L670-L710)，相位挠子。
  - [`docs/research/0048-cellular-annulus-nodal-torus-dehn-twist.md`](https://github.com/mountain/adva/blob/17e1842a/docs/research/0048-cellular-annulus-nodal-torus-dehn-twist.md#L438-L450)，无限循环挠子。
  - [`docs/research/0223-surreal-order-and-the-tear.md`](https://github.com/mountain/adva/blob/17e1842a/docs/research/0223-surreal-order-and-the-tear.md#L1-L110)，值/呈现日撕裂与规范截面读法。
- **adva-machine** `51ee989`
  - [`docs/research/0079-typed-hole-open-close-calibration-v0.md`](https://github.com/mountain/adva-machine/blob/51ee989/docs/research/0079-typed-hole-open-close-calibration-v0.md#L15-L40)，洞作为填充纤维；另见[一句话形式](https://github.com/mountain/adva-machine/blob/51ee989/docs/research/0079-typed-hole-open-close-calibration-v0.md#L157-L167)。
  - [`docs/research/0070-typed-surreal-through-forms.md`](https://github.com/mountain/adva-machine/blob/51ee989/docs/research/0070-typed-surreal-through-forms.md#L300-L325)，未标记 through 关系与消解纤维。
  - [`docs/research/0021-surreal-cut-objectification-no-go.md`](https://github.com/mountain/adva-machine/blob/51ee989/docs/research/0021-surreal-cut-objectification-no-go.md#L26-L50)，非单射、非自然的对象化。
  - [`docs/research/0037-finite-observer-tricusp-surreal-reduction.md`](https://github.com/mountain/adva-machine/blob/51ee989/docs/research/0037-finite-observer-tricusp-surreal-reduction.md#L1040-L1060)，有限观察者与全局截面的失效。

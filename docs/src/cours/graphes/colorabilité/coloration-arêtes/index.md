---
layout: layout/post.njk

title: Coloration des arêtes d'un graphe

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD <https://fr.wikipedia.org/wiki/Coloration_des_ar%C3%AAtes_d'un_graphe>

{% note "**Définition**" %}
Soit $G=(V, E)$ un graphe. Une **_$k$-coloration des arêtes_** $G$ est une fonction $c: E \to \\{1,\dots, k\\}$ telle que pour triplet de sommets $x \neq y \neq z \in E$ si $xy, xz \in E$ alors $c(xy) \neq c(xz)$.
{% endnote %}

> TBD exemples :
>
> - discret
> - arbre
> - cycle pair
> - cycle impair C5
> - clique K6
>

Les exemples précédent le montre, il existe une borne minimum pour tout graphe :

<span id="definition-notation-coloration-arête-minimum"></span>
{% note "**Définition**" %}

Soit $G=(V, E)$ un graphe. On note $\chi'(G)$ le nombre minimum de couleurs qu'il faut pour colorier ses arêtes et on l'appelle **_nombre chromatique des arêtes de $G$_**.

{% endnote %}

Le lecteur attentif aura remarqué que la notion de colorabilité des arêtes se rapproche de la notion [de couplage](../couplages) : la $k$ colorabilité des arêtes correspond à une partition en couplages de $G$. Ce qui donne immédiatement une borne minimum à notre problème :

{% note "**Proposition**" %}
Pour tout graphe $G$ on a :

<div>
$$
\Delta(G)\leq \chi'(G)
$$
</div>
{% endnote %}
{% details "preuve", "open" %}

clair

{% enddetails %}

On a montré en introduction que l'on peut le faire en $n-1$ couplages de $n/2$ arêtes pour $K_n$ on a donc :

{% note "**Proposition**" %}
<div>
$$
\chi'(K_n) = n-1
$$
</div>
{% endnote %}
{% details "preuve", "open" %}

On utilise un algorithme [round robin scheduling](https://nrich.maths.org/articles/tournament-scheduling) comme on l'a fait en introduction.

{% enddetails %}
{% info %}
cas particulier du [Théorème de Baranyai](https://en.wikipedia.org/wiki/Baranyai%27s_theorem).

> TBD en DM. C'est ds flots. <https://math.stackexchange.com/questions/1827816/proof-of-baranyais-theorem> et p20 <http://discretemath.imp.fu-berlin.de/DMII-2018-19/connectivity-flows-baranyai.pdf>

{% endinfo %}

> TBD NP-complet. exercice 8.16 de <https://www-sop.inria.fr/members/Frederic.Havet/Cours/coloration.pdf>

### Bornes la colorabilité des arêtes

{% note "**Proposition (Vizing, 1964)**" %}
Pour tout graphe $G$ on a :

<div>
$$
\Delta(G) \leq \chi'(G) \leq \Delta(G) +1
$$
</div>
{% endnote %}
{% details "preuve", "open" %}

Le théorème va se prouver en utilisant [des chaînes de Kempe](https://en.wikipedia.org/wiki/Kempe_chain) appliquées à la coloration d'arêtes.

On suppose que $G$ admet une coloration de ses arêtes $f$ et on note $F(u) = \\{f(ux) \vert x \in V, ux \in E \\}$. Une chaîne de Kempe est une suite $uv_0, \dots, uv_k$ de $k+1$ arêtes de $G$ telle que la couleur $c_i = f(uv_{i+1})$ n'est pas dans $F(v_i)$ pour tout $0 \leq i <k$

Pour toute chaîne de Kempe, il est clair que l'on peut remplacer les couleurs de $uv_{i}$ par $c_i$. Enfin, s'il existe $c$ une couleur qui n'est ni dans $F(u)$ ni dans $F(v_k)$ on peut également changer la couleur de $uv_k$ en $c$.

On va construire une coloration des arêtes de $G$ en $\Delta(G) + 1$ couleurs en commençant par le graphe discret et ajoutant une arête à la fois. Supposons que l'on ait une coloration d'un graphe partiel $G'$ de $G$ en $\Delta(G) + 1$ couleurs et on ajoute l'arête $uv_0$. Comme on a à notre disposition $\Delta(G) + 1$ couleurs, il existe forcément une couleur qui n'est pas dans
$F(u)$ et une couleur qui n'est pas dans $F(v_0)$ ce qui permet d'initialiser une chaîne de Kempe que l'on peut itérativement faire grossir construire (la couleur $c_i = f(uv_{i+1})$ n'est pas dans $F(v_i)$ pour tout $0 \leq i <k$) jusqu'à :

- soit arriver à un point où il existe $c$ une couleur qui n'est ni dans $F(u)$ ni dans $F(v_k)$ et l'on peut colorier l'arête $uv_0$ en utilisant la propriété des chaînes de Kempe
- soit arriver à un point où toutes les couleurs qui ne sont pas dans $F(v_k)$ ont déjà été utilisées.

Dans ce deuxième cas, soit $c_k$ une des couleurs qui n'est pas dans $F(v_k)$ et $l$ le plus petit indice tel que $f(uv_l) = c_k$. On peut maintenant construire une autre chaîne $w_0\dots w_p$ telle que $w_0 = u$, $w_1 = v_l$ et telle que si $f(w_iw_{i+1}) = c_k$, alors $f(w_{i+1}w_{i+2}) = c_0$. Cette chaîne ne peut revenir sur ces pas : on va arriver à un moment où la chaîne ne peut être prolongée.

On peut alors :

1. changer les couleurs de la chaîne $uv_0, \dots, uv_l$
2. échanger les couleurs sur la chaîne $w_0\dots w_p$

Ce qui donne une coloration en $\Delta(G) + 1$ couleurs de $G'$ auquel on a ajouté l'arête $uv_0$.

> TBD rendre la preuve plus clair

{% enddetails %}

{% lien %}
[Vizing's Theorem](https://www.youtube.com/watch?v=OZWZpQmGp0g)
{% endlien %}

Notez que la preuve donne un algo pour edge colorier avec delta+1 couleurs.

> TBD :
>
> - C'est NP-complet de savoir si le graphe est de classe 1 ou 2.<https://www.lirmm.fr/~bessy/GraphesStructM1/DM3/Papers/LevenGalil.pdf> et <https://epubs.siam.org/doi/10.1137/0210055> On le verra plus tard (graphe aléatoires) qu'un graphe est presque sûrement de type 1.
> - c'est une illustration de ce qu'est NP-complet. Presque tout le temps facile, sauf quelques exemples qui sont inextricables.

> TBD exo graphe biparti type 1. TBD preuve générale sur edge coloring <https://mathweb.ucsd.edu/~gptesler/154/slides/154_graphcoloring_20-handout.pdf>

> TBD fun fact. Graphes réguliers avec un nombre impair de sommet sont de classe 2.
> TBD la NP-complétude se niche donc uniquement sur les graphes 3-réguliers avec un nombre pair de sommets

---
layout: layout/post.njk 
title:  "Réduction de problèmes"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Une méthode classique de résoudre un problème algorithmique ($P_1$) est de le transformer en un autre problème ($P_1$) que l'on sait résoudre ($S_2$) puis de transformer sa solution en une solution du problème initial ($S_1$) :

<div>
$$
\begin{array}{ccc}
P_1 & \rightarrow & P_2\\
\uparrow &  & \downarrow\\
S_1 & \leftarrow & S_2
\end{array}
$$
</div>

La formalisation de cette opération s'appelle [une réduction](https://fr.wikipedia.org/wiki/R%C3%A9duction_(complexit%C3%A9)) et peut prendre plusieurs formes, que nous expliciterons. Outre ses applications pratiques évidentes pour le design d'algorithme et la résolution de problèmes, la réduction est est un outil fondamental permettant de comparer et de classer les problèmes algorithmiques.

{% info %}
Nous ne parlerons pas ici de la [Réduction de Turing](https://en.wikipedia.org/wiki/Turing_reduction), trop générale et demandant des connaissances comme [les machines à oracles](https://fr.wikipedia.org/wiki/Oracle_(machine_de_Turing)) dont nous ne parlerons pas dans ce cours d'algorithmie.
{% endinfo %}

## Définitions

{% note "**Définition**" %}
Soient $P_1$ et $P_2$ deux problèmes algorithmiques. Une **_réduction_** de $P_2$ en $P_1$ est un couple d'algorithmes $A_1$ et $A_2$ tels que :

- Si $E_1$ est une entrée du problème $P_1$ alors $A_1(E_1)$ est une entrée de du problème $P_2$
- Si $S_2$ est une solution au problème $P_2$ avec $A_1(E_1)$ comme entrée alors $A_2(S_2)$ est une solution au problème $P_1$ d'entrée $E_1$.

Les réductions forment un ordre sur les problèmes algorithmiques : s'il existe une réduction de $P_2$ en $P_1$ on notera $P_1 \leq P_2$.
{% endnote %}

Cette définition, très générale, permet de montrer qu'un problème est plus général qu'un autre : $A \leq B$ signifie que $A$ est un cas particulier de $B$ : que résoudre $B$ permet de résoudre $A$. De là, la complexité du problème $B$ ne peut être plus petite que celle du problème $A$. Par exemple :

{% exercice %}
Montrez que le problèmes de recherche du minimum dans un tableau d'entiers relatifs et le problème de recherche du maximum dans un tableau d'entiers relatifs sont équivalent et que la réduction est linéaire.
{% endexercice %}
{% details "corrigé", "open" %}
Pour des entiers relatifs, il suffit de faire $T'[x] = -T[x]$.
{% enddetails %}

Si l'on veut utiliser la réduction pour résoudre notre problème réduit, on cherche le couple d'algorithmes avec la complexité la plus faible, si possible linéaire (comme dans l'exercice précédent) et au mieux polynomiale :

{% note "**Définition**" %}
Soient $P_1$ et $P_2$ deux problèmes algorithmiques. Une **_réduction polynomiale_** de $P_2$ en $P_1$ est une réduction ou les deux algorithmes $A_1$ et $A_2$ sont de complexité polynomiale.
{% endnote %}

Une réduction polynomiale nous permettra d'utiliser effectivement l'algorithme résolvant $P_2$ pour résoudre $P_1$.

Enfin :

{% note "**Définition**" %}
On dira que deux problèmes $P_1$ et $P_2$ sont **_équivalents_** s'il existe deux **réductions polynomiales** $P_1 \leq P_2$ et $P_2 \leq P_1$.
{% endnote %}

## Exemples et exercices

### Min et max

{% exercice %}
Montrez que le problème de recherche du minimum dans un tableau d'entiers  est plus simple que le problème de recherche du maximum dans un tableau d'entiers.
{% endexercice %}
{% details "corrigé" %}

Pour cela, On crée le tableau $T'$ tel que $T'[x] = \max(T)-T[x]$ et on cherche $\max(T')$. Le min est alors : $\min(T) = \max(T) - \max(T')$.

{% enddetails %}

## Tris

Trier un tableau d'entier va souvent rendre les problèmes bien plus facile. ce qui fait que c'est souvent utile de faire une réduction au tri.

{% exercice %}
Montrez que le problème de recherche du maximum dans un tableau d'entiers  est plus simple que le problème du tri d'un tableau d'entiers.
{% endexercice %}
{% details "corrigé" %}

On trie puis on prend le max.

{% enddetails %}

{% exercice %}
Montrez que le problème de la recherche de doublon dans un tableau d'entiers est plus simple que le problème du tri d'un tableau d'entiers.
{% endexercice %}
{% details "corrigé" %}

On trie puis on parcourt le tableau jusqu'à trouver deux éléments successifs égaux.

{% enddetails %}

### Nombres premiers

{% exercice %}
Montrez que le problème de savoir si un nombre entier est premier (problème PRIME) est équivalent au problème de savoir si un nombre entier est composé (problème COMPOSÉ).

{% endexercice %}
{% details "corrigé" %}

un problème est la négation de l'autre.

{% enddetails %}

Il existe de plus un algorithme polynomial permettant de savoir un nombre est premier, mais sa preuve dépasse le cadre de ce cours.

{% lien %}
[Article montrant que le problème PRIME est polynomial](https://annals.math.princeton.edu/wp-content/uploads/annals-v160-n2-p12.pdf).
{% endlien %}

Cet algorithme ne permet cependant pas de déterminer les facteurs dont il est composé (problème FACTORS). On a cependant clairement COMPOSITE ≤ FACTOR.

{% exercice %}
Montrez que [l'algorithme du crible d'Ératosthène](https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne) n'est pas polynomial.
{% endexercice %}
{% details "corrigé" %}

Il faut regarder tous les nombres jusqu'à $\sqrt{n}$ alors qu'il ne faut que $\log_2{n}$ bits pour stocker $n$. L'algorithme est donc de complexité exponentiel par rapport à la taille des entrées.

{% enddetails %}

On espère, mais on a aucune preuve, qu'il n'existe pas de réduction polynomiale FACTOR ≤ COMPOSITE car le problème FACTORS est à la base des algorithmes actuels de cryptographie.

### Produit et carré

{% exercice %}
Montrer que le problème d'élever un entier au carré est équivalent au problème de multiplier deux entiers entres eux.
{% endexercice %}
{% details "corrigé" %}

Soit $C(x)$ un algorithme qui rend $x^2$ et $M(x, y)$ un algorithme qui rend $xy$.

Comme $C(x) = M(x, x)$ on a clairement $C \leq M$.

La réciproque vient du produit remarquable $(x + y)^2 = x^2 + y^2 + 2xy$ et donc $M(x, y) = \frac{1}{2}(C(x+y) - C(x) - C(y))$.

{% enddetails %}

### 3-SUM

{% lien %}

- <https://people.csail.mit.edu/virgi/6.s078/papers/gajovermars.pdf>
- <https://www.cs.mcgill.ca/~jking/papers/3sumhard.pdf>

{% endlien %}

Reprenons le problème 3-SUM que nous avons déjà vu :

{% note "**Problème**" %}

- **nom** : 3-SUM
- **données** :
  - T : un tableau de $n$ entiers relatifs
- **question** : existe-t-il 3 indices (pouvant être égaux) tels que $T[i] + T[j] + T[k] = 0$

{% endnote %}

De nombreux problèmes lui sont équivalent comme par exemple le suivant :

{% note "**Problème**" %}

- **nom** : 3-SUM'
- **données** :
  - $T$, $T'$ et $T''$ : trois tableaux d'entiers relatifs
- **question** : existe-t-il 3 indices tels que $T[i] + T'[j] = T''[k]$

{% endnote %}

Prouvons le :

{% exercice %}
Montrer que 3-SUM ≤ 3-SUM'
{% endexercice %}
{% details "corrigé" %}

On prend $T = T'$ et $T''[x] = -T[x]$

{% enddetails %}
{% exercice %}
Montrer que 3-SUM' ≤ 3-SUM
{% endexercice %}
{% details "corrigé" %}

On prend $A = 3(\sum \vert T[i]\vert + \sum \vert T'[i]\vert + \sum \vert T''[i]\vert) + 1$ et on crée un tableau $[T[i] + A \\;\vert\\; i] + [T'[i] + 3A \\;\vert\\; i] + [-T''[i] - 4A \\;\vert\\; i]$.

Soient $i, j, k$ tels que T[i] + T[j] + T[k] = 0$.

Pour que la somme fasse 0 il faut que les $A$ ajoutés s'annulent : donc
obligatoirement 1 élément de chaque tableau initial $T$, $T'$ et $T''$.
{% enddetails %}

3-SUM est un problème fondamental en [géométrie algébrique](https://fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_alg%C3%A9brique). Considérons par exemple le problème suivant :

{% note "**Problème**" %}

- **nom** : Geobase
- **données** :
  Un ensemble de $n$ points du plan à coordonnées entières sur trois lignes horizontales avec $y = 0$, $y = 1$ et $y = 2$
- **question** : Existe-t-il une droite non horizontale passant par 3 points.
{% endnote %}

Montrons qu'il est équivalent à 3-SUM :

{% exercice %}
Montrer que 3-SUM' ≤ GEOBASE
{% endexercice %}
{% details "corrigé" %}

Deux vecteurs $\vec{u} = (x, y)$ et $\vec{v} = (x', y')$ sont colinéaires si $\vec{u} \cdot \vec{v}^{\perp} = 0$. Comme $\vec{v}^{\perp} = (-y', x')$, $\vec{u}$ et $\vec{v}$ sont colinéaires si $xy' - yx' = 0$.

Il suffit alors de construire les points :

- $(T[i], 0)$
- $(T''[i]/2, 1)$
- $(T'[i], 2)$

si trois points sont colinéaires alors il existe i, j et k tels que $T[i] + T'[j] = T''[k]$
{% enddetails %}

{% exercice %}
Montrer que GEOBASE ≤ 3-SUM'
{% endexercice %}
{% details "corrigé" %}

On fait le contraire. On ajoute chaque point de :

- $(x, 0)$ dans $T = [x | \forall (x, 0)]$
- $(x, 1)$ dans $T'' = [2x | \forall (x, 1)]$
- $(x, 2)$ dans $T' = [x | \forall (x, 2)]$

{% enddetails %}

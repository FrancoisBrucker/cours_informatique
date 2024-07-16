---
layout: layout/post.njk 
title: Castors Affairés

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous en donnons une ici, la plus célèbre des fonction non calculable : [les castors affairés](https://fr.wikipedia.org/wiki/Castor_affair%C3%A9) (*busy beavers* dans la version originale). On a pas pu la donner avant car elle dépend intrinsèquement de la notion de machine de Turing.

{% note "**Définition**" %}
On définit le ***score*** $\rho(M)$ d'une machine de Turing $M$ acceptant le mot vide comme étant le nombre de $1$ de $M()$.

La fonction du **castor affairé** $\Sigma : \mathbb{N} \rightarrow \mathbb{N}$ est définie telle que $\beta(n)$ vaut le score maximal pour toutes les machine de Turing à $n$ états acceptant le mot vide.
{% endnote %}

La fonction est bien définie pour tout $n>0$ puisqu'il n'y a qu'un nombre fini de machine de Turing à $n$ états : la valeur $\beta(n)$ est un maximum d'un ensemble fini, ce nombre existe.

{% note "**Proposition**" %}
$\beta(n) \geq n - 1$ pour tout $n >0$
{% endnote %}
{% details "preuve", "open" %}

Considérons la machine $M_n$ à $n$ états $(q_0, \dots, q_{n-1}) telle que :

* $q_0$ est l'état initial
* $q_{n-1}$ l'état d'acceptation
* la fonction de transition $\delta$ telle que $\delta(q_i, \sharp) = (q_{i+1}, 1, \rightarrow)$

On a $M_n() = \underbracket{1\cdots 1}_{n-1}{}$.
{% enddetails %}

{% note "**Proposition**" %}
$\beta(n)$ est strictement croissante
{% endnote %}
{% details "preuve", "open" %}
Soit $B_n$ une machine à $n$ états telle que $\rho(B_n) = \beta(n)$. La machine obtenue en enchaînant $B_n$ et $M_1$ (voir preuve précédente) en associant l'état final de $B_n$ à l'état initial de $M_1$ a $n+1$ états (les état de B_n$ plus l'état d'acceptation de $M_1$) et sa sorite produit un 1 de plus que $\beta_n$ : $\beta(n+1) \geq \beta(n) + 1$.

{% enddetails %}

Ce qui nous permet de prouver que :

{% note "**Proposition**" %}
La fonction $\beta$ est non calculable.
{% endnote %}
{% details "preuve", "open" %}

Supposons que $\beta$ soit calculable. Il existe alors une machine $F$ de pseudo code :

```text
def F(n):

efface l'entrée du ruban

i = 0
tant que i < 2 * β(n):
    écrire 1 sur le ruban et décaler le curseur un cran à droite
    i = i + 1
```

On peut supposer, sans perte de généralité, que l'entrée de $F$ soit uniquement composée de $1$(donc $n$ signifie que l'entrée est composée de n $1$ consécutifs).

De là, on peut également construire la machine $M$ :

```text
def M():
    M_n()
    déplace le curseur à gauche jusqu'à obtenir un blanc puis déplace le curseur d'un cran à droite
    F(n)
```

Cette machine enchaîne $M_n$ à $F$. Pour la sorite de $M_n()$ soit l'entrée de $F$, il faut décaler le ruban pour le placer jusqu'au premier 1 (ceci se fait avec une machine à 3 états). Cette machine à un nombre d'états égal au nombre d'état de $M_n$ plus le nombre d'état de la machine qui déplace le ruban (3) plus le nombre d'état de $F$ (disons $k$) moins les liants entre les machines (les états finaux des machines intermédiaires sont les états initiaux des machines suivantes), c'est à dire 2. Au final, la machine $M$ à : $n + 3 + k - 2 = n + k +1$ états et est telle que $\rho(M) = \beta(2n)$.

On en déduit l'inégalité : $\beta(n + k + 1) \geq \beta(2n)$ et comme $\beta$ est strictement croissante on a l'inégalité : $2n \leq n + k + 1$ pour tout $n > 0$ ce qui est impossible.

{% enddetails %}

{% lien %}
L'[article](https://www.gwern.net/docs/cs/1962-rado.pdf) de Tibor Radò où les busy beavers sont définis.
{% endlien %}

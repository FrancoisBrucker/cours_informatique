---
layout: layout/post.njk

title: Graphes à valuations positives
authors:
  - François Brucker

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Dans le cas là où les valuation sont positives trouver un chemin de poids minimum ou un [chemin élémentaire](../../chemins-cycles-connexite#définition-élémentaire){.interne} de poids minimum sont deux problème équivalents :

{% note "**Proposition**" %}
S'il existe un chemin entre $a$ et $b$ dans un graphe orienté $G$, alors **il existe** un pseudo-chemin de longueur minimum. De plus, un pseudo-chemin de longueur minimum est nécessairement **élémentaire**.

Plus généralement, si le graphe $G$ est valué par une fonction $f$ positive ($f: E \rightarrow \mathbb{R}^+$) alors :

- **il existe** un chemin de poids minimum
- parmi tous les chemins de poids minimum, ceux de longueur minimum sont **élémentaire**

{% endnote %}
{% details "preuve", "open" %}
Le problème de longueur minimum est un cas particulier de valuation positive (la valeur est toujours égale à 1), on considère donc :

- un graphe orienté valué positivement $(G, f)$
- deux sommets $a$ et $b$ de $G$
- un chemin $c$ entre $a$ et $b$

Un chemin $c'$ réalisant le minimum est donc tel que $0 \leq f(c') \leq f(c)$. Comme l'intervalle $[0, f(c)]$ est un compact, la fonction $f$ va atteindre son minimum pour un élément de l'ensemble des chemins $c'$ entre $a$ et $b$ telles que $0 \leq f(c') \leq f(c)$. On en conclut qu'il existe un chemin $c^\star$ entre $a$ et $b$ dans $G$ de poids minimum.

Si $c^\star$ est un chemin non élémentaire, il existe une boucle. Cette boucle est de longueur strictement positive, la supprimer ne change pas l'origine et la fin du chemin tout en diminuant strictement sa longueur : $c^\star$ ne peut pas être un chemin de poids minimum de longueur minimum.

{% enddetails %}

De là :

{% note %}
On peut se restreindre à rechercher des **chemins élémentaires** de poids minimum sans perte de généralité.
{% endnote %}

Enfin, une propriété fondamentale des chemins de poids minimum pour des graphes valués positivement — et le moteur des algorithmes qui permettent de trouver des chemins de poids minimum — est qu'un chemin de poids minimum est lui-même composé de chemin de poids minimum :

{% note "**Proposition : Programmation dynamique**" %}
Soit $c = v_0 \dots v_{k-1}$ un chemin de longueur minimum entre $v_0$ et $v_{k-1}$ pour un graphe orienté valué positivement $(G, f)$. Alors pour tout $0 \leq i < j < k$ : $c'= v_{i} \dots v_j$ est un chemin de longueur minimum entre $v_i$ et $v_j$

{% endnote %}
{% details "preuve" %}
S'il existait un chemin $c'' = w_0 \dots w_{k'-1}$ entre $v_i$ et $v_j$ de poids strictement plus petit que $c'$, alors le pseudo-chemin : $c^\star = v_0\dots v_{i-1} w_0 \dots w_{k'-1} v_{j+1} \dots v_{k-1}$ serait de poids strictement plus petit que $c$. Comme de tout pseudo-chemin on peut extraire un chemin élémentaire (en supprimant itérativement les boucles) on peut _raffiner_ $c^\star$ en un chemin élémentaire entre $v_0$ et $v_{k-1}$ de poids strictement plus petit que $c$, ce qui est impossible par hypothèse.

{% enddetails %}

## Algorithmes

### Dijkstra

{% aller %}

[Algorithme de Dijkstra](./dijkstra/){.interne}

{% endaller %}

### <span id="a-star"></span>$A^\star$

{% aller %}

[Algorithme $A^\star$](./A-étoile/){.interne}

{% endaller %}

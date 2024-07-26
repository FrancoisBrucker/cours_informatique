---
layout: layout/post.njk 
title:  "Réduction de problèmes"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Une méthode classique de résoudre un problème algorithmique ($P_1$) est de le transformer en un autre problème ($P_1$) que l'on sait résoudre ($S_2$)puis de transformer sa solution en une solution du problème initial ($S_1$) :

<div>
$$
\begin{array}{ccc}
P_1 & \rightarrow & P_2\\
\uparrow &  & \downarrow\\
S_1 & \leftarrow & S_2
\end{array}
$$
</div>

La formalisation de cette opération s'appelle [une réduction](https://fr.wikipedia.org/wiki/R%C3%A9duction_(complexit%C3%A9)) et peut prendre plusieurs formes, que nous expliciterons. Outre ses applications pratiques évidentes pour le design d'algorithme et la résolution de problèmes, la réduction est est un outil fondamental permettant de comparer et de classer les problèmes algorithmique.

{% info %}
Nous ne parlerons pas ici de la [Réduction de Turing](https://en.wikipedia.org/wiki/Turing_reduction), trop générale et demandant des connaissances, comme [les machines à oracles](https://fr.wikipedia.org/wiki/Oracle_(machine_de_Turing)), dont nous ne parlerons pas dans ce cours d'algorithmie.
{% endinfo %}

## Définitions

{% note "**Définition**" %}
Soient $P_1$ et $P_2$ deux problèmes algorithmiques. Une **_réduction_** de $P_2$ en $P_1$ est un couple d'algorithmes $A_1$ et $A_2$ tels que :

- Si $E_1$ est une entrée du problème $P_1$ alors $A_1(E_1)$ est une entrée de du problème $P_2$
- Si $S_2$ est une solution au problème $P_2$ avec $A_1(E_1)$ comme entrée alors $A_2(S_2)$ est ue solution au problème $P_1$ d'entrée $E_1$.

Les réductions forment un ordre sur les problèmes algorithmiques : s'il existe une réduction de $P_2$ en $P_1$ on notera $P_1 \leq P_2$.
{% endnote %}

Cette définition, très générale, permet de montrer qu'un problème est plus général qu'un autre : $A \leq B$ signifie que $A$ est un cas particulier de $B$ : que résoudre $B$ permet de résoudre $A$. De là, la complexité du problème $B$ ne peut être plus petite que celle du problème $A$.

Rappelez-vous, c'est exactement ce qu'on a fait lorsque l'on a étudié la complexité de [la recherche de l'enveloppe convexe](../enveloppes-convexes/#complexité-problème), on a montré que le problème du tri est plus simple que la complexité de la recherche de l'enveloppe convexe.

Si l'on veut une utilisation plus pratique de la réduction, on va chercher le couple d'algorithmes avec la complexité la plus faible, si possible linéaire et au mieux polynomiale :

{% note "**Définition**" %}
Soient $P_1$ et $P_2$ deux problèmes algorithmiques. Une **_réduction polynomiale_** de $P_2$ en $P_1$ est une réduction ou le couple d'algorithmes $A_1$ et $A_2$ est de complexité polynomiale.
{% endnote %}

Une réduction polynomiale nous permettra d'utiliser effectivement l'algorithme résolvant $P_2$ pour résoudre $P_1$.

Enfin :

{% note "**Définition**" %}
Lorsque $P_1 \leq P_2$ et $P_2 \leq P_1$, on dira que $P_1$ est équivalent à $P_2$.
{% endnote %}

## Exemples et exercices

### Min et max

Cette première réduction est simple :

{% exercice %}
Montrez que le problèmes de recherche du minimum dans un tableau d'entiers relatifs et le problème de recherche du maximum dans un tableau d'entiers relatifs sont équivalent et que la réduction est linéaire.
{% endexercice %}
{% details "corrigé" %}
Pour des entiers relatifs, il suffit de faire $T'[x] = -T[x]$.
{% enddetails %}

La seconde un peu moins :

{% exercice %}
Montrez que le problème de recherche du minimum dans un tableau d'entiers  est plus simple que le problème de recherche du maximum dans un tableau d'entiers.
{% endexercice %}
{% details "corrigé" %}

Pour cela, On crée le tableau $T'$ tel que $T'[x] = \max(T)-T[x]$ et on cherche $\max(T')$. Le min est alors : $\min(T) = \max(T) - \max(T')$.

{% enddetails %}

{% exercice %}
Montrez que le problème de recherche du maximum dans un tableau d'entiers  est plus simple que le problème du tri d'un tableau d'entiers.
{% endexercice %}
{% details "corrigé" %}

> On trie puis on prend le max

{% enddetails %}

### Nombres premiers

PRIME = COMPOSITE ≤ FACTOR

On espère que FACTOR > PRIME.

### Produit et carré

#### Entiers

> TBD Wikipedia <https://fr.wikipedia.org/wiki/R%C3%A9duction_(complexit%C3%A9)#Exemple_introductif>

#### Matrices

> TBD <https://people.cs.pitt.edu/~kirk/cs1510/notes/reducenotes.pdf>

### 3-SUM

> TBD classique en géométrie algébrique.

> TBD <https://www.cs.mcgill.ca/~jking/papers/3sumhard.pdf>
> TBD <https://en.wikipedia.org/wiki/3SUM#3SUM-hardness>

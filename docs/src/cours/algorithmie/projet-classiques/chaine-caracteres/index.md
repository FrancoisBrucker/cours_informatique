---
layout: layout/post.njk

title: Chaînes de caractères

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Corrigé](./corrigé){.interne}
{% endlien %}

Le but de cet série d'exercice est d'étudier les modifications d'une chaîne de caractères.

## Sous-séquence

Soient deux chaînes de caractères $S_1$ et $S_2$. On dit que $S_2$ est une _sous-séquence_ de $S_1$ si il existe une fonction strictement croissante

$$
f : \{0,\ldots, len(S_2)-1\} \longrightarrow \{0,\ldots, len(S_1)-1\}
$$

Telle que $S_1[f(j)] = S_2[ j]$ pour tout $j$ de $\{0,\ldots, len(S_2)-1\}$.

Proposez, prouvez et donnez la complexité d'un algorithme qui détermine si $S_2$ est une sous-séquence de $S_1$.

## Sous-mot

Soient deux chaînes de caractères $S_1$ et $S_2$. On dit que $S_2$ est un **_sous-mot_** de $S_1$ s'il existe un indice $i$ tel que $S_2[j] = S_1[i + j]$ pour tout $j$ de $0$ à $len(S_2) - 1$.

- Proposez, prouver et donner la complexité d'un algorithme qui détermine si $S_2$ est un sous-mot de $S_1$.
- Si toutes les lettres de $S_2$ sont deux à deux différentes, donnez un algorithme en $\mathcal{O}(len(S_1))$ pour résoudre ce problème.

## Permutation circulaire

Étant donné un liste $L$ de longueur $n$ et un entier $k$, le problème est de transformer $L$ par permutation circulaire en décalant (circulairement) tous les éléments de $L$ de $k$ places. Par exemple, avec $L = \text{LongtempsJeMeSuisCouchéDeBonneHeure}$ et $k = 4$, on obtient $L' = \text{eureLongtempsJeMeSuisCouchéDeBonneH}$.

- Donnez un algorithme $\text{Permut}(L, k)$ qui, avec une liste $L$ et un entier $k$ en entrées, construit une nouvelle liste $L'$, permutation circulaire de $L$.
- Si on veut transformer $L$ en $\text{Permut}(L,k)$, montrez que la place mémoire utilisée (en plus de celle des données du problème ($L$)) par votre algorithme est $O(n)$.

On veut maintenant faire une permutation circulaire sur site, _ie._ sans utiliser plus que $O(1)$ place mémoire supplémentaire (il arrive (par exemple quand on étudie le génome) que $n$ soit très grand). Il faut pour cela
remarquer que permuter circulairement $L$ revient à prendre les $k$ dernières lettres de $L$ et à les mettre en tête. On note $L^R$ la liste $L$ **_renversée_** (par exemple, si $L =\text{Couché}$, $L^R = \text{éhcuoC}$).

- Donnez un algorithme en $O(n)$ et utilisant $O(1)$ place mémoire supplémentaire, qui transforme $L$ en $L^R$.
- Montrez que, si on note $L = AB$, où $B$ est de longueur $k$ (par exemple, avec $L = \text{LongtempsJeMeSuisCouchéDeBonneHeure}$ et $k = 4$, $A =\text{LongtempsJeMeSuisCouchéDeBonneH}$ et $B =\text{eure}), alors \text{Permut}(L, k) = (A^RB^R)^R$.
- Déduisez-en un algorithme de complexité $O(n)$ qui permute une liste (de longueur $n$), _ie._ qui transforme $L$ en $\text{Permut}(L,k)$, en utilisant $O(1)$ espace mémoire supplémentaire.

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

Le but de cet série d'exercices est d'étudier les modifications d'une chaîne de caractères.

## Sous-séquence

Soient deux chaînes de caractères $S_1$ et $S_2$ de longueurs $n_1$ et $n_2$ respectivement.

{% note "**Définition**" %}
La chaîne $S_2$ est **_une sous-séquence_** de $S_1$ si il existe une fonction strictement croissante $f: [0, n_2[ \to [0, n_1[$ telle que $S_1[f(j)] = S_2[j]$ pour tout $j$ de $[0, n_2[$.
{% endnote %}
{% faire %}
Proposez, prouvez et donnez la complexité d'un algorithme qui détermine si $S_2$ est une sous-séquence de $S_1$.
{% endfaire %}

## Sous-mot

Soient deux chaînes de caractères $S_1$ et $S_2$ de longueurs $n_1$ et $n_2$ respectivement.

{% note "**Définition**" %}
La chaîne $S_2$ est un **_sous-mot_** de $S_1$ s'il existe un indice $i$ tel que $S_2[j] = S_1[i + j]$ pour tout $j$ de $[0, n_2[$.

{% endnote %}

Être un sous-mot est plus restrictif qu'être une sous-séquence.

{% faire %}

- Proposez, prouver et donner la complexité d'un algorithme simple qui détermine si $S_2$ est un sous-mot de $S_1$.
- Si toutes les lettres de $S_2$ sont deux à deux différentes, donnez un algorithme en $\mathcal{O}(n_1)$ pour résoudre ce problème.

{% endfaire %}

## Permutation circulaire

Étant donné un tableau de caractères $S$ de longueur $n$ et un entier $k$, le problème est de transformer $S$ par **_permutation circulaire_** en décalant (circulairement) tous les éléments de $S$ de $k$ places. Par exemple, avec $S = \text{LongtempsJeMeSuisCouchéDeBonneHeure}$ et $k = 4$, on obtient $S' = \text{eureLongtempsJeMeSuisCouchéDeBonneH}$.

{% faire %}

Donnez un algorithme optimal simple, `permutation(S: [caractère], k: entier) →[caractère]`{.language-} qui rend à partir de $S$ et de $k$, un nouveau tableau permutation circulaire de $S$ de $k$ caractères.
{% endfaire %}

On veut maintenant faire une permutation circulaire sur site, _ie._ sans utiliser plus que $\mathcal{O}(1)$ place mémoire supplémentaire (il arrive (par exemple quand on étudie le génome) que $n$ soit très grand). Il faut pour cela
remarquer que permuter circulairement $L$ revient à prendre les $k$ dernières lettres de $L$ et à les mettre en tête. On note $L^R$ la liste $L$ **_renversée_** (par exemple, si $L =\text{Couché}$, $L^R = \text{éhcuoC}$).

{% faire %}

Donnez un algorithme `retournement(S: [caractère]) → ∅`{.language-} en $\mathcal{O}(n)$ et utilisant $\mathcal{O}(1)$ place mémoire supplémentaire, qui transforme $L$ en $L^R$.

{% endfaire %}
{% faire %}
Montrez que, si on note $L = AB$, où $B$ est de longueur $k$ (par exemple, avec $L = \text{LongtempsJeMeSuisCouchéDeBonneHeure}$ et $k = 4$, $A =\text{LongtempsJeMeSuisCouchéDeBonneH}$ et $B =\text{eure}$), alors \text{Permut}(L, k) = (A^RB^R)^R$.
{% endfaire %}
{% faire %}
Déduisez-en un algorithme de complexité $\mathcal{O}(n)$ qui permute une liste (de longueur $n$), _ie._ qui transforme $L$ en $\text{Permut}(L,k)$, en utilisant $\mathcal{O}(1)$ espace mémoire supplémentaire.

{% endfaire %}

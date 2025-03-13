---
layout: layout/post.njk 
title:  "Problèmes algorithmiques"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Quelques exemples de problèmes algorithmiques classiques car :

- pouvant être approchés de multiples manières,
- la solution optimale est non triviale et belle.

## Élément majoritaire

{% aller %}

- [élément majoritaire](/enseignements/MPCI/programmation-algorithmes/annales/2023-2024/ds-1/ds1_2023_2024.pdf)
{% endaller %}

## Calcul de la médiane

{% note "**Définition**" %}
La **_médiane_** d'un ensemble fini d'entiers $E$ est un élément $m$ de cet ensemble tel que :

- $\vert E \vert / 2$ éléments de $E$ sont plus petit ou égal à $m$
- $\vert E \vert / 2$ éléments de $E$ sont plus grand ou égal à $m$

{% endnote %}

Trouver la médiane d'un ensemble va se faire en utilisant un problème (algorithmique) a priori plus général,$k$-SELECT :

{% note "**Problème**" %}

- **Nom** : $k$-SELECT
- **Entrées** : Un tableau $T$ d'entiers (relatifs)
- **Sortie** : un entier $x=T[i]$ de $T$ tel que l'on peut séparer les autres élément de $T$ (ceux d'indice différent de $i$) en deux tableaux :
  - l'un de $k-1$ éléments éléments plus petit ou égal à $x$
  - l'un de $T.\mbox{\small longueur}-k$ éléments éléments plus grand ou égal à $x$
{% endnote %}

Commencez par montrer que c'est vrai :

{% faire %}
Montrer que le problème de la médiane est un cas particulier du problème $k$-SELECT
{% endfaire %}

Puis que l'on peut effectivement résoudre le problème $k$-SELECT par un algorithme :

{% faire %}
Montrer que le problème $k$-SELECT est un problème algorithmique en modifiant l'algorithme du [tri par sélection](../problème-tris/algorithme-sélection/){.interne} pour qu'il résolve $k$-SELECT.

{% endfaire %}
{% faire %}
Quelle est la complexité de cet algorithme ?
{% endfaire %}

### On fait (un peu) mieux

> TBD tri

### On fait mieux (mais en moyenne)

> TBD pivot

### On fait optimal (mais c'est plus compliqué)

> TBD calcul optimal.

### ref

[calcul de la médiane (exercice 4)](/enseignements/MPCI/programmation-algorithmes/annales/2020-2021/mpci_et_2020_2021.pdf)

## Autres problèmes

{% aller %}

- [tri de crêpes (exercice 2)](/enseignements/MPCI/programmation-algorithmes/annales/2021-2022/ds_1_2021_2022.pdf)
- [échanges d'indices (exercice 3)](/enseignements/MPCI/programmation-algorithmes/annales/2021-2022/ds_1_2021_2022.pdf)
- [points fixe](/enseignements/MPCI/programmation-algorithmes/annales/2024-2025/dm-doublons/)
- [palindromes](/enseignements/MPCI/programmation-algorithmes/annales/2023-2024/palindromes/)
{% endaller %}

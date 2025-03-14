---
layout: layout/post.njk 
title:  "Calcul de la médiane d'un tableau d'entiers"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On va ici étudier un problème classique, le calcul de la médiane d'un tableau, en essayant de nombreuses techniques jusqu'à arriver à une solution optimale à la fois élégante et surprenante.

{% info %}
Pour s'éviter des nœuds au cerveau, on considérera que les tableaux sont en fait [des listes](../../structure-liste/){.interne} et qu'on peut donc :

- ajouter un élément en fin de tableau en $\mathcal{O}(1)$
- supprimer le dernier élément du tableau en $\mathcal{O}(1)$

{% endinfo %}

Le problème est classique et joli. Il devient cependant de plus en plus difficile.

## Définitions

{% note "**Définition**" %}
La **_médiane_** d'un ensemble fini d'entiers $E$ est un élément $m$ de cet ensemble tel que :

- $\vert E \vert / 2$ éléments de $E$ sont plus petit ou égal à $m$
- $\vert E \vert / 2$ éléments de $E$ sont plus grand ou égal à $m$

{% endnote %}

Trouver la médiane d'un ensemble va se faire en utilisant un problème (algorithmique) a priori plus général,$k$-SELECT :

{% note "**Problème**" %}

- **Nom** : $k$-SELECT
- **Entrées** :
  - Un tableau $T$ d'entiers (relatifs)
  - un entier $k$
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
Montrer que le problème $k$-SELECT est un problème algorithmique en modifiant l'algorithme du [tri par sélection](../../problème-tris/algorithme-sélection/){.interne} pour qu'il résolve $k$-SELECT.

{% endfaire %}
{% faire %}
Quelle est la complexité de cet algorithme ?
{% endfaire %}

{% faire %}
Quelle est la complexité ce cet algorithme appliqué au calcul de la médiane ?
{% endfaire %}

## On fait (un peu) mieux

Ajoutons des conditions initiales à nos problème pour voir s'il ne deviendrait pas plus simple :

{% note "**Problème**" %}

- **Nom** : $k$-SELECT-SORT
- **Entrées** :
  - Un tableau $T$ d'entiers (relatifs) trié par ordre croissant
  - un entier $k$
- **Sortie** : un entier $x=T[i]$ de $T$ tel que l'on peut séparer les autres élément de $T$ (ceux d'indice différent de $i$) en deux tableaux :
  - l'un de $k-1$ éléments éléments plus petit ou égal à $x$
  - l'un de $T.\mbox{\small longueur}-k$ éléments éléments plus grand ou égal à $x$
{% endnote %}

On a du coup un problème bien plus simple :

{% faire %}
Montrer que le problème $k$-SELECT-SORT peut être résolu en $\mathcal{O}(1)$ opérations.

{% endfaire %}

Et c'est utile pour notre problème :

{% faire %}
Montrer qu'en utilisant l'algorithme précédant, on peut résoudre le $k$-SELECT en $\mathcal{O}(n\ln(n))$ opérations, où $n$ est la taille du tableau en entrée.

{% endfaire %}

{% faire %}
Quelle est la complexité ce cet algorithme appliqué au calcul de la médiane ?
{% endfaire %}

## On fait mieux (mais en moyenne)

Les deux algorithmes précédents pour résoudre le problème de $k$-SELECT ont la même complexité minimale, maximale et en moyenne.

Tentons une autre approche, encore une fois issue d'un algorithme de tri pour tenter d'accélérer l'exécution de notre algorithme au moins en moyenne.

Pour cela, on reprend l'idée du pivot utilisée dans [l'algorithme du tri rapide](../../problème-tris/algorithme-rapide/){.interne} :

{% faire %}
Donnez un algorithme `pivot(T: [entier], v: entier) → ([entier], [entier])`{.language-} de complexité égale à la taille du tableau en entrée qui rend deux tableaux $T_1$ et $T_2$ tels que :

- $T_1$ contient tous les éléments de $T$ strictement plus petit que $v$
- $T_2$ contient tous les éléments de $T$ strictement plus grand que $v$

{% endfaire %}
{% faire %}
Utilisez l'algorithme `pivot(T[1:], T[0])`{.language-} pour créer un algorithme récursif permettant de résoudre le problème $k$-SELECT avec une équation de récursion valant :

<div>
$$
C(n, k) = \mathcal{O}(n) + C(n', k')
$$
</div>

Vous expliciterez $n'$ et $k'$ en fonction de :

- la taille $n$ du tableau $T$ en entrée
- l'entier $k$
- $T[0]$

{% endfaire %}
{% faire %}
Déduisez en la complexité maximale et minimale de ce nouvel algorithme.

{% endfaire %}

{% faire %}
En utilisant l'argument utilisé pour le calcul de la complexité en moyenne du tri rapide, montrez que la complexité en moyenne de l'algorithme précédent suit l'équation de récurrence suivante pour une constante donnée $K$ et $n$ assez grand :

<div>
$$
C_{\mbox{\small moy}}(n) \leq K\cdot n + C_{\mbox{\small moy}}(\frac{n}{2})
$$
</div>

Vous donnerez les conditions d'applications de ce calcul.
{% endfaire %}
{% faire %}
En déduire que la complexité en moyenne de cet algorithme de calcul de la médiane est en $\mathcal{O}(n)$.
{% endfaire %}

## Peut-on faire mieux ?

On peut considérer un algorithme idéal résolvant le problème $k$-SELECT dont la complexité suit l'équation de récurrence suivante :

<div>
$$
C(n) = K\cdot n + C(\lambda \cdot n)
$$
</div>

Avec $K$ une constante positives et $0 < \lambda < 1$.

{% faire %}
Montrez que dans ce cas idéal : $C(n) = \mathcal{O}(n)$.
{% endfaire %}

Ce cas idéal est atteint pour notre algorithme $k$-SELECT actuel si le pivot choisi permet **toujours** de découper le tableau en deux parties dont la plus grande est toujours plus petite ou égale à $\lambda \cdot n$ avec $0 < \lambda < 1$.

Pour trouver ce pivot, il faut voir de combien de ressource disponible on a. Pour cela considérons un nouvel algorithme de complexité :

<div>
$$
C(n) \leq K\cdot n + p \cdot C(\lambda \cdot n)
$$
</div>

Avec $K$ et $p$ deux constantes positives et $0 < \lambda < 1$.

{% faire %}
Calculez $C(n)$ et déduisez en une condition pour laquelle $C(n) = \mathcal{O}(n)$.
{% endfaire %}

On a donc une petite marge pour trouver ce pivot idéal. Vendons un peu la mèche en supposant que l'on se donne une complexité de l'ordre de $C(\lambda' \cdot n)$ avec $0 < \lambda' < 1$ pour trouver ce pivot.

{% faire %}
Montrer que dans ce cas là, notre algorithme est de complexité :

<div>
$$
C(n) = \mathcal{O}(n) + C(\lambda' \cdot n) + C(\lambda \cdot n)
$$
</div>

{% endfaire %}

Comme notre algorithme est de complexité croissante :

{% faire %}
Donnez des conditions pour $\lambda'$ et $\lambda$ pour que notre algorithme final soit de complexité $\mathcal{O}(n)$
{% endfaire %}

La complexité de notre algorithme $k$-SELECT réel est : <div>
$$
C(n, k) = \mathcal{O}(n) + C(n', k')
$$
</div>

Avec $k' \leq k$. Si on arrive à trouver un pivot permettant d'avoir $n' \leq \lambda \cdot n$ avec $0< \lambda< 1$, on pourra borner notre complexité réelle par :

<div>
$$
C(n, k) \leq \mathcal{O}(n) + C(\lambda \cdot n, k')
$$
</div>

En prenant le $k'$ le pire à chaque fois, on a : $C(n, k) \leq C(n)$. SI on trouve un tel pivot pour notre algorithme $k$-SELECT, on aura gagné.

Il n'y a plus qu'à.

## On fait optimal (mais c'est plus compliqué)

Et c'est parti. L'astuce ultime est de :

1. découper le tableau en $n/5$ paquets de 5 éléments
2. on calcule la médiane de chacun de ces $n/5$ petits tableaux de 5 éléments.
3. le pivot sera la médiane des $n/5$ médianes calculées précédemment

{% faire %}
Montrez que si $C(n)$ est la complexité du calcul de la médiane d'un tableau de $n$ entiers, alors le calcul du pivot peut se faire en une complexité de $\mathcal{O}(n) + C(n/5)$.
{% endfaire %}

Et maintenant c'est facile :

{% faire %}
Montrez que l'algorithme pivot appliqué à tableau initial  et au pivot calculé précédemment va découper le tableau en deux tableau dont le plus grand ne peut pas être de taille supérieure à $7n/10$.
{% endfaire %}
{% info %}
Vous pourrez supposer qu'il y a plus de 50% de valeurs strictement plus petite que le pivot et compter le nombre de valeurs minimales plus grande ou égale à celui-ci.
{% endinfo %}

{% faire %}
En déduire que l'algorithme $k$-SELECT avec notre choix de pivot est de complexité :

<div>
$$
C(n) \leq \mathcal{O}(n) + C(n/5) + C(7n/10)
$$
</div>

{% endfaire %}

{% faire %}
En déduire que $C(n) = \mathcal{O}(n)$

{% endfaire %}

Un petit dernier pour la route. On a découpé notre tableau initial en paquets de 5.
{% faire %}
Pourquoi n'est il pas possible de le découper en paquets de 3 ?

{% endfaire %}

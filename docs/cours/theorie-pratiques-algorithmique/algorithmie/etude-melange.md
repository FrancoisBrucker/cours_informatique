---
layout: page
title:  "étude / mélanger un tableau"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithmie]({% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}) / [étude :  mélanger un tableau]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-melange.md %})
>
> prérequis :
>
>* [étude : l'exponentiation]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-exponentiation.md %})
>
{: .chemin}

Nous allons étudier ici deux algorithmes permettant de mélanger un tableau. Commençons par identifier le problème. Nous allons utiliser le problème suivant, qui consiste à rendre une permutation des $n$ premiers entiers :

* **nom** : permutation
* **entrée** : un tableau d'entiers
* **sortie** : une permutation aléatoire du tableau en entrée

> une permutation d'un tableau $T$ de taille $n$ est un tableau $T'$ de taille $n$ où $T'[i] = T[\sigma(i)]$ avec $\sigma$ une bijection de $[0 .. n-1]$.

L'algorithme que nous allons montrer ici nécessite que l'on puisse obtenir un entier aléatoire plus petit qu'un nombre donné $n$. On va donc considérer que l'on a une fonction `randint` de complexité $\mathcal{O}(1)$ qui résout le problème "randint" suivant :

* **nom** : randint
* **entrées** : deux entiers $a$ et $b$
* **sortie** : un entier aléatoire $c$ tel que $a \leq c \leq b$.

On ne va pas définir plus que ça la notion d'aléatoire en informatique. On va ici prendre la définition mathématique : rend un nombre entre $a$ et $b$ de façon équiprobable, et considérer que c'est ok.

> Il n'existe pas d'aléatoire au sens mathématique en informatique. On ne peut atteindre que des nombre [pseudo-aléatoires](https://fr.wikipedia.org/wiki/Pseudo-al%C3%A9atoire), mais c'est une autre histoire.

## remarques préliminaires

Attention, l'algorithme suivant :

```text
soit T un tableau à n cases
de i = 0 à n-1:
    T[i] = randint(0, n-1)
rendre T
```

Ne résout pas le problème "permutation" puisqu'il peut y avoir des répétitions.

## borne min du problème

Comme il faut rendre un tableau de longueur $n$, une borne minimum du problème "permutation" est de $\mathcal{O}(n)$. Mais rien ne dit qu'un tel algorithme existe.

## existence d'un algorithme

Avant de chercher plus loin commençons par montrer qu'il existe un algorithme pour résoudre le problème. Si l'on possède une liste de toutes les permutations possible, l'algorithme suivant fonctionne :

```text
soit P un tableau contenant une fois chaque permutation de T
i = randint(0, n! - 1)
rendre P[i]
```

Il nous reste à créer toutes les permutations possibles d'un tableau. C'est ce que fait l'algorithme suivant, récursif et en python.

### toutes les permutations

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight python linenos %}

def permutations(elements):
    if len(elements) == 0:
        return [[]]
    
    les_permutations = []
    for i in range(len(elements)):
        premier = elements[i]
        elements_sans_premier = elements[:i] + elements[i+1:]
        permutations_sans_premier = permutations(elements_sans_premier)
        for une_fin_de_permutation in permutations_sans_premier:
            permutation = [premier] + une_fin_de_permutation
            les_permutations.append(permutation)
    return les_permutations

{% endhighlight %}

Pour placer dans la liste de listes `P` toutes les permutations de `[0, 1, 2, 3, 4, 5]`, on lance l'algorithme comme ça : `P = permutations([0, 1, 2, 3, 4, 5])`.

Analysons cet algorithme pour vérifier qu'il fait bien ce qu'on pense qu'il fait (bien).

#### finitude

A chaque récursion, le tableau `elements` est strictement plus petit. En effet le tableau `elements_sans_premier` sur lequel porte la récursion est la restriction du tableau `elements` en supprimant l'élément d'indice `i` (`elements_sans_premier = elements[:i] + elements[i+1:]`).

Il arrivera donc une récursion où `elements` sera vide : le test de la ligne 2 stoppera la récursion.

#### preuve

on prouve par récurrence sur la taille du tableau `elements` que `permutations_rec(elements)` donne un tableau contenant toutes les permutations de `elements`.

   1. pour `len(elements) == 0` c'est clair.
   2. on suppose la propriété vrai pour `len(elements) == p`. Pour `len(elements) == p + 1`, par hypothèse de récurrence, le retour de la récursion `permutations_rec(elements_sans_premier)` sera l'ensemble des permutations de `elements[:i] + elements[i+1:]` pour une position `i` de `elements`. Pour un `i`  donné on obtient alors  toutes les permutations de `elements` ayant `elements[i]` en première position (on ajoute `elements[i]` à toutes les permutations de `elements[:i] + elements[i+1:]`). Comme `i` prend tous les indice de `elements`, on on obtient aufinal toutes les permutations du tableau `elements`.

#### complexité

La complexité de l'algorithme va dépendre de la taille $n$ du tableau `elements`. : on note sa complexité $C(n)$. Comme il est récursif, on va chercher une équation de récurrence que satisfait $C(n)$ à résoudre.

Complexité de chaque ligne :

1. $\mathcal{O}(1)$ définition de la fonction
2. $\mathcal{O}(1)$ un test
3. $\mathcal{O}(1)$ retour d'une constante
4.
5. $\mathcal{O}(1)$ affectation d'une constante
6. une boucle de $n$ itérations
7. $\mathcal{O}(1)$ une affectation d'un élément d'un tableau
8. $\mathcal{O}(n)$ car on crée un **nouveau** tableau de taille $n-1$
9. $C(n-1)$, c'est notre récursion.
10. une boucle de $\mathcal{O}((n-1)!)$ itérations (toutes les permutations d'un tableau à n-1 éléments)
11. $\mathcal{O}(n)$ car on crée un **nouveau** tableau de taille $n$
12. $\mathcal{O}(1)$, on ajoute un élément à la fin d'une liste (les tableau en pthon sont des listes, l'ajout d'un élément à la fin d'une liste est en temps constant)
13. $\mathcal{O}(1)$ retour d'une fonction

Ce qui donne :

$$
\begin{array}{lcl}
    C(n) = & & \mathcal{O}(1)\\
    & + & \mathcal{O}(1)\\
    & + & \mathcal{O}(1)\\
    & + & \mathcal{O}(1)\\
    & + & n \cdot (\\
    &  & \mathcal{O}(1)\\
    & + & \mathcal{O}(n)\\
    & + & C(n-1)\\
    & + & (n-1)! \cdot (\\
    & & \mathcal{O}(n)\\
    & + & \mathcal{O}(1)\\
    & & ))\\
    & + & \mathcal{O}(1)\\
\end{array}
$$

En simplifiant les $\mathcal{O}(1)$, on obtient l'équation de récurrence suivante :

$$
\begin{array}{lcl}
C(n) & = & \mathcal{O}(1) + n \cdot (\mathcal{O}(n) + C(n-1) + (n-1)! \cdot (\mathcal{O}(n)))\\
     & = & \mathcal{O}(1) + \mathcal{O}(n^2) + n \cdot C(n-1) + n! \cdot \mathcal{O}(n)\\
     & = & \mathcal{O}(n^2) + n \cdot C(n-1) + \mathcal{O}(n\cdot n!)\\
     & = & n \cdot C(n-1) + \mathcal{O}(n\cdot n!)\\
\end{array}
$$

On peut maintenant étendre la récurrence

$$
\begin{array}{lcl}
C(n) & = & n \cdot C(n-1) + \mathcal{O}(n\cdot n!)\\
     & = & n \cdot (n-1) \cdot C(n-2) + n \mathcal{O}(n-1)\cdot (n-1)!)) + \mathcal{O}(n\cdot n!)\\
     & = & n \cdot (n-1) \cdot C(n-2) + \mathcal{O}(n-1)\cdot (n)!)) + \mathcal{O}(n\cdot n!)\\
     & = & n \cdot (n-1) \cdot C(n-2) + \mathcal{O}((n + (n-1))n!)\\
     & = & ...\\
     & = & \Pi_{i=0}^p (n -i)\cdot C(n-i-1) + \mathcal{O}(\sum_{i=0}^p (n -i))n!)\\
     & = & n! \cdot C(0) + \mathcal{O}(\sum_{i=0}^{n-1} (n - i))n!)\\
\end{array}
$$

Comme $C(0) = \mathcal{O}(1)$ et que $\sum_{i=0}^{n-1}(n-i) = \mathcal{O}(n^2)$ On en déduit que :

$$C(n) = \mathcal{O}(n^2n!) = \mathcal{O}((n+2)!)$$

### algorithme final

```python
from random import randint

def melange(elements):
    P = permutations(elements)
    i = randint(0, len(P) - 1)
    return P[i]

```

Comme on a considéré que la complexité de `randint` étant de $\mathcal{O}(1)$, la complexité de `melange` est de l'ordre de la complexité de `permutations` donc : $\mathcal{O}((n+2)!)$ avec $n$ la taille du tableau `element`. On a donc maintenant également une borne max au problème, même si elle est gigantesque !

> L'algorithme `melange` n'est pas utilisable en pratique car [n! est trop gros]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-max-min.md %}#n_factoriel)

## Algorithme de Knuth / fisher-yates

L'algorithme que l'on va montrer maintenant, dit de [Knuth ou encore de fisher-yates](https://fr.wikipedia.org/wiki/M%C3%A9lange_de_Fisher-Yates), va également résoudre le problème "permutation", mais de façon bien plus élégante.

```python
from random import randint

def melange_knuth(elements):
    copie_elements = list(elements)
    for i in range(len(copie_elements)):
        j = randint(0, i)
        copie_elements[i], copie_elements[j] = copie_elements[j], copie_elements[i]
    return copie_elements
    
```

> montrer les proportions (`from collections import Counter`) avec seaborn
> résout la complexité du problème
{: .tbd}

## algorithme de python

* random randint
* shuffle

## attention !

### maths

suite de transpositions

## ref

* <https://possiblywrong.wordpress.com/2014/12/01/card-shuffling-algorithms-good-and-bad/>
* <https://blog.codinghorror.com/the-danger-of-naivete/>
* <https://draftsim.com/mtg-arena-shuffler/> ce que les maths disent de l'aléatoire vs ce que les humains disent de l'aléatoire
* <https://www.stashofcode.fr/tri-aleatoire-des-elements-dun-tableau/>


## mélanger des listes ?

On s'est appuyé sur la fonction [shuffle du module random](https://docs.python.org/3/library/random.html#random.shuffle) pour mélanger des listes.

Mais sommes-nous bien sur que le mélange est bien équiprobable ? Sinon nos mesures de complexité en moyenne seraient tous faux...

Rassurez vous c'est le cas. Elle utilise la méthode de mélange de [Fisher-Yates](https://fr.wikipedia.org/wiki/M%C3%A9lange_de_Fisher-Yates), qui est un algorithme linéaire permettant d'obtenir toutes les permutations possibles de façon équiprobable.

Ce qui est marrant c'est que cet algorithme est *"l'inverse"* d'un tri par sélection. 

Implémentez cet algorithme et vérifiez que pour la liste des 4 premiers entiers vous obtenez bien (sur un grand nombre d'essais) à peut prêt le même nombre des 24 permutations possibles.

Si vous voulez en savoir un peu plus sur cet algorithme et de comment générer un nombre aléatoire en python : 
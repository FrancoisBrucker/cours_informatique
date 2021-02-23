---
layout: page
title:  "corrigé Test 6 : gloutons"
category: cours
tags: informatique cours 
---

## Introduction

Cet exercice est classique et s'appelle le [sac à dos fractionnel](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos#Variables_continues) (dans le test, les prix étaient déjà au kilo).

### algorithme

* entrée : liste de produits, chaque produit étant une liste [prix au kilo, kg, nom]
* sortie : liste de produits [nom, kilo] où nom est le nom du produit dans la liste d'entrée et kilo, le nombre de kilo pris.

``` python
def sac_a_dos_fractionel(produits, masse_totale):
    produits.sort()
    produits.reverse()
    sac_a_dos = []
    for i in range(len(produits)):
        prix, kilo, nom = produits[i]

        if masse_total >= kilo:
            sac_a_dos.append((nom, kilo))
            masse_totale -= kilo
        else:
            sac_a_dos.append((nom, masse_totale))
            masse_totale = 0        

    return sac_a_dos
```

On trie la liste dans le code. Comme le 1er élément de chaque liste est le prix au kilo, le résultat sera une liste de produit trié par prix au kilo croissante. On la retourne (avec la méthode `reverse()`) pour avoir les produit triés par prix au kilo décroissant.

**Remarques** :

* Astuce du tri : lorsque l'on trie une liste de liste, python utilise l'[ordre lexicographique](https://fr.wikipedia.org/wiki/Ordre_lexicographique). Cela permet ici de trier sur les prix volumique tout en conservant l'indice du tableau d'origine (le deuxième élément de la liste n'intervient dans le tri que si les 2 premiers éléments sont identique, ce qui ne change pas le tri par prix volumique)
* attention, les méthodes de liste `sort` et `reverse` ne rendent rien. Elles modifient la liste. De là `l.sort().reverse()` **ne fonctionne pas** puisque cette commande signifie que l'on applique la méthdoe `reverse` à l'objet donné en retour de `l.sort()`. Or comme `l.sort()` ne rend rien elle retourne l'objet `None` (l'objet *rien du tout* en python) qui ne possède pas de méthode `reverse`. C'est ce que dit le message d'erreur quand on essaie de le faire : `AttributeError: 'NoneType' object has no attribute 'reverse'`  (le type de l'objet `None` (comme le tpe des entier est `int` ou le type des réels est `float`) est `NoneType` (il a un type à lui)).

#### preuve

On peut remarquer que l'algorithme glouton prend toujours tout le produit disponible jusqu'au dernier choix où il ne prend qu'une fraction de celui-ci (la place restante) pour finir de remplir le sac-à-dos .

Pour notre solution, on note $(k_0, k_1, \dots, k_n)$ les kilos choisis dans l'ordre de choix de l'algorithme glouton.
On suppose que notre solution n'est pas optimale et, parmi toutes les solutions optimales possible, on en prend une qui correspond le plus longtemps possible avec la solution rendue par l'algorithme. Soit alors $0 \leq i <n$ le plus petit indice telle que la solution optimale et celle rendue par l'algorithme est différente.  La solution optimale est alors $(k_0, \dots, k_{i-1}, k'_i, \dots, k'_n)$.

On peut enfin, sans perte de généralité, choisir la solution optimale ayant $k_i'$ le plus grand possible parmi toutes les solutions optimales coïncidant avec la solution de l'algorithme glouton jusqu'à $k_{i-1}$.

Jusqu'à l'étape $i-1$ tous les choix sont identiques donc une fois placés les $i$ premiers produits (les produits d'indices $0$ à $i-1$) avec le même kilo, il reste la même place dans le sac-à-dos et pour notre algorithme et pour la solution optimale. De là, par construction de l'algorithme glouton (on prend à chaque choix soit tout le produit soit juste assez pour finir de remplir tout le sac) les kilos $k'_i$ de la solution optimale pour le produit d'indice $i$ est forcément plus petit strictement que $k_i$.

Donc :

* soit $k'_j = 0$ pour tout $j > i$ et notre solution est meilleure que la solution optimale, ce qui est impossible par hypothèse,
* soit il existe $k'_j >0$ pour un $j>i$. On peut alors diminuer d'un kilo $k_j'$ pour augmenter d'un kilo $k_i'$ et obtenir une solution strictement  meilleure que la solution optimale : c'est impossible.

Notre hypothèse arrivant à une contradiction, elle était fausse : la solution de l'algorithme glouton est optimale.

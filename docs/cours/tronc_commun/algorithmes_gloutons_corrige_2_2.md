---
layout: page
title:  "Algorithmes gloutons : corrigé"
category: cours
tags: informatique cours  corrigé
author: "François Brucker"
---


## exercice 5 : le problème du sac à dos


### on essaie 

Exemple (traduit) tiré de <https://home.cse.ust.hk/~dekai/271/notes/L14/L14.pdf> :

* produit A, 2kg, 100kcal
* produit B, 2kg, 10kcal
* produit C, 3kg, 120kcal


De 1 à 7kg :

  - 1kg : rien
  - 2kg : A
  - 3kg : C
  - 4kg : C
  - 5kg : A+C
  - 6kg : A+C
  - 7kg et plus A+B+C

Vous voyez qu'il y a des sauts et que ce n'est pas toujours le nombre maximum d'objet qui fonctionne.

### sac à dos fractionnel

  - sac de 4kg : 2 kg de A, 2kg de C
  - sac de 5 kg : 3kg de C , 2kg de A

### algorithme glouton

* entrée : liste de produits, chaque produit étant une liste [prix, kg, nom]. 
* sortie : liste de produits [indice, ratio] où indice est l'indice du produit dans la liste d'entrée et 0 < ratio <= 1  le ratio de produit prit.

#### code 

~~~ python 
def sac_a_dos_fractionel(produits, masse_totale):
    prix_volumique_produits = []
    for i, produit in enumerate(produits):
        prix, volume, nom = produit

        prix_volumique_produits.append((prix / volume, i))

    prix_volumique_produits.sort()
    prix_volumique_produits.reverse()

    sac_a_dos = []
    for produit in prix_volumique_produits:
        prix_volumique, indice = produit

        ratio = min(1, masse_totale / produits[indice][1])
        masse_totale -= ratio * produits[indice][1]

        sac_a_dos.append((indice, ratio))

    return sac_a_dos
~~~ 

En exécutant le programme avec ces paramètres : `[[100, 2, "A"], [10, 2, "B"], [120, 3, "C"]]` on obtient : `[(0, 1), (2, 0.6666666666666666), (1, 0.0)]`  c'est à dire : 

  - 1 du produit "A" (d'indice 0)
  - 2/3 du produit "C" (d'indice 2)
  - 0 du produit "B" (d'indice 1)

*Nota Bene* : On a utilisé quelques astuces de programmation python :

* `enumerate` : appliqué à une liste retourne un énumérateur qui rend un couple (indice, element) pour chaque élément de la liste. <http://book.pythontips.com/en/latest/enumerate.html#enumerate>
* Astuce du tri : lorsque l'on trie une liste de liste, python utilise l'[ordre lexicographique](https://fr.wikipedia.org/wiki/Ordre_lexicographique). Cela permet ici de trier sur les prix volumique tout en conservant l'indice du tableau d'origine (le deuxième élément de la liste n'intervient dans le tri que si les 2 premiers éléments sont identique, ce qui ne change pas le tri par prix volumique)
* attention, les méthodes de liste `sort` et `reverse` ne rendent rien. Elles modifient la liste. De là `l.sort().reverse()` **ne fonctionne pas** puisque cette commande signifie que l'on applique la méthdoe `reverse` à l'objet donné en retour de `l.sort()`. Or comme `l.sort()` ne rend rien elle retourne l'objet `None` (l'objet *rien du tout* en python) qui ne possède pas de méthode `reverse`. C'est ce que dit le message d'erreur quand on essaie de le faire : `AttributeError: 'NoneType' object has no attribute 'reverse'`  (le type de l'objet `None` (comme le tpe des entier est `int` ou le type des réels est `float`) est `NoneType` (il a un type à lui)).

#### Preuve

Même place dans le sac-à-dos et pour notre algorithme et pour la solution optimale. De là, par construction de l'algorithme glouton (on prend à chaque choix soit tout le produit soit juste assez pour finir de remplir tout le sac) le ratio $r'_i$ de la solution optimale pour le produit d'indice $i$ est forcément plus petit strictement que $r_i$.

Donc : 

* soit $r'_j = 0$ pour tout $j > i$ et notre solution est meilleure que la solution optimale, ce qui est impossible par hypothèse,
* soit il existe $r'_j >0$ pour un $j>i$. On pose alors $\epsilon = \min ((r_i -r'_i) * p_i, r'_j * p_j)$ avec $p_k$ la quantité du produit $k$. On a que $\epsilon >0$ et  la solution $(r_1, \dots, r_{i-1}, r'_i + \epsilon / p_i, r'_{i+1}, \dots r'_{j-1}, r'_j - \epsilon / p_j, r'_{j+1}, \dots, r'_n)$ est admissible, est meilleure que la solution optimale car le prix volumique du produit $j$ est inférieur à celui du produit $i$ et est telle que le ratio du produit $i$ est strictement plus grand que celui de la solution optimale. Ceci est impossible par hypothèse.

Notre hypothèse arrivant à une contradiction, elle était fausse : la solution de l'algorithme glouton est optimale.



### sac à dos non fractionnel

#### si on ne peut pas couper ?

Notre algorithme glouton ne fonctionne pas si on ne peut pas prendre de factions. En effet il rendrait : "A" et "B" (puisque une fois mis "A" on ne peut pas mettre "C") de calories totales 110kcal, alors que la réponse optimale serait de prendre "C" qui rapporte 120kcal.

#### algorithme

On suppose que l'on a une matrice $S[i][j]$ correspondant à un couple $(w, elements)$, où $w$ est la valeur de la solution optimale pour les $i$ premiers objets et un poids de $j$ kilos et $elements$ la listes des objets pris dans ce sac optimal.

L'algorithme est alors : 

  - pour $i$ allant de $1$ à $n$
    - pour $j$ allant de $0$ à $W$ kilos
      - si $j \geq w_i$ alors la valeur de $S[i][j]$ est le maximum de :
        - la valeur de $S[i-1][j]$ (dans ce cas là on ne prenant pas l'objet $i$ dans la solution)
        - la valeur de $S[i-1][j - w_i]$ plus $p_i$ (dans ce cas on prend l'objet $i$ dans la solution)
      - sinon la soluton $S[i][j]$ est égale à la solution $S[i-1][j]$


Il est clair que l'algorithme ci-dessus est juste une écriture de l'équation de récurrence, il est donc exact.

Il n'est pas glouton car on ne peut utiliser la technique de preuve par récurrence pour le démontrer. C'est en fait une autre technique d'algortime qui est utilise ici : **la programmation dynamique**. Cette technique consiste à trouver une relation de récurrence qui lie les solutions partielles entres elles.

#### complexité

La complexité en nombre d'opération de l'algorithme est en $\mathcal{O}(n * W)$

#### hein ?

Ca semble être une complexité polynomiale, mais c'est dans le stockage des variables qu'on prend une place exponentielle par rapport à la taille en entrée du problème ! 

**En algorithmie la complexité est calculée en nombre d'opérations par rapport à la taille de l'entrée.**

Ici, le poids $W$ est codé avec $\ln_2(W)$ bits en machine, donc la place mémoire prise pour stocker nos entrées est de : 

  - $\ln_2(W)$ pour encoder le poids du sac à dos
  - $n * \ln_2(P)$ où $P$ est la valeur nutritionnelle max pour stocker les poids des $n$ produits,
  - $n * \ln_2(W)$  pour stocker les poids des $n$ produits (on suppose que chaque produit pèse moins que le poids du sac  dos),

On a donc besoin en tout de $\mathcal{O}(n * \ln_2(A))$ cases mémoires pour stocker toute notre entrée (avec $A$ le plus grand nombre)

Notre tableau à $n * W$ cases, donc le seul fait de le parcourir prend un nombre exponentiel d'opérations par rapport à notre taille d'entrée.


Ouf, nous voilà rassuré. Ce n'est pas la peine de brûler tous les livres d'algortihmie. Les problèmes les plus dur du monde sont effectivement dur à résoudre (un nombre exponentiel d'opérations en temps et/ou en mémoire).


> **Nota Bene :** commencer à regarder les nombres comme prenant de la place ($\ln_2(x)$ case pour un nombre valant $x$) peut vous doner le tourni. En effet, que devient la complexité d'un tri par exemple ? Est-ce toujours $\mathcal{O}(n\ln(n))$ opérations ? Cela ne dépend pas de la valeur des nombres à trier ? 
> Si bien sur ça dépend des nombres à trier. Mais si P est la valeur max des nombres à trier. On a besoin de $\mathcal{O}(n\ln_2(P))$ places mémoire pour les stocker et comme la comparaisons de deux nombres prend $\mathcal{O}(\ln_2(P))$ opérations, la complexité toale de l'algorithme est alors de $\mathcal{O}(n\ln(n)\ln_2(P))$ opérations qui est toujours en  $\mathcal{O}(n\ln(n))$ opérations par rapport à la taille en entrée.

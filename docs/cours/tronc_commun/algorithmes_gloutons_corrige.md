---
layout: page
title:  "Algorithmes gloutons corrigé"
category: cours
tags: informatique cours  corrigé
authors: "François Brucker"
---


## exercice 1 : le gradient

On suppose que l'on a une fonction $$f$$ continue et dérivable sur $$\mathbb{R}$$. 

l'algorithme fonctionne avec un élément initial $$x_0$$. A l'étape $i$ de l'algorithme on pose 

\$$x_{i+1} = x_i - \alpha f'(x_i) $$

C'est bien un algorithme glouton puisque la construction de la solution ne dépend que d'une condition initiale et que la solution au pas $$i+1$$ est construite à partir de la solution au pas $$i$$ sans jamais remettre en cause les décisions prisent aux pas précédents.

La constante $$\alpha$$ est un paramètre dit de vitesse de convergence. Vous pouvez allez voir [ce tuto](https://www.charlesbordet.com/fr/gradient-descent/#cest-quoi-la-descente-de-gradient-) pour une petite explication sur cet algorithme. Il faut faire un peu attention avec le paramètre de pente parce que :

  - il doit être positif car il se dirige à l'oppose de la valeur de la dérivée
  - s'il est trop petit on va converger trop lentement
  - s'il est trop grand on risque de rater la solution
  
De part la définition de la dérivée, l'algorithme va suivre la pente et se loger dans un minimum : il va osciller autour d'une valeur où la dérivée change. Si la fonction est concave on va bien trouver le minimum global, sinon on peut se retrouver dans un minimum local.

## ordonnancement

### ensemble compatible

- si l'ordonnancement par date croissante permet de tout vendre il est compatible
- s'il existe un autre ordonnancement avec la tâche $$j$$ placé avant la tâche $$i$$ alors que $$d_j > d_i$$, on peut échanger la tâche $$i$$ et la tâche $$j$$ et l'ordonnancement reste compatible

### algorithme

  - initialisation : si une solution ne contient pas l'élément de prix maximum on l'échange avec le 1er élément choisi et la solution reste compatible tout en ayant un profit plus grand
  - récurrence : clair. S'il reste dans les solutions possible l'élément qu'on rajoute à l'étape $$i$$ on peut toujours le rendre à la place de celui pris par l'autre solution pour augmenter le profit.

## optimalité

### Algo général de rendu de pièces

* **Problème** : "comment rendre R sous en un nombre minimum de pièces"
* **algo glouton** : 
    * "répéter : choisir la pièce de plus grande valeur $v$ qui ne dépasse pas la somme restante R puis poser R = R - v". 
    * ce qui est équivalent à :
        1. choisir la plus grande valeur $v$ de pièce plus petite que $R$
        2. donner $p = R // v$ pièces
        3. R = R - p * v
        4. revenir en 1. si R > 0
    * **complexité** : tri des valeur de pièce + une opération par pièce (division puis soustraction). Comme il suffit de trier une fois pour toute, la complexité peut être de l'ordre du nombre de pièces.

### Preuve d'optimalité pour un système de pièce valant 1, 2 et 5


Si on a une solution optimale pour un problème donné, quelques cas seulement sont possibles pour le nombre de pièces de 2 et de 1 :
* pas plus de 2 pièces de 2 : on peut rendre moins de pièce en transformant 3 pièces de 2 en 1 pièce de 5 plus une pièce de 1
* pas plus de 1 pièce de 1 : sinon on transforme 2 pièces de 1 en 1 pièce de 2


* on ne peux pas avoir 2 pièces de 2 et 1 pièce de 1 : sinon on peut convertir 2 pièces de 2 et 1 pièce de 1 en 1 pièce de 5.

Ceci prouve que la somme d'argent rendu en pièce de 2 et de 1 ne peut dépasser 4.

Pour prouver l'algorithme on doit prouver les 2 propriétés :

* initialisation : On regarde le 1er choix de l'algorithme.
    * Si le nombre de pièce à rendre est 0, 1, 2, 3 ou 4, notre algorithme va rendre à chaque fois le nombre optimal de pièce. Son premier choix est donc toujours contenu dans une solution optimale : la propriété est ok.
    * si le nombre de pièce est plus grand ou égal à 5, l'algorithme va choisir de rendre $p = R // 5$ pièces de 5.  si on suppose que toute solution optimale rend un nombre différent de $p$ pièces de 5, toute solution optimale en rend forcement strictement moins que $p$ puisque $(p+1) * 5$ est strictement plus grand que le nombre de sous à rendre initial. Mais si les solutions optimales rendent moins de $p$ pièces de 5 la somme à rendre en pièce de 2 et de 1 est strictement plus grande que 5 ce qui est impossible : la propriété est ok.
* récurrence : Les solutions optimales choisissent toute le même nombre de pièce de 5 que notre algorithme. La valeur totale des pièces de 2 et de 1 ne peut donc pas excéder 4 pour les solutions optimales et donc le nombre de pièces coïncide avec notre algorithme (puisqu'il est optimal lorsqu'il faut rendre 4 ou moins).

### système de pièces quelconque ?

Attention, ne marche pas pour tous les systèmes de pièces  : exemple 1, 3, 4. Pour rendre 6 il donne 4 + 1 + 1 alors que c'est 3 + 3 le mieux.

Il est clair que le système supercroissant fonctionne car c'est exactement la condition de la preuve pour que ça fonctionne.

Le système de pièce européen fonctionne puisque l'on a des pièces billets de : 1, 2, 5, 10, 20, 50, 100 et 200 :

  - 5 > 2+1
  - 10 > 5+2+1
  - 20 > 10+5+2+1
  - 50 > 20+10+5+2+1
  - 100 > 50+20+10+5+2+1
  - 200 > 100+50+20+10+5+2+1


*Nota Bene* : 

* c'est pourquoi il n'y a pas de billets de 7 euros (10 = 7 + 2 + 1, mais surtout 5 + 5). Dingue, non ?
* ce n'est pas la seule solution puisque les américains ont des pièces de 25c (les quarter) 
* peut poser des soucis : les machines à café vous indiquent qu'elles ne peuvent plus vous rendre la monnaie car il n'y a plus de pièces d'une valeur particulière, alors qu'en réalité elle disposent de la somme à rendre en utilisant une autre combinaison.


## Problèmes de salles de cinéma

Chaque film est décrit par un couple $(d, f)$ où $d$ est la date de début du film et $f$ la date de fin. 

### voir un maximum de films

On va construire l'algorithme glouton en utilisant la création classique de ceux-ci : on trouve un ordre dans lequel classer les entrées puis on regarde les entrées dans cet ordre et on les ajoute à la solution si c'est possible.

L'ordre que l'on va choisir est celui de la date de fin croissante.

En effet, si l'on classe les séances de cinéma par 

* durée croissante : l'ensemble de films $$[(1, 3), (3, 5), (5, 7), (2.5, 3.5), (4.5, 5.5)]$$ produit un contre exemple,
* date de début croissante : l'ensemble de films $$[(1, 10), (2, 3), (3, 4)]$$ produit un contre exemple,

#### algorithme

* entrée : liste de films, chaque liste étant une liste [depart, fin, nom]. 
* sortie : liste d'indices de films où indice est l'indice du film dans la liste d'entrée.

~~~ python
def nombre_films_maximal(films):
    film_a_trier = []
    for i, film in enumerate(films):
        date_depart, date_fin, nom = film

        film_a_trier.append((date_fin, i))

    film_a_trier.sort()

    films_a_voir = [0]
    for fin, i in film_a_trier:
        fin_dernier_film = films[films_a_voir[-1]][1]
        debut_nouveau_film = films[i][0]
        if fin_dernier_film <= debut_nouveau_film:
            films_a_voir.append(i)

    return films_a_voir
~~~

La sortie de l'algorithme glouton correspond à un ordre de visionnage de films maximisant le nombre de films vus.


**Nota Bene** : On a utilisé quelques astuces de programmation python :

  - `l[-1]` rend le dernier élément d'une liste. 
  - `for a, b in l` si chaque élément d'une liste est une liste, on peut mettre autant de variables que d'élément dans une boucle `for`.
 
 
#### preuve

On prouve notre algorithme comme tout algorithme glouton : on suppose que l'algorithme glouton ne donne pas une solution optimale et on considère une solution optimale coïncidant le plus longtemps possible avec la solution donnée par celui-ci.

Soit $$i$$ l'indice de la première différence. On note $$f_i$$ le film choisi par le glouton et $$f'_i$$ le film (différent de $$f_i$$) choisi par la solution optimale :

* la date de fin de $$f'_i$$ est plus grande que la date de fin de $$f_i$$ par construction de la solution par l'algorithme glouton.
* la date de début de $$f'_i$$ est avant la date de fin de $$f_i$$ sinon on pourrait ajouter $$f_i$$ à la solution optimale et rendre une solution avec strictement plus de films

Les deux remarques ci-dessus amènent au fait que l'on peut construire une nouvelle solution en échangeant $$f'_i$$ par $$f_i$$ dans la solution optimale. Comme cette nouvelle solution a autant de films que la solution optimale, elle est aussi optimale. Ceci est impossible par hypothèse (on prend une solution optimale coïncidant le plus longtemps possible avec la solution de l'algorithme glouton) : notre hypothèse était fausse, l'algorithme glouton est optimal.

### nombre minium de salles pour placer tous les films en stock

On va ici classer les films par date de début croissante. On commence par 0 salles de cinéma.

 En analysant dans cet ordre les films, on cherche s'il existe une salle à laquelle on peut rajouter le film (la date de fin du dernier film de la salle est plus tôt que le début du nouveau film). Si oui on rajoute le film à cette salle, si non on crée une nouvelle salle.

#### Algorithme

``` 
def nombre_salle_min_films(films):
    film_a_trier = []
    for i, film in enumerate(films):
        date_depart, date_fin, nom = film

        film_a_trier.append((date_depart, i))

    film_a_trier.sort()

    salles = []
    for debut, i in film_a_trier:
        nouvelle_salle = True
        for salle in salles:

            fin_dernier_film = films[salle[-1]][1]
            if debut >= fin_dernier_film:
                salle.append(i)
                nouvelle_salle = False
                break

        if nouvelle_salle:
            salles.append([i])

    return salles
```
    

*Nota Bene* : 

* on a utilisé l'instruction [`break`](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) qui quite la boucle la plus imbriquée. C'est pratique pour designer des boucles où l'on recherche quelque chose dans un ensemble (ici une salle où ajouter notre film) et qu'une fois qu'on l'a trouvé on sort de la boucle.
* on a une sentinelle nommée `nouvelle_salle` dont le but est savoir si on a trouvé une salle possible dans la boucle. 
* Les objets peuvent avoir [plusieurs noms](https://informatique.centrale-marseille.fr/tutos/post/python-bases.html#variables) mais c'est **toujours** le même objet. Ici la salle où ou ajoute un films est un élément de la liste `salles` et aussi la variable `salle` de la boucle for. La méthode append modifie donc cet objet. 

 
#### Preuve

La preuve est ici aisée car si on rajoute une salle pour loger un nouveau film $f$, ca veut dire que pour toutes les $k$ salles actuelle il y a un film qui n'est pas fini pendant le début du nouveau film. Ca signifie qu'il existe $k$ films dont le début est avant $f$ et la fin après $f$ : il faut donc au moins $k+1$ salles pour jouer tous ces films en parallèle.

## sac à dos 

### on essaie 

Exemple (traduit) tiré de <https://home.cse.ust.hk/~dekai/271/notes/L14/L14.pdf> :

* produit A, 2kg, 100€
* produit B, 2kg, 10€
* produit C, 3kg, 120€


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

Même place dans le sac-à-dos et pour notre algorithme et pour la solution optimale. De là, par construction de l'algorithme glouton (on prend à chaque choix soit tout le produit soit juste assez pour finir de remplir tout le sac) le ratio $$r'_i$$ de la solution optimale pour le produit d'indice $$i$$ est forcément plus petit strictement que $$r_i$$.

Donc : 

* soit $$r'_j = 0$$ pour tout $$j > i$$ et notre solution est meilleure que la solution optimale, ce qui est impossible par hypothèse,
* soit il existe $$r'_j >0$$ pour un $$j>i$$. On pose alors $$\epsilon = \min ((r_i -r'_i) * p_i, r'_j * p_j)$$ avec $$p_k$$ la quantité du produit $$k$$. On a que $$\epsilon >0$$ et  la solution $$(r_1, \dots, r_{i-1}, r'_i + \epsilon / p_i, r'_{i+1}, \dots r'_{j-1}, r'_j - \epsilon / p_j, r'_{j+1}, \dots, r'_n)$$ est admissible, est meilleure que la solution optimale car le prix volumique du produit $$j$$ est inférieur à celui du produit $$i$$ et est telle que le ratio du produit $$i$$ est strictement plus grand que celui de la solution optimale. Ceci est impossible par hypothèse.

Notre hypothèse arrivant à une contradiction, elle était fausse : la solution de l'algorithme glouton est optimale.

#### si on ne peut pas couper ?

Notre algorithme ne fonctionne pas si on ne peut pas prendre de factions. En effet il rendrait : "A" et "B" (puisque une fois mis "A" on ne peut pas mettre "C") de prix total 110€, alors que la réponse optimale serait de prendre "C" qui rapporte 120€.


### sac à dos non fractionnel optimal

#### algorithme

On suppose que l'on a une matrice $$S[i][j]$$ correspondant à un couple $$(w, elements)$$, où $$w$$ est la valeur de la solution optimale pour les $i$ premiers objets et un poids de $j$ kilos et $$elements$$ la listes des objets pris dans ce sac optimal.

L'algorithme est alors : 

  - pour $$i$$ allant de $$1$$ à $$n$$
    - pour $$j$$ allant de $$0$$ à $$W$$ kilos
      - si $$j \geq w_i$$ alors la valeur de $$S[i][j]$$ est le maximum de :
        - la valeur de $$S[i-1][j]$$ (dans ce cas là on ne prenant pas l'objet $$i$$ dans la solution)
        - la valeur de $$S[i-1][j - w_i]$$ plus $$p_i$$ (dans ce cas on prend l'objet $$i$$ dans la solution)
      - sinon la soluton $$S[i][j]$$ est égale à la solution $$S[i-1][j]$$


Il est clair que l'algorithme ci-dessus est juste une écriture de l'équation de récurrence, il est donc exact.

Il n'est pas glouton car on ne peut utiliser la technique de preuve par récurrence pour le démontrer. C'est en fait une autre technique d'algortime qui est utilise ici : **la programmation dynamique**. Cette technique consiste à trouver une relation de récurrence qui lie les solutions partielles entres elles.

#### complexité

La complexité en nombre d'opération de l'algorithme est en $$\mathcal{O}(n * W)$$

#### hein ?

Ca semble peut, mais en fait c'est beacuoup ! Cette complexité ne dépend pas polynomialement de la taille du problème en entrée. En effet, le poids $$W$$ est codé avec $$log_2(W)$$ bits en machine, donc le nombre d'opérations pour résoudre le problème du sac à dos est ici exponentiel par rapport à la taille en entrée.

Ouf, nous voilà rassuré. Ce n'est pas la peine de brûler tous les livres d'algortihmie. Les problèmes les plus dur du monde sont effectivement dur à résoudre (un nombre exponentiel d'opérations).



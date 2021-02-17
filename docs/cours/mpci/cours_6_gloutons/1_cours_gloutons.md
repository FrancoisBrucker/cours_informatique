---
layout: page
title:  "Algorithmes gloutons"
category: cours
tags: informatique cours 
authors: "François Brucker"
---



## But

Montrer l'intérêt des algorithmes gloutons, la façon de les construire et de prouver qu'ils fonctionnent. On s'attachera dans cette séance tableau à prouver qu'ils rendent une solution optimale à un problème donné.

On va voir la construction et la preuve des algorithmes gloutons à l'aide d'exemples, de plus en plus complexes :

1. [le rendu de pièce](#exemple--le-rendu-de-pièces)
2. [l'allocation de ressources](#exemple--allocation-de-salles-de-cinéma)
3. [ordonnancement](#exemple--ordonnancement)

## Algorithmes gloutons

Un [algorithme glouton](https://fr.wikipedia.org/wiki/Algorithme_glouton) choisit à chaque étape la meilleure possibilité localement. Ce type d'algorithmes est très utilisé pour résoudre des problèmes où l'on veut une réponse rapide, mais pas forcément une réponse optimale. D'un point de vue théorique, ces algorithmes sont extrêmement importants. Il sont, par exemple, en bijection avec la [structure de matroïde](https://fr.wikipedia.org/wiki/Matro%C3%AFde).

Intérêt :

* donne toujours un résultat
* souvent de complexité faible

Problème :

* ne donne pas forcément le meilleur résultat : une *heuristique*
* pas forcément de solution unique

Pour beaucoup de problèmes d'optimisation, un algorithme glouton est optimal pour une version simplifiée du problème. Comme l'algorithme va vite, on peut recommencer plusieurs fois pour trouver une meilleure solution.

### optimalité et glouton

Les problèmes d'optimalité demandent de trouver, parmi un ensemble de solutions possible, une solution minimisant (ou maximisant) un critère. Par exemple :

* pour un ensemble de coûts de constructions possibles d'une voiture, trouver celle qui minimise le coûts tout en maximisant la qualité totale des pièces,
* parmi tous les parcours passant par un ensemble de villes donné, choisir celui qui minimise le nombre de kilomètres parcourus
* maximiser le nombre de films projetés dans un multiplexe de cinéma
* ...

La difficulté de ces problèmes vient du fait que l'on ne peut a priori pas trouver la meilleure solution sans les examiner toutes. Et s'il y a beaucoup de solutions ça peut prendre vraiment beaucoup de temps.

Certains problèmes cependant permettent d'être résolus en construisant petit à petit une solution, sans jamais remettre en cause ses choix. On peut alors souvent trouver très rapidement la meilleure solution possible. On peut également utiliser cette solution construite petit à petit pour trouver une solution approchée à un problème plus général. Cette classe d'algorithmes qui construit itérativement d'une solution est appelée *algorithmes gloutons*.

### condition nécessaire et suffisante d'optimalité

Pour qu'un algorithme glouton **trouve une solution optimale** il faut :

* **initialisation** : montrer qu'il existe une solution optimale contenant le 1er choix de l'algorithme
* **récurrence** : montrer que la première différence entre une solution optimale et la solution de l'algorithme ne peut résulter en une meilleure solution. Pour cela on cherchera une solution optimale dont les choix coïncident le plus longtemps possible avec la solution donnée par notre algorithme et on prouvera qu'elles coïncident jusqu'à la fin.

## exemple : le rendu de pièces

### Un système de pièce particulier

Proposons un algorithme glouton permettant de rendre la monnaie d'un achat en un nombre minimum de pièces valant 5, 2 et 1 pokédollar.

Cet algorithme doit répéter : choisir la pièce de plus grande valeur $v$ qui ne dépasse pas la somme restante R puis poser R = R - v".

#### algorithme : rendu de pièce

* **Problème** : "comment rendre R sous en un nombre minimum de pièces"
* **algo glouton** :
  1. choisir la plus grande valeur $v$ de pièce plus petite que $R$
  2. donner $p = R // v$ pièces
  3. $R = R - p * v$
  4. revenir en 1. si R > 0
* **complexité** : tri des valeur de pièce + une opération par pièce (division puis soustraction). Comme il suffit de trier une fois pour toute, la complexité peut être de l'ordre du nombre de pièces.

#### Preuve d'optimalité pour un système de pièce valant 1, 2 et 5

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
Démontrez que votre algorithme est bien optimal.

### système de pièces quelconque ?

On peut démontrer que [le système de pièce européen fonctionne](https://cm2.ens.fr/sites/default/files/Algorithmes%20gloutons%20avec%20la%20classe_v4.pdf) (page 7. Mais tout le reste est bien intéressant aussi) avec les pièces et billets de : 1, 2, 5, 10, 20, 50, 100 et 200.

Attention, ne marche pas pour tous les systèmes de pièces :

* exemple 1, 3, 4. Pour rendre 6 il donne 4 + 1 + 1 alors que c'est 3 + 3 le mieux.
* 1, 6, 11, 19 ne fonctionne pas non plus pour 22 par exemple (le système est cependant super-croissant).

**Remarques** :

* c'est pourquoi il n'y a pas de billets de 7 euros (10 = 7 + 2 + 1, mais surtout 5 + 5). Dingue, non ?
* ce n'est pas la seule solution puisque les américains ont des pièces de 25c (les quarter)
* peut poser des soucis : les machines à café vous indiquent qu'elles ne peuvent plus vous rendre la monnaie car il n'y a plus de pièces d'une valeur particulière, alors qu'en réalité elle disposent de la somme à rendre en utilisant une autre combinaison.

## exemple : allocation de salles de cinéma

Un gérant de cinéma a en sa possession $m$ films caractérisés chacun par des couples ($d_i$, $f_i$) où $d_i$ est l'heure de début du film et $f_i$ l'heure de fin. Il se pose 2 problèmes :
  
* Quel est le nombre maximum de films que je peux voir en une journée ?
* Quel est le nombre minimum de salles à avoir pour visionner tous les films en stock.

Chaque film est décrit par un couple $(d, f)$ où $d$ est la date de début du film et $f$ la date de fin.

### voir un maximum de films

On cherche à rendre une liste maximale de films à voir en une journée.

On va construire l'algorithme glouton en utilisant la création classique de ceux-ci : on trouve un ordre dans lequel classer les entrées puis on regarde les entrées dans cet ordre et on les ajoute à la solution si c'est possible.

L'ordre que l'on va choisir est celui de la date de fin croissante.

En effet, si l'on classe les séances de cinéma par :

* durée croissante : l'ensemble de films $[(1, 3), (3, 5), (5, 7), (2.5, 3.5), (4.5, 5.5)]$ produit un contre exemple,
* date de début croissante : l'ensemble de films $[(1, 10), (2, 3), (3, 4)]$ produit un contre exemple,

#### algorithme : maximum de films

* entrée : liste de films, chaque liste étant une liste `[depart, fin, nom]`.
* sortie : liste d'indices de films où indice est l'indice du film dans la liste d'entrée.

```python
def nombre_films_maximal(films):

    films.sort(key=lambda x: x[1])

    films_a_voir = [films[0]]
    for film in films:
        fin_dernier_film = films_a_voir[-1][1]
        début_nouveau_film = film[0]
        if fin_dernier_film <= début_nouveau_film:
            films_a_voir.append(film)

    return films_a_voir
```

La sortie de l'algorithme glouton correspond à un ordre de visionnage de films maximisant le nombre de films vus.

**remarques** : On a utilisé quelques astuces de programmation python :

* `l[-1]` rend le dernier élément d'une liste.
boucle `for`.
* on a un peu fait de magie noire sur les tris en utilisant le paramètre [key](https://docs.python.org/fr/3/howto/sorting.html#key-functions) qui permet de passer une fonction en paramètre. Cette fonction est appelé pour chaque élément. C'est pratique pour ne trier que selon 1 élément d'une liste (ici le 2ème élément).

On utilise aussi l'écriture lambda qui permet de créer des fonction d'une ligne anonyme. Notre fonction lambda est équivalente à :

```python
def truc(x):
    return x[1]
```

#### preuve de l'algorithme : maximum de films

On prouve notre algorithme comme tout algorithme glouton : on suppose que l'algorithme glouton ne donne pas une solution optimale et on considère une solution optimale coïncidant le plus longtemps possible avec la solution donnée par celui-ci.

Soit $i$ l'indice de la première différence. On note $f_i$ le film choisi par le glouton et $f'_i$ le film (différent de $f_i$) choisi par la solution optimale :

* la date de fin de $f'_i$ est plus grande que la date de fin de $f_i$ par construction de la solution par l'algorithme glouton.
* la date de début de $f'_i$ est avant la date de fin de $f_i$ sinon on pourrait ajouter $f_i$ à la solution optimale et rendre une solution avec strictement  plus de films

Les deux remarques ci-dessus amènent au fait que l'on peut construire une nouvelle solution en échangeant $f'_i$ par $f_i$ dans la solution optimale. Comme cette nouvelle solution a autant de films que la solution optimale, elle est aussi optimale. Ceci est impossible par hypothèse (on prend une solution optimale coïncidant le plus longtemps possible avec la solution de l'algorithme glouton) : notre hypothèse était fausse, l'algorithme glouton est optimal.

### nombre minimum de salles pour placer tous les films en stock

On essaie ici de trouver le nombre minimum de salles à construire pour pouvoir projeter tous les films

#### algorithme : nombre de salle minimum

On va ici classer les films par date de début croissante. On commence par 0 salles de cinéma.

En analysant dans cet ordre les films, on cherche s'il existe une salle à laquelle on peut rajouter le film (la date de fin du dernier film de la salle est plus tôt que le début du nouveau film). Si oui on rajoute le film à cette salle, si non on crée une nouvelle salle.

#### preuve de l'algorithme : minimum de salles

La preuve est ici aisée car si on rajoute une salle pour loger un nouveau film $f$, ca veut dire que pour toutes les $k$ salles actuelle il y a un film qui n'est pas fini pendant le début du nouveau film. Ca signifie qu'il existe $k$ films dont le début est avant $f$ et la fin après $f$ : il faut donc au moins $k+1$ salles pour jouer tous ces films en parallèle.

## exemple : ordonnancement

Les problèmes d'ordonnancement sont multiples. Certains sont durs d'autres faciles. Mais un algorithme glouton permet de trouver souvent une solution acceptable pour beaucoup d'entres eux et même parfois optimale pour certains problèmes.

Le problème suivant est résoluble par un algorithme glouton : On considère $m$ produits de durée 1 à fabriquer. Si le produit $i$ est réalisée avant la date $d_i$ on peut le vendre pour un prix $p_i$, sinon il est invendable. Proposez un algorithme permettant de maximiser les profits en considérant que l'on a qu'un seul ouvrier.

Il faut procéder en deux temps :

* on doit tout d'abord se doter d'un algorithme permettant de savoir si on peut vendre tous les éléments d'un ensemble de produit donné
* créer un ensemble maximum de produits dont on peut vendre tous les éléments.

### ensemble compatible

Un ensemble de produits est dit *compatible* s'il existe un ordonnancement de leur production permettant de tous les vendre (chaque produit est fabriqué avant sa date de péremption).

On montre qu'un ensemble de produits est compatible si et seulement si l'ordonnancement par date $d_i$ croissante permet de tous les vendre. En effet :

* si l'ordonnancement par date croissante permet de tout vendre il est compatible
* s'il existe un autre ordonnancement avec la tâche $j$ placé avant la tâche $i$ alors que $d_j > d_i$, on peut échanger la tâche $i$ et la tâche $j$ et l'ordonnancement reste compatible

### algorithme : ensemble compatible maximum

Montrons que l'algorithme glouton suivant est optimal :

1. on trie les produits par prix décroissant
2. ensemble = {}
3. pour chaque produit x dans cet ordre : on ajoute x à ensemble s'il reste compatible
4. rendre ensemble (qui est un ensemble de profit maximal)

### preuve : ensemble compatible maximum

* initialisation : si une solution ne contient pas l'élément de prix maximum on l'échange avec le 1er élément choisi et la solution reste compatible tout en ayant un profit plus grand
* récurrence : clair. S'il reste dans les solutions possible l'élément qu'on rajoute à l'étape $i$ on peut toujours le rendre à la place de celui pris par l'autre solution pour augmenter le profit.

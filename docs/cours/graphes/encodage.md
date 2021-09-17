---
layout: page
title:  "Théorie des graphes : encodage des graphes"
category: cours
tags: informatique graphes
author: "François Brucker"
---

[graphes]({% link cours/graphes/index.md %}) / [encodage]({% link cours/graphes/encodage.md %})

## But

Montrer comment l'on peut passer d'une structure *tableau blanc* (*ie.* *tableau noir* pour les plus nostalgiques d'entres nous) à une structure informatique.
Chaque représentation de graphes va avoir son utilité, selon l'algorithme utilisé. On se restreint ici aux graphes simples, orientés ou non.

En informatique, on a coutume de regarder la complexité de chaque opération que l'on va faire sur la structure. De là, selon l'algorithme utilisé et les opérations qu'il va faire sur cette structure, on pourra utiliser telle ou telle implémentation.

Pour un graphe, les opérations que l'on va considérer sont :

* manipulation de la structure :
  * savoir si $xy$ est une arête
  * savoir si $x$ est un sommet
  * parcourir tous les voisins d'un sommet
  * parcourir tous les sommets
  * parcourir toutes les arêtes
* construction de la structure :
  * création de la structure
  * destruction de la structure
  * ajout d'un sommet
  * ajout d'une arête

## liste

Structure simple. Utilisable pour des graphes orienté ou non.

$G = (V, E)$ où :

* $V$ : est une liste de $n$ sommets
* $E$ : est une liste de $m$ couples de sommets.

La complexité de stockage : $\mathcal{O}(m+n)$

Structure de stockage la plus simple. N'est optimisé pour aucune opération spécifique :

* manipulation de la structure :
  * savoir si $xy$ est une arête : $\mathcal{O}(m)$ il faut parcourir toute la liste $E$
  * savoir si $x$ est un sommet : $\mathcal{O}(n)$ il faut parcourir toute la liste $V$
  * parcourir tous les voisins d'un sommet : $\mathcal{O}(m)$ il faut parcourir toute la liste $E$
  * parcourir tous les sommets : $\mathcal{O}(n)$
  * parcourir toutes les arêtes : $\mathcal{O}(m)$
* construction de la structure :
  * création de la structure : $\mathcal{O}(\vert V \vert + \vert E \vert)$
  * destruction de la structure : $\mathcal{O}(1)$
  * ajout d'un sommet :
    * $\mathcal{O}(1)$ si l'on ajoute en fin de liste,
    * $\mathcal{O}(n)$ si l'on utilise un tableau de taille fixe qu'il faut recréer
  * ajout d'une arête :
  * $\mathcal{O}(1)$ si l'on ajoute en fin de liste,
  * $\mathcal{O}(m)$ si l'on utilise un tableau de taille fixe qu'il faut recréer

## liste d'adjacence

$G = (V, E)$ où :

* $V$ : est une liste de $n$ sommets
* $E$ : est une liste de $n$ listes.

Nécessite un re-codage des sommets en entiers allant de 0 à $n-1$. Ceci peut être fait en associant à chaque sommet son indice dans la liste $V$ ou en considérant que les sommets sont des entiers allant de $0$ à $n-1$.

Pour utiliser cette structure, on va toujours considérer que **les sommets sont des entiers** allant de $0$ à $n-1$. La liste $V$ n'est là que pour pouvoir associer plus tard un sommet à autre chose qu'un entier (dépendant de l'application).

Avec cette convention et cet encodage : $E[i]$ est la liste de tous les voisins de $i$.

L'intérêt de cette encodage est que certaines opérations sont optimisées :

* manipulation de la structure :
  * savoir si $xy$ est une arête : $\mathcal{O}(\delta(x) + \delta(y))$ il faut parcourir les listes $E[x]$ et $E[y]$
  * savoir si $x$ est un sommet : $\mathcal{O}(1)$
  * parcourir tous les voisins d'un sommet : $\mathcal{O}(\delta(x))$ On parcourt $E[x]$
  * parcourir tous les sommets : $\mathcal{O}(n)$
  * parcourir toutes les arêtes : $\mathcal{O}(m)$ : on parcourt tous les $E[i]$ pour $0\leq i < n$
* construction de la structure :
  * création de la structure : $\mathcal{O}(\vert V \vert + \vert E \vert)$
  * destruction de la structure : $\mathcal{O}(1)$
  * ajout d'un sommet :
    * $\mathcal{O}(1)$ (un entier de plus)
  * ajout d'une arête :
  * $\mathcal{O}(1)$ si l'on ajoute en fin de liste,
  * $\mathcal{O}(m)$ si l'on utilise un tableau de taille fixe qu'il faut recréer

> En code, on utilise souvent une variante de cette structure qui utilise des [tableaux associatifs](https://fr.wikipedia.org/wiki/Tableau_associatif). Voir par exemple [l'implémentation en python](https://www.python.org/doc/essays/graphs/). On troque alors les complexités maximale par des complexités en moyennes, mais on a plus besoin de l'encodage des éléments sous la forme d'entiers.

## matrice d'adjacence

$G = (V, E)$ où :

* $V$ : est une liste de $n$ sommets
* $E$ : est une matrice $n \times n$.

Nécessite un re-codage des sommets en entiers allant de 0 à $n-1$. Ceci peut être fait en associant à chaque sommet son indice dans la liste $V$ ou en considérant que les sommets sont des entiers allant de $0$ à $n-1$.

Pour utiliser cette structure, on va toujours considérer que **les sommets sont des entiers** allant de $0$ à $n-1$. La liste $V$ n'est là que pour pouvoir associer plus tard un sommet à autre chose qu'un entier (dépendant de l'application).

Avec cette convention et cet encodage : $E[i][j]$ vaut $1$ si $xy$ est une arête, et $0$ sinon.

Cet encodage permet de traiter les graphes orientés (on traite de façon distincte $E[i][j]$ et $E[j][i]$), et même les graphes valués (la valeurs de $E[i][j]$ est la valuation de l'arête $xy$). Notez que pour un graphe non orienté la matrice $E$ est symétrique et vaut $0$ sur la diagonale.

L'intérêt de cette encodage est que le fait de savoir si un arête est présente dans le graphe est optimisé :

* manipulation de la structure :
  * savoir si $xy$ est une arête : $\mathcal{O}(1)$ : on regarde la valeur de $E[i][j]$.
  * savoir si $x$ est un sommet : $\mathcal{O}(1)$
  * parcourir tous les voisins d'un sommet : $\mathcal{O}(n)$ On parcourt toute la ligne $E[x]$
  * parcourir tous les sommets : $\mathcal{O}(n)$
  * parcourir toutes les arêtes : $\mathcal{O}(n^2)$ : on parcourt toute la matrice $E[i][j]$ pour $0\leq i, j < n$
* construction de la structure :
  * création de la structure : $\mathcal{O}(n^2)$ création de la matrice et initialisation des valeurs à 0.
  * destruction de la structure : $\mathcal{O}(1)$
  * ajout d'un sommet :
    * $\mathcal{O}(1)$ (un entier de plus)
  * ajout d'une arête :
  * ajout d'une ligne et d'une colonne. Selon comment la matrice est crée, Cela peut coûter $\mathcal{O}(n)$ (la matrice est consituée de $n$ lignes ou $n$ colonnes) ou $\mathcal{O}(n^2)$ s'il faut recréer la matrice.

## quand utiliser quoi ?




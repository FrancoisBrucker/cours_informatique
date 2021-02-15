---
layout: page
title:  "Théorie des graphes : encodage des graphes"
category: cours
tags: informatique graphes
author: "François Brucker"
---

## But

Montre comment l'on peut passer d'une structure *tableau* à une structure informatique.
Chaque représentation des graphes va avoir sn utilité, selon l'algorithme utilisé. On se restreint ici aux graphes simples, orientés ou non.

## liste

Structure simple. Utilisable pour des graphes orienté ou non.

$G = (V, E)$ où :

* $V$ : est une liste de $n$ sommets
* $E$ : est une liste de $m$ couples de sommets.

La complexité de stockage : $\mathcal{O}(m+n)$

Structure de stockage la plus simple. N'est optimisé pour aucune opération spécifique :

* parcourir tous les voisins d'un sommet : $\mathcal{O}(m)$ il faut parcourir toute la liste $E$
* parcourir tous les sommets : $\mathcal{O}(n)$
* parcourir tous les arêtes : $\mathcal{O}(m)$
* savoir si $xy$ est une arête : $\mathcal{O}(m)$ il faut parcourir toute la liste $E$

## liste d'adjacence

$G = (V, E)$ où :

* $V$ : est une liste de $n$ sommets
* $E$ : est une liste de $n$ listes.

Nécessite un recodage des sommets en entiers allant de 0 à $n-1$. Ceci peut être fait en associant à chaque sommet son indice dans la liste $V$ ou en considérant que les sommets sont des entiers allant de $0$ à $n-1$.

Avec cet encodage : $E[i]$ est la liste de tous les voisins de $i$.

L'intérêt de cette encodage est que certaines opérations sont optimisées :

* parcourir tous les voisins d'un sommet $x$ : $\mathcal{O}(\delta(x))$ On parcours $E[x]$
* parcourir tous les sommets : $\mathcal{O}(n)$
* parcourir tous les arêtes : $\mathcal{O}(m)$ : on parcours tous les $E[i]$ pour $0\leq i < n$
* savoir si $xy$ est une arête : $\mathcal{O}(\delta(x) + \delta(y))$ il faut parcourir les listes $E[x]$ et $E[y]$

> **Remarque** : En python, on utilise souvent une variante de cette structure qui [utilise des dictionnaires](https://www.python.org/doc/essays/graphs/). On troque alors les complexités maximale par des complexités en moyennes, mais on a plus besoin de l'encodage des éléments sous la forme d'entiers.

## matrice d'adjacence

$G = (V, E)$ où :

* $V$ : est une liste de $n$ sommets
* $E$ : est une matrice $n \times n$.

Nécessite un recodage des sommets en entiers allant de 0 à $n-1$. Ceci peut être fait en associant à chaque sommet son indice dans la liste $V$ ou en considérant que les sommets sont des entiers allant de $0$ à $n-1$.

Avec cet encodage : $E[i][j]$ vaut $1$ si $xy$ est une arête, et $0$ sinon. 

Cet encodage permet de traiter les graphes orientés (on traite de façon distincte $E[i][j]$ et $E[j][i]$), et même graphes valués (la valeurs de $E[i][j]$ est la valuation de l'arête $xy$). Notez que pour un graphe non orienté la matrice $E$ est symétrique et vaut $0$ sur la diagonale.

L'intérêt de cette encodage est que le fait de savoir si un arête est présente dans le graphe est optimisé :

* parcourir tous les voisins d'un sommet $x$ : $\mathcal{O}(n)$ On parcours toute la ligne $E[x]$
* parcourir tous les sommets : $\mathcal{O}(n)$
* parcourir tous les arêtes : $\mathcal{O}(n^2)$ : on parcours toute la matrice $E[i][j]$ pour $0\leq i, j < n$
* savoir si $xy$ est une arête : $\mathcal{O}(1)$ On regarde la valeur de $E[i][j]$.

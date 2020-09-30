---
layout: page
title:  "Algorithmes gloutons : comme heuristiques"
category: cours
tags: informatique cours 
authors: "François Brucker"
---



## But

Montrer que, même s'ils ne réussissent pas toujorus à trouver la solution optimale, les algorithmes gloutons sont souvent des heuristiques bien pratiques.



> Une version [pdf pour les TDs]({{ "ressources/algorithmes_gloutons/latex/algorithmes_gloutons_2_2.pdf" }}) est disponible.

> Le corrigé est [disponible]({% link cours/tronc_commun/algorithmes_gloutons_corrige_2_2.md %})


## exercice 5 : le problème du sac à dos

Le [problème du sac à dos](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos) est un exemple de problème d'optimisation. Il fait parti des problèmes les plus durs du monde car les solutions n'entretiennent pas de relations les unes avec les autres, il faut a priori toutes les regarder pour trouver la meilleure, et il y en a beaucoup. 

Il est possible de modéliser beaucoup de problèmes courants par un problème de sac à dos, en particuliers les: 

  - problèmes de découpe pour minimiser les chutes
  - problèmes de remplissage (déménagement)

### énoncé du problème

On dispose de :

  - $n$ objets ayant chacun un poids $w_i$ (*weight*) et une valeur nutritionnelle $p_i$ ($1 \leq i \leq n$)
  - d'un sac à dos d'une contenance de $W$
  
On veut maximiser la valeur nutritionnelle que l'on peut emporter avec notre sac.

### on essaie


On suppose que l'on est un randonneur et que l'on peut emporter 3 produits : 

  - produit A, 2kg, 100kcal
  - produit B, 2kg, 10kcal
  - produit C, 3kg, 120kcal
  
Selon la valeur du sac à dos quel est la quantité maximale d'énergie que le randonneur peut emporter avec lui ? 


### sac à doc fractionnel

Si l'on peut prendre qu'une partie des objets (comme pour une poudre ou un liquide), le problème peut être résolu par un algorithme glouton.

Problème :

  - entrée : 
    - liste de produits décrit par leur masse et le prix total
    - une masse totale transportable 
  - sortie : une liste de produits et leur masse qui maximise l'énergie pour une masse ne dépassant pas la masse transportable


#### résolvez le problème avec les données précédentes

On suppose que l'on peut découper les objet pour obtenir une fraction de leurs valeurs. résolvez le problème pour une capacité de sac de 4kg et de 5kg. 

#### algorithme glouton

Proposez un algorithme glouton pour résoudre ce problème et montrer qu'il est optimal.


### sac à dos non fractionnel 

#### si on ne peut pas couper ?

Donner un exemple où l'algorithme glouton ne donne pas la solution optimale si l'on ne peut pas prendre une partie fractionnelle d'un produit.


#### solution optimale

On peut trouver un algorithme optimal pour le problème du sac à dos en remarquant que l'on peut construire une solution optimale avec $i$ objets à partir de solutions optimales à $i-1$ objets. 

En effet la solution optimale à $i$ objets pour une capacité $W$ est soit :

  - une solution optimale à $i-1$ objets pour une capacité $W$ si on ne prend pas l'objet $i$,
  - une solution optimale à $i-1$ objets pour une capacité $W - w_i$ si on prend l'objet $i$.
  
#### algorithme optimal

Ecrivez l'algorithme permettant de résoudre le problème. 

Et explicitez pourquoi cet algorithme n'est pas glouton.

#### Complexité de l'algorithme

Quel est la complexité de cet algorithme.

#### Le millions de dollars

Le problème du sac à dos fait partie des problème "les plus dur de l'informatique", or on a un algorithme polynomial pour le résoudre... Soit on vient de démontrer [P = NP](https://fr.wikipedia.org/wiki/Probl%C3%A8mes_du_prix_du_mill%C3%A9naire#Probl%C3%A8me_ouvert_P_=_NP) et on a gagné 1millions de dollars, soit il y a un piège.

Quel est ce piège ?




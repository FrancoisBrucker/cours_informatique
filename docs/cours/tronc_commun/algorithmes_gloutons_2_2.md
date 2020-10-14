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


## exercice 1 : le problème du voyageur de commerce

Le [problème du voyageur de commerce](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce) peut s'énoncer comme suit : 

étant donné un ensemble de villes reliées entre elles par des routes, trouver l'itinéraire le plus court passant par chaque ville une et une seule fois. 

On suppose dans la suite de cet exercice que l'on connaît la distance $d(u, v)$ pour n'importe quel couple de villes $u$ et $v$.

### nombre de solutions

combien de solutions possibles possède un problème du voyageur de commerce à $n$ villes ?

### algorithme glouton


  1. Proposez un algorithme glouton qui résout ce problème. 
  2. Montrer que votre algorithme glouton n'est pas toujours optimal pour un ensemble de points du plan.

### optimisation 

Proposez un moyen d'optimiser la solution obtenue par l'algorithme glouton. On pourra par exemple remarquer que si l'on supprime 2 arêtes disjointes d'un cycle on peut créer un autre cycle en ajoutant seulement 2 autres arêtes disjointes.

## exercice 2 :  coloration de graphes

Le problème de la [coloration de graphes](https://fr.wikipedia.org/wiki/Coloration_de_graphe) peut s'écrire comme suit :

Soit un graphe (simple) $G = (V, E)$. Une fonction $f$ de $V$ dans $\\{1, \dots, \vert k \vert \\}$ (avec $k \leq \vert V \vert$) est une *coloration* de $G$ si $f(x) \neq f(y)$ pour toute arête $xy$ du graphe. Le nombre de couleurs différentes utilisées est $k$.

Le *nombre chromatique* d'un graphe $G$, noté $\chi(G)$ est le nombre minimum de couleur qu'il faut pour le colorier.

Cette notion modélise très bien les problèmes de ressources partagées (interférences entres antennes), d'incompatibilités ou encore de coloration de cartes de géographie (ce que nous verrons).

### exemples

Montrez que :

  - les cycles paires sont 2 coloriables
  - les cycles impairs sont 3 coloriables et pas 2 coloriables
  - un graphe $G=(V, E)$ est 2-coloriable si et seulement si il est [*bi-parti*](https://fr.wikipedia.org/wiki/Graphe_biparti) (si on eut partitionner $V$ en deux ensembles $V_1$ et $V_2$ tel que chaque arête a un sommet dans $V_1$ et un autre dans $V_2$).
  
### glouton

Connaître le nombre chromatique d'un graphe est un problème NP-difficile (un des problème les plus durs en informatique).


Proposez un algorithme glouton pour résoudre ce problème. Cet algorithme doit prendre itérativement un sommet du graphe (dans un ordre quelconque) et lui donner une couleur (qu'il ne remettra jamais en cause).

Quel est sa complexité ?

Essayez sur le graphe suivant en prenant les sommet par ordre alphabétique : ![couleurs]({{ "ressources/algorithmes_gloutons/couleur_graphe.png" }})

### glouton avec ordre choisi

Quel ordre pensez-vous prendre ? Testez le sur le graphe précédent.


### prouvons avec glouton

Montrez en utilisant l'algorithme que pour un graphe donné $\chi(G) \leq max_x(\delta(x)) +1$. Est-ce que cette borne est atteinte ?

### exemple 

On reprend l'exemple des salles de cinéma de la première partie. Ecrivez le problème du nombre minimum de salles de cinéma pour faire passer tous les films sous forme d'un problème de coloration.

Application aux films : 

  - a : (2, 6)
  - b : (3, 8)
  - c : (5, 12)
  - d : (7, 9)
  - e : (11, 15)
  - f : (12, 17)
  - g : (13, 20)
  - h : (1, 4)


## exercice 3 : cartes de géographie

Le problème est, étant donné une carte de géographie, on veut la colorier de telle sorte que chaque pays est une couleur différente de ses voisins.

### coloration de cartes

Montrez que l'on peut modéliser ce problème comme un problème de coloration.

Et testez le sur l'exemple suivant :  ![carte]({{ "ressources/algorithmes_gloutons/carte.png" }})

### planarité

Un graphe est dit *planaire* si on peut le représenter graphiquement dans le plan sans arête qui se croise.

Montrez que le graphe de coloration d'une carte est planaire.

Pour une représentation planaire donnée, les nœuds et les arêtes sont représentés par des courbes (les arêtes) et des points (les nœuds). Le dessin défini ainsi une partition du plan ou chaque composante connexe est appelée *face*. Notez que selon la représentation planaire du graphe ses faces peuvent changer (mais sont  liées par la formule d'Euler).

### formule d'Euler

Soit $G = (V, E)$ un graphe planaire (avec $n = \vert V \vert$ et $m = \vert E \vert$). On note $F$ le nombre de face (le bord extérieur étant considéré comme une face). 
  
Montrez que : $n - m + F = 2$ (cette relation est appelée *formule d'Euler*).

De là :

  1. en utilisant le fait que toute arête sépare exactement 2 faces et qu'une face a au moins 3 arêtes démontrez que $m\leq 3n - 6$
  2. de l'inégalité ci-dessus, déduisez-en qu'il existe toujours un sommet de degré au plus 5
  3. enfin, en utilisant l'algorithme de coloration prouver qu'il faut au maximum 6 couleurs pour coloriez toute carte de géographie


## exercice 4 : le problème du sac à dos

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

#### Le million de dollars

Le problème du sac à dos fait partie des problème "les plus durs de l'informatique", or on a un algorithme polynomial pour le résoudre... Soit on vient de démontrer [P = NP](https://fr.wikipedia.org/wiki/Probl%C3%A8mes_du_prix_du_mill%C3%A9naire#Probl%C3%A8me_ouvert_P_=_NP) et on a gagné 1millions de dollars, soit il y a un piège.

Quel est ce piège ?




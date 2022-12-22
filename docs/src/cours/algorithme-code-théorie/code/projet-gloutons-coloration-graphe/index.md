---
layout: layout/post.njk 
title: "Projet : Coloration de graphe glouton"

eleventyNavigation:
  key: "Projet : Coloration de graphe glouton"
  parent: Code

prerequis:
    - "../../algorithme/algorithmes-gloutons/"
    - "../format-données-json/"
---

<!-- début résumé -->

Problème de coloration de graphe et résolution avec un algorithme glouton.

<!-- end résumé -->

> TBD à faire bien.

Pays pas planaire, mais europe oui (DOM et TOM en france par exemple).

4 couleurs europe
plus pour le monde mais couleur unique par pays.

> TBD : dépendances des pays.

Le problème de la [coloration de graphes](https://fr.wikipedia.org/wiki/Coloration_de_graphe) peut s'écrire comme suit :

Soit un graphe (simple) $G = (V, E)$. Une fonction $f$ de $V$ dans $\\{1, \dots, \vert k \vert \\}$ (avec $k \leq \vert V \vert$) est une *coloration* de $G$ si $f(x) \neq f(y)$ pour toute arête $xy$ du graphe. Le nombre de couleurs différentes utilisées est $k$.

Le *nombre chromatique* d'un graphe $G$, noté $\chi(G)$ est le nombre minimum de couleur qu'il faut pour le colorier.

Cette notion modélise très bien les problèmes de ressources partagées (interférences entres antennes), d'incompatibilités ou encore de coloration de cartes de géographie (ce que nous verrons).

### exemples

Montrez que :

* les cycles paires sont 2 coloriables
* les cycles impairs sont 3 coloriables et pas 2 coloriables
* un graphe $G=(V, E)$ est 2-coloriable si et seulement si il est [*bi-parti*](https://fr.wikipedia.org/wiki/Graphe_biparti) (si on eut partitionner $V$ en deux ensembles $V_1$ et $V_2$ tel que chaque arête a un sommet dans $V_1$ et un autre dans $V_2$).
  
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


## correction

## exercice 2 :  coloration de graphes

### exemples

La 2 coloriabilité des cycles paires et la 3 coloriabilité des cycles impaires est claire.

Pour un graphe bi-parti :

  - s'il est biparti, on colorie chaque partie avec une couleur,
  - s'il est 2-coloriable, chaque couleur est une partie.

On peut montrer qu'un graphe est bi-parti si et seulement si il ne contient pas de cycle de longueur impaire, mais cela dépasse de peu le cadre de cette séance.

### glouton

On va prendre les sommets un a un et ajouter une couleur différente à celle de tous ses voisins déjà vus.

Ce qui donne : 

- les couleurs sont des nombres
- on ordonne les sommets selon $x_1, \dots, x_n$
- on donne à $x_i$ **la plus petite couleur** non encore utilisée pour ses voisins

On prend la plus petite couleur non utilisée pour minimiser le nombre de couleurs.

Pour chaque sommet, regarde tous ses voisins, la complexité totale de l'algorithme est donc en $\mathcal{O}(\sum_x\delta(x)) = \mathcal{O}(\vert E\vert)$, c'est linéaire en la taille du graphe !


Avec l'exemple on a comme couleurs :

 A | B | C | D | E | F | G
---|---|---|---|---|---|---
 1 | 2 | 1 | 2 | 3 | 1 | 4  
  
###  ordre choisi

C'est l'algorithme de [Welsh Powell](https://fr.wikipedia.org/wiki/Coloration_de_graphe#Algorithme_de_Welsh_et_Powell). On range les sommets par degré décroissant.

Avec l'exemple on a comme couleurs :

 G | E | A | D | B | C | F
---|---|---|---|---|---|---
 1 | 2 | 3 | 1 | 2 | 3 | 2  

Mettre les plus gros d'abord nous permet de mettre une petite couleur à ceux qui ont des gros degrés puisque sa couleur sera au pire : $\min(\delta(x_i), i-1) +1$ :
  
  - les gros degré auront une couleurs relevant de l'ordre dans lequel on les a pris,
  - les petites degré conserveront au pire leur degré comme couleur.

### Prouvons avec glouton

La formule ci-dessus nous donne directement le résultat. La borne est atteinte pour les graphes complets et les cycles impaires.

Notez que  si le graphe n'est pas complet et n'est pas un cycle impaire on peut prouver que $\chi(G) \leq  max_x(\delta(x))$ ([Brooks (1941)](https://en.wikipedia.org/wiki/Brooks%27_theorem)). On peut le prouver en utilisant notre algorithme glouton, mais nous ne le détaillerons pas ici.

### exemple

Chaque film est un sommet et on met une arête entre 2 films si leurs intervalles se chevauchent. 

Dans l'exemple, les arêtes sont : ha, hb, ab, bc, ac, bd, dc, ce, ef, eg, fg. Et on a une coloration en 3 couleurs. 

## exercice 3 : cartes de géographie

### coloration

Chaque pays est un sommet et une arêtes est placé entre chaque pays voisins.

Le graphe assoié à la carte est :  ![carte_couleur]({{ "ressources/algorithmes_gloutons/carte_graphe.png" }})

Et ses couleurs :

 H | A | F | B | C | D | E | G
---|---|---|---|---|---|---|---
 1 | 2 | 3 | 3 | 2 | 3 | 2 | 4 

Il y a 4 couleurs uniquement alors quele degré de  H est 7.

### planarité

Comme une carte est planaire on peut associer chaque sommet à un point de la carte et comme les pays forment des courbes fermées, on peut les traverser sans se croiser s'ils partagent un bout de frontière. 

### formule d'Euler

On prouve la formule d'Euler par récurrence sur $n$. 

  - $n = 0$. 
    - $m = 0$ on a qu'une seule face extérieure
    - $m >0$ : le graphe est une successions de "disques" : ![carte]({{ "ressources/algorithmes_gloutons/graphe_n_0_m.png" }}). Il y a donc $m$ faces intérieures plus la face extérieure : $F = m + 1 = m - 1 + 2$
  - $n >1$. Il existe une arête $xy$. On peut la contracter en 1 seul sommet (voir exemple ci-après). Cela ne change pas sa planarité ni son nombre de face. Ce nouveau graphe à une nombre de face $F' = F$, un nombre de sommets $n' = n - 1$ et un nombre d'arêtes $m' = m-1$. Comme l'hypothèse de récurrence fonctionne pour le graphe contracté, on a $F' = m'-n' +2$ donc $F = (m-1) -(n-1) + 2 = m-n+2$.
  
Exemple de contractation : ![contraction]({{ "ressources/algorithmes_gloutons/contraction_graphe.png" }})
  

Comme chaque arête départage toujours 2 faces exactement Si on somme le nombre d'arête de chaque face, on  obtient $2m$. Comme chaque face a au moins 3 arêtes, on en déduit : $2m \geq 3F$, si on remplace $F$ part $m-n+2$ on obtient : $m\leq 3n - 6$. Un graphe planaire a très peu d'arêtes.

La somme des degrés de chaque sommet vaut $2m$ et est plus grand que $n\cdot \min_x\delta(x)$. On a alors les 2 inégalités : $n\cdot \min_x\delta(x) \leq 2m \leq 2(3n-6) = 6n - 12$ et donc $\min_x(\delta(x)) < 6$.

Enfin, il est clair que si l'on supprime un sommet à un graphe planaire, il reste planaire. On peut donc choisir comme ordre $x_1, \dots x_n$ de choix de l'algorithme de coloration un ordre tel que $\delta(x_i) < 6$ pour le graphe planaire $G$ restreint à $\\{x_1,\dots, x_i\\}$ sa couleur sera toujours plus petite que son degré plus 1, c'st à dire 6. 

On peut démontrer qu'il ne faut pas plus que 4 couleurs pour colorier une carte de géogrpahie. C'est la première démonstration faite par ordinateur (il y a trop de cas particulier à regarder pour un humain). La preuve qu'il faut moins que 5 couleurs est atteignable, mais (la encore) c'est un peut trop pour cette séance.

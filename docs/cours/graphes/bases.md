---
layout: page
title:  "Théorie des graphes : bases"
category: cours
tags: informatique graphes
author: "François Brucker"
---

## But

Essentiellement du vocabulaire de théorie des graphe. Histoire de fixer un peu les idées.

##  définition générale

Dans toute sa généralité, on peut définir un *multi-graphe* comme étant un couple $G = (V, E)$ où :

  - $V$ est un ensemble de d'éléments appelés *sommets* (*vertices*)
  - $E$ est une liste de couples d'éléments de $V$ appelés *arc* ou *arêtes* (*edges*)
  
### exemples

Le multi-graphe $G = (V E)$ avec :

  - $V = {1, 2, 3, 4, 5}$,
  - $E = ((1, 2), (2, 3), (2, 2), (1, 2), (4, 5), (5, 4))$.

Peut se représenter graphiquement (sur le plan) :

![un multi graphe]({{ " ressources/un_multi_graphe.png" }})

Remarquez qu'avec notre définition on :

  - peut avoir plusieurs fois le même arc : ici $(1, 2)$,
  - peut avoir des *boucles* : $(2, 2)$
  - a des *arcs* qui sont orientés.
  
### utilité
  
Les multi-graphes sont des outils puissant de modélisation permettant de résoudre nombre de problèmes courants.
Ils sont très utilisés lorsque l'on cherche **une solution globale à partir d'un problème décrit localement** comme :

  - [google maps](https://www.google.fr/maps/dir/). On cherche un itinéraire entre deux villes en ne connaissant à priori que ce qui se passe entre deux croisement consécutifs, mais on connaît tous les croisements,
  - les contraintes d'allocations de ressources. Les sommets sont les antennes et les arêtes si il y a des interférences possibles, on cherche à trouver une [coloration du graphe](https://fr.wikipedia.org/wiki/Coloration_de_graphe),
  - problèmes de transports où l'on veut distribuer le plus de ressources possibles dans un réseau routier/fluvial/informatique.

Ils sont aussi très utiles de modélisation pour comprendre le réel en utilisant des classes particulières de multi-graphes. Ainsi :

  -  le modèle arboré des [arbres phylogénétique](https://fr.wikipedia.org/wiki/Arbre_phylog%C3%A9n%C3%A9tique) modélisent l'évolution des espèces 
  - des graphes aléatoire générrés en utilisant par exmple [le modèle de Barabasi-Albert](https://fr.wikipedia.org/wiki/Mod%C3%A8le_de_Barab%C3%A1si-Albert) permettent de créer des graphes "*petit monde*" typiques des réseaux sociaux ou de l'internet.

Enfin, ils procurent une satisfaction purement estétique de part la grande beauté des démonstrations.


## restrictions 


Notre définition est tellement générale qu'elle est très peu utilisée telle quelle. On utilisera souvent des cas particuliers selon le problème que l'on veut résoudre :

  - se restreindre à un nombre fini de sommets et d'arcs. **Ce sera toujours le cas ici**.
  - ne pas permettre à un arc d'apparaître plusieurs fois, c'est que qu'on appelle un *graphe*. On a alors que pour un graphe $G = (V, E)$, $E$ est un ensemble de couple tel que $E \subseteq V \times V$ : c'est une *relation*. 
  - on interdit les boucles (les arcs qui commencent et finissent au même nœud). Les boucles induisent en effet souvent des cas particuliers besogneux dans les démonstrations sans apporter de grandes propriétés.
  - si $(x, y) \in E$ alors $(y, x) \in E$. On appelle ces graphes *non orienté*. Les éléments de $E$ sont maintenant des ensembles à deux éléments et on les appelle *arêtes* plutôt qu'*arc* (qu'on réserve aux graphes orientés).
  
On appelle *graphe simple* un graphe sans boucle et non orienté. Classiquement, et on suivra cette règle ici, le mot *graphe* est équivalent à graphe simple et sinon on précisera :

  - *graphe orienté* si le graphe est sans boucle et que les éléments de $E$ sont des couples,
  - *graphe avec boucles* si le graphe peut posséder des boucles,
  - ...
 
Par abus de langage on écrira $xy$ pour designer une arête (*resp.* arc) plutôt que $\{x, y\}$ (*resp.* $(x, y)$).

 >**Nota Bene :** ne soyez pas étonné que selon l'application ou le problème étudié on appelle graphe, le cas particulier de mutli-graphe qui nous intéresse. Donc parfois, selon le contexte, un graphe sera orienté et dans d'autres cas il ne le sera pas s'il n'y a pas de confusion possible. En cas de doute, revenez au vocabulaire précis.

## vocabulaire

### graphes

Pour un graphe (orienté ou non) $G = (V, E)$ on appelle :

  - $V$ est  l'ensemble des *sommets* du graphe et on note $\vert V\vert = n$ qu'on appelle l'*ordre* de $G$.
  - $E$ est l'ensemble des *arcs* pour un graphe orienté et des *arêtes* pour un graphe non orienté et on note $\vert E \vert = m$ la *taille* de $G$.

### graphe orienté

Une *arc* est un élément de $E$ pour les graphes orientés. On le représente graphiquement comme ça : ![arc]({{ "ressources/arc.png" }})

  - $x$ est l'origine de l'arc,
  - $y$ est la destination de l'arc
  
L'ensemble des arcs sortants de $x$ est appelé *voisinage sortant de $x$* (*neighbors*) et vaut : $N^+(x) = \\{ y \vert xy \in E\\}$. Le *degré* sortant de $x$ vaut  $\delta^+(x) = \vert N^+(x) \vert$. 
De la même manière l'ensemble des arcs entrant en $y$ est appelé  *voisinage entrant en $y$* et vaut : $N^-(y) = \\{ x \mid xy \in E\\}$. Le degré entrant de $y$ vaut $\delta^-(y) = \vert N^-(y) \vert$. 

### graphe non orienté 

Une *arête* est un élément de $E$ pour les graphes non orienté. On la représente graphiquement comme ça : ![arête]({{ "ressources/arete.png" }})


Il n'y a pas de différence entre voisinage sortant et voisinage entrant pour un graphe non orienté. On note simplement le *voisinage de $x$* comme étant : $N(x) = \\{ y \mid  xy \in E\\}$ et son *degré* comme étant : $\delta(x) = \vert N(x) \vert$.


## exemple

### orienté 

Considérons le multi-graphe suivant :

![multi-graphe]({{ "ressources/graphe_oriente_boucle.png" }})

C'est un *graphe orienté avec boucle*.

On a :

  - $N^+(a) = \{ b, e\}$,
  - $\delta^+(b) = \delta^-(b) = 2$.
  
Que vaut $\sum_x \delta^+(x)$ ? et $\sum_x \delta^-(x)$ ?  

### non orienté

La version non orienté du graphe précédent est : 

![graphe]({{ "ressources/graphe_simple.png" }})

On a : 

  - $\delta(a) = 3$,
  - $N(a) = \\{b, d, e\\}$.

Que vaut $\sum_x \delta(x)$ ?

## Premières propriétés

Pour un graphe orienté, chaque arc est compté exactement 1 fois dans la somme $\sum_x \delta^+(x)$, donc $\sum_x \delta^+(x) = \mid E \mid$. De là, on a notre première propriété qui lie local (les voisinages) et global (le nombre total d'arc) pour un graphe orienté :

$$ \sum_x \delta^+(x) =  \sum_x \delta^-(x) = \vert E  \vert$$

Ce qui, pour un graphe non-orienté donne :

$$ \sum_x \delta(x)  = 2\vert E \vert$$

Puisque chaque arête $xy$ est comptée deux fois, une fois dans $N(x)$ et une autre dans $N(y)$.


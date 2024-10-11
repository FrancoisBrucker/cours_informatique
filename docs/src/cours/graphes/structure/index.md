---
layout: layout/post.njk
title: Structure d'un graphe

authors:
  - François Brucker

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Définition de la structure de graphe et de ses composants (sommets et arêtes). On terminera cette partie en démontrant une première propriété fondamentale les liant.

## Définition générale

Dans toute sa généralité, on peut définir un **_multi-graphe_** comme étant un triplet $G = (V, E, \phi)$ où :

- $V$ est un ensemble de **_sommets_** (**_vertices_**)
- $E$ est un ensemble d'**_arcs_** (**_edges_**)
- $\phi: E \rightarrow V \times V$ une **_fonction d'incidence_** qui associe à chaque arête un couple (possiblement égaux) de sommets.

Cette définition permet de considérer des ensemble a priori infini, mais elle le fait au prix d'une grosse lourdeur de manipulation puisqu'il faut passer par une fonction d'incidence.

En pratique, on aura toujours un nombre fini de sommets et d'arêtes, on choisit donc une définition plus restrictive, mais plus facilement manipulable en informatique :

{% note "**Définition**" %}

Un **_multi-graphe_** est un couple $G = (V, E)$ où :

- $V$ est un ensemble fini de **_sommets_** (**_vertices_**)
- $E$ est une liste finie de d'éléments de $V \times V$ appelés **_arcs_** (**_edges_**)

{% endnote %}

### Exemple

Le multi-graphe $G = (V, E)$ avec :

- $V = \\{1, 2, 3, 4, 5\\}$
- $E = ((1, 2), (2, 3), (2, 2), (1, 2), (4, 5), (5, 4))$

Peut se représenter graphiquement (sur le plan) :

![exemple multi-graphe](multi_graphe_exemple.png)

{% info %}
Remarquez qu'un multi-graphe peur avoir :

- plusieurs fois le même arc : l'arc $(1, 2)$
- des _boucles_ : l'arc $(2, 2)$
  {% endinfo %}

### Utilité

Les multi-graphes sont des outils puissants de modélisation permettant de résoudre nombre de problèmes d'optimisation.

#### Résolution de problème

Outre le problème évident de construction ou de maintien de réseaux (informatique, de transports ou encore sociaux), on peut aussi citer :

- [google maps](https://www.google.fr/maps/dir/). On cherche un itinéraire entre deux villes en ne connaissant à priori que ce qui se passe entre deux croisement consécutifs, mais on connaît tous les croisements,
- les contraintes d'allocations de ressources. Les sommets sont les antennes et les arêtes si il y a des interférences possibles, on cherche à trouver une [coloration du graphe](https://fr.wikipedia.org/wiki/Coloration_de_graphe),
- problèmes de transports où l'on veut distribuer le plus de ressources possibles dans un réseau routier/fluvial/informatique,

Les problèmes ci-dessus ont ceci de particulier qu'ils peuvent très facilement **se décrire localement** :

- le problème de la recherche d'itinéraire se décrit par une liste de croisement et, pour chaque croisement, une liste de ceux qu'il peut atteindre
- le problème d'allocation de ressources se décrit de même par une liste d'antenne et, pour chaque antenne, une liste de celles avec laquelle il y a interférence possible
- enfin, le problème de transport se décrit de la même manière que le problème d'itinéraire en ajoutant une capacité à chaque couple de croisement)

Mais la **solution cherchée est globale** :

- une suite de croisement pour le problème d'itinéraire
- une fréquence à associer à chaque antenne pour le problème d'allocation de ressources
- un flot sur chaque route pour le problème de transport

C'est une caractéristique générale :

{% note %}
Un problème pouvant se décrire localement mais dont la solution est globale peut **souvent** se modéliser puis se résoudre à l'aide de graphes.
{% endnote %}

#### Modélisation

Ils permettent également de comprendre le réel en utilisant des classes particulières de multi-graphes. Par exemple :

- le modèle arboré des [arbres phylogénétique](https://fr.wikipedia.org/wiki/Arbre_phylog%C3%A9n%C3%A9tique) modélisent l'évolution des espèces
- des graphes aléatoire générés en utilisant par exemple [le modèle de Barabasi-Albert](https://fr.wikipedia.org/wiki/Mod%C3%A8le_de_Barab%C3%A1si-Albert) permettent de créer des graphes "_petit monde_" typiques des réseaux sociaux ou de l'internet.

#### Esthétique

Enfin, ils procurent une satisfaction purement esthétique de part la grande beauté des démonstrations de leurs théorèmes et de leurs algorithmes.

## Graphe

Notre définition est tellement générale, qu'elle est très peu utilisée telle quelle. On utilisera souvent des cas particuliers selon le problème que l'on veut résoudre :

- **_sans boucles_**. Les arcs commencent et finissent toujours sur nœuds différents.
- **_sans arcs multiples_**. On a alors que pour $G = (V, E)$, $E$ est un sous-ensemble de $V \times V$ : c'est une **relation**.
- **_non orienté_**. Si $(x, y) \in E$ alors $(y, x) \in E$.

{% info %}
Ainsi, un **_multi-graphe non orienté sans boucle_** est un multigraphe tel que si $(x, y) \in E$ alors $(y, x) \in E$ et tel que $(x, x) \notin E$ pour tout $x \in V$.
{% endinfo %}

Le cas le plus simple (et donc celui que l'on utilisera en priorité) est le multi-graphe sans boucle, sans arcs multiples et non orienté. On les appelle **_graphes_** et on peut les définir comme suit :

<span id="definition-graphe"></span>
{% note "**Définition**" %}
Un **graphe** est un couple $G = (V, E)$ où :

- $V$ est un ensemble fini
- $E$ est un sous-ensemble de $\\{ \\{x, y\\} \mid x \neq y \in V \\}$. Ses éléments sont appelés **_arêtes_**.

{% endnote %}

De cette définition minimale on pourra alors définir d'autres cas, comme le **_graphe orienté_** :

<span id="definition-graphe-orienté"></span>
{% note "**Définition**" %}

Un **_graphe orienté_** est un multi-graphe sans boucle et sans arcs multiples. C'est un couple $G = (V, E)$ où :

- $V$ est un ensemble fini
- $E$ est un sous-ensemble de $\\{ (x, y) \mid x \neq y \in V \\}$

{% endnote %}

Enfin, plus rarement, vous pourrez rencontrer des **graphe mixte** qui permettent de rendre compte de situations réelles comme lorsque l'on modélise des réseaux routiers où il existe à la fois des routes à doubles sens et à sens unique et où l'on ne veut parcourir une route qu'une seule fois (pas une fois dans un sens et une fois dans l'autre pour les routes à double sens) :

<span id="definition-graphe-mixte"></span>
{% note "**Définition**" %}

Un **graphe mixte** est un triplet $G= (V, E, A)$ tel que $G_1=(V, E)$ soit un graphe non orienté et $G_2=(V, A)$ soit un graphe orienté.

{% endnote %}

Ou toutes les combinaisons de ceux-ci, comme :

- le **_graphe avec arêtes multiples_**
- le **_graphe avec boucles_**
- un **_multi-graphe mixte orienté_**
- ...

Il est important de connaître précisément de quels type de graphe on parle car les algorithmes ne fonctionnent pas toujours sur toutes les classes de graphes.

## Vocabulaire

Par abus de langage on écrira $xy$ pour designer une arête (_resp._ arc) plutôt que $\\{x, y\\}$ (_resp._ $(x, y)$).

### Taille et ordre

Pour un graphe (orienté ou non) $G = (V, E)$ on appelle :

- $\vert V\vert = n$ l'**_ordre_** de $G$.
- $\vert E \vert = m$ la **_taille_** de $G$.

A ordre fixe, les graphes de taille maximum son dit **_complet_** :

<span id="definition-graphe-complet"></span>
{% note "**Définition**" %}
Un graphe est **_complet_** s'il possède toutes les arêtes : pour tous $x, y \in V$ $xy$ est une arête. On le note $K_n$ et $m = n(n-1)/2$.
{% endnote %}

Réciproquement, un graphe sans arête est dit **_discret_** :

<span id="definition-graphe-discret"></span>
{% note "**Définition**" %}
Un graphe est **_discret_** s'il ne possède aucune arête.{% endnote %}

On peut noter qu'un graphe orienté ayant un nombre maximum d'arêtes est en fait un graphe (non orienté) complet. C'est pour cela que la définition d'un **_graphe orienté complet_** n'existe pas. On préfère parler de [tournoi](<https://fr.wikipedia.org/wiki/Tournoi_(th%C3%A9orie_des_graphes)>) :

<span id="definition-tournoi"></span>
{% note "**Définition**" %}
Un **_tournoi_** est un graphe orienté $G=(V, E)$ tel que :

- si $xy \in E$ alors $yx \notin E$
- pour tous $x \neq y \in V$, soit $xy$ soit $yx$ est un arc de $G$.
{% endnote %}

### Arcs

Un **_arc_** $xy$ est un élément de $E$ pour les graphes orientés. On le représente graphiquement comme ça :

![arc](arc.png)

Quelques notations et définitions relatives aux arcs :

{% note "**Définitions**" %}

- $x$ est l'**_origine_** de l'arc,
- $y$ est la **_destination_** de l'arc.

On appelle **_voisinage sortant de $x$_** (**_neighbors_**) l'ensemble des arcs d'origine $x$ et on le note :

$$N^+(x) = \\{ y \mid xy \in E\\}$$

Son cardinal est appelé **_degré sortant_** de $x$ et est noté :

$$\delta^+(x) = \vert N^+(x) \vert$$

De la même manière, l'ensemble des arcs de destination $y$ est appelé **_voisinage entrant en $y$_** et est noté :

$$N^-(y) = \\{ x \mid xy \in E\\}$$

Son cardinal est appelé **_degré entrant_** de $y$ et on le note :

$$\delta^-(y) = \vert N^-(y) \vert$$

{% endnote %}

### Arêtes

Une **_arête_** $xy$ est un élément de $E$ pour les graphes non orienté. On la représente graphiquement comme ça :

![arête](arete.png)

Contrairement aux arcs, il n'y a pas de distinction entre origine et destination :

{% note "**Définitions**" %}
Le **_voisinage_** d'un sommet $x$ est l'ensemble des sommets $y$ tels que $xy \in E$. ON le note :

$$N(x) = \\{ y \mid  xy \in E\\}$$

Le cardinal d'un voisinage est appelé **_degré_**. On le note :

$$\delta(x) = \vert N(x) \vert$$

{% endnote %}

En remarquant que $0 \leq \delta(x) < n$ pour un sommet $x$ d'un graphe à $n$ sommets, prouvez la propriété suivante :

{% exercice %}

Montrez que dans tout graphe (à au moins 2 sommets) il existe au moins deux sommets différents ayant même degré.

{% endexercice %}
{% details "solution" %}
C'est une application directe du [principe des tiroirs](https://fr.wikipedia.org/wiki/Principe_des_tiroirs).
Pour un graphe à $n$ sommet, le degré de tout sommet est entre 0 et $n-1$, soit $n$ possibilités. Si tous les sommets avaient des degrés différents il y en aurait 1 avec 0 voisins et un autre avec $n-1$, ce qui est impossible.

{% enddetails %}

## Voisinages et arêtes

Nous allons présenter une première relation fondamentale pour les graphes. Cette propriété va lier une notion locale : les voisinages de sommets, à une notion globale : le nombre d'arêtes du graphe.

Avant d'énoncer la propriété, commençons par le visualiser. Considérons le graphe orienté avec boucles suivant :

![un graphe orienté](graphe_oriente_boucle.png)

On a par exemple :

- $N^+(a) = \\{ b, e \\}$,
- $\delta^+(b) = \delta^-(b) = 2$.

{% exercice %}

Calculez $\sum_x \delta^+(x)$ ? et $\sum_x \delta^-(x)$
{% endexercice %}
{% details "solution" %}

$$\sum_x \delta^+(x) = \delta^+(a) + \delta^+(b) + \delta^+(c) + \delta^+(d) + \delta^+(e) = 2 + 2 + 1 + 1 + 2 = 8$$

$$\sum_x \delta^-(x) = \delta^-(a) + \delta^-(b) + \delta^-(c) + \delta^-(d) + \delta^-(e) = 2 + 2 + 1 + 2 + 1 = 8$$

On remarque que la boucle en $b$ est comptée pour $\delta^-(b)$ et pour $\delta^+(b)$.
On peut également remarquer que $\sum_x \delta^+(x) = \sum_x \delta^-(x) = \vert E \vert$.

{% enddetails %}

On voit que $\sum_x \delta^+(x) = \sum_x \delta^-(x)$et vaut le nombre d'arcs du graphe orienté avec boucle.

Cette constatation va — peu ou prou — s'étendre aux graphes. Une version non orienté du graphe orienté avec boucles précédent pourrait être :

![un graphe simple](graphe_simple.png)

On a :

- $\delta(a) = 3$,
- $N(a) = \\{b, d, e \\}$.

{% exercice %}

Calculez $\sum_x \delta(x)$

{% endexercice %}
{% details "solution" %}

$$\sum_x \delta(x) = \delta(a) + \delta(b) + \delta(c) + \delta(d) + \delta(e) = 3 + 2 + 2 + 3 + 2 = 12$$

{% enddetails %}

On peut remarquer que $\sum_x \delta(x) = 2\vert E \vert$.

On peut maintenant démontrer :

{% note "**Propriété**" %}
Pour un graphe orienté avec boucle $G=(V, E)$, on a la propriété suivante :

$$ \sum_x \delta^+(x) = \sum_x \delta^-(x) = \vert E \vert$$

Pour un graphe $G=(V, E)$, on a :

$$ \sum_x \delta(x) = 2\vert E \vert$$

{% endnote %}
{% details "**Preuve**", "open" %}

Pour un graphe orienté avec boucle, chaque arc $uv$ est unique. Il est compté exactement 1 fois dans la somme $\sum_x \delta^+(x)$ (pour $\delta^+(u)$), donc $\sum_x \delta^+(x) = \mid E \mid$.

Pour un graphe, chaque arête $uv$ est unique et est comptée 2 fois dans la somme $\sum_x \delta(x)$ (une fois pour $\delta(u)$ et une fois pour $\delta(v)$), donc $\sum_x \delta^+(x) = 2 \mid E \mid$.

{% enddetails %}

## Parties de graphes

On a parfois envie de découper un graphe pour en étudier une partie (s'il est trop gros ou que certains sommet et/ou arêtes ne nous intéresse pas) ou au contraire de rabouter plusieurs graphes entres eux pour en former un plus gros.

### Découpage

Il existe deux façons canonique de découper un graphe, supprimer soit des sommets, soit des arêtes :

<div id="definition-sous-graphe"></div>
<div id="definition-graphe-partiel"></div>
{% note "**Définitions**" %}
Soit $G = (V, E)$ un (multi-)graphe (non) orienté.

- si $V' \subsetneq V$, $\left.G\right|_{V'} = (V', V' \times V' \cap E)$ est un **sous-graphe de $G$ induit par $V'$**.
- si $E' \subsetneq E$, $\left.G\right|_{E'} = (V, E')$ est un **graphe partiel de $G$ induit par $V'$**.
- si $V' \subsetneq V$ et $E' \subsetneq E$ $\left.G\right|_{(V', E')} = (V', V' \times V' \cap E')$ est un **sous-graphe partiel de $G$ induit par $V'$ et $E'$**.
  {% endnote %}

Et si on a besoin de supprimer les deux :

{% note "**Définition**" %}
Soit $G = (V, E)$ un (multi-)graphe (non) orienté. Si $V' \subsetneq V$ et $E' \subsetneq E$ $\left.G\right|_{(V', E')} = (V', V' \times V' \cap E')$ est un **sous-graphe partiel de $G$ induit par $V'$ et $E'$**.
{% endnote %}

### Composition de graphes

Coller plusieurs graphes ensemble pour en former un plus gros peut se faire de multiples façons. Nous allons en montrer trois, classiques, mais il doit en exister bien d'autres.

Commençons par la plus simple, qui ne rajoute aucune arête entre les deux graphes que l'on compose :

{% note "**Définition**" %}
Soient $G_1 = (V_1, E_1)$ et $G_2 = (V_2, E_2)$ deux graphes. On note $G_1 + G_2$ le graphe :

$$G_1 + G_2 = (V_1 \cup V_2, E_1 \cup E_2)$$

{% endnote %}
{% exercice %}
Que vaut :
![g plus g](./g_plus_g.png)
{% endexercice %}
{% details "**Solution**" %}
![g plus g solution](./g_plus_g_solution.png)
{% enddetails %}

On peut aussi utiliser l'approche opposée, qui consiste à ajouter toutes les arêtes possibles entre les deux graphes :

{% note "**Définition**" %}
Soient $G_1 = (V_1, E_1)$ et $G_2 = (V_2, E_2)$ deux graphes. On note $G_1 \vee G_2$ la **liaison forte** entre $G_1$ et $G_2$. C'est le graphe :

$$G_1 \vee G_2 = (V_1 \cup V_2, E_1 \cup E_2 \cup \{ xy \mid x \in V_1, y \in V_2})$$

{% endnote %}
{% exercice %}
Que vaut :
![g plus g](./g_V_g.png)
{% endexercice %}
{% details "**Solution**" %}
![g plus g solution](./g_V_g_solution.png)
{% enddetails %}

Enfin, de façon plus subtile :

{% note "**Définition**" %}
Soient $G_1 = (V_1, E_1)$ et $G_2 = (V_2, E_2)$ deux graphes. On note $G_1 \square G_2$ le **produit cartésien** entre $G_1$ et $G_2$. C'est le graphe :

$$G_1 \square G_2 = (V_1 \times V_2, E)$$

Avec $((x_1, x_2), (y_1, y_2)) \in E$ si :

- $x_2 = y_2$ et $x_1y_1 \in E_1$
- $x_1 = y_1$ et $x_2y_2 \in E_2$

{% endnote %}
{% exercice %}
Que vaut :
![g carré g](./g_carré_g.png)
{% endexercice %}
{% details "**Solution**" %}
![g carré g solution](./g_carré_g_solution.png)
{% enddetails %}

On peut aussi chercher l'approche inverse qui consiste à décomposer un graphe donné. C'est très efficace sur les graphes _"en pattern"_ :

{% exercice %}
La grille 2D est le produit cartésien de deux graphes, lesquels ?
![g carré g](./grille.png)
{% endexercice %}
{% details "**Solution**" %}
![g carré g solution](./grille_solution.png)
{% enddetails %}

Ce n'est cependant pas toujours aussi simple :
{% exercice %}
Le graphe suivant est le produit cartésien de deux graphes, lesquels ?
![g carré g](./quel_carré.png)
{% endexercice %}
{% details "**Solution**" %}
![g carré g solution](./quel_carré_solution.png)
{% enddetails %}

## Graphes dérivés

A tout graphe on peut lui associer d'autres graphes, dérivés de celui-ci.

### Graphe complémentaire

{% lien %}
<https://fr.wikipedia.org/wiki/Graphe_compl%C3%A9mentaire>
{% endlien %}

complémentaire de complémentaire = graphe

> TBD tout graphe est complémentaire d'un autre. le carré est identité

### Graphe adjoint

{% lien %}
<https://fr.wikipedia.org/wiki/Line_graph>
{% endlien %}
Aussi appelé line graph

> TBD stable pour cycle, diminue pour chemin et augmente pour clique
> TBD tout graphe n'est pas adjoint d'un autre (exemple ?)
adjoint de adjoint = graphe

### Mineurs

{% lien %}
<https://fr.wikipedia.org/wiki/Mineur_(th%C3%A9orie_des_graphes)>
{% endlien %}

> TBD très très important, a donné des caractérisation et des théorèmes extrêmement important en théorie des graphes.

> TBD rend compte de l'intrication locale de chemins entre sommets.
>

## Clique et stable

<span id="definition-clique"></span>
{% note "**Définitions**" %}
Une **_clique_** $C$ d'un graphe $G=(V, E)$ est un ensemble de sommet de graphe tel que quelque soient $x \neq y \in C \subseteq V$, $xy \in E$.
{% endnote %}

Un **_stable_** est l'opposé :

<span id="definition-stable"></span>
{% note "**Définitions**" %}
Une **_stable_** $S$ d'un graphe $G=(V, E)$ est un ensemble de sommet de graphe tel que quelque soient $x \neq y \in S$, $xy \notin E$.
{% endnote %}

Des deux définition précédentes, un sommet est à la fois une clique et un stable. Ils constituent les ensembles minimaux non vide. Réciproquement, on appelle **_clique maximale_** (_resp._ **_stable maximal_**) un ensemble maximal pour l'inclusion.

Dans le graphe suivant, les ensembles rouges et verts sont des cliques, mais seule l'ensemble rouge est maximal.

![cliques](cliques.png)

On appelle **_clique maximum_** (_resp._ **_stable maximum_**) une clique maximale (_resp._ **_stable maximal_**) maximum pour l'inclusion (il n'en existe pas de plus grande).

Notez que pour l'exemple précédent, l'ensemble de sommets rouges n'est pas une clique maximum.

{% exercice %}
Montrez que pour le graphe précédent, la taille maximum de la clique est 4.
{% endexercice %}
{% details "corrigé" %}
Pour ce genre de preuves, il faut procéder en deux temps :

1. exhiber une clique de taille 4
2. montrer que tout ensemble de 5 sommet n'est pas une clique.

Le sous ensemble des sommets bleus suivant est une clique :

![cliques](cliques2.png)

Si on prend 5 éléments, cela revient à supprimer 1 élément du graphe et aucuns de ceux ci n'est une clique.
{% enddetails %}

Il est facile, itérativement à partir d'une clique possiblement réduite à un point, de trouver une clique maximale :

> TBD exercice où il faut trouver l'algo.

 trouver une clique maximum d'un graphe est un problème NP-complet. Considérons le problème suivant :

{% note "**Problème**" %}

- **nom** : clique
- **Entrée** :
  - un graphe
  - un entier $K$
- **Question** : le graphe contient-il une clique de taille supérieure ou égale à $K$ ?

{% endnote %}

Le problème est clairement dans NP puisque vérifier qu'un ensemble est une clique se résout polynomialement (il suffit de vérifier toutes les paires de sommets). Il est de plus NP-complet :

{% note "**Proposition**" %}
Le problème clique est NP-complet.
{% endnote %}
{% details "preuve", "open" %}
On va le montrer par réduction depuis [le problème 3-SAT](/cours/algorithmie/problème-SAT/#3-sat).

Soit l'ensemble de clauses suivante, formant une entrée du problème 3-SAT, sur l'ensemble de variables $\\{ x_1, \dots, x_n \\}$ :

<div>
$$
\mathcal{C} = \land_{1\leq i \leq m}( l_i^1\lor l_i^2\lor l_i^3)
$$
</div>

Avec pour tous $1\leq i \leq m$ et $1\leq j \leq 3$, $l_i^j \in \\{x_i \vert 1\leq i \leq n \\} \cup \\{\overline{x_i} \vert 1\leq i \leq n \\}$.

On associe (polynomialement) à cette instance un graphe $G=(V, E)$ tel que :

- $V = \\{ l_i^j \vert 1\leq i \leq m, 1\leq j \leq 3 \\}$
- $l_i^jl_k^l$ est une arête si :
  - $i \neq j$
  - $l_i^j \neq \overline{l_i^j}$

Et on cherche s'il existe une clique de taille supérieure ou égale à $m$.

S'il existe une solution au problème 3-SAT alors il existe un littéral $l_i^{u_i}$ qui est vrai pour toute clause $i$. L'ensemble $\mathcal{C} = \\{ l_i^{u_i} \vert 1\leq i \leq m\\}$ est une clique de taille $K$ de $G$.

Réciproquement toute clique de $G$ ne peut contenir qu'au plus un littéral de chaque clause, donc une clique de taille $K$ contient un littéral par clause que l'on peut positionner à vrai.
{% enddetails %}

En reprenant [l'exemple du problème 3-SAT](/cours/algorithmie/problème-SAT/#3-sat-exemple) on obtient le graphe associé $G=(V, E)$ :

![réduction](3-sat-clique-reduction-1.png)

Ce graphe possède de multiples cliques de taille 4, comme par exemple :

![réduction](3-sat-clique-reduction-2.png)

Ce qui fixe 1 littéral pour chaque clause :

- ${x_3}$ de la clause 1
- $\overline{x_1}$ des clauses 2 et 3
- ${x_4}$ de la clause clause 4

Qui fixe 3 variables. On aura toutes les clauses de vérifiées quelques soient les valeurs de $x_2$ et $x_5$ si :

- $x_3 = 1$,
- $x_1 = 0$,
- $x_4 = 1$

Dans la plupart des exemples réels, il y aura plus de clauses que de variables mais la clique max sera toujours compatible, la variable apparaissant toujours de façon identique pour chaque littéral de la clique : comme chez nous il y a 2 fois $\overline{x_1}$.

C'est le premier problème de graphe que l'on voit NP-complet, il va y en avoir tout un tas d'autres.

{% exercice %}
Montrez que le problème de savoir si un graphe donné possède un stable de taille supérieure ou égale à $K$ est un problème NP-complet.
{% endexercice %}
{% details "corrigé" %}

1. NP
2. réduction depuis clique en prenant le graphe complémentaire.

> TBD écrire propre

{% enddetails %}

## Morphismes de graphes

{% lien %}
[Les définitions d'une excellente chaîne d'informatique](https://www.youtube.com/watch?v=21bMUXO-QYQ)
{% endlien %}

Les notions définies dans cette partie le seront -- par commodité -- pour des graphes mais elles se généralisent directement à des graphes orienté ou à des multigraphes.

### Définitions

{% note "**Définition**" %}
Soient $G = (V, E)$ et $G' = (V', E')$ deux graphes. Une fonction $f: V\to V'$ est un **_morphisme_** entre $G$ et $G'$ si $xy \in E$ implique $f(x)f(y) \in E'$.

{% endnote %}

> TBD exemple

On le voit dans l'exemple $f$ n'est pas forcément une bijection de $V$ dans $V'$ et l'implication n'est que dans un sens : l'arête  $f(x)f(y)$ peut exister dans $G'$ alors que $xy \notin E$. Pour avoir une correspondance parfaite entre $G$ et $G'$ il faut qu'il existe un **_isomorphisme_** entre eux :

{% note "**Définition**" %}
Soient $G = (V, E)$ et $G' = (V', E')$ deux graphes. Une bijection $f: V\to V'$ est un **_isomorphisme_** entre $G$ et $G'$ si $xy \in E$ est équivalent à $f(x)f(y) \in E'$.

{% endnote %}

Deux graphes isomorphes sont structurellement équivalents. Ils ne diffèrent que par le nom des sommets.

> TBD dire que c'est une relation d'équivalence et que les classes d'équivalences donnent les formes de graphes à $n$ sommets. Donner exemple à 3 ?

En ce sens, notez que le si et seulement si entre les arêtes n'est pas suffisant pour que les graphes soient équivalents

> TBD un chemin de longueur 3 dans une arête. On a bien le ssi mais les deux graphes ne sont clairement pas identiques.

L'identité est toujours un isomorphisme d'un graphe dans lui même, et certains graphes (les graphes complets par exemple) en admettent beaucoup d'autres. On appelle ces isomorphisme d'un graphe dans lui-même des automorphismes :

{% note "**Définition**" %}
Un isomorphisme d'un graphe dans lui-même est appelé **_automorphisme_**.

{% endnote %}

> TBD exemple.

{% lien %}
<https://www.bourbaki.fr/TEXTES/1125.pdf>
{% endlien %}

### Reconnaissance

{% lien %}
<https://perso.ens-lyon.fr/eric.thierry/Graphes2009/jonas-lefevre.pdf>
{% endlien %}

Définissons le problème algorithmique associé :

{% note "**Problème de décision**" %}

- **nom** : isomorphisme de graphe
- **données** : deux graphes
- **question** : les deux graphes sont-ils isomorphes ?

{% endnote %}

Si on se donne une fonction $f$ allant de l'ensemble des sommets d'un graphe à un autre, il est facile de vérifier si c'est un isomorphisme entre les deux graphes ou non : le problème de l'isomorphisme de graphe est donc clairement dans NP.

En revanche, on ne connaît pas son status exact : on ne sait ni s'il est NPcomplet, ni s'il est polynomial. [Le meilleur algorithme connu](https://en.wikipedia.org/wiki/Graph_isomorphism_problem) est de complexité $2^{\mathcal{O}(\log^3(n))}$ ce qui est plus que polynomial mais moins qu'exponentiel. On verra que pour certaines classes de graphes, le problème est simple.

---
layout: layout/post.njk
title: "Flots"

authors: 
    - François Brucker
---

{% chemin %}
[Graphes]({{ ".." }}) / [{{title}}]({{ "." }})
{% endchemin %}
{% prerequis "**Prérequis** :" %}
* [Structure d'un graphe](../structure)
{% endprerequis %}

> TBD : fix les prés-requis.

<!-- début résumé -->


Modéliser des problèmes de robinets par la théorie des graphes.

<!-- end résumé -->

{% info %}
Les exemples de ce cours ont été pris dans l'excellent livre [méthodes d'optimisation combinatoire](https://www.eyrolles.com/Informatique/Livre/methodes-d-optimisation-combinatoire-9782225853074/) de Charon, Germa et Hudry qui a appris la théorie des graphes et l'optimisation combinatoire à de nombreux étudiants des années 2000 (voir même un peu avant).
{% endinfo %}


## Introduction

On considère un réseau de canalisations, chaque tuyau le constituant ayant une capacité (le diamètre) particulière. Dans ce réseau on considère deux nœuds d'intérêt :

* la source : le robinet
* le puits : l'endroit on l'on veut récupérer l'eau.

Lorsque l'on ouvre le robinet, on peut mesurer le débit (en $m^3/s$) au puits.

![un flot](../assets/img/flot-def-1.png)

Quel est le flot maximum (débit maximum) que l'on peut avoir si on ouvre à fond le robinet ?

![un flot maximum](../assets/img/flot-def-max.png)

> Remarquez bien qu'une fois le flot maximum atteint, il ne sert rien d'ouvrir plus le robinet.

Où est le goulot d'étranglement du réseau ?

![un flot maximum](../assets/img/flot-def-max-goulot.png)

> Notez que le goulot d'étranglement est le flot maximum.

C'est pour résoudre ces problèmes d'importance capitale sans avoir besoin de se mouiller que nous allons [utiliser la théorie des graphes](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_flot_maximum). On verra aussi quelques cas d'applications où les flots apparaissent alors qu'on ne les attendait pas.

## définitions

Un **réseau** est un graphe (simple) orienté $G=(V, E)$ avec :

* une **capacité** $c : E \rightarrow \mathbb{R}^{+\star}$ (réels strictement positifs)
* deux sommets spéciaux nommées **source** (noté $s$) et **puits** (noté $p$).

exemple de réseau :

![réseau](../assets/img/flot-ex-1.png)

{% info %}
Notez que si on veut une capacité nulle, il suffit de supprimer l'arc
{% endinfo %}

Un **flot** dans un réseau donné est une application $f : E \rightarrow \mathbb{R}^{+}$ telle que :

* $0 \leq f(u) \leq c(u)$ pour tout arc $u \in E$
* pour tout sommet $x$ différent de $s$ et $p$, il y a **conservation du flot**, c'est à dire que le flot entrant est égal au flot sortant : $\sum_{y \in N^-(x)} f(yx) = \sum_{y \in N^+(x)} f(xy)$.

On dit que pour un arc donné $u$ son **flux** est $f(u)$.

Exemple de flot (nombres en bleu) :

![réseau](../assets/img/flot-ex-2.png)

{% note %}
On peut d'ores et déjà noter qu'il existe toujours un flot dans n'importe quel réseau, le flot nul qui vaut $0$ pour tout arc.
{% endnote %}

Une **coupe** est déterminée à partir d'un ensemble $S \subseteq V$ contenant $s$ et pas $p$. En notant $\overline{S} = V \backslash S$ le complémentaire de $S$, une coupe, notée $(S, \overline{S})$  est l'ensemble des arcs ayant leurs origines dans $S$ et leurs extrémités dans $\overline{S}$.

{% info %}
Notez bien que $S$ n'est pas forcément connexe dans $G$.
{% endinfo %}

Exemples de coupes pour notre réseau :

* $(\\{s\\}, V \backslash \\{s\\})$ qui contient les arcs : $sa$ et $sb$
* $(V \backslash \\{p\\}, \\{p\\})$ qui contient les arcs $dp$ et $ep$
* $(\\{s, d\\}, \overline{\\{s, d\\}})$ qui contient les arcs : $sa$, $sb$, $dp$ et $de$

La **capacité d'une coupe** $c(S, \overline{S})$ est la somme des capacités des arcs de la coupe :

$$c(S, \overline{S}) = \sum_{xy \in (S, \overline{S})}c(xy)$$

On note également pour une coupe $(S, \overline{S})$ les valeurs suivantes :

* $f(S, \overline{S})$ comme étant la somme des flux des arcs ayant pour origine $S$ et pour extrémité $\overline{S}$ (les éléments de la coupe)
* $f(\overline{S}, S)$ comme étant la somme des flux des arcs ayant pour extrémité $S$ et pour origine $\overline{S}$

Exemples :

* $f(\\{s\\}, \overline{\\{s\\}}) = 1 + 0 = 1$
* $f(\\\{p\\}, V \backslash \\{p\\}) = 1 + 0 = 1$
* $f(\\{s, d\\}, \overline{\\{s, d\\}}) = 1 + 0 + 1 + 0 = 2$

## valeur d'un flot

On va prouver que pour toute coupe $(\overline{S}, S)$, la quantité suivante est constante :

$$f(S, \overline{S}) - f(\overline{S}, S) = \mbox{val}(f)$$ 

Pour tout sommet $x$ de $S$ différent de $s$, on a conservation du flot donc :

$$\sum_{x \in S} (\sum_{xy \in E} f(xy) - \sum_{yx \in E} f(yx)) = \sum_{sy \in E} f(sy) - \sum_{ys \in E} f(ys) = f(\{s\}, \overline{\{s\}}) - f(\overline{\{s\}}, \{s\})$$

De plus, les arcs internes à $S$ sont comptés deux fois une fois pour l'origine de façon positive et une fois pour l'extrémité de façon négative. Les seuls arcs qui ne sont comptés qu'une fois sont ceux qui rentre ou qui sortent de $S$. de là :

$$\sum_{x \in S} (\sum_{xy \in E} f(xy) - \sum_{yx \in E} f(yx)) = f(S, \overline{S}) - f(\overline{S}, S)$$

On en conclut donc que $f(S, \overline{S}) - f(\overline{S}, S)$ est une constante pour n'importe quelle coupe et vaut :

$$ \mbox{val}(f) = \sum_{sx \in E}f(sx) - \sum_{xs \in E}f(xs) = \sum_{xp \in E}f(xp) - \sum_{px \in E}f(px)$$

{% info %}
Ce qui rentre dans le réseau en ressort
{% endinfo %}

Pour notre exemple, on a donc une valeur de flot de $\mbox{val}(f) = 1$

## flot maximum

On a clairement que :

* $\mbox{val}(f) \leq c(S, \overline{S})$ pour toute coupe du réseau.
* si $\mbox{val}(f) = c(S^\star, \overline{S^\star})$ alors :
  * $S^\star$ est la coupe réalisant le minimum de $c(S, \overline{S})$ pour toute coupe $S$
  * $\mbox{val}(f)$ est maximum
  * pour tout arc $u$ partant de $S^\star$ pour finir en $\overline{S^\star}$, $f(u) = c(u)$
  * pour tout arc $u$ partant de $\overline{S^\star}$ pour finir en $S^\star$, $f(u) = 0$

La réciproque est également vraie et nous allons le prouver. On va prouver :

1. que le flot maximum existe
2. que le flot maximum est égale à la coupe minium.

### existence du flot maximum

Commençons pas montrer que le flot maximum est atteint.

Soient $G= (V, E)$ et $c$ un réseau donné. Une valuation $f$ des arcs de $G$ peut être vue comme  un vecteur de l'espace vectoriel $\mathbb{R}^m$ où $m = \vert E \vert$ que l'on munie d'une norme $\vert\vert . \vert\vert$ . Si cette valuation n'est pas un flot, alors :

* soit une des coordonnées est strictement négative : $f(u) < 0$,
* soit la conservation du flot n'est pas respectée pour au moins un sommet de $G$ : la valeur absolue de la différence vaut $d > 0$.

Il existe alors $\epsilon > 0$ tel que toute valuation $f'$ avec $\vert\vert f - f'\vert\vert \leq \epsilon$ n'est pas non plus un flot (on prend $\epsilon$ plus petit que $f(u) > 0$ et $d > 0$) : l'espace de $\mathbb{R}^m$ où $f$ n'est pas un flot est un ouvert. Donc son complémentaire, l'espace de $\mathbb{R}^m$ où $f$ est un flot, est fermé. Ce fermé est de plus borné puisque les flux ne peuvent dépasser les capacités.

Un fermé borné atteignant ses bornes, on en déduit que $\mbox{val}(f)$ va atteindre ses bornes : il existe bien un flot maximum.

### chaîne augmentante

Pour montrer que le flot maximum est égal à la coupe minimum on va introduire la notion de chaîne augmentante.

Une **chaîne** $c_0 \dots c_k$ dans un graphe orienté $G=(V, E)$ est une suite de sommets tels que pour tout $0 \leq i < k$, soit $c_ic_{i+1}$ soit $c_{i+1}c_i$ soit un arc du graphe.

On suppose que l'on ait un réseau $G=(V, E)$ avec ses capacités $c$ et un flot $f$. Soit alors $C = c_0\dots c_k$ une chaîne de $s$ à $p$ dans $G$.

Par exemple :

![une chaîne](../assets/img/flot-chaine-1.png)

Cette chaîne a 3 arcs qui vont dans le sens de $s$ à $p$ ($sa$, $ce$ et $ep$) et un arc qui va de $p$ vers $s$ ($ca$).

Si l'on peut augmenter la valeurs des arcs allant de $s$ à $p$ et diminuer la valeur des flots allant de $p$ à $s$ on augmentera le flot. Pour garder la conservation des flots, il faut augmenter et diminuer de la même valeur absolue.

Notons alors $C^+$ (respectivement $C^-$) l'ensemble des arcs de la chaîne allant de $s$ à $p$ (respectivement de $p$ à $s$) et calculons :

* $\alpha^+ = \min \\{ c(u) - f(u) \vert u \in C^+ \\}$
* $\alpha^- = \min \\{ f(u) \vert u \in C^- \\}$
* $\alpha = \min \\{\alpha^+, \alpha^-\\}$

Si $\alpha > 0$, $C$ est dit être une **chaîne augmentante** car on peut augmenter le flot des arcs de $C^+$ de $\alpha$ et diminuer les arcs de $C^-$ de $\alpha$ ce qui garde la conservation du flot et augmente $\mbox{val}(f)$ de $\alpha > 0$.

Dans l'exemple on a : $\alpha^+ = \alpha^- = 1$ : notre flot n'est pas maximum

{% note %}
On en conclut que s'il existe une chaîne augmentante de $s$ à $p$ alors $\mbox{val}(f)$ n'est pas maximum.
{% endnote %}

Réciproquement, supposons qu'il n'existe pas de chaînes augmentante de $s$ à $p$. Soit alors  $S'$ l'ensemble des sommets $x$ tels qu'il existe une chaîne augmentante de $s$ à $x$. L'ensemble $S = S' \cup \\{ s\\}$ est alors une coupe de notre réseau et :

* pour tout arc $xy$ commençant dans $S$ et finissant dans $\overline{S}$ on a $f(xy) = c(xy)$ sinon il existerait une chaîne augmentante de $s$ à $x$ et de $x$ à $y$, donc une chaîne augmentante entre $s$ et $y$
* pour tout arc $xy$ commençant dans $\overline{S}$ et finissant dans $S$ on a $f(xy) > 0$ sinon il existerait une chaîne augmentante de $s$ à $y$ et de $y$ à $x$, donc une chaîne augmentante entre $s$ et $y$

On en déduit que pour cette coupe : $c(S, \overline{S}) = f(S, \overline{S}) - f(\overline{S}, S)$, la valeur de notre flot est maximum !

On a donc qu'il existe une chaîne augmentante de $s$ à $p$ si et seulement si $\mbox{val}(f)$ n'est pas maximum.

{% attention %}
Les arcs d'une chaîne augmentante ne sont **pas forcément** tous dans le même sens ! La chaîne $sacep$ de l'exemple précécdent le prouve. Cette chaîne est augmentante mais les arcs sont $s\rightarrow a \leftarrow c \rightarrow e \rightarrow p$.
{% endattention %}

### théorème des flots

Finalement :

* il existe une chaîne augmentante de $s$ à $p$ si et seulement si $\mbox{val}(f)$ n'est pas maximum.
* comme le flot maximum est atteint sa valeur ne peut être que la valeur de la coupe minimum puisque l'ensemble des sommets admettant une chaîne augmentante forme alors une coupe.

{% info %}
La coupe minimum est le goulot d'étranglement du réseau.
{% endinfo %}

## algorithmes

Il existe de nombreux algorithme pour résoudre le problème du flot maximum. Nos allons ici juste montrer un exemple en suivant l'idée des chaînes augmentantes.

L'idée est d'itérativement :

1. trouver une chaîne augmentante
2. maximiser sa valeur en l'augmentant au maximum sa valeur de flot

Lorsque l'on ne trouve plus de chaîne augmentante, le flot est maximum. L'initialisation est toujours possible puisque le flot nul est un flot possible.

Si l'on suppose que nos capacités sont entières on pourra augmenter au minimum de 1 unité toutes nos chaînes augmentantes à chaque fois, donc l'algorithme va converger en :

* au maximum $C(S, \overline{S})$ itérations où $S$ est une coupe
* au maximum $\max \mbox{val}(f)$ itérations où $\max \mbox{val}(f)$ est la valeur de flot maximum
* au maximum $\vert V \vert \cdot c_\max$ itérations où $c_\max$ est la capacité maximale (pour montrer ça on considère la coupe $(\\{s\\}, V \backslash \\{s \\})$ : $s$ a au plus $\vert V\vert$ voisins et chacun de capacité maximale au plus $c_\max$)

### Ford et Fulkerson

L'algorithme de Ford et Fulkerson (1955) est une implémentation de ce principe. Il cherche une chaîne augmentante puis la résous. La procédure de recherche de chaîne est paradigmatique des algorithme *marquer/ examiner*

Son algorithme de recherche de chaîne est le suivant :

```text
Entrée :
    * un graphe orienté G = (V, E)
    * une capacité c qui associe un réel strictement positif à toute arc de G
    * deux sommets s et p
    * un flot f admissible
Initialisation :
    * marquer s par ({}, +∞)
    * considérer tous les sommet différent de s comme non marqué
    * considérer qu'aucun sommet n'est examiné
Algorithme :
    * tant que p est non marqué et qu'il existe un sommet marqué et non examiné:
        * soit x marqué et ⍺ la valeur absolue du second paramètre de sa marque
        * pour voisin y de x tel que xy est un arc et y non marqué:
            * si c(xy) > f(xy) alors :
                * β = min(⍺, c(xy) - f(xy))
                * marquer y par (x, +β)
        * pour voisin y de x tel que yx est un arc et y non marqué:
            * si f(yx) > 0 alors :
                * β = min(⍺, f(yx))
                * marquer y par (x, -β)
        * considérer x comme examiné
Retour :
    * les marques des sommets
```

Si le sommet p est marqué à la fin de l'algorithme, il existe une chaîne augmentante que l'on trouve par l'algorithme suivant :

```text
Entrée : 
    * s et p
    * les marques de l'algorithme de marquage
Initialisation :
    * C = [p]
Algorithme :
    * x = p
    * tant que x est différent de s:
        * soit y la première marque de x
        * x = y
        * ajouter x au début de C
Retour : 
    * C
```

Pour se convaincre que l'algorithme trouve bien une chaîne augmentante si elle existe, il suffit de remarquer qu'un sommet est marqué que si et seulement si il existe une chaîne augmentante allant de s à lui. Ceci fonctionne car s'il existe une chaîne augmentante allant de $s$ à $x$ et une chaîne augmentante allant de $x$ à $y$ alors il existe une chaîne augmentante allant de $s$ à $y$.

De là, si p n'est pas marqué, il n'existe pas de chaîne augmentante, et le flot est maximum. Sinon, on peut augmenter le flot avec l'algorithme suivant et recommencer

```text
Entrée : 
    * une chaîne augmentante C
    * les marques 
Algorithme
    * soit ⍺ la valeur absolue de la seconde marque de p
    * C=c0 ... ck la chaîne augmentante de s à p que l'on retrouve en remontant les premières marques jusqu'à s
    * pour chaque i allant de 1 à k:
        * si le premier paramètre de de la marque de ci est positif alors :
            * f(c(i-1)ci) += ⍺
        * sinon :
            * f(c(i-1)ci) -= ⍺
Retour :
    * f
```

La complexité de tout cet algorithme est proportionnelle au nombre d'arête du graphe (il suffit de stocker les éléments marqué dans une liste que l'on prend petit à petit). Il est donc optimal pour trouver et traiter une chaîne augmentante.

### exemple

On va utiliser notre graphe qui possède déjà un flot :

![réseau](../assets/img/flot-ex-2.png)

#### algorithme de marquage

Les graphes ci-dessous montre les différentes étapes de l'algorithme de marquage (en orange les résultats de l'étape courante).

![marquage](../assets/img/flot-ff-1.png)

On s'arrête une fois le puits marqué.

#### mise à jour

La chaîne augmentante trouvée est :

![une chaîne](../assets/img/flot-chaine-1.png)

On peut augmenter de +1 (le premier paramètre de la marque du puits) :

![marquage](../assets/img/flot-ff-2.png)

Ce qui donne le flot suivant :

![flot trouvé](../assets/img/flot-ff-3.png)

On relance l'algorithme de Ford et Fulkerson et on obtient (par exemple), la chaîne augmentante suivante :

![re marquage](../assets/img/flot-ff-4.png)

Et le flot :

![flot maximum](../assets/img/flot-ff-5.png)

Ce flot est maximum puisque l'on sature les arcs arrivant en p.

Montrons le en exécutant l'algorithme de Ford et Fulkerson pour trouver la coupe minimum (en magenta un ordre possible d'examinage des sommets):

![coupe min](../assets/img/flot-ff-6.png)

La coupe minimum est en orange.

### Autres algorithmes

La complexité de l'algorithme de Ford et Fulkerson n'est pas polynomiale (elle dépend des valuations), mais il existe des algorithmes polynomiaux, variations de l'algorithme de Ford et Fulkerson pour résoudre notre problème de flot. Vous pouvez voir la page [wikipedia](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_flot_maximum) pour quelques exemples, dont l'algorithme de [Dinic](https://fr.wikipedia.org/wiki/Algorithme_de_Dinic) ou d'[Edmonds Karp](https://fr.wikipedia.org/wiki/Algorithme_d%27Edmonds-Karp).

## flot maximum à coût minimum

Si les arcs ont un coût de passage $v(u)$, le coût du flot est : $\sum_{u \in E} v(u)f(u)$

On peut alors chercher à trouver un flot maximum à coût minimum. Ceci est possible pour les graphes antisymétriques (c'est à dire que si l'arête $xy$ existe, l'arête $yx$ n'existe pas) en utilisant les graphes d'écart pour trouver une chaîne augmentante.

{% info %}
La complexité est plus importante qu'avec l'algorithme de Ford et Fulkerson car il faut utiliser Dijkstra pour trouver un chemin.
{% endinfo %}

### graphe d'écart

Si le graphe du réseau est antisymétrique (c'est à dire que si l'arête $xy$ existe, l'arête $yx$ n'existe pas) alors on peut utiliser un graphe auxiliaire, appelé **graphe d'écart** pour trouver une chaîne augmentante.

Soit $G=(V, E)$ un graphe orienté anti-symétrique, une capacité $x$ et un flot $f$. on appelle graphe d'écart le graphe orienté $G_f = (V, E')$ tel que pour toute arc $xy$ de $G$ :

* si $f(xy) < c(xy)$ alors on crée un arc $xy$ dans $G_f$ avec une valuation de $v(xy)$
* si $f(xy) > 0$ alors on crée un arc $yx$ dans $G_f$ avec une valuation de $v(xy)$

Il est alors clair qu'il n'existe un chemin allant de $s$ à $p$ dans $G_f$ que si et seulement si il existe une chaîne augmentante pour le réseau initial.

### algorithme

On procède comme avant, mais la chaîne augmentante cherchée correspondra à un chemin de longueur minimum dans le graphe d'écart, en valuant ses arcs avec le coût de passage de chaque arc.

On peut utiliser l'[algorithme de Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra) par exemple pour trouver ce chemin.

### exemple avec le graphe d'écart

Reprenons notre exemple fétiche (On ne mettra pas de valuation sur le graphe) :

![réseau](../assets/img/flot-ex-2.png)

Le graphe d'écart associé est alors (avec en orange les arcs inverses) :

![graphe d'écart 1](../assets/img/flot-ecart-1.png)

Ce qui donne comme chemin possible :

![graphe d'écart 2](../assets/img/flot-ecart-2.png)

Et après mise à jour du flot :

![flot trouvé](../assets/img/flot-ff-3.png)

Le nouveau graphe d'écart (et un chemin possible) devient alors :

![graphe d'écart 2](../assets/img/flot-ecart-3.png)

D'où le flot :

![flot maximum](../assets/img/flot-ff-5.png)

Et le graphe d'écart qui ne permet plus de trouver un chemin entre $s$ et $p$ :

![graphe d'écart 3](../assets/img/flot-ecart-4.png)
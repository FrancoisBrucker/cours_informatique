---
layout: page
title:  "Théorie des graphes : flots - appication (corrigé)"
category: cours
tags: informatique graphes
author: "François Brucker"
---

> [graphes]({% link cours/graphes/index.md %}) / [flots : applications]({% link cours/graphes/flots-applications.md %})
{: .chemin}

Element de corrigé des applications des flots.

[les exercices]({% link cours/graphes/flots-applications.md %})

## application simple

### graphe d'écart

Le graphe d'écart associé à ce réseau :

![flot application]({{ "/assets/cours/graphes/flot-app-2.png" | relative_url }}){:style="margin: auto;display: block;"}

### résolution du problème de flot

Une chaine augmentante et l'augmentation de flot associée dans la foulée :

![flot application]({{ "/assets/cours/graphes/flot-app-3.png" | relative_url }}){:style="margin: auto;display: block;"}

La coupe min :

![flot application]({{ "/assets/cours/graphes/flot-app-4.png" | relative_url }}){:style="margin: auto;display: block;"}

## problème du transport de marchandise

### modélisation

On ajoute au graphe :

* un sommet $s$ et des arcs $sx$ pour $x \in S$ de coût 0 et de capacité l'excédent en $x$
* un sommet $p$ et des arcs $xp$ pour $x \in P$ de coût 0 et de capacité la demande en $x$

On considère que les capacités des autres arcs du graphe sont égales à $+\infty$.

Le problème du transport de marchandise revient à trouver le flot maximum à coût minimum.

Le graphe exemple transformé en problème de flot est :

![flot transport]({{ "/assets/cours/graphes/flot-app-6.png" | relative_url }}){:style="margin: auto;display: block;"}

Les capacités sont en gras (les arcs sans capacités sont considérés comme étant de capacité infini) et les coûts sont sur les arcs (les arcs sans coûts sont considérés comme étant de coût nul).

### résolution du problème de transport

On peut redessiner le réseau sous cette forme :

![flot transport graphe d'écart]({{ "/assets/cours/graphes/flot-app-transport-1.png" | relative_url }}){:style="margin: auto;display: block;"}

Le flot étant nul au départ, le graphe d'écart pondéré est égal à :

![flot transport graphe d'écart]({{ "/assets/cours/graphes/flot-app-transport-2.png" | relative_url }}){:style="margin: auto;display: block;"}

Un chemin de poids min entre $s$ et $p$ pourra alors être : $scap$ de poids 0 et qui permet d'augmenter le flot de 2 :

![flot transport augmentation 1]({{ "/assets/cours/graphes/flot-app-transport-3.png" | relative_url }}){:style="margin: auto;display: block;"}

On a de là le graphe d'écart :

![flot transport augmentation 1]({{ "/assets/cours/graphes/flot-app-transport-4.png" | relative_url }}){:style="margin: auto;display: block;"}

Un chemin de poids min entre $s$ et $p$ pourra alors être : $sebp$ de poids 2 et qui permet d'augmenter le flot de 1 :

![flot transport flot max]({{ "/assets/cours/graphes/flot-app-transport-5.png" | relative_url }}){:style="margin: auto;display: block;"}

Le flot est maximum, l'algorithme de Ford et Fulkerson nous donnant une coupe min valant 3 :

![flot transport coupe min]({{ "/assets/cours/graphes/flot-app-transport-6.png" | relative_url }}){:style="margin: auto;display: block;"}

## problème du transport amoureux

On peut écrire le graphe suivant, en liant les affinités par une arête. Le graphe est bi-parti car les mariages sont ici hétérosexuels :

![graphe bi-parti]({{ "/assets/cours/graphes/flot-app-mariage-1.png" | relative_url }}){:style="margin: auto;display: block;"}

Comme on ne peut marier une personne qu'une seule fois, c'est bien un problème de couplage (l'arête choisie est le mariage).

Pour le transformer en problème de flot on peut créer le réseau suivant, avec des capacités de 1 partout :

![graphe bi-parti]({{ "/assets/cours/graphes/flot-app-mariage-2.png" | relative_url }}){:style="margin: auto;display: block;"}

Cela fonctionne car pour chaque chaine augmentante, on va la saturer par un entier (donc 1) : on est assuré que le flot maximum sera entier, on ne va pas marier à moitié une personne.

En résolvant le problème on trouve :

* Iphigénie - Achille
* Cléopâtre - César
* Juliette - Rodrigue
* Fanny - Marius
* Chimène - Roméo

Il y a aussi la solution classique où vous échangez les maris de Juliette et Chimène.

> Notez que si l'on ne se restreint pas aux mariages hétérosexuels, le graphe n'est plus biparti. Le problème du couplage dans un graphe ne peut plus se résoudre comme un problème de flot, il faut utiliser [l'algorithme d'Edmonds](https://fr.wikipedia.org/wiki/Algorithme_d%27Edmonds_pour_les_couplages) pour le résoudre.
>
> Enfin, si l'on veut rajouter des amants (chaque personne doit avoir un conjoint et un amant), le problème devient NP-difficile.

## stockage dans les noeuds

Pour modéliser ce problème comme un problème de flot, on va une source d'eaux usée de capacité égale au bassin de rétention :

![flot]({{ "/assets/cours/graphes/flot-app-stock-2.png" | relative_url }}){:style="margin: auto;display: block;"}

On  peut alors résoudre le problème avec un flot classique :

![flot]({{ "/assets/cours/graphes/flot-app-stock-3.png" | relative_url }}){:style="margin: auto;display: block;"}

## k-connectivité dans un graphe

### P <= N

Comme les chemins sont disjoints, il faut au moins supprimer $P(s, p)$ arcs pour les déconnecter.

### val(f) <= P

Soit $f$ un flot maximum pour le réseau.

Comme les capacités valent toutes 1, chaque flux est soit 0 soit 1. De là tous les arcs sortant de $s$ de flux 1 vont créer des chemins disjoints vers $p$.

### N <= val(f)

Sur une coupe minimum $(S, \overline{S})$, toutes les arêtes allant de $S$ vers $\overline{S}$ sont à 1 et sont au nombre de $\mbox{val}(f)$. Or si on supprime toutes ces arcs, on déconnecte $s$ de $p$ : $N(s, p) \leq \mbox{val}(f)$.

### N = val(f) = P

On a les 3 inégalités :

* $P(s, p) \leq N(s, p)$
* $\mbox{val}(f) \leq P(s, p)$
* $N(s, p) \leq \mbox{val}(f)$

Donc : $P(s, p) = N(s, p) = \mbox{val}(f)$

### lemme de zorn

On suppose par l'absurde que le minimum de $N(x_i, x_{i+1})$ soit strictement plus grand que la forte arc connectivité de $G$ que l'on note $k$. En supprimant $k$ arcs je déconnecte $x_i$ de $x_j$. On a deux cas :

* si $i < j$ alors comme on peut toujours aller de $x_k$ à $x_{k+1}$ pour tous $i \leq k < j$, il existe un chemin entre $x_i$ et $x_j$ ce qui est impossible.
* si $j < i$ alors comme on peut toujours aller de $x_k$ à $x_{k+1}$ pour tous $j \leq k < n - 1$ il existe un chemin entre $x_i$ et $x_0$, puis un raisonnement identique nous indique qu'on peut aller de $x_0$ à $x_j$. Il existe donc un chemin entre $x_i$ et $x_j$ ce qui est impossible.

Trouver la forte arc connectivité d'un graphe orienté se fait donc en procédant à $\vert V \vert$ calcul de flot maximum.

### graphe non orienté

#### N >= P

On a clairement que $N(s, p) \geq P(s, p)$.

#### P >= P*

De plus, $P(a, b) \geq P^\star(s, p)$. Si les $P^\star(s, p)$ chemins ne partagent pas d'arcs issus du dédoublement des arêtes en arcs, on peut créer $P^\star(s, p)$ chemins disjoints entre $s$ et $p$ dans $G$.

Si 2 chemins partagent une arête $xy$ l'un l'$xy$ et l'autre l'arc $yx$, on peut procéder comme dans la figure ci-dessous pour créer 2 chemins partageant strictement moins d'arêtes.

![flot menger]({{ "/assets/cours/graphes/flot-menger-1.png" | relative_url }}){:style="margin: auto;display: block;"}

On peut alors itérativement construire $P^\star(s, p)$ chemins ne partageant pas d'arcs issus du dédoublement des arêtes en arcs.

#### N* >= N

En supprimant $N^\star(s, p)$ arcs de $G^\star$ on déconnecte $s$ de $p$. Si on supprime les arêtes de $G$ qui ont donné naissance à ces arcs, on déconnecte $s$ de $p$ dans $G$. En effet, s'il restait un chemin entre $s$ et $p$ dans $G$, il en resterait également un dans $G^\star$.

On a donc $N^\star(s, p) \geq N(s, p)$.

#### conclusion

On a les inégalités suivantes : $N^\star(s, p) \geq N(s, p) \geq P(s, p) \geq P^\star(s, p)$

Or $P^\star(s, p) = N^\star(s, p) = \mbox{val}(f)$ ce qui conclut la preuve d'égalité.

#### connectivité du graphe

Sa connectivité est de 3.

## bataille de la marne

Sans corrigé, c'est quasi impossible de trouver une solution. On a pas donné d'indices pour vous montrer que modéliser un problème réel peut être compliqué.

Le problème est :

* qu'une route a à la fois une capacité et une longueur, caractéristiques très différentes
* qu'il faut gérer le temps

On considère le temps comme étant une valeur discrète prenant 0, 1, 2, ..., K comme valeur.

Chaque ville est alors représentée par $K+1$ sommet, chacune représentant la ville à un temps donné. La ville A sera ainsi représentée par les sommets $A_0$, ...,  $A_K$, le sommet $A_i$ représentant la ville au temps $i$.

De là, une route de longueur 5 (et de capacité x) de A vers B va être représentée par :

* un arc de $A_0$ vers $B_5$ de capacité x
* un arc de $A_1$ vers $B_6$ de capacité x
* ...
* un arc de $A_{K-5}$ vers $B_K$ de capacité x

Une voiture qui reste dans la ville $A$ au temps $i$ emprunte un arc de $A_i$ vers $A_{i+1}$ dont la capacité est le nombre de places de parking de la ville A.

Le sommets spéciaux sont :

* le puits est la Marne au temps K.
* la source est un sommet fictif que l'on relie aux sommets $A_0$ correspondant aux villes où il y a des taxis (au temps 0); la capacité de ces arcs est le nombre de taxis disponibles.

> remarque : le graphe devient rapidement impossible à dessiner à la main, mais pour un ordi, aucun problème

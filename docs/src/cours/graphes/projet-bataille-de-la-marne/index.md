---
layout: layout/post.njk
title: "Projet : bataille de la Marne"

eleventyNavigation:
  key: "Projet : bataille de la Marne"
  parent: "Graphes"
---

<!-- début résumé -->

Un exercice de modélisation complexe.

<!-- end résumé -->

On va optimiser l'arrivée des [taxis à la bataille de la marne de 1914](https://fr.wikipedia.org/wiki/Taxis_de_la_Marne).

On a un ensemble $S$ de villes, et des routes reliant certaines villes entre elles (il peut exister plusieurs routes entre deux villes).

* chaque ville $i$ est caractérisée par un nombre $p_i$ de places de parking,
* chaque route $j$ est caractérisée par une longueur $l_j$ (le temps pour aller d’une extrémité à l’autre)
* chaque route $j$ a une capacité $c_j$ (nombre de véhicules qui peuvent l’emprunter par unité de temps)

Au temps $t = 0$, on a un certain nombre de véhicules stationnés dans différentes villes et il faut qu’au temps $t = K$, le plus possible de véhicules soient arrivés à une ville donnée (la Marne).

Il est possible que des véhicules arrivent avant cette date butoir, mais après la date K, c’est
trop tard.

## Modélisation

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

## Résolution

Le graphe devient rapidement impossible à dessiner à la main, mais pour un ordi, aucun problème.

{% exercice %}
Faites-le.
{% endexercice %}
---
layout: layout/post.njk
title: "Problèmes NP complets"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La classe NP regroupe l'ensemble des problèmes algorithmiques utilisables en pratique, c'est à dire vérifiable en temps polynomial par une machine de Turing.

Nous allons voir ici que ces deux problématiques sont liées et que

> TBD
> Si P ≠ NP alors il existe des pbs entre.
> Si  P ≠ NP alors NP \cap co-NP = P (je ne sais plus si c'est vrai ça)

## Machine de Turing et clauses

Nous allons modéliser une machine de Turing (possiblement non déterministe) par une conjonction de clauses.

### Machine à un instant donné

À un instant donné, une machine de Turing est déterminée par :

- les valeurs sur son ruban
- une position sur le ruban
- son état

On va pouvoir associer à chacune de ses parties une conjonction de clause dont exactement toutes les assignations vraies sont possibles.

#### Clause de case

Chaque case du ruban peut avoir 2 valeurs : `0` ou `1`. On associe donc à une case $c$ sa variable booléenne qui peut être vrai si la valeur de la case vaut `1` et est faux si la valeur de la case vaut `0`.

#### Clause de ruban

Un bout fini de ruban est un tableau de cases, on peut donc lui associer :

<div>
$$
R = \bigwedge_{0\leq i < n} c_i
$$
</div>

#### Clause de position

Le curseur est positionné sur une case, on peut donc lui associer $n$ variables p dont une seule est vraie. Par exemple si la position est sur la case $i$ on a :

<div>
$$
p_i \land (\bigwedge_{j\neq i} \overline{p_j})
$$
</div>

Ce qui donne la conjonctions de clause suivante pour la position sur le ruban :

<div>
$$
P = \bigvee_{0\leq i < n} (p_i \land (\bigwedge_{j\neq i} \overline{p_j}))
$$
</div>

#### Clause d'état

Une machine de Turing ne peut être que dans un seul état parmi $\vert Q\vert$. La conjonction de clauses associée est donc similaire à celui de la position :

<div>
$$
Q = \bigvee_{0\leq i < q} (q_i \land (\bigwedge_{j\neq i} \overline{q_j}))
$$
</div>

### Transition

Les transitions permettent de passer d'une étape à une autre, elles peuvent également être modélisées par des clauses. En reprenant la partie précédente, une machine de Turing au début de la $k$ème étape vaut :

<div>
$$
M^k = R^k \land P^k \land Q^k
$$
</div>

#### Conservation si pas de curseur

Toutes les cases où n'est pas le curseur ne changent pas entre l'étape $k$ et l'étape $k+1$. Ceci peut s'écrire, si le curseur n'est pas à la case $i$, que soit la case vaut 1 aux étapes $k$ et $k+1$ soit elle vaut 0 aux étapes $k$ et $k+1$:

<div>
$$
C^k_i = (c^{k}_{i} \land c^{k+1}_{i}) \lor (\overline{c^{k}_{i}} \land \overline{c^{k+1}_{i}})
$$
</div>

On en déduit une conjonction de clause qui traduit la conservation du ruban là où ne se trouve pas le curseur :

<div>
$$
C^k = \bigwedge_{0\leq i < n}[(\overline{p^k_i}\land C^k_i) \lor p^k_i]
$$
</div>

#### Transition si curseur

À l'endroit où le curseur se trouve, la fonction de transition s'applique et on peut aussi l'écrire comme une conjonction de clause ! Par exemple la transition $\delta(q_j, 0) = (\delta_e(q_j, 0), \delta_c(q_j, 0), \delta_d(q_j, 0))$ d'une machine de Turing simple cva s'écrire, en supposant que $\delta_c(q_j, 0) = 1$ et que $\delta_d(q, 0) \in \\{-1, +1\\}$ pour respectivement gauche et droite :

<div>
$$
T^k_{q_j, 0} = \bigvee_{0\leq i < n} [\underbracket{p^k_i \land q^k_j \land \overline{c^k_{i}}}_{\text{étape courante}} \land \underbracket{p^{k+1}_{i + \delta_{d}(0, q_j)} \land q^{k+1}_{\delta_{e}(0, q_j)}\land c^{k+1}_{i}}_{\text{prochaine étape}}]
$$
</div>

Et si $\delta_c(q_j, 0) = 0$ :

<div>
$$
T^k_{q_j, 0} = \bigvee_{0\leq i < n} [\underbracket{p^k_i \land q^k_j \land \overline{c^k_{i}}}_{\text{étape courante}} \land \underbracket{p^{k+1}_{i + \delta_{d}(0, q_j)} \land q^{k+1}_{\delta_{e}(0, q_j)}\land \overline{c^{k+1}_{i}}}_{\text{prochaine étape}}]
$$
</div>

En faisant de même avec $T^k_{q_j, 1}$, on associe une conjonction de clauses à la fonction de transition de l'étape $k$ à l'étape $k+1$ :

<div>
$$
T^k = \bigvee_{0\leq j < \vert Q\vert} (T^k_{q_j, 0} \lor T^k_{q_j, 1})
$$
</div>

Ceci fonctionne car une seule clause $p^k_i \land q^k_j \land c^k_{i, 0}$ est vraie : on ne procède qu'à une seule transition.

Si la machine est non déterministe, on ajoute autant de $T^k_{q_j, 1}$ qu'il y a de choix dans la transition.

### Conditions initiales

Les conditions initiales $M^0 = R^0 \land P^0 \land Q^0
$doivent fixer le ruban $R^0$, la position du curseur $P^0$ et l'état $Q^0$ initiaux de la machine.

- Si le ruban est initialement vide on a $R^0 = \bigwedge_{0\leq i < n}\overline{c_{i,0}}$ et sinon on le positionne à sa valeur
- Le curseur est initialement à la case $n/2$ (on verra pour quoi tout à l'heure) : $C^0 = p^0_{n/2}$
- et l'état initial est $q_0$ : $Q^0 = q^0_{0}$

### Exécution de la machine

On va supposer que l'état `START` est l'état $q_0$ et $q_1$ l'état `STOP`. La machine de Turing va s'arrêter au bout de $K$ étapes si la conjonction de clause suivante admet une solution :

<div>
$$
M = \bigwedge_{0\leq k < K} (M^k) \land \bigwedge_{0\leq k < K-1} (T^k) \land q^{K-1}_1
$$
</div>

Si la machine de Turing es simple, il n'y a qu'une possibilité puisque les transitions vont toutes être déterministes, mais si la machine est non déterministe l'assignation des états peut ou pas produire une assignation vraie.

## Théorème de Cook

On a assez de matériel maintenant pour démontrer [le théorème de Cook (1971)](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Cook) :

{% note "**Théorème**" %}
Pour problème de décision $D$ de la classe NP il existe une réduction polynomiale telle que $D \leq \text{SAT}$
{% endnote %}
{% details "preuve", "open" %}
Soit $L$ un langage de la classe $NP$. Il existe donc une machine de Turing non déterministe $M$ qui l'accepte en temps polynomial $\mathcal{O}(n^k)$. Il existe alors $p$ tel que $M$ ne prennent jamais plus de $n^p$ opérations. Pour s'assurer que $M$ puisse toujours effectuer $n^p$ opérations on remplace change toutes les transitions vers `STOP` en une transition vers un nouvel état `TEMP` qui ne change rien et peut transitionner vers `STOP` ou `TEMP` : la machine peut boucler sur l'état `TEMP` aussi longtemps que nécessaire avant de s'arrêter.

Soit $e$ un mot et Soit $C(M, e, 2\cdot \vert e \vert^p)$ l'ensemble de clauses associée à $M$ et avec $e$ comme ruban initial $2\cdot \vert e \vert^p$ rubans de longueur $2\cdot \vert e \vert^p$ (ceci pour garantir que l'exécution de la machine ne puisse pas dépasser notre ruban de taille finie en allant constamment à gauche ou constamment à droite). Notez enfin que cette conversion est polynomiale en $2\cdot \vert e \vert^p$ donc en $\vert e \vert$ (les états de $M$ ne changent pas avec l'entrée et sont donc des constantes dans la transformation).

Nous venons d'effectuer la première étape de la réduction : passer d'une instance du problème de décision $d$ à une instance de SAT en temps polynomial. Enfin, cette instance de SAT n'a de solution que si le problème initial en a une ce que montre que nous avons fait une réduction polynomial entre le problème initial et SAT.

{% enddetails %}

Le problème SAT est donc le problème le plus dur de NP (il est clair que SAT est donc NP) puisqu'il est supérieur polynomialement à tout autre : le résoudre permet de résoudre tous les autre problèmes de $NP$. Ce n'est pas le seul problème dans ce cas, puisqu'on a montré que SAT ≤ 3-SAT et il y en a plein d'autres.

{% note "**Définition**" %}
Les problèmes de décision $d$ de $NP$ tels que SAT ≤ d sont dit **_NP-complets_**.

Les problèmes $p$ qui ne sont pas dans NP et tels que SAT ≤ p sont dit **_NP-difficiles_**.
{% endnote %}

Les problèmes NP-complets signifient qu'ils sont universels : les solutions peuvent apparaître partout ; ils n'ont pas de structure qui permettent d'inférer une solution par rapport à une entrée.

On suppose très fortement qu'il n'existe pas d’algorithme polynomial pour résoudre SAT et donc que P ≠ NP mais toutes les recherches faites en ce sens n'ont pour l'instant pas été couronné de succès. Certains se demandent même si le fait de savoir si P ≠ NP ne serait pas un problème non décidable. Ceci dit, on l'a vu même si P = NP les constantes multiplicatives risquent d'être prohibitive pour avoir une solution acceptable en pratique.

## Autres problèmes NP-complets

> TBD comment faire pour montrer NP-complet. Utilisation de [gadgets](https://fr.wikipedia.org/wiki/Gadget_(informatique))

> TBD bi-partition
> TBD trouver des exemples simple avec gadget rigolo

## Problèmes co-NP complets

On peut montrer exactement de la même manière que pour le théorème de cook que la problème Tautologie, qui est le contraire de SAT est co-NP Complet.

```
nom : tautologie
Entrée : une conjonction de clauses.
Question : Toute assignation des variables est-elle satisfiable ?
```

C'est à dire que pour tout problème $p$ de décision de co-NP il existe une réduction polynomiale telle que $p$ est inférieure à Tautologie.

Si $NP \neq co-NP$ les problème NP-complets et co-NP complets sont disjoints :

{% note "**Proposition**" %}

Si $NP \neq co-NP$ alors :

- les problèmes NP-complets ne sont pas dans co-$NP$
- les problèmes co-NP-complets ne sont pas dans $NP$

{% endnote %}
{% details "preuve", "open"%}
Soit $c$ un problème NP-complet qui est également co-NP et $p$ un problème de NP. On a alors $y \leq c$ et comme $c$ est également dans co-NP on a que $y$ est dans co-NP (la machine qui répond non pour $c$ répond aussi non pour $y$)
Comme $y$ a été pris au hasard tout problème de NP est dans co-NP ce qiu est faut par hypothèse.

Le second item se démontre exactement de la même manière.
{% enddetails %}

On a finalement trois cas possible :

1. P = NP = co-NP = NP-complet = co-NP-complet. Ce cas est hautement improbable, en tous les cas la quasi totalité des informaticien n'y croient pas.
2. P $\subsetneq$ NP = co-NP$. Dans ce cas NP-complet = co-NP-complet. Ce cas est très improbable, en tous les cas la très grande majorité des informaticiens n'y croient pas non plus.
3. P $\subsetneq$ NP ≠ co-NP$ qui est le cas admis par la quasi totalité des informaticiens. On se retrouve dans le schéma ci-après.

![npc et conpc](npc-conpc)

{% lien %}
[np et co-np](https://www.youtube.com/watch?v=Hx6sfus7PIk&list=PLdUzuimxVcC0DENcdT8mfhI3iRRJLVjqH&index=46)
{% endlien %}

## Conclusion

> TBD A quoi ça sert :
>
> 1. à ne pas avoir l'air ridicule si on fait une heuristique.
> 2. à utiliser des techniques de preuves efficaces de problèmes NPC pur résoudre son problème.
> Attention à ne pas faire le contraire : résoudre un problème simple avec un problème compliqué. ON peut résoudre le problème du max d'un tableau avec SAT, mais c'est bête.

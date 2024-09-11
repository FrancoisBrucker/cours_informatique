---
layout: layout/post.njk
title: "Problèmes NP complets"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons montrer que la classe NP contient des problèmes plus généraux que tous les autres. Soit $M$ une machine de Turing non déterministe polynomiale. Il existe alors $K$ et $k$ tels que pour toute entrée $E$ de taille $n$, la machine s'arrête au bout de $Kn^k$ opérations.

De là :

- la machine n'a pas pu effectuer plus de $Kn^m$ transitions
- le curseur de la machine n'a pas pu visiter plus de $Kn^m$ cases différentes du ruban

On va montrer que l'exécution de cette machine est équivalente à trouver une affectation de littéraux d'une conjonction de clauses.

Ceci montrera que résoudre SAT permet de résoudre toute exécution d'une machine de Turing non déterministe.

> TBD <https://www.enseignement.polytechnique.fr/informatique/INF412/uploads/Main/chap12-goodINF412.pdf>
> TBD <https://perso.eleves.ens-rennes.fr/~tpier758/agreg/dvpt/info/cook.pdf>

## Variables

### du ruban

Le curseur pouvant aller à droite ou à gauche, simuler son fonctionnement peut se faire sur un ruban de taille $2\cdot Kn^m$ en positionnant initialement le curseur à la position $Kn^m$.

Chaque case du ruban peut avoir 2 valeurs : `0` ou `1`. On associe donc à une case une variable qui peut être vrai si la valeur de la case vaut `1` et est faux si la valeur de la case vaut `0`.

Comme il y aura au plus $Kn^m$ étapes, on peut simuler les valeurs du rubans par les variables $r_i^k$ avec L

- $0\leq i \leq 2\cdot Kn^m$ qui correspond à la position de la case sur le ruban
- $0\leq k \leq Kn^m$ qui correspond au nombres d'instructions

La seule chose dont on est sur concernant la valeur du ruban est leurs valeurs initiales, positionnées à l'entrée de la machine. Si l'entrée est nulle on a :

<div>
$$
R^0 = \bigwedge_{i} \overline{r_i^0}
$$
</div>

Sinon, si l'entrée est $E=e_0\dots e_p$ on aura $r_i^0 = e_i$ pour tout $i$, ce qui donne :

<div>
$$
R^0 = (\bigwedge_{i < 0\mbox{ et } i \geq p} \overline{r_i^0}) \wedge (\bigwedge_{0 \leq i < p} (r_i^0 = e_i)) = (\bigwedge_{i < 0\mbox{ et } i \geq p} \overline{r_i^0}) \wedge (\bigwedge_{0 \leq i < p} (r_i^0 \lor \overline{e_i}) \land (\overline{r_i^0} \lor e_i))
$$
</div>

La conjonction $R^k$ montrera l'état du ruban à l'instruction $k$

### de l'état

Il y $\vert Q \vert$ état différents et à chaque instruction, il n'y a qu'un seul état possible. En notant $q_i^k$ les variables associés à l'état on a :

- $0\leq i < \vert Q \vert$ qui correspond à la valeur de l'état
- $0\leq k \leq Kn^m$ qui correspond au nombres d'instructions

Comme un seul état est possible on a pour pour tout $k>0$ :

<div>
$$
Q^k = \bigvee_{i} (q^k_i \land (\bigwedge_{j\neq i} \overline{q^k_j})) = (\bigvee_{i} {q^k_i}) \land (\bigwedge_{j\neq i} (\overline{q^k_i} \vee \overline{q^k_j}))
$$
</div>

À l'état initial on a :

<div>
$$
Q^0 = q^0_0 \land (\bigwedge_{j\neq 0} \overline{q^0_j}))
$$
</div>

### du curseur

Tout comme les états, le curseur ne peut être qu'à une seule position à chaque étape d'une exécution. On le modélise donc de façon identique qux états par des variables $c_i^k$ tels que pour une instruction $k$ donnée, seule une position $i$ aura $c_i^k =1$, les autres seront fausse.

Ceci s'écrit tel que pour tout $k>0$ :

<div>
$$
C^k = (\bigvee_{i} {c^k_i}) \land (\bigwedge_{j\neq i} (\overline{c^k_i} \vee \overline{c^k_j}))
$$
</div>

À l'état initial on a :

<div>
$$
C^0 = c^0_{Kn^m} \land (\bigwedge_{j\neq Kn^m} \overline{c^0_j}))
$$
</div>

### Variables et exécution de la machine

Pour garantir ceci tout au long de l'exécution de la machine, la conjonction de causes suivante doit être vérifiée :

<div>
$$
R^0 \land Q^0 \land C^0 \wedge (\bigwedge_{k>0}Q^k \wedge C^k)
$$
</div>

Il faut maintenant contraindre l'évolution des valeurs du ruban en fonction de la fonction de transition.

> TBD faire le matrice de l'exécution en mettant en ligne le ruban.

## Ruban et transition

> TBD la transition permet de passer d'une ligne à l'autre. La modification est locale puisque on ne peut aller que d'une case à gauche ou d'une case à droite.
> TBD c'est une fenêtre de 3x2 sur la matrice d'exécution centrée au niveau du curseur.
>

Les transitions permettent de passer d'une étape à une autre, elles peuvent également être modélisées par des clauses.

### Conservation si pas de curseur

Toutes les cases où n'est pas le curseur ne changent pas entre l'étape $k$ et l'étape $k+1$. Ceci peut s'écrire :

<div>
$$
\bigwedge_{i}(\overline{c_i^k} \land (r_i^k = r_i^{k+1})) = \bigwedge_{i}(\overline{c_i^k} \land ((r_i^k \lor \overline{r_i^{k+1}}) \land (\overline{r_i^k} \lor {r_i^{k+1}})))
$$
</div>

### Transition si curseur

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

## Théorème de Cook-Levin

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

## Conclusion

> TBD A quoi ça sert :
>
> 1. à ne pas avoir l'air ridicule si on fait une heuristique.
> 2. à utiliser des techniques de preuves efficaces de problèmes NPC pur résoudre son problème.
>    Attention à ne pas faire le contraire : résoudre un problème simple avec un problème compliqué. On peut résoudre le problème du max d'un tableau avec SAT, mais c'est bête.

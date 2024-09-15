---
layout: layout/post.njk
title: "SAT est un problème NP complet"

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

{% lien %}

- <https://www.youtube.com/watch?v=0LZ39iyLMog>
- <https://www.enseignement.polytechnique.fr/informatique/INF412/uploads/Main/chap12-goodINF412.pdf>

{% endlien %}

Nous allons prendre comme exemple [la machine non déterministe exemple](../Turing-non-déterministe/#exemple){.interne} $M$ avec comme entrée $E=101$. Le nombre d'opération est linéaire et on peut montrer qu'il n'y aura jamais plus de $\vert E \vert + 1$ opérations.

## Variables

### Ruban

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

Sinon, si l'entrée est $E=e_0\dots e_{p-1}$ on aura $r_i^0 \Leftrightarrow e_i$ pour tout $i$ (les deux valeurs sont identiques), ce qui donne :

<div>
$$
R^0 = (\bigwedge_{i < 0\mbox{ et } i \geq p} \overline{r_i^0}) \wedge (\bigwedge_{0 \leq i < p} (r_i^0 \Leftrightarrow e_i)) = (\bigwedge_{i < 0\mbox{ et } i \geq p} \overline{r_i^0}) \wedge (\bigwedge_{0 \leq i < p} (r_i^0 \lor \overline{e_i}) \land (\overline{r_i^0} \lor e_i))
$$
</div>

En prenant [la machine non déterministe exemple](../Turing-non-déterministe/#exemple){.interne} et l'entrée $E = 101$, il va y avoir au plus $4$ opérations et donc on a :

<div>
$$
R_M^0 = \overline{r_0^0} \land \overline{r_1^0} \land \overline{r_2^0} \land ({r_3^0}\Leftrightarrow 1) \land ({r_4^0}\Leftrightarrow 0) \land ({r_5^0}\Leftrightarrow 1) \land \overline{r_6^0} \land \overline{r_7^0} =
\overline{r_0^0} \land \overline{r_1^0} \land \overline{r_2^0} \land {r_3^0} \land \overline{r_4^0} \land r_5^0  \land \overline{r_6^0} \land \overline{r_7^0}
$$
</div>

La conjonction de clause $R^0$ ne possède qu'une solution, qui correspond au ruban à l'instruction 0 :

```
0 : 00010100  START
```

La position de la case $i$ pour l'étape $k$ sera donnée par les variables $r_i^k$. Elles vont être déterminées grace à $R^0$ et aux transitions.

### États

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

Les états de [la machine non déterministe exemple](../Turing-non-déterministe/#exemple){.interne} sont au nombre de 3 :

- `START` qu'on nommera $q_0$
- `STOP` qu'on nommera $q_1$
- `STEP` qu'on nommera $q_2$

On a alors :

<div>
$$
Q_M^0 = q^0_0 \land \overline{q^0_1} \land \overline{q^0_2}
$$
</div>

Et :

<div>
$$
Q_M^k = (q^k_0 \lor q^k_1 \lor q^k_2) \land (\overline{q^k_0} \vee \overline{q^k_1})  \land (\overline{q^k_0} \vee \overline{q^k_2})  \land (\overline{q^k_1} \vee \overline{q^k_2})
$$
</div>

### Curseur

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

Le curseur [la machine non déterministe exemple](../Turing-non-déterministe/#exemple){.interne} peut être sur une des 8 cases du ruban :

<div>
$$
C_M^k = (\bigvee_{0\leq i < 8} {c^k_i}) \land (\bigwedge_{0\leq j\neq i <8} (\overline{c^k_i} \vee \overline{c^k_j}))
$$
</div>

Et est initialement sur la case d'indice 3 :
<div>
$$
C_M^0 = c^0_3 \land \overline{c^0_1} \land \overline{c^0_2}\land \overline{c^0_4}\land \overline{c^0_5}\land \overline{c^0_6}\land \overline{c^0_7}
$$
</div>

### Variables et exécution de la machine

Pour garantir ceci tout au long de l'exécution de la machine, la conjonction de causes suivante doit être vérifiée :

<div>
$$
M_0 = R^0 \land Q^0 \land C^0 \wedge (\bigwedge_{k>0}Q^k \wedge C^k)
$$
</div>

Cependant sans contrôle de ces variables elles peuvent s'affecter comme on veut. C'est le but de la partie suivante.

Pour l'exemple [la machine non déterministe exemple](../Turing-non-déterministe/#exemple){.interne}, comme on a déterminé qu'il ne pouvait pas y avoir plus de 8 instructions on aura :

<div>
$$
M_0 = {R_M}^0 \land {Q_M}^0 \land {C_M}^0 \wedge (\bigwedge_{0 < k <8} Q_M^k \wedge C_M^k)
$$
</div>

et correspond à l'exécution de la machine :

<div>
$$
\begin{array}{cccc}
\text{instruction}&\text{ruban}&\text{curseur}&\text{état}\\
0&0\;\; 0\;\; 0\;\; 1\;\; 0\;\; 1\;\; 0\;\; 0&3&q_0\\
1&r_0^1\, r_1^1\, r_2^1\, r_3^1\, r_4^1\, r_5^1\, r_6^1\, r_7^1&?&?\\
2&r_0^2\, r_1^2\, r_2^2\, r_3^2\, r_4^2\, r_5^2\, r_6^2\, r_7^2&?&?\\
3&r_0^3\, r_1^3\, r_2^3\, r_3^3\, r_4^3\, r_5^3\, r_6^3\, r_7^3&?&?\\
4&r_0^4\, r_1^4\, r_2^4\, r_3^4\, r_4^4\, r_5^4\, r_6^4\, r_7^4&?&?\\
5&r_0^5\, r_1^5\, r_2^5\, r_3^5\, r_4^5\, r_5^5\, r_6^5\, r_7^5&?&?\\
6&r_0^6\, r_1^6\, r_2^6\, r_3^6\, r_4^6\, r_5^6\, r_6^6\, r_7^6&?&?\\
7&r_0^7\, r_1^7\, r_2^7\, r_3^7\, r_4^7\, r_5^7\, r_6^7\, r_7^7&?&q_1
\end{array}
$$
</div>

Les positions intermédiaires des curseurs et les valeurs des états et des cases du ruban sont inconnues. On connaît en revanche :

- la position initiale du curseur : indice 3
- l'état initial est `START` ($q_0$)
- le ruban initial est : $r_1^0\, r_2^0\, r_3^0\, r_4^0\, r_5^0\, r_6^0\, r_7^0 = 0\, 0\, 0\, 1\, 0\, 1\, 0\, 0$
- l'état final est `STOP` ($q_0$)

## Ruban et transitions

Il faut maintenant contraindre l'évolution des valeurs du ruban en fonction de la fonction de transition.

Comme l'exécution de la machine de Turing est locale, contrôler ces transitions est simple à faire : si le curseur est en position $i$ à l'étape $k$ ($c^k_i = 1$ et $c^k_j = 0$ pour $j\neq i$) et se trouve à l'état $q_l^k$ ($q^k_l = 1$ et $q^k_m = 0$ pour $m\neq l$) il suffit de  :

1. connaître la transition $\delta(q_l^k, r_i^k)$
2. modifier uniquement 2 cases du ruban :
   - $r_i^k$,
   - soit $r_{i-1}^{k+1}$ soit $r_{i+1}^{k+1}$ selon la direction de la transition

Cela revient à suivre une matrice de 3x2 centrée en la position du ruban tout au long de l'exécution : tout ceci va pouvoir se faire par des clauses et de manière polynomiale.

### Conservation si pas de curseur

Toutes les cases où n'est pas le curseur ne changent pas entre l'étape $k$ et l'étape $k+1$. Ceci peut s'écrire :

<div>
$$
I^k = \bigwedge_{i}(\overline{c_i^k} \land (r_i^k \Leftrightarrow r_i^{k+1})) = \bigwedge_{i}(\overline{c_i^k} \land ((r_i^k \lor \overline{r_i^{k+1}}) \land (\overline{r_i^k} \lor {r_i^{k+1}})))
$$
</div>

Pour l'exemple [la machine non déterministe exemple](../Turing-non-déterministe/#exemple){.interne}, le ruban possède 8 cases :

<div>
$$
{I_M}^k = \bigwedge_{0\leq i < 8}(\overline{c_i^k} \land ((r_i^k \lor \overline{r_i^{k+1}}) \land (\overline{r_i^k} \lor {r_i^{k+1}})))
$$
</div>

### Transition si curseur

À l'endroit où le curseur se trouve, la fonction de transition s'applique et on peut aussi l'écrire comme une conjonction de clause ! Par exemple la transition $\delta(q_j, 0) = (\delta_e(q_j, 0), \delta_c(q_j, 0), \delta_d(q_j, 0))$ d'une machine de Turing simple va s'écrire, en supposant que $\delta_c(q_j, 0) = 1$ et que $\delta_d(q, 0) \in \\{-1, +1\\}$ pour respectivement gauche et droite :

<div>
$$
T^k_{q_j, 0} = \bigvee_{0\leq i < 2Kn^m} (\underbracket{c^k_i \land q^k_j \land \overline{r^k_{i}}}_{\text{étape courante}} \land \underbracket{c^{k+1}_{i + \delta_{d}(q_j, 0)} \land q^{k+1}_{\delta_{e}(q_j, 0)}\land r^{k+1}_{i}}_{\text{prochaine étape}})
$$
</div>

Et si $\delta_c(q_j, 0) = 0$ :

<div>
$$
T^k_{q_j, 0} = \bigvee_{0\leq i < 2Kn^m} (\underbracket{c^k_i \land q^k_j \land \overline{r^k_{i}}}_{\text{étape courante}} \land \underbracket{c^{k+1}_{i + \delta_{d}(q_j, 0)} \land q^{k+1}_{\delta_{e}(q_j, 0)}\land \overline{r^{k+1}_{i}}}_{\text{prochaine étape}})
$$
</div>

En faisant de même avec $T^k_{q_j, 1}$, on associe une conjonction de clauses à la fonction de transition de l'étape $k$ à l'étape $k+1$ :

<div>
$$
T^k = \bigvee_{0\leq j < \vert Q\vert} (T^k_{q_j, 0} \lor T^k_{q_j, 1})
$$
</div>

Ceci fonctionne car une seule clause $p^k_i \land q^k_j \land c^k_{i, 0}$ est vraie : on ne procède qu'à une seule transition.

Si la machine est non déterministe, on ajoute autant de $T^k_{q_j, 1}$ et $T^k_{q_j, 0}$ qu'il y a de choix dans la transition.

[La machine non déterministe exemple](../Turing-non-déterministe/#exemple){.interne} a uniquement 5 transitions :

état  | case | nouvel état | écriture | déplacement
------|------|-------------|----------|------------
START |   0  |  STOP       |     0    |  gauche
START |   1  |  START      |     0    |  droite
START |   1  |  STEP       |     0    |  droite
STEP  |   0  |  STOP       |     0    |  droite
STEP  |   1  |  STOP       |     0    |  gauche

En notant l'état `START` $q_0$, l'état `STOP` $q_1$ et l'état `STEP` $q_2$ et avec les 8 cases sur le ruban, on a :

<div>
$$
\begin{array}{lcl}
{T_M^k}_{q_0, 0} &=& \bigvee_{0 < i < 8} ({c^k}_{i} \land {q^k}_{0} \land \overline{r^k_{i}} \land c^{k+1}_{i - 1} \land q^{k+1}_{q_1} \land \overline{r^{k+1}_{i}})\\
{T_M^k}_{q_0, 1} &=& \bigvee_{0 \leq i < 7} ({c^k}_{i} \land {q^k}_{0} \land {r^k_{i}} \land c^{k+1}_{i + 1} \land q^{k+1}_{q_0} \land \overline{r^{k+1}_{i}})\\
{T_M'^k}_{q_0, 1} &=& \bigvee_{0 < i < 7} ({c^k}_{i} \land {q^k}_{0} \land {r^k_{i}} \land c^{k+1}_{i + 1} \land q^{k+1}_{q_2} \land \overline{r^{k+1}_{i}})\\
{T_M^k}_{q_2, 0} &=& \bigvee_{0 \leq i < 7} ({c^k}_{i} \land {q^k}_{2} \land \overline{r^k_{i}} \land c^{k+1}_{i + 1} \land q^{k+1}_{q_1} \land \overline{r^{k+1}_{i}})\\
{T_M^k}_{q_2, 1} &=& \bigvee_{0 < i < 8} ({c^k}_{i} \land {q^k}_{2} \land {r^k_{i}} \land c^{k+1}_{i - 1} \land q^{k+1}_{q_1} \land \overline{r^{k+1}_{i}})\\
\end{array}
$$
</div>

L'ensemble des transition pour l'étape $0 \leq k <8$ est alors :

<div>
$$
\begin{array}{lcl}
{T_M^k} &=& {T_M^k}_{q_0, 0} \lor {T_M^k}_{q_0, 1} \lor {T_M'^k}_{q_0, 1} \lor {T_M^k}_{q_2, 0} \lor {T_M^k}_{q_2, 1}\\
\end{array}
$$
</div>

### Exécution de la machine

On va supposer que l'état `START` est l'état $q_0$ et $q_{1}$ l'état `STOP`. La machine de Turing va s'arrêter au bout de $Kn^m$ étapes :

<div>
$$
M = \underbracket{M_0}_{\text{init}} \land \underbracket{(\bigwedge_{0\leq k < Kn^m} (I^k \land T^k))}_{\text{exécution}} \land \underbracket{q^{Kn^m}_{1}}_{\text{STOP à la fin}}
$$
</div>

Si on cherche à savoir si notre entrée est reconnue par la machine, il faut de plus ajouter que le curseur est sur un 1 à la fin :

<div>
$$
M = \underbracket{M_0}_{\text{init}} \land \underbracket{(\bigwedge_{0\leq k < Kn^m} (I^k \land T^k))}_{\text{exécution}} \land \underbracket{(q^{Kn^m}_{1} \land (\bigvee_{i} (r^{Kn^m}_i \land c^{Kn^m}_i)))}_{\text{STOP sur 1}}
$$
</div>

Si la machine de Turing est simple, il n'y a qu'une possibilité puisque les transitions vont toutes être déterministes, mais si la machine est non déterministe l'assignation des états peut ou pas produire une assignation vraie. En revanche on a :

{% note %}
Le système de clauses est satisfiable si et seulement si l'entrée est reconnue par la machine !

{% endnote %}

Ce qui donne pour [la machine non déterministe exemple](../Turing-non-déterministe/#exemple){.interne} a uniquement 5 transitions :

<div>
$$
M = {M_0} \land {(\bigwedge_{0\leq k < 7} (I_M^k \land T_M^k))} \land {(q^{7}_{1} \land (\bigvee_{i} (r^{7}_i \land c^{7}_i)))}
$$
</div>

## Théorème de Cook-Levin

On a assez de matériel maintenant pour démontrer [le théorème de Cook (1971)](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Cook) :

{% note "**Théorème**" %}
Pour problème de décision $D$ de la classe NP il existe une réduction polynomiale telle que $D \leq \text{SAT}$
{% endnote %}
{% details "preuve", "open" %}

Soit $M$ une machine de Turing non déterministe polynomiale qui résout $D$ en $\mathcal{O}(n^k)$ opérations. Il existe alors $p$ tel que $M$ ne prennent jamais plus de $n^p$ opérations. Pour s'assurer que $M$ puisse toujours effectuer $n^p$ opérations on remplace change toutes les transitions vers `STOP` en une transition vers un nouvel état `TEMP` qui ne change rien et peut transitionner vers `STOP` ou `TEMP` : la machine peut boucler sur l'état `TEMP` aussi longtemps que nécessaire avant de s'arrêter.

On peut lui associer **en temps polynomial** la conjonction de clauses définie précédemment pour associer à cette machine un problème SAT qui n'a de solution que si et seulement si notre machine en à une.

{% enddetails %}

Le problème SAT est donc le problème le plus dur de NP (il est clair que SAT est donc NP) puisqu'il est supérieur polynomialement à tout autre : le résoudre permet de résoudre tous les autre problèmes de $NP$. Ce n'est pas le seul problème dans ce cas, puisqu'on a montré que SAT ≤ 3-SAT et il y en a plein d'autres.

{% note "**Définition**" %}
Les problèmes de décision $d$ de $NP$ tels que SAT ≤ d sont dit **_NP-complets_**.

Les problèmes $p$ qui ne sont pas dans NP et tels que SAT ≤ p sont dit **_NP-difficiles_**.
{% endnote %}

Les problèmes NP-complets signifient qu'ils sont universels : les solutions peuvent apparaître partout ; ils n'ont pas de structure qui permettent d'inférer une solution par rapport à une entrée.

On suppose très fortement qu'il n'existe pas d’algorithme polynomial pour résoudre SAT et donc que P ≠ NP mais toutes les recherches faites en ce sens n'ont pour l'instant pas été couronné de succès. Certains se demandent même si le fait de savoir si P ≠ NP ne serait pas un problème non décidable. Ceci dit, on l'a vu même si P = NP les constantes multiplicatives risquent d'être prohibitive pour avoir une solution acceptable en pratique.

Pour [la machine non déterministe exemple](../Turing-non-déterministe/#exemple){.interne} il faut ajouter un état non déterministe juste avant l'état `STOP` pour garantir qu'il existe toujours une exécution prenant 8 instructions et pouvant se terminer sur un `1`. Comme l'état `STOP` est atteint depuis `STEP` ou `START`, on ajouter une boucle non déterministe de taille 2 :

état  | case | nouvel état | écriture | déplacement
------|------|-------------|----------|------------
START |   0  |  STOP       |     0    |  gauche
START |   0  |  STOP'      |     0    |  droite
START |   1  |  START      |     0    |  droite
START |   1  |  STEP       |     0    |  droite
STEP  |   0  |  STOP       |     0    |  droite
STEP  |   0  |  STOP'      |     0    |  droite
STEP  |   1  |  STOP       |     0    |  gauche
STEP  |   1  |  STOP'      |     0    |  droite
STOP' |   0  |  STOP       |     0    |  gauche
STOP' |   1  |  STOP       |     1    |  gauche

Ce nouvel état temporaire permet de cycler autant de fois que nécessaire avant de s'arrêter.

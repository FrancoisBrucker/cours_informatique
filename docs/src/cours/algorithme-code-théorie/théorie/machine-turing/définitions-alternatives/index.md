---
layout: layout/post.njk 
title:  "Définitions alternatives"

eleventyNavigation:
    order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le modèle simple de la machine de Turing peut sembler simpliste et on est tenté de le généraliser pour pouvoir calculer plus de choses. Cependant toutes les tentatives de généralisation tentées (en restant dans le domaine fini puisque l'on cherche à exprimer ce qu'est un algorithme) se sont révélées vaines car aucune d'entres elles n'arrive à calculer plus de choses.

Elle sont cependant utiles car si elles ne permettent pas de calculer plus de choses, elle permettent de les calculer plus simplement.

Nous allons examiner 4 définitions alternatives d'une machine de Turing et donner la définition d'une machine de Turing `01#` qui est la plus utilisée en algorithmie car elle permet de faire facilement des ponts entre pseudo-code et machine de Turing.

## <span id="plusieurs-curseurs"></span>Machine à plusieurs curseurs

Une machine de Turing à $k$ curseurs peut être définie comme suit.

{% note "**définition**" %}
Une ***machine de Turing à $k$ curseurs*** est composée :

* de un ***ruban*** (supposé infini) constitué de cases contiguës pouvant chacune contenir soit le caractère `0` soit le caractère `1`
* de $k$ ***curseurs***, positionnés sur une case de son ruban (on suppose que le ruban est infini à gauche et à droite du curseur)
* d'un ensemble fini $Q$ d'***états possibles***, contenant les états `START`  et `STOP`
* d'un ***état courant*** $q \in Q$
* d'une ***fonction de transition*** $\delta(q, r_1, \dots, r_k) = (\delta_e(q, r_1, \dots, r_k), \delta_{c_1}(q, r_1, \dots, r_k), \dots, \delta_{c_k}(q, r_1, \dots, r_k), \delta_{d_1}(q, r_1, \dots, r_k), \dots, \delta_{d_k}(q, r_1, \dots, r_k))$ dépendant de l'état $q$ de la machine et des caractères $r_i$ contenus dans chaque case des rubans pointée par son curseur associé. Cette fonction définie sur $Q \times \\{0, 1\\}^k$ permet de modifier :
  * l'état de la machine : $\delta_e : Q \times \\{0, 1\\}^k \mapsto Q$
  * les caractères des cases pointées par chaque curseur $1\leq i \leq k$ : $\delta_{c_i} : Q \times \\{0, 1\\}^k \mapsto \\{0, 1\\}$
  * les positions des $1\leq i \leq k$ curseurs : $\delta_{d_i} : Q \times \\{0, 1\\}^k \mapsto \\{\leftarrow, \rightarrow\\}$
{% endnote %}

Cette machine permet de prendre en compte plusieurs cases du ruban pour les transition. La gestion des curseurs est faite ainsi :

* A l'initialisation, les $k$ curseurs sont considérés être sur la même case
* A l'exécution,  on effectue l'écriture dans l'ordre des curseurs pour rendre déterministe le comportement d'une étape où deux curseurs sont sur la même case.

On va montrer que cette extension n'en est pas vraiment une car on peut toujours transformer une machine à plusieurs curseurs en une machine de Turing normale équivalente.

Nous allons pour cela montrer que l'on peut simuler une machine à 2 curseurs par une machine à un curseur.

### Simulation d'une machine à 2 curseurs par une machine simple

Le principe de cette conversion est d'associer à chaque case du ruban de la machine à deux curseurs, une 4-case composé de 4 cases de la machine à 1 curseur.

Chaque paquet est décomposé ainsi :

* case d'indice 0 : une borne. Un marqueur valant 1 pour une case strictement plus à gauche du curseur 1 et 2 (sera utile pour la suite)
* case d'indice 1 : un marqueur valant 1 si le curseur 1 est est dans la case, 0 sinon
* case d'indice 2 : un marqueur valant 1 si le curseur 2 est est dans la case, 0 sinon
* case d'indice 3 : valeur de la case associée

Par exemple si l'on a la machine à 2 curseurs suivante :

```
numéro case :  12345
ruban       :  00101
curseurs    :   ^ ^
                1 2 
```

Machine à 1 curseur simulant la machine :

```
case machine à 2 curseurs : 1   2   3   4   5
ruban                     : 10000100000100100001
indice paquet de 4 cases  : 01230123012301230123

```

On initialise la machine comme suit :

```
ruban                     : 10000110000000000000
curseur                   : ^
indice paquet de 4 cases  : 01230123012301230123
```

On suppose que l'on est dans le cas où la machine à 1 ruban simulant la machine à deux rubans est telle que :

* son état est $q$
* une seule case contient le marqueur du curseur 1 à 1
* une seule case contient le marqueur du curseur 2 à 1
* une seule case contient le marqueur de la borne à 1 et est strictement à gauche des marqueurs des curseurs 1 et 2
* le curseur est placé sur la case contenant le marqueur de borne

Les différentes étapes ci-après permettent de simuler l'avancement de la machine à 2 rubans. On utilise le formalisme des [compositions de machine vue la partie précédente](../définition/#composition-machine){.interne} pour une écriture un peu plus lisible.

1. Lecture des deux valeurs du curseurs et retour à la case ayant la borne
{% details "programme" %}

* ÉTAPE1(q): $q \in Q$ (*trouve la case avec le curseur 1*)
  1. se déplace de 1 case à droite
  2. SI 0 ALORS ÉTAPE1-D1(q) SINON ÉTAPE1-C1(q)
* ÉTAPE1-D1(q): $q \in Q$
  1. se déplace de 4 cases à droite
  2. SI 0 ALORS ÉTAPE1-D1(q) SINON ÉTAPE1-C1(q)
* ÉTAPE1-C1(q): $q \in Q$ (*lit la valeur et la "stocke" dans un état*)
  1. se déplace de 2 cases vers la droite
  2. SI 0 ALORS ÉTAPE1-C1'(q, 0) SINON ÉTAPE1-C1'(q, 1)
* ÉTAPE1-C1'(q, x): $q,x \in Q \times \\{0, 1\\}$ (*trouve la case avec la borne*)
  1. se déplace de 3 cases à gauche
  2. SI 0 ALORS ÉTAPE1-G2(q, x) SINON ÉTAPE1-C2(q, x)
* ÉTAPE1-G2(q, x): $q,x \in Q \times \\{0, 1\\}$
  1. se déplace de 4 cases à gauche
  2. SI 0 ALORS ÉTAPE1-G2(q, x) SINON ÉTAPE1-C2(q, x)
* ÉTAPE1-C2(q, x): $q,x \in Q \times \\{0, 1\\}$ (*trouve la case avec le curseur 2*)
  1. se déplace de 2 cases à droite
  2. SI 0 ALORS ÉTAPE1-D2(q, x) SINON ÉTAPE1-C2'(q, x)
* ÉTAPE1-D2(q, x): $q,x \in Q \times \\{0, 1\\}$
  1. se déplace de 4 cases à droite
  2. SI 0 ALORS ÉTAPE1-D2(q, x) SINON ÉTAPE1-C2'(q, x)
* ÉTAPE1-C2'(q, x): $q,x \in Q \times \\{0, 1\\}$ (*lit la valeur et la "stocke" dans un état*)
  1. se déplace de 1 case vers la droite
  2. SI 0 ALORS ÉTAPE1-R(q, x, 0) SINON ÉTAPE1-R(q, x, 1)
* ÉTAPE1-R(q, x, y): $q,x, y \in Q \times \\{0, 1\\} \times \\{0, 1\\}$ (*trouve la case avec la borne*)
  1. se déplace de 3 cases à gauche
  2. SI 0 ALORS ÉTAPE1-R'(q, x, 0) SINON ÉTAPE2(q, x, y)
* ÉTAPE1-R'(q, x, y): $q,x, y \in Q \times \\{0, 1\\} \times \\{0, 1\\}$
  1. se déplace de 4 cases à gauche
  2. SI 0 ALORS ÉTAPE1-R'(q, x, y) SINON ÉTAPE2(q, x, y)

{% enddetails %}
2. Écriture des valeurs aux positions des curseurs 1 et 2 et retour à la case ayant la borne
{% details "programme" %}

On se trouve sur la case avec la borne. Il faut faire les même manipulations que pour l'étape 1.

* ÉTAPE2(q, x, y): (*trouve la case avec le curseur 1*)
  1. se déplace de 1 case à droite
  2. SI 0 ALORS ÉTAPE2-D1(q, x, y) SINON ÉTAPE2-C1(q, x, y)
* ÉTAPE2-D1(q, x, y):
  1. se déplace de 4 cases à droite
  2. SI 0 ALORS ÉTAPE2-D1(q, x, y) SINON ÉTAPE2-C1(q, x, y)
* ÉTAPE2-C1(q, x, y): (*écrit la nouvelle valeur*)
  1. se déplace de 2 cases vers la droite
  2. écrit $\delta_{c_1}(q, x, y)$ sur la case
  3. se déplace de 3 cases à gauche
  4. SI 0 ALORS ÉTAPE2-G2(q, x, y) SINON ÉTAPE2-C2(q, x, y)
* ÉTAPE2-G2(q, x, y): (*trouve la case avec la borne*)
  1. se déplace de 4 cases à gauche
  2. SI 0 ALORS ÉTAPE2-G2(q, x) SINON ÉTAPE2-C2(q, x)
* ÉTAPE2-C2(q, x, y):  (*trouve la case avec le curseur 2*)
  1. se déplace de 2 cases à droite
  2. SI 0 ALORS ÉTAPE2-D2(q, x, y) SINON ÉTAPE2-C2'(q, x, y)
* ÉTAPE2-D2(q, x, y):
  1. se déplace de 4 cases à droite
  2. SI 0 ALORS ÉTAPE2-D2(q, x) SINON ÉTAPE2-C2'(q, x)
* ÉTAPE2-C2'(q, x): (*écrit la valeur*)
  1. se déplace de 1 case vers la droite
  2. écrit $\delta_{c_2}(q, x, y)$ sur la case
  3. se déplace de 3 cases à gauche
  4. SI 0 ALORS ÉTAPE2-R(q, x, 0) SINON ÉTAPE3(q, x, 1)
* ÉTAPE2-R(q, x, y): (*trouve la case avec la borne*)
  1. se déplace de 4 cases à gauche
  2. SI 0 ALORS ÉTAPE2-R(q, x, 0) SINON ÉTAPE3(q, x, y)

{% enddetails %}
3. déplacement des curseurs 1 et 2 et retour à la case ayant la borne
{% details "programme" %}

* ÉTAPE3(q, x, y): (*trouve la case avec le curseur 1*)
  1. se déplace de 1 case à droite
  2. SI 0 ALORS ÉTAPE3-D1(q, x, y) SINON ÉTAPE3-C1(q, x, y)
* ÉTAPE3-D1(q, x, y):
  1. se déplace de 4 cases à droite
  2. SI 0 ALORS ÉTAPE3-D1(q, x, y) SINON ÉTAPE3-C1(q, x, y)
* ÉTAPE3-C1(q, x, y): (*déplace le curseur 1*)
  1. écrit 0 sur la case
  2. se déplace de 4 cases selon la direction de $\delta_{d_1}(q, x, y)$
  3. écrit 1 sur la case
  4. se déplace d'une case vers la gauche
  5. SI 0 ALORS ÉTAPE3-G2(q, x) SINON ÉTAPE3-C2(q, x)
* ÉTAPE3-G2(q, x, y): (*trouve la case avec la borne*)
  1. se déplace de 4 cases à gauche
  2. SI 0 ALORS ÉTAPE2-G2(q, x) SINON ÉTAPE2-C2(q, x)
* ÉTAPE3-C2(q, x, y):  (*trouve la case avec le curseur 2*)
  1. se déplace de 2 cases à droite
  2. SI 0 ALORS ÉTAPE3-D2(q, x, y) SINON ÉTAPE3-C2'(q, x, y)
* ÉTAPE3-D2(q, x, y):
  1. se déplace de 4 cases à droite
  2. SI 0 ALORS ÉTAPE3-D2(q, x) SINON ÉTAPE3-C2'(q, x)
* ÉTAPE3-C2'(q, x): (*déplace le curseur 2*)
  1. écrit 0 sur la case
  2. se déplace de 4 cases selon la direction de $\delta_{d_2}(q, x, y)$
  3. écrit 1 sur la case
  4. se déplace de 2 case vers la gauche
  5. SI 0 ALORS ÉTAPE3-R(q, x) SINON ÉTAPE4(q, x)
* ÉTAPE3-R(q, x, y): (*trouve la case avec la borne*)
  1. se déplace de 4 cases à gauche
  2. SI 0 ALORS ÉTAPE3-R(q, x, 0) SINON ÉTAPE4(q, x, y)

{% enddetails %}
4. décale la borne d'une case vers la gauche (ceci assure que la case marquée est toujours avant les cases avec le curseurs 1 et 2) et s'y placer.
{% details "programme" %}

* ÉTAPE4(q, x, y): (*trouve la case avec le curseur 1*)
  1. écrit 0 sur la case
  2. se déplace de 4 cases à gauche
  3. écrit 1 sur la case
  4. ALLER ÉTAPE5(q, x, y)

{% enddetails %}
5. changer l'état en suivant la transition de la machine à 2 curseurs
{% details "programme" %}
On ajoute une transition allant de (ÉTAPE5(q, x, y), STOP) à (ÉTAPE1(q'), START) avec $q' = \delta_{e}(q, x, y)$
{% enddetails %}

Après ces 5 méta-étapes, la machine est de nouveau dans un état stable et peut recommencer son cycle.

Cela fait tout un tas de transitions, mais on arrive bien à simuler 2 curseurs par un seul !

### <span id="curseur-equivalence"></span>Equivalence avec la machine de Turing classique

La partie précédente a montré que l'on peut simuler une machine à deux curseurs avec une machine classique. On peut alors procéder de même avec une machine à $k>1$ curseur et la simuler par une machine à $k-1$ curseurs en combinant deux curseurs en un seul en utilisant la technique précédente.

En réitérant le processus, on obtient bien à ce qui est demandé :

{% note "**proposition**" %}
Toute machine de Turing à $k$ curseurs peut être simulée par une machine de Turing simple.

Les deux notions sont donc équivalentes.
{% endnote %}

## <span id="plusieurs-rubans"></span>Machine à plusieurs rubans

Une machine de Turing à $k$ rubans peut être définie comme suit.

{% note "**définition**" %}
Une ***machine de Turing à $k$ rubans*** est composée :

* de $k$ ***rubans*** (supposés infinis) constitués de cases contiguës pouvant chacune contenir soit le caractère `0` soit le caractère `1`
* de $k$ ***curseurs***, un par ruban, positionnés sur une case de son ruban (on suppose que le ruban est infini à gauche et à droite du curseur)
* d'un ensemble fini $Q$ d'***états possibles***, contenant les états `START`  et `STOP`
* d'un ***état courant*** $q \in Q$
* d'une ***fonction de transition*** $\delta(q, r_1, \dots, r_k) = (\delta_e(q, r_1, \dots, r_k), \delta_{c_1}(q, r_1, \dots, r_k), \dots, \delta_{c_k}(q, r_1, \dots, r_k), \delta_{d_1}(q, r_1, \dots, r_k), \dots, \delta_{d_k}(q, r_1, \dots, r_k))$ dépendant de l'état $q$ de la machine et des caractères $r_i$ contenus dans chaque case des rubans pointée par son curseur associé. Cette fonction définie sur $Q \times \\{0, 1\\}^k$ permet de modifier :
  * l'état de la machine : $\delta_e : Q \times \\{0, 1\\}^k \mapsto Q$
  * les caractères des cases de chaque ruban $1\leq i \leq k$ pointées par les curseurs : $\delta_{c_i} : Q \times \\{0, 1\\}^k \mapsto \\{0, 1\\}$
  * les positions des $1\leq i \leq k$ curseurs : $\delta_{d_i} : Q \times \\{0, 1\\}^k \mapsto \\{\leftarrow, \rightarrow\\}$
{% endnote %}

L'***exécution*** est alors identique à la machine simple. Tout se passe comme si on avait $k$ machines différentes, mais un seul état et une fonction de transition dépendant de tous les rubans.

De même, l'entrée et la sortie se généralise aisément en considérant l'ensemble des $k$ rubans.

Cette généralisation semble permettre plein de choses nouvelles ! Mais il n'en est rien : on peut toujours transformer une machine à plusieurs rubans en une machine de Turing normale équivalente.

Pour prouver ceci, nous allons montrer que l'on peut simuler une machine à 2 rubans par une machine à 1 ruban. Ceci va prendre plusieurs étapes.

### Simulation d'une machine à 2 rubans par une machine classique

Représentons une machine à 2 rubans par le schéma suivant :

```
curseur 1 :              v
ruban 1   : ...000111001001001...
ruban 2   : ...000111001001001...
curseur 2 :       ^
```

A priori les deux rubans sont décorrélées, mais comme à l'initialisation les deux rubans sont remplis de 0, les deux rubans peuvent être considérés comme superposés :

```
curseur 1 :           v
ruban 1   : ...000000000000000...
ruban 2   : ...000000000000000...
curseur 2 :           ^
```

1. déplace de deux
2. superpose les 2 rubans en affectant les cases paire au ruban 1 et les cases impaires au ruban 2

Une machine à deux rubans est donc équivalente à une machine à un ruban et 2 curseurs. Chaque curseur :

```
curseur 1     :           v
ruban         : ...000000000000000...
curseur 2     :            ^
ruban initial :    212121212121212
```

On modifie également la fonction de transition pour qu'elle se déplace de 2 cases à chaque déplacement de curseur.

### <span id="rubans-equivalence-entrée"></span> Simulation d'une entrée d'une machine à 2 rubans sur une machine classique

> TBD
> 00 = séparateur
> 10 = 0
> 11 = 1
>
> faire exemple
>
> Dire que l'on coder et décoder. Prendre le premier 11 et gauche droite

### <span id="rubans-equivalence"></span>Equivalence avec la machine de Turing classique

La partie précédente a montré que l'on peut simuler une machine à deux curseurs avec une machine classique. On peut alors procéder de même avec une machine à $k>1$ curseur et la simuler par une machine à $k-1$ curseurs en combinant deux curseurs en un seul en utilisant la technique précédente.

En réitérant le processus, on obtient bien à ce qui est demandé :

{% note "**proposition**" %}
Toute machine de Turing à $k$ rubans peut être simulée par une machine de Turing simple.

Les deux notions sont donc équivalentes.
{% endnote %}

## Machines à plusieurs curseurs et rubans

On peut bien sur combiner les deux approches et construire une machine de Turing à $k$ rubans et $k'$ curseurs répartis sur les rubans. Mais, comme vous devez vous en douter :

{% note "**proposition**" %}
Toute machine de Turing à $k$ rubans et $k'$ curseurs peut être simulée par une machine de Turing simple.

Les deux notions sont donc équivalentes.
{% endnote %}
{% details "preuve" %}
En utilisant les technique de preuve précédentes on arrive facilement à montrer que :

* toute machine de Turing à $k$ rubans et $k'$ curseurs peut être simulée par une machine de Turing $k$ rubans et $k'-1$ curseurs.
* toute machine de Turing à $k$ rubans et $k'$ curseurs peut être simulée par une machine de Turing $k-1$ rubans et $k'$ curseurs.

Une double récurrence immédiate nous permet de conclure.
{% enddetails %}

## Alphabets

Ne travailler qu'avec des `0` et des `1` peut sembler réducteur :

{% note "**définition**" %}
Une ***machine de Turing sur un alphabet $\mathcal{A}$*** est composée :

* d'un ensemble fini $\mathcal{A}$ nommé ***alphabet***
* un ***caractère blanc***, élément de $\mathcal{A}$
* d'un ***ruban*** (supposé infini) constitué de cases contiguës pouvant chacune contenir des caractères de $\mathcal{A}$
* d'un ***curseur*** qui est positionné sur une case du ruban (on suppose que le ruban est infini à gauche et à droite du curseur)
* d'un ensemble fini $Q$ d'***états possibles***, contenant les états `START`{.language-}  et `STOP`{.language-}
* d'un ***état courant*** $q \in Q$
* d'une ***fonction de transition*** $\delta(q, r) = (\delta_e(q, r), \delta_c(q, r), \delta_d(q, r))$ dépendant de l'état $q$ de la machine et du caractère $r$ contenu dans la case du ruban pointée par le curseur. Cette fonction définie sur $Q \times \mathcal{A}$ permet de modifier :
  * l'état de la machine : $\delta_e : Q \times \mathcal{A} \mapsto Q$
  * le caractère de la case du ruban pointée par le curseur : $\delta_c : Q \times \mathcal{A} \mapsto \mathcal{A}$
  * la position du curseur : $\delta_d : Q \times \mathcal{A} \mapsto \\{\leftarrow, \rightarrow\\}$
{% endnote %}

L'***exécution*** est alors identique à la machine simple, sauf pour l'initialisation où le ruban est rempli de caractères blanc plutôt que de `0`.

### <span id="alphabet-equivalence"></span>Equivalence avec la machine de Turing classique

On simule une machine de Turing sur un alphabet $\mathcal{A}$ par une machine de Turing à $|\mathcal{A}|-1$ rubans.

L'idée est d'associer chaque caractère de $\mathcal{A}$ par un $(\mathcal{A}-1)$-uplet valant :

* $(0, \dots, 0)$ pour le caractère blanc
* $(0, \dots, 0, 1, 0, \dots, 0)$ pour un caractère donné

Par exemple si $|\mathcal{A}| = \{a, b, c\}$ avec b valant blanc, on a :

* $(0, 0)$ associé à $b$
* $(1, 0)$ associé à $a$
* $(0, 1)$ associé à $c$

La fonction de transition de la machine est alors répartie sur les rubans. Par exemple si $\delta(q, a)$ fait aller la machine originale à droite, écrit $c$ la machine et change l'état en $q'$, la machine à 2 rubans va avoir comme transition :

* $\delta_1(q, 1, 0) =  (q', 0, \rightarrow)$
* $\delta_2(q, 1, 0) = (q', 1, \rightarrow)$

De façon formelle. Soit une machine de Turing sur un alphabet $\mathcal{A} de fonction de transition $\delta$ et une bijection $\phi: \mathcal{A} \mapsto \\{0, dots, \mathcal{A}-1\\}$ qui associe 0 au caractère blanc.

On construit la fonction de transition de la machine à $\mathcal{A}-1$ ruban telle que si $\delta(q, a) = (q', a', f)$ alors pour le $\mathcal{A}-1$-uplet $(0,\dots , 0, 1, 0, \dots, 0)$ tel que le 1 est à la position $\phi(a)$, on a :

* $\delta_i(q, 0,\dots , 0, 1, 0, \dots, 0) =  (q', 0, f)$ si $i\neq \phi(a')$
* $\delta_i(q, 0,\dots , 0, 1, 0, \dots, 0) =  (q', 1, f)$ si $i = \phi(a')$

On a donc simulé une machine de Turing d'alphabet $\mathcal{A}$ par une machine de TUring à $k$ rubans et comme une machine de Turing à $k$ rubans peut être simulée par une machine de Turing, on en conclut :

{% note "**proposition**" %}
Toute machine de Turing d'alphabet $\mathcal{A}$ peut être simulée par une machine de Turing simple.

Les deux notions sont donc équivalentes.
{% endnote %}

## Machines de Turing non déterministe

Il existe enfin, [la machine de Turing non déterministe](https://fr.wikipedia.org/wiki/Machine_de_Turing_non_d%C3%A9terministe), qui se définit comme suit :

{% note "**définition**" %}
Une ***machine de Turing non déterministe*** diffère de la machine de Turing par sa fonction de transition définie sur $2^{Q \times \\{0, 1\\} \times \\{\leftarrow, \rightarrow\\}}$.
{% endnote %}

Cette machine se distingue de la machine de Turing normale parce que la fonction de transition rend un sous ensemble fini de $Q \times \\{0, 1\\} \times \\{\leftarrow, \rightarrow\\}$ et non juste un nouvel état, un nouveau caractère et une direction : elle donne plusieurs possibilités.

Ce qui nous intéresse ici ce n'est plus l'exécution effective d'une telle machine mais **s'il existe pour une entrée donnée, une suite de transitions emmenant à l'état final**. C'est à dire qu'il existe une suite de nombres $(t_1, \dots, t_k)$ telle que à chaque instruction $i$  on ait pu choisir le $t_i$ème choix pour que la $k$ instruction mène à un état final.

En représentant les choix sous la forme d'un arbre, on peut représenter $\delta$ comme ça :

![Turing non déterministe arbre](turing-nd-arbre.png)

Une exécution de la machine revient à suivre un chemin dans cet arbre, donc qu'à partir de l'état initial $e$ et du caractère $a$ sous le curseur, on a :

* $(e_{t_1}, a_{t_1}, f_{t_1}) \in \delta(e, a)$
* $(e_{t_1\dots t_i}, a_{t_1\dots t_i}, f_{t_1\dots t_i}) \in \delta(e_{t_1t_2\dots t_{i-1}}, a_{t_1t_2\dots t_1i-1})$

C'est un outil théorique très puissant car il permet de démontrer simplement beaucoup de théorèmes d'informatique théorique. Cependant, **elle ne permet pas de faire plus de chose qu'une machine normale** :

{% note %}
Pour toute machine de Turing non déterministe, on peut créer une machine de Turing *normale* qui s'arrêtera sur les même entrées.
{% endnote %}
{% details "idée de la preuve" %}
En utilisant la représentation arborée, on peut faire toutes les possibilités en parcourant l'arbre **couche par couche** (on appelle ça faire un [parcours en largeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur)).

Pour chaque nœud parcouru, on s'arrête lorsque ce nœud est dans l'état `STOP`. On vérifie si le chemin allant du départ à celui si est possible. Si oui, on s'arrête, sinon on continue le parcourt.

Au final, cette machine de Turing s'arrêtera bien si et seulement si la machine de Turing non déterministe s'arrête.
{% enddetails %}

## <span id="MT-01#"></span>Machine de Turing `01#`

La définition d'une machine de Turing la plus couramment utilisée en algorithmie théorique est la machine de Turing d'alphabet $\\{0, 1, #\\}$ avec `#` comme caractère blanc et la possibilité de ne pas avancer le ruban :

{% note "**définition**" %}
Nous nommerons : ***Machine de Turing `01#`*** une machine $M$ de Turing d'alphabet $\\{0, 1, \sharp\\}$ avec `#` comme caractère blanc avec les caractéristiques suivantes  :

* $\delta_d(q, r)$ (ou les $\delta_{d_i}(q, r_1, \dots, r_p)$ si la machine possède plusieurs rubans ou curseurs) prend ses valeurs dans $\\{ \leftarrow, \emptyset, \rightarrow \\}$. Si la valeur est $\emptyset$ le curseur ne bouge pas.
* la **sortie** Machine de Turing `01#` sera la portion de ruban entourant le curseur du premier caractère blanc à la gauche de celui-ci exclu au premier caractère blanc à la droite de celui-ci exclu.
* l'**entrée** sera :
  * $M(E)$ avec $E$ uniquement composée de `0` ou de `1`
  * $M([E])$ avec $[E] = E_1\sharp...\sharp E_i\sharp ...\sharp E_n$ avec les E_i uniquement composée de `0` ou de `1`

Une machine ***Machine de Turing `01#` à $k$ rubans*** aura comme entrée $M(E_1, \dots, E_k)$, $M([E_1], \dots, [E_k])$ ou une combinaison de ceux-ci.
{% endnote %}

La fait d'accepter de ne pas se déplacer permet des transitions de type $\delta_i(q, r_1, \dots, r_p) = (q, r_i, \emptyset)$ pour tout $i \neq I$ et  $\delta_I(q, r_1, \dots, r_p) = (q, r'_I, \leftarrow)$. On peut bouger les rubans indépendamment les uns des autres !

Mais, comme toujours, ce n'est qu'une facilité d'écriture, on ne peut faire plus qu'avec une machine de Tuning *simple* :

{% note "**proposition**" %}
On peut simuler une machine de Turing `01#` à plusieurs rubans et plusieurs curseurs par une machine de Turing.
{% endnote %}
{% details "preuve" %}
Il nous faut juste montrer que l'ajout de transitions où le curseur d'un ruban ne bouge pas peut être simulé par une machine de Turing.

Pour cela on ne va écrire que sur les cases paires du ruban et ajouter des état tampons permettant de simuler le sur place. Ci après un exemple avec 2 rubans et on suppose que le second ruban ne bouge pas alors que le premier va à droite (les autres cas sont identiques):

```
curseur du ruban 1 :     v
parité de la case  : 01010101010
curseur du ruban 2 :     ^
```

Premier état tampon, on se déplace sur une case impaire. Celui qui doit bouger avance et celui qui doit rester sur place recule :

```
curseur du ruban 1 :      v
parité de la case  : 01010101010
curseur du ruban 2 :    ^
```

Second état tampon, l;es deux se déplace dans la même direction :

```
curseur du ruban 1 :       v
parité de la case  : 01010101010
curseur du ruban 2 :     ^
```

{% enddetails %}

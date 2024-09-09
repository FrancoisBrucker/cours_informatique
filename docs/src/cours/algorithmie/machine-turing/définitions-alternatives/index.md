---
layout: layout/post.njk
title: "Définitions alternatives"

eleventyNavigation:
  order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On a vue que le modèle de la machine de Turing permet de créer des programmes ayant les mêmes structures de contrôle que le [pseudo-assembleur](../../../exécuter-code/pseudo-assembleur/){.interne}. C'est au niveau de la gestion de la mémoire que le modèle de la machine de Turing semble moins complet :

- on ne peut lire/écrire qu'au niveau du curseur qui ne peut se déplacer que d'une case par instruction
- il n'y a pas de registre

Nous allons montrer que ce n'est qu'une apparence et qu'en réalité, on peut gérer la mémoire exactement comme on le ferait en pseudo-code.

Nous allons pour cela donner 4 définitions alternatives mais équivalentes d'une machine de Turing.

## Machine de Turing à accès aléatoire en mémoire

Commençons par un cas simple, le fait de ne pas avoir à se déplacer que de 1 case à la fois :

{% note "**définition**" %}
Une **_machine de Turing à accès aléatoire en mémoire_** est composée :

- d'un **_ruban_** (supposé infini) constitué de cases contiguës pouvant chacune contenir soit le caractère `0` soit le caractère `1`
- d'un **_curseur_** qui est positionné sur une case du ruban (on suppose que le ruban est infini à gauche et à droite du curseur)
- d'un ensemble fini $Q$ d'**_états possibles_**, contenant les états `START`{.language-} et `STOP`{.language-}
- d'un **_état courant_** $q \in Q$
- d'une **_fonction de transition_** $\delta(q, r) = (\delta_e(q, r), \delta_c(q, r), \delta_d(q, r))$ dépendant de l'état $q$ de la machine et du caractère $r$ contenu dans la case du ruban pointée par le curseur. Cette fonction définie sur $Q \times \\{0, 1\\}$ permet de modifier :
  - l'état de la machine : $\delta_e : Q \times \\{0, 1\\} \mapsto Q$
  - le caractère de la case du ruban pointée par le curseur : $\delta_c : Q \times \\{0, 1\\} \mapsto \\{0, 1\\}$
  - la position du curseur : $\delta_d : Q \times \\{0, 1\\} \mapsto \mathbb{Z}$
{% endnote %}
  
À l'exécution d'une machine de Turing à accès aléatoire en mémoire, le curseur peut se déplacer d'autant de case vers la droite (si positif) ou la gauche (si négatif) qu'il le souhaite.

### Simulation d'une machine à accès aléatoire en mémoire par une machine simple

Comme le nombre de cases où se déplace le curseur est dans la fonction de transition, c'est une constante associée à chaque état. On peut alors pour chaque état ajouter une chaîne d'état se déplaçant que d'une case et modifier la machine à accès aléatoire en mémoire pour qu'elle ne se déplace plus que d'une case à droite ou une case à gauche.

Ainsi, supposons que $\delta(q, r) = (\delta_e(q, r), \delta_c(q, r), \delta_d(q, r))$, on va distinguer 3 cas :

1. $\delta_d(q, r) = 0$ : dans ce cas là on modifie la transition et on ajoute 1 états :
   1. $\delta(q, r) = (q-0, \delta_c(q, r), +1)$
   2. $\delta(q-0, s) = (\delta_e(q, r), s, -1)$ ($s$ valant 0 ou 1)
2. $\delta_d(q, r) > 1$ : dans ce cas là on modifie la transition et on ajoute $\delta_d(q, r) - 1$ états :
   1. $\delta(q, r) = (q-0, \delta_c(q, r), +1)$
   2. ...
   3. $\delta(q-i, s) = (q-(i+1), s, +1)$ ($s$ valant 0 ou 1)
   4. ...
   5. $\delta(q-(\delta_d(q, r)-1), s) = (\delta_e(q, r), s, +1)$ ($s$ valant 0 ou 1)
3. $\delta_d(q, r) < -1$ : identique au cas précédent, mais dans l'autre sens.

En appliquant ce procédé à tous les état de la machine, on a maintenant une machine équivalente à la machine précédente mais qui se déplace toujours d'une case vers la droite ou une case vers la gauche : c'est une machine classique.

### <span id="accès-aléatoire-equivalence"></span>Equivalence avec la machine de Turing classique

La construction précédente permet d'écrire :

{% note "**Proposition**" %}
Toute machine de Turing à  accès aléatoire en mémoire peut être simulée par une machine de Turing simple.

Les deux notions sont donc équivalentes.
{% endnote %}

## <span id="plusieurs-curseurs"></span>Machine à plusieurs curseurs

Une machine de Turing à $k$ curseurs peut être définie comme suit.

{% note "**définition**" %}
Une **_machine de Turing à $k$ curseurs_** est composée :

- de un **_ruban_** (supposé infini) constitué de cases contiguës pouvant chacune contenir soit le caractère `0` soit le caractère `1`
- de $k$ **_curseurs_**, positionnés sur une case de son ruban (on suppose que le ruban est infini à gauche et à droite du curseur)
- d'un ensemble fini $Q$ d'**_états possibles_**, contenant les états `START` et `STOP`
- d'un **_état courant_** $q \in Q$
- d'une **_fonction de transition_** $\delta(q, c_1, \dots, c_k) = (\delta_e(q, c_1, \dots, c_k), \delta_{c_1}(q, c_1, \dots, c_k), \dots, \delta_{c_k}(q, c_1, \dots, c_k), \delta_{d_1}(q, c_1, \dots, c_k), \dots, \delta_{d_k}(q, c_1, \dots, c_k))$ dépendant de l'état $q$ de la machine et des caractères $r_i$ contenus dans chaque case des rubans pointée par son curseur associé. Cette fonction définie sur $Q \times \\{0, 1\\}^k$ permet de modifier :
  - l'état de la machine : $\delta_e : Q \times \\{0, 1\\}^k \mapsto Q$
  - les caractères des cases pointées par chaque curseur $1\leq i \leq k$ : $\delta_{c_i} : Q \times \\{0, 1\\}^k \mapsto \\{0, 1\\}$
  - les positions des $1\leq i \leq k$ curseurs : $\delta_{d_i} : Q \times \\{0, 1\\}^k \mapsto \\{\leftarrow, \rightarrow\\}$
    {% endnote %}

Cette machine permet de prendre en compte plusieurs cases du ruban pour les transition. La gestion des curseurs est faite ainsi :

- A l'initialisation, les $k$ curseurs sont considérés être sur la même case
- A l'exécution, on effectue l'écriture dans l'ordre des curseurs pour rendre déterministe le comportement d'une étape où deux curseurs sont sur la même case.

On va montrer que cette extension n'en est pas vraiment une car on peut toujours transformer une machine à plusieurs curseurs en une machine de Turing normale équivalente.

Nous allons pour cela montrer que l'on peut simuler une machine à 2 curseurs par une machine à un curseur.

### Simulation d'une machine à $k$ curseurs par une machine simple

Le principe de cette conversion est d'associer à chaque case du ruban de la machine à deux curseurs, une $(k+2)-case composé de $k+2$ cases de la machine à 1 curseur.

Chaque paquet est décomposé ainsi :

- case d'indice 0 : une borne. Un marqueur valant 1 pour une case strictement plus à gauche de tous les curseurs (sera utile pour la suite)
- case d'indice 1 : un marqueur valant 1 si le curseur 1 est est dans la case, 0 sinon
- case d'indice 2 : un marqueur valant 1 si le curseur 2 est est dans la case, 0 sinon
- ...
- case d'indice $k$ : un marqueur valant 1 si le curseur $k$ est est dans la case, 0 sinon
- case d'indice $k+1$ : valeur de la case associée

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

L'idée force est de multiplier les états de la machine pour stocker l'état de tous les curseur et le nouvel état vers lequel aller. Ceci est possible car il n'y a que 2 possibilités de valeur pour chaque case (0 ou 1) et un nombre fini d'états. Pour chaque état $q$, on va ajouter $3^k\cdot (\vert Q\vert + 1)$ états : $(q, c_1, \dots, c_k, q')$ où chaque $c_k \in \{x, 0, 1\}$ et $q' \in Q \cup \{z\}$ (on suppose sans perte de généralité que $z \notin Q$). On rajoute donc beaucoup d'états mais toujours un nombre fini.

On suppose que l'on est dans le cas où la machine à 1 ruban simulant la machine à deux rubans est telle que :

- son état est $q$
- une seule case contient le marqueur du curseur $i$ à 1 ($1\leq i \leq k$)
- une seule case contient le marqueur de la borne à 1 et est strictement à gauche des marqueurs des curseurs 1 et 2
- le curseur est placé sur la case contenant le marqueur de borne

Les différentes étapes ci-après permettent de simuler l'avancement de la machine à $k$ rubans d'un état. Là où une machine $k$ rubans traite l'état $q$ en une étape, nous ferons les 5 étapes suivantes :

1. **préparer le nouvel état** :
   1. passer de l'état $q$ à l'état $(q, x, \dots, x, z)$
2. **trouver l'état actuel**. On exécute la procédure suivante avec les paramètres $(i, q, x, \dots, x, z)$ pour $i$ allant de 1 à k:
   1. se déplacer de $i$ cases vers la droite
   2. si `1` sur le ruban aller en 5
   3. se déplacer de $k+2$ cases vers la droite
   4. aller en 1
   5. se déplacer de $k-i$ cases vers la droite
   6. passer de l'état $(i, q, c_1, \dots, c_k, z)$ à l'état $(i, q, c'_1, \dots, c'_k, z)$ où :
      - $c'_j = c_j$ pour tout $j \neq i$
      - $c'_i$ vaut la valeur du ruban (`1` ou `0`)
   7. se déplacer de $k+1$ cases vers la gauche
   8. se déplacer de $k+2$ cases vers la gauche
   9. si `0` sur le ruban aller en 7.
3. passer de l'état $(q, c_1, \dots, c_k, z)$ à l'état $(q, c_1, \dots, c_k, \delta_e(q, c_1, \dots, c_k))$
4. **Écriture des nouvelles valeurs sur le ruban**. On exécute la procédure suivante avec les paramètres $(i, q, c_1, \dots, c_k, q')$ pour $i$ allant de 1 à k:
   1. se déplacer de $i$ cases vers la droite
   2. si `1` sur le ruban aller en 5
   3. se déplacer de $k+2$ cases vers la droite
   4. aller en 1
   5. se déplacer de $k-i$ cases vers la droite
   6. placer $\delta_{c_i}(q, c_1, \dots, c_k)$ sur le ruban
   7. se déplacer de $k+1$ cases vers la gauche
   8. se déplacer de $k+2$ cases vers la gauche
   9. si `0` sur le ruban aller en 7.
5. **Déplacement des curseurs**. On exécute la procédure suivante avec les paramètres $(i, q, c_1, \dots, c_k, q')$ pour $i$ allant de 1 à k:
   1. se déplacer de $i$ cases vers la droite
   2. si `1` sur le ruban aller en 5
   3. se déplacer de $k+2$ cases vers la droite
   4. aller en 1
   5. écrire `0` sur le ruban
   6. si $\delta_{d_i}(q, c_1, \dots, c_k) = \rightarrow$ se déplacer de $k+2$ cases vers la droite, sinon $k+2$ cases vers la gauche
   7. écrire `1` sur le ruban
   8. se déplacer de $i$ cases vers la gauche
   9. si `0` sur le ruban aller en 14.
   10. écrire `0` sur le ruban
   11. se déplacer de $k+2$ cases vers la gauche
   12. écrire `1` sur le ruban
   13. aller en 15
   14. se déplacer de $k+2$ cases vers la gauche
   15. si `0` sur le ruban aller en 14.
6. **fin de transition** :
   1. passer de l'état $(q, c_1, \dots, c_k, \delta_e(q, c_1, \dots, c_k))$ à l'état $\delta_e(q, c_1, \dots, c_k)$

Après ces 6 méta-étapes, la machine est de nouveau dans un état stable et peut recommencer son cycle.

Les étapes précédentes peuvent être écrite en utilisant le formalisme des [compositions de machine](../composition){.interne}. Ceci fonctionne car $k$ est une constante et le nombre d'états fini. On peut donc utiliser les procédures qui génèrent autant d'états que nécessaire.

### Exemple

Supposons que l'on ait la machine à deux ruban suivante :

```
numéro case :  12345
ruban       :  010101
curseurs    :    ^ ^
                 2 1
```

Et qu'il soit simulé par la machine à 1 ruban :

```
indice paquet de 4 cases  : 012301230123012301230123
ruban                     : 000010010010000101000001
curseur                   :     ^
```

On veut passer de à l'état $\delta(q, 0, 0) = (q', 1, 0, \rightarrow, \leftarrow)$. On montre chaque fin d'étape

```
indice 4-cases          : 012301230123012301230123
étape - état
1     - (q, x, x, z)    : 000010010010000101000001
                        :     ^
2.1   - (1, q, x, x, z) : 000010010010000101000001
                        :      ^
...

```

> TBD finir l'exemples
> faire l'exemple avec 2 curseurs. Parler des différentes parties. En particulier le décalage de la borne

Cela fait tout un tas de transitions, mais on arrive bien à simuler les $2$ curseurs par un seul !

### <span id="curseurs-equivalence"></span>Equivalence avec la machine de Turing classique

{% note "**Proposition**" %}
Toute machine de Turing à $k$ curseurs peut être simulée par une machine de Turing simple.

Les deux notions sont donc équivalentes.
{% endnote %}

## <span id="plusieurs-rubans"></span>Machine à plusieurs rubans

Une machine de Turing à $k$ rubans peut être définie comme suit.

{% note "**définition**" %}
Une **_machine de Turing à $k$ rubans_** est composée :

- de $k$ **_rubans_** (supposés infinis) constitués de cases contiguës pouvant chacune contenir soit le caractère `0` soit le caractère `1`
- de $k$ **_curseurs_**, un par ruban, positionnés sur une case de son ruban (on suppose que le ruban est infini à gauche et à droite du curseur)
- d'un ensemble fini $Q$ d'**_états possibles_**, contenant les états `START` et `STOP`
- d'un **_état courant_** $q \in Q$
- d'une **_fonction de transition_** $\delta(q, r_1, \dots, r_k) = (\delta_e(q, r_1, \dots, r_k), \delta_{c_1}(q, r_1, \dots, r_k), \dots, \delta_{c_k}(q, r_1, \dots, r_k), \delta_{d_1}(q, r_1, \dots, r_k), \dots, \delta_{d_k}(q, r_1, \dots, r_k))$ dépendant de l'état $q$ de la machine et des caractères $r_i$ contenus dans chaque case des rubans pointée par son curseur associé. Cette fonction définie sur $Q \times \\{0, 1\\}^k$ permet de modifier :
  - l'état de la machine : $\delta_e : Q \times \\{0, 1\\}^k \mapsto Q$
  - les caractères des cases de chaque ruban $1\leq i \leq k$ pointées par les curseurs : $\delta_{c_i} : Q \times \\{0, 1\\}^k \mapsto \\{0, 1\\}$
  - les positions des $1\leq i \leq k$ curseurs : $\delta_{d_i} : Q \times \\{0, 1\\}^k \mapsto \\{\leftarrow, \rightarrow\\}$
    {% endnote %}

L'**_exécution_** est alors identique à la machine simple. Tout se passe comme si on avait $k$ machines différentes, mais un seul état et une fonction de transition dépendant de tous les rubans.

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

### <span id="rubans-equivalence"></span>Equivalence avec la machine de Turing classique

La procédure précédente peut se généraliser à $k$ rubans et on peut alors simuler une machine à $k$ rubans par une machine à $k$ curseur elle-même simulation par une machine classique :

{% note "**Proposition**" %}
Toute machine de Turing à $k$ rubans peut être simulée par une machine de Turing simple.

Les deux notions sont donc équivalentes.
{% endnote %}

## Machines à plusieurs curseurs et rubans

On peut bien sur combiner les deux approches et construire une machine de Turing à $k$ rubans et $k'$ curseurs répartis sur les rubans. Mais, comme vous devez vous en douter :

{% note "**Proposition**" %}
Toute machine de Turing à $k$ rubans et $k'$ curseurs peut être simulée par une machine de Turing simple.

Les deux notions sont donc équivalentes.
{% endnote %}
{% details "preuve", "open" %}
En utilisant les technique de preuve précédentes on arrive facilement à montrer que :

- toute machine de Turing à $k$ rubans et $k'$ curseurs peut être simulée par une machine de Turing $1$ rubans et $k'$ curseurs.
- toute machine de Turing à $k$ rubans et $k'$ curseurs peut être simulée par une machine de Turing $k$ rubans et $1$ curseur.

{% enddetails %}

## Alphabets

Ne travailler qu'avec des `0` et des `1` peut sembler réducteur :

{% note "**définition**" %}
Une **_machine de Turing sur un alphabet $\mathcal{A}$_** est composée :

- d'un ensemble fini $\mathcal{A}$ nommé **_alphabet_**
- un **_caractère blanc_**, élément de $\mathcal{A}$
- d'un **_ruban_** (supposé infini) constitué de cases contiguës pouvant chacune contenir des caractères de $\mathcal{A}$
- d'un **_curseur_** qui est positionné sur une case du ruban (on suppose que le ruban est infini à gauche et à droite du curseur)
- d'un ensemble fini $Q$ d'**_états possibles_**, contenant les états `START`{.language-} et `STOP`{.language-}
- d'un **_état courant_** $q \in Q$
- d'une **_fonction de transition_** $\delta(q, r) = (\delta_e(q, r), \delta_c(q, r), \delta_d(q, r))$ dépendant de l'état $q$ de la machine et du caractère $r$ contenu dans la case du ruban pointée par le curseur. Cette fonction définie sur $Q \times \mathcal{A}$ permet de modifier :
  - l'état de la machine : $\delta_e : Q \times \mathcal{A} \mapsto Q$
  - le caractère de la case du ruban pointée par le curseur : $\delta_c : Q \times \mathcal{A} \mapsto \mathcal{A}$
  - la position du curseur : $\delta_d : Q \times \mathcal{A} \mapsto \\{\leftarrow, \rightarrow\\}$
    {% endnote %}

L'**_exécution_** est alors identique à la machine simple, sauf pour l'initialisation où le ruban est rempli de caractères blanc plutôt que de `0`.

### <span id="alphabet-equivalence"></span>Equivalence avec la machine de Turing classique

On simule une machine de Turing sur un alphabet $\mathcal{A}$ par une machine de Turing à $|\mathcal{A}|-1$ rubans.

L'idée est d'associer chaque caractère de $\mathcal{A}$ par un $(\mathcal{A}-1)$-uplet valant :

- $(0, \dots, 0)$ pour le caractère blanc
- $(0, \dots, 0, 1, 0, \dots, 0)$ pour un caractère donné

Par exemple si $|\mathcal{A}| = \{a, b, c\}$ avec b valant blanc, on a :

- $(0, 0)$ associé à $b$
- $(1, 0)$ associé à $a$
- $(0, 1)$ associé à $c$

La fonction de transition de la machine est alors répartie sur les rubans. Par exemple si $\delta(q, a)$ fait aller la machine originale à droite, écrit $c$ la machine et change l'état en $q'$, la machine à 2 rubans va avoir comme transition :

- $\delta_1(q, 1, 0) =  (q', 0, \rightarrow)$
- $\delta_2(q, 1, 0) = (q', 1, \rightarrow)$

De façon formelle. Soit une machine de Turing sur un alphabet $\mathcal{A}$ de fonction de transition $\delta$ et une bijection $\phi: \mathcal{A} \mapsto \\{0, dots, \mathcal{A}-1\\}$ qui associe 0 au caractère blanc.

On construit la fonction de transition de la machine à $\mathcal{A}-1$ ruban telle que si $\delta(q, a) = (q', a', f)$ alors pour le $\mathcal{A}-1$-uplet $(0,\dots , 0, 1, 0, \dots, 0)$ tel que le 1 est à la position $\phi(a)$, on a :

- $\delta_i(q, 0,\dots , 0, 1, 0, \dots, 0) =  (q', 0, f)$ si $i\neq \phi(a')$
- $\delta_i(q, 0,\dots , 0, 1, 0, \dots, 0) =  (q', 1, f)$ si $i = \phi(a')$

On a donc simulé une machine de Turing d'alphabet $\mathcal{A}$ par une machine de TUring à $k$ rubans et comme une machine de Turing à $k$ rubans peut être simulée par une machine de Turing, on en conclut :

{% note "**Proposition**" %}
Toute machine de Turing d'alphabet $\mathcal{A}$ peut être simulée par une machine de Turing simple.

Les deux notions sont donc équivalentes.
{% endnote %}

## <span id="MT-01#"></span>Machine de Turing `01#`

La définition d'une machine de Turing la plus couramment utilisée en algorithmie théorique est la machine de Turing d'alphabet $\\{0, 1, \sharp\\}$ avec `#` comme caractère blanc et la possibilité de ne pas avancer le ruban :

{% note "**définition**" %}
Nous nommerons : **_Machine de Turing `01#`_** une machine $M$ de Turing d'alphabet $\\{0, 1, \sharp\\}$ avec `#` comme caractère blanc avec les caractéristiques suivantes :

- $\delta_d(q, r)$ (ou les $\delta_{d_i}(q, r_1, \dots, r_p)$ si la machine possède plusieurs rubans ou curseurs) prend ses valeurs dans $\\{ \leftarrow, \emptyset, \rightarrow \\}$. Si la valeur est $\emptyset$ le curseur ne bouge pas.
- la **sortie** Machine de Turing `01#` sera la portion de ruban entourant le curseur du premier caractère blanc à la gauche de celui-ci exclu au premier caractère blanc à la droite de celui-ci exclu.
- l'**entrée** sera :
  - $M(E)$ avec $E$ uniquement composée de `0` ou de `1`
  - $M([E])$ avec $[E] = E_1\sharp...\sharp E_i\sharp ...\sharp E_n$ avec les E_i uniquement composée de `0` ou de `1`

Une machine **_Machine de Turing `01#` à $k$ rubans_** aura comme entrée $M(E_1, \dots, E_k)$, $M([E_1], \dots, [E_k])$ ou une combinaison de ceux-ci.
{% endnote %}

La fait d'accepter de ne pas se déplacer permet des transitions de type $\delta_i(q, r_1, \dots, r_p) = (q, r_i, \emptyset)$ pour tout $i \neq I$ et $\delta_I(q, r_1, \dots, r_p) = (q, r'_I, \leftarrow)$. On peut bouger les rubans indépendamment les uns des autres !

Mais, comme toujours, ce n'est qu'une facilité d'écriture, on ne peut faire plus qu'avec une machine de Tuning _simple_ :

{% note "**Proposition**" %}
On peut simuler une machine de Turing `01#` à plusieurs rubans et plusieurs curseurs par une machine de Turing.
{% endnote %}
{% details "preuve", "open"  %}
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

Second état tampon, les deux se déplacent dans la même direction :

```
curseur du ruban 1 :       v
parité de la case  : 01010101010
curseur du ruban 2 :     ^
```

{% enddetails %}

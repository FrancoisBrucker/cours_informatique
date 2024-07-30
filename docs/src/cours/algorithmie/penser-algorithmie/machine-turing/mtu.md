---
layout: layout/post.njk 
title:  "Machine de Turing universelle"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Ce qui différencie une machine de Turing d'une autre c'est la fonction de transition.

Un des résultats les plus surprenant de Turing est qu'en fait on ne peut construire qu'**une seule machine** qui simulera toutes les autres. Cette machine est appelée [Machine de Turing universelle](https://fr.wikipedia.org/wiki/Machine_de_Turing_universelle) et possède deux paramètres, le premier, $M$ représentant le programme d'une machine de Turing et le second $E$ une entrée.

Nous allons dans cette partie faire deux choses :

1. encoder une machine de Turing sous la forme d'une suite de `0` et de `1`
2. écrire une machine, nommée [Machine de Turing Universelle](https://fr.wikipedia.org/wiki/Machine_de_Turing_universelle) (MTU), qui prend ses encodages en paramètre et les exécute

{% info %}
Nous utiliserons ici dès que nous le pourrons et sans perte de généralité les [Machines de Turing `01#`](../définitions-alternatives/#MT-01#) ce qui nous permettra, entre autres, d'avoir plusieurs paramètres d'entrée.
{% endinfo %}

## code associé à une machine

Une machine de Turing $M$, est définie par sa fonction de transition. Coder $M$ revient à lui associer de façon bijective une suite binaire, il faut donc un moyen d'encoder les 3 fonctions constituant la fonction de transition :

- $\delta_e: Q \times \\{1, 0\\} \mapsto Q$
- $\delta_c: Q \times \\{1, 0\\} \mapsto \\{1, 0\\}$
- $\delta_d: Q \times \\{1, 0\\} \mapsto \\{\leftarrow, \rightarrow\\}$

Par des suites de `0` et de `1`.

### Encodage

Pour cela considérons les bijections :

- $\phi_q: Q \mapsto [\\![ 0, |Q|-1]\\!]$ telle que :
  - $\phi_q(\text{START}) = 0$
  - $\phi_q(\text{STOP}) = 1$
- $\phi_d: \\{\leftarrow, \rightarrow\\} \mapsto \\{0, 1\\}$ telle que :
  - $\phi_d(\leftarrow) = 0$
  - $\phi_d(\rightarrow) = 1$

Encoder une transition par un quintuplet :

$$
T(q, r) = (\phi_q(q), r, \phi_q(\delta_e(q, r)), \delta_c(q, r), \phi_d(\delta_d(q, r)))
$$

Et finalement associer à la fonction de transition le tableau constitué de la concaténation ($+$ est ici l'opération de concaténation des tableaux):

$$
T = T(q_1, 0) + T(q_1, 1) + \dots + T(q_i, 0) + T(q_i, 1) + \dots + T(q_{|Q|}, 0) + T(q_{|Q|}, 1)
$$

On a alors les correspondances :

- $\delta_e(q, r) = T[5 \cdot (k + r) + 2]$
- $\delta_c(q, r) = T[5 \cdot (k + r) + 3]$
- $\delta_d(q, r) = T[5 \cdot (k + r) + 4]$

Avec $k$ le plus petit indice tel que $T[5\cdot k] = \phi_q(q)$

Par exemple, [la machine oscillation](../définition/#exemple-oscillation) pourra par exemple être encodée par :

<div>
$$
\begin{array}{rl}
T = (0, 0, 2, 0, 0,\\
     0, 1, 0, 0, 0, & \text{quintuplet jamais utilisé} \\
     1, 0, 0, 0, 0, & \text{quintuplet jamais utilisé} \\
     1, 1, 0, 0, 0, & \text{quintuplet jamais utilisé} \\
     2, 0, 3, 1 , 1,\\
     2, 1, 0, 0, 0,& \text{quintuplet jamais utilisé} \\
     3, 0, 4, 0, 1,\\
     3, 1, 3, 1, 1,\\
     4, 0, 1, 1, 0,\\
     4, 1, 3, 1, 1)\\
\end{array}
$$
</div>

Il nous reste à transformer cette liste d'entiers en suite de `0` et de `1`. Chaque entier peut évidemment s'écrire sous sa forme binaire, ce qui donne pour l'oscillateur :

<div>
$$
\begin{array}{rl}
T = (0, 0, 10, 0, 0,\\
     0, 1, 0, 0, 0, \\
     1, 0, 0, 0, 0,\\
     1, 1, 0, 0, 0, \\
     10, 0, 11, 1 , 1,\\
     10, 1, 0, 0, 0, \\
     11, 0, 100, 0, 1,\\
     11, 1, 11, 1, 1,\\
     100, 0, 1, 1, 0,\\
     100, 1, 11, 1, 1)\\
\end{array}
$$
</div>

Mais il nous faut aussi encoder la virgule ce qui nous fait 3 symboles à encoder avec seulement des `0` et des `1`.

On utilise alors l'astuce classique d'encoder :

- `0` par `00`,
- `1` par `01`,
- `,` par `11`.

Ce qui double la taille des nombre (on lit un chiffre sur 2) mais permet d'encoder nos 3 caractères. On a alors pour l'oscillateur :

<div>
$$
\begin{array}{rl}
T = 0011001101001100110011\\
    00110111001100110011 \\
    01110011001100110011\\
    01110111001100110011\\
    010011001101011101110111\\
    0100110111001100110011 \\
    01011100110100001100110111\\
    010111011101011101110111\\
    010000110011011101110011\\
    010000110111010111011101\\
\end{array}
$$
</div>

{% note "**Définition**" %}
On note $\<M\>$ l'encodage de la fonction de transition associé à la machine de Turing $M$.
{% endnote %}

### Décodage

Pour le décodage, on peut supposer qu'on le fait avec une machine de Turing `01#` à plusieurs rubans, donc on examine les couples $T[2i:2(i+1)]$ pour tous les $i$ de façons croissante et on associe dans un autre ruban :

- `0` à `00`,
- `1` à `01`,
- `#` à `11`.

À la fin de cette opération on aura le tableau représentant la machine dans un ruban dédié. Pour l'oscillateur cela donnerait :

```
ruban      : 0#0#10#0#0#0#1#0#0#0#1#0#0#0#0#1#1#0#0#0#10#0#11#1#1#10#1#0#0#0#11#0#100#0#1#11#1#11#1#1#100#0#1#1#0#100#1#11#1#1
transition : 0 0        0 1       1 0       1 1        2 0         2 1        3 0          3 1          4 0         4 1
indice     : 0 1 2  3 4 0 1 2 3 4 0 1 2 3 4 0 1 2 3 4  0 1  2 3 4  0 1 2 3 4  0 1   2 3 4  0 1  2 3 4   0 1 2 3 4   0 1  2 3 4
```

## <span id="MTU"></span> Machine de Turing Universelle (MTU)

### <span id="pseudo-code-MTU"></span>Algorithme

Le pseudo-code ci-après décrit le principe d'une machine de Turing universelle.

```
Nom : MTU
Entrées : 
    T : une fonction de transition sous la forme d'un tableau
    E : une suite de 0 et de 1
Programme :
    Soit R un ruban initialement rempli par E et un curseur c qui pointe sur une le premier caractère de E.
    q = 0

    Tant que q ≠ 1:
      Soit r la valeur de la case du ruban pointée par c    
      Trouver le plus petit k tel que T[5k] = q

      écrire T[5(k+r) + 3] sur R
      déplacer le curseur à droite si T[5(k+r) + 4] == 1 et vers la gauche sinon
      q = T[5(k+r) + 2]

    Rendre R
```

On voit que la MTU va simuler toute machine de Turing encodée par T.

### Création effective

Pour terminer la preuve, il nous reste à montrer que le pseudo-code précédent et T peuvent être converti en une machine de Turing et son entrée.

Ceci est plus facile qu'attendu car on peut simuler une [machines de Turing `01#`](../définitions-alternatives/#MT-01#){.interne} à plusieurs rubans par une machine de Turing.

Commençons par voir le nombre de rubans qu'il nous faudrait pour être bien :

- pour la machine à simuler, on peut demander 6 rubans :
  - `R-S` : un ruban contenant le ruban de la machine simulée
  - cinq rubans permettant de stocker la transition :
    - `R-T0` : un ruban contenant les éléments $E[5\cdot k]$ séparé par des `#`
    - `R-T1` : un ruban contenant les éléments $E[5\cdot k + 1]$ séparé par des `#`
    - `R-T2` : un ruban contenant les éléments $E[5\cdot k + 2]$ séparé par des `#`
    - `R-T3` : un ruban contenant les éléments $E[5\cdot k + 3]$ séparé par des `#`
    - `R-T4` : un ruban contenant les éléments $E[5\cdot k + 4]$ séparé par des `#`
- pour le simulateur 2 rubans supplémentaires devraient suffire :
  - un ruban `R-Q` pour stocker l'état courant `q` : On supposera que le curseur est toujours placé au début de l'état. On initialisera ce ruban en recopiant le premier élément de l'entrée $E$
  - `R-I` : un dernier ruban pour les opérations internes de la MTU

Enfin, il faut adapter le pseudo-code de la MTU à notre machine. Ceci est aisé puisque :

- les différents paramètres sont des chaînes formées des caractères `0` et `1` séparées par 1 caractères `#` qui ne sont utilisé que comme séparateur
- dés que l'on rencontre la chaîne  `##`, on est en bout de ruban (la suite à gauche ou à droite sera uniquement composées de `#`)
- on peut bouger les curseurs de façon indépendante et donc avec des sous-programmes qui ne manipulent que certains rubans.

On obtient alors l'algorithme ci-après qui est une écriture de l’algorithme de la MTU sous une forme où chaque étape est facilement implémentable avec une machine de Turing `01#` :

1. Initialisation. Elle peut aisément être fait par une machine de Turing qui dispatche l'entrée sur les différents rubans
   1. Le ruban `R-Q` contient la chaîne `0`. Son curseur est placé sur le caractère non `#` le plus à gauche
   2. le ruban `R-T0` contient tous les éléments $E[5\cdot k]$, de $k=0$ jusqu'au premier élément $k_\max$ tel que $E[5\cdot k_\max] = \sharp$. Son curseur est placé sur le caractère non `#` le plus à gauche
   3. le ruban `R-T1` contient tous les éléments $E[5\cdot k + 1]$, de $k=0$ jusqu'au premier élément $k_\max$ tel que $E[5\cdot k_\max + 1] = \sharp$. Son curseur est placé sur le caractère non `#` le plus à gauche
   4. le ruban `R-T2` contient tous les éléments $E[5\cdot k + 2]$, de $k=0$ jusqu'au premier élément $k_\max$ tel que $E[5\cdot k_\max + 2] = \sharp$. Son curseur est placé sur le caractère non `#` le plus à gauche
   5. le ruban `R-T3` contient tous les éléments $E[5\cdot k + 3]$, de $k=0$ jusqu'au premier élément $k_\max$ tel que $E[5\cdot k_\max + 3] = \sharp$. Son curseur est placé sur le caractère non `#` le plus à gauche
   6. le ruban `R-T4` contient tous les éléments $E[5\cdot k + 4]$, de $k=0$ jusqu'au premier élément $k_\max$ tel que $E[5\cdot k_\max + 4] = \sharp$. Son curseur est placé sur le caractère non `#` le plus à gauche
   7. le rubans `R-S` contient `E` et le curseur est placé sur le premier caractère non `#` le plus à gauche.
   8. le ruban `R-I` est initialement vide.
2. Trouver la transition courante :
   1. recopier le paramètre du ruban `R-Q` sur `R-I` se décaler d'un cran à droite sur `R-I` et se replacer au début du paramètre sur `R-Q`
   2. recopier le paramètre du ruban `R-T0` sur `R-I` se décaler sur la gauche sur `R-I` jusqu'à être au début du ruban (à gauche du curseur il y a deux caractères `#` à la suite) et se replacer au début du paramètre sur `R-T0`
   3. exécuter un programme qui s'arrête sur un `1` sur `R-I` si les deux paramètres du ruban `R-I` sont égaux et qui s'arrête sur un `0` sinon
   4. Si le résultat vaut `0` :
      1. effacer le ruban `R-I`
      2. décaler les rubans `R-T0` à `R-T4` d'un paramètre à droite
   5. Si le résultat vaut `1` :
      1. si la valeur du ruban de `R-S` vaut la valeur sur le ruban `R-T1`, aller en 3.
      2. sinon décaler les rubans `R-T0` à `R-T4` d'un paramètre à droite et retour en 2.
3. Faire la transition courante sur `R-S`
   1. nouvel état : efface le ruban `R-Q` et écriture du paramètre de `R-T2` sur `R-Q`
   2. écriture du ruban : écriture de la case sous `R-T3` sur `R-S`
   3. déplacement du ruban : déplacement de `R-S` vers la droite si la case du ruban `R-T4` vaut `1` et déplacement vers la gauche sinon
4. Retour au début des paramètres pour les rubans `R-Q` et de `R-T0` à `R-T4` (à gauche de chaque curseur il y a deux caractères `#` à la suite)
5. retour en 2.

## Conclusion

Nous venons de faire un ordinateur avec une machine de Turing ! La machine de Turing est tout à la fois un programme et une machine pour exécuter automatiquement des programmes.

{% note "**Théorème fondamental de l'algorithmie**" %}
On peut encoder toute machine de Turing $M$ par une chaîne $\<M\>$ composée de `0` et de `1`, de telle sorte que l'exécution de la machine de Turing universelle $\text{MTU}(\<M\>, E)$ simule l'exécution de $M$ avec une entrée $E$.

{% endnote %}

La machine de Turing universelle est donc [la machine qui les gouverne toutes](https://fr.wikipedia.org/wiki/Anneau_unique) : une machine qui permet de simuler toutes les autres machine.

Il suffit de construire une seule machine pour avoir toutes les machines de Turing possible via leur code.

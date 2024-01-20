---
layout: layout/post.njk 
title:  "Équivalence entre pseudo-code et machine de Turing"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[Le pseudo-code](../../pseudo-code/){.interne} est une façon d'écrire des algorithmes, nous allons voir dans cette partie qu'un pseudo-code est équivalent à une machine de Turing et qu'on (les informaticiens) est même persuadé que c'est aussi équivalent à la notion même d'algorithme.

Nous allons démontrer dans cette partie que les notions de pseudo-code et de Machine de Turing sont les mêmes. IL est équivalent d'écrire ses algorithmes sous la forme de pseudo-code ou de Machine de Turing. On se demande même si la notion même d'algorithme n'est pas équivalente à celle de pseudo-code, c'est la [Thèse de Church-Turing](./#thèse-Church-Turing)

Pour cela, nous allons commencer à montrer que tout pseudo-code peut être écrit sous la forme d'une machine de Turing, puis que toute machine de Turing peut être écrite sous la forme de pseudo-code grâce à l'introduction d'une machine particulière, la machine deTuring universelle.

## Turing et pseudo-code minimal

Le but de cette partie est de montrer l'implication :

{% note "**Proposition**" %}

Tout [pseudo-code](../../pseudo-code/){.interne} peut être simulé par une [machine de Turing](../définition){.interne}.

{% endnote %}

### Pseudo-code minimal

Nous allons donner ici une version expurgé de la notion d'algorithme et de pseudo-code. Cette version, plus compliquée à écrire mas pas plus puissante sera plus facile à mettre en correspondance avec les machines de Turing.

#### Objets et opérations d'un algorithme

On a vu qu'un [algorithme](../../algorithme/définition/){.interne} pouvait ne manipuler que des entiers.

Sous sa représentation binaire, un entier étant un tableau de bit, on en conclut :

{% note %}
Les seuls objets qu'un **algorithme** peut utiliser sont les tableaux de bits.
{% endnote %}

De plus, toutes les opérations arithmétiques sur les nombres binaires peuvent se déduire de l'addition et l'addition peut s'écrire en utilisant uniquement l'opération [NON-ET](https://fr.wikipedia.org/wiki/Fonction_NON-ET).

{% lien %}
Sur comment faire, voir par exemple <https://www.circuits-logiques.polymtl.ca/help/Chapitre05.pdf>
{% endlien %}

De là :

{% note %}
La seule opération qu'un **algorithme** peut utiliser est l'opération [NON-ET](https://fr.wikipedia.org/wiki/Fonction_NON-ET)
{% endnote %}

On peut donc se restreindre aux pseudo-codes pouvant manipuler des bits avec l'opération booléenne NON-ET.

#### Structures de contrôles

Un algorithme dans toute sa généralité n'a pas de définition précise d'une structure de contrôle, mais un [pseudo-code](../../pseudo-code/){.interne}, oui. Il possède :

- une instruction conditionnelle : SI condition ALORS bloc
- une répétition conditionnelle : TANT QUE condition EXÉCUTE bloc

Une condition devant être vraie (1) ou fausse (0), on peut se restreindre à :

{% note %}
Les seules structures de contrôle nécessaires pour un **pseudo-code** sont :

- SI v == 0 ALORS  bloc
- TANT QUE v == 0 EXÉCUTER bloc

{% endnote %}

### Machine de Turing et pseudo-code minimal

Il est clair que la machine de Turing possède les propriétés nécessaire pour convertir du pseudo code minimal en fonction de transition :

- le ruban nous permet d'avoir des tableaux de bits
- les condition `SI r == 0 ALORS  machine` a été définie dans la partie [composition de machines](../définition/#composition-machine){.interne}. Une machine étant pouvant être considéré comme un bloc d'instructions.
- l'opération NON-ET peut être est trivialement construite sous la forme d'une fonction de transition

Pour gérer les variables, l'équivalence des machines de Turing nous permet d'utiliser une machine à plusieurs rubans, dont 1 est consacré au stockage des variables. Ceci nous permet de définir les opérations :

- SI v == 0 ALORS  bloc
- TANT QUE v == 0 EXÉCUTER bloc

Et donc on en conclut :

{% note "**proposition**" %}

Tout [Pseudo-code]("../..//pseudo-code/"){.interne} peut être simulé par une [machine de Turing](../définition){.interne}.

{% endnote %}

## Pseudo-code et Turing <span id="mtu"></span>

Il nous reste à montrer l'autre implication :

{% note "**Proposition**" %}

Toute machine de Turing peut être écrite sous la forme de pseudo-code.

{% endnote %}

La preuve de cette implication est magnifique (on la doit à Turing lui-même) car elle montre qu'un ordinateur - dont le but est d'exécuter des programmes donc des machines - est lui aussi une machine de Turing.

Ce qui différencie une machine de Turing d'une autre c'est la fonction de transition.

Un des résultats les plus surprenant de Turing est qu'en fait on ne peut construire qu'**une seule machine** qui simulera toutes les autres. Cette machine est appelée [Machine de Turing universelle](https://fr.wikipedia.org/wiki/Machine_de_Turing_universelle) et possède deux paramètres, le premier, $M$ représentant le programme d'une machine de Turing et le second $E$ une entrée.

Avant de construire effectivement une machine de Turing universelle, essayons de voir comment en encoder une sous la forme d'une ou plusieurs chaînes de 0 et de 1.

### Encodage d'une machine

Une machine de Turing, est définie par sa fonction de transition. Il nous faut donc un moyen d'encoder les 3 fonctions constituant la fonction de transition :

- $\delta_e: Q \times \\{1, 0\\} \mapsto Q$
- $\delta_c: Q \times \\{1, 0\\} \mapsto \\{1, 0\\}$
- $\delta_d: Q \times \\{1, 0\\} \mapsto \\{\leftarrow, \rightarrow\\}$

Par des suites de `0` et de `1`.

On peut pour cela considérer des bijections :

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

Et finalement associer à la fonction de transition le tableau constitué de la concaténation :

$$
T = T(q_1, 0) + CT(q_1, 1) + \dots + CT(q_i, 0) + CT(q_i, 1) + \dots + CT(q_{|Q|}, 0) + CT(q_{|Q|}, 1)
$$

On a alors les correspondances :

- $\delta_e(q, r) = T[5 \cdot (k + r) + 2]$
- $\delta_c(q, r) = T[5 \cdot (k + r) + 3]$
- $\delta_d(q, r) = T[5 \cdot (k + r) + 4]$

Avec $k$ le plus petit indice tel que $T[5\cdot k] = \phi_q(q)$

Par exemple, [la machine oscillation](../définition/#exemple-oscillation) pourra par exemple être encodée par :

<div>
$$
\begin{array}{r}
T = (0, 0, 2, 0, 0,\\
     2, 0, 3, 1 , 1,\\
     3, 0, 4, 0, 1,\\
     3, 1, 3, 1, 1,\\
     4, 1, 3, 1, 1,\\
     4, 0, 1, 1, 0)\\
\end{array}
$$
</div>

### <span id="MTU"></span> Machine de Turing Universelle (MTU)

#### <span id="pseudo-code-MTU"></span>Principe

Le pseudo-code ci-après décrit le principe d'une machine de Turing universelle.

```
Nom : MTU
Entrée : 
    T : une fonction de transition sous la forme d'un tableau
Programme :
    Soit R un ruban initialement vide et un curseur c qui pointe sur une de ses cases.
    q = 0

    Tant que q ≠ 1:
      Soit r la valeur de la case du ruban pointée par c    
      Trouver le plus petit k tel que T[5k] = q

      écrire T[5(k+r) + 3] sur R
      déplacer le curseur à droite si T[5(k+r) + 4] == 1 et vers la gauche sinon
      q = T[5(k+r) + 2]

    Rendre R
```

On voit que la MTU va simulée toute machine de Turing encodée par T.

#### Création effective

Pour terminer la preuve, il nous reste à montrer que le pseudo-code précédent et T peuvent être converti en une machine de Turing et son entrée.

Ceci est plus facile qu'attendu car :

- on peut simuler une [machines de Turing `01#`](../définitions-alternatives/#MT-01#){.interne} par une machine de Turing.
- on peut simuler tout pseudo-code par une machine de Turing

Commençons par transformer $T$ en une entrée composée des caractères `0`, `1` et `#` :

- on sépare chaque élément par des `#`
- le seul élément qui n'est pas un `0` ou un `1` est l'état qui est un entier. On peut le représenter par sa représentation unaire. Pour représenter $0 \leq q < |Q| on a :
  - $q$ caractères `1`
  - suivis de $|Q| - 1 - q$ caractères `0`

Par exemple, [la machine oscillation](../définition/#exemple-oscillation){.interne} sera encodée par la chaîne :

```
E : 0000#0#1100#0#0#1100#0#1110#1#1#1110#0#1111#0#1#1110#1#1110#1#1#1111#0#1110#1#1#1111#1#1000#1#0
k : 0               1               2               3               4               5
```

Cette transformation est l'entrée $E$ de notre MTU.

Puis nous allons simuler la MTU par une machine de Turing `01#`. Faisons simple et séparons les variables en autant de ruban :

- un ruban `R-Q` pour stocker l'état courant `q` : On supposera que le curseur est toujours placé au début de l'état. On initialisera ce ruban en recopiant le premier élément de l'entrée $E$
- cinq rubans permettant de stocker la transition :
  - `R-T0` : un ruban contenant les éléments $E[5\cdot k]$ séparé par des `#`
  - `R-T1` : un ruban contenant les éléments $E[5\cdot k + 1]$ séparé par des `#`
  - `R-T2` : un ruban contenant les éléments $E[5\cdot k + 2]$ séparé par des `#`
  - `R-T3` : un ruban contenant les éléments $E[5\cdot k + 3]$ séparé par des `#`
  - `R-T4` : un ruban contenant les éléments $E[5\cdot k + 4]$ séparé par des `#`
- `R-S` : un ruban contenant le ruban de la machine simulée
- `R-I` : un dernier ruban pour les opérations internes de la MTU

Enfin, il faut adapter le pseudo-code de la MTU à notre machine. Ceci est aisé puisque :

- les différents paramètres sont des chaînes formées des caractères `0` et `1` séparées par 1 caractères `#` qui ne sont utilisé que comme séparateur
- dés que l'on rencontre la chaîne  `##`, on est en bout de ruban (la suite à gauche ou à droite sera uniquement composées de `#`)
- on peut bouger les curseurs de façon indépendante et donc avec des sous-programmes qui ne manipulent que certains rubans.

On obtient alors l'algorithme ci-après qui est une écriture de l’algorithme de la MTU sous une forme où chaque étape est facilement implémentable avec une machine de Turing `01#` :

1. Initialisation. Elle peut aisément être fait par une machine de Turing qui dispatche l'entrée sur les différents rubans
   1. Le ruban `R-Q` contient la chaîne `00000`, avec autant de `0` que la longueur du premier élément de $E$. Son curseur est placé sur le caractère non `#` le plus à gauche
   2. le ruban `R-T0` contient tous les éléments $E[5\cdot k]$, de $k=0$ jusqu'au premier élément $k_\max$ tel que $E[5\cdot k_\max] = \sharp$. Son curseur est placé sur le caractère non `#` le plus à gauche
   3. le ruban `R-T1` contient tous les éléments $E[5\cdot k + 1]$, de $k=0$ jusqu'au premier élément $k_\max$ tel que $E[5\cdot k_\max + 1] = \sharp$. Son curseur est placé sur le caractère non `#` le plus à gauche
   4. le ruban `R-T2` contient tous les éléments $E[5\cdot k + 2]$, de $k=0$ jusqu'au premier élément $k_\max$ tel que $E[5\cdot k_\max + 2] = \sharp$. Son curseur est placé sur le caractère non `#` le plus à gauche
   5. le ruban `R-T3` contient tous les éléments $E[5\cdot k + 3]$, de $k=0$ jusqu'au premier élément $k_\max$ tel que $E[5\cdot k_\max + 3] = \sharp$. Son curseur est placé sur le caractère non `#` le plus à gauche
   6. le ruban `R-T4` contient tous les éléments $E[5\cdot k + 4]$, de $k=0$ jusqu'au premier élément $k_\max$ tel que $E[5\cdot k_\max + 4] = \sharp$. Son curseur est placé sur le caractère non `#` le plus à gauche
   7. les rubans `R-S` et `R-I` sont initialement vides.
2. Trouver la transition courante :
   1. recopier le paramètre du ruban `R-Q` sur `R-I` se décaler d'un cran à droite sur `R-I` et se replacer au début du paramètre sur `R-Q`
   2. recopier le paramètre du ruban `R-T0` sur `R-I` se décaler sur la gauche sur `R-I` jusqu'à être au début du ruban (à gauche du curseur il y a deux caractères `#` à la suite) et se replacer au début du paramètre sur `R-T0`
   3. exécuter un programme qui rend `1` sur la machine si les deux paramètres du ruban `R-I` sont égaux et `0` sinon
   4. Si le résultat vaut `0` :
      1. effacer le ruban `R-I`
      2. décaler les rubans `R-T0` à `R-T4` d'un paramètre à droite
   5. Si le résultat vaut `1`` :
      1. si la valeur du ruban de `R-S` vaut la valeur sur le ruban `R-T1`, aller en 3.
      2. sinon décaler les rubans `R-T0` à `R-T4` d'un paramètre à droite et retour en 2.
3. Faire la transition courante sur `R-S`
   1. nouvel état : efface le ruban `R-Q` et écriture du paramètre de `R-T2` sur `R-Q`
   2. écriture du ruban : écriture de la case sous `R-T3` sur `R-I`
   3. déplacement du ruban : déplacement de `R-I` vers la droite si la case du ruban `R-T4` vaut `1` et déplacement vers la gauche sinon
4. Retour au début des paramètres pour les rubans `R-Q` et de `R-T0` à `R-T4` (à gauche de chaque curseur il y a deux caractères `#` à la suite)
5. retour en 2.

### Conclusion

Nous venons de faire un ordinateur avec une machine de Turing !

- les registres : état
- l'unité arithmétique : le ruban interne
- le code : la représentation de la transition sous une forme *compilée*, compréhensible par un ordinateur.
- la mémoire : le ruban de la machine à simuler

Le principe que nous venons d'expliciter en créant une MTU est exactement celui qui est utilisé en vrai avec vos ordinateurs.

{% note "**Théorème fondamental de l'algorithmie**" %}
On peut encoder toute machine de Turing $M$ par une chaîne $E$ composée de `0` et de `1`, de telle sorte que l'exécution de la machine de Turing universelle $\text{MTU}(E)$ simule l'exécution de $M$.

{% endnote %}

La machine de Turing universelle est donc [la machine qui les gouverne toutes](https://fr.wikipedia.org/wiki/Anneau_unique).

Attention cependant, On a l'impression qu'on a besoin de rien, que toutes les machines de Turing sont en faite une seule. Ce n'est pas exactement le cas car l'encodage cache la machine. C'est un petit peu comme dans la blague ci-dessous. Un numéro n'est drôle que parce qu'il code une blague !

```text
Une famille qui connaît toutes les blagues de la planète 
les a classées et numérotées. Ainsi, le seul numéro suffit 
à les faire rire.

Lors d' un repas le père s'exclame : "12" !
Tout le monde pouffe de rire.
La mère dit : "32" !
Et ils éclatent de rire.
Le petit sort alors : "104" !
Et personne ne rit.
Son frère lui dit alors : " Tu la racontes mal !"
```

Grâce à la machine de Turing universelle, démontrer qu'un langage est [Turing complet](https://fr.wikipedia.org/wiki/Turing-complet) c'est à dire qu'il permet de calculer tout ce qu'une machine de Turing peut calculer revient à montrer qu'on peut simuler une machine de Turing. Comme il est facile de simuler une MTU en pseudo-code (on l'a fait [juste avant](./#pseudo-code-MTU)){.interne} on en conclut :

{% note "**Proposition**" %}
Tout ce qui peut s'écrire avec une machine de Turing peut s'écrire avec un pseudo-code.
{% endnote %}

## Turing complet

Les deux parties précédentes ont permit de démontrer les deux implication du théorème suivant :

{% note "**théorème**" %}

[Pseudo-code]("../..//pseudo-code/"){.interne} et [machine de Turing](../définition){.interne} sont deux notions équivalentes.

{% endnote %}

Mais le pseudo-code n'est pas le seul système qui permet de simuler toutes les machines de Turing.

{% note "**définition**" %}
Un système est dit [Turing complet](./https://fr.wikipedia.org/wiki/Turing-complet) s'il permet de faire tout ce qu'une machine de Turing peut faire.
{% endnote %}

Une façon de montrer qu'un système est Turing complet est de faire ce qu'on a fait pour le pseudo--code, montrer qu'il peut simuler l'exécution d'une machine de Turing. De là il peut simuler l'exécution d'une machine de Turing Universelle et donc faire tout ce que peut faire une machine de Turing.

Cette preuve permet de montrer que les systèmes suivant sont Turing complet :

- un processeur
- la quasi-totalité des langages de programmation
- excel
- Factorio
- Minecraft
- ...

Ce qu'il faut retenir de tout ça, c'est qu'il est très facile d'être Turing Complet !

{% lien %}
L'exemple de système Turing complet le plus simple que je connaisse est l'automate uni-dimensionnel respectant la [règle 110](https://en.wikipedia.org/wiki/Rule_110).

Jetez-y un coup d'œil, c'est assez bluffant.
{% endlien %}

Bien qu'il soit très facile pour un système d'être Turing Complet, toute les tentatives de généralisation  se sont révéler vaines.
La notion de Machine de Turing semble capturer l'essence même de ce qu'est un algorithme.

## <span id="thèse-Church-Turing"></span>Thèse de Church-Turing

Une machine de Turing (et donc le pseudo-code) est a priori un cas particulier d'algorithme puisque l'on se limite à un nombre fixé d'instructions et à une construction rigide et normée de ceux ci. Mais toutes les tentatives de généralisation ont échoués : elle n'ont jamais permis de faire des algorithmes impossible à réaliser en pseudo-code.

{% lien %}
Si ces considérations vous intéressent, n'hésitez pas à jeter un coup d'œil à ce lien :
<https://plato.stanford.edu/entries/turing-machine/#ThesDefiAxioTheo>

C'est en Anglais, mais c'est très bien.
{% endlien %}

On pense donc (mais ce n'est pas démontré) que :

{% note "**Thèse de Church-Turing**" %}
Les notions d'algorithme et de pseudo-code sont équivalentes.

Tout algorithme peut être écrit en pseudo-code.
{% endnote %}

En bon informaticien, on considérera la thèse de Church-Turing vérifiée et :

- on écrira tous nos algorithmes en pseudo-code
- pseudo-code et algorithme seront considérés comme synonyme.

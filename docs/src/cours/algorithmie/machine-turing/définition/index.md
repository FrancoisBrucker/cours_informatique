---
layout: layout/post.njk 
title:  "Définition et premières manipulations"

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% note "**définition**" %}
Une ***machine de Turing*** est composée :

* d'un ***ruban*** (supposé infini) constitué de cases contiguës pouvant chacune contenir soit le caractère `0` soit le caractère `1`
* d'un ***curseur*** qui est positionné sur une case du ruban (on suppose que le ruban est infini à gauche et à droite du curseur)
* d'un ensemble fini $Q$ d'***états possibles***, contenant les états `START`{.language-}  et `STOP`{.language-}
* d'un ***état courant*** $q \in Q$
* d'une ***fonction de transition*** $\delta(q, r) = (\delta_e(q, r), \delta_c(q, r), \delta_d(q, r))$ dépendant de l'état $q$ de la machine et du caractère $r$ contenu dans la case du ruban pointée par le curseur. Cette fonction définie sur $Q \times \\{0, 1\\}$ permet de modifier :
  * l'état de la machine : $\delta_e : Q \times \\{0, 1\\} \mapsto Q$
  * le caractère de la case du ruban pointée par le curseur : $\delta_c : Q \times \\{0, 1\\} \mapsto \\{0, 1\\}$
  * la position du curseur : $\delta_d : Q \times \\{0, 1\\} \mapsto \\{\leftarrow, \rightarrow\\}$
{% endnote %}

Une machine c'est donc un **programme** (la fonction de transition) qui agit à partir de **données** (le ruban et l'état interne de la machine). Une machine de Turing n'a d'intérêt que si elle est **exécutée**  :

{% note "**définition**" %}
L'***exécution*** d'une machine de Turing se déroule comme suit :

1. initialisation :
   1. le ruban est constitué uniquement `0`
   2. l'état courant de la machine est `START`{.language-}
2. étape :
   1. on lit l'état courant  $q$ de la machine
   2. Si $q$ vaut `STOP`{.language-} on arrête l'exécution de la machine
   3. on lit le caractère $r$ dans la case du ruban pointée par le curseur
   4. on écrit le caractère $\delta_c(q, r)$ dans la case du ruban pointée par le curseur
   5. on déplace le curseur d'une case à droite ou à gauche selon la valeur de $\delta_d(q, r)$
   6. on change l'état courant de la machine en $\delta_e(q, r)$
   7. retour en 2.1
{% endnote %}

L'exécution d'une machine de Turing, n'est pas forcément finie. Elle ne s'arrête que si elle atteint l'état `STOP`{.language-}, ce qui peut ne jamais arriver.

Remarquez la minimalité du fonctionnement :

* on ne peut déplacer la tête de lecture que d'une case vers la gauche ou vers la droite (il est impossible d'écrire où l'on veut dans la mémoire comme on peut le faire avec un ordinateur classique)
* on ne peut écrire qu'un caractère à la fois (pas d'entier, de réel, rien que `0` ou `1`)
* pas de variables
* pas de boucle for ni de saut
* un unique test entre un état et une case du ruban

Et pourtant (nous le verrons), elle capte toutes les possibilités d'un algorithme.

## Exemples

### <span id="exemple-répétition"></span> Répétitions

Considérons la machine de Turing dont une fonction de transition partielle est la suivante :

* $\delta(\text{START}, 0) = (\text{UN}, 1, \rightarrow)$
* $\delta(\text{UN}, 0) = (\text{START}, 0, \rightarrow)$

{% exercice %}
Montrer que la fonction de transition partielle précédente est suffisante pour que l'exécution de la machine soit bien définie
{% endexercice %}
{% details "solution" %}
À l'initialisation le ruban est rempli de `0` et comme la machine ne va que à droite, le caractère lu sur le ruban ne peut être que `0`. Comme l'état initial est `START`{.language-}, la machine va osciller entre l'état `START`{.language-} et `UN`{.language-}.
{% enddetails %}
{% exercice %}
Montrer que l'exécution de cette machine de Turing ne va jamais s'arrêter
{% endexercice %}
{% details "solution" %}
La fonction de transition ne contient pas de changement d'état vers `STOP`{.language-}.
{% enddetails %}
{% exercice %}
Que fait cette machine ?
{% endexercice %}
{% details "solution" %}
À chaque étape la machine écrit `1` (respectivement `0`) si elle a précédemment écrit `0` (respectivement `1`) et se déplace à droite
{% enddetails %}

### <span id="exemple-oscillation"></span> Oscillation

Considérons la machine de Turing dont une fonction de transition partielle est la suivante :

* $\delta(\text{START}, 0) = (\text{L1}, 0, \leftarrow)$
* $\delta(\text{L1}, 0) = (\text{R0}, 1, \rightarrow)$
* $\delta(\text{R0}, 0) = (\text{R1}, 0, \rightarrow)$
* $\delta(\text{R0}, 1) = (\text{R0}, 1, \rightarrow)$
* $\delta(\text{R1}, 1) = (\text{R0}, 1, \rightarrow)$
* $\delta(\text{R1}, 0) = (\text{STOP}, 1, \leftarrow)$

{% exercice %}
Montrer que la fonction de transition partielle précédente est suffisante pour que l'exécution de la machine soit bien définie
{% endexercice %}
{% details "solution" %}
Les transitions à partir des états `R0`{.language-} et `R1`{.language-} sont définis pour `0` et `1`. Seul `L1`{.language-} n'est défini que pour `0`. Or la seule étape où la machine peut se trouver dans l'état `L1`{.language-} est la seconde étape (les autres transitions ne transitionnent jamais vers `L1`{.language-}), où il ne peut y avoir qu'un 0 sur la case du ruban pointée par le curseur.
{% enddetails %}
{% exercice %}
Montrer que l'exécution de cette machine de Turing va s'arrêter et donnez les caractères présents sur le ruban
{% endexercice %}
{% details "solution" %}
`···01010···`
{% enddetails %}
<span id="exemple-oscillation-infini"></span>
{% exercice %}
Que faudrait-il ajouter/modifier à la fonction de transition pour que la machine oscille infiniment ?
{% endexercice %}
{% details "solution" %}

* $\delta(\text{START} = (\text{L1}, 0, \leftarrow)$
* $\delta(\text{L1}, 0) = (\text{R0}, 1, \rightarrow)$
* $\delta(\text{L1}, 1) = (\text{L0}, 1, \leftarrow)$ (**Ajout**)
* $\delta(\text{R0}, 0) = (\text{R1}, 0, \rightarrow)$
* $\delta(\text{R0}, 1) = (\text{R0}, 1, \rightarrow)$
* $\delta(\text{R1}, 1) = (\text{R0}, 1, \rightarrow)$
* $\delta(\text{R1}, 0) = (\text{L0}, 1, \leftarrow)$ (**Modification**)
* $\delta(\text{L0}, 0) = (\text{L1}, 0, \leftarrow)$ (**Ajout**)
* $\delta(\text{L0}, 1) = (\text{L0}, 1, \leftarrow)$ (**Ajout**)

{% enddetails %}

## Visualisation

Voir une machine de Turing s'exécuter est très gratifiant, surtout lorsqu'on a passé du temps à la créer. Il existe de nombreux sites permettant de visualiser l'exécution d'une machine, nous allons utiliser celui-ci :

{% lien %}
<https://turingmachine.io/>
{% endlien %}

Il utilise une définition plus générale d'une machine de Turing (c'est celle - classique - de [Wikipedia](https://fr.wikipedia.org/wiki/Machine_de_Turing#D%C3%A9finition_formelle)) mais nous pouvons tout à fait utiliser notre définition.

Reprenons [le premier précédent](./#exemple-répétition){.interne} et écrivons le sous la forme utilisée par le site.

{% faire %}
Copiez/coller le code ci-dessous dans la fenêtre de texte de la page <https://turingmachine.io/> , puis cliquez sur le bouton `load machine`.

```text
blank: 0
start state: START
table:
  START:
    0: {
      write: 1,
      R: UN
    }
  UN:
    0: {
      write: 0,
      R: START
    }
  STOP:
```

Le *code* de la machine de Turing utilisé est expliqué au bas de la page du site.

{% endfaire %}

La machine est chargée :

![chargement exemple](./chargement-exemple.png)

On y voit :

* un diagramme représentant la fonction de transition (les état sont les sommets et les arcs les transitions)
* le ruban et son curseur

Grâce aux boutons `step` et `run` sous le ruban, vous pourrez exécuter une étape de la machine ou en continue.

{% faire %}
Exécutez plusieurs étapes de la Machine et vérifiez que les états sont bien représentez sur le diagramme au dessus de du ruban.
{% endfaire %}

Jouons un peu avec cette machine :

{% exercice %}
Modifiez le code précédant pour que la machine écrive indéfiniment `110` sur le ruban.
{% endexercice %}
{%details "solution" %}

```text
blank: 0
start state: START
table:
  START:
    0: {
      write: 1,
      R: UN
    }
  UN:
    0: {
      write: 1,
      R: DEUX
    }
  DEUX:
    0: {
      write: 0,
      R: START
    }
    
  STOP:
```

{% enddetails %}

{% exercice %}
Modifiez le code précédant pour que la machine commence par écrire `110` sur le ruban, puis revienne en arrière sans modifier le ruban et s'arrête lorsque le curseur est de nouveau sur la position de départ.

![répétition retour](./répétition-retour.gif)

{% endexercice %}
{%details "solution" %}

```text
blank: 0
start state: START
table:
  START:
    0: {
      write: 1,
      R: UN
    }
    1: {
      write: 1,
      L: STOP
    }

  UN:
    0: {
      write: 1,
      R: DEUX
    }
    
  DEUX:
    0: {
      write: 0,
      L: START
    }
    
  STOP:
```

{% enddetails %}

{% exercice %}
Écrivez le code de l'[oscillateur](./#exemple-oscillation){.interne} qui s'arrête.
{% endexercice %}
{%details "solution" %}

```text
blank: 0
start state: START
table:
  START:
    0: {
      write: 0,
      L: L1
    }
  L1:
    0: {
      write: 1,
      R: R0
    }
  R0:
    0: {
      write: 0,
      R: R1
    }
    1: {
      write: 1,
      R: R0
    }
  R1:
    1: {
      write: 1,
      R: R0
    }
    0: {
      write: 1,
      L: STOP
    }
  STOP:
```

{% enddetails %}
{% exercice %}
Écrivez le code de l'[oscillateur infini](./#exemple-oscillation-infini){.interne}.
{% endexercice %}
{%details "solution" %}

```
blank: 0
start state: START
table:
  START:
    0: {
      write: 0,
      L: L1
    }
  L1:
    0: {
      write: 1,
      R: R0
    }
    1: {
      write: 1,
      L: L0
    }
  R0:
    0: {
      write: 0,
      R: R1
    }
    1: {
      write: 1,
      R: R0
    }
  R1:
    1: {
      write: 1,
      R: R0
    }
    0: {
      write: 1,
      L: L0
    }
  L0:
    0: {
      write: 0,
      L: L1
    }
    1: {
      write: 1,
      L: L0
    }
    
  STOP:
```

{% enddetails %}

## Sortie et Entrée d'une machine

### Sortie

Mais si la machine s'arrête, le ruban constitue sa ***sortie***. Comme la machine a effectuée un nombre fini d'étape avant de s'arrêter, on peut uniquement considérer une portion finie de celui-ci :

{% note "définition" %}
La ***sortie*** d'une machine de Turing est constituée la partie finie du ruban entourant le curseur allant de :

* la case contenant le caractère `1` le plus à gauche du curseur ou la case contenant le curseur s'il n'y a que des `0` à gauche du curseur
* à la case contenant le caractère `1` le plus à droite la case contenant le curseur s'il n'y a que des `0` à droite du curseur
{% endnote %}

Par exemple si le ruban est :

```
···0110001101010000···
        ^
```

la sortie sera : `11000110101`

Et si le ruban vaut :

```
···0110001101010000···
                ^
```

La sortie sera : `100`

Cette définition de sortie n'est pas totalement satisfaisante puisqu'elle est vaut soit `0` soit elle aura un `1` au début ou à la fin. On verra [plus tard](./#turing-01#){.interne} comment régler ce (petit) problème.

### Entrée

Avant de définir l'***entrée*** d'une machine de Turing, commençons par une propriété anodine mais avec de grosses conséquences :

<span id="addition-turing"></span>
{% note "**définition**" %}
Si $M$ et $M'$ sont deux machines de Turing, définit la machine de Turing $M+M'$ en suivant la procédure suivante :

* on s'assure que les états de $M$ et les états de $M'$ (à part `START`{.language-} et `STOP`{.language-}) soient différents
* on renomme l'état `STOP`{.language-} de la machine $M$ en `START'`{.language-}
* on renomme l'état `START`{.language-} de la machine M' en `START'`{.language-}
{% endnote %}

La définition ci-dessus nous permet d'exécuter à la suite deux machine de Turing, l'état de fin de la première machine devenant l'état de départ de la suivante.

{% info %}
Notez que l'addition de Machine de Turing est bien commutative et associative.
{% endinfo %}

Cette addition nous permet d'exécuter une machine $M$ avec autre chose que des `0` sur le ruban en exécutant la machine $M_\text{Init} + M$, avec $M_\text{Init}$ une machine qui *prépare* le ruban.

Par exemple, supposons que l'on veuille exécuter la machine [oscillateur](./#exemple-oscillation){.interne} avec la chaîne `0101` sur le ruban on peut commencer par utiliser la machine de fonction de transition :

* $\delta(\text{START}, 0) = (UN, 1, \rightarrow)$
* $\delta(UN, 0) = (DEUX, 0, \rightarrow)$
* $\delta(DEUX, 0) = (TROIS, 1, \leftarrow)$
* $\delta(TROIS, 0) = (QUATRE, 0, \leftarrow)$
* $\delta(QUATRE, 1) = (STOP, 1, \leftarrow)$

Qui laisse le ruban avec les données `···01010···` et le curseur sur le `0` le plus à gauche.

{% exercice %}
Vérifiez que la machine ci-dessus fait fait ce-que l'on pense et vérifiez le en la codant sur <https://turingmachine.io/>
{% endexercice %}
{% details "solution" %}

```text
blank: 0
start state: START
table:
  START:
    0: {
      write: 1,
      R: UN
    }
  UN:
    0: {
      write: 0,
      R: DEUX
    }
  DEUX:
    0: {
      write: 1,
      L: TROIS
    }
  TROIS:
    0: {
      write: 0,
      L: QUATRE
    }
  QUATRE:
    1: {
      write: 1,
      L: STOP
    }

  STOP:
```

{% enddetails %}

On exécute ensuite, initialisation notre [oscillateur](./#exemple-oscillation){.interne}.

Cette succession de l'exécution de deux machines est une machine dont
la fonction de transition complète de cette nouvelle machine serait, en respectant les règle de l'addition :

* $\delta(\text{START}, 0) = (UN, 1, \rightarrow)$
* $\delta(UN, 0) = (DEUX, 0, \rightarrow)$
* $\delta(DEUX, 0) = (TROIS, 1, \leftarrow)$
* $\delta(TROIS, 0) = (QUATRE, 0, \leftarrow)$
* $\delta(QUATRE, 1) = (START', 1, \leftarrow)$
* $\delta(\text{START'}, 0) = (\text{L1}, 0, \leftarrow)$
* $\delta(\text{L1}, 0) = (\text{R0}, 1, \rightarrow)$
* $\delta(\text{R0}, 0) = (\text{R1}, 0, \rightarrow)$
* $\delta(\text{R0}, 1) = (\text{R0}, 1, \rightarrow)$
* $\delta(\text{R1}, 1) = (\text{R0}, 1, \rightarrow)$
* $\delta(\text{R1}, 0) = (\text{STOP}, 1, \leftarrow)$

{% exercice %}
Combinez le code de la machine qui initialise et l'oscillateur pour tester le résultat sur <https://turingmachine.io/>
{% endexercice %}
{% details "solution" %}

```text
blank: 0
start state: START
table:
  START:
    0: {
      write: 1,
      R: UN
    }
  UN:
    0: {
      write: 0,
      R: DEUX
    }
  DEUX:
    0: {
      write: 1,
      L: TROIS
    }
  TROIS:
    0: {
      write: 0,
      L: QUATRE
    }
  QUATRE:
    1: {
      write: 1,
      L: START'
    }
  START':
    0: {
      write: 0,
      L: L1
    }
  L1:
    0: {
      write: 1,
      R: R0
    }
  R0:
    0: {
      write: 0,
      R: R1
    }
    1: {
      write: 1,
      R: R0
    }
  R1:
    1: {
      write: 1,
      R: R0
    }
    0: {
      write: 1,
      L: STOP
    }
  STOP:
```

{% enddetails %}

Ce cas étant très courant, plutôt que de concaténer une machine qui initialise le ruban à la machine principale, on donne la possibilité de donner une entrée à l'exécution d'une machine :

{% note "définition" %}
Le ***paramètre d'entrée*** de l'exécution d'une machine de Turing $M$ est une suite **finie** $E$ (pouvant être vide) de caractères `0` et `1`.

Lors de l'initialisation de l'exécution de la machine on rajoute deux étapes :

1. inscription de la chaîne `E` sur le ruban
2. positionnement du curseur sur la case contenant le premier élément de la chaîne.

L'exécution de la machine $M$ avec l'entrée $E$ s'écrit : $M(E)$
{% endnote %}

Remarquez bien que :

* l'ajout d'un paramètre d'entrée n'est qu'une facilité d'écriture, cela ne change rien au modèle initial de la machine de Turing.
* l'entrée est **finie** puisqu'elle résulte de l'exécution d'une machine. Il est donc impossible d'initialiser un ruban avec un nombre infini de `1`.

{% exercice %}
En utilisant le code <https://turingmachine.io/> de l'[oscillateur](./#exemple-oscillation){.interne}, ajoutez la chaîne `0101` comme paramètre d'entrée avec le mot clé `input:`{.language-}
{% endexercice %}
{% details "solution" %}

```text
blank: 0
start state: START
input: '0101'
table:
  START:
    0: {
      write: 0,
      L: L1
    }
  L1:
    0: {
      write: 1,
      R: R0
    }
  R0:
    0: {
      write: 0,
      R: R1
    }
    1: {
      write: 1,
      R: R0
    }
  R1:
    1: {
      write: 1,
      R: R0
    }
    0: {
      write: 1,
      L: STOP
    }
  STOP:
```

{% enddetails %}

Attention cependant, une machine peut s'arrêter pour certaines entrées et pas d'autres.

## <span id="composition-machine"></span> Composition de machines

Nous allons montrer comment combiner plusieurs machines entres-elles afin de réaliser des machines de plus en plus complexe. Ce processus d'agrégation montre que le modèle très simple de la machine de Turing permet en fait de fait tout ce que l'on veut, si l'on sépare bien le problème à résoudre en élément facile à écrire.

Nous allons expliciter les deux principes fondamentaux en algorithmie :

* l'exécution séquentielle de plusieurs machines/instruction
* l'exécution conditionnelle d'une machine/instruction ou d'une autre

### Succession de Machines

Nous formalisons ici l'[addition](./#addition-turing) vue dans la partie entrée.

<span id="exécution-séquentielle"></span>
{% note "**définition**" %}
Soient $M_i$, $1\leq i \leq n$, $n$ machines de Turing de fonctions de transition respectives $\delta^i(q, r) = (\delta^i_e(q, r), \delta^i_c(q, r), \delta^i_d(q, r))$.

L'***exécution séquentielle*** des $M_i$ machines est alors la machine définie par la fonction de transition $\delta$ telle que :

* Initialisation :
  * $\delta(\text{START}, r) = (\text{START}', r, \rightarrow)$
  * $\delta(\text{START}', r) = ((1, \text{START}), r, \leftarrow)$
* Re-labellisation des états des machines :
  * Pour tout état $q$ de la machine $M_i$ :  $\delta((i, q), r) = ((i+1, \delta^i_e(q, r)), \delta^i_c(q, r),\delta^i_d(q, r))$
* Exécution successive des $n$ machines :
  * $\delta((i, \text{STOP}), r) = ((i, \text{STOP}'), r,\rightarrow)$
  * $\delta((i+1, \text{STOP}'), r) = ((i+1, \text{START}), r,\leftarrow)$

{% endnote %}
{% info %}
On a ajouté une machine qui fait un aller-retour d'une case entre chaque exécution d'une machine pour garantir que la case du début de la machine $i+1$ est bien la même que la case qui a déclenchée la transition de fin de la machine $i$. Cela est cohérent avec la définition de $M+M'$ et rend indépendant les instructions $i$ et $i+1$.
{% endinfo %}

On pourra écrire l'exécution séquentielle des machines $M_i$ comme l'*algorithme* :

* $1$: $M_1$
* ...
* $i$: $M_i$
* ...
* $n$: $M_n$

Chaque ligne correspond à une *instruction* indépendante,  l'interaction entre les machines se faisant grâce au ruban.

### Exécution conditionnelle de machines

Pour l'instant nos compositions sont des successions indépendantes de machines. Nous allons utiliser les fonctions de transition pour pouvoir exécuter conditionnellement une machine ou une autre.

Dans la partie précédente, nous avons exécuté des machines de façons successives en utilisant des "*labels*" entiers : la machine de label $i$ s'exécutant juste avant la machine de Label $i+1$. Explicitons cela :

{% note "**définition**" %}
Un ***programme*** est une machine de Turing définie par une succession de lignes : **LABEL: MACHINE**, où chaque label est unique.

Un programme est toujours composé d'un label nommé **MAIN**.

Si on note $\delta^M(q, r) = (\delta^M_e(q, r), \delta^M_c(q, r),\delta^M_d(q, r))$ la fonction de transition d'une machine de uring $M$, la fonction de transition $\delta$ associée à un programme est définie pour chaque ligne **LABEL: M** telle que :

$$
\delta((LABEL, q)) = ((LABEL, \delta^M_e(q, r)), \delta^M_c(q, r),\delta^M_d(q, r))
$$

Le label spécial **MAIN** constitue le départ du programme. Pour démarrer l'exécution du programme, on ajoute à la fonction de transition :

* $\delta(START, r) = (\text{START}'), r,\rightarrow)$
* $\delta(\text{START}', r) = ((MAIN, \text{START}), r,\leftarrow)$

{% endnote %}

Un programme démarre toujours en exécutant la machine de label **START**. Pour passer d'un label à un autre, on peut utiliser la machine spéciale nommée **ALLER label**.

{% note "**définition**" %}
Dans un programme, La machine ***ALLER LABEL*** est définie par la fonction de transition :

* $\delta(START, r) = (\text{START}'), r,\rightarrow)$
* $\delta(\text{START}', r) = ((\text{LABEL}, \text{START}), r,\leftarrow)$

{% endnote %}

Nous n'avons pour l'instant que redéfini de façon plus générale l'[exécution séquentielle](./#exécution-séquentielle) de machines.

{% exercice %}
Utilisez les labels et la machine **ALLER label**, pour redéfinir l'[exécution séquentielle](./#exécution-séquentielle) de machines.
{% endexercice %}
{% details "solution" %}
> TBD
{% enddetails %}

Pour aller plus loin, il nous faut formaliser une machine permettant l'exécution conditionnelle de machines.

{% note "**définition**" %}
Dans un programme, La machine ***SI $x$ LABEL1 SINON LABEL2*** avec $x \in \\{0, 1\\}$ est définie par la fonction de transition :

* $\delta(START, 0) = ((\text{START}', 0), 0,\rightarrow)$
* $\delta(START, 1) = ((\text{START}', 1), 1,\rightarrow)$
* $\delta((\text{START}', 0), r) = ((\text{LABEL1}, \text{START}), r,\leftarrow)$
* $\delta((\text{START}', 1), r) = (((\text{LABEL2}, \text{START}), r,\leftarrow)$

{% endnote %}

### Procédure

Souvent lorsque l'on crée un programme avec une machine de Turing on se trouve confronté à des machines qui doivent être exécutées dans des contextes différents. Un peu comme un appel de fonction dans du pseudo-code classique.

Pour permettre d'écrire cela de façon condensée on peut définir des labels spéciaux dans nos programmes :

{% note "**définition**" %}

Dans un programme, on permet de définir un label générique **LABEL($p_1, \dots, p_k$): M** où les $p_i$ peuvent prendre toutes les valeurs d'un ensemble $P_i$ **fini**. On peut utiliser les noms $p_i$ ($1\leq i \leq k$) dans la définition de la machine M.

On génère pour cette ligne les transitions :

$$
\delta((\text{LABEL}(p_1, \dots, p_k), q)) = ((\text{LABEL}(p_1, \dots, p_k), \delta^M_e(q, r)), \delta^M_c(q, r),\delta^M_d(q, r))
$$

Pour tous les $(p_1, \dots, p_k) \in P_1 \times \dots \times P_k$
{% endnote %}
{% attention %}
Attention, ce ne sont pas vraiment des fonctions car on ne fait que créer une fonction de transition pour tous les cas possible. Il est donc nécessaire que le nombre de possibilité soit fini.
{% endattention %}

### Exemples de composition

#### Doublement de bâtons

Utilisons cette formalisation pour réaliser une machine un peu plus complexe que ce que nous avons fait jusqu'à présent :

> Nous allons créer une machine de Turing qui prend en entrée un suite finie de $k$ `1` ($k$ *bâtons*) et rend comme sortie une suite de $2k$ `1` ($2k$ *bâtons*).

Cette machine fait l'opération *fois 2* si l'on encode les entiers positifs par un [système unaire](https://fr.wikipedia.org/wiki/Syst%C3%A8me_unaire).

Pour cela, nous allons utiliser le fait que l'exécution successive de deux machines est également une machine pour décomposer le problème en plusieurs machines élémentaires.

L'idée est de fabriquer la sortie à droite de l'entrée en supprimant itérativement un bâton à l'entrée et d'en ajouter 2 à la sortie. Lorsque l'on aura supprimé tous les bâtons de l'entrée, il ne restera que la sortie et la machine s'arrêtera :

![doublement de bâtons](./turing_double_batons.gif)

Créons cette procédure en combinant des étapes élémentaires (ie pouvant être facilement crées avec une machine de Turing) :

1. Si l'entrée est vide arrêter le programme, sinon écrire un 0 et aller au début de la sortie
2. aller à la fin de la sortie et écrire `11` sur le ruban
3. revenir à la fin de l'entrée
4. revenir au début de l'entrée et retour en 1.

Ce qui donne avec une entrée l'algorithme suivant :

```
entrée      : 011100000000
               ^
fin étape 1 : 001100000000
                   ^ 
fin étape 2 : 001101100000
                     ^ 
fin étape 3 : 001101100000
                 ^ 
fin étape 4 : 001101100000
                ^ 
fin étape 1 : 000101100000
                   ^ 
fin étape 2 : 000101111000
                       ^ 
fin étape 3 : 000101111000
                 ^ 
fin étape 4 : 000101111000
                 ^ 
fin étape 1 : 000001111000
                   ^ 
fin étape 2 : 000001111110
                         ^ 
fin étape 3 : 000001111110
                 ^ 
fin étape 4 : 000001111110
                  ^ 
fin étape 1 : 000001111110
                   ^ 
```

Pour conclure, il nous reste à montrer que notre algorithme peut s'écrire sous la forme d'une machine de Turing.

{% exercice %}
Montrez que chacune des quatre étapes peut être simulées par une machine de Turing
{% endexercice %}
{% details "solution" %}
> TBD
{% enddetails %}
{% exercice %}
En conclure qu'il existe une machine de Turing permettant de faire le doublement de bâton et donnez en la fonction de transition.
{% endexercice %}
{% details "solution" %}
La machine $M = M1 + M2 + M3 + M4$ est presque la solution. Il faut juste s'assurer que l'on stoppe la machine si on lit `0` dans l'état start : \delta^M(\text{START}, 0) = (\text{STOP}, 0, \rightarrow)$, ce qui n'est plus le cas après addition.

{% enddetails %}
{% exercice %}
Combinez les quatres machine en une seule et visualisez le résultat.
{% endexercice %}
{% details "solution" %}

```
blank: 0
start state: START
input: '111'
table:
  START:
    0: {
      write: 0,
      R: STOP
    }
    1: {
      write: 0,
      R: RETOUR
    }
  RETOUR:
    1: {
      write: 1,
      R: RETOUR
    }
    0: {
      write: 0,
      R: START'
    }
  START':
    0: {
      write: 1,
      R: ÉCRIT
    }
    1: {
      write: 1,
      R: START'
    }      
  ÉCRIT:
    0: {
      write: 1,
      L: START''
    }
  START'':
    1: {
      write: 1,
      L: START''
    }
    0: {
      write: 0,
      L: START'''
    }
  START''':
    1: {
      write: 1,
      L: START'''
    }
    0: {
      write: 0,
      R: START
    }
  STOP:
```

{% enddetails %}

#### Écrire toutes les k cases

> TBD : à partir d'une machine $M$,  saut de 1 puis de 2 puis 3 et on recommence

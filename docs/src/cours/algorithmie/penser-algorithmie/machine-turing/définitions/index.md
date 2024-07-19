---
layout: layout/post.njk
title: "Définitions"

eleventyNavigation:
  order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Une machine de Turing est une structure minimaliste permettant d'être exécutée pour réaliser son programme. Commençons par définir sa structure :

{% note "**définition**" %}
Une **_machine de Turing_** est composée :

- d'un **_ruban_** (supposé infini) constitué de cases contiguës pouvant chacune contenir soit le caractère `0` soit le caractère `1`
- d'un **_curseur_** qui est positionné sur une case du ruban (on suppose que le ruban est infini à gauche et à droite du curseur)
- d'un ensemble fini $Q$ d'**_états possibles_**, contenant les deux états :
  - l'**_état initial_** noté `START`{.language-}
  - l'**_état d'acceptation_**, noté `STOP`{.language-}
- d'un **_état courant_** $q \in Q$
- d'une **_fonction de transition_** $\delta(q, r) = (\delta_e(q, r), \delta_c(q, r), \delta_d(q, r))$ dépendant de l'état $q$ de la machine et du caractère $r$ contenu dans la case du ruban pointée par le curseur. Cette fonction définie sur $Q \times \\{0, 1\\}$ permet de modifier :
  - l'état de la machine : $\delta_e : Q \times \\{0, 1\\} \mapsto Q$
  - le caractère de la case du ruban pointée par le curseur : $\delta_c : Q \times \\{0, 1\\} \mapsto \\{0, 1\\}$
  - la position du curseur : $\delta_d : Q \times \\{0, 1\\} \mapsto \\{\leftarrow, \rightarrow\\}$
    {% endnote %}

Une machine c'est donc un **programme** (la fonction de transition) qui agit à partir de **données** (le ruban et l'état interne de la machine). Une machine de Turing n'a d'intérêt que si elle est **exécutée** :

{% note "**définition**" %}
L'**_exécution_** d'une machine de Turing se déroule comme suit :

1. initialisation :
   1. le ruban est constitué uniquement `0`
   2. l'état courant de la machine est l'état initial `START`{.language-}
2. étape :
   1. on lit l'état courant $q$ de la machine
   2. Si $q$ vaut l'état d'acceptation `STOP`{.language-} on arrête l'exécution de la machine
   3. on lit le caractère $r$ dans la case du ruban pointée par le curseur
   4. on écrit le caractère $\delta_c(q, r)$ dans la case du ruban pointée par le curseur
   5. on déplace le curseur d'une case à droite ou à gauche selon la valeur de $\delta_d(q, r)$ (à gauche si $\leftarrow$, à droite si $\rightarrow$)
   6. on change l'état courant de la machine en $\delta_e(q, r)$
   7. retour en 2.1
      {% endnote %}

L'exécution d'une machine de Turing ne s'arrête pas forcément. Elle ne le fait que si elle atteint l'état `STOP`{.language-}, ce qui peut ne jamais arriver.

Remarquez la minimalité du fonctionnement :

- on ne peut déplacer la tête de lecture que d'une case vers la gauche ou vers la droite (il est impossible d'écrire où l'on veut dans la mémoire comme on peut le faire avec un ordinateur classique)
- on ne peut écrire qu'un caractère à la fois (pas d'entier, de réel, rien que `0` ou `1`)
- pas de variables
- pas de boucle `while`{.language-} ni de saut
- un unique test entre un état et une case du ruban

Et pourtant (nous le verrons), elle capte toutes les possibilités d'un algorithme.

## Exemples

Rien de tel que d'exécuter quelques machines pour mieux comprendre le fonctionnement général.

### <span id="exemple-répétition"></span> Répétitions

Considérons la machine de Turing dont une fonction de transition partielle est la suivante :

- $\delta(\text{START}, 0) = (\text{UN}, 1, \rightarrow)$
- $\delta(\text{UN}, 0) = (\text{START}, 0, \rightarrow)$

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

Voir une machine de Turing s'exécuter est très gratifiant, surtout lorsqu'on a passé du temps à la créer. Il existe de nombreux sites permettant de visualiser l'exécution d'une machine, nous allons utiliser celui-ci :

{% lien %}
<https://turingmachine.io/>
{% endlien %}

Il utilise une définition plus générale d'une machine de Turing (c'est celle - classique - de [Wikipedia](https://fr.wikipedia.org/wiki/Machine_de_Turing#D%C3%A9finition_formelle)) mais nous pouvons tout à fait utiliser notre définition.

Reprenons notre exemple et vérifions que nous avons bien compris son fonctionnement.

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

Le _code_ de la machine de Turing utilisé est expliqué au bas de la page du site.

{% endfaire %}

La machine est chargée :

![chargement exemple](./chargement-exemple.png)

On y voit :

- un diagramme représentant la fonction de transition (les état sont les sommets et les arcs les transitions)
- le ruban et son curseur

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

### <span id="exemple-oscillation"></span> Oscillation

Considérons la machine de Turing dont une fonction de transition partielle est la suivante :

- $\delta(\text{START}, 0) = (\text{L1}, 0, \leftarrow)$
- $\delta(\text{L1}, 0) = (\text{R0}, 1, \rightarrow)$
- $\delta(\text{R0}, 0) = (\text{R1}, 0, \rightarrow)$
- $\delta(\text{R0}, 1) = (\text{R0}, 1, \rightarrow)$
- $\delta(\text{R1}, 1) = (\text{R0}, 1, \rightarrow)$
- $\delta(\text{R1}, 0) = (\text{STOP}, 1, \leftarrow)$

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
{% exercice %}
Écrivez le code de l'oscillateur.
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

On va maintenant faire osciller l'oscillateur infiniment.

<span id="exemple-oscillation-infini"></span>
{% exercice %}
Que faudrait-il ajouter/modifier à la fonction de transition pour que la machine oscille infiniment ?
{% endexercice %}
{% details "solution" %}

- $\delta(\text{START} = (\text{L1}, 0, \leftarrow)$
- $\delta(\text{L1}, 0) = (\text{R0}, 1, \rightarrow)$
- $\delta(\text{L1}, 1) = (\text{L0}, 1, \leftarrow)$ (**Ajout**)
- $\delta(\text{R0}, 0) = (\text{R1}, 0, \rightarrow)$
- $\delta(\text{R0}, 1) = (\text{R0}, 1, \rightarrow)$
- $\delta(\text{R1}, 1) = (\text{R0}, 1, \rightarrow)$
- $\delta(\text{R1}, 0) = (\text{L0}, 1, \leftarrow)$ (**Modification**)
- $\delta(\text{L0}, 0) = (\text{L1}, 0, \leftarrow)$ (**Ajout**)
- $\delta(\text{L0}, 1) = (\text{L0}, 1, \leftarrow)$ (**Ajout**)

{% enddetails %}

{% exercice %}
Écrivez le code de l'oscillateur infini.
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

Mais si la machine s'arrête, le ruban constitue sa **_sortie_**. Comme la machine a effectuée un nombre fini d'étape avant de s'arrêter, on peut uniquement considérer une portion finie de celui-ci :

{% note "définition" %}
La **_sortie_** d'une machine de Turing est constituée la partie finie du ruban entourant le curseur allant de :

- la case contenant le caractère `1` le plus à gauche du curseur ou la case contenant le curseur s'il n'y a que des `0` à gauche du curseur
- à la case contenant le caractère `1` le plus à droite la case contenant le curseur s'il n'y a que des `0` à droite du curseur
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

La sortie sera : `1100011010100`

Cette définition de sortie n'est pas totalement satisfaisante puisqu'elle est vaut soit `0` soit elle aura un `1` au début ou à la fin. On peut régler ce problème en entourant toujours le ruban d'un `1` à gauche et d'un `1` à droite. Les sorties seront alors ainsi toutes les suites commençant et finissant pas un `1` ce qui n'est pas gênant il suffit de les supprimer a posteriori.

### Entrée

Avant de définir l'**_entrée_** d'une machine de Turing, commençons par une propriété anodine mais avec de grosses conséquences :

<span id="addition-turing"></span>
{% note "**définition**" %}
Si $M$ et $M'$ sont deux machines de Turing, on définit la machine de Turing $M+M'$ en suivant la procédure suivante :

- on s'assure que les états de $M$ et les états de $M'$ (à part `START`{.language-} et `STOP`{.language-}) soient différents
- on renomme l'état `STOP`{.language-} de la machine $M$ en `START'`{.language-}
- on renomme l'état `START`{.language-} de la machine M' en `START'`{.language-}
  {% endnote %}

La définition ci-dessus nous permet d'exécuter à la suite deux machine de Turing, l'état de fin de la première machine devenant l'état de départ de la suivante.

{% info %}
Notez que l'addition de Machine de Turing n'est pas commutative mais est associative.
{% endinfo %}

Cette addition nous permet d'exécuter une machine $M$ avec autre chose que des `0` sur le ruban en exécutant la machine $M_\text{Init} + M$, avec $M_\text{Init}$ une machine qui _prépare_ le ruban.

Par exemple, supposons que l'on veuille exécuter la machine [oscillateur](./#exemple-oscillation){.interne} avec la chaîne `0101` sur le ruban on peut commencer par utiliser la machine de fonction de transition :

- $\delta(\text{START}, 0) = (UN, 1, \rightarrow)$
- $\delta(UN, 0) = (DEUX, 0, \rightarrow)$
- $\delta(DEUX, 0) = (TROIS, 1, \leftarrow)$
- $\delta(TROIS, 0) = (QUATRE, 0, \leftarrow)$
- $\delta(QUATRE, 1) = (STOP, 1, \leftarrow)$

Qui laisse le ruban avec les données `···01010···` et le curseur sur le `0` le plus à gauche.

{% exercice %}
Codez la machine ci-dessus sur sur <https://turingmachine.io/> et vérifiez son fonctionnement.
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

- $\delta(\text{START}, 0) = (UN, 1, \rightarrow)$
- $\delta(UN, 0) = (DEUX, 0, \rightarrow)$
- $\delta(DEUX, 0) = (TROIS, 1, \leftarrow)$
- $\delta(TROIS, 0) = (QUATRE, 0, \leftarrow)$
- $\delta(QUATRE, 1) = (START', 1, \leftarrow)$
- $\delta(\text{START'}, 0) = (\text{L1}, 0, \leftarrow)$
- $\delta(\text{L1}, 0) = (\text{R0}, 1, \rightarrow)$
- $\delta(\text{R0}, 0) = (\text{R1}, 0, \rightarrow)$
- $\delta(\text{R0}, 1) = (\text{R0}, 1, \rightarrow)$
- $\delta(\text{R1}, 1) = (\text{R0}, 1, \rightarrow)$
- $\delta(\text{R1}, 0) = (\text{STOP}, 1, \leftarrow)$

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
Le **_paramètre d'entrée_** de l'exécution d'une machine de Turing $M$ est une suite **finie** $E$ (pouvant être vide) de caractères `0` et `1`.

Lors de l'initialisation de l'exécution de la machine on rajoute deux étapes :

1. inscription de la chaîne `E` sur le ruban
2. positionnement du curseur sur la case contenant le premier élément de la chaîne.

L'exécution de la machine $M$ avec l'entrée $E$ s'écrit : $M(E)$
{% endnote %}

Remarquez bien que :

- l'ajout d'un paramètre d'entrée n'est qu'une facilité d'écriture, cela ne change rien au modèle initial de la machine de Turing.
- l'entrée est **finie** puisqu'elle résulte de l'exécution d'une machine. Il est donc impossible d'initialiser un ruban avec un nombre infini de `1`.

{% exercice %}
En utilisant le code <https://turingmachine.io/> de l'[oscillateur infini](./#exemple-oscillation-infini){.interne}, ajoutez la chaîne `01110111` comme paramètre d'entrée avec le mot clé `input:`{.language-}
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

Attention cependant, une machine peut s'arrêter pour certaines entrées et pas d'autres. On défini alors :

{% note "définition" %}

Un machine de Turing $M$ **_accepte_** la chaîne de caractères $E\in \\{0, 1\\}^\star$ (qui peut être vide) si l'exécution de $M(E)$ s'arrête. Par abus de notation, on associera alors $M(E)$ à sa sortie.

Le **_langage_** de $M$ est l'ensemble de toutes les chaînes de caractères $E\in \\{0, 1\\}^\star$ qu'elle accepte.
{% endnote %}

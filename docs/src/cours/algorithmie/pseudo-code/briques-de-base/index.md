---
layout: layout/post.njk
title: Briques de base

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le pseudo-code est constitué d'instructions dont le but est soit de manipuler des objets (création, affectation ou lecture) ou de contrôler le flux d'instructions (test et boucles).

{% attention %}
Vous trouverez autant de type de pseud-code différents que d'informaticiens. Je vous donne ici _"mon"_ pseudo-code. Son but est d'être assez explicite pour décrire sans ambiguïté les algorithmes de ce cours. Ne soyez donc pas étonné si en lisant d'autres pseudo-codes ils ne suivent pas mes notations : ayez l'esprit ouvert.
{% endattention %}

Le but d'un pseudo-code est d'être lu et compris par un humain. Il se doit d'être sans ambiguïté sans être lourd.

## Commentaires

Comme en python, on considérera que tout ce qui suit le caractère `#`{.language-} est considéré comme un commentaire dont le but est d'éclairer le lecteur.

{% algorithme %}
#pseudocode-list(line-numbering: none)[

- #text(stroke: green)[\# un commentaire]
  ]
  {% endalgorithme %}

## Objets et opérations

Commençons par décrire les objets que l'on peut manipuler en pseudo-code et les moyens d'y accéder.

### Objets

#### <span id="objets-basiques"></span> Objets basiques

Les objets que nous aurons directement à notre disposition sans avoir besoin de les définir sont appelés **_objets basiques_** et correspondent aux cinq **_types_** suivant :

- le type `booléen`{.language-} qui contient deux objets : `vrai`{.language-} et `faux`{.language-}
- le type `bit`{.language-} qui contient les 2 objets : `0`{.language-} et `1`{.language-}
- le type `entier`{.language-} qui contient tous les entiers relatifs
- le type `réel`{.language-} qui contient un ensemble dénombrable d'approximation de réels
- le type `caractère`{.language-} qui contient l'ensemble des glyphes UNICODE : `"a"`{.language-}, `"b"`{.language-}, ...

#### Le vide

En algorithmie on a également coutume de se doter d'un élément vide `∅`{.language-} (nommé `None`{.language-} en python, `null`{.language-} en javascript ou encore `void`{.language-} en C) qui peut être à la fois considéré comme un type ou un objet :

- **le type vide** `∅`{.language-} ne contient aucun objet. On l'utilise pour des fonctions ne rendant aucun objet par exemple
- **l'objet vide** `∅`{.language-} est de tous les types (le `∅`{.language-} entier, bit, ...). Utilisé pour simuler un soucis ou un cas particulier : une fonction division pouvant rendre soit un réel soit le vide si on divise par 0 par exemple.

#### Autres types

Tous les autres types d'objets que l'on peut imaginer seront des compositions de ces 5 types d'objets (un point en 3D est constitué de 3 réels, une chaîne de caractères est un tableau de caractères, etc).

#### Taille et stockage des objets

Notez que tous les objets basiques à part les entiers sont de taille fixe :

- un booléen sur 1bit
- un caractère 32bits si on utilise [les caractères Unicode](https://fr.wikipedia.org/wiki/Unicode)
- un réel sur 64 bits si on utilise [la norme IEEE 754 double précision](https://fr.wikipedia.org/wiki/IEEE_754)

On peut sans perte de généralité se restreindre aux entiers entre 0 et $2^{64}$, et c'est d'ailleurs ce que beaucoup de langages de programmation font, puisque qu'un entier quelconque peut être représenté en base $2$ et découpé en paquets de 64 bits. C'est ce que font les languages d programmation comme python où un entier, qui n'est pas borné par nature, est composé d'un tableau d'entiers codés sur 64bits. Ceci est cependant transparent pour l'utilisateur (et c'est tant mieux).

{% attention "**À retenir**" %}
On considérera toujours qu'un objet basique est de taille connue et donnée au début du programme.
{% endattention %}

Les objets que l'on manipule doivent pouvoir être conservés pour que l'on puisse les réutiliser tout au long du programme. Cet espace espace de stockage, que l'on nomme **_une mémoire_**, est identifié d'un point de vue algorithmique, à une gigantesque suite de cases adjacentes à laquelle l'algorithme peut accéder en 1 instruction et pouvant contenir **_un objet basique_**. An algorithmie, on ne préoccupe pas vraiment de ce qu'est la mémoire.cela peut être celle de l'informaticien lecteur ou sur un ordinateur : peu importe. Pour un ordinateur réel, les objets sont stockés dans une partie de la mémoire nommée **tas** (le tas est un tableau où chaque case contient 1 byte = 8 bit).

![tas](tas.png)

Les objets sont stockées dans le tas. Notez que le tas peut contenir des "trous", c'est à dire des endroits sans objets.

### <span id="opérations"></span> Opérations

Les opérations que peuvent effectuer les pseudo-codes sont liées aux objets. On doit pouvoir :

- **_créer des objets_** : le caractère "Ç", l'entier `42`, etc...
- **_opérer sur des objets_** : rendre la somme de deux entiers, le résultat d'une formule logique, etc
- **_afficher un objet_**. On suppose que l'on possède une opération unaire spéciale nommée `affiche` qui affiche à l'écran (ou à n'importe quoi permettant à l'utilisateur d'avoir un retour) l'objet. Par exemple `affiche 42`{.language-} va afficher l'objet entier valant 42 à l'écran.

#### Créer des objets

La seule façon de créer un objet à partir de rien est de définir une constante.

{% algorithme %}
#pseudocode-list(line-numbering: none)[

- 42
  ]
  {% endalgorithme %}

#### Opérations

De façon formelle, une **_opération_** est une fonction dont l'espace de départ est un produit cartésien de types et l'espace d'arrivée un type donné. Les opérations sont le second moyen de créer des objets via leur résultat. Par exemple le booléen Vrai est crée comme résultat de l'opération `40 > 2`. Les seules opérations définies par défaut dans tout pseudo-code sont peu nombreuses :

- pour les entiers et les réels :
  - arithmétique : addition (`+`{.language-}), soustraction (`-`{.language-}), multiplication (`*`{.language-}), division (`/`{.language-})
  - opérations usuelles comme prendre la valeur entière, la valeur absolue, ...
  - la division entière de deux nombre (`//`{.language-}) et le modulo (`%`{.language-})
  - logique : égalité (avec le signe `==`{.language-}), plus petit que (`<`{.language-}), plus grand que (`>`{.language-}), plus petit ou égal (`≤`{.language-}), plus grand ou égal (`≥`{.language-})
- pour les caractères :
  - logique : égalité (avec le signe `==`{.language-})
- opérations sur les bits et les booléens :
  - "négation logique" (non, `NOT`{.language-}, $\neg$),
  - "et logique" (et, `&&`{.language-}, `AND`{.language-} ou $\land$), "ou logique" (ou, `||`{.language-}, `OR`{.language-} ou $\lor$)

{% algorithme %}
#pseudocode-list(line-numbering: none)[

- 40 + 2 #text(stroke: green)[\# rendra l'objet entier 42]
  ]
  {% endalgorithme %}

Toutes les autres opérations devront être définies soit dans le pseudo-code (avec des fonctions, comme on va le voir) soit dans un texte avant celui-ci.

#### Affichage

Enfin, la dernière opération autorisée pour les objet est l'affichage :

{% algorithme %}
#pseudocode-list(line-numbering: none)[

- _affiche_ 42
  ]
  {% endalgorithme %}

L'affichage est destiné, comme le commentaire, au lecteur du pseudo-code. Son but est de lui montrer des résultats intermédiaires intéressant lors de l'exécution du pseudo-code. Ne confondez pas un commentaire avec un retour de fonction : ce qui est affiché sort du contrôle du pseudo-code. Dans l'exemple précédent, l'entier 42 est affiché, le pseudo-code n'en a pas conscience.

{% attention "**À retenir**" %}
Pour distinguer le retour de fonction, d'un affichage supprimez tous les affichages de votre pseudo-code et il doit continuer de fonctionner.
{% endattention %}

## Variables

Une **_variable_** permet de retrouver un objet stocké en mémoire pour sa réutilisation :

{% note "**Définition**" %}
Une **_variable_** est un nom auquel est associé un objet d'**un type donné**.
{% endnote %}

Les variables nous permettent de manipuler les objets. Conceptuellement parlant, ce sont juste des **liens vers** les objets qu'elles référencent.

En algorithmie, tout comme pour les objets on ne se préoccupe pas vraiment où sont stockés les variables. Pour un ordinateur réel, elles sont stockées dans une partie de la mémoire nommée **pile** et contiennent l'indice de la mémoire du tas où commence l'objet qu'elle référence. Chaque variable est donc juste assez grande pour stocker un indice (64bit sur les ordinateur actuel ce qui permet d'avoir théoriquement un tas de taille $2^{64}$byte = 18446744073709551616B = 16777216 terabyte).

![pile](pile.png)

Chaque variable a la même taille et sont stockés de façon consécutives dans la pile. En effet, les variables sont crées au début de l'algorithme et sont toues supprimées en même temps à la fin de l'algorithme.

### Définition

Avant de pouvoir être utilisée, une variable doit être définie. La ligne suivante définie une variable de nom $a$ pouvant référencer un objet de type entier :

{% algorithme %}
#pseudocode-list(line-numbering: none)[

- $a colon.eq$ #text(weight: "bold")[entier]
  ]
  {% endalgorithme %}

La ligne précédente crée une nouvelle variable nommée `a` pouvant référencer des objets de type entier. Dans tout le reste du pseudo-code, on sera sur que `a` contient une valeur entière.

{% note "**Définition**" %}
Le format général de la définition d'une variable est :

{% algorithme %}
#pseudocode-list(line-numbering: none)[

- #text(stroke: blue)[nom] $colon.eq$ #text(stroke: red)[type]
  ]
  {% endalgorithme %}

On utilise l'**_opérateur de définition_** `:=`{.language-} pour créer une variable.

{% endnote %}

En pseudo-code, comme le principal soucis est la non ambiguïté, une variable ne peut contenir que des objets d'un type spécifié lors de sa définition.

{% info %}
Ce comportement est utilisé dans certains langages de programmation (java, rust, go) mais pas d'en d'autres comme le python où une variable peut être associée à des objets de types différents.

{% endinfo %}

### Affectation

Une fois la variable crée, on peut lui **_affecter_** des objets, par exemple pour notre variable `a`{.language-} crée précédemment :

```pseudocode
a ← 3
```

La ligne précédente La ligne précédente associe ainsi à la variable `a` un objet entier valant 3.

{% note "**Définition**" %}
Le format général de l'affectation d'un objet à une variable est :

{% algorithme %}
#pseudocode-list(line-numbering: none)[

- #text(stroke: blue)[nom] $<-$ #text(stroke: red)[objet]
  ]
  {% endalgorithme %}

On utilise l'**_opérateur d'affectation_** `←`{.language-} pour affecter une variable.

{% endnote %}

On n'utilisera pas le signe `=` en pseudo-code pour l'affectation car cette opération n'est pas symétrique : à gauche une variable à droite un objet.

{% info %}
Comme le symbole `←`{.language-} n'est pas présent sur un clavier, de nombreux langages de programmation utilisent cependant le signe `=`{.language-} pour une affectation.
{% endinfo %}

Une variable est une opération temporaire. On peut réaffecter une variable à un autre objet au cours du pseudo-code :
{% algorithme %}
#pseudocode-list()[

- $a colon.eq$ _entier_
- #text(stroke: green)[\# des instructions]
- $a <- 4$
- #text(stroke: green)[\# des instructions]
- $a <- 2$
  ]
  {% endalgorithme %}

Après la troisième ligne, le code précédent associe la variable `a`{.language-} à un entier valant 4 et à un entier valant 2 après la cinquième ligne. Il est important de noter que :

{% attention "**À retenir**" %}
Une variable n'**est pas** un objet, c'est un lien vers un objet qui pourra changer au cours du temps.
{% endattention %}

D'un point de vue matériel, rappelez vous qu'une variable est un entier qui correspond à un indice dans le tableau de la mémoire.

### Utilisation

Utiliser une variable consiste à la remplacer dans l'instruction par l'objet qu'elle référence. Par exemple :

{% algorithme %}
#pseudocode-list(line-numbering: none)[

- $a colon.eq$ _entier_
- $a <- 42$
- _affiche_ $a$
  ]
  {% endalgorithme %}

Le code précédent affiche l'objet référencé par $a$. Il est équivalent à : `affiche 42`{.language-}.

{% note "**Définition**" %}
**_Utiliser_** une variable dans un code revient à la remplacer par l'objet qu'elle référence. Ce remplacement se fait **avant** l'exécution de l'instruction.

{% endnote %}

Regardons ceci avec quelques exemples :

{% algorithme %}
#pseudocode-list()[

- $a colon.eq$ _entier_
- $a <- 42$
- $b colon.eq$ _entier_
- $b <- a$
  ]
  {% endalgorithme %}

La ligne 4, une instruction d'affectation, s'exécute de la façon suivante :

1. on commence par retrouver objet à droite de l'opérateur `←`{.language-}. C'est une variable : on récupère son objet, un entier valant 3
2. on affecte cet objet à la variable à gauche de l'opérateur `←`{.language-}, la variable `b`{.language-}

Autre exemple :

{% algorithme %}
#pseudocode-list()[

- $a colon.eq$ _entier_
- $a <- 3$
- $b colon.eq$ _entier_
- $b <- a + 1$
  ]
  {% endalgorithme %}

La ligne 4, une instruction composée d'une opération puis d'ue affectation, s'exécute de la façon suivante :

1. on commence par retrouver objet à droite de l'opérateur `←`{.language-}. C'est le résultat d'une opération :
   1. pour effectuer l'opération, il faut commencer par retrouver l'objet associé à `a` : un entier valant 3
   2. on peut maintenant effectuer l'opération d'addition qui rend un objet valant 4
2. on affecte cet objet à la variable à gauche de l'opérateur `←`{.language-}, la variable `b`{.language-}

Attention cependant :

{% attention "**À retenir**" %}
On ne peut utiliser une variable qu'après l'avoir affectée. Utiliser une variable qui n'a été que définie rend un résultat non prédictif : c'est interdit en algorithmie.
{% endattention %}

## <span id="tableaux"></span>Tableaux

{% note "**Définition**" %}
Un **_tableau_** est un conteneur nommé pouvant contenir $n$ variables **de même type**. $n$ est la **_longueur_** ou la **_taille_** du tableau. La taille d'un tableau est déterminée à sa création et ne peut être modifiée. Chaque variable du tableau peut être accédée via son **_indice_**, qui est un entier entre $0$ et $n-1$.

Si le tableau est nommé $t$ :

- $t.\mbox{longueur}$ sera égal à sa taille.
- $t[i]$ est sa variable d'indice $i$ si $0 \leq i < n$
- $t[-i]$ vaut $t[n-i]$ si si $0 < i  \leq n$

{% endnote %}

Créons un tableau :

{% algorithme %}
#pseudocode-list(line-numbering: none)[

- T $colon.eq$ [entier] {longueur: 13}
  ]
  {% endalgorithme %}

La ligne précédente crée un tableau de 13 entiers.

{% note "**Définition**" %}
Le format général de la création d'un tableau de longueur $n$ est :

{% algorithme %}
#pseudocode-list(line-numbering: none)[

- #text(stroke: blue)[nom] $colon.eq$ [#text(stroke: red)[type]] {longueur: #text(stroke: orange)[n]}
  ]
  {% endalgorithme %}

Le type d'un tableau est défini par le type des objets qu'il contient entre crochet : `[type]`{.language-}.
{% endnote %}

Un tableau est un mix entre variables et objet : c'est un objet contenant des variables. Les différentes références des variables du tableau sont stockées de façon contiguë en mémoire pour pouvoir y accéder rapidement pour y être lu ou modifiée :

![tableau](tableau.png)

On considère que :

- la taille en mémoire d'un tableau est proportionnelle à la taille d'un objet fois la taille.
- il faut 1 instruction pour créer un tableau
- il faut 1 instruction pour accéder à une variable d'indice donné.

{% info %}
On considère que créer un tableau prend 1 instruction car celui-ce est de taille fixée. [On justifiera ceci proprement plus tard](../../complexité-calculs/O-pour-l-algorithmie){.interne}.
{% endinfo %}

Les tableaux peuvent être simples comme une suite finie d'entiers ou des types plus complexes comme une matrice à 2 dimensions où chaque élément du tableau est un autre tableau. La seule opération spécifique à un tableau est sa création qui prendra toujours 1 instruction, puis on affecte les variables.

{% attention %}
Tout comme une variable, une fois le tableau crée, la valeur de chaque case est **indéterminée !**. Il est **indispensable** d'initialiser les valeurs de chaque case avant de les utiliser.
{% endattention %}

Toutes les autres opérations sur les tableaux sont faites graces aux opérations des objets basiques qui les composent. Il n'y a pas d'opérations spécifiques à ceux-ci :

{% attention "**À retenir**" %}
Les opérations sur les tableaux seront toujours des opérations composées d'une suite d'opérations effectuées sur les objets basiques les constituants.
{% endattention %}

Ainsi, on ne peut **pas** affecter un tableau. Il faut créer un nouveau tableau puis y recopier tous les éléments de l'ancien.

### Tranches

On utilisera parfois, comme en python par exemple des sous tableaux via des **_tranches_** (**_slices_** en anglais) :

- `T[i:]`{.language-} représentera le tableau constitué des éléments de T à partir de l'indice i **inclus** jusqu'à la fin
- `T[:j]`{.language-} représentera le tableau constitué des éléments de T à partir de l'indice 0 **inclus** jusqu'à j **exclu**
- `T[i:j]`{.language-} représentera le tableau constitué des éléments de T à partir de l'indice i **inclus** jusqu'à j **exclu**

{% attention %}
Tout comme pour les tableaux, on ne peut **pas** affecter une tranche de tableau. Il faut créer un nouveau tableau puis y recopier tous les éléments de l'ancien.
{% endattention %}

### <span id="str"></span>Chaînes de caractères

Les chaines de caractères sont un tableau uniquement composés de caractères. Cette structure est utilisée lorsque l'on veut écrire ou représenter plus qu'un caractère, c'est à dire quasi tout le temps.

Une **_chaîne de caractères_** est un tableau constitué uniquement de caractères.

Comme ce sont des tableaux, on peut :

- créer une chaîne de caractères : `"salut"`{.language-} crée la chaîne contenant les caractères `"s"`{.language-}, `"a"`{.language-}, `"l"`{.language-}, `"u"`{.language-} et `"t"`{.language-} de façon contiguë en mémoire.
- affecter une chaîne de caractères à une variable prend 1 instruction : `s ← "salut"`{.language-} prend 2 instructions, une pour la création et une pour l'affectation.
- accéder à un caractère particulier en utilisant les crochets : `s[2]`{.language-} vaut le caractère `"l"`{.language-}
- connaître la longueur de la chaîne avec : `s.longueur`{.language-}

Les chaines étant très utilisées, des langages comme python les considèrent comme un type de base et considèrent les caractères comme étant des chaîne de langueur 1.

{% note %}
Chacune des quatre opérations précédentes (création, affectation, accès et concaténation) prend 1 instruction (les chaînes crées sont des constantes).
{% endnote %}

La chaîne de caractère étant très utilisée, on se permettra les abus suivant :

- de définir une chaîne directement : `s := chaine"`{.language-} en utilisant le type chaîne
- puis de l'affecter : `s ← "Salut"`{.language-}
- on définit l'opération de concaténation avec l'opérateur `+`{.language-} : `"salut" + " toi !"`{.language-} vaut la chaîne de caractères `"salut toi !"`{.language-}

Le type `chaîne`{.language-} peut être vu comme un synonyme `[caractère]`{.language-} sauf que l'on ne peut pas modifier un de ses indices (`s[2] ← "p"`{.language-} ne sera pas une instruction valide), bien que l'on puisse y accéder (`affiche s[2]`{.language-} sera une instruction valide). Un tableau de chaînes sera de type `[chaîne]`{.language-}.

## <span id="instruction-contrôle"></span> Instructions de contrôle

Si un des deux buts d'une instruction est de créer des objets à partir d'autres (ce que l'on vient de voir), le second but est de contrôler le flux d'instructions à exécuter. Ces instructions sont de deux types :

- [l'exécution conditionnelle d'instructions](./#tests){.interne},
- [la répétition d'instructions](./#répétition){.interne}

Ces formes d'instruction nécessitent de grouper les instructions en blocs.

### Blocs

Lier les instructions en blocs. On va utiliser ici le formalisme de python pour définir un bloc :

```text
type de bloc:
    instruction 1
    instruction 2
    ...
    instruction n
```

On décale les instructions du bloc de sa définition. C'est un truc clair qui permet de voir du premier coup d'œil les instructions d'un bloc.

### <span id="tests"></span> Exécution conditionnelle d’instructions

On veut pouvoir exécuter un bloc de code si une condition logique est VRAIE :

```pseudocode
si (condition logique):
    instruction 1

    ...
    instruction n
```

Cette instruction basique peut avoir plein de variantes comme :

```pseudocode
si (condition logique):
    instruction 1
    ...
    instruction n
sinon:
    instruction 1
    ...
    instruction n'
```

ou encore :

```pseudocode
si (condition logique):
    instruction 1
    ...
    instruction n
sinon si (autre condition logique):
    instruction 1
    ...
    instruction n'
```

Ou tout mix de tout ça, du moment que c'est clair !

{% info %}
On peut dériver toutes les variantes de la forme initiale.
{% endinfo %}

### <span id="répétition"></span> Répétition

On doit pouvoir répéter un bloc tant qu'une condition logique est vérifiée :

```pseudocode
tant que (condition logique):
    instruction 1
    ...
    instruction n
```

Le ploc précédent est exécuté tant que la condition logique est vraie. Il existe une variation de ce bloc très utile :

```pseudocode
pour chaque élément x d'un tableau:
    instruction 1
    ...
    instruction n
```

On exécutera alors le bloc autant de fois qu'il y a d'éléments dans le tableau et à chaque itération du bloc, la variable `x`{.language-pseudocode} (de type de celui des objets stockés dans le tableau) vaudra un autre élément du tableau. On prendra les éléments du tableau par indice croissant.

Le code précédent est équivalent au code suivant, moins élégant, mais qui explicite le numéro de l'itération courante : à l'itération $i$ on examine le $i+1$ ème élément du tableau et on a déjà examiné les $i$ premiers.
:

```pseudocode
x := entier
pour chaque i de [0 .. tableau.longueur[:
    x ← tableau[i]

    instruction 1
    ...
    instruction n
```

Enfin, on peut tout à fait écrire la variante `pour chaque`{.language-pseudocode} de la forme initiale `tant que`{.language-pseudocode} :

```pseudocode
x := entier

i := entier
i ← 0
tant que i < tableau.longueur:
    x ← tableau[i]

    instruction 1
    ...
    instruction n

    i ← i + 1
```

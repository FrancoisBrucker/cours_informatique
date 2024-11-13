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

Commençons par décrire les objets que l'on peut manipuler en pseudo-code et les moyens d'y accéder.

> TBD définir les opérations et donner les variantes ($\leftarrow$, $:=$)
> TBD fonction = algorithme
> TBD dire que $=$ est un _devient_.
> TBD parler des portée des variables : l'algorithme c'est à dire la fonction.

## <span id="objets-basique"></span> Objets et variables

### <span id="objets-basique"></span> Objets basiques

Les objets que nous aurons directement à notre disposition sans avoir besoin de les définir sont appelés **_objets basiques_** et sont au nombre de cinq :

- le vide (nommé `None`{.language-} en python, `null`{.language-} en javascript ou encore `void`{.language-} en C)
- les booléens (vrai et faux)
- les nombres entiers
- les nombres réels
- les caractères

Tous les autres types d'objets que l'on peut créer seront des compositions de ces 5 types d'objets (un point en 3D par exemple est constitué de 3 réels).

Les instructions liées à ces objets sont de deux ordres. On doit pouvoir :

- **_créer des objets_**
- **_opérer sur ces objets_** :
  - opérations sur les entiers et/ou réels :
    - arithmétique : addition (`+`{.language-}), soustraction (`-`{.language-}), multiplication (`*`{.language-}), division (`/`{.language-})
    - opérations usuelles : prendre la valeur entière, valeur absolue, le modulo
    - logique : égalité (avec le signe `==`{.language-} ou `=`{.language-}), plus petit que (`<`{.language-}), plus grand que (`>`{.language-}), plus petit ou égal (`≤`{.language-}), plus grand ou égal (`≥`{.language-})
  - opérations sur les caractères :
    - logique : égalité (avec le signe `==`{.language-})
  - opérations sur les booléens : "négation logique" (non, `NOT`{.language-}, $\neg$), "et logique" (et, `&&`{.language-}, `AND`{.language-}), "ou logique" (ou, `||`{.language-}, `OR`{.language-})

Notez que tous les objets basiques à part les entiers sont de taille fixe :

- booléen 1bit
- caractères 32bits si on utilise les caractères Unicode
- réel norme IEEE sur 64bits

On peut très bien sans perte de généralité se restreindre aux entiers entree 0 et $2^{64}$, et c'est d'ailleurs ce que beaucoup de langages de programmation font, puisque qu'un entier quelconque peut être représenté en base $2^{64}$ et ainsi être représenté par un tableau d'entiers codé sur 64bits. C'est d'ailleurs ce qui se passe en python pr exemple où un entier, qui n'est pas borné, est composé d'un tableau d'entiers codés sur 64bits. Ceci est cependant transparent pour l'utilisateur (et c'est tant mieux).

{% note "**À retenir**" %}
On considérera toujours qu'un objet basique est de taille connue et donnée au début du programme.
{% endnote %}

### Variables

Les objets que l'on manipule doivent pouvoir être conservés pour que l'on puisse les réutiliser tout au long du programme. Cet espace espace de stockage, que l'on nomme **_une mémoire_**, est identifié d'un point de vue algorithmique, à une gigantesque suite de cases adjacentes à laquelle l'algorithme peut accéder en 1 instruction et pouvant contenir **_un objet basique_**.

Une **_variables_** est alors associé à la première case de la mémoire contenant l'objet. D'un point de vue algorithmique, cela revient à référencer un objet, à le nommer :

{% note "**Définition**" %}
Une **_variable_** est un nom auquel est associé un objet.
{% endnote %}

Les instructions autorisées sur les variables sont :

- **_l'affectation_** : `a = 3`{.language-} défini le nom `a`{.language-} (appelé _variable_) qui est associé à un entier valant `3`{.language-}. (vous verrez parfois utilisé $a \leftarrow 3$ à la place de $a = 3$ pour qu'il n'y ait pas de confusion si l'on utilise `=`{.language-} pour l'égalité)
- **_la lecture_**. Si j'ai affecté `3`{.language-} à la variable `a`{.language-}, je dois pouvoir l'utiliser, par exemple en écrivant `b = a * 3`{.language-}
- **_l'affichage à l'écran_**. Pour permettre un retour à l'utilisateur de ce qu'à produit le pseudo-code.

{% attention %}
Une variable est un nom, elle ne copie ni ne modifie un objet dans le pseudo-code suivant, les deux variables `a`{.language-} et `b`{.language-} référencent le même objet entier.

```pseudocode
a = 3
b = a
```

Dans la seconde instruction, on commence par retrouver l'objet nommé par `a`{.language-} et on le nomme `b`{.language-} : la case où est stocké l'entier dans la mémoire est donné à `a`{.language-} et à `b`{.language-}
{% endattention %}

## <span id="structures"></span> Structures

Les objets basiques sont les briques élémentaires permettant de créer tout ce dont un algorithme à besoin. Un nombre complexe est composé de 2 approximations de réels ou une phrases d'une suite de caractères par exemples. Gérer ces objets complexes, appelés **_structures_**, se fait aux **_tableaux_**. Comme une structure est toujours _in fine_ composée d'objet basiques :

{% note "**À retenir**" %}
On considérera toujours que la taille d'une structure est proportionnelle à la taille des objets qui la compose et est connue à sa création.
{% endnote %}

### <span id="tableaux"></span>Tableaux

{% note "**Définition**" %}
Un **_tableau_** est un conteneur nommé pouvant contenir $n$ variables. $n$ est la **_longueur_** ou la **_taille_** du tableau. La taille d'un tableau est déterminée à sa création et ne peut être modifiée.

Chaque variable du tableau peut être accédée via son **_indice_**, qui est un entier entre $0$ et $n-1$. Si le tableau est nommé $t$ :

- $t[i]$ est sa variable d'indice $i$ si $0 \leq i < n$
- $t[-i]$ vaut $t[n-i]$ si si $0 < i  \leq n$

{% endnote %}

Les différentes variables du tableaux sont stockées de façon contiguë en mémoire pour pouvoir y accéder rapidement pour y être lu ou modifiée.

Les tableaux peuvent être simples comme une suite finie d'entiers ou des types plus complexes comme une matrice à 2 dimensions où chaque élément du tableau est un autre tableau.

On considérera que :

- la création d'un tableau prend 1 instruction : `[1, 3, x]`{.language-} crée un tableau qui affecte à sa variable :
  - d'indice 0 un entier valant 1
  - d'indice 1 un entier valant 3
  - d'indice 2 l'objet associé à la variable `x`{.language-}
- l'affectation d'un tableau à une variable prend 1 instruction : `t=[1, 3, x]`{.language-} prend 2 instructions une pour la création et une pour l'affectation
- l’accès à un élément particulier du tableau se fait en 1 instruction et en utilisant les crochets : `t[2]`{.language-} vaut le caractère `"l"`{.language-}

{% info %}
On considère que créer un tableau prend 1 instruction car celui-ce est de taille fixée. [On justifiera ceci proprement plus tard](../../complexité-calculs/O-pour-l-algorithmie).
{% endinfo %}

Les opérations sur les tableaux sont faites graces aux opérations des objets basiques qui les composent. Il n'y a pas d'opérations spécifiques à ceux-ci :

{% note "**À retenir**" %}
Les opérations sur les tableaux seront toujours des opérations composées d'une suite d'opérations effectuées sur les objets basiques les constituants.
{% endnote %}

### <span id="str"></span>Chaînes de caractères

Les chaines de caractères sont un tableau uniquement composés de caractères. Cette structure est utilisée lorsque l'on veut écrire ou représenter plus qu'un caractère, c'est à dire quasi tout le temps.

Une **_chaîne de caractères_** est un tableau constitué uniquement de caractères.

On peut les manipuler essentiellement comme un tableau. On peut :

- créer une chaîne de caractères : `"salut"`{.language-} crée la chaîne contenant les caractères `"s"`{.language-}, `"a"`{.language-}, `"l"`{.language-}, `"u"`{.language-} et `"t"`{.language-} de façon contiguë en mémoire.
- affecter une chaîne de caractères à une variable prend 1 instruction : `s = "salut"`{.language-} prend 2 instructions, une pour la création et une pour l'affectation.
- accéder à un caractère particulier en utilisant les crochets : `s[2]`{.language-} vaut le caractère `"l"`{.language-}

Les chaines étant très utilisées, des langages comme python les considèrent comme un type de base et considèrent les caractères comme étant des chaîne de langueur 1. Les chaines de caractères héritent donc de certains comportements spécifiques aux objets basiques :

- une fois crées **on ne peut pas les modifier** (`s[2] ="p"`{.languages} n'est pas une instruction valide).
- on définit l'opération de concaténation avec l'opérateur `+`{.language-} : `"salut" + " toi !"`{.language-} vaut la chaîne de caractères `"salut toi !"`{.language-}

{% note %}
Chacune des quatre opérations précédentes (création, affectation, accès et concaténation) prend 1 instruction. [On justifiera ceci proprement plus tard](../../complexité-calculs/O-pour-l-algorithmie) (les chaînes crées sont des constantes).
{% endnote %}

## <span id="instruction"></span> Instructions de contrôle

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

> TBD : dire que l'on en a de deux types : for et while. Que l'on peut tout faire en while mais les boucles for sont plus lisible, en particulier leur condition d'arrêt est claire.

On doit pouvoir répéter un bloc tant qu'une condition logique est vérifiée (boucle _while_):

```pseudocode
tant que (condition logique):
    instruction 1
    ...
    instruction n
```

Il existe une variation de ce bloc très utile (boucle _for_):

```pseudocode
pour chaque élément x d'un tableau:
    instruction 1
    ...
    instruction n
```

On exécutera alors le bloc autant de fois qu'il y a d'éléments dans le tableau et à chaque itération du bloc, la variable `x` vaudra un autre élément du tableau. On prendra les éléments du tableau par indice croissant.

{% info %}
On peut dériver la variante `pour chaque`{.language-pseudocode} de la forme initiale `tant que`{.language-pseudocode}.
{% endinfo %}

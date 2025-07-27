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

## Objets et instructions

### <span id="objets-basiques"></span> Objets basiques

Les objets que nous aurons directement à notre disposition sans avoir besoin de les définir sont appelés **_objets basiques_** et correspondent aux cinq **_types_** suivant :

- le type `booléen`{.language-} qui contient deux objets : `vrai`{.language-} et `faux`{.language-}
- le type `bit`{.language-} qui contient les 2 objets : `0`{.language-} et `1`{.language-}
- le type `entier`{.language-} qui contient tous les entiers relatifs
- le type `réel`{.language-} qui contient un ensemble dénombrable d'approximation de réels
-  le type `caractère`{.language-} qui contient l'ensemble des glyphes  UNICODE : `"a"`{.language-}, `"b"`{.language-}, ...

Enfin on considérera le type vide `∅`{.language-} (nommé `None`{.language-} en python, `null`{.language-} en javascript ou encore `void`{.language-} en C) qui ne contient aucun objet.

Tous les autres types d'objets que l'on peut créer seront des compositions de ces 5 types d'objets (un point en 3D est constitué de 3 réels, une chaîne de caractères est une liste de caractères, etc).

Notez que tous les objets basiques à part les entiers sont de taille fixe :

- booléen 1bit
- caractères 32bits si on utilise les caractères Unicode
- réel norme IEEE sur 64bits

On peut sans perte de généralité se restreindre aux entiers entree 0 et $2^{64}$, et c'est d'ailleurs ce que beaucoup de langages de programmation font, puisque qu'un entier quelconque peut être représenté en base $2$ et découpé en paquets de 64 bits. C'est ce  que font les languages d programmation comme python où un entier, qui n'est pas borné pfr nature, est composé d'un tableau d'entiers codés sur 64bits. Ceci est cependant transparent pour l'utilisateur (et c'est tant mieux).

{% attention "**À retenir**" %}
On considérera toujours qu'un objet basique est de taille connue et donnée au début du programme.
{% endattention %}


### <span id="opérations"></span> Opérations

Les opérations que peuvent effectuer les pseudo-codes sont liées aux objets. On doit pouvoir :

- **_créer des objets_**
- **_opérer sur des objets_** :
  - opérations sur les entiers et/ou réels :
    - arithmétique : addition (`+`{.language-}), soustraction (`-`{.language-}), multiplication (`*`{.language-}), division (`/`{.language-})
    - opérations usuelles comme prendre la valeur entière, la valeur absolue, ...
    - la division entière de deux nombre (`//`{.language-}) et le modulo (`%`{.language-})
    - logique : égalité (avec le signe `==`{.language-}), plus petit que (`<`{.language-}), plus grand que (`>`{.language-}), plus petit ou égal (`≤`{.language-}), plus grand ou égal (`≥`{.language-})
  - opérations sur les caractères :
    - logique : égalité (avec le signe `==`{.language-})
  - opérations sur les booléens : "négation logique" (non, `NOT`{.language-}, $\neg$), "et logique" (et, `&&`{.language-}, `AND`{.language-}), "ou logique" (ou, `||`{.language-}, `OR`{.language-})

## Variables

Les objets que l'on manipule doivent pouvoir être conservés pour que l'on puisse les réutiliser tout au long du programme. Cet espace espace de stockage, que l'on nomme **_une mémoire_**, est identifié d'un point de vue algorithmique, à une gigantesque suite de cases adjacentes à laquelle l'algorithme peut accéder en 1 instruction et pouvant contenir **_un objet basique_**.

Une **_variables_** est alors associé à la première case de la mémoire contenant l'objet. D'un point de vue algorithmique, cela revient à référencer un objet, à le nommer :

{% note "**Définition**" %}
Une **_variable_** est un nom auquel est associé un objet.
{% endnote %}

Les instructions autorisées sur les variables sont :

- **_l'affectation_** : `a ← 3`{.language-} défini le nom `a`{.language-} (appelé _variable_) qui est associé à un entier valant `3`{.language-}. On n'utilisera pas le signe `=` en pseudo-code car l'affectation n'est pas symétrique : à gauche une variable à droite un objet (comme le symbole `←`{.language-} de nombreux langages de programmation utilisent cependant le signe `=`{.language-}).
- **_la lecture_**. Si j'ai affecté `3`{.language-} à la variable `a`{.language-}, je dois pouvoir l'utiliser, par exemple en écrivant `b ← a * 3`{.language-}
- **_l'affichage à l'écran_**. Pour permettre un retour à l'utilisateur de ce qu'à produit le pseudo-code.

{% attention %}
Une variable est un nom, elle ne copie ni ne modifie un objet dans le pseudo-code suivant, les deux variables `a`{.language-} et `b`{.language-} référencent le même objet entier.

```pseudocode
a ← 3
b ← a
```

Dans la seconde instruction, on commence par retrouver l'objet nommé par `a`{.language-} et on le nomme `b`{.language-} : la case où est stocké l'entier dans la mémoire est donné à `a`{.language-} et à `b`{.language-}
{% endattention %}

## <span id="tableaux"></span>Tableaux

{% note "**Définition**" %}
Un **_tableau_** est un conteneur nommé pouvant contenir $n$ variables **de même type**. $n$ est la **_longueur_** ou la **_taille_** du tableau. La taille d'un tableau est déterminée à sa création et ne peut être modifiée. Chaque variable du tableau peut être accédée via son **_indice_**, qui est un entier entre $0$ et $n-1$.

Si le tableau est nommé $t$ :

- $t.\mbox{longueur}$ sera égal à sa taille.
- $t[i]$ est sa variable d'indice $i$ si $0 \leq i < n$
- $t[-i]$ vaut $t[n-i]$ si si $0 < i  \leq n$

{% endnote %}

Les différentes variables du tableaux sont stockées de façon contiguë en mémoire pour pouvoir y accéder rapidement pour y être lu ou modifiée, on considère que :

- la taille en mémoire d'un tableau est proportionnelle à la taille d'un objet fois la taille.
- il faut 1 instruction pour créer un tableau
- il faut 1 instruction pour accéder à une variable d'indice donné.

{% info %}
On considère que créer un tableau prend 1 instruction car celui-ce est de taille fixée. [On justifiera ceci proprement plus tard](../../complexité-calculs/O-pour-l-algorithmie){.interne}.
{% endinfo %}

Les tableaux peuvent être simples comme une suite finie d'entiers ou des types plus complexes comme une matrice à 2 dimensions où chaque élément du tableau est un autre tableau. La seule opération spécifique à un tableau est sa création qui peut être directe :

- `t ← [1, 3, 2]`{.language-} qui crée un tableau de 3 entiers
- `t ← tableau de 23 caractères`{.language-} qui crée un tableau de 23 caractères

On considère que la création d'un tableau prendra toujours 1 instruction, puis on affecte les variables. La première affectation est donc un raccourci pour 4 instructions :

1. la création d'un tableau de longueur 3
2. l'affectation `t[0] ← 1`{.language-} 
3. l'affectation `t[1] ← 3`{.language-} 
4. l'affectation `t[2] ← 2`{.language-} 

{% attention %}
Une fois le tableau crée, la valeur de chaque case est **indéterminée !**. Il est **indispensable** d'initialiser les valeurs de chaque case avant de les utiliser.
{% endattention %}


Toutes les autres opérations sur les tableaux sont faites graces aux opérations des objets basiques qui les composent. Il n'y a pas d'opérations spécifiques à ceux-ci :

{% attention "**À retenir**" %}
Les opérations sur les tableaux seront toujours des opérations composées d'une suite d'opérations effectuées sur les objets basiques les constituants.
{% endattention %}

Le type d'un tableau sera de la forme `[T]`{.language-} et signifiera que le tableau contient des objets de type `T`{.language-}. Un tableau de type `[entier]`{.language-} contiendra des entiers.

### Tranches

On utilisera parfois, comme en python par exemple des sous tableaux via des **_tranches_** (**_slices_** en anglais) :

- `T[i:]`{.language-} représentera le tableau constitué des éléments de T à partir de l'indice i **inclus** jusqu'à la fin
- `T[:j]`{.language-} représentera le tableau constitué des éléments de T à partir de l'indice 0 **inclus** jusqu'à j **exclu**
- `T[i:j]`{.language-} représentera le tableau constitué des éléments de T à partir de l'indice i **inclus** jusqu'à j **exclu**

{% attention %}
On ne peut  **pas** affecter une tranche de tableau. Il faut créer un nouveau tableau puis y recopier tous les éléments de l'ancien.
{% endattention %}

### <span id="str"></span>Chaînes de caractères

Les chaines de caractères sont un tableau uniquement composés de caractères. Cette structure est utilisée lorsque l'on veut écrire ou représenter plus qu'un caractère, c'est à dire quasi tout le temps.

Une **_chaîne de caractères_** est un tableau constitué uniquement de caractères.

Comme ce sont des tableaux, on peut :

- créer une chaîne de caractères : `"salut"`{.language-} crée la chaîne contenant les caractères `"s"`{.language-}, `"a"`{.language-}, `"l"`{.language-}, `"u"`{.language-} et `"t"`{.language-} de façon contiguë en mémoire.
- affecter une chaîne de caractères à une variable prend 1 instruction : `s ← "salut"`{.language-} prend 2 instructions, une pour la création et une pour l'affectation.
- accéder à un caractère particulier en utilisant les crochets : `s[2]`{.language-} vaut le caractère `"l"`{.language-}
- connaître la longueur de la chaîne avec : `s.longueur`{.language-}

Les chaines étant très utilisées, des langages comme python les considèrent comme un type de base et considèrent les caractères comme étant des chaîne de langueur 1. Les chaines de caractères héritent donc de certains comportements spécifiques aux objets basiques :

- une fois crées **on ne peut pas les modifier** (`s[2] ← "p"`{.language-} n'est pas une instruction valide pour des chaînes alors que c'est une instruction valide pour un tableau).
- on définit l'opération de concaténation avec l'opérateur `+`{.language-} : `"salut" + " toi !"`{.language-} vaut la chaîne de caractères `"salut toi !"`{.language-}

{% note %}
Chacune des quatre opérations précédentes (création, affectation, accès et concaténation) prend 1 instruction (les chaînes crées sont des constantes).
{% endnote %}

La chaîne de caractère étant très utilisée, on se permettra les abus suivant :

- de définir une chaîne directement `s ← "Salut"`{.language-}
- d'utiliser le type `chaîne`{.language-} plutôt que `[caractère]`{.language-} (les 2 sont synonymes)

Ainsi, un tableau de chaînes sera de type `[chaîne]`{.language-} qui est égal à `[[caractère]]`{.language-} (un tableau de tableaux de caractères).

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

On exécutera alors le bloc autant de fois qu'il y a d'éléments dans le tableau et à chaque itération du bloc, la variable `x`{.language-pseudocode} vaudra un autre élément du tableau. On prendra les éléments du tableau par indice croissant.

Le code précédent est équivalent au code suivant, moins élégant, mais qui explicite le numéro de l'itération courante : à l'itération $i$ on examine le $i+1$ ème élément du tableau et on a déjà examiné les $i$ premiers.
 :

```pseudocode
pour chaque i de [0 .. tableau.longueur[:
    x ← tableau[i]

    instruction 1
    ...
    instruction n
```

Enfin, on peut tout à fait écrire la variante `pour chaque`{.language-pseudocode} de la forme initiale `tant que`{.language-pseudocode} :

```pseudocode
i ← 0
tant que i < tableau.longueur:
    x ← tableau[i]

    instruction 1
    ...
    instruction n

    i ← i + 1
```

## _"Abus"_ de notation

On se permettra, lorsque l'instruction est assez claire de procéder à des raccourci pour rendre le pseudocode plus digeste. Attention, la plupart de ces opérations ne seront pas des opérations élémentaires !

### Répétitions

```pseudocode
répéter k fois:
    ...
```

Pour :

```pseudocode
pour chaque i de [1 .. k]:
    ...
```

#### Répétitions par borne

Tout un tas de variations sont possibles, du moment que ce soit compréhensible. Par exemple :

```pseudocode
pour i de a à b:
    ...
```

Ou encore :

```pseudocode
pour i=a à i=b:
    ...
```

Pour :

```pseudocode
pour chaque i de [a .. b]:
    ...
```

#### Répétitions à pas fixé

```pseudocode
pour i de a à b par par pas de k:
    ...
```

ou encore :

```pseudocode
pour chaque i de [a .. b] par pas de k:
    ...
```

pour :

```pseudocode
i ← a
tant que i ≤ b:
  ...

  i ← i + k
```

### Affectation d'une tranche de tableau

```pseudocode
T[a:b] ← k
```

pour :

```pseudocode
pour chaque i de [a .. b[:
    T[i] ← k
```

Fonctionne aussi pour :

```pseudocode
T[:] ← k
```

Qui correspond à :

```pseudocode
pour chaque i de [0 .. T.longueur[:
    T[i] ← k
```

Ou encore à :

```pseudocode
T[a:b] ← T'[a':]
```

Qui correspond à :

```pseudocode
pour chaque i de [0 .. b-a[:
    T[a + i] ← T'[a' + i]
```

{% attention %}
Les affectations de tranches ne sont **pas** une instruction simple, mais nécessitent plusieurs instructions : ceux de la boucle sous-jacente.

Ainsi, le code suivant nécessite $1 + j - i$ instructions (1 instruction de création du nouveau tableau puis j-i affectations) :

```pseudocode
T' ← un nouveau tableau contenant T[i:j]  # j - i + 1 instructions en 1 ligne
```

{% endattention %}

### Concaténation

Avec deux tableaux :

```pseudocode
T ← T1 + T2
```

pour :

```pseudocode
T ← un nouveau tableau de taille T1.longueur + T2.longueur

pour chaque i de [0 .. T1.longueur[:
    T[i] ← T1[i]
pour chaque i de [0 .. T2.longueur[:
    T[T1.longueur + i] ← T2[i]

```

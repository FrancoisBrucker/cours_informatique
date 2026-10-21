---
layout: layout/post.njk
title: Briques de base

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le but d'un pseudo-code est d'être lu et compris par un humain. Il se doit d'être sans ambiguïté sans être lourd. Il est constitué d'instructions dont le but est soit :

- de manipuler des objets (création, affectation ou lecture)
- de contrôler le flux d'instructions (tests et boucles).

{% attention %}
Vous trouverez autant de types de pseudo-code différents que d'informaticiens. Je vous donne ici _"mon"_ pseudo-code. Son but est d'être assez explicite pour décrire sans ambiguïté les algorithmes de ce cours. Ne soyez donc pas étonnés si en lisant d'autres pseudo-codes ils ne suivent pas mes notations : ayez l'esprit ouvert.
{% endattention %}

Nous allons montrer ici une version de pseudo-code sans accès direct à la mémoire (_ie._ sans pointeur). Ce modèle est tout à fait fonctionnel et est utilisé dans les langages de programmation comme python ou javascript par exemple. Nous ajouterons l'accès direct à la mémoire (bien) plus tard dans ce cours. Ce modèle est plus simple à comprendre et à implémenter que le modèle avec pointeur et ne change rien algorithmiquement. Il va cependant nécessiter des opérations élémentaires supplémentaires (on appelle ceci des _overheads_) pour trouver la valeur de la variable en mémoire par rapport à l'utilisation directe de pointeurs.

## Commentaires

Comme en python, on considérera que tout ce qui suit le caractère `#`{.language-} est considéré comme un commentaire dont le but est d'éclairer le lecteur.

```pseudocode
# un commentaire
```

## Objets et opérations

Commençons par décrire les objets que l'on peut manipuler en pseudo-code et les moyens d'y accéder.

### Objets

Les objets sont ce que l'on manipule en algorithmie. [On a vu](../../bases-théoriques/définition/#manipuler-01) qu'a priori on peut n'utiliser que des suites finies de `0` et de `1` (ou de façon équivalente des entiers), mais cela nuirait grandement à la lisibilité. En pseudo code on se permet d'utiliser d'autres formes d'objets appartenant à 6 types fondamentaux. 

#### <span id="objets-basiques"></span> Objets basiques

Les objets que nous aurons directement à notre disposition sans avoir besoin de les définir sont appelés **_objets basiques_** et correspondent aux six **_types_** suivants :

{% definition %}

Un **_objet basique_** peut être d'un des cinq **_types_** suivants :

- le type `bool`{.language-} (booléen) qui contient deux objets : `vrai`{.language-} et `faux`{.language-}
- le type `bit`{.language-} qui contient les 2 entiers : `0`{.language-} et `1`{.language-}
- le type `int`{.language-} (entier) qui contient tous les entiers relatifs
- le type `float`{.language-} (réel) qui contient un ensemble dénombrable d'approximations de réels (un nombre fini de décimales)
- le type `char`{.language-} (caractère) qui contient l'ensemble des glyphes UNICODE : `"a"`{.language-}, `"b"`{.language-}, ...

{% enddefinition %}

Un type peut être vu comme un ensemble d'objets : le type entier contient tous les entiers possibles.

#### Chaîne de caractères

Le type `str`{.language-} (chaîne de caractères) représente contient l'[ensemble des mots](../../bases-théoriques/définition/#définition-mot) dont l'alphabet est l'ensemble des caractères. Ce n'est pas un type basique en tant que tel mais est tellement utilisé qu'il fait parti des types toujours présent.

#### Le vide

En algorithmie on a également coutume de se doter d'un élément vide `∅`{.language-} (nommé `None`{.language-} en python, `null`{.language-} en javascript ou encore `void`{.language-} en C) qui sera à la fois considéré comme un type ou un objet :

{% definition %}

- **le type vide** `∅`{.language-} ne contient aucun objet. On l'utilise pour des fonctions ne rendant aucun objet par exemple
- **l'objet vide** `∅`{.language-} est de tous les types (le `∅`{.language-} `int`{.language-}, `bit`{.language-}, ...). Utilisé pour simuler un souci ou un cas particulier : une fonction division pouvant rendre soit un réel soit le vide si on divise par 0 par exemple.

{% enddefinition %}

#### Taille et stockage des objets

La plupart des objets basiques sont de taille fixe :

- un booléen a une taille de 1bit (`0` pour faux, `1` pour vrai)
- un caractère a une taille de 32bit puisqu'on utilise [les caractères Unicode](https://fr.wikipedia.org/wiki/Unicode){.externe}
- un réel a une taille de 64bit si on utilise [la norme IEEE 754 double précision](https://fr.wikipedia.org/wiki/IEEE_754){.externe}

D'autres n'ont pas de limite fixée :

- les entiers 
- les chaînes de caractères


Les objets que l'on manipule doivent pouvoir être conservés pour que l'on puisse les réutiliser tout au long du programme. Cet espace de stockage, que l'on nomme **_une mémoire_**, est identifié, d'un point de vue algorithmique, à une gigantesque suite de cases adjacentes à laquelle l'algorithme peut accéder en 1 instruction et pouvant contenir **_un objet basique_**. En algorithmie, on ne se préoccupe pas vraiment de ce qu'est la mémoire : cela peut être celle de l'informaticien lecteur ou sur un ordinateur : peu importe.

{% retenir %}
On considérera toujours que l'on possède assez de mémoire pour pouvoir exécuter nos programmes.
{% endretenir %}


{% info "**Implémentation**" %}

En réalité, les objets sont stockés dans une partie de la mémoire de l'ordinateur nommée **tas**. Chaque case du tas peut contenir [1 byte](https://fr.wikipedia.org/wiki/Byte) qui correspond à 8 bits.

![tas](tas.png)

Notez que le tas peut contenir des "trous", c'est-à-dire des endroits sans objets. Enfin, dans cette implémentation réelle un entier sera stocké sur plusieurs bytes et donc plusieurs cases mémoire.

{% endinfo %}

On verra d'autres modèles de pseudo-code plus tard qui gèrent la mémoire de façon plus réaliste mais pour celui que nous présentons maintenant on considérera que :

{% retenir %}
- la taille en mémoire des objets de type basique (`bool`{.language-} (booléen), `bit`{.language-}, `int`{.language-}, `float`{.language-} et `char`{.language-}) est de 1
- la taille en mémoire d'une chaîne de caractère est le nombre de caractères qui la compose.
{% endretenir %}


### <span id="opérations"></span> Opérations

Les opérations que peuvent effectuer les pseudo-codes sont liées aux objets. On doit pouvoir :

- **_créer des objets_** : le caractère "Ç", l'entier `42`{.language-}, etc...
- **_opérer sur des objets_** : rendre la somme de deux entiers, le résultat d'une formule logique, etc
- **_afficher un objet_**. On suppose que l'on possède une opération unaire spéciale nommée `affiche`{.language-} qui affiche à l'écran (ou à n'importe quoi permettant à l'utilisateur d'avoir un retour) l'objet. Par exemple `affiche 42`{.language-} va afficher l'objet entier valant 42 à l'écran.

#### Créer des objets

La seule façon de créer un objet à partir de rien est d'écrire sa valeur. Par exemple :

```pseudocode
42
```

Crée un objet entier de valeur `42`.

On peut aussi demander à l'utilisateur de créer un objet d'un type donné (on suppose que l'utilisateur ne se trompe pas) :

```pseudocode
donne int
```

#### Opérations

{% definition %}

Une **_opération_** est une fonction dont l'espace de départ est un produit cartésien de types et l'espace d'arrivée un type donné. Elle prend en paramètre des objets (de l'espace de départ) et produit un objet du type de l'espace d'arrivée.

{% enddefinition %}

Les opérations correspondent au second moyen de créer des objets. Par exemple le booléen Vrai est créé comme résultat de l'opération `40 > 2`{.language-}. Les seules opérations définies par défaut dans tout pseudo-code sont peu nombreuses :

- pour les entiers et les réels :
  - arithmétique : addition (`x + y`{.language-}), soustraction (`x - y`{.language-}), multiplication (`x * y`{.language-}), division (`x / y`{.language-})
  - opérations usuelles comme prendre la valeur entière, la valeur absolue, ...
  - la division entière de deux nombres (`//`{.language-}) et le modulo (`mod`{.language-} ou `%`{.language-}) qui correspond au reste de la division entière
  - logique : égalité (avec le signe `==`{.language-}), plus petit que (`<`{.language-}), plus grand que (`>`{.language-}), plus petit ou égal (`≤`{.language-}), plus grand ou égal (`≥`{.language-})
  - comparaisons : maximum (`max(x, y)`{.language-}), minimum (`min(x, y)`{.language-})
- pour les caractères :
  - logique : égalité (avec le signe `==`{.language-})
- pour les chaînes de caractères :
  - logique : égalité (avec le signe `==`{.language-}), plus petit que (`<`{.language-}), plus grand que (`>`{.language-}), plus petit ou égal (`≤`{.language-}), plus grand ou égal (`≥`{.language-}) en utilisant l'[ordre du dictionnaire](https://fr.wikipedia.org/wiki/Ordre_lexicographique){.externe}
  - opération de concaténation (avec l'opérateur `+`{.language-}) : `"comment vas-tu" + " yau d’poêle ?"`{.language-} vaut la chaîne de caractères `"comment vas-tu yau d’poêle ?"`{.language-}
- opérations sur les bits et les booléens :
  - "négation logique" (non, `NON`{.language-}, `NOT`{.language-} ou encore $\neg$),
  - "et logique" (et, `ET`{.language-}, `&&`{.language-}, `AND`{.language-} ou encore $\land$), "ou logique" (ou, `OU`{.language-}, `||`{.language-}, `OR`{.language-} ou encore $\lor$)

```pseudocode
40 + 2  # rendra l'objet entier 42
```

Toutes les autres opérations devront être définies soit dans le pseudo-code (avec des fonctions, comme on va le voir) soit dans un texte avant celui-ci.

#### Affichage

Enfin, la dernière opération autorisée pour les objets est l'affichage :

```pseudocode
affiche 42
```

L'affichage est destiné, comme le commentaire, au lecteur du pseudo-code. Son but est de lui montrer des résultats intermédiaires intéressants lors de l'exécution du pseudo-code. Ce qui est affiché sort du contrôle du pseudo-code : dans l'exemple précédent l'entier 42 est affiché, le pseudo-code n'en a pas conscience.

On peut afficher plusieurs objets à la suite, par exemple :

```pseudocode
affiche 40 " plus " 2 " égal " 42
```

Qui va afficher à la suite les cinq objets : `40`{.language-}, `" plus "`{.language-}, `2`{.language-}, `" égal "`{.language-} et `42`{.language-}

## Variables

Une **_variable_** permet de retrouver un objet stocké en mémoire pour sa réutilisation :

{% definition %}
Une **_variable_** est une référence contenant l'endroit en mémoire où est stocké un objet d'**un type donné**.
{% enddefinition %}

Les variables nous permettent de manipuler les objets. Conceptuellement parlant, ce sont des **liens vers** les objets qu'elles référencent.

En algorithmie, tout comme pour les objets on ne se préoccupe pas vraiment de l'endroit où sont stockées les variables. On sait qu'elles existent : elles sont rangées dans une partie de la mémoire différente de celle des objets (les variables ne sont pas considérées comme des objets).

{% info "**Implémentation**" %}

En python, elles sont stockées dans une partie de la mémoire nommée **pile** et contiennent l'indice de la mémoire du tas où commence l'objet qu'elles référencent. Chaque variable est de taille fixe, 64bit pour les ordinateurs actuels. Ceci limite la taille maximale de mémoire que peut posséder un ordinateur : $2^{64}$byte = 18446744073709551616B = 16777216 terabytes.

![pile](pile.png)

Les variables sont stockées de façon consécutive dans la pile : toutes les variables sont créées au début de l'algorithme et sont toutes supprimées en même temps à la fin de l'algorithme.

{% endinfo %}

Concernant la taille en mémoire d'une variable, on considérera pour notre modèle de pseudo-code que :

{% retenir %}
Toutes les variables ont la même taille : 1 case mémoire.

La valeur d'une variables sera :

- soit `∅`{.language-} (correspond à une variable non associée à un objet), 
- soit l'indice dans le tableau de la mémoire où commence l'objet qui lui est associé.
{% endretenir %}

### Définition d'une variable

Avant de pouvoir être utilisée, une variable doit être définie. La ligne suivante définit une variable de nom $a$ pouvant référencer un objet de type entier :

```pseudocode
ref a int
```

La ligne précédente crée une nouvelle variable nommée `a`{.language-} pouvant référencer des objets de type entier. Dans tout le reste du pseudo-code, on sera sûr que `a`{.language-} contient une valeur entière.

{% definition %}
On utilise l'**_opérateur de définition_** `ref`{.language-} pour créer une variable. Le format général d'une définition de variable est :

```pseudocode
ref <nom de la variable> <type d'objet qu'elle peut référencer>
```

Après sa définition, la valeur de la variable est `∅`{.language-} (elle ne référence aucun objet).
{% enddefinition %}

En pseudo-code, comme le principal souci est la non-ambiguïté, une variable ne peut référencer que des objets du type spécifié lors de sa définition. 

{% info %}
Ce mode de fonctionnement n'est pas utilisé en python où une variable peut être associée à des objets de types différents, mais est suivi par la plupart des langages compilé comme java, rust ou go.

{% endinfo %}

### Affectation

Une fois la variable créée, sa valeur est `∅`{.language-} : elle est non affectée. Pour l'utiliser dans un programme il faut lui **_affecter_** un objet, par exemple pour notre variable `a`{.language-} créée précédemment :

```pseudocode
a ← 3
```

La ligne précédente associe à la variable `a`{.language-} un objet entier valant 3.

{% definition %}
On utilise l'**_opérateur d'affectation_** `←`{.language-} pour affecter une variable. Le format général de l'affectation d'un objet à une variable est :

```pseudocode
<nom de la variable> ← <objet qu'elle va référencer>
```

{% enddefinition %}
{% attention %}
On n'utilisera pas le signe `=` en pseudo-code pour l'affectation car cette opération n'est pas symétrique : à gauche une variable, à droite un objet. Mais comme le symbole `←`{.language-} n'est pas présent sur un clavier, de nombreux langages de programmation utilisent cependant `=`{.language-} pour une affectation.

{% endattention %}

L'affectation d'une variable est une opération répétable, on peut la réaffecter à un autre objet au cours du pseudo-code :

```pseudocode
ref a int

# ... des instructions

a ← 4

# ... des instructions

a ← 2
```

Après la troisième ligne, le code précédent associe la variable `a`{.language-} à un entier valant 4 et à un entier valant 2 après la cinquième ligne. Il est important de noter que :

{% retenir %}
Une variable n'est **pas** un objet, c'est un lien vers un objet qui pourra changer au cours du temps.

Après la définition d'une variable, elle n'est encore liée à aucun objet, sa valeur est **vide**. Il ne faut pas l'utiliser avant sa première affectation.
{% endretenir %}

### Utilisation

Utiliser une variable consiste à la remplacer dans l'instruction par l'objet qu'elle référence. Par exemple :

```pseudocode
ref a int
a ← 42
affiche a
```

Le code précédent affiche l'objet référencé par $a$. Il est équivalent à : `affiche 42`{.language-}.

{% definition %}
**_Utiliser_** une variable dans un code revient à la remplacer par l'objet qu'elle référence. Ce remplacement **se fait avant** l'exécution de l'instruction.

{% enddefinition %}

Regardons ceci avec quelques exemples :

```pseudocode/
ref a int
a ← 42
ref b int
b ← a
```

La ligne 4, une instruction d'affectation, s'exécute de la façon suivante :

1. on commence par retrouver l'objet à droite de l'opérateur `←`{.language-}. C'est une variable : on récupère son objet, un entier valant 42
2. on affecte cet objet à la variable à gauche de l'opérateur `←`{.language-}, la variable `b`{.language-}

Autre exemple :

```pseudocode/
ref a int
a ← 41
ref b int
b ← a + 1
```

La ligne 4, une instruction composée d'une opération puis d'une affectation, s'exécute de la façon suivante :

1. on commence par retrouver l'objet à droite de l'opérateur `←`{.language-}. C'est le résultat d'une opération :
   1. pour effectuer l'opération, il faut commencer par retrouver l'objet associé à `a`{.language-} : un entier valant 41
   2. on peut maintenant effectuer l'opération d'addition qui rend un objet de type entier valant 42
2. on affecte cet objet à la variable à gauche de l'opérateur `←`{.language-}, la variable `b`{.language-}

Attention cependant :

{% retenir %}
On ne peut utiliser une variable qu'après l'avoir affectée. Utiliser une variable qui n'a été que définie est interdit en algorithmie.
{% endretenir %}


### Type d'un objet

On aura parfois besoin de connaître le type d'un objet pour définir une variable du même type. On suppose qu'il existera toujours une opération unaire spéciale nommée `type`{.language-} qui rend le type de l'objet passé en paramètre, et que l'on pourra utiliser dans les déclarations de variables. Par exemple `type 42`{.language-} va rendre `int`{.language-}. Ceci permet d'écrire :

```pseudocode
ref a int
ref b (type a)
``` 

## <span id="tableaux"></span>Tableaux

{% definition %}
Un **_tableau_** est un conteneur nommé pouvant contenir $n$ variables **de même type**, où $n$ est la **_longueur_** ou la **_taille_** du tableau. 

La longueur d'un tableau est déterminée à sa création et ne peut être modifiée. Chaque variable du tableau peut être accédée via son **_indice_**, qui est un entier entre $0$ et $n-1$.

Si le tableau est nommé $T$ :

- $T.\mbox{longueur}$ sera égal à sa taille.
- $T[i]$ est sa variable d'indice $i$ si $0 \leq i < n$
- $T[-i]$ vaut $T[n-i]$ si $0 < i \leq n$

Le type d'un tableau est défini par le type `T`{.language-} des objets qu'il contient précédé de crochets : 

```pseudocode
[]T
```

Un tableau d'entiers est ainsi de type `[]int`{.language-}.

{% enddefinition %}

Créons un objet tableau pouvant contenir 13 variables de type entier :

```pseudocode
ref T []int  # création de la variable pouvant accueillir un tableau d'entiers

T ← [13]int  # création d'un tableau pouvant contenir 13 variables entières
```

{% definition %}

- le format général de la création d'une variable tableau : `ref nom_du_tableau []T`{.language-}
- création d'un tableau de longueur $n$ : `[n]T`{.language-}

Une fois le tableau créé, chaque case du tableau vaut `∅`{.language-}. Comme pour les variables, il **faut** les initialiser avant de les utiliser.
{% enddefinition %}

Un tableau est un mix entre variables et objets : c'est un objet contenant des variables de même type. 

{% attention %}
Lors de la définition d'un tableau on crée à la fois la variable contenant le tableau et le tableau lui-même qui est une suite de $n$ variables valant initialement `∅`{.language-}.

{% endattention %}

La remarque ci-dessus est cruciale à comprendre car cela peut entraîner tout un tas d'effets de bord incompréhensibles sinon. Pour comprendre ce qui se passe, voyez comment python gère les tableaux :

{% info "**Implémentation en python**" %}

Une façon d'implémenter cette structure en pratique est de stocker les différentes références des variables du tableau de façon contiguë en mémoire pour pouvoir y accéder rapidement pour y être lues ou modifiées :

![tableau](tableau.png)

L'implémentation en python est simple et générale mais nécessite une indirection : avant d'accéder à un objet on passe d'abord par son adresse.

{% endinfo %}

On utilise un tableau comme une collection de variables, par exemple :

```pseudocode
ref T []int
T ← [3]int

T[0] ← 41
T[1] ← 1
T[2] ← T[0] + T[1]
```

La seule opération spécifique à un tableau est sa création qui est un mix entre création d'objet et création de variable, puis on affecte ses variables avant de pouvoir les utiliser. Toutes les autres opérations sur les tableaux sont faites grâce aux opérations des objets basiques qui les composent. Il n'y a pas d'opérations spécifiques à ceux-ci :

{% retenir %}
Les opérations sur les tableaux seront toujours des opérations composées d'une suite d'opérations effectuées sur les objets basiques les constituant.
{% endretenir %}

Ainsi, on ne peut **pas** affecter un tableau à un autre. Il faut créer un nouveau tableau puis y recopier tous les éléments de l'ancien.

On considère que :

{% note %}
- créer un tableau prend autant de temps que de créer une variable (1 instruction) fois sa longueur, puisqu'il faut affecter chaque case du tableau à `∅`{.language-},
- la taille en mémoire d'un tableau est proportionnelle à la taille d'une variable fois sa longueur,
- accéder à une variable d'indice donné d'un tableau ne prend pas plus de temps que d'accéder à l'objet d'une simple variable (1 instruction) car sa position en mémoire est connue.
{% endnote %}

Les tableaux peuvent être simples comme une suite finie d'entiers ou des types plus complexes comme une matrice à 2 dimensions où chaque élément du tableau est un autre tableau (on y reviendra). 

### Tranches

On utilisera parfois, comme en python par exemple, des sous-tableaux via des **_tranches_** (**_slices_** en anglais) :

- `T[i:]`{.language-} représentera le tableau constitué des éléments de T à partir de l'indice i **inclus** jusqu'à la fin
- `T[:j]`{.language-} représentera le tableau constitué des éléments de T à partir de l'indice 0 **inclus** jusqu'à j **exclu**
- `T[i:j]`{.language-} représentera le tableau constitué des éléments de T à partir de l'indice i **inclus** jusqu'à j **exclu**

{% attention %}
Tout comme pour les tableaux, **on ne peut pas** affecter une tranche de tableau. Il faut créer un nouveau tableau puis y recopier tous les éléments de l'ancien.
{% endattention %}


### Chaînes de caractères et tableaux

Les chaînes de caractères, une fois créées, peuvent être utilisées comme un tableau composé de caractères. On peut :

- accéder à un caractère particulier en utilisant les crochets : `s[2]`{.language-} vaut le caractère `"l"`{.language-}
- connaître la longueur de la chaîne avec : `s.longueur`{.language-}

On ne peut cependant pas : modifier un caractère de la chaîne. Elle est créée une fois pour toutes.

## <span id="instruction-contrôle"></span> Instructions de contrôle

Si un des deux buts d'une instruction est de créer des objets à partir d'autres (ce que l'on vient de voir), le second but est de contrôler le flux d'instructions à exécuter. Ces instructions sont de deux types :

- [l'exécution conditionnelle d'instructions](./#tests),
- [la répétition d'instructions](./#répétition)

Ces formes d'instruction nécessitent de grouper les instructions en blocs.

## Blocs

Lier les instructions en blocs. Ce formalisme a été popularisé par python et permet de voir du premier coup d'œil un bloc et ses instructions :


{% definition %}
**_Un bloc d'instructions_** est une suite d'instructions décalées. 

```pseudocode
<type de bloc>:
    instruction 1
    instruction 2
    ...
    instruction n
```

{% enddefinition %}

Les blocs vont être utiles dans les très nombreuses situations où l'on veut, par exemple, répéter une suite d'instructions ou encore exécuter des instructions conditionnellement.

### <span id="tests"></span> Exécution conditionnelle d’instructions

On veut pouvoir exécuter des instructions si une condition logique est VRAIE :

{% definition %}

```pseudocode
si <condition logique>:
    instruction 1

    ...
    instruction n
```

{% enddefinition %}

Par exemple :

```pseudocode
si (age ≥ 18):
    affiche "Tu peux voter !"

```

Cette instruction basique suffit pour gérer toutes les exécutions de bloc conditionnelles, par exemple :

```pseudocode
si (age ≥ 18):
    affiche "Tu peux voter !"
si (age < 18):
    affiche "Tu ne peux pas jouer au Loto."

```

Mais pour plus de lisibilité on admettra plein de variantes comme la variante "si-sinon" :

```pseudocode
si <condition logique>:
    instruction 1
    ...
    instruction n
sinon:                      # <condition logique> est fausse
    instruction 1
    ...
    instruction n'
```

ou encore "si-sinon-si" :

```pseudocode
si <condition logique>:
    instruction 1
    ...
    instruction n
sinon si <autre condition logique>:
    instruction 1
    ...
    instruction n'
```

Ou tout mix de tout ça (comme "si-sinon si-sinon"), du moment que c'est clair :


```pseudocode
si <condition logique A>:
    # instructions A
sinon si <condition logique B>:
    # instructions B
sinon:                            # <condition logique A> et <condition logique B> sont fausses
    # instructions C
```

{% exercice %}
Écrire la variante `si, sinon si, sinon`{.language-pseudocode} précédente en utilisant uniquement la forme initiale `si`{.language-pseudocode}.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
si <condition logique A>:
    # instructions A
si ((NON <condition logique A>) ET (<condition logique B>)):
    # instructions B
si ((NON <condition logique A>) ET (NON <condition logique B>)):
    # instructions C
```

{% enddetails %}


{% retenir %}
Les différentes formes d'instruction conditionnelle peuvent toutes s'écrire uniquement avec la forme simple `si`{.language-pseudocode}.
{% endretenir %}

### <span id="répétition"></span> Répétitions

On doit pouvoir répéter un bloc tant qu'une condition logique est vérifiée. Les répétitions en pseudo-code vont prendre deux formes dont l'une est un cas particulier de l'autre.

#### Boucles `tant que`{.language-}

{% definition %}

```pseudocode
tant que <condition logique>:
    instruction 1
    ...
    instruction n
```

Le bloc précédent est exécuté tant que la condition logique est vraie.

{% enddefinition %}

#### Boucles `pour chaque`{.language-}

Tout comme l'exécution conditionnelle, la forme précédente suffit pour exprimer toutes les formes de répétition possibles, mais on admet la variation suivante, très utile :

```pseudocode
pour chaque <variable> de <objet pouvant être énuméré>:
    instruction 1
    ...
    instruction n
```

On exécutera alors le bloc autant de fois qu'il y a d'éléments dans l'`<objet pouvant être énuméré> `{.language-} et à chaque itération du bloc, la variable (de type de celui des objets stockés dans le tableau) vaudra un autre élément de l'objet. 

Par exemple : 

```pseudocode
pour chaque x de [1 .. 10]:
    affiche x
```


{% attention %}
Si la variable de l'itération n'est pas déclarée avant la boucle, elle sera déclarée et utilisable uniquement pendant l'exécution de la boucle.
{% endattention %}

Typiquement l'`<objet pouvant être énuméré> `{.language-} est un tableau ou une chaîne de caractères que l'on parcourt par ordre d'indice croissant. 

{% info %}
Notez que le type de la variable utilisée pour la boucle est sous-entendu mais clairement défini puisque le type de l'objet sur lequel on itère est connu.

{% endinfo %}

Les deux codes suivants sont équivalents. Le second, moins élégant, explicite le numéro de l'itération courante d'un tableau de chaînes.

Code `pour chaque`{.language-} : 

```pseudocode
pour chaque x de T:
    affiche x
```


Code `tant que`{.language-} : 

```pseudocode
ref x int

ref i int
i ← 0
tant que i < T.longueur:
    x ← T[i]
    affiche x
    i ← i + 1
```

{% retenir %}
La boucle `pour chaque`{.language-} peut s'écrire avec la boucle `tant que`{.language-}.
{% endretenir %}

Comme on va souvent faire des itérations sur des intervalles d'entiers, on utilise les notations suivantes :

- `[a .. b]`{.language-} pour représenter l'intervalle formé des entiers allant de `a` à `b` (cet intervalle peut être vide) par incrément de +1,
- `[a .. b[`{.language-} pour représenter l'intervalle formé des entiers allant de `a` à `b-1` (cet intervalle peut être vide),
- `]a .. b]`{.language-} pour représenter l'intervalle formé des entiers allant de `a + 1` à `b` (cet intervalle peut être vide),
- `]a .. b[`{.language-} pour représenter l'intervalle formé des entiers allant de `a + 1` à `b -1` (cet intervalle peut être vide),

On peut alors écrire, par exemple :

```pseudocode
ref x int
x ← 0

pour chaque i de [0 .. 10000[:
    x ← i + x
```

#### Sortir d'une boucle avant la fin

On a parfois besoin de sortir d'un bloc de boucle avant la fin de sa condition. On utilise pour cela deux instructions spéciales de sortie de boucle :

- `break`{.language-} : qui termine l'exécution du bloc
- `continue`{.language-} : qui termine l'itération courante du bloc

Ces instructions sont utiles si elles permettent de rendre le pseudo-code plus lisible, en séparant le cas général (la condition de la boucle) des cas particuliers (traités avec un `break`{.language-} ou un `continue`{.language-})

##### `break`{.language-}

Par exemple le code suivant qui trouve le pgcd (plus grand commun diviseur dont [on a déjà vu l'algorithme](../../bases-théoriques/calculabilité/#algorithme-euclide)) entre deux nombres :

```pseudocode
ref x int
ref y int

x ← donne int
y ← donne int

ref d int
d ← min(x, y)

tant que (d > 0):
    si (x mod d == 0) ET (y mod d == 0):
        break
    d ← d - 1

affiche "le pgcd entre " x " et " y " vaut " d
```

Qui est équivalent au code suivant, moins lisible :

```pseudocode
ref x int
x ← donne int

ref y int
y ← donne int

ref d int
d ← min(x, y)

ref sortir bool
sortir ← Faux

tant que (sortir == Faux) ET (d > 0):
    si (x mod d == 0) ET (y mod d == 0):
        sortir ← Vrai
    sinon:
        d ← d - 1

affiche "le pgcd entre " x " et " y " vaut " d
```

Et qui donne en python :

```python
x = int(input("Donne un entier : "))
y = int(input("Donne un entier : "))

d = min(x, y)

while (d > 0):
    if (x % d == 0) and (y % d == 0):
        break
    d -= 1

print("le pgcd entre", x, "et", y, "vaut", d)

```

##### `continue`{.language-}

Par exemple le code suivant qui va afficher tous les diviseurs de x. Le `continue`{.language-} permet d'expliciter les cas rejetés :

```pseudocode
ref x int
x ← donne int

pour chaque d de [1 .. x]:
    si (x mod d != 0):
        continue

    affiche d " divise " x
```

Qui est équivalent au code suivant, un peu moins lisible :

```pseudocode
ref x int
x ← donne int

pour chaque d de [1 .. x]:
    si (x mod d == 0):
        affiche d " divise " x
```


Et qui donne en python :

```python
x = int(input("Donne un entier : "))

for d in range(1, x + 1):
    if (x % d != 0):
        continue
    
    print(d, "divise", x)

```

##### Boucles imbriquées

{% attention %}
Les instructions `break`{.language-} et `continue`{.language-} n'agissent que dans le bloc dans lequel elles sont définies, elles n'affectent pas les boucles extérieures.
{% endattention %}

Par exemple :

```pseudocode
pour chaque x de [1 .. 3]:
    pour chaque y de [0 .. 3]:
        si x * y > 2:
            break
        affiche "x = " x "; y = " y
```

{% details "code python" %}
```python
for x in range(1, 4):
    for y in range(4):
        if x * y > 2:
            break

        print("x =", x, "; y =", y)

```

{% enddetails %}

Va afficher :

- `x = 1; y = 0`
- `x = 1; y = 1`
- `x = 1; y = 2`
- `x = 2; y = 0`
- `x = 2; y = 1`
- `x = 3; y = 0`

L'instruction `break`{.language-} ne sort que de la boucle la plus imbriquée.

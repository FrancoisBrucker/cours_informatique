---
layout: layout/post.njk
title: Pseudo-code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[La définition générale d'un algorithme](../../bases-théoriques/définition){.interne} ne spécifie rien sur les instructions à utiliser, juste qu'elles doivent être décrites en un nombre fini de mots. Un **_pseudo-code_** est une proposition d'instructions possibles pour décrire un algorithme, compréhensibles par un humain.

Ce n'est cependant pas une langue car il n'y a pas de place pour l'ambiguïté ni l'invention : tout doit y être rigoureusement défini, et chaque étape élémentaire doit être réalisable en un temps fini par un humain :

{% info %}

Rappelez-vous les trois premières règles de la [définition d'un algorithme](../../bases-théoriques/définition/#règles-générales) qui sont faciles à respecter.

{% endinfo %}

Ce n'est pas non plus un langage informatique dont le but est d'être compris par un ordinateur.

Il est communément admis que tout algorithme peut être écrit en **_pseudo-code_** :

{% note "**Thèse de Church-Turing**" %}

Tout programme (et donc algorithme) peut s'écrire sous la forme d'un pseudo-code (et réciproquement).

{% endnote %}

Notez que cette affirmation n'est pas démontrée mais que toutes les tentatives (et il y en a eu) pour infirmer cette affirmation ont été des échecs.

{% lien %}
[Thèse de Church-Turing](https://fr.wikipedia.org/wiki/Th%C3%A8se_de_Church).
{% endlien %}

La thèse de Church-Turing a été initialement formulée pour les Machines de Turing mais, nous le verrons pseudo-code et machines de Turing sont deux notions équivalentes.

## <span id="règles"></span> Éléments de pseudo-code

Un pseudo-code est une succession de lignes qui seront exécutées **_en séquence_** les unes à la suite des autres. Chaque ligne est composée d'une instruction qu'il faut réaliser en entier avant de passer à la ligne suivante.

Le but de chaque instruction est de manipuler des objets, auxquels on peut accéder via des variables.

### <span id="objets-basique"></span> Objets et variables

On doit pouvoir manipuler et stocker des _objets_ pour faire fonctionner nos algorithmes ce qui nécessite de posséder un espace de stockage, que l'on nomme **_une mémoire_**. D'un point de vue algorithmique, on identifie celle-ci à une gigantesque suite de cases adjacentes à laquelle l'algorithme peut accéder en 1 instruction et pouvant contenir **_un objet basique_** ou **_une variable_**.

#### Objets basiques

Les objets que nous aurons directement à notre disposition sans avoir besoin de les définir sont appelés **_objets basiques_** et sont au nombre de six :

- le vide (nommé `None`{.language-} en python, `null`{.language-} en javascript ou encore `void`{.language-} en C)
- les booléens (vrai et faux)
- les nombres entiers
- les nombres réels
- les nombres complexes
- les caractères

Tous les autres types d'objets que l'on peut créer seront des compositions de ces 6 types d'objets élémentaires (un point en 3D par exemple est constitué de 3 réels).

Les instructions liées à ces objets sont de deux ordres. On doit pouvoir :

- **_créer des objets_**
- **_opérer sur ces objets_** :
  - opérations sur les entiers et/ou réels :
    - arithmétique : addition (`+`{.language-}), soustraction (`-`{.language-}), multiplication (`*`{.language-}), division (`/`{.language-})
    - opérations usuelles : prendre la valeur entière, valeur absolue, le modulo
    - logique : égalité (avec le signe `==`{.language-} ou `=`{.language-}), plus petit que (`<`{.language-}), plus grand que (`>`{.language-}), plus petit ou égal (`≤`{.language-}), plus grand ou égal (`≥`{.language-})
  - opérations sur les booléens : "négation logique" (non, `NOT`{.language-}, $\neg$), "et logique" (et, `&&`{.language-}, `AND`{.language-}), "ou logique" (ou, `||`{.language-}, `OR`{.language-})

> TBD ici attention en pratique, on utilise des entier fini de taille fixe (64bits) sinon impossible d'avoir 1 opération simple pour les manipuler.

#### Variables

On doit pouvoir affecter des objets à des **_variables_**.

{% note "**Définition**" %}
Une **_variable_** est un nom auquel est associé un objet.
{% endnote %}

Les instructions autorisées sur les variables sont :

- **_l'affectation_** : `a = 3`{.language-} défini le nom `a`{.language-} (appelé _variable_) qui est associé à un entier valant `3`{.language-}. (vous verrez parfois utilisé $a \leftarrow 3$ à la place de $a = 3$ pour qu'il n'y ait pas de confusion si l'on utilise `=`{.language-} pour l'égalité)
- **_la lecture_**. Si j'ai affecté `3`{.language-} à la variable `a`{.language-}, je dois pouvoir l'utiliser, par exemple en écrivant `b = a * 3`{.language-}
- **_l'affichage à l'écran_**. Pour permettre un retour à l'utilisateur de ce qu'à produit le pseudo-code.

#### <span id="str"></span>Chaînes de caractères

Une **_chaîne de caractères_** est un objet constitué d'une suite finie de caractères $c_0c_1\dots c_{n-1}$ stockées de façon et contiguë en mémoire.

D'un point de vue complexité, on considérera que :

- la création d'une chaîne de caractère prend 1 instruction : `"salut"`{.language-} crée la chaîne contenant les caractères `"s"`{.language-}, `"a"`{.language-}, `"l"`{.language-}, `"u"`{.language-} et `"t"`{.language-} de façon contiguë en mémoire.
- l'affectation d'une chaîne de caractères à une variable prend 1 instruction : `s = "salut"`{.language-} prend 2 instructions, une pour la création et une pour l'affectation.
- l'accès à un caractère particulier se fait en 1 instruction et en utilisant les crochets : `s[2]`{.language-} vaut le caractère `"l"`{.language-}

{% info %}
On considère que créer une chaîne prend 1 instruction car cette chaîne est une constante. [On justifiera ceci proprement plus tard](../../complexité-calculs/O-pour-l-algorithmie).
{% endinfo %}

Les chaînes de caractères sont non mutables :

{% attention %}
On ne peut pas changer un caractère d'une chaîne de caractères.
{% endattention %}

#### <span id="tableaux"></span>Tableaux

Un **_tableau_** est un objet qui en contient d'autres.

{% note "**Définition**" %}
Un **_tableau_** est un conteneur nommé pouvant contenir $n$ variables. $n$ est la **_longueur_** ou la **_taille_** du tableau. La taille d'un tableau est déterminée à sa création et ne peut être modifiée.

Chaque variable du tableau peut être accédée via son **_indice_**, qui est un entier entre $0$ et $n-1$ : si le tableau est nommé $t$, $t[i]$ est sa variable d'indice $i$.

{% endnote %}

Comme une chaîne de caractères, les différentes variables du tableaux sont stockées de façon contiguë en mémoire pour pouvoir y accéder rapidement, mais contrairement à une chaîne de caractères qui contient uniquement des caractères constants, chaque élément du tableau est une variable et peut donc être affectée ou modifiée.

Les tableaux peuvent être simples comme une suite finie d'entiers ou des types plus complexes comme une matrice à 2 dimensions où chaque élément du tableau est un autre tableau.

D'un point de vue complexité, on considérera que :

- la création d'un tableau prend 1 instruction : `[1, 3, x]`{.language-} crée un tableau qui affecte à sa variable :
  - d'indice 0 un entier valant 1
  - d'indice 1 un entier valant 3
  - d'indice 2 l'objet associé à la variable `x`{.language-}
- l'affectation d'un tableau à une variable prend 1 instruction : `t=[1, 3, x]`{.language-} prend 2 instructions une pour la création et une pour l'affectation
- l’accès à un élément particulier du tableau se fait en 1 instruction et en utilisant les crochets : `t[2]`{.language-} vaut le caractère `"l"`{.language-}

{% info %}
On considère que créer un tableau prend 1 instruction car celui-ce est de taille fixée. [On justifiera ceci proprement plus tard](../../complexité-calculs/O-pour-l-algorithmie).
{% endinfo %}

### <span id="instruction-basique"></span> Instruction basique

Le but d'une instruction est de transformer des objets. On utilisera un nombre restreint d'instructions, appelées instructions basiques, dont la composition permet (a priori) de réaliser toutes les instructions imaginables.

Il y a 3 types d'instructions basiques :

- [les opérations sur les objets basiques](./#objets-basique){.interne} qu'on a déjà vu,
- [l'exécution conditionnelle d'instructions](./#tests){.interne}
- [la répétition d'instructions](./#répétition){.interne}

Les deux dernières formes d'instruction nécessitent de grouper les instructions en blocs.

#### Blocs

Lier les instructions en blocs. On va utiliser ici le formalisme de python pour définir un bloc :

```text
type de bloc:
    instruction 1
    instruction 2
    ...
    instruction n
```

On décale les instructions du bloc de sa définition. C'est un truc clair qui permet de voir du premier coup d'œil les instructions d'un bloc.

#### <span id="tests"></span> Exécution conditionnelle d’instructions

On veut pouvoir exécuter un bloc de code si une condition logique est vérifiée :

```text
si (condition logique) est vraie:
    instruction 1
    ...
    instruction n
```

Cette instruction basique peut avoir plein de variantes comme :

```text
si (condition logique) est vraie:
    instruction 1
    ...
    instruction n
sinon:
    instruction 1
    ...
    instruction n'
```

ou encore :

```text
si (condition logique) est vraie:
    instruction 1
    ...
    instruction n
sinon si (autre condition logique) est vraie:
    instruction 1
    ...
    instruction n'
```

Ou tout mix de tout ça, du moment que c'est clair !

{% info %}
On peut dériver toutes les variantes de la forme initiale.
{% endinfo %}

#### <span id="répétition"></span> Répétition

On doit pouvoir répéter un bloc tant qu'une condition logique est vérifiée (boucle _while_):

```text
tant que (condition logique) est vraie:
    instruction 1
    ...
    instruction n
```

Il existe une variation de ce bloc très utile (boucle _for_):

```text
pour chaque élément x d'un tableau:
    instruction 1
    ...
    instruction n
```

On exécutera alors le bloc autant de fois qu'il y a d'éléments dans le tableau et à chaque itération du bloc, la variable `x` vaudra un autre élément du tableau. On prendra les éléments du tableau par indice croissant.

{% info %}
On peut dériver la variante `pour chaque`{.language-} de la forme initiale `tant que`{.language-}.
{% endinfo %}

### <span id="complexité"></span> Complexité

La complexité d'un pseudo-code est le nombre d'instructions basiques utilisées pour l'exécuter. La complexité d'un bloc d'instruction est égale à la somme des complexités des instructions qui le composent.

Par exemple le pseudo-code suivant :

```text#
x = 30
if ((x > 12) AND (x < 36)):
    z = x * "coucou"
```

1. Création de l'entier valant 30 : 1 instruction
2. on affecte l'entier à x : 1 instruction
3. Pour faire cette instruction il faut :
   - faire `x > 12`{.language-}. Pour cela :
     - on crée l'entier valant 12 : 1 instruction
     - on récupère la valeur de `x`{.language-} : 1 instruction
     - on effectue la comparaison : 1 instruction
   - faire `x < 36`{.language-}. Pour cela :
     - on crée l'entier valant 36 : 1 instruction
     - on récupère la valeur de `x`{.language-} : 1 instruction
     - on effectue la comparaison : 1 instruction
   - faire l'instruction `AND`{.language-} : 1 instruction
   - faire le `if`{.language-} : 1 instruction
4. on commence par récupérer la valeur de `x`{.language-} (1 instruction), on crée la chaîne (1 instruction) puis affecte le résultat d'une opération élémentaire (2 instructions) : donc un total de 4 instructions

Un nombre total d'instructions de 14.

### Nom des termes utilisés ?

Leurs noms importent peu, seuls leurs fonctions sont importantes. Vous pouvez donc utiliser les mots qui vous plaisent, du moment qu'ils sont compréhensible pour vous et — surtout — pour votre lecteur. Le plus souvent, on utilisera un mix de python et de français, ou d'anglais.

Les trois pseudo-code suivant sont ainsi équivalent :

```python
for i in range(10):
    affiche à l'écran i
```

```python
pour chaque entier i allant de 0 à 9:
    print(i)
```

```c
for (i=0 ; i < 10 ; i++) {
    printf(i);
}
```

## Pseudo-code

Le pseudo-code d'un algorithme va contenir, en plus de ses instructions, un nom, des entrées et souvent une sortie. Par exemple :

<div id="problème-recherche"></div>

```text
Nom : recherche
Entrées :
    t : un tableau d'entiers
    x : un entier
Programme :
    pour chaque élément e de t:
        si e == x:
            Retour vrai
    Retour faux
```

ou de manière équivalente, en un mélange de python et de français :

```python#
def recherche(t, x):
    pour chaque élément e de t:
        si e == x:
            return vrai
    return faux
```

Ou encore, complètement en python :

<div id="fonction-recherche"></div>

```python#
def recherche(t, x):
    for e in t:
        if e == x:
            return True
    return False
```

Ceci permet ensuite de définir des fonctions pour écrire des algorithmes de façon plus concise.

### Fonctions

Une fonction est un algorithme. Une fois que sa complexité est connue, on peut l'utiliser comme une instruction dans un pseudo-code.

```text
nom(entrée 1, ..., entrée n)
```

{% attention %}
Ne confondez pas `nom`{.language-} qui est l'algorithme et `nom(a, b)`{.language-} qui est le résultat de son exécution avec les paramètres `a`{.language-} et `b`{.language-}
{% endattention %}

Si l'algorithme a un retour, on peut directement l'utiliser, en l'affectant à une variable par exemple :

```text
variable = nom(entrée 1, ..., entrée n)
```

{% info %}
Les fonctions nous donnent accès à la récursivité : Il suffit que notre pseudo-code s'appelle lui-même comme une fonction.
{% endinfo %}

Si on veut utiliser le pseudo code _recherche_ défini plus haut, cela pourrait être une instruction du type : `trouve = recherche(tab, 3)`{.language-}. On affecte la sortie de l'algorithme `recherche`{.language-} avec comme paramètres `tab`{.language-} (le tableau d'entier) et `3`{.language-} (un entier) à la variable `trouve`{.language-}.

Il est important de voir que lorsque l'on exécute une fonction, les variables qu'elle crée existeront dans un espace à elle, pas dans celui du pseudo-code appelant. Ainsi dans le code suivant :

```python#
e = 4
t = [1, 2, 6]
trouve = recherche(t, 6)
affiche à l'écran e
```

On affichera bien 4 à l'écran et pas 6 (le nom de variable `e`{.language-} défini dans recherche reste dans recherche).

{% attention %}
Lorsque l'on calcule la complexité d'un pseudo-code utilisant des fonctions, il faut compter le nombre d'instructions de l'exécution des fonctions !
{% endattention %}

Prenons par exemple le code précédent et comptons les instructions utilisées ligne à ligne :

1. création d'un objet et affectation à une variable : 2 instructions
2. création d'un tableau et affectation à une variable : 2 instructions
3. affectation d'une variable (1 instruction) plus l'exécution de la fonction recherche (ligne à ligne) :
   1. affectation des paramètres :
      1. trouver les objets à mettre en paramètres :
         - pour le premier paramètre il faut trouver l'objet associé à t : 1 instruction
         - pour le second paramètre, l'objet est à créer : 1 instruction
      2. affecter les paramètres aux variables de la fonction :
         - affectation du premier paramètre à la variable locale t : 1 instruction
         - affectation du second paramètre à la variable locale e : 1 instruction
   2. une boucle de 3 itérations
   3. un test
      - on trouve les objets associées à t et e : 2 instructions
      - on teste l'égalité : 1 instruction
      - on fait le `if`{.language-} : 1 instruction
   4. on arrive à cette ligne à la troisième itération : 1 instruction
4. afficher quelque chose à l'écran :
   - 1 instruction pour trouver l'objet à afficher
   - 1 instruction pour trouver l'afficher

Au total on eu besoin de $2+2+1+\underbracket{(1+1+1+1+3 \cdot (2+1+1) + 1)}_{\mbox{recherche(t, 6)}} + 1 + 1$
instructions c'est à dire $24$ instructions.

### Signature d'une fonction

Lorsque l'on défini un algorithme ou un pseudo-code on explicite souvent le type des objets en entrées et en sortie. Par exemple [le problème recherche](./#problème-recherche) nécessite un tableau d'entier et un entier en paramètre et sa sortie est un booléen. Lorsque l'on écrit une fonction, en particulier en python on a pas toujours l'habitude (ni le besoin) de le faire, mais on peut le spécifier en utilisant **_les signatures de fonctions_**

{% note "**Définition**" %}
Une signature de fonction associe :

- son type à chaque paramètre (précédé d'un `:`)
- le type de sortie (précédé d'un `->`)
  {% endnote %}
  {% info %}
  Par exemple, la signature de [la fonction recherche](./#fonction-recherche) est :

```python
recherche(t: [int], x: int) -> bool
```

{% endinfo %}

On ne peut bien sur utiliser de signature que lorsque les entrées et les sorties sont de types parfaitement définis, ce qui n'est pas toujours le cas.

### Instructions avancées

Si l'on devait à chaque pseudo-code redéfinir tout les algorithmes qu'on utilise ce serait vraiment fastidieux. On utilise souvent des fonctions non basiques (comme l'affichage à l'écran qu'on a déjà vu) ou des structures plus élaborées (les listes par exemples qui sont des extensions des tableaux). Il faudra cependant toujours connaître les complexités de ce qu'on utilise.

Par exemple pour les listes, qui sont des tableaux redimensionnables :

- complexité d'ajout d'un élément à la fin de la liste : coût de 1 instruction
- complexité de l'ajout d'un élément pas à la fin de la liste : coût de la taille de la liste instructions
- complexité de la suppression d'un élément à la fin de la liste : coût de 1 instruction
- complexité de la suppression d'un élément pas à la fin de la liste : coût de la taille de la liste instructions
- usage comme un tableau : 1 instruction

Si vous utilisez des méthodes d'objets comme vous avez l'habitude de le faire en python (comme une `ma_liste.index("?")`{.language-}, `x in ma_chaîne_de_caractères`{.language-}) ou des structures compliquées (télécharger un fichier d'internet) vous avez le droit mais vous **devez** en connaître le coût : la complexité, les cas d'usage (comme être connecté à internet), etc.

## Comment écrire du pseudo-code

Le pseudo-code est une représentation d'un algorithme. Son but est de :

- démontrer que l'algorithme fait bien ce qu'on pense qu'il fait
- calculer ses performances :
  - nombre d'instructions utilisées
  - nombre de cases mémoire utilisées

Pour réaliser cela le plus simplement possible, on voudra **toujours** :

- qu'il soit lisible,
- qu'il soit juste,
- en connaître les performances.

### Lisible

Le but d'un algorithme papier est d'être compris. On utilisera pour l'écrire une série de règles compréhensibles par tout le monde : le pseudo-code. Ce n'est ni une langue ni un langage.

préférez des noms de variables explicites et n'hésitez pas à séparer votre pseudo-code en fonctions pour qu'il soit plus clair.

{% note "**N'oubliez pas**" %}
Les fonctions doivent être décrites si elles ne sont pas immédiatement compréhensibles.
{% endnote %}

### Preuve

On **démontrera** le fonctionnement de l'algorithme en utilisant des preuves mathématiques.

### Performances

On calculera la complexité de l'algorithme :

- nombre d'instructions
- place en mémoire

Ces complexités dépendent des paramètres de l'algorithme et, parfois de circonstances extérieures comme l'état du réseau par exemple.

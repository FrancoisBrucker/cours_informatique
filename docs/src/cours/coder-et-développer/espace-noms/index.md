---
layout: layout/post.njk
title: Espace de noms

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Python stocke ses variable dans un objet appelé **_espace de noms_**. Une variable a un nom et est associé à un objet python. Il est important de dissocier le nom de l'objet pour une variable et surtout la variable de l'objet qu'elle représente.

## Variable et objet

La quasi-entièreté des langages actuellement sont dit _objet_. C'est à dire que :

- ce que manipule un programme est appelé objet.
- les variables représentent les objets. On dit aussi parfois qu'une variable est une **_référence_** d'un objet.

Ces langages permettent de créer des programmes en utilisant uniquement les deux mécanismes ci-dessous :

{% note %}
Pour qu'un programme objet fonctionne, on a besoin de deux mécanismes :

- un moyen de stocker des données et de les manipuler (les objets et leurs méthodes)
- un moyen d'y accéder (les variables)

{% endnote %}

### Objets

On y reviendra, mais pour l'instant considérez qu'un objet est une structure de donnée générique permettant de gérer tout ce dont à besoin un programme :

- des données
- des fonctions
- des modules
- ...

Tout est objet dans un langage objet.

### Variables

Les variables sont des références aux objets. Pour ce faire, on utilise l’opérateur d’affectation `=`{.language-} :

```txt
variable = objet
```

A gauche de l’opérateur `=`{.language-} se trouve une **variable** (en gros, quelque chose ne pouvant commencer par un nombre) et à droite un **objet**. Dans toute la suite du programme, dès que le programme rencontrera le nom, il le remplacera par l'objet.

{% attention %}
Un variable n'est **PAS** une chaîne de caractères. Une chaîne de caractères est un objet alors qu’une variable est un alias vers un objet.
{% endattention %}

Il est important de comprendre que l’opérateur d’affectation `=`{.language-} n’est pas symétrique. À gauche, des variables et à droite, des objets.

{% note %}
Une variable n'est **pas** l'objet, c'est une référence à celui-ci
{% endnote %}

La variable peut être vue comme un **nom** de l'objet à ce moment du programme. Un objet pourra avoir plein de noms différents au cours de l'exécution du programme, voire plusieurs noms en même temps.

Pour s'y retrouver et avoir une procédure déterministe pour retrouver les objets associés aux variables, voire choisir parmi plusieurs variables de même nom, elles sont regroupées par ensembles — nommés **espaces de noms** — hiérarchiquement ordonnés.

## <span id="espace-noms"></span> Espaces de noms

Les espaces de noms sont des objets de python qui nous permettent de lier variables et objets :

- on considère que les objets sont stockés dans _**l'espace des objets**_ : cet espace est **unique**
- on accède aux objets via leurs noms, eux même stockés dans des _**espaces de noms**_ qui sont des objets comme les autres : il y a de **nombreux** espaces de noms.

Pour chaque _espace de noms_ :

- il ne peut y avoir 2 noms identiques dans un même espace de noms
- à chaque nom est associé un objet
- certains espaces de noms possèdent un parent


{% info %}
Pour expliciter comment tout ça se passe, on va se concentrer sur le [langage python](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces), mais la procédure est similaire pour les autres langages à objets.
{% endinfo %}

Lorsque l'on exécute un programme, un premier espace de noms est créé :

{% note %}
Au démarrage d'une exécution d'un programme, l'espace de noms principal, nommé `global`{.language-} est créé. C'est à partir de lui que toutes les variables doivent être atteintes.
{% endnote %}

Au départ, il ne contient rien, à part des noms commençant et finissant par `__`{.language-}, qui sont utilisés par python.

{% info %}
Pour voir les noms définit dans l'espace de noms global, on utilise en python la fonction `globals()`{.language-} qui rend un dictionnaire contenant le nom et l'objet associé à chaque variable.

Au démarrage del'interpréteur, il n'y pas grand chose dans globals :

```python
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}

```

{% endinfo %}

A tout moment de l'exécution d'un programme, un espace de noms pourra être créé. En revanche :

{% note %}
A tout moment du programme, on pourra créer un nouvel espace de noms : de nombreux espaces de noms pourront être définis, mais il existera toujours **un** espace de noms courant où l'on créera les variables et où on cherchera les noms par défaut.
{% endnote %}

On donnera dans la suite de cette partie des exemples qui permettront de mieux comprendre ce processus.

{% info %}
Pour voir les noms définis dans l'espace de noms courant, on utilise en python la fonction `locals()`{.language-}.
{% endinfo %}

### Noms et variables

Prenons plusieurs exemples, qui illustreront les cas principaux.

#### Association objet et noms

Considérons le programme suivant :

```python
x = 1
y = 1
```

Exécutons le ligne à ligne :

1. avant l'exécution de la première ligne :
   1. on a un unique espace de noms (`global`{.language-}) qui est l'espace courant (en vert sur la figure)
      ![cas-1-1](cas-1-1.png)
2. on exécute la première ligne. Elle s'exécute ainsi :
   1. on commence à droite du `=`{.language-} : on crée un objet de type entier
   2. on crée le nom `x`{.language-} dans l'espace de noms courant (ici `global`{.language-}) et on lui affecte l'objet.
      ![cas-1-2](cas-1-2.png)
3. on exécute la deuxième ligne. Elle s'exécute ainsi :
   1. on commence à droite du `=`{.language-} : on crée un objet de type entier
   2. on crée le nom `y`{.language-} dans l'espace de noms courant (ici `global`{.language-}) et on lui affecte l'objet.
      ![cas-1-3](cas-1-3.png)

A la fin du programme, il y a **2 objets entiers différents** (même si tous les 2 valent 1), dont les noms sont, dans l'espace de noms global, respectivement `x`{.language-} et `y`{.language-}.

#### Réutilisation du même nom

```python
x = 1
x = 3
```

Exécutons le ligne à ligne :

1. avant l'exécution de la première ligne :
   1. on a un unique espace de noms (`global`{.language-}) qui est l'espace courant (en vert sur la figure)
      ![cas-1-1](cas-1-1.png)
2. on exécute la première ligne. Elle s'exécute ainsi :
   1. on commence à droite du `=`{.language-} : on crée un objet de type entier
   2. on crée le nom `x`{.language-} dans l'espace de noms courant (ici `global`{.language-}) et on lui affecte l'objet.
      ![cas-1-2](cas-1-2.png)
3. on exécute la deuxième ligne. Elle s'exécute ainsi :
   1. on commence à droite du `=`{.language-} : on crée un objet de type entier
   2. on crée le nom `x`{.language-} dans l'espace de noms courant (ici `global`{.language-}) et on lui affecte l'objet.
      ![cas-2-1](cas-2-1.png)

Notez que le fait qu'un nom identique existe déjà n'est pas important. Le nouveau nom écrase l'autre :

{% note %}
Dans un espace de noms, chaque nom est différent. Réutiliser le même nom remplace le nom précédent.
{% endnote %}

Le programme a créé **2 objets** (un entier valant 1 et un entier valant 3), mais à la fin de la deuxième ligne du programme, seul l'entier valant 3 a un nom (`x`{.language-}).

Comme il est maintenant impossible d'accéder à l'entier valant `1`{.language-} : python le détruit.

![cas-2-2](cas-2-2.png)

{% note %}
Tout objet qui n'est plus référencé par une variable est détruit par un mécanisme appelé [ramasse-miettes](<https://fr.wikipedia.org/wiki/Ramasse-miettes_(informatique)>).
{% endnote %}

#### Un objet peut avoir plusieurs noms

```python
x = 1
y = x
```

Exécutons le ligne à ligne :

1. avant l'exécution de la première ligne :
   1. on a un unique espace de noms (`global`{.language-}) qui est l'espace courant (en vert sur la figure)
      ![cas-1-1](cas-1-1.png)
2. on exécute la première ligne. Elle s'exécute ainsi :
   1. on commence à droite du `=`{.language-} : on crée un objet de type entier
   2. on crée le nom `x`{.language-} dans l'espace de noms courant (ici `global`{.language-}) et on lui affecte l'objet.
      ![cas-1-2](cas-1-2.png)
3. on exécute la deuxième ligne. Elle s'exécute ainsi :
   1. on commence à droite du `=`{.language-} : on cherche le nom `x`{.language-} dans l'espace de noms courant. On le trouve et on lui substitue son objet (un entier valant 1)
   2. on crée le nom `x`{.language-} dans l'espace de noms courant (ici `global`{.language-}) et on lui affecte l'objet.
      ![cas-3-1](cas-3-1.png)

Le programme n'a crée qu'un objet (un entier valant 1) et il a deux noms (`x`{.language-} et `y`{.language-}) :

{% note %}
Dans un même espace de noms, un même objet peut être référencé plusieurs fois, sous plusieurs noms différents.
{% endnote %}

Les noms ne sont jamais utilisés en tant que tel. Dès qu'ils sont rencontrés, ils sont immédiatement remplacés par les objets qu'ils référencent.

{% note %}
Pour exécuter une instruction, on commence **toujours** par remplacer les variables par les objets qu'elles référencent.
{% endnote %}

La remarque précédente permet de comprendre mieux ce que fait le code suivant (et pourquoi cela fonctionne) :

```python
x = 1
y = 3
x, y = y, x
```

{% details "solution" %}
Il échange les objets référencés par `x`{.language-} et `y`{.language-}.

Cela marche car on commence par remplacer les variables par les objets (la droite du `=`{.language-}) avant de créer les variables (la gauche du `=`{.language-}).
{% enddetails %}


## Port d'attache d'un espace de noms

Les espaces de noms sont des objets spéciaux qui ne peuvent vivre indépendamment. Il sont toujours rattachés à leur contexte qui est soit :

- le programme principal : c'est le cas de l'espace de nom globals
- une fonction : crée lors de l'appel d'une fonction pour gérer ses paramètre et variables locales.
- un module : les espaces de noms crées après un import

### Fonctions

L'exécution d'une fonction est un moment où un espace de noms est créé. Cela se passe selon le processus suivant :

{% note %}
Lorsque l'on exécute une fonction on procède comme suit :

1. on crée un nouvel espace de noms $F$
2. l'espace de noms courant est affecté au parent de $F$
3. $F$ devient le nouvel espace de noms courant.
4. on affecte les paramètres de la fonction à leurs noms
5. on exécute ligne à ligne la fonction
6. le parent de $F$ devient le nouvel espace de noms courant
7. on supprime l'espace de noms $F$

{% endnote %}

#### Exécution d'une fonction

```python#
def f(x):
   i = 2 * x
   return i + 3

i = 2
x = f(i)
```

Exécutons le ligne à ligne :

1. avant l'exécution de la première ligne :
   1. on a un unique espace de noms (`global`) qui est l'espace courant (en vert sur la figure)
      ![cas-1-1](cas-1-1.png)
2. la ligne 2 définit une fonction de nom `f`{.language-} qui est ajouté à l'espace de noms courant.
   ![cas-4-1](cas-4-1.png)
3. on passe directement à la ligne 5 puisque les lignes 3 et 4 sont le contenu de la fonction.
   1. Cette ligne crée un objet entier (valant 2) et l'affecte au nom `i`{.language-}.
      ![cas-4-2](cas-4-2.png)
4. la ligne 6 est encore une affectation. On commence par trouver l'objet à droite du `=` c'est le résultat de `f(i)`{.language-}. Il faut donc exécuter la fonction `f`{.language-} pour connaître cet objet :
   1. on cherche l'objet associé à `i`{.language-} qui sera le (premier) paramètre de la fonction
   2. on crée un espace de noms qui devient l'espace de noms courant :
      1. l'ancien espace de noms courant devient son parent
         ![cas-4-3](cas-4-3.png)
   3. on affecte le premier paramètre de `f`{.language-} au nom `x`{.language-} (le nom du premier paramètre de `f`{.language-} lors de sa définition)
      1. les nouveaux noms sont **toujours** créés dans l'espace de noms courant
         ![cas-4-4](cas-4-4.png)
   4. on exécute la ligne 2 qui est la première ligne de la fonction `f`{.language-} :
      1. on crée un objet entier (valant 4) qui est le résultat de l'opération à droite du `=`{.language-} (notez que le nom `x`{.language-} est bien défini dans l'espace de noms courant) et on l'affecte au nom `i`{.language-} dans l'espace de noms courant
         ![cas-4-5](cas-4-5.png)
   5. on exécute la ligne 3 :
      1. on crée l'objet résultant de l'opération somme (un entier valant 7)
      2. la fonction est terminée, son espace de noms courant est détruit
      3. l'espace de noms courant devient le parent de l'espace de noms détruit
         ![cas-4-6](cas-4-6.png)
      4. on rend l'objet résultat de la fonction
   6. la droite du signe `=`{.language-} de la ligne 6 est trouvée (c'est un entier valant 7) et il est affecté à la variable `x`{.language-} de l'espace de noms courant (qui est à nouveau `global`)
      1. ![cas-4-7](cas-4-7.png)
      2. les objets sans nom sont détruits
         ![cas-4-8](cas-4-8.png)

#### Espaces de noms parent

L'espace de noms parent sert lorsque l'on cherche un nom qui n'est pas défini dans l'espace de noms courant :

{% note %}
Si un nom est recherché, mais que celui-ci n'est défini dans l'espace de noms courant, le nom est recherché dans l'espace de noms parent de l'espace courant.
{% endnote %}

```python#
def f(x):
   i = C * x
   return i + 3

C = 2
i = 2
x = f(i)
```

Lors de l'exécution de la fonction `f`{.language-} (instruction de la ligne 7), sa première ligne cherche la variable nommée `C`{.language-}. On se trouve dans cet état là :

![cas-5-1](cas-5-1.png)

La variable `C`{.language-} n'existe pas dans l'espace de noms courant (celui de `f`{.language-}), le programme va alors chercher dans l'espace de noms parent s'il existe. Ici c'est le cas puisque l'espace parent de `f`{.language-} est `global` dans lequel `C`{.language-} est défini : le programme ne produit donc pas une erreur et trouve le bon objet.

{% note %}
Les variables sont **toujours** créées dans l'espace de noms courant, mais leur recherche remonte de parent en parent jusqu'à la trouver.
{% endnote %}

### Import de module

Lorsque l'on importe un fichier, un espace de noms est créé et le fichier entier est lu. Lors de sa lecture, les noms définis sont placés dans cet espace.

{% note %}
Les modules possèdent un espace de noms qui contient les variables qui y sont définies
{% endnote %}

```python
import random
from math import log

print(log(random.randrange(1, 43)))
```

Avant l'exécution de l'instruction `print`{.language-} on est dans cet état :

![cas-6-1](cas-6-1.png)

On accède à l'espace de noms du module par la notation pointée : `random.randrange`{.language-} signifie le nom `randrange`{.language-} dans l'espace de noms de `random`{.language-}.

{% info %}
Notez que le module `math`{.language-} n'a plus d'espace de noms associé puisque l'on a juste _récupéré_ un nom qui y est défini.
{% endinfo %}

## <span id="notation-pointée"></span> Notation pointée

En python, (pratiquement) tout a un espace de nom. On s'en sert dès qu'on utilise la notation pointée.

on l'a vue pour les modules, mais c'est aussi vrai pour les objets. En considérant le code suivant :

```python
c = "coucou"
c2 = c.uppercase()
```

Le nom `uppercase`{.language-} est défini dans l'espace de noms de la chaîne de caractères `"coucou"`{.language-} (en fait, c'est dans sa classe, mais on le verra précisément plus tard).

C'est une notation **très puissante** ! Il ne faut pas avoir peur de chaîner ces notations. On appelle cela des chaînages :

```python
a.b.c.d()
```

Signifie :

1. On exécute `d`{.language-} qui est dans l'espace de noms de `a.b.c`{.language-}
2. `c`{.language-} est dans l'espace de noms de `a.b`{.language-}
3. `b`{.language-} est dans l'espace de noms de `a`{.language-}
4. `a`{.language-} est dans l'espace de noms courant

---
layout: page
title:  "espaces de noms"
category: cours
tags: informatique cours 
authors: 
  - François Brucker
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [coder]({% link cours/theorie-pratiques-algorithmique/coder/index.md %}) / [programmation objet]({% link cours/theorie-pratiques-algorithmique/coder/programmation-objet/index.md %}) / [mémoire et espace de noms]({% link cours/theorie-pratiques-algorithmique/coder/programmation-objet/memoire-et-espace-noms.md %})
{: .chemin}

On montrer comment on peut gérer les variables dans un programme, et l'utilité des espaces de noms (en prenant l'exemple de python) pour le faire.

Nous ne rentrerons pas dans les détails, la gestion de la mémoire est quelque chose de compliqué. Nous présenterons juste ici les caractéristiques fondamentales et les conséquences que cela a sur les variables et les objets.

## la mémoire

On peut considérer la mémoire d'un ordinateur comme un long tableau de taille (habituellement mesurée en [octet](https://fr.wikipedia.org/wiki/Octet)) fixe, dépendant de votre ordinateur.

![mémoire]({{ "/assets/cours/algorithmie/poo/memoire.png" | relative_url }}){:style="margin: auto;display: block;"}

> Cette taille est souvent plus grande que votre [RAM](https://fr.wikipedia.org/wiki/M%C3%A9moire_vive), grâce au mécanisme du [swap](https://fr.wikipedia.org/wiki/Espace_d%27%C3%A9change).

Comme un programme n'est jamais seul à être exécuté sur un ordinateur et que — pour des raisons de sécurité — un programme $A$ ne doit pas pouvoir accéder à la mémoire utilisée par un programme $B$ :

> Le **système d'exploitation** est le seul à pouvoir accéder à une case donnée de la mémoire via son indice, comme on pourrait le faire avec un tableau normal. Un programme spécifique en revanche, ne peut accéder qu'à la partie de la mémoire qui lui a été allouée par le système d'exploitation
{: .note}

### accéder/allouer de la mémoire

Comme le système d'exploitation alloue de la mémoire et que plusieurs programmes se la partagent, il est uniquement possible pour un programme donné :

* de demander un **bloc** de $k$ octets **consécutifs** de la mémoire
* de libérer un bloc de mémoire alloué.

Il lui est en revanche impossible :

* de modifier un bloc qui lui a été alloué
* de choisir l'endroit de la mémoire qu'il veut se faire allouer

On ne sait en effet pas si la mémoire à côté d'un bloc est libre ou non. Par exemple dans la figure ci-dessous, le seul emplacement libre en mémoire est la case blanche. Le programme *vert* ne peut demander à augmenter le bloc de 3 octets qui lui est alloué, sinon il risque de rentrer en conflit avec le programme *rouge*.

![mémoire partagée]({{ "/assets/cours/algorithmie/poo/memoire-partagee.png" | relative_url }}){:style="margin: auto;display: block;"}

> C'est ce qui fait qu'il est impossible d'augmenter simplement la taille d'un tableau. Il faut le recréer et recopier toutes ses valeurs dans un autre endroit de la mémoire.
{: .note}

### stocker en mémoire

Avant de parler des moyens qu'à un programme pour se rappeler ce qu'il a stocké, regardons comment on peut stocker des objets en mémoire en prenant l'exemple d'un entier.

La façon courante de stocker des objets est d'utiliser des **références**. Mais pour pour bien comprendre ce que c'est il faut commencer par parler (un peu) des valeurs.

#### stockage de valeurs

La mémoire étant une suite fini d'octets, si l'on veut stocker plus qu'un nombre entre 0 et 255 (ou -128, 127 s'il est [signé](https://en.wikipedia.org/wiki/Signed_number_representations)), il faut lui réserver plus d'une case.

Au début de l'informatique, il y avait plusieurs types d'entiers, selon ce qu'on voulait stocker. Pa exemple :

* pour stocker ds entier de 0 à 255 on avait le `char` ( octet)
* pour stocker des entiers de -32768 à 32767 on avait le type `int` (2 octet)
* pour des entiers allant de −2147483647 à 2147483647 on avait le type `long` (4 octet)

On précisait dans notre programme quel type d'entier on voulait utiliser pour telle ou telle variable et un espace mémoire lui était alloué :

> Dans l'**ancien temps** une variable était égale à son indice en mémoire et ne contenant qu'une donnée
{: .note}

![un int]({{ "/assets/cours/algorithmie/poo/memoire-int.png" | relative_url }}){:style="margin: auto;display: block;"}

Ce type de fonctionnement a ses avantages :

* de ne pas se préoccuper de la taille en mémoire. La taille est fixée au départ selon le type choisi
* il y a une correspondance stricte entre variable et indice dans le tableau de la mémoire
* la taille d'un tableau d'objets d'un type fixé est facile à calculer.

Mais cela avait aussi de (très) gros inconvénients :

* comment coder 32768 si je n'ai décidé au départ que ma variable était un `int` ?
* on ne peut pas avoir de tableaux combinant plusieurs types d'objets car il est impossible de calculer facilement l'indice donné d'un tableau contenant plusieurs types .
* si on écrit `i = j`, il **faut** recopier le contenu de `i` (à l'adresse mémoire de `i`) dans `j` (à l'adresse mémoire de `j`) : un même objet ne peut pas avoir plusieurs noms.

#### stockage d'objets

Actuellement, on préfère ne pas avoir à gérer directement la mémoire et surtout, dissocier la variable de la valeur  : écrire `i = j` doit signifier que l'objet désigné par la variable `j` doit **aussi** être désigné par `i`.

Pour cela, il faut dissocier la variable de l'emplacement en mémoire de l'objet. La définition actuelle d'une *variable* est alors :

> Une **variable** est une référence à un objet stocké en mémoire.
{: .note}

Le moyen de le plus simple de définir une référence, c'est de prendre l'indice de la première case mémoire contenant l'objet.

Prenons un exemple : supposons que notre ordinateur dispose de 16Go octets de RAM. L'indice de notre notre tableau de mémoire va alors de $0$ à $10^9-1$ : il faut 4 octets pour stocker un indice en mémoire.

![référence]({{ "/assets/cours/algorithmie/poo/memoire-reference.png" | relative_url }}){:style="margin: auto;display: block;"}

La figure ci-dessus montre alors une variable (*verte*) représentant un objet entier (*orange*) : elle contient l'indice du tableau de la mémoire contenant le premier élément de l'objet (sa référence, $i^\star$ dans la figure).

Les bénéfices de cette méthode sont énormes :

* les objets sont uniques, en écrivant `i = j` les deux variables ont le même objet en référence
* un tableau devient un tableau de référence, il peut contenir des types d'objets différents sans soucis
* on peut facilement modifier un objet, sans avoir à changer toutes les variables qui le référencent.

> Avec de grands pouvoirs viennent de grandes responsabilités. Il faut tout de même faire un peu attention à l'unicité des objets.
{: .attention}

Par exemple en python :

```python
t = [1, 2, 3]
u = t
u[1] = 12
print(t)
```

{% details que vaut `print(t)` ? %}

`[1, 12, 3]` on a modifié l'objet référencé par `u`, qui est le même que celui référencé par `t`

{% enddetails %}

Plus insidieux :

```python
t = [1, 2, 3]
u = [1, t, "?"]
u[1][1] = 12
print(t)
```

{% details que vaut `print(t)` ? %}

`[1, 12, 3]` on a modifié l'objet référencé par `u[1]`, qui est le même que celui référencé par `t`

{% enddetails %}

## programme objet

La quasi-entièreté des langages actuellement sont dit *à objet*. C'est à dire que :

* ce que manipule un programme est appelé objet.
* les variables sont des références aux objets.

Ces langages permettent de créer des programmes en utilisant uniquement les deux mécanismes ci-dessous :

> Pour qu'un programme objet fonctionne, on a besoin de deux mécanismes :
>
> * un moyen de stocker des données et de les manipuler (les objets et leurs méthodes)
> * un moyen d'y accéder (les variables)
>
{: .note}

### objets

On y reviendra, mais pour l'instant considérez qu'un objet est une structure de donnée générique permettant de gérer tout ce dont à besoin un programme :

* des données
* des fonctions
* des modules
* ...

Tout est objet dans un langage objet.

### variables

Les variables sont des références aux objets. Pour ce faire, on utilise l’opérateur d’affectation `=` :

```txt
variable = objet
```

A gauche de l’opérateur `=` se trouve une **variable** (en gros, quelque chose ne pouvant commencer par un nombre) et à droite un **objet**. Dans toute la suite du programme, dès que le programme rencontrera le nom, il le remplacera par l'objet.

> Un variable n'est **PAS** une chaîne de caractères. Une chaîne de caractère est un objet alors qu’un nom n’est qu’un alias vers un objet.
{: .attention}

Il est important de comprendre que l’opérateur d’affectation `=` n’est pas symétrique. À gauche, des variables et à droite, des objets.

> Une variable n'est **pas** l'objet, c'est une référence à celui-ci
{: .note}

La variable peut être vue comme le **nom** de l'objet à ce moment du programme. Un objet pourra avoir plein de noms différents au cours de l'exécution du programme, voir plusieurs noms en même temps.

Pour s'y retrouver et et avoir une procédure déterministe pour retrouver les objets associés aux variables, voir choisir parmi plusieurs variables de même noms, elles sont regroupées par ensembles — nommés **espaces de noms** hiérarchiquement ordonnés.

## espaces de noms

Les espaces de noms nous permettent d'abstraire ce qu'il se passe en mémoire :

* on considère que les objets sont stocké dans *l'espace des objets*
* on accède aux objets via leurs noms, eux même stockés des des *espaces de noms*

Pour chaque *espace de noms* :

* il ne peut y avoir 2 noms identiques dans un même espace de noms
* les espaces de noms sont hiérarchisés : chaque espace de nom (à part le premier) possède un parent au-dessus de lui.

Pour expliciter comment tout ça se passe, on va se concentrer sur le [langage python](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces), mais la procédure est similaire pour les autres langages à objets.

Lorsqu'un nouveau programme démarre l'espace de nom principal, nommé `global` est crée. Au départ, il ne contient rien, à part des noms commençant et finissant par `__`, et qui sont utilisés par python.

> La fonction `globals()` donne l'espace de nom global de python.

```python
x = 1
print(x)
```

module builtins. A l'import d'un module, on crée un espace de noms. 

`vars(__builtins__)`


### noms et variables

```python
x = 1
y = 1
```

deux objets différents

```python
x = 1
x = 3
```

un nouveau nom `x` qui remplace l'autre. L'objet 1 n'a plus de nom (il n'est plus référencé nulle part), il disparait.

```python
x = 1
y = x
```

On commence par trouver les objets puis on affecte. Pour les noms, ils sont toujorus remplacé par les objets.

```python
x = 1
y = 3
y, x = y, x
```

d'abord à droite du `=` puis affectation des noms.

### import

exemple d'import : `import random` (`vars(random)`) et `from random import randint`(pas importé)

### fonctions

espace de crée, puis disparait.

Il y a toujours un namespace associé à la ligne entrain d'être exéctué, c'est le `locals()`

mettre ne caché pour la bonne bouche. (comme les noms, un espace de nom qui est encore référencé ne disparait pas)

1. *globals* : il ne contient rien au départ (à part des objets spécifiques à python, c'est à dire commençant et finissant par des `__`).

module *built-in* qui contient tous les mots du langage utilisable (`list` ou encore `range`, `print`, etc)

lorsqu'une ligne de code est exécutée, il existe l'espace de nom le plus proche d'elle. 

Création d'espace de noms :

* import de modules
* exécution de fonctions : l'espace de nom est (a priori) détruit lorsque la fonction s'arrête
* création de classes ou d'objets : l'espace de nom est détruit lorsque l'objet o la classe est détruit

un objet est détruit lorsqu'il n'est plus présent dans aucun espace de nom.

vars() et vars(truc avec un namespace)
Les variables que l'on va créer se retrouve

> Si un objet contient un
quand quoi pourquoi

<https://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html>

En python, tout peut être vu comme un *namespace* particulier, un endroit où sont rangés des noms : noms de variables, de fonctions, de classes, etc.

Les namespaces possibles sont :

* le namespace global
* la classe, ici `Counter`. Contient tout ce qui est défini dans la classe comme les méthodes ou les constantes.
* l'objet : ici un objet counter de la classe `Counter`. Contient tout ce qui est défini pour l'objet en particulier (par exemple dans le `__init__` quand l'objet est appelé self)
* les méthodes : ce qui n'existe que de l'exécution de la méthode à la fin de son exécution

Plusieurs namespaces peuvent cohabiter en même temps, pour connaître celui qui va être utilisé, python va du [local au global](http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html). S'il n'y a pas d'inclusion (comme une fonction dans une fonction), cela donne :

1. fonction (inclut les méthodes)
2. objet
3. classe
4. global
5. built-in (les mots du langage python comme `list` ou encore `range`)


les imports et leurs espaces de noms.

`[i for i in range(4)]` : i n'existe pas
`for i in range(4):` : i existe

[module inspect](https://docs.python.org/3/library/inspect.html)

namespace plus référencé : il meure (comme tout autre objet)

1. si un objet n'est plus dans aucun espace de nom il disparait (on libère de la méméoire). Ex.
2. pluseirus espaces de noms, il faut pouvoir s'y retrouver. 
   1. lorsque l'on crée on crée dans l'espace le plus proche.
   2. Si on ne le trouve pas on remonte
   3. ex de la création de fonction. 
      1. espace de nom par défaut
      2. lorsque l'on exécute une fonction on crée un espace de nom
      3. on y place les entrées
      4. à la fin de la fonction, on supprime l'espace de nom si on en a plus besoin.
3. règle des espaces de noms
4.  exemples d'espace de noms: 
   1.  fnction
   2.  modules
   3.  objets et classes (on va le voir
5.  ex 2 : fonction de fonctions. O garde l'espace de nom car on en a encore besoin

   
Comment rendre compte d'une variable, et de la portée de celles-ci


> * que des variables globales c'es nulles : variables dans les fonctions (c'est le cas par défaut en javascript)
> * quelle portée choisi ? Le bloc for ? non, la fonction ? les modules ?
> * comment savoir quelle variable utiliser si les espaces de noms s'embriquent?
> * et comment de temps en temps modifier un objet au-dessus
> * donner des exemples récursifs
{: .tbd}
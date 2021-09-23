---
layout: page
title:  "Arbre de recherche"
category: cours
tags: informatique code graphes
authors : 
    - François Brucker
    - Pascal Préa
---

> [graphes]({% link cours/graphes/index.md %}) / [arbre de recherche]({% link cours/graphes/arbre-de-recherche.md %})
{: .chemin}

## Introduction

Le but de ce travail est d'étudier les arbres de recherche, qui sont une structure de stockage efficaces pour maintenir un ensemble d'éléments triés.

## Arbre binaire

Comme vu [précédemment]({% link cours/graphes/arbres.md %}#arbre-binaire), un arbre binaire planté est une structure de graphe qui possède :

* un noeud particulier appelé racine qui n'est enfant de personne
* chaque nœud à un ou deux enfants, nommé *enfant gauche* ou *enfant droit*
* chaque nœud de la structure a des enfants différents
* chaque nœud différent de la racine est enfant d'un autre nœeud

Les nœuds sans enfants sont appelées *feuilles*.

Un des intérêt d'un arbre binaire est qu'il suffit de connaitre la racine et pour chaque noeud ses enfant pour retrouver toute la structure : **Se donner une racine ou tout l'arbre binaire est équivalent**.

### calcul de la hauteur d'un arbre binaire planté

On rappelle que la hauteur d'un arbre est la longueur maximale du chemin d'un nœud à la racine. Par extension,la hauteur d'un nœud sera la longueur maximale d'un chemin allant d'un de ses descendants à lui même.

> Si l'on connait la hauteur de chacun de ses enfants, quelle est la hauteur d'un nœud ?
{: .a-faire}
{% details solution %}

En notant $g$ et $d$ les enfants gauche et droit d'un nœud $n$, on a que :
$h(n) = \max(h(g), h(d))$

{% enddetails %}
{: .a-faire}

> En déduire un algorithme qui calcule récursivement la hauteur d'un arbre. Et donnez en sa complexité.
{: .a-faire}
{% details solution %}

On suppose que l'on a les fonction `enfant_gauche(noeud)`et `enfant_droit(noeud)` qui rende respectivement l'enfant gauche et l'enfant droit d'un noeud s'il existe et `None` sinon.

On a alors :

```python

def hauteur(noeud):
    if noeud is None:
        return 0
    return max(hauteur(enfant_gauche(noeud)), hauteur(enfant_droit(noeud)))

print(hauteur(racine))
```

De part la définition des arbres binaires, on ne va parcourir qu'une seule fois chaque noeud de l'arbre, la complexité est donc en $\mathcal{O}(n)$, avec $n$ le nombre de nœuds de l'arbre.

{% enddetails %}
{: .a-faire}

### calcul du nombre de sommets d'un arbre binaire planté

On dira que l'arbre composé d'un nœud $x$ et de tous ses descendants est le **sous-arbre de $x$**.

Même question que précédemment pour le calcul du nombre de nœuds d'un arbre.

> Si l'on connait le nombre de nœud de chacun des sous arbres de ses enfants, quelle est le nombre de nœuds du sous-arbre d'un nœud ?
{: .a-faire}
{% details solution %}

En notant $g$ et $d$ les enfants gauche et droit d'un nœud $n$, on a que :
$N(n) = N(g) + N(d) + 1$

{% enddetails %}
{: .a-faire}

> En déduire un algorithme qui calcule récursivement le nombre de nœuds d'un arbre. Et donnez en sa complexité.
{: .a-faire}
{% details solution %}

On suppose que l'on a les fonction `enfant_gauche(noeud)`et `enfant_droit(noeud)` qui rende respectivement l'enfant gauche et l'enfant droit d'un noeud s'il existe et `None` sinon.

On a alors :

```python

def nombre(noeud):
    if noeud is None:
        return 0
    return nombre(enfant_gauche(noeud)) + nombre(enfant_droit(noeud)) + 1

print(nombre(racine))
```

De part la définition des arbres binaires, on ne va parcourir qu'une seule fois chaque noeud de l'arbre, la complexité est donc en $\mathcal{O}(n)$, avec $n$ le nombre de nœuds de l'arbre.

{% enddetails %}
{:.a-faire}

### structure de donnée

Si l'on code un nœud d'un arbre binaire par une liste à trois éléments où :

* le premier élément est sa valeur,
* le second élément est son enfant gauche ou `None`s'il n'en a pas
* le troisième élément est son enfant droit ou `None` s'il n'en a pas

> donnez le code des fonctions :
>
> * `enfant_gauche(x)` et `change_enfant_gauche(x, nouveau)` : qui rende et change l'enfant gauche d'un nœud `x`
> * `enfant_droit(x)` et `change_enfant_droit(x,nouveau)` : qui rende et change l'enfant droit d'un nœud `x`
> * `valeur(x)` et `change_valeur(x, nouveau)`  : qui rende et change la valeur d'un nœud `x`
{: .a-faire}
{% details solution %}

```python

def enfant_gauche(x):
    return x[1]


def change_enfant_gauche(x, nouveau):
    x[1] = nouveau


def enfant_droit(x):
    return x[2]


def change_enfant_droit(x, nouveau):
    x[2] = nouveau


def valeur(x):
    return x[0]


def change_valeur(x, nouveau):
    x[0] = nouveau

```

{% enddetails %}
{:.a-faire}

### exemple

> TBD : un arbre tableau -> arbre python (sans algo)
{:.note}

## arbre binaire de recherche : définitions

### def

### structure

### exemple tableau

plusieurs possibilités avec les même nombres ?

## algorithmes de manipulation

### création

### trouve

### insertion

### suppression

## trie des valeurs

### ordre complet

### prédécesseur d'une valeur (pas forcément dans l'arbre)

### successeur d'une valeur (pas forcément dans l'arbre)

## propriétés de hauteur max, min

> shuffle pour hauteur min.
> exemple structure toujours équilibrée (donner noms)
{: .note}

### hauteur min à partir d'une liste triée

## exemple du dictionnaire

> les mots d'un dico (ou livre) puis on les prend random et on voit la hauteur
{:.note}

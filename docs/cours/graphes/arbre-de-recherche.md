---
layout: page
title:  "Arbre de recherche"
category: cours
tags: informatique code graphes
authors : 
    - François Brucker
    - Pascal Préa
    - Sébastien Ratel
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
$h(n) = \max(h(g), h(d)) + 1$

{% enddetails %}
{: .a-faire}

> En déduire un algorithme qui calcule récursivement la hauteur d'un arbre. Et donnez en sa complexité.
{: .a-faire}
{% details solution %}

On suppose que l'on a les fonctions `enfant_gauche(noeud)`et `enfant_droit(noeud)` qui rende respectivement l'enfant gauche et l'enfant droit d'un noeud s'il existe et `None` sinon.

On a alors :

```python

def hauteur(noeud):
    if noeud is None:
        return 0
    return max(hauteur(enfant_gauche(noeud)), hauteur(enfant_droit(noeud))) + 1

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

### encodage

Prenons les deux tas de la figure ci-après :

![tas possibles]({{ "/assets/cours/graphes/tas_2-possibilites.png" | relative_url }}){:style="margin: auto;display: block;"}

En utilisant l'encodage précédent, le tas de gauche va s'écrire :

```python
[42, [12, [6, None, None], [5, None, None]], [3, [1, None, None], None]]
```

> pourquoi ?
{: .a-faire}
{% details solution %}

On peut ainsi lire l'arbre comme ceci : `[42, enfant_gauche, enfant_droit]`. avec `enfant_gauche = [12, enfant_gauche_2, enfant_droit_2]`. Comme `enfant_gauche_2` est une feuille ce sera : `enfant_gauche_2 = [6, None, None]`.
Les nœud étant aussi des listes, elles s'imbriquent donc les unes dans les autres, jusqu'à avoir des feuilles `None`, c'et à dire pas de feuilles.

{% enddetails %}
{: .a-faire}

> Quel est l'encodage du tas de droite ?
{: .a-faire}
{% details solution %}

```python
[42, [12, [3, None, None], [1, None, None]], [6, [5, None, None], None]]
```

{% enddetails %}
{: .a-faire}

### code

> Exécutez en python les algorithmes de hauteur et de nombre sur les 2 tas de la question précédente.
{: .a-faire}
{% details solution %}

fichier *"arbre_binaires.py"* :

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


def hauteur(noeud):
    if noeud is None:
        return 0
    return max(hauteur(enfant_gauche(noeud)), hauteur(enfant_droit(noeud))) + 1


def nombre(noeud):
    if noeud is None:
        return 0
    return nombre(enfant_gauche(noeud)) + nombre(enfant_droit(noeud)) + 1

racine_1 = [42, [12, [6, None, None], [5, None, None]], [3, [1, None, None], None]]
racine_2 = [42, [12, [3, None, None], [1, None, None]], [6, [5, None, None], None]]

print("hauteur : ", hauteur(racine_1), " - nombre : ", nombre(racine_1))

```

{% enddetails %}
{: .a-faire}

## arbre binaire de recherche : définitions

Un **arbre binaire de recherche** est un arbre binaire planté dont les sommets sont valués par un ensemble ordonné (e.g. des nombres) & tel que, pour chaque sommet $s$ :

* l'enfant gauche et ses descendants aient une valuation strictement plus petite que celle de $s$,
* l'enfant droit et ses descendants aient une valuation plus grande ou égale à celle de $s$.

### exemple

![abr possibles]({{ "/assets/cours/graphes/abr-ou-pas.png" | relative_url }}){:style="margin: auto;display: block;"}

>Des deux figures précédentes, laquelle est un arbre binaire de recherche ?
{: .a-faire}
{% details solution %}

Celui de gauche n'est pas un arbre binaire de recherche, car 15 est à gauche de 10 et il est plus grand. C'est tous les descendants d'au nœud qui doivent être plus petit s'il sont à gauche ou plus grand s'il sont à droite.

{% enddetails %}
{: .a-faire}

> Il existe d'autres possibilités d'arbre binaire de recherche avec ces nombres. Donnez-en une.
{: .a-faire}
{% details solution %}

Il y a au moins celui-là :

![abr lignes]({{ "/assets/cours/graphes/abr-ligne.png" | relative_url }}){:style="margin: auto;display: block;"}

{% enddetails %}
{: .a-faire}

> Donnez la structure python des deux arbres binaires de recherche
{: .a-faire}
{% details solution %}

```python
[12, [8, [6, None, None], [10, None, None]], [15, None, [20, None, None]]]

[6, None, [8, None, [10, None, [12, None, [15, None, [20, None, None]]]]]]
```

{% enddetails %}
{: .a-faire}

## algorithmes de manipulation

### création

>En utilisant la structure des arbres binaires, donnez un fonction python qui crée un arbre binaire de recherche à partir d'une valeur.
{: .a-faire}
{% details solution %}

```python
def creation(valeur):
    return [valeur, None, None] 
```

{% enddetails %}
{: .a-faire}

### trouve

>Donnez un fonction python qui, à partir d'une valeur et d'un arbre binaire de recherche répond `True` si la valeur est dans l'arbre et `False` sinon. Cet algorithme pourra s'inspirer de la [recherche dichotomique](https://fr.wikipedia.org/wiki/Recherche_dichotomique).
{: .a-faire}
{% details solution %}

```python
def recherche(val, racine):
    if racine is None:
        return False
    elif valeur(racine) == val:
        return True
    elif valeur(racine) > val:
        return recherche(val, enfant_gauche(racine))
    else:
        return recherche(val, enfant_droit(racine))
```

{% enddetails %}
{: .a-faire}

> Quelle est la complexité de cette fonction ?
{: .a-faire}
{% details solution %}

Elle est proportionnelle à la hauteur de l'arbre.

{% enddetails %}
{: .a-faire}

> Ajouter à votre code la fonction de recherche et les deux arbres que vous avez trouvé. Essayez de trouver 10 et 42 sur vos deux arbres.
{: .a-faire}
{% details solution %}

```python
# ...

abr_1 = [12, [8, [6, None, None], [10, None, None]], [15, None, [20, None, None]]]
abr_2 = [6, None, [8, None, [10, None, [12, None, [15, None, [20, None, None]]]]]]

print(recherche(10, abr_1))
print(recherche(42, abr_1))

print(recherche(10, abr_2))
print(recherche(42, abr_2))

```

{% enddetails %}
{: .a-faire}

### insertion

> Déduire de la question précédente que pour un arbre binaire donné et une valeur, il n'y a qu'une seule position possible pour insérer une valeur donnée.
{: .a-faire}
{% details solution %}

Dans la recherche, il n'y a à chaque fois qu'une seule possibilité. Si on ne trouve pas la valeur, l'endroit où on est arrivé dans l'arbre est la position où on doit l'insérer

{% enddetails %}
{: .a-faire}

> En modifiant l'algorithme de recherche, donner l'algorithme de l'insertion d'une valeur dans l'arbre.
{: .a-faire}
{% details solution %}

```python
def insertion(val, racine):
    if racine is None or valeur(racine) == val:
        return
    elif valeur(racine) > val:
        if enfant_gauche(racine) is None:
            change_enfant_gauche(racine, abr(val))
        else:
            insertion(val, enfant_gauche(racine))
    else:
        if enfant_droit(racine) is None:
            change_enfant_droit(racine, abr(val))
        else:
            insertion(val, enfant_droit(racine))
```

{% enddetails %}
{: .a-faire}

> Quelle est la complexité de cette fonction ?
{: .a-faire}
{% details solution %}

Elle est proportionnelle à la hauteur de l'arbre.

{% enddetails %}
{: .a-faire}

>Insérez 42 dans les 2 arbres de recherche précédents. Et donner le résultat.
{: .a-faire}
{% details solution %}

```python
insertion(42, abr_1)
print(abr_1)
insertion(42, abr_2)
print(abr_2)
```

Ce qui donne :

```python
[12, [8, [6, None, None], [10, None, None]], [15, None, [20, None, [42, None, None]]]]
[6, None, [8, None, [10, None, [12, None, [15, None, [20, None, [42, None, None]]]]]]]
```

{% enddetails %}
{: .a-faire}

### suppression

Supprimer un noeud d'un arbre de recherche peut être simple si :

* ce nœud n'a pas d'enfant : on le remplace dans son parent par `None`
* ce nœud n'a qu'un seul enfant : on le remplace par son enfant dans son parent.

Si le noeud, disons $x$ à 2 enfants, on peut chercher le noeud contenant la plus grande des valeurs plus petite que celle du noeud parmi ses descendants, disons $y$. Ce noeud n'aura qu'un seul enfant.

> pourquoi ?
{: .a-faire}
{% details solution %}

Le noeud recherché sera un descendant de $x$ à gauche. Il ne peut avoir de fils droit sinon ce fils aurait une valeur plus grande que sont père ($y$) et donc serait plus proche en valeur de $x$. ce qui est impossible par construction.

{% enddetails %}
{: .a-faire}

> Comment trouver $y$ ?
{: .a-faire}
{% details solution %}

C'est le premier enfant à droite des descendants de $x$.

{% enddetails %}
{: .a-faire}

On peut alors échanger les valeur de $x$ et de $y$ puis supprimer $y$ pour conserver la structure d'arbre binaire de recherche.

> pourquoi ?
{: .a-faire}
{% details solution %}

$y$ n'a qu'un enfant, il est donc facile de le supprimer et de conserver la structure d'arbre de recherche.

En échangeant les valeurs, on a pris une valeur inférieure à celle de $x$ mais plus grande que toute les autres valeurs plus petite que $x$ dans l'arbre, elle ne viole donc aucune règle dans l'arbre.

{% enddetails %}
{: .a-faire}

> Quelle est la complexité de cette fonction ?
{: .a-faire}
{% details solution %}

Elle est proportionnelle à la hauteur de l'arbre.

{% enddetails %}
{: .a-faire}

## ordre des valeurs

### trie des valeurs

>Que donne comme résultat le parcours [en-ordre]({% link cours/graphes/arbres.md %}#en-ordre) d'un arbre de recherche ?
{: .a-faire}
{% details solution %}

Ca rend les valeurs de l'arbre dans l'ordre du plus petit au plus grand.

{% enddetails %}
{: .a-faire}

## hauteur d'un arbre binaire de recherche

On voit que toutes les opérations sur un arbre binaire de recherche sont proportionnelles à sa hauteur.

> Quelle est la hauteur maximale d'un arbre binaire de recherche ?
{: .a-faire}
{% details solution %}

c'est le nombre d'élément si tous les noeud n'ont qu'un seul enfant.

{% enddetails %}
{: .a-faire}

> A partir d'une liste de valeurs, donner un algorithme qui rend un arbre binaire de recherche de hauteur maximale contenant ces valeurs.
{: .a-faire}
{% details solution %}
On commence par trier la liste puis on insère les éléments un à un dans cet ordre.

{% enddetails %}
{: .a-faire}

> Quelle est la hauteur minimale d'un arbre binaire de recherche ?
{: .a-faire}
{% details solution %}

la hauteur minimale est atteinte si tous les nœuds on 2 enfants. La hauteur est alors $log_2(n)$ où $n$ est le nombre de sommet.
{% enddetails %}
{: .a-faire}

> A partir d'une liste de valeurs, donner un algorithme qui rend un arbre binaire de recherche de hauteur minimale contenant ces valeurs. On s'inspirera de la recherche dichotomique pour à chaque fois insérer le milieu.
{: .a-faire}
{% details solution %}
On commence par trier la liste puis on insère les éléments en prenant récursivement le milieu.

```python

liste.sort()

abr = creation(liste[len(liste) // 2])

def abr_insere_min(debut, fin):
    if fin > debut + 1:
        x = liste[(debut + fin) // 2]
        insertion(x, abr)
        abr_insere_min(debut, x)
        abr_insere_min(x, fin)

abr_insere_min(0, len(liste) // 2)
abr_insere_min(len(liste) // 2, len(liste))

print(abr)
```

{% enddetails %}
{: .a-faire}

## hauteur expérimentale

Conserver une hauteur minimale dans un arbre binaire de recherche est donc crucial pour maintenir de bonnes performances. 

> Il existe des version des arbres re cherche qui s'équilibrent tout seul comme les [AVL](https://fr.wikipedia.org/wiki/Arbre_AVL) ou les arbres [rouge/noir](https://fr.wikipedia.org/wiki/Arbre_bicolore) mais leur structure est plus lourde algorithmiquement.

La clé est d'insérer les valeurs dans un ordre aléatoire. Nous allons de montrer expérimentalement.

Essayez avec la liste des 1000 premiers entiers.

> Insérer des nombre pris dans une liste triée et vérifier que la hauteur est égale à la longueur de la liste
{: .a-faire}
{% details solution %}

```python
liste = list(range(1000))

abr = creation(liste[0])
for x in liste[1:]:
    instertion(x, abr)
```

{% enddetails %}
{: .a-faire}

> Insérer des nombre pris dans la même liste que précédemment de façon à minimiser la hauteur et vérifier que celle-ci est égale au log en base 2 la longueur de la liste
{: .a-faire}
{% details solution %}

reprendre le code de la question sur la hauteur minimale.

{% enddetails %}
{: .a-faire}

> Insérer de façon aléatoire des nombre pris dans la même liste que précédemment et vérifier que la hauteur est de l'ordre du au log en base 2 la longueur de la liste
{: .a-faire}
{% details solution %}

```python
import random

liste = list(range(1000))
random.shuffle(liste)

abr = creation(liste[0])
for x in liste[1:]:
    instertion(x, abr)
```

{% enddetails %}
{: .a-faire}

Lors de mes expérimentation, je trouve :

* une hauteur max de 1000
* une hauteur min de 10
* une hauteur aléatoire de l'ordre de 20

> essayez avec des listes plus grandes.
{: .a-faire}

## conclusion

Les [arbres de recherche](https://fr.wikipedia.org/wiki/Arbre_binaire_de_recherche) sont une structure qui fonctionne comme une liste triée pour la recherche d'un élément, mais qui est bien plus efficace pour l'insertion,à condition que les éléments à insérer arrivent dans un ordre aléatoire.

On l'utilise lorsque l'on veut maintenir une liste d'éléments qui varie au court du temps triés (si la liste est constante, autant juste la. trier).

> L'ordre entre les éléments n'est pas forcément totale. Par exemple dans les [arbres AABB](https://www.azurefromthetrenches.com/, une variation des arbres binaires de recherche très utilisés en informatique graphique pour gérer efficacement les collisions en 2D ou 3D.

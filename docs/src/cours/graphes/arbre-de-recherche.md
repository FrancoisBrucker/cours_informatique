---
layout: layout/post.njk
title: Arbres binaire de recherche
authors: 
    - François Brucker
    - Pascal Préa
    - Sébastien Ratel

eleventyNavigation:
  key: "Arbres binaire de recherche"
  parent: "Graphes"
---

{% prerequis "**Prérequis** :" %}

* [Arbres](../arbres)
* python code

{% endprerequis %}

> TBD : FIX prés-requis

<!-- début résumé -->

Le but de ce travail est d'étudier les arbres de recherche, qui sont une structure de stockage efficaces pour maintenir un ensemble d'éléments triés.

<!-- fin résumé -->

## Arbre binaire

Comme vu [précédemment]({{ "/cours/graphes/arbres" | url }}#arbre-binaire), un arbre binaire planté est une structure de graphe qui possède :

* un nœud particulier appelé racine qui n'est enfant de personne
* chaque nœud à un ou deux enfants, nommé *enfant gauche* ou *enfant droit*
* chaque nœud de la structure a des enfants différents
* chaque nœud différent de la racine est enfant d'un autre nœud

Les nœuds sans enfants sont appelées *feuilles*.

Un des intérêt d'un arbre binaire est qu'il suffit de connaître la racine et pour chaque nœud ses enfant pour retrouver toute la structure : **Se donner une racine ou tout l'arbre binaire est équivalent**.

### calcul de la hauteur d'un arbre binaire planté

On rappelle que la hauteur d'un arbre est la longueur maximale du chemin d'un nœud à la racine. Par extension,la hauteur d'un nœud sera la longueur maximale d'un chemin allant d'un de ses descendants à lui même.

{% exercice %}
Si l'on connaît la hauteur de chacun de ses enfants, quelle est la hauteur d'un nœud ?
{% endexercice %}
{% details "solution" %}
En notant $g$ et $d$ les enfants gauche et droit d'un nœud $n$, on a que :
$h(n) = \max(h(g), h(d)) + 1$

{% enddetails %}

{% exercice %}
En déduire un algorithme qui calcule récursivement la hauteur d'un arbre. Et donnez en sa complexité.

{% endexercice %}
{% details "solution" %}
On suppose que l'on a les fonctions `enfant_gauche(nœud)` et `enfant_droit(nœud)` qui rende respectivement l'enfant gauche et l'enfant droit d'un nœud s'il existe et `None` sinon.

On a alors :

```python

def hauteur(nœud):
    if nœud is None:
        return 0
    return max(hauteur(enfant_gauche(nœud)), hauteur(enfant_droit(nœud))) + 1  

print(hauteur(racine))

```

De part la définition des arbres binaires, on ne va parcourir qu'une seule fois chaque nœud de l'arbre, la complexité est donc en $\mathcal{O}(n)$, avec $n$ le nombre de nœuds de l'arbre.

{% enddetails %}


### structure de donnée

Si l'on code un nœud d'un arbre binaire par une liste à trois éléments où :

* le premier élément est sa valeur,
* le second élément est son enfant gauche ou `None`s'il n'en a pas
* le troisième élément est son enfant droit ou `None` s'il n'en a pas

{% exercice %}
donnez le code des fonctions :

* `enfant_gauche(x)` et `change_enfant_gauche(x, nouveau)` : qui rende et change l'enfant gauche d'un nœud `x`
* `enfant_droit(x)` et `change_enfant_droit(x,nouveau)` : qui rende et change l'enfant droit d'un nœud `x`
* `valeur(x)` et `change_valeur(x, nouveau)`  : qui rende et change la valeur d'un nœud `x`


{% endexercice %}
{% details "solution" %}
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

### encodage

Prenons les deux tas de la figure ci-après :

![tas possibles](../assets/img/tas_2-possibilites.png)

En utilisant l'encodage précédent, le tas de gauche va s'écrire :

```python
[42, [12, [6, None, None], [5, None, None]], [3, [1, None, None], None]]
```

{% exercice %}
pourquoi ?
{% endexercice %}
{% details "solution" %}
On peut ainsi lire l'arbre comme ceci : `[42, enfant_gauche, enfant_droit]`. avec `enfant_gauche = [12, enfant_gauche_2, enfant_droit_2]`. Comme `enfant_gauche_2` est une feuille ce sera : `enfant_gauche_2 = [6, None, None]`.
Les nœud étant aussi des listes, elles s'imbriquent donc les unes dans les autres, jusqu'à avoir des feuilles `None`, c'et à dire pas de feuilles.

{% enddetails %}

{% exercice %}
Quel est l'encodage du tas de droite ?

{% endexercice %}
{% details "solution" %}
```python
[42, [12, [3, None, None], [1, None, None]], [6, [5, None, None], None]]
```

{% enddetails %}

### code

{% exercice %}
Exécutez en python les algorithmes de hauteur et de nombre sur les 2 tas de la question précédente.


{% endexercice %}
{% details "solution" %}
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


## arbre binaire de recherche : définitions

Un **arbre binaire de recherche** est un arbre binaire planté dont les sommets sont valués par un ensemble ordonné (e.g. des nombres) & tel que, pour chaque sommet $s$ :

* l'enfant gauche et ses descendants aient une valuation strictement plus petite que celle de $s$,
* l'enfant droit et ses descendants aient une valuation plus grande ou égale à celle de $s$.

### exemple

![abr possibles](../assets/img/abr-ou-pas.png)

{% exercice %}
Des deux figures précédentes, laquelle est un arbre binaire de recherche ?

{% endexercice %}
{% details "solution" %}
Celui de gauche n'est pas un arbre binaire de recherche, car 15 est à gauche de 10 et il est plus grand. C'est tous les descendants d'au nœud qui doivent être plus petit s'il sont à gauche ou plus grand s'il sont à droite.

{% enddetails %}

{% exercice %}
Il existe d'autres possibilités d'arbre binaire de recherche avec ces nombres. Donnez-en une.

{% endexercice %}
{% details "solution" %}
Il y a au moins celui-là :

![abr lignes](../assets/img/abr-ligne.png}})
{% enddetails %}

{% exercice %}
Donnez la structure python des deux arbres binaires de recherche.

{% endexercice %}
{% details "solution" %}
```python
[12, [8, [6, None, None], [10, None, None]], [15, None, [20, None, None]]]

[6, None, [8, None, [10, None, [12, None, [15, None, [20, None, None]]]]]]
```
{% enddetails %}

## algorithmes de manipulation

### création

{% exercice %}
En utilisant la structure des arbres binaires, donnez un fonction python qui crée un arbre binaire de recherche à partir d'une valeur.
{% endexercice %}
{% details "solution" %}
```python
def creation(valeur):
    return [valeur, None, None] 
```
{% enddetails %}

### trouve

{% exercice %}
Donnez un fonction python qui, à partir d'une valeur et d'un arbre binaire de recherche répond `True` si la valeur est dans l'arbre et `False` sinon. Cet algorithme pourra s'inspirer de la [recherche dichotomique](https://fr.wikipedia.org/wiki/Recherche_dichotomique).

{% endexercice %}
{% details "solution" %}

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

{% exercice %}
Quelle est la complexité de cette fonction ?

{% endexercice %}
{% details "solution" %}

Elle est proportionnelle à la hauteur de l'arbre.

{% enddetails %}

{% exercice %}
Ajouter à votre code la fonction de recherche et les deux arbres que vous avez trouvé. Essayez de trouver 10 et 42 sur vos deux arbres.
{% endexercice %}
{% details "solution" %}


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

### insertion

{% exercice %}
Déduire de la question précédente que pour un arbre binaire donné et une valeur, il n'y a qu'une seule position possible pour insérer une valeur donnée.
{% endexercice %}
{% details "solution" %}

Dans la recherche, il n'y a à chaque fois qu'une seule possibilité. Si on ne trouve pas la valeur, l'endroit où on est arrivé dans l'arbre est la position où on doit l'insérer

{% enddetails %}

{% exercice %}
En modifiant l'algorithme de recherche, donner l'algorithme de l'insertion d'une valeur dans l'arbre.
{% endexercice %}
{% details "solution" %}

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

{% exercice %}
Quelle est la complexité de cette fonction ?

{% endexercice %}
{% details "solution" %}

Elle est proportionnelle à la hauteur de l'arbre.

{% enddetails %}


{% exercice %}
Insérez 42 dans les 2 arbres de recherche précédents. Et donner le résultat.
{% endexercice %}
{% details "solution" %}

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


### suppression

Supprimer un noeud d'un arbre de recherche peut être simple si :

* ce nœud n'a pas d'enfant : on le remplace dans son parent par `None`
* ce nœud n'a qu'un seul enfant : on le remplace par son enfant dans son parent.

Si le noeud, disons $x$ à 2 enfants, on peut chercher le noeud contenant la plus grande des valeurs plus petite que celle du noeud parmi ses descendants, disons $y$. Ce noeud n'aura qu'un seul enfant.

{% exercice %}
pourquoi ?
{% endexercice %}
{% details "solution" %}

Le noeud recherché sera un descendant de $x$ à gauche. Il ne peut avoir de fils droit sinon ce fils aurait une valeur plus grande que sont père ($y$) et donc serait plus proche en valeur de $x$. ce qui est impossible par construction.

{% enddetails %}

{% exercice %}
Comment trouver $y$ ?
{% endexercice %}
{% details "solution" %}
C'est le descendant le plus à droite du sous-arbre gauche de $x$.
{% enddetails %}

On peut alors échanger les valeur de $x$ et de $y$ puis supprimer $y$ pour conserver la structure d'arbre binaire de recherche.

{% exercice %}
pourquoi ?
{% endexercice %}
{% details "solution" %}

$y$ n'a qu'un enfant, il est donc facile de le supprimer et de conserver la structure d'arbre de recherche.

En échangeant les valeurs, on a pris une valeur inférieure à celle de $x$ mais plus grande que toute les autres valeurs plus petite que $x$ dans l'arbre, elle ne viole donc aucune règle dans l'arbre.

{% enddetails %}

{% exercice %}
Quelle est la complexité de cette fonction ?
{% endexercice %}
{% details "solution" %}

Elle est proportionnelle à la hauteur de l'arbre.

{% enddetails %}

## ordre des valeurs

### tri des valeurs

{% exercice %}
Que donne comme résultat le parcours [en-ordre]({{ "cours/graphes/arbres" | url }}#en-ordre) d'un arbre de recherche ?
{% endexercice %}
{% details "solution" %}

Ca rend les valeurs de l'arbre dans l'ordre du plus petit au plus grand.

{% enddetails %}

## hauteur d'un arbre binaire de recherche

On voit que toutes les opérations sur un arbre binaire de recherche sont proportionnelles à sa hauteur.

{% exercice %}
Quelle est la hauteur maximale d'un arbre binaire de recherche ?de recherche ?
{% endexercice %}
{% details "solution" %}

c'est le nombre d'élément si tous les noeud n'ont qu'un seul enfant.

{% enddetails %}

{% exercice %}
A partir d'une liste de valeurs, donner un algorithme qui rend un arbre binaire de recherche de hauteur maximale contenant ces valeurs.
{% endexercice %}
{% details "solution" %}

On commence par trier la liste puis on insère les éléments un à un dans cet ordre.

{% enddetails %}

{% exercice %}
Quelle est la hauteur minimale d'un arbre binaire de recherche ?
{% endexercice %}
{% details "solution" %}

la hauteur minimale est atteinte si tous les nœuds on 2 enfants. La hauteur est alors $log_2(n)$ où $n$ est le nombre de sommet.

{% enddetails %}


{% exercice %}
A partir d'une liste de valeurs, donner un algorithme qui rend un arbre binaire de recherche de hauteur minimale contenant ces valeurs. On s'inspirera de la recherche dichotomique pour à chaque fois insérer le milieu.
{% endexercice %}
{% details "solution" %}

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

## hauteur expérimentale

Conserver une hauteur minimale dans un arbre binaire de recherche est donc crucial pour maintenir de bonnes performances. 

{% info %}
Il existe des version des arbres recherche qui s'équilibrent tout seul comme les [AVL](https://fr.wikipedia.org/wiki/Arbre_AVL) ou les arbres [rouge/noir](https://fr.wikipedia.org/wiki/Arbre_bicolore) mais leur structure est plus lourde algorithmiquement.
{% endinfo %}

L'idée est d'insérer les valeurs dans un ordre aléatoire. Nous allons de montrer expérimentalement.

Essayez avec la liste des 1000 premiers entiers.

{% exercice %}
Insérer des nombre pris dans une liste triée et vérifier que la hauteur est égale à la longueur de la liste.

{% endexercice %}
{% details "solution" %}


```python
liste = list(range(1000))

abr = creation(liste[0])
for x in liste[1:]:
    instertion(x, abr)
```

{% enddetails %}

{% exercice %}
Insérer des nombre pris dans la même liste que précédemment de façon à minimiser la hauteur et vérifier que celle-ci est égale au log en base 2 la longueur de la liste.
{% endexercice %}
{% details "solution" %}

Reprendre le code de la question sur la hauteur minimale.

{% enddetails %}

{% exercice %}
Insérer de façon aléatoire des nombre pris dans la même liste que précédemment et vérifier que la hauteur est de l'ordre du au log en base 2 la longueur de la liste.

{% endexercice %}
{% details "solution" %}

```python
import random

liste = list(range(1000))
random.shuffle(liste)

abr = creation(liste[0])
for x in liste[1:]:
    insertion(x, abr)
```

{% enddetails %}

Lors de mes expérimentations, je trouve :

* une hauteur max de 1000
* une hauteur min de 10
* une hauteur aléatoire de l'ordre de 20

{% exercice %}
Essayez avec des listes plus grandes.
{% endexercice %}

## conclusion

Les [arbres de recherche](https://fr.wikipedia.org/wiki/Arbre_binaire_de_recherche) sont une structure qui fonctionne comme une liste triée pour la recherche d'un élément, mais qui est bien plus efficace pour l'insertion,à condition que les éléments à insérer arrivent dans un ordre aléatoire.

On l'utilise lorsque l'on veut maintenir une liste d'éléments qui varie au court du temps triés (si la liste est constante, autant juste la. trier).

{% info %}
L'ordre entre les éléments n'est pas forcément totale. Par exemple dans les [arbres AABB](https://www.azurefromthetrenches.com), une variation des arbres binaires de recherche très utilisés en informatique graphique pour gérer efficacement les collisions en 2D ou 3D.
{% endinfo %}
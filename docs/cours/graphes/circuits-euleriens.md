---
layout: page
title:  "circuits eulérien"
category: cours
tags: informatique code graphes
author : "François Brucker"
---

> [graphes]({% link cours/graphes/index.md %}) / [euleriens]({% link cours/graphes/circuits-euleriens.md %})
{: .chemin}

## Introduction

Le but de ce cours est d'apprendre à coder un (multi-)graphe dirigé et de s'en servir pour trouver un circuit eulérien d'un de ces graphes (s'il existe).

Le code complet de ce tutoriel est disponible sur [le github du projet](https://github.com/FrancoisBrucker/cours_informatique/tree/master/docs/cours/graphes/circuits-euleriens-code). Essayez tout de même de résoudre les questions par vous-même, vous apprendrez plus que juste lire le corrigé.

## Outils

Vous aurez besoin de connaitre un peu de python et que vous sachiez faire des tests. Suivez les 4 premières parties du [cours de développement]({% link cours/graphes/index.md %})

Les tests vont s'ajouter petit à petit et à la fin de la séance votre fichier *"test_multi_graph.py"* contiendra plus d'une vingtaine de tests !

## Plan

  1. modéliser un multi-graphe dirigé en python
  2. algorithme du circuit eulérien
  3. suppression itératives de circuits à un multi-graphe eulérien
  4. création d'un multi-graphe à partir d'une suite de circuits
  5. le programme qui trouve un circuit eulérien d'un multi-graphe donné.

## code du projet

Les fonctions que l'on vous demande de coder sont la plupart du temps simples, mais certaines nécessitent de réfléchir et — surtout — de se tromper un peu avant de voir la lumière. Comme cous avez le corrigé et les tests que l'on vous demande de faire passer, vous savez lorsque vous avez bon. On vous demande donc :

* de ne pas regarder la solution avant que vous ayez fait passer les tests
* de vous creuser la tête pour faire marcher l'algorithme
* de bien nommer vos variables et de séparer par des retours à la lignes les différentes parties de l'algorithme

## multi-graphe dirigé

Un multi-graphe dirigé est un couple $G = (V, E)$ tel que soit une liste de couples $(x, y)$ (que l'on notera $xy$) appartenant à $V^2$. Cette structure de graphe permet :

* d'avoir des arêtes dirigées ($xy$ étant différent de $yx$),
* d'avoir plusieurs fois la même arête ($$E$$ est une liste et non un ensemble)
  
### structure python

La structure python que nous utiliserons pour créer un graphe sera la liste d'adjacence. On va donc avoir besoin :

* d'une liste `vertices` de noms de sommets. On identifiera le sommet avec son indice dans cette liste.
* une liste `edges` de listes de voisins.

Par exemple, on pourra coder le graphe suivant :

![un graphe orienté]({{ "/assets/cours/graphes/graphe_oriente_boucle.png" | relative_url }}){:style="margin: auto;display: block;"}

Par la liste de sommets :

```python
vertices = ['a', 'b', 'c', 'd', 'e']
```

Et les arcs codées sous forme de [liste d'adjacence]({% link cours/graphes/encodage.md %}#liste-adjacence) :

```python
edges = [[1, 4],
         [1, 2],
         [3],
         [0],
         [3, 0]]
```

**Exemple :** le sommet d'indice 4 (c'est à dire le sommet de nom `vertices[4]`; donc `'e'`) à 2 voisins qui correspondent à `edges[4]`, c'est à dire les sommets d'indice 3 (`'d'`) et d'indice 0 (`'a`').

#### codage de la structure

Créez une méthode python `create_multi_graph(number_vertices, edges)` qui prend en paramètre une liste de couples et rend un multi-graphe. On supposera que les sommets sont déjà codés par des entiers allant de `0` à `number_vertices-1`.

On s'assurera de la validité de la structure choisie en faisant en sorte que les tests suivants passent.

Pour bien faire, créez votre structure de façon itérative en commençant par faire une structure qui fait passer le 1er test. Puis améliorez votre structure pour qu'elle fasse passer les 2 premiers tests, et ainsi de suite jusqu'à avoir une structure qui fasse passer tous les tests.

#### code

La structure de votre projet sera :

* un fichier *"multi_graph.py"* contenant tout le code relatif à la structure de multi-graphe,
* le fichier *"main.py"* contiendra le programme principal avec l'exemple finalisé
  
Tout ce qui concerne la structure de multi-graphe doit être stockée dans un fichier nommé *"multi_graph.py"*. Ce fichier sera importé dans le fichier *"main.py"* pour l'exécution du programme ou importé dans les fichiers de tests.

#### points critiques : tests et code

* les tests vous montrent l'implémentation demandée, sous la forme d'une liste de istes de sommets.
* on essaie (dans la mesure du possible) de coder en anglais. Vous aurez dans votre vie professionnels à travailler avec des personnes de nationalités différentes et l'anglais est la langue de communication.

#### tests

Les tests doivent être exécutés dans le fichier *test_multi_graph.py*, n'oubliez pas d'importer de *multi_graph.ph* les fonction que vous voulez tester, par exemple :

``` python
from multi_graph import create_multi_graph
```

> On déconseille fortement d'importer `*` (*ie.* toutes les fonctions), importez les une à une. Ca ne prend pas de temps avec *pycharm* et ça permet de savoir précisément ce qui est testé.

Les différents tests vont montrer comment organiser votre structure.

##### multi-graphe vide

``` python
def test_create_multi_graph_empty():
    assert create_multi_graph(0, []) == []

def test_create_multi_graph_empty_three_vertices():
    assert create_multi_graph(3, []) == [[], [], []]
```

##### multi-graphe une arête

``` python
def test_multi_graph_one_edge():
    assert create_multi_graph(2, [[0, 1]]) == [[1], []]
```

##### multi-graphe des arêtes

``` python
def test_multi_graph_several_edges():
    edges = [[0, 1], [1, 2], [1, 0], [0, 1], [3, 3]]
    assert create_multi_graph(4, edges) == [[1, 1], [2, 0], [], [3]]
```

#### usage

On a utilisé une structure sous la forme de listes pour stocker notre multi-graphe dirigé. En reprenant l'exemple du graphe :

![un graphe orienté]({{ "/assets/cours/graphes/graphe_oriente_boucle.png" | relative_url }}){:style="margin: auto;display: block;"}

codé en python :

```python
vertices = ['a', 'b', 'c', 'd', 'e']
edges = [[1, 4],
         [1, 2],
         [3],
         [0],
         [3, 0]]
```

On pourra facilement accéder à :

* tous ses sommets : `list(range(len(edges)))` ou `list(range(len(vertices)))` rendra une liste des indices des différents sommets
* savoir si $xy$ est une arête (avec $x$ et $y$ des indices) : `y in edges[x]` rendra `True`si $xy$ est une arête et `False` sinon.
* aux voisins de `x` : `list(g[x])` (avec `x` un indice). On copie la liste plutôt que d'utiliser celle de `edges` pour éviter les soucis.

> de part la structure proposée :
>
>* la complexité de `y in g[x]` est en $\mathcal{O}$(`len(g[x])`),
>* lorsque vous manipulez `g[x]` faites attention à ne pas la modifier sinon vous modifiez la structure du multi-graphe.
{: .attention}

## multi-graphes eulérien

Créez une fonction `is_eulerian(edges)` qui répond `True` si la liste d'adjacence en paramètre est eulérienne, et `False` sinon.

On rappelle qu'un multi-graphe est eulérien si chaque sommet à un nombre d'arêtes entrantes et d'arêtes sortantes égal.

Il faut que votre fonction passe les tests ci-après :

``` python
def test_is_eulerian_empty():
    assert is_eulerian([])


def test_is_eulerian_one_edge():
    assert is_eulerian(create_multi_graph(2, [[0, 1]])) is False


def test_is_eulerian_loop():
    assert is_eulerian(create_multi_graph(1, [[0, 0]]))


def test_is_eulerian_cycle():
    assert is_eulerian(create_multi_graph(3, [[0, 1], [2, 0], [1, 2]]))


def test_is_eulerian_no_eulerian():
    edges = create_multi_graph(4, [[0, 1], [1, 2], [2, 0], [1, 3]])
    assert is_eulerian(edges) is False
```

### Points critiques : eulérien

* on doit savoir si le nombre d'arêtes entrante est égal au nombre d'arêtes sortantes mais seule le nombre d'arête sortante est facilement accessible. Il faut donc commender par trouver ces nombres pour tous les sommets
* on doit répondre vrai que si l'on a vérifié le nombre d'arêtes sortantes et entrantes pour tous les sommets
   on peut coder l'algorithme en $$\mathcal{O}(|V| + |E|)$$ si $$G=(V, E)$$ est le multi-graphe.

## circuits dans un multi-graphe eulérien

On a vu en cours qu'un graphe dont le degré minimum est > 2 contient un cycle. La même démonstration permet de montrer que pour un multi-graphe connexe, si chaque sommet a au moins 1 arête entrante et 1 arête sortante, il existe un circuit.

### circuit

Avant de créer la vrai fonction, on va commencer par régler les cas particuliers. Créez un algorithme qui, a partir d'un multi-graphe eulérien (que l'on supposera connexe) :

* rend un circuit non vide sous la forme d'une liste si le graphe a au moins 1 arête,
* rend la liste si le graphe est sans arêtes.

Vous implémenterez cet algorithme dans la fonction `circuit_from_eulerian(edges)`. Elle doit satisfaire les tests suivants :

```python
def test_circuit_empty():
    assert circuit_from_eulerian([]) == []


def test_circuit_no_edge():
    assert circuit_from_eulerian([[], []]) == []


def test_circuit_loop():
    assert circuit_from_eulerian(create_multi_graph(1, [[0, 0]])) == [0]
```

### points critiques : circuits

* l'algorithme du cours est itératif mais sa boucle est une boucle `while` : on essaie d'étendre le chemin courant en cherchant un sommet qui n'est pas encore dans le chemin et qui forme une arête avec le dernier élément du chemin
* si l'on trouve une arête entre le dernier élément du chemin et un autre sommet du chemin on a trouvé un cycle. Mais ce cycle ne concerne pas forcément tous les éléments du chemin.
* si le multi-graphe ne contient pas de circuit faites en sorte que l'algorithme s'arrête tout de même en rendant `None` par exemple.

#### un circuit

Pour ces tests on a un petit soucis. Un graphe eulérien va avoir plein de circuits possibles. Il faut donc dans les tests prévoir tous les cas car on ne sait pas a priori quel chemin va trouver l'algorithme.

``` python
def test_circuit():
    assert circuit_from_eulerian(create_multi_graph(3, [[0, 1], [2, 0], [1, 2]])) in [[0, 1, 2], [1, 2, 0], [2, 0, 1]]
```

## copie de graphe

Pour trouver un circuit eulérien d'un graphe, il faut itérativement supprimer un cycle de celui-ci. On va donc commencer par créer une fonction qui duplique un graphe et appelez-la `copy_multi_graph(edges)`.

``` python
def test_copy_multi_graph():
    edges = create_multi_graph(1, [[0, 0]])
    copy_edges = copy_multi_graph(edges)
    assert copy_edges == edges

    edges[0].append("X")
    assert copy_edges != edges
```

### points critiques : copie

* la liste d'adjacence doit être copiée pas juste donnée au nouveau graphe. Les listes sont en effet des [objets](https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/1-starters/3-mutables-hashables/) (modifiables)

## suppression de circuit

Créez une fonction qui, à partir d'un multi-graph et d'un cycle rend un **autre** multi-graph correspondant au multi-graph d'origine auquel on a supprimé le cycle.

``` python
def test_delete_cycle():
    new_edges = delete_circuit([0, 1, 2], create_multi_graph(4, [[0, 1], [2, 0], [1, 2], [0, 3]]))
    assert new_edges == [[3], [], [], []]


def test_delete_cycle_different_graph():
    initial_graph = create_multi_graph(4, [[0, 1], [2, 0], [1, 2], [0, 3]])
    delete_circuit([0, 1, 2], initial_graph)
    
    assert initial_graph == create_multi_graph(4, [[0, 1], [2, 0], [1, 2], [0, 3]])
```

### points critiques : suppression de circuit

* utilisez les fonctions créées précédemment comme `copy_multi_graph`
* la structure de multi-graphe est stockée sous la forme de listes d'adjacence et le circuit est une succession d'arêtes

## suite de circuits

Pour trouver un circuit eulérien, le cours vous indique qu'il faut itérativement supprimer un cycle à un graphe eulérien jusqu'à ce qu'on ne puisse plus le faire.

Créez une fonction qui, à partir d'un multi-graphe eulérien, rend une suite de circuits permettant de recréer son circuit eulérien.

``` python
def test_list_of_circuits_empty():
    assert list_of_circuits([]) == []


def test_list_of_circuits_one_circuit():
    circuits = list_of_circuits(create_multi_graph(3, [[0, 1], [1, 2], [2, 0]]))

    assert len(circuits) == 1
    assert set(circuits[0]) == {0, 1, 2}


def test_list_of_circuits_several_circuits():
    circuits = list_of_circuits(create_multi_graph(3, [[0, 1], [1, 2], [2, 0], [0, 0]]))

    assert len(circuits) == 2
    assert {frozenset(circuits[0]), frozenset(circuits[1])} == {frozenset({0, 1, 2}), frozenset({0})}
```

### points critiques : suite de circuits

* on a créé pratiquement toutes les fonctions utiles à cet algorithme.
* une liste vide en python est considérée comme `False` pour ce qui est de tests booléens.
* le dernier test est un peu tricky, car il ne compare pas des listes de listes mais des ensembles d'ensembles. On est obligé de faire comme ça car on ne sais pas a priori dans quel ordre l'algorithme va trouver les cycles ni dans quel ordre il va les écrire (`[0, 1, 2]` et `[2, 0, 1]` correspondent au même circuit et sont tous les deux représentés par l'ensemble `{0, 1, 2}`)
* un `set` est mutable et ne peut contenir comme élément que des objets non mutable. On utilise ainsi dans les tests des `frozenset` qui sont des objets ensembles non mutable. Voir [là](https://www.python-course.eu/sets_frozensets.php) par exemple pour une petite étude sur leurs différences.
* en python `{0, 1, 2, 3}` est un ensemble.

## raboutage de 2 circuits en un circuit plus gros

Maintenant qu'on a une liste de circuits d'un multi-graphe eulérien, il faut les rabouter petit à petit pour obtenir un circuit eulérien. Commençons par rabouter 2 circuits en 1 seul.

``` python
def test_raboutage_left_empty():
    assert raboutage([], [0, 1]) == [0, 1]


def test_raboutage_right_empty():
    assert raboutage([0, 1], []) == [0, 1]


def test_raboutage():
    assert raboutage([0], [0, 1]) in [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
```

### points critiques

* il faut trouver un élément commun aux deux circuits. On peut faire ça facilement en intersectant les ensembles créés à partir des listes de sommets des deux circuits.
* en manipulant les [slycing](https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/) des listes, rabouter ceux cycles devient facile.

## raboutage de circuits en un circuit eulérien

Prenez un muti-graphe euliérien et rendez un de ses circuits eulériens

``` python
def test_eulerian_circuit_empty():
    assert eulerian_circuit([]) == []


def test_eulerian_circuit_one_loop():
    assert eulerian_circuit(create_multi_graph(1, [[0, 0]])) == [0]


def test_eulerian_circuit():
    assert eulerian_circuit(create_multi_graph(2, [[0, 1], [1, 0], [0, 0]])) in ([0, 1, 0], [0, 0, 1], [1, 0, 0])
```

### points critiques : raboutage de circuits

* si vous êtes arrivé jusque là vous avez codé toutes les fonctions utile à cet algorithme.
* faite grossir un circuit initialement vide en le raboutant.

## processus complet dans le main

Et [voilà, c'est fini](https://www.youtube.com/watch?v=EVDlleOUQXY), il ne vous reste plus qu'à faire votre programme principal qui, à partir d'un multi-graphe vérifie qu'il est eulérien et si c'est le cas, rend un circuit eulérien du graphe.

Pour cela, prenez un graphe du court permettant de trouver une [suite de Brujin](https://fr.wikipedia.org/wiki/Suite_de_de_Bruijn) (c'est une variante des mots de brujin vus en cours) des mots de longueur 3 de l'alphabet ${0, 1}$

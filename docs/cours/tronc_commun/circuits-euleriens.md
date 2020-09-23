---
layout: page
title:  "circuits eulérien"
category: cours
tags: informatique code graphes
author : "François Brucker"
---

## Introduction

Le but de ce cours est d'apprendre à coder un (multi-)graphe dirigé et de s'en servir pour trouver un circuit eulérien d'un de ces graphes (s'il existe). .


## Outils

Vous aurez besoin d'un environnement de développement fonctionnel (suivez [ce tuto]({% link cours/tuto/anaconda-pycharm-pytest.md %}), si ce n'est pas déjà fait).
Lorsque l'on vous demandera de *faire passer un test*, il faudra ajouter le test à votre fichier de test, comme indiqué dans le [tuto sur les tests]({% link cours/tuto/tests-unitaires.md %}).

Les tests vont s'ajouter petit à petit et à la fin de la séance votre fichier *test_multi_graph.py* contiendra plus d'une vingtaine de tests ! 

## Plan

  1. modéliser un multi-graphe dirigé en python
  2. algorithme du circuit eulérien
  3. suppression itératives de circuits à un multi-graphe eulérien
  4. création d'un multi-graphe à partir d'une suite de circuits
  5. le programme qui trouve un circuit eulérien d'un multi-graphe donné.

## code

Les fonctions que l'on vous demande de coder sont la plupart du temps simple, mais certaines nécessitent de réfléchir et — surtout — de se tromper un peu avant de voir la lumière. Comme cous avez le corrigé et les tests que l'on vous demande de faire passer, vous savez lorsque vous avez bon. On vous demande donc :

  - de ne pas regarder la solution avant que vous ayez fait passer les tests
  - de vous creuser la tête pour faire marcher l'algorithme
  - de bien nommer vos variables et de séparer par des retours à la lignes les différentes parties de l'algorithme

## multi-graphe dirigé

Un multi-graphe dirigé est un couple $$ G = (V, E) $$ tel que soit une liste de couples $$(x, y)$$ (que l'on notera $$xy$$) appartenant à $$V^2$$. Cette structure de graphe permet :

  - d'avoir des arêtes dirigées ($$xy$$ étant différent de $$yx$$),
  - d'avoir plusieurs fois la même arête ($$E$$ est une liste et non un ensemble)
  
  
### structure python

Créez une méthode python `create_multi_graph(edges)` qui prend en paramètre une liste de couples et rend un multi-graphe. On s'assurera de la validité de la structure choisie en faisant en sorte que les tests suivants passent. 

Pour bien faire, créez votre structure de façon itérative en commençant par faire une structure qui fait passer le 1er test. Puis améliorez votre structure pour qu'elle fasse passer les 2 premiers tests, et ainsi de suite jusqu'à avoir une structure qui fasse passer tous les tests.

> **Bota Bene :** si le graphe ne prend qu'une suite d'arêtes en paramètre, on ne pourra pas créer de graphes avec des sommets isolés. Pour notre application, les circuits eulériens, ce n'est pas très grave, mais autant le noter.


#### code

La structure de votre projet sera :

  - un fichier *multi_graph.py* contenant tout le code relatif à la structure de multi-graphe,
  - le fichier *main.py* contiendra le programme principal avec l'exemple finalisé
  
Tout ce qui concerne la structure de multi-graphe doit être stockée dans un fichier nommé *multi_graph.py*. Ce fichier sera importé dans le fichier *main.py* pour l'exécution du programme ou importé dans les fichiers de tests.

#### Points critiques 

  - Les tests vous montrent l'implémentation demandée, sous la forme d'un dictionnaire les sommets étant les clés et les arêtes les valeurs codées sous la forme d'une [liste d'adgacence](https://fr.wikipedia.org/wiki/Liste_d%27adjacence).
  - on essaie (dans la mesure du possible) de coder en anglais. Vous aurez dans votre vie professionnels à travailler avec des personnes de nationalités différentes et l'anglais est la langue de communication. 

#### tests

Les tests doivent être exécutés dans le fichier *test_multi_graph.py*, n'oubliez pas d'importer de *multi_graph.ph* les fonction que vous voulez tester, par exemple :

~~~ python
from multi_graph import create_multi_graph
~~~

> **Nota Bene :** On déconseille fortement d'importer `*` (*ie.* toutes les fonctions), importez les une à une. Ca ne prend pas de temps avec *pycharm* et ça permet de savoir précisément ce qui est testé.

Les différents tests vont montrer comment organiser votre structure.


##### multi-graphe vide

~~~ python
def test_create_multi_graph_empty():
    assert create_multi_graph([]) == dict()
~~~

##### multi-graphe une arête

~~~ python
def test_multi_graph_one_edge():
    assert create_multi_graph([[1, 2]]) == {1: [2], 2: []}
~~~


##### multi-graphe des arêtes

~~~ python
def test_multi_graph_several_edges():
    assert create_multi_graph([[1, 2], [2, 3], [2, 1], [1, 2], [4, 4]]) == {1: [2, 2], 
                                                                            2: [3, 1], 
                                                                            3: [], 
                                                                            4: [4]}
~~~


#### usage

On a utilisé une structure sous la forme d'un [dictionnaire](https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries) pour stocker notre multi-graphe dirigé.

Par exemple, le multi-graphe dirigé de la figure ci-dessous 

![un multi-graphe]({{ "./multi-graphe.png" }})

s'écrira en python : 

~~~ python
{"a": ["b", "e"],
 "b": ["b", "b", "c"],
 "c": ["d"],
 "d": ["a"],
 "e": ["d", "a"],
}
~~~

On pourra alors facilement accéder à la structure d'un multi-graphe `g`:

  - tous ses sommets : `set(g.keys())` sera l'ensemble de ses sommets
  - savoir si $$xy$$ est une arête de `g` : `"y" in g["x"]`
  - les voisins de `"x"` : `list(g["x"])`

>**Attention :** de part la structure proposée :
>  - la complexité de `"y" in g["x"]` est en $$\mathcal{O}$$(`len(g["x"])`),
>  - lorsque vous manipulez `g["x"]` faites attention à ne pas le modifier sinon vous modifiez la structure du multi-graphe.
 
## multi-graphes eulérien

Créez une fonction `is_eulerian(multi_graph)` qui répond `True` si le graphe en paramètre est eulérien, et `False` sinon.

On rappelle qu'un multi-graphe est eulérien si chaque sommet à un nombre d'arêtes entrantes et d'arêtes sortantes égal. 

Il faut que votre fonction passe les tests ci-après

### Points critiques 

  - on doit savoir si le nombre d'arêtes entrante est égal au nombre d'arêttes sortantes mais seule le nombre d'arête sortante est facilement accessible. Il faut donc commender par trouver ces nombres pour tous les sommets
  - on doit répondre vrai que si l'on a vérifié le nombre d'arêtes sortantes et entrantes pour tous les sommets
  - on peut coder l'algorithme en $$\mathcal{O}(|V| + |E|)$$ si $$G=(V, E)$$ est le multi-graphe.

### tests

#### graphe vide

~~~ python
def test_is_eulerian_empty():
    assert is_eulerian(dict())
~~~

### graphe 1 arête

~~~pyhton
def test_is_eulerian_one_edge():
    assert is_eulerian(create_multi_graph([[1, 2]])) is False
~~~

### graphe boucle

~~~pyhton
def test_is_eulerian_loop():
    assert is_eulerian(create_multi_graph([[1, 1]]))
~~~

### un circuit

~~~pyhton
def test_is_eulerian_cycle():
    assert is_eulerian(create_multi_graph([[1, 2], [3, 1], [2, 3]]))
~~~


### pas eulérien plus gros

~~~pyhton
def test_is_eulerian_no_eulerian():
    assert is_eulerian(create_multi_graph([[1, 2], [2, 3], [3, 1], [2, 4]])) is False
~~~


## circuits dans un multi-graphe eulérien.

On a vu en cours qu'un graphe dont le degré minimum est > 2 contient un cycle. La même démonstration permet de montrer que pour un multi-graphe connexe, si chaque sommet a au moins 1 arête entrante et 1 arête sortante, il existe un circuit.

### circuit

Créez un algorithme qui, a partir d'un multi-graphe eulérien (que l'on supposera connexe) :

  - rend un circuit non vide sous la forme d'une liste si le graphe a au moins 1 arête,
  - rend la liste si le graphe est sans arêtes.

Vous implémenterez cet algorithme dans la fonction `circuit_from_eulerian(multi_graph)`

### points critiques

  - l'algorithme du cours est itératif mais sa boucle est une boucle `while` : on essaie d'étendre le chemin courant en cherchant un sommet qui n'est pas encore dans le chemin et qui forme une arête avec le dernier élément du chemin
  - si l'on trouve une arête entre le dernier élément du chemin et un autre sommet du chemin on a trouvé un cycle. Mais ce cycle ne concerne pas forcément tous les éléments du chemin.
  - si le multi-graphe ne contient pas de circuit faites en sorte que l'algorithme s'arrête tout de même en rendant `None` par exemple.

### test


#### vide 

~~~pyhton
def test_circuit_empty():
    assert circuit_from_eulerian(dict()) == []
~~~

#### sans arêtes

~~~pyhton
def test_circuit_no_edge():
    assert circuit_from_eulerian({1: [], 2: []}) == []
~~~

#### une boucle

~~~pyhton
def test_circuit_loop():
    assert circuit_from_eulerian(create_multi_graph([[1, 1]])) == [1]
~~~

#### un circuit

Pour ces tests on a un petit soucis. Un graphe eulérien va avoir plein de circuits possible. Il faut donc dans les tests prévoir tous les cas car on ne sait pas a priori quel chemin va trouver l'algorithme.

~~~ pyhton
def test_circuit():
    assert circuit_from_euleriancreate_multi_graph([[1, 2], [3, 1], [2, 3]])) in [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
~~~


## copie de graphe

Pour trouver un circuit eulérien d'un graphe, il faut itérativement supprimer un cycle de celui-ci. On va donc commencer par créer une fonction qui duplique un graphe et appelez-la `copy_multi_graph(multi_graph)`. 

### points critiques

  - la liste d'adjacence doit être copiée pas juste donnée au nouveau graphe. Les listes sont en effet des [objets](https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/1-starters/3-mutables-hashables/) (modifiables)
  - regardez du côté de la méthode [.items()](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques) des dictionnaires.

### tests 

Pour vérifier que tout fonctionne assurez vous que le test suivant passe.

~~~ python
def test_copy_multi_graph():
    graph = create_multi_graph([[1, 1]])
    copy_graph = copy_multi_graph(graph) 
    assert copy_graph == graph
    
    graph[1].append("X")
    assert copy_graph != graph
~~~

## suppression de circuit

Créez une fonction qui, à partir d'un multi-graph et d'un cycle rend un **autre*** multi-graph correspondant au multi-graph d'origine auquel on a supprimé le cycle. 

### points critiques

  - utilisez les fonctions créees précédemment comme `copy_multi_graph`
  - la structure de multi-graphe est stockées sous la forme de listes d'adjacence et le circuit est une succession d'arêtes
  - la méthode [.remove()](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) des listes peut être super utile.

### tests 

Vérifiez qu'elle fonctionne avec les tests suivants :


~~~ python
def test_delete_cycle():
    assert delete_circuit([1, 2, 3], create_multi_graph([[1, 2], [3, 1], [2, 3], [1, 4]])) == {1: [4], 2: [], 3: [], 4: []} 
~~~

~~~ python
def test_delete_cycle_different_graph():
     
    initial_graph = create_multi_graph([[1, 2], [3, 1], [2, 3], [1, 4]])
    delete_circuit([1, 2, 3], create_multi_graph([[1, 2], [3, 1], [2, 3], [1, 4]]))
    
    assert initial_graph == create_multi_graph([[1, 2], [3, 1], [2, 3], [1, 4]])
~~~

## suite de circuits

Pour trouver un circuit eulérien, le cours vous indique qu'il faut itérativement supprimer un cycle à un graphe eulérien jusqu'à ce qu'on ne puisse plus le faire.

Créez une fonction qui, à partir d'un multi-graphe eulérien, rend une suite de circuits permettant de recréer son circuit eulérien.

### points critiques

  - on a créé pratiquement toutes les fonctions utiles à cet algorithme.
  - une liste vide en python est considérée comme `False` pour ce qui est de tests booléens.
  - le dernier test est un peu tricky, car il ne compare pas des listes de listes mais des ensembles d'ensemble. On est obligé de faire comme ça car on ne sais pas a priori dans quel ordre l'algorithme va trouver les cycle ni dans quel ordre il va les écrire (`[1, 2, 3]` et `[3, 1, 2]` correspondent au même circuit et sont tous les deux représenté par l'ensemble `{1, 2, 3}`)
  - un `set` est mutable et ne peut contenir comme éléments que des objets non mutable. On utilise ainsi dans les tests des `frozenset` qui sont des objet ensemble non mutable. Voir [là](https://www.python-course.eu/sets_frozensets.php) par exemple pour une petite étude sur leurs différence.
  - en python `{1, 2, 3, 4}` est un ensemble et `{1: 2, 3: 4}` un dictionnaire avec deux clés 1 et 3.

### tests

Testez ces fonctions avec les deux tests suivants :

#### liste déjà vide

~~~ python
def test_list_of_circuits_empty():
    assert list_of_circuits(dict()) == []
~~~

#### un circuit

~~~ python
def test_list_of_circuits_one_circuit():
    circuits = list_of_circuits(create_multi_graph([[1, 2], [2, 3], [3, 1]]))

    assert len(circuits) == 1
    assert set(circuits[0]) == {1, 2, 3}
~~~


#### plusieurs circuits

~~~ python
def test_list_of_circuits_several_circuits():
    circuits = list_of_circuits(create_multi_graph([[1, 2], [2, 3], [3, 1], [1, 1]]))

    assert len(circuits) == 2
    assert {frozenset(circuits[0]), frozenset(circuits[1])} == {frozenset({1, 2, 3}), frozenset({1})}
~~~

## raboutage de 2 circuits en un circuit plus gros

Maintenant qu'on a une liste de circuits d'un multi-graphe eulérien, il faut les rabouter petit à petit pour obtenir un circuit eulérien. Commençons par rabouter 2 circuits en 1 seul.

### points critiques

  - il faut trouver un élément commun aux deux circuits. On peut faire ça facilement en intersectant les ensembles crées à parrir des listes de sommets des deux circuits.
  - en manipulant les [slycing](https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/) des listes, rabouter ceux cycle devient facile.

### tests

#### un circuit vide

~~~ python
def test_raboutage_left_empty():
    assert raboutage([], [1, 2]) == [1, 2]


def test_raboutage_right_empty():
    assert raboutage([1, 2], []) == [1, 2]
~~~


#### deux circuits 

~~~ python
def test_raboutage():
    assert raboutage([1], [1, 2]) in [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
~~~


## raboutage de circuits en un circuit eulérien

Prenez un muti-graphe euliérien et rendez un de ses circuits eulérien

### points critiques

  - si vous êtes arrivé jusque là vous avez codé toutes les fonctions utile à cet algorithme.
  - faite grossir un circuit initalement vide en le raboutant le raboutage itératif des circuits peut se faire en parcourant les éléments de la liste des circuits et 

### tests 

#### graphe vide

~~~ python
def test_eulerian_circuit_empty():
    assert eulerian_circuit(dict()) == []
~~~


#### une boucle

~~~ python
def test_eulerian_circuit_one_loop():
    assert eulerian_circuit(create_multi_graph([[1, 1]])) == [1]
~~~

#### 2 circuits

~~~ python
def test_eulerian_circuit():
    assert eulerian_circuit(create_multi_graph([[1, 2], [2, 1], [1, 1]])) in ([1, 2, 1], [1, 1, 2], [2, 1, 1])
~~~


## processus complet dans le main

Et [voilà, c'est fini](https://www.youtube.com/watch?v=EVDlleOUQXY), il ne vous reste plus qu'à faire votre programme principal qui, à partir d'un multi-graphe vérifie qu'il est eulérien et si c'est le cas, rend un circuit eulérien du graphe.

Pour cela, prenez un graphe du court permettant de trouver une [suite de Brujin](https://fr.wikipedia.org/wiki/Suite_de_de_Bruijn) (c'est une variante des mots de brujin vus en cours) des mots de longueur 3 de l'alphabet $${0, 1}$$

## un corrigé du code

Le code complet de ce tuto est disponible sur [le github du projet](https://github.com/FrancoisBrucker/cours_informatique/tree/master/docs/cours/tronc_commun/circuits-euleriens-code).



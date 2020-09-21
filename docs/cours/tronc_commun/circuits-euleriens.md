---
layout: page
title:  "circuits eulérien"
category: cours
tags: informatique code graphes
---

## Introduction

Le but de ce cours est d'apprendre à coder un (multi-)graphe dirigé et de s'en servir pour trouver un circuit eulérien d'un de ces graphes (s'il existe). On appliquera cet algorithme à la découvertes de [suites de Brujin](https://fr.wikipedia.org/wiki/Suite_de_de_Bruijn) d'un alphabet donné.


## Outils

Vous aurez besoin d'un environnement de développement fonctionnel (suivez [ce tuto]({% link cours/tuto/anaconda-pycharm-pytest.md %}), si ce n'est pas déjà fait).
Lorsque l'on vous demandera de *faire passer un test*, il faudra ajouter le test à votre fichier de test, comme indiqué dans le [tuto sur les tests]({% link cours/tuto/tests-unitaires.md %})

## Plan

  1. modéliser un multi-graphe dirigé en python
  2. algorithme du circuit eulérien
  3. tbd
  
## multi-graphe dirigé

Un multi-graphe dirigé est un couple $$ G = (V, E) $$ tel que soit une liste de couples $$(x, y)$$ (que l'on notera $$xy$$) appartenant à $$V^2$$. Cette structure de graphe permet :

  - d'avoir des arêtes dirigées ($$xy$$ étant différent de $$yx$$),
  - d'avoir plusieurs fois la même arête ($$E$$ est une liste et non un ensemble)
  
### structure python

Créez une méthode python `create_multi_graph(edges)` qui prend en paramètre une liste de couples et rend un multi-graphe. On s'assurera de la validité de la structure choisie en faisant en sorte que les tests suivants passent. 

Pour bien faire, créez votre structure de façon itérative en commençant par faire une structure qui fait passer le 1er test. Puis améliorez votre structure pour qu'elle fasse passer les 2 premiers tests, et ainsi de suite jusqu'à avoir une structure qui fasse passer tous les tests.

> **Bota Bene :** si le graphe ne prend qu'une suite d'arêtes en paramètre, on ne poura pas créer de graphes avec des sommets isolés. Pour notre application, les circuits eulériens, ce n'est pas très grave, mais autant le noter.


#### code

La structure de votre projet sera :

  - un fichier *multi_graph.py* contenant tout le code relatif à la structure de multi-graphe,
  - le fichier *main.py* contiendra le programme principal avec l'exemple finalisé
  
Tout ce qui concerne la structure de multi-graphe doit être stockée dans un fichier nommé *multi_graph.py*. Ce fichier sera importé dans le fichier *main.py* pour l'exécution du programme ou importé dans les fichiers de tests.

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

##### multi-graphe plusieurs fois la même arête

##### multi-graphe des arêtes  opposées

#### correspondance tructure python et structure "tableau"

A quoi doit correspondre la structure python du graphe suivant : 



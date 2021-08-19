---
layout: page
title:  "Tests unitaires en Python avec pytest et pycharm"
category: tests unitaires
tags: pytest unittest
---

Mise en œuvre de tests unitaires en python avec l'éditeur pycharm.
<!--more-->

# Introduction


Nous devons être certains que toutes les méthodes, fonctions ou modules que nous créons sont corrects. On écrira donc des tests pour être moralement sûrs que nos programmes fonctionnent (la plupart du temps une preuve de code est illusoire). 

Pour éviter de retaper tous ces tests à chaque modification du code (ce qui arrive souvent lorsqu'un algorithme ou une application est utilisée longtemps) ou à chaque découverte de bug, ils sont conservés dans un fichier à part. Ceci nous permettra d'exécuter ces tests à loisir (c'est à dire très souvent) et d'être sûrs que **tous** les tests seront exécutés. Ces  [tests sont dit unitaires]([https://fr.wikipedia.org/wiki/Test_unitaire) et sont essentiels dans toutes les pratiques courantes de code.


De nombreux frameworks de tests existent pour python, le plus connu étant certainement [unittest](https://docs.python.org/3/library/unittest.html), ou encore [nose](http://nose.readthedocs.io/en/latest/). Nous allons utiliser [pytest](http://pytest.org).

> **Nota Bene :**
>Une très bonne introduction au développement par les tests est l'inusable Test Driven Development: By Example de Kent Beck. Tous les exemples sont en revanche en Java.
> Sinon en python mais orienté développement web, il y a le bon (mais il faut s'accrocher si on débute) "Test-Driven Development with Python" de Harry J.w Percival.


# Un exemple

Créez un nouveau projet avec pycharm que l'on pourra appeler `essai_tests`, puis ajoutez-y un fichier que vous nommerez `aide_mathematiques.py`. Ce fichier contiendra le code suivant :
~~~ python

def double(entier):
  return 2 * entier
~~~

Pour tester ce code, j'imagine que si les deux conditions suivantes sont remplies :
  - `double(0)` vaut `0`,
  - `double (21)` vaut `42`

Ma méthode sera exacte. 

On utilise le mot clé [assert](http://www.tutorialspoint.com/python/assertions_in_python.htm) pour créer notre fonction de test. 

> **Attention :**
> Les fonctions de tests doivent toutes commencer par ''test_''.
>

Ajouter la méthode ci-après à votre fichier :

~~~ python

def test_double():
  assert double(0) == 0
  assert double(21) == 42

~~~

et exécutez là : 

~~~ python

test_double()
~~~


Si tout s'est passé comme prévu, il ne s'est rien passé. Normal, l' `assert` était vérifié. Changez un des `assert` de la fonction `test_double` pour que le résultat soit faux (par exemple `assert double(0) == 7`). Le programme doit maintenant s'arrêter sur une exception. Chez moi, j'obtiens ça :

~~~
Traceback (most recent call last):
  File "/Users/francois/Documents/pycharm/essai_tests/aide_mathematiques.py", line 10, in <module>
    test_double()
  File "/Users/francois/Documents/pycharm/essai_tests/aide_mathematiques.py", line 6, in test_double
    assert double(0) == 7
AssertionError
~~~

Ainsi, si tout se passe bien, nos tests sont passés, si le programme s'arrête sur une exception de type `AssertionError`, nos tests ne correspondent pas à la réalité. Nous sommes en face d'un bug (qu'il faut corriger).

# Séparer code et tests 

Placez la fonction de test (et son exécution) dans un fichier que vous nommerez `test_aide_mathematiques.py`. 

Faites en sorte qu'il s'exécute sans problème (attention aux `import`. Vous pouvez [lire la doc officielle](https://docs.python.org/fr/3.7/tutorial/modules.html),  un [petit tuto bien fait](https://www.learnpython.org/en/Modules_and_Packages) ou encore [le tuto de sam&max](http://sametmax.com/les-imports-en-python/) qui est un peu vieux (en particulier la partie absolue_import n'est plus du `__future__` mais est implémenté dans python3) mais toujours éclairant).

> **Attention :**
>On séparera toujours les tests du code. Tout fichier de test commence par ''test_''.
>


# Utilisation de l'environnement de test avec pycharm


Nous allons demander à l'environnement [py.test](http://pytest.org/latest/) d'exécuter nos tests. Il nous donnera plus d'informations sur les tests réussis ou échoués (une application normale contient des centaines de tests). 

Commencez par supprimer l'exécution de `test_double` dans le fichier `test_aide_mathematiques.py`. 

>**Attention :**
>Un fichier de tests ne doit contenir que des fonctions.
>


Puis nous allons demander à [Pycharm](https://www.jetbrains.com/pycharm/) d'exécuter `test_aide_mathematiques.py` à l'aide de notre environnement de test.



 Pour cela, créez un environnement d'exécution (expliqué dans ce [tuto]({% link cours/tuto/anaconda-pycharm-pytest.md %})) et créez une configuration  *pyhton test > pytest*. Ici, les paramètres dont nous aurons besoin sont :
 
  - le champ *name*, qui donne un nom à notre contexte. Par exemple *"mes tests"*
  - le champ *target*, qui spécifie quel script utiliser. Cliquez tout à droite de ce champ sur un petit bouton avec *…* puis choisissez le fichier `test_aide_mathematiques.py`

Une fois ceci configuré, cliquez sur *OK*.


Un nouvel environnement de tests est créé dans le menu *run*. Exécutez le. Vous devriez voir une nouvelle fenêtre en bas de l'écran pycharm apparaître et vos tests s'exécuter. Si tout s'est bien passé, une barre verte doit apparaître.

Pour finir cette partie :

  - Séparez votre fonction de tests en 2 fonctions (chaque fonction de test ne doit contenir qu'une chose à tester, donc a priori qu'un seul `assert`).
  - Exécutez votre nouvel environnement.
  - Ajoutez une fonction de test qui plante. Exécutez votre environnement de test. Voyez la barre rouge. Supprimez ce test non valide.


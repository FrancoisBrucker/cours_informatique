---
layout: page
title:  "pratiques de développement"
category: cours
tags: informatique cours 
author: "François Brucker"
---

## Introduction

On va implémenter des algorithmes en vrai et en python. On en profitera pour voir toutes les étapes d'un bon code.

On va se concentrer sur 3 points :

* on veut que notre code soit juste
* on veut pouvoir le modifier/ajouter des fonctionnalités rapidement
* on veut pouvoir partager notre code avec soit-même dans d'autres projet, son équipe ou le monde)

Le langage d'application n'a que peut d'intérêt en soit. On choisit celui qui est le plus adapté à notre but. Ici, on retranscrit de petit algorithmes, le python est idéal.

Écrire du code nécessite ne nombreuses automatisations et aides pour que ce ne soit pas pénible, ne vous privez pas d'outils parce que vous n'avez pas envie d'apprendre de nouvelles choses et que *ça suffit bien pour ce que je veux faire*. Vous allez au final perdre plus de temps que l'apprentissage initial (ce qui est tarte). Nos allons utiliser [visual studio code](https://code.visualstudio.com/) pour nos codes. Il permet de vous donner rapidement de bonnes habitudes de développement. 

## outils de développement

### un interpréteur python qui fonctionne

VOus pouvez soit utiliser l'interpréteur de votre système soit l'installer à la main.Une solution courante et pratique est d'installer [Anaconda](https://www.anaconda.com/) (voir [le début de ce tuto]({% link cours/tuto/anaconda-pycharm-pytest.md %}))


### interpréteur python

Le langage python n'est qu'une façon parmi d'autres de décrire et d'écrire des algorithmes. 

L'interpréteur python est le logiciel qui permet de transcrire le langage python en langage machine exécutable. On accède à l'interpréteur python en exécutant le programme `python3` (ou juste `python` si vous êtes sous windows) depuis une fenêtre terminal.

Ce programme python est utilisable essentiellement de 2.5 manières en [ligne de commande](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande) (voir <https://informatique.centrale-marseille.fr/tutos/post/initiation-linux.html> pour une aide sur le terminal unix, ou <https://www.varonis.com/blog/windows-powershell-tutorials/> pour le powershell windows) : 

* on exécute l'application `python3` dans un terminal. On est ensuite devant une ligne finissant par `>>>`. En tapant une ligne du langage python, elle est exécutée immédiatement, puis est à nouveau affiché les `>>>`. Comme chaque ligne est directement exécutée, il est très difficile d'écrire plus d'une ligne de code. 
* on exécute la commande `python3 mon_programme.py` où `mon_programme.py`est un fichier python dans le même dossier que votre terminal (le début de la ligne vous dit où est le terminal)
* `python3 -m une_bibliothèque_python` Utilisé pour exécuter des utilitaires python comme `pip3` pour installer un package ou les bibliothèques de tests

*Note Bene* : Un terminal est disponible dans la version pro de pycharm : <https://www.jetbrains.com/help/pycharm/working-with-system-console.html>


### visual code studio (vscode)

Nous allons juste nous concentrer sur la partie [python de vscode](https://code.visualstudio.com/docs/python/python-tutorial) en créant un projet de test et en utilisant tous les outils mis à notre disposition pour faire du bon code.

## un projet test

On va juste créer un projet vide pour comprendre comment tout ça fonctionne.

### fichier python

Commencez par télécharger l'extension [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) pour vcs.

Puis on crée notre projet python :

1. On choisit d'ouvrir un nouveau dossier. Je l'ai appelé `hello`
2. dans le tab de gauche (nommé *EXPLORER*), on clique sur *hello* pour ouvrir le tab puis *clique droit > new file* que l'on nomme *main.py*
3. vscode doit comprendre que c'est du python et vous demande peut-être de :
   1. choisir un interpréteur : prenez le python3 de votre distribution
   2. choisir un lint : supprimer la fenêtre de warning, on fera ça plus tard.
   3. choisir des tests : supprimer la fenêtre de warning, on fera ça plus tard.

### exécution d'un fichier

On écrit *main.py* :

```python
print("bonjour les gens !")

```

Et on sauve. Ou bien on met en route l'autosave (*file > autosave*)

On peut ensuite exécuter notre code de plusieurs façons :

* on clique sur le triangle vert en haut à droite de la fenêtre : une sous-fenêtre apparaît avec marqué `TERMINAL` et notre fichier est passé à l'interpréteur python. Chez moi j'ai marqué ça : 
  ```text
  fbrucker@emma  » /usr/local/bin/python3 "/Users/fbrucker/projets/hello/main.py"
  Bonjour les gens !
  ```
* on exécute notre fichier via l'interpréteur directement dans un terminal : `python3 main.py` (ou `python main.py` sous windows). Tout devrait bien se passer si :
    1. `python3` est reconnu (ou `python` sous windows)
    2. vous êtes bien dans le dossier contenant votre fichier `main.py`.


### linter

[linter](https://code.visualstudio.com/docs/python/linting)

Le linter est une aide pour écrire du code qui est à la fois fonctionnel et lisible. Cela permet de supprimer la majorité des problèmes avant l'exécution.

On va utiliser [pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html) qui permet de respecter la [PEP8](https://www.python.org/dev/peps/pep-0008/).

On commence par l'installer avec la commande : `pip3 install pycodestyle` (ou `pip install pycodestyle` sous windows).

Placez vous ous dans l'onglet correspondant à votre code et mettez en route le linter. POur cela :
1. on le choisit en tapant la commande (crtl/cmd+shift+P) : *Python: Select Linter* et on choisit `pycodestyle`
2. on le met en route si ce n'est pas déjà le cas avec la commande : *python: Enable Linter*.

Une fois le fichier sauvé, on voit s'il y a des soucis ou pas. Créons en un pour voir si le linter fonctionne : 


```python
print ("bonjour les gens !")

```


Une fois le fichier sauvé vous devriez voir que print est souligné en rouge. En passant sa souris dessus on voit pourquoi : `whitespace before '(' pycodestyle(E211)`

>**Conclusion** : **NE JAMAIS METTRE D'ESPACE APRÈS UN NOM DE FONCTION** c'est mal car on ne sais pas si c'est une fonction ou un nom de variable.

Vous devriez peut-être aussi avoir la parenthèse de fin souligné en jaune. C'est parce que la dernière ligne de votre fichier n'est pas vide. Si ce n'est pas le cas, c'es que vous avez bien que 2 lignes dans votre fichier, la seconde étant vide.

### séparer code et main

on va créer deux fichiers, l'un nommé *"le_code.py"* qui contiendra notre code et l'autre nommé *"main.py"* qui sera notre programme principal

*le_code.py* :

```python
def bonjour():
    return "Bonjour les gens !"

``` 

*main.py* :

```python
from le_code import bonjour

print(bonjour())

``` 

On a importer le nom `bonjour` défini dans le fichier *"le_code.py"* grace à un import. L'autre façon aurait été d'importer juste le fichier code. On aurait alors eu :

```python
import le_code

le_code.bonjour()

``` 

La notation pointée se lit alors : exécute le nom `bonjour` définit dans *"le_code"*.

>**ATTENTION** : ne jamais jamais jamais utiliser `from le_code import *` qui importe tous les noms définis dans *"le_code.py"*. On ne sais pas vraiment ce qui a été importé en lisant *"le_code.py"*: notre code n'est pas lisible ! Le gain d'écriture de `*` plutôt que `bonjour` sera perdu au centuple plus tard lorsque l'on devra chercher dans tous les fichiers du projet où l'on a bien pu définir `bonjour`...

En code comme dans la vie, il faut faire rapidement ce que l'on fait souvent. Comme on va passer plus de temps à lire/comprendre du code qu'à l'écrire, il faut optimiser la lecture et non l'écriture. D'où l'utilisation de nom explicites et on préférera toujours la lisibilité à la rapidité.


### tests

[tests](https://code.visualstudio.com/docs/python/testing). 

#### test des tests

On y reviendra plus tard et à de nombreuses reprise, les tests sont partie intégrante d'une bonne programmation. 

On va juste ici vérifier que tout fonctionne. Il existe de nombreuse bibliothèques de tests possible pour python. Nous allons utiliser [pytest](https://docs.pytest.org/en/stable/). Commençons par l'installer : `pip3 install pytest` (ou `pip install pytest` sous windows).

Le boulot d'une bibliothèque de test est d'exécuter toutes les fonction commençant par `test_` de tous les fichiers commençant par `test_` d'un projet.

Les tests sont de petites fonction dont le but est de *tester* une fonctionnalité du programme( souvent l'exécution d'une fonction). On utilisera l'instruction [assert](https://docs.python.org/fr/3/reference/simple_stmts.html#the-assert-statement) pour ces tests : si ce qui est à droite d'assert est juste, le programme continue sans encombre, si c'est faux, le programme plante.


On va donc créer dans notre projet situé dans le dossier *hello* un fichier nommé *test_projet.py* qui contiendra :

```python
def test_oui():
    assert 1 == 1


def test_non():
    assert 1 == 2

``` 
>**Remarque* : le premier test est vrai : `1 == 1` est `True` donc assert ne va rien faire. Le second va planter car `1== 2`va rendre `False` et assert va arrêter le programme.

Vous ne devriez pas avoir de rouge, le linter doit être content :

* une ligne vide à la fin
* deux lignes vides entre deux définitions de fonctions

Mettons en place nos tests. 

1. dans les préférences (*file/code > preferences > settings*) tapez `python.testing.pytestEnabled`  dans la barre de recherche et cochez la case. Ceci dit à vscode que notre framework de test est pytest (il y en a d'autres possible comme [unittest](https://docs.python.org/fr/3.9/library/unittest.html) ou encore [nosetests](https://nose.readthedocs.io/en/latest/), mais on ne va pas les utiliser. Assurez vous cependant qu'un seul framework de test soit utilisé à la fois. Ca devrait être le cas si vous n'avez pas cliqué un peu partout).
2. on configure les tests de notre projet en tapant la commande (ctrl/cmd+shift+p) : *python : Configure tests* on choisit *pytest* puis *. (root)* qui donne le dossier de départ où aller chercher nos tests
3. On lance nos tests avec soit :
   * la commande : *Python: Discover Tests* puis on clique sur *run tests* en bas à gauche de la fenêtre (à côté du nom de l'interpréteur), on choisit *Run all Tests*
   * il y a un petit erlenmeyer dans la colonne de gauche de la fenêtre, c'est les tests. On pet les exécuter tous en cliquant sur les 2 triangles verts dans le tab des tests. Vous pouvez voir le résultat complet en cliquant sur le petit terminal (5ème icône du tab des tests.)
   * dans un terminal en tapant `pytest` alors que vous êtes dans le dossier du projet.


Vous devriez voir :
* dans le tab des tests qu'un test est vert, l'autre rouge
* le test qui est rouge est marqué dans la sortie complète : 
    ```text
            def test_non():
        >       assert 1 == 2
        E       assert 1 == 2
    ```

Ceci est normal car le but d'assert est de vérifier que ce qui suit est juste. Si c'est le cas il ne se passe rien, si c'est faux le programme s'arrête.

Écrire un test revient à vérifier qu'un comportement d'une fonction est correct (l'`assert` est juste) et si le test plante (il est rouge) c'est que l'`assert` s'est révélé faux.

>**Attention** : si vous exécutez un fichier de test avec python (essayer en cliquant sur le petit triangle vert lorsque vous êtes sur un fichier de test) il ne va rien se passer. C'est normal car ce fichier n'a pas de commande python, juste des définitions de fonctions.

### test pour notre projet

On va juste faire un test qui vérifie que notre fonction rend bien une chaîne de caractère qui commence par `bonjour`. L'usage veut que l'on ait (au moins) un fichier de test par fichier de code, et que l'on nomme ses tests, le nom du fichier testé précédé de *test_*.

*test_le_code.py* :

```python
from le_code import bonjour

def test_bonjour():
    assert bonjour().startswith('Bonjour')
```

## TBD

* voir avec windows si tout va bien. En particulier avec l'invit de commande
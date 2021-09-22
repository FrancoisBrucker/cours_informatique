---
layout: page
title:  "outils de développement"
category: cours
tags: informatique cours 
author: "François Brucker"
---

En développement, on se concentre sur trois objectifs pour obtenir du bon code :

* on veut que notre code soit juste
* on veut pouvoir le modifier/ajouter des fonctionnalités rapidement
* on veut pouvoir partager notre code avec soit-même dans d'autres projet, son équipe ou le monde)

Le langage d'application n'a que peut d'intérêt en soit. On choisit celui qui est le plus adapté à notre but. Ici, on utilise le python mais il existe les outils qu'on va voir pour tout langage sérieux.

Écrire du code nécessite ne nombreuses automatisations et aides pour que ce ne soit pas pénible, ne vous privez pas d'outils parce que vous n'avez pas envie d'apprendre de nouvelles choses et que *ça suffit bien pour ce que je veux faire*. Vous allez au final perdre plus de temps que l'apprentissage initial (ce qui est tarte).

## prérequis

On suppose que vous avez suivis le [cours de développement]({% link cours/developpement/index.md %}) jusque là. Sinon, faite le, ou tout du moins ayez un vsc opérationnel pour le dévelopement python.

On suppose aussi que :

* vous connaissez le terminal de vsc et que vous savez y exécuter des programmes python.
* vous savez comment installer de nouveaux packages python.

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

[linting vsc et python]({% post_url tutos/editeur/vsc/2021-09-14-vsc-python %}#linter)

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
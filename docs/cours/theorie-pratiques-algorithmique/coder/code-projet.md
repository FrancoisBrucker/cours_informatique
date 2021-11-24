---
layout: page
title:  "mise en oeuvre d'un projet"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [coder]({% link cours/theorie-pratiques-algorithmique/coder/index.md %}) / [principes de développement]({% link cours/theorie-pratiques-algorithmique/coder/code-projet.md %})
>
> **prérequis :**
>
>* [python et vscode]({% post_url tutos/editeur/vsc/2021-09-14-vsc-python %})
>
{: .chemin}


> mettre en pratique les principes de développement dans un projet info.
> un projet pour le dev : toujours mieux que des fichiers épars
{: .tbd}

En développement, on se concentre sur trois objectifs pour obtenir du bon code :

* on veut que notre code soit juste
* on veut pouvoir le modifier/ajouter des fonctionnalités rapidement
* on veut pouvoir partager notre code avec soit-même dans d'autres projet, son équipe ou le monde)

Le langage d'application n'a que peut d'intérêt en soit. On choisit celui qui est le plus adapté à notre but. Ici, on utilise le python mais il existe les outils qu'on va voir pour tout langage sérieux.

Écrire du code nécessite ne nombreuses automatisations et aides pour que ce ne soit pas pénible, ne vous privez pas d'outils parce que vous n'avez pas envie d'apprendre de nouvelles choses et que *ça suffit bien pour ce que je veux faire*. Vous allez au final perdre plus de temps que l'apprentissage initial (ce qui est tarte).

## prérequis

On suppose que vous avez suivis le [cours de développement]({% link cours/developpement/index.md %}) jusque là. Sinon, faite le, ou tout du moins ayez un vsc opérationnel pour le développement python.

On suppose aussi que :

* vous connaissez le terminal de vsc et que vous savez y exécuter des programmes python.
* vous savez comment installer de nouveaux packages python.

## un projet test

On va juste créer un projet vide pour comprendre comment tout ça fonctionne.

Nous allons préparer le projet dans lequel nous allons coder. Ceci se fait avec vscode en ouvrant un dossier. Ce dossier sera le départ de votre projet et s'appelle *workspace*.

1. Commencez par créer le dossier *"hello-dev"*
2. dans vscode, choisissez : "*Menu File > open*" puis naviguez jusqu'à votre dossier *"hello-dev"*. On vous demande si vous faites confiances aux auteurs, puisque c'est vous dites oui.

> Lorsque l'on code et que l'on ne veut pas de problèmes en développement, les noms de fichiers doivent êtres sans espaces et sans accents.

### fichier python

On va créer notre premier fichier javascript : *menu Fichier > Nouveau Fichier* et sauvez le de suite : *menu Fichier > Enregistrer* avec le nom *"main.py"*.

Vscode à compris que c'était du python, il l'écrit dans la barre de statut (la dernière ligne, en bleu, de la fenêtre vscode, voir [user interface](https://code.visualstudio.com/docs/getstarted/userinterface)).

Vscode vous demande peut-être de :

   1. choisir un interpréteur : prenez le python3 de votre distribution
   2. choisir un lint : supprimer la fenêtre de warning, on fera ça plus tard.
   3. choisir des tests : supprimer la fenêtre de warning, on fera ça plus tard.

### exécution d'un fichier

On écrit *main.py* :

```python
print("bonjour les gens !")

```

Exécutez le deux manière que vous avez vu dans [le tutorial python et vscode]({% post_url tutos/editeur/vsc/2021-09-14-vsc-python %}#execution-python) :

* avec le terminal
* avec le triangle

## du joli code

Vous allez passer beaucoup de temps à lire du code, le votre et celui des autres. Il est important que ce soit facile :

* de lire du code
* de partager du code entre utilisateur.

Pour cela il faut que le style de code soit cohérent. Python donne des règle de style, c'est ce qu'on appelle la [PEP8](https://www.python.org/dev/peps/pep-0008/). Nous allons intaller des plugins qui vont :

* vous montrer les fautes de styles
* les corriger toutes seules

### linter

Suivez la partie [linter]({% post_url tutos/editeur/vsc/2021-09-14-vsc-python-modules-supplementaires %}#linter) du tuto des installations supplémentaires.

Puis testons le de suite. Modifiez le fichier *"main.py"* pour écrire :

```python
print ("bonjour les gens !")

```

Une fois le fichier sauvé vous devriez voir que print est souligné en rouge. En passant sa souris dessus on voit pourquoi : `whitespace before '(' pycodestyle(E211)`

>**Conclusion** : **NE JAMAIS METTRE D'ESPACE APRÈS UN NOM DE FONCTION** c'est mal car on ne sais pas si c'est une fonction ou un nom de variable.

Vous devriez peut-être aussi avoir la parenthèse de fin souligné en jaune. C'est parce que la dernière ligne de votre fichier n'est pas vide. Si ce n'est pas le cas, c'es que vous avez bien que 2 lignes dans votre fichier, la seconde étant vide.

### séparer code et main

>**bonne pratique** : un projet c'est trois chose d'égale importance :
>
> * le code : les fonctions utilisées
> * le main : le programme principal, c'est ce qu'on exécute lorsque veut faire marcher le projet
> * les tests : que l'on verra plus tard.
> Aucune n'est plus importante que l'autre et il est important qu'elles oisent bine distincte l'une de l'autre.
>

On va ainsi  créer deux fichiers, l'un nommé *"le_code.py"* qui contiendra notre code et l'autre nommé *"main.py"* qui sera notre programme principal

Fichier *le_code.py* :

```python
def bonjour():
    return "Bonjour les gens !"

```

Fichier *main.py* :

```python
from le_code import bonjour

print(bonjour())

```

On a importé le nom `bonjour` défini dans le fichier *"le_code.py"* grâce à un import. L'autre façon aurait été d'importer juste le fichier code. On aurait alors eu :

```python
import le_code

le_code.bonjour()

```

La notation pointée se lit alors : exécute le nom `bonjour` définit dans *"le_code"*.

>ne jamais jamais jamais utiliser `from le_code import *` qui importe tous les noms définis dans *"le_code.py"*. On ne sais pas vraiment ce qui a été importé en lisant *"le_code.py"*: notre code n'est pas lisible ! Le gain d'écriture de `*` plutôt que `bonjour` sera perdu au centuple plus tard lorsque l'on devra chercher dans tous les fichiers du projet où l'on a bien pu définir `bonjour`...
{: .attention}

En code comme dans la vie, il faut faire rapidement ce que l'on fait souvent. Comme on va passer plus de temps à lire/comprendre du code qu'à l'écrire, il faut optimiser la lecture et non l'écriture. D'où l'utilisation de nom explicites et on préférera toujours la lisibilité à la rapidité.

### black

> linter : pycodestyle
> 
{: .tbd}

Quand on utilise black, c'est facile d'écire du joli code : il le fait tout seul.

Suivez la partie [black]({% post_url tutos/editeur/vsc/2021-09-14-vsc-python-modules-supplementaires %}#black) du tuto des installations supplémentaires.

Testons black, en modifiant le fichier *"le_code.py"* :

```python
def        bonjour   (    )  :
    return    "Bonjour les gens !"

```

Dieu que ce code est laid. En sauvant et en exécutant black (le tuto vous deux deux manières de faires), on retrouve, sans rien faire du joli code :

```python
def bonjour():
    return "Bonjour les gens !"
```

> Black c'est tellemnt bien ! Utilisez le tout le temps pour rendre votre code joli !

## tests

Les tests permettent de vérifier que notre code fonctionne. Ils sont parti du programme et on peut s'y référer quand on veut. Lorsque l'on modifie le code, on pourra toujours exécuter tous les tests pour vérifier que notre programme fonctionne toujours aussi bien qu'avant.

Mettez en place les outils pour exécuter les tests en suivant la partie [tests]({% post_url tutos/editeur/vsc/2021-09-14-vsc-python-modules-supplementaires %}#tests).

### test des tests

On y reviendra plus tard et à de nombreuses reprise, les tests sont partie intégrante d'une bonne programmation.

On va juste ici vérifier que tout fonctionne. Il existe de nombreuse bibliothèques de tests possible pour python. Nous allons utiliser [pytest](https://docs.pytest.org/en/stable/) (vous l'installerez bienôt).

Le boulot d'une bibliothèque de test est d'exécuter toutes les fonctions commençant par `test_` de tous les fichiers commençant par `test_` d'un projet.

Les tests sont de petites fonction dont le but est de *tester* une fonctionnalité du programme( souvent l'exécution d'une fonction). On utilisera l'instruction [assert](https://docs.python.org/fr/3/reference/simple_stmts.html#the-assert-statement) pour ces tests : si ce qui est à droite d'assert est juste, le programme continue sans encombre, si c'est faux, le programme plante.

On va donc créer dans notre projet situé dans le dossier *hello* un fichier nommé *test_projet.py* qui contiendra :

```python
def test_oui():
    assert 1 == 1


def test_non():
    assert 1 == 2

```

**Remarque* : le premier test est vrai : `1 == 1` est `True` donc assert ne va rien faire. Le second va planter car `1== 2` va rendre `False` et assert va arrêter le programme.

Vous ne devriez pas avoir de rouge, le linter doit être content (au pire, faite un coup de black pour être sur) :

* une ligne vide à la fin
* deux lignes vides entre deux définitions de fonctions

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

>si vous exécutez un fichier de test avec python (essayer en cliquant sur le petit triangle vert lorsque vous êtes sur un fichier de test) il ne va rien se passer. C'est normal car ce fichier n'a pas de commande python, juste des définitions de fonctions.
{: .attention}

### test pour notre projet

On va juste faire un test qui vérifie que notre fonction rend bien une chaîne de caractère qui commence par `bonjour`. L'usage veut que l'on ait (au moins) un fichier de test par fichier de code, et que l'on nomme ses tests, le nom du fichier testé précédé de *test_*.

*test_le_code.py* :

```python
from le_code import bonjour

def test_bonjour():
    assert bonjour().startswith('Bonjour')
```

---
layout: layout/post.njk 
title: Coder ses objets

eleventyNavigation:
  key: "Coder ses objets"
  parent: "Programmation Objet"
---

{% prerequis "**Prérequis** :" %}

* [classes et objets](../classes-et-objets)
* [vscode et python sont installés]({{ '/tutoriels/vsc-python' | url }})

{% endprerequis %}

<!-- début résumé -->

Exemple complet d'utilisation complet de vscode pour créer des objets en python.

<!-- end résumé -->

Nous allons reprendre ici la première partie du cours [classes et objets](../classes-et-objets). 

## Création du projet

On suit les directives du [projet hello-dev](../../projet-hello-dev) pour créer un nouveau projet :

1. on crée un dossier `coder-objets`{.fichier} dans un explorateur de fichier
2. on ouvre le dossier `coder-objets`{.fichier} avec vscode, ce qui crée notre projet
3. on crée un nouveau fichier `main.py`{.fichier} où l'on écrit `print("hello world !")`

### Exécution du projet

1. assurez vous d'être dans l'onglet contenant le fichier `main.py`{.fichier} de vscode
2. cliquez sur le triangle en haut à droite de la fenêtre pour exécuter le programme.

Vous devriez obtenir quelque chose du genre :

![exécution python](./exécution-python.png)

{% info %}
Pour connaître le python utilisé, il suffit de cliquer en bas à droite de la fenêtre de vscode. On voit tout les pythons connus :

![quel python ?](./quel-python.png)

Celui utilisé est précédé d'une étoile.
{% endinfo %}

Pour exécuter du python, vscode écrit une *ligne de commande* dans le terminal. Dans l'exemple précédent, la ligne de code était :

```shell
/usr/local/bin/python3 /Users/fbrucker/Documents/sous_git/cours_informatique/docs/src/cours/algorithme-code-théorie/code/programmation-objet/coder-ses-objets/coder-objets/main.py
```

{% info %}
Ce qui est avant la ligne de code, c'est à dire `fbrucker@macminibrucker coder-ses-objets/coder-objets ±main⚡ »` dans l'exemple précédent est appelé le *prompt* et est ce que le terminal met au début de chaque ligne avant que l'on puisse taper des commandes.
{% endinfo %}

La ligne de commande d'un terminal est toujours composée de la même façon :

```shell
nom-du-programme paramètre-1-du-programme ... paramètre-n-du-programme 
```

Dans notre cas:

* nom du programme : `/usr/local/bin/python3` Qui est le chemin vers l'exécutable python
* un unique paramètre : `/Users/fbrucker/Documents/sous_git/cours_informatique/docs/src/cours/algorithme-code-théorie/code/programmation-objet/coder-ses-objets/coder-objets/main.py` qui est le chemin vers le fichier à exécuter

### Installer des packages pour notre python <did id="pip"></div>

Pour installer des modules pour notre python, il faut taper la commande :

```shell
nom-du-programme-python -m pip install nom-du-module-à-installer
```

Où :

* `nom-du-programme-python` est le python pour lequel on veut installer un package, c'est à dire la première partie de la ligne de commande écrite par vscode. Chez moi (sous mac avec brew), c'est : `/usr/local/bin/python3`
* `nom-de-la-bibliothèque-à-installer` est le nom de la bibliothèque à installer.

Cette ligne se comprend ainsi : pour mon python (`nom-du-programme-python`), je veux utiliser le module `pip` (`-m pip`) avec les paramètres `install nom-du-module-à-installer` (on veux installer un module)

Si je veux installer la bibliothèque `pytest` par exemple, ma ligne de commande (sous mac) à taper dans le terminal vscode sera :

```shell
/usr/local/bin/python3 -m pip install pytest
```

Pour vous, ce sera différent car le `nom-du-programme-python` sera différent.

## Coder ses objets : le compteur

Nous allons reprendre l'exemple du cours [classes et objets](../classes-et-objets), avec le compteur. On sait que l'on veut arriver à la modélisation UML suivante :

![uml compteur](../classes-et-objets/classes-2.png)

On va coder petit à petit la classe.

### Préparation du projet

Notre projet est pour l'instant organisé de cette manière :

```text
coder-objets
└── main.py
```

Nous allons avoir besoin d'un objet `Compteur` donc :

1. on crée un fichier un fichier `compteur.py`{.fichier} dans notre projet
2. on crée la classe `Compteur`{.language} la plus petite possible
3. on importe et on crée un objet de classe `Compteur`{.language} dans le programme principal

#### classe `Compteur`{.language} minimale

Fichier : `compteur.py`{.fichier} :

```python

class Compteur:
    pass

```

{% note "**Conventions :**" %}

* les **noms** de classe commencent par une **majuscule**
* l'implémentation de la classe est placée dans un **fichier** de même nom mais avec une **minuscule**

{% endnote %}

On a utilisé l'instruction [`pass`{.language-}](https://www.docstring.fr/glossaire/pass/) qui ne fait rien. Nous l’utilisons ici car la définition d'une classe crée un bloc (il y a un `:`) et que tout bloc **doit** contenir une instruction.

#### création d'un objet dans le programme principal

Fichier : `main.py`{.fichier}

```python
from compteur import Compteur

c = Compteur()

```

Lorsque l'on exécute le programme `main.py` il ne se passe rien. C'est une bonne nouvelle ! Ca signifie que notre programme n'a pas d'erreur et qu'un objet a bien été créé.

#### Convertir notre essai en test

Lorsque l'on programme, on fait constamment des tests pour vérifier que le programme fonctionne. Lorsque notre programme grossi, on a tendance à ne tester **que** les nouvelles fonctionnalités et non pas de **vérifier** que les anciennes fonctionnent toujours.

De plus, on a souvent oublié commet on avait fait pour tester nos anciennes fonctionnalités. C'est bête ! Autant garder nos tests pour pouvoir les exécuter à chaque modification de code.

Enfin, un programme informatique (en vrai, pas en TD où il ne dure que 2h) n'est **jamais** fini. On va travailler à ce programme pendant des semaines, voir des mois et pour certains des années. On ne peux donc pas :

1. décider au départ tout ce qu'on va coder puis stopper le développement.
2. coder chaque classe indépendamment des autres. Le code d'une classe va influer sur le code d'une autre

Les deux points ci-dessus impliquent que :

1. il faut retester les classes déjà écrites lorsque l'on en code de nouvelles à cause des effets de bords possibles
2. il faut parfois modifier des classes que l'on a écrite précédemment et donc il faut retester toutes leurs fonctionnalités.

{% note %}

* tester ses classes est une nécessité
* il faut conserver ses tests pour ne pas avoir à les re-écrire à chaque fois

{% endnote %}

Pour arriver à ce résultat, nous allons utiliser la boucle de programmation suivante :

1. on code une petite fonctionnalité
2. on vérifie dans le programme principale ou dans un programme principal de test que cette fonctionnalité fonctionne
3. on convertit cette vérification en test que l'on conserve

Pour l'instant, on crée un objet et on en fait rien. Vérifions qu'il est bien de la bonne classe, `Compteur`{.language-} :

Fichier : `main.py`{.fichier}

```python
from compteur import Compteur

c = Compteur()
print(type(c))
```

En exécutant le fichier main, on obtient :

```
» python main.py
<class 'compteur.Compteur'>
```

C'est de la classe `Compteur`{.language}. Améliorons notre vérification :

Fichier : `main.py`{.fichier}

```python
from compteur import Compteur

c = Compteur()
print(type(c) == Compteur)
```

En exécutant le fichier main dans le terminal, j'obtiens :

```
» /usr/local/bin/python3 main.py
True
```

Notre vérification est juste :

* notre vérification rend `True` si l'objet crée est de la classe compteur
* notre vérification rend `False` sinon

{% attention %}
Ne confondez pas `Compteur`{.language}, **la classe** et `Compteur()`{.language} qui est le **résultat** de l'exécution de la classe, c'est à dire un objet.
{% endattention %}

Maintenant que notre vérification est transformée en quelque chose qui doit `True` ou `False`, on peut la transformer en un test. Pour cela on crée un fichier `test_compteur.py` qui retranscrit notre vérification:

Fichier : `test_compteur.py`{.fichier}

```python
from compteur import Compteur


def test_constructeur():
    c = Compteur()
    assert type(c) == Compteur

```

{% info %}
Un fichier de test commence **toujours** par `test_`. Un fichier un uniquement nommé `test.py` n'est **pas** un fichier de test aux yex de python.
{% endinfo %}

Pour exécuter ce fichier sous la forme de test, on ne **peut pas** juste l'exécuter. En effet, on ne fait **que** définir des fonctions de tests, aucune n'est exécutée (faite le test en exécutant directement ce fichier de test et en créant un test objectivement faux par exemple `assert 1 == 2`). Il faut donc passer ce fichier à un programme qui exécute les tests : [pytest](https://docs.pytest.org/)

Il y a 2 moyens d’exécuter les tests :

1. en utilisant l'erlenmeyer à gauche de la fenêtre de vscode
2. dans le terminal, dans le dossier du projet, en tapant la commande : ````nom-du-programme-python -m pytest` où `nom-du-programme-python` est le nom du python utilisé par vscode (voir [partie utilisation de pip](./#pip))

{% info %}
Dans le terminal, la flèche du haut de votre clavier rappelle les commandes précédentes, vous n'avez donc pas besoin de retaper toute la commande de test à chaque fois.
{% endinfo %}

En exécutant le test avec le terminal, j'obtiens :

```
» /usr/local/bin/python3 -m pytest               
========================================================== test session starts ===========================================================
platform darwin -- Python 3.9.13, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /Users/fbrucker/Documents/sous_git/cours_informatique/docs/src/cours/algorithme-code-théorie/code/programmation-objet/coder-ses-objets/coder-objets
plugins: dash-1.19.0, cov-3.0.0
collected 1 item                                                                                                                         

test_compteur.py .                                        
```

A la fin de cette partie, notre projet ressemble à :

```text
coder-objets
├── compteur.py
├── main.py
└── test_compteur.py
```

### coder l'attribut `valeur`{.language-}

Maintenant qu'on est assuré que l'on peut créer des objets, on peut améliorer les fonctionnalités de notre compteur (c'est facile, pour l'instant il ne fait rien). On décide de commencer par ajouter l'attribut `valeur`{.language-} et son accesseur `donne_valeur()`{.language-}

On utilise la boucle de programmation vue précédemment :

1. on code une petite fonctionnalité
2. on vérifie dans le programme principale ou dans un programme principal de test que cette fonctionnalité fonctionne
3. on convertit cette vérification en test que l'on conserve

Donc dans notre cas :

#### code l'attribut

Fichier `compteur.py`{.fichier} :

```python
class Compteur:
    def __init__(self):
        self.valeur = 0

    def donne_valeur(self):
        return self.valeur
```

#### vérification du fonctionnement de l'attribut

Fichier `main.py`{.fichier} :

```python
from compteur import Compteur

c = Compteur()
print(c.donne_valeur())
```

puis, une fois que tout marche :

```python
from compteur import Compteur

c = Compteur()
print(c.donne_valeur() == 0)
```

#### test de la fonctionnalité

On **ajoute** le test à notre fichier de test, pour avoir :

Fichier `test_compteur.py`{.fichier} :

```python
from compteur import Compteur


def test_constructeur():
    c = Compteur()
    assert type(c) == Compteur


def test_valeur_initiale():
    c = Compteur()
    assert c.donne_valeur() == 0

```

{% attention %}
On ne supprime pas d'anciens tests, sinon on perd tout les bénéfices de programmer des tests.
{% endattention %}

L'exécution des tests via le terminal donne alors :

```
» /usr/local/bin/python3 -m pytest
========================================================== test session starts ===========================================================
platform darwin -- Python 3.9.13, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /Users/fbrucker/Documents/sous_git/cours_informatique/docs/src/cours/algorithme-code-théorie/code/programmation-objet/coder-ses-objets/coder-objets
plugins: dash-1.19.0, cov-3.0.0
collected 2 items                                                                                                                        

test_compteur.py ..                                                                                                                [100%]

=========================================================== 2 passed in 0.02s ============================================================
```

Les deux tests sont passés.

### coder incrémente

On procède de la même manière pour incrémente.

#### code de la méthode `incrémente`{.language-}

Fichier `compteur.py`{.fichier} :

```python
class Compteur:
    def __init__(self):
        self.valeur = 0

    def donne_valeur(self):
        return self.valeur

    def incrémente(self):
        self.valeur += 1

```

#### vérification du fonctionnement de la méthode

Fichier `compteur.py`{.fichier} :

```python
from compteur import Compteur

c = Compteur()

c.incrémente()
print(c.donne_valeur())
c.incrémente()
print(c.donne_valeur())

```

On a mis deux appels à la méthode incrémente, car si on ne garde qu'une unique vérification, on est pas assuré que la valeur incrémente (`self.valeur = 1` plutôt que `self.valeur += 1` dans le code de la méthode par exemple).

#### ajout des tests

Fichier `test_compteur.py`{.fichier} :

```python
from compteur import Compteur


def test_constructeur():
    c = Compteur()
    assert type(c) == Compteur


def test_valeur_initiale():
    c = Compteur()
    assert c.donne_valeur() == 0


def test_incrémente():
    c = Compteur()

    c.incrémente()
    assert c.donne_valeur() == 1

    c.incrémente()
    assert c.donne_valeur() == 2

```

Chaque test doit être indépendant, on recrée donc notre objet **à chaque** test.

## Améliorer ses objets : le compteur avec paramètres

Entraînez vous à créer des tests en ajoutant les paramètres par défaut. Cela vous entraînera à modifier des méthodes puis à mettre en concordance les tests.

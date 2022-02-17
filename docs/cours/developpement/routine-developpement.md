---
layout: page
title:  "Routine de developpement"
category: cours
tags: informatique cours 
author: "François Brucker"
---


On va créer ici un projet complet visant à compter le pourcentage de `0` dans un nombre écrit en binaire.

Le but de ce cours est de dérouler la création et la mise en œuvre d'un projet, petit à petit.

## mise en place

### ouverture du dossier

On crée un projet avec vscode, c'est à dire que l'on ouvre un nouveau dossier que l'on nomme `"pourcentage_binaire"`.

### créations des fichiers

On crée tout de suite nos 3 fichiers (que l'on garde vide pour l'instant) :

* *"test_pourcentage.py"* : notre fichier de test
* *"pourcentage.py"* : le code
* *"main.py"* : le programme principal

## le projet

### le code

On veut compter le nombre de `0` d'un nombre écrit en binaire.

Fichier *"pourcentage.py"* :

```python
def pourcent(chaîne_de_caractères):
    nombre_de_0 = chaîne_de_caractères.count('0')

    return nombre_de_0 / len(chaîne_de_caractères)

```

Remarquez que l'on ne vérifie pas dans la fonction :

* que notre entrée est une chaîne de caractères
* que la chaîne est uniquement composée de 0 et de 1

Notre nom de paramètre est explicite, donc s'il y a une erreur c'est de la faute du développeur. Le programme va planter si on met un entier dans `chaîne_de_caractères`, puisque les entiers ne connaissent pas la méthode [`count`](https://docs.python.org/3/library/stdtypes.html?highlight=count#str.count) : si les entrées sont spécifiées dans la documentation ou par des nom explicite, ce n'est pas la peine de vérifier dans le code que c'est ok.

>* **Coding mantra** : il vaut mieux qu'un programme plante plutôt qu'il cache l'erreur (en mettant par exemple 0 si le nom `chaîne_de_caractères` n'a pas de méthode `count`).
>* **pourquoi ?** L'erreur ne va pas partir, elle va juste faire planter le programme autre-part, loin de la réelle erreur. Ce sera donc bien plus dur à trouver.

### les tests

Ajoutons des tests. Par exemple, on pourrait tester que :

* `"1"` rende `0`
* `"0"` rende `1`.

Fichier *"test_pourcentage.py"* :

```python
from pourcentage import pourcent


def test_pourcent_0():
    assert pourcent('11') == 0


def test_pourcent_1():
    assert pourcent('00') == 1

```

Pour finir, on pourrait ajouter un test un peut plus compliqué : que `"01"` rende `.5`.

>On va tester des réels, pas des entiers. Rappelez vous que les réels ne le sont pas. Seuls les entiers existent. Voir [la doc](https://docs.python.org/fr/3/tutorial/floatingpoint.html))
{: .attention}

On ne peut pas écrire directement `assert pourcent('01') == .5` (même si là, ça risque de marcher) car si ça se trouve on aura `.499999999` à la place de `.5`. Lorsque l'on compare des réels c'est toujours à epsilon prêt.

Donc on va utiliser une fonction spéciale de `pytest`, qui vérifie si 2 réels sont *à peu prêt égaux* (par défaut à dix moins six prêt) : [approx](https://docs.pytest.org/en/latest/reference.html#pytest-approx) pour ça.

Fichier  *"test_pourcentage.py"* :

```python
from pytest import approx

from pourcentage import pourcent


def test_pourcent_0():
    assert pourcent('11') == 0


def test_pourcent_1():
    assert pourcent('00') == 1


def test_pourcent_01():
    assert pourcent('01') == approx(.5)

```

>* **Coding mantra** : que tester ?
>* **réponse** : ce qui est nécessaire pour que **vous** (*ie.* le développeur) soyez convaincu que votre fonction marche. Ni plus, ni moins.
>
>* **Coding mantra** : pourquoi tester ?
>* **réponse** : pour être sûr que le programme fonctionne. Pour permettre d'ajouter rapidement des fonctionnalités sans avoir à **tout** re-tester (les tests sont déjà écrit). Parce que **tout le monde** fait des erreurs. Oui oui, même toi qui te croit fort.

C'est **TOUJOURS** au développeur de la fonction de faire ses tests. Parce qu'il faut que les testent accompagnent le code, pour que l'on soit sur du fonctionnement et puisse coder la suite tranquillement. Si l'on fait les tests à la fin de la journée :

* c'est embêtant
* si ça se trouve on devra refaire plein de choses car un bug en aura entraîné un autre et tout un tas de fonctions seront à corriger. En faisant les tests dès que la méthode est écrite, on gagne du temps
* si c'est quelqu'un d'autre qui les fait, comment être sur que ce soit les bons tests ? Qu'ils couvrent bien tout le fonctionnement du code ? Il faut que l'autre personne comprenne également le code. On perd donc du temps puisqu'il faut faire 2 fois le boulot de compréhension.

>* **Coding mantra** : Pour ma part, je fais du [TDD](https://fr.wikipedia.org/wiki/Test_driven_development). J'écris mes tests **avant** de coder. Celà peut sembler contre intuitif mais c'est super bien car cela permet d'utiliser son code avant de l'écrire. Souvent, en cherchant comment écrire un test, on trouve la bonne façon d'utiliser la fonction que l'on va écrire. Coder la fonction puis l'utiliser dans les tests est alors une perte de temps puisque parfois il faut complètement la réécrire car elle n'est pas pratique à utiliser.

Ce n'est pas le cas ici, mais dans la vraie vie, on ne sais pas trop à quoi va ressemble notre fonction une fois écrite. Le TDD permet d'écrire la fonction petit à petit. Une fois que vous aurez vu la programmation objet tenter [ce tuto](https://francoisbrucker.github.io/cours_informatique/cours/mie/developpement-objet/tdd_et_test_pattern.html).

### programme principal

Fichier "main.py"* :

```python
from pourcentage import pourcent

chaîne = input('Donnez un nombre écrit en binaire :')

print("Votre nombre contient ", pourcent(chaîne), "pourcent de 0.")
```

On ne vérifie pas que :

* c'est bien un nombre binaire : que donne le code si on ne mets pas un nombre binaire ?
* il a une longueur non vide : que fait le programme si on appuie sur la touche entrée sans rien écrire ?

#### correction d'un bug

Si l'on ne rend rien, le programme plante ! On va corriger notre code et rajouter un test pour être sur que ça n'arrive plus :

dans *"test_pourcentage.py"*, ajoutez le test :

```python
# ...

def test_pourcent_vide():
    assert pourcent('') == 0

# ...
```

> On a coutume de mettre des `# ...` pour dire que le reste du code du fichier n’est pas changé. Ce n’est pas la peine de les copier/coller.

Puis on corrige la fonction `pourcent` de *"pourcentage.py"* :

```python
# ...

def pourcent(chaîne_de_caractères):
    nombre_de_0 = chaîne_de_caractères.count('0')

    if len(chaîne_de_caractères):
        return nombre_de_0 / len(chaîne_de_caractères)
    else:
        return 0

# ...
```

#### prise en compte de l'utilisateur

Quand je vous avait dit de ne pas faire de vérification, c'est vrai pour tout ce qui a trait au code utilisé par l'ordinateur. Dès qu'un humain utilise du code, il faut **TOUT** vérifier et faire en sorte qu'il ait la meilleur expérience possible.

Donc ici on pourrait :

* faire rentrer à l'utilisateur un nombre en base 10,
* lui montrer son nombre en base 2 puis donner son pourcentage
* il faut ne pas planter et redemander à l'utilisateur de taper un nombre si ce n'est pas un nombre en base 10

On utilise la [gestion des erreurs de python](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) pour ça (Cela dépasse un peu le cadre de ce cours, on ira donc pas plus loin que vous montrer que ça existe)

>**Amélioration possible** : ne s'arrêter que si l'utilisateur tape une chaîne de caractère vide.

Fichier *"main.py"* :

```python
from pourcentage import pourcent

correct = False
entier = 0

while not correct:
    correct = True
    chaine = input('Donnez un nombre écrit en base 10 :')
    try:
        entier = int(chaine)
    except ValueError:
        correct = False
        print("ce n'est pas un nombre. Essayez encore une fois.")

nombre_binaire = bin(entier)[2:]

print("Votre nombre",
      chaine, "contient ", pourcent(nombre_binaire),
      "pourent de 0 en base 2 (" + nombre_binaire + ").")
```

### couverture de code

Pour savoir si nos tests couvrent bien l'ensemble du projet, c'est à dire si les tests passent bien par chaque ligne de code, on utilise des outils de [couverture de code](https://fr.wikipedia.org/wiki/Couverture_de_code).

>**Attention** : Avoir 100% de couverture de code ne signifie pas que votre projet est bien testé...Juste que les tests ont utilisé toutes les lignes de codes :
>
>* ça ne prouve pas que les fonctionnalités de votre code sont correctes
>* certaines fonctions n'ont pas besoin d'être testées (comme les constantes ou les affichages à l'écran par exemple)

Suivez le [tutoriel d'installation]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-python-modules-supplementaires.md %}#code-coverage) pour mettre en place les outils de coverage.

En tapant `pytest --cov=.` dans [un terminal](https://code.visualstudio.com/docs/editor/integrated-terminal), j'obtient le résultat suivant ;

```text
fbrucker@emma projets/pourcentage_binaire » pytest --cov=.
=== test session starts ===
platform darwin -- Python 3.9.1, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: /Users/fbrucker/projets/pourcentage_binaire
plugins: cov-2.11.1
collected 4 items

test_pourcentage.py .... [100%]


---------- coverage: platform darwin, python 3.9.1-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
main.py                  13     13     0%
pourcentage.py            5      0   100%
test_pourcentage.py      10      0   100%
-----------------------------------------
TOTAL                    28     13    54%


=== 4 passed in 0.19s ===
```

On a regardé la couverture de code des fichiers du dossier `.` (c'est à dire le dossier courant) qui ont été lu lors de l'éxecution de pytest (qui regarde tous les fichiers qui commencent par `"test_"` et exécutent toutes les fonctions qui commencent par `"test_"` dans ceux-ci).

On se rend compte que `"main.py"` n'a pas été lu (0% de ses lignes ont été parcourues), et que 100% des lignes de `"pourcentages"` ont été lues.

Rajoutons une fonction dans `"pourcentage.py"` qui ne sera pas lue dans les tests et voyons la différence

Fichier *"pourcentage.py"* :

```python
# ...

def non_lue():
    pass

#...
```

J'obtiens maintenant ça :

```text
fbrucker@emma projets/pourcentage_binaire » pytest --cov=.
=== test session starts ===
platform darwin -- Python 3.9.1, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: /Users/fbrucker/projets/pourcentage_binaire
plugins: cov-2.11.1
collected 4 items                                        

test_pourcentage.py .... [100%]

---------- coverage: platform darwin, python 3.9.1-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
main.py                  13     13     0%
pourcentage.py            7      1    86%
test_pourcentage.py      10      0   100%
-----------------------------------------
TOTAL                    30     14    53%


=== 4 passed in 0.19s ===
```

1 ligne de `"pourcentage.py"`  n'est pas lue. C'est le corps de la fonction `non_lue`, c'est à dire `pass`.

> Un rapport détaillé de la couverture est par défaut écrit and le fichier `.coverage` (vérifiez, il y en a bien un dans votre dossier).

Finissons cette partie en utilisant le coverage avec l'extension vscode : `pytest --cov=. --cov-report xml:cov.xml`

Regardez le fichier `"pourcentage.py"` : il doit avoir de lignes vertes et rouge.
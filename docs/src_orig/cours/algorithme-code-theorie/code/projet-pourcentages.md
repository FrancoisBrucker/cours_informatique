---
layout: page
title:  "projet / pourcentage binaire"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [code]({% link cours/algorithme-code-theorie/code/index.md %}) / [projet : pourcentages]({% link cours/algorithme-code-theorie/code/projet-pourcentages.md %})
>
> **prérequis :**
>
>* [coder/mise en oeuvre d'un projet]({% link cours/algorithme-code-theorie/code/projet-hello-dev.md %})
>* [naviguer dans un système de fichiers]({% link _tutoriels/systeme/fichiers-navigation.md %})
{.chemin}

Vous allez créer un projet visant à compter le pourcentage de `0` dans un nombre écrit en binaire.

Le but de ce cours est de dérouler la création et la mise en œuvre d'un projet, petit à petit.

## mise en place

### où est python

> Dans un terminal :
>
> * affichez le path
> * déterminez quel est chemin absolu du python utilisé par défaut dans le terminal
>
{.a-faire}

Une fois que le chemin du python du terminal est connu :

> * déterminez l'exécutable python utilisé par défaut par vscode
> * faites en sorte que le python de vscode et celui du terminal coïncident, en changeant celui de vscode si nécessaire.
{.a-faire}

### dossier du projet

> 1. Créez ci ce n'est pas déjà fait avec l'explorateur de fichier un dossier où vous placerez tous les projets de ce cours.
> 2. ouvrez un terminal dans ce dossier
> 3. créer **avec le terminal** un dossier intitulé *"pourcentage_binaire"* dans le dossier courant du terminal
{.a-faire}

### projet vscode

> Créer un nouveau projet vscode en ouvrant le dossier *"pourcentage_binaire"*.
{.a-faire}

### créations des fichiers

> Créez avec vscode 3 fichiers (que l'on garde vides pour l'instant) dans le projet :
>
> * *"main.py"* : le programme principal
> * *"pourcentage.py"* : le code
> * *"test_pourcentage.py"* : notre fichier de tests
>
{.a-faire}

> On a coutume d'associer à chaque fichier de code son fichier de tests dont le nom est le même que le fichier de code précédé de `test_`

## le projet

Le projet final consistera à demander à l'utilisateur un nombre décimal et de répondre le pourcentage de 0 dans ce nombre lorsqu'on l'écrit en binaire.

Pour arriver à ce but, on va procéder petit à petit. On s'assurera du bon fonctionnement du code en ajoutant des tests (qu'on conservera !) à chaque étape.

### le code

On veut compter le nombre de `0` d'un nombre écrit en binaire. Un entier n'ayant pas de base définie (c'est le même entier quelque soit la base), si l'on veut compter le nombre de $0$ de sa représentation binaire, il faut transformer notre entier en une chaine de caractères constituées de `"0"` et de `"1"` et compter le nombre de caractères `"0"`.

Mais avant de penser à la conversion d'un entier, essayons de voir comment compter le nombre de `"0"` d'une chaine de caractères.

> Dans le fichier *"pourcentage.py"* créez une fonction `pourcent` dont l'entrée nommée `chaîne_de_caractères` est une chaine de caractères composée de de "0" et de "1" et qui rend le pourcentage de "0" dans cette chaîne.
>
> Assurez vous que le [linter]({% link cours/algorithme-code-theorie/code/projet-hello-dev.md %}#linter) soit content. Il ne doit y avoir aucune faute de style.
{.a-faire}

Vous ne vérifierez pas :

* que l'entrée est une chaîne de caractères
* que la chaîne est uniquement composée de `"0"` et de `"1"`

En effet, le nom du paramètre est explicite, donc s'il y a une erreur c'est de la faute du développeur. Le programme va planter si on met un entier dans `chaîne_de_caractères`, puisque les entiers ne peuvent être mis dans une boucle for.

> Si les entrées de nos méthodes sont spécifiées dans le code ou la documentation ou par des noms explicites, ce n'est pas la peine de vérifier dans le code que c'est ok.
{.note}

On aurait pu aussi rendre 0 si l'entrée n'était pas une chaine de caractère. Ceci aurait masqué le mauvais type d'entrée dans la fonction tout en donnant un résultat cohérent. **CE N'EST PAS UNE BONNE IDEE !**

>* **Coding mantra** : il vaut mieux qu'un programme plante plutôt qu'il cache une erreur.
>* **pourquoi ?** L'erreur ne va pas partir d'elle même, elle va juste faire planter le programme autre-part, loin de la réelle erreur. Elle sera donc bien plus dur à trouver et à corriger.
{.note}

### les tests

Pour nous assurer que la fonction `pourcent` fonctionne, vous avez du faire des tests. Il faut les conserver car un code c'est la fonction **et** ses tests.

Par exemple, on pourrait tester que :

* `"11"` rende bien `0`
* `"00"` rende bien `1`.

> Mettez le code suivant dans *"test_pourcentage.py"* :
{.a-faire}

```python
from pourcentage import pourcent


def test_pourcent_0():
    assert pourcent('11') == 0


def test_pourcent_1():
    assert pourcent('00') == 100

```

> Testez ensuite que vos tests fonctionnent :
>
> * avec l'erlenmeyer de vscode
> * dans un terminal dont le dossier courant est le dossier du projet en tapant `python -m pytest`
>
{.a-faire}

On a testé les cas limites de notre fonction. Ajoutons un cas général, où il y a à la fois des `"0"` et des `"1"`, par exemple que  `"101"` rende `100 * (1/3)`.

Ceci nous impose de tester l'égalité entre 2 réels. Ceci est impossible à faire en informatique car il faudrait regarder une infinité de chiffres après la virgule... Or les réels en informatique sont en fait des entiers déguisés, ce sont des approximations (voir [la doc](https://docs.python.org/fr/3/tutorial/floatingpoint.html))).

> Les réels sont des limites, ils n'ont pas d'existence tangible. En bref : les réels ne le sont pas, seuls les entiers le sont.

On ne peut donc pas écrire directement `assert pourcent('101') == 100 * (1/3)` (même si là, ça risque de marcher) car si ça se trouve on aura `33.333333336` à la place de `100/3`.

> On ne teste **JAMAIS** l'égalité entre 2 réels. On les compare toujours à $\epsilon$ près.
{.note}

Pour cela, on va utiliser une fonction spéciale de `pytest`, qui vérifie si 2 réels sont *à peu près égaux* (par défaut à dix moins six près) : [approx](https://docs.pytest.org/en/latest/reference.html#pytest-approx).

Comme nos deux autres tests comparaient déjà des réels, on va les modifier pour qu'ils utilisent approx avant d'ajouter le nouveau test

> Mettez le code suivant dans *"test_pourcentage.py"*, et vérifiez que les tests passent toujours :
{.a-faire}

```python
from pytest import approx

from pourcentage import pourcent


def test_pourcent_0():
    assert pourcent('11') == approx(0)


def test_pourcent_1():
    assert pourcent('00') == approx(100)

```

> **style** : L'ordre des `import` est, [par coutume](https://google.github.io/styleguide/pyguide.html#s3.13-imports-formatting), le suivant :
>
> 1. les modules de python
> 2. les modules externes
> 3. les imports de notre projet
>
> On saute une ligne entre chaque groupe d'import pour bien voir les différences.
{.note}

On peut maintenant ajouter le nouveau test :

> Ajoutez à *"test_pourcentage.py"* le test suivant, puis testez que les 3 tests passent.
{.a-faire}

```python
# ...

def test_pourcent_01():
    assert pourcent('101') == approx(100/3)

# ...
```

> On a coutume de mettre des `# ...` pour dire que le reste du code du fichier n’est pas changé. Ce n’est pas la peine de les copier/coller.

On a 3 tests. Deux de ces tests correspondent aux cas limites, et le troisième à un cas général.

>* **Coding mantra** : que tester ?
>* **réponse** : ce qui est nécessaire pour que **vous** (*ie.* le développeur) soyez convaincu que votre fonction marche. Ni plus, ni moins.
>
>* **Coding mantra** : pourquoi tester ?
>* **réponse** : pour être sûr que le programme fonctionne. Pour permettre d'ajouter rapidement des fonctionnalités sans avoir à **tout** re-tester (les tests sont déjà écrits). Parce que **tout le monde** fait des erreurs. Oui oui, même toi qui te crois fort.
{.note}

C'est **TOUJOURS** au développeur de la fonction de faire ses tests. Parce qu'il faut que les testent accompagnent le code, pour que l'on soit sûr du fonctionnement et puisse coder la suite tranquillement. Si l'on fait les tests à la fin de la journée :

* c'est embêtant
* si ça se trouve on devra refaire plein de choses car un bug en aura entraîné un autre et tout un tas de fonctions seront à corriger. En faisant les tests dès que la méthode est écrite, on gagne du temps
* si c'est quelqu'un d'autre qui les fait, comment être sûr que ce soit les bons tests ? Qu'ils couvrent bien tout le fonctionnement du code ? Il faut que l'autre personne comprenne également le code. On perd donc du temps puisqu'il faut faire 2 fois le boulot de compréhension.

### programme principal

Faisons notre première tentative de programme principal. On va demander directement à l'utilisateur de rentrer un nombre écrit en binaire.

#### un premier jet

> Dans  le fichier *"main.py"*, créez un programme principal qui demande à l'utilisateur d'écrire un nombre en binaire, puis qui rende le pourcentage de "0" de ce nombre. Faite le programme le plus simple possible.
>
> Pour interagir avec l'utilisateur, vous utiliserez la fonction [input](https://docs.python.org/fr/3/library/functions.html#input) de python pour cela. Répondez aux questions :
>
> * de quel type est le résultat de la fonction `input` ?
> * pourquoi ?
>
{.a-faire}
{% details input %}

Le retour de la fonction input est une chaine de caractères. C'est normal car l'utilisateur a tapé des caractères sur son clavier. Toute interaction avec l'utilisateur est par défaut considéré comme une chaine de caractères. C'est au programme de faire la conversion si nécessaire.

{% enddetails %}

A priori,comme le code est simple on ne vérifie pas que :

* c'est bien un nombre binaire : que donne le code si on ne met pas un nombre binaire ?
* il a une longueur non vide : que fait le programme si on appuie sur la touche entrée sans rien écrire ?

#### vérification des entrées utilisateurs

Quand je vous avais dit de ne pas faire de vérification, c'est vrai pour tout ce qui a trait au code utilisé par l'ordinateur. Dès qu'un humain utilise du code, il faut **TOUT** vérifier et faire en sorte qu'il ait la meilleure expérience possible.

> Tout ce que fait l'utilisateur doit être vérifié avant d'être injecté dans le programme. C'est la [loi de Murphy](https://fr.wikipedia.org/wiki/Loi_de_Murphy) : si on laisse la possibilité de se tromper, quelqu'un va forcément le faire à un moment.
{.note}

Donc ici on pourrait :

* faire rentrer à l'utilisateur un nombre en base 10,
* il faut ne pas planter et redemander à l'utilisateur de taper un nombre si ce n'est pas un nombre en base 10
* lui montrer son nombre en base 2 puis donner son pourcentage

On utilise la [gestion des erreurs de python](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) pour ça (Cela dépasse un peu le cadre de ce cours, on ira donc pas plus loin que vous montrer que ça existe)

> Mettez le code suivant dans *"main.py"* :
{.a-faire}

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
      "pourcent de 0 en base 2 (" + nombre_binaire + ").")
```

> Exécutez le code et comprenez comment il fonctionne. En particulier :
>
> * comment fonctionne la boucle `while` ?
> * notre nombre a été converti en plein de types différents. Lesquels ?
> * comment est géré l'erreur possible ?
> * ..
>
> Faites de petits bout de code qui isolent ces différents points et exécutez les pour comprendre comment cela fonctionne.
{.a-faire}

Il faut toujours faire l'effort de comprendre le code que vous copiez/collez. Ce n'est que comme ça que vous progresserez. Pour cela, isolez la partie de code que vous voulez comprendre en refaisant un programme qui n'utilise que ça.

> **La magie n'existe pas**. Du moins en informatique. Dès qu'un bout de code vous semble magique, **il faut s'arrêter et essayer de le comprendre**. Quite à y passer du temps ! Ce temps n'est jamais perdu car il vous fait progresser et vous permettra de comprendre plus vite les prochains bouts de code.
>
> De plus, n'oubliez pas qu'internet existe et est plein de ressources et enfin, que certains profs savent aussi des choses et peuvent peut-être vous aider :-)
{.note}

## les fichiers

les trois fichiers du projet final sont [disponibles](https://github.com/FrancoisBrucker/cours_informatique/tree/master/docs/cours/algorithme-code-theorie/code/projets-code/pourcentages)

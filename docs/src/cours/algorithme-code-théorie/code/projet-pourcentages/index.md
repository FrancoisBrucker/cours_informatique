---
layout: layout/post.njk 
title: "Projet pourcentage"

eleventyNavigation:
  key: "Projet pourcentage"
  parent: Code
---

{% prerequis "**Prérequis** :" %}

* [Mise en œuvre d'un projet informatique](../projet-hello-dev/)
* [Naviguer dans un système de fichiers]({{"/tutoriels/fichiers-navigation" | url }})
* [Terminal]({{"/tutoriels/terminal" | url }})
* [Utilisation du Terminal]({{"/tutoriels/terminal-utilsation" | url }})

{% endprerequis %}

<!-- début résumé -->

Le but de ce cours est de dérouler la création et la mise en œuvre d'un projet, petit à petit.

<!-- end résumé -->

Vous allez créer un projet visant à compter le pourcentage de `0` dans un nombre écrit en binaire.

## Mise en place

### Où est python

{% faire "Dans un terminal ou un explorateur de fichier :" %}

Déterminez quel est chemin absolu du python utilisé par défaut dans le terminal

{% endfaire %}

Une fois que le chemin du python du terminal est connu :

{% faire %}

* déterminez l'exécutable python utilisé par défaut par vscode
* faites en sorte que le python de vscode et celui du terminal coïncident, en changeant celui de vscode si nécessaire.

{% endfaire %}

{% attention %}

Il est crucial de savor quel interpréteur python est exécuté pendant un projet.

{% endattention %}

Dans la suite de ce TD, on utilisera toujours le nom de python pour l'interpréteur par défaut utilisé dans vscode. Votre interpréteur peut être différent (utilisez [ce tutoriel]({{ "/tutoriels/vsc-python" | url}}#quel-python) pour le connaître).

### Dossier du projet

{% faire %}

1. Créez ci ce n'est pas déjà fait avec l'explorateur de fichier un dossier où vous placerez tous les projets de ce cours.
2. ouvrez un terminal dans ce dossier
3. créer **avec le terminal** un dossier intitulé `pourcentage_binaire`{.fichier} dans le dossier courant du terminal

{% endfaire %}

### Projet vscode

{% faire %}
Créer un nouveau projet vscode en ouvrant le dossier `pourcentage_binaire`{.fichier}.
{% endfaire %}

### Créations des fichiers

{% faire %}

Créez avec vscode 3 fichiers (que l'on garde vides pour l'instant) dans le projet :

* `main.py`{.fichier} : le programme principal
* `pourcentage.py`{.fichier} : le code
* `test_pourcentage.py`{.fichier} : notre fichier de tests

{% endfaire %}

{% info %}

On a coutume d'associer à chaque fichier de code son fichier de tests dont le nom est le même que le fichier de code précédé de `test_`{.fichier}.

{% endinfo %}

## Le projet

Le projet final consistera à demander à l'utilisateur un nombre décimal et de répondre le pourcentage de 0 dans ce nombre lorsqu'on l'écrit en binaire.

Pour arriver à ce but, on va procéder petit à petit. On s'assurera du bon fonctionnement du code en ajoutant des tests (qu'on conservera !) à chaque étape.

### Le code

On veut compter le nombre de $0$ d'un nombre écrit en binaire. Un entier n'ayant pas de base définie (c'est le même entier quelque soit la base), si l'on veut compter le nombre de $0$ de sa représentation binaire, il faut transformer notre entier en une chaîne de caractères constituées de `"0"`{.language-} et de `"1"`{.language-} et compter le nombre de caractères `"0"`{.language-}.

Mais avant de penser à la conversion d'un entier, essayons de voir comment compter le nombre de `"0"` d'une chaîne de caractères.

{% exercice %}

Dans le fichier `pourcentage.py`{.fichier} créez une fonction `pourcent` dont l'entrée nommée `chaîne_de_caractères` est une chaîne de caractères composée de de `"0"`{.language-} et de `"1"`{.language-} et qui rend le pourcentage de `"0"`{.language-} dans cette chaîne.

{% endexercice %}
{% attention %}

Assurez vous que le [linter](../projet-hello-dev#linter) soit content. Il ne doit y avoir aucune faute de style.

{% endattention %}

Il n'est pas nécessaire de vérifier :

* que l'entrée est une chaîne de caractères
* que la chaîne est uniquement composée de `"0"` et de `"1"`

En effet, le nom du paramètre est explicite, donc s'il y a une erreur c'est de la faute du développeur. Le programme va planter si on met un entier dans `chaîne_de_caractères`, puisque les entiers ne peuvent être mis dans une boucle for.

{% note %}
Si les entrées de nos méthodes sont spécifiées dans le code ou la documentation ou par des noms explicites, ce n'est pas la peine de vérifier dans le code que c'est ok.
{% endnote %}

On aurait pu être tenté de rendre aussi `0`{.language-} lorsque l'entrée n'est pas une chaîne de caractère. **CE N'EST PAS UNE BONNE IDÉE !** car aurait masqué le mauvais type d'entrée dans la fonction tout en donnant un résultat cohérent :

{% note "**Coding mantra :** il vaut mieux qu'un programme plante plutôt qu'il cache une erreur." %}

L'erreur ne va pas partir d'elle même, elle va juste faire planter le programme autre-part, loin de l'erreur réelle. Elle sera donc bien plus dur à trouver et à corriger.

{% endnote %}

### Les tests

Pour vous assurer que la fonction `pourcent`{.language-} fonctionne, vous avez du faire des tests. Il faut les conserver car un code c'est la fonction **et** ses tests.

Par exemple, on pourrait tester que :

* `"11"` rende bien `0`
* `"00"` rende bien `1`.

{% faire %}
Mettez le code suivant dans `test_pourcentage.py`{.fichier} :

```python
from pourcentage import pourcent


def test_pourcent_0():
    assert pourcent('11') == 0


def test_pourcent_1():
    assert pourcent('00') == 100

```

Testez ensuite que vos tests fonctionnent :

* avec l'erlenmeyer de vscode
* dans un terminal dont le dossier courant est le dossier du projet en tapant `python -m pytest`

{% endfaire %}

On a testé les cas limites de notre fonction. Ajoutons un cas général, où il y a à la fois des `"0"`{.language-} et des `"1"`{.language-}, par exemple que  `"101"`{.language-} rende `100 * (1/3)`{.language-}.

Ceci nous impose de tester l'égalité entre 2 réels. Ceci est impossible à faire en informatique car il faudrait regarder une infinité de chiffres après la virgule... Or les réels en informatique sont en fait des entiers déguisés, ce sont des approximations (voir [la doc](https://docs.python.org/fr/3/tutorial/floatingpoint.html))).

{% note %}
Les réels sont des limites, ils n'ont pas d'existence tangible. En bref : les réels ne le sont pas, seuls les entiers le sont.
{% endnote %}

On ne peut donc pas écrire directement `assert pourcent('101') == 100 * (1/3)` (même si là, ça risque de marcher) car si ça se trouve on aura `33.333333336` à la place de `100/3`.

{% note  "**Coding mantra :**" %}
On ne teste **JAMAIS** l'égalité entre 2 réels. On les compare toujours à $\epsilon$ près.
{% endnote %}

Pour cela, on va utiliser une fonction spéciale de `pytest`, qui vérifie si 2 réels sont *à peu près égaux* (par défaut à dix moins six près) : [approx](https://docs.pytest.org/en/latest/reference.html#pytest-approx).

Comme nos deux autres tests comparaient déjà des réels, on va les modifier pour qu'ils utilisent approx avant d'ajouter le nouveau test

{% faire %}
Mettez le code suivant dans `test_pourcentage.py`{.fichier}, et vérifiez que les tests passent toujours :

```python
from pytest import approx

from pourcentage import pourcent


def test_pourcent_0():
    assert pourcent('11') == approx(0)


def test_pourcent_1():
    assert pourcent('00') == approx(100)

```

{% endfaire %}
{% note "**Style** : L'ordre des `import` est, [par coutume](https://google.github.io/styleguide/pyguide.html#s3.13-imports-formatting), le suivant :" %}

1. les modules de python
2. les modules externes
3. les imports de notre projet

On saute une ligne entre chaque groupe d'import pour bien voir les différences.
{% endnote %}

On peut maintenant ajouter le nouveau test :

{% faire %}
Ajoutez à `test_pourcentage.py`{.fichier} le test suivant, puis testez que les 3 tests passent.

```python
# ...

def test_pourcent_01():
    assert pourcent('101') == approx(100/3)

# ...
```

{% endfaire %}

On a 3 tests. Deux de ces tests correspondent aux cas limites, et le troisième à un cas général.

{% note  "**Coding mantra :** que tester ?" %}
Ce qui est nécessaire pour que **vous** (*ie.* le développeur) soyez convaincu que votre fonction marche. Ni plus, ni moins.
{% endnote %}

{% note  "**Coding mantra :** pourquoi tester ?" %}
Pour être sûr que le programme fonctionne. Pour permettre d'ajouter rapidement des fonctionnalités sans avoir à **tout** re-tester (les tests sont déjà écrits). Parce que **tout le monde** fait des erreurs. Oui oui, même toi qui te crois fort.
{% endnote %}

C'est **TOUJOURS** au développeur de la fonction de faire ses tests. Parce qu'il faut que les testent accompagnent le code, pour que l'on soit sûr du fonctionnement et puisse coder la suite tranquillement. Si l'on fait les tests à la fin de la journée :

* c'est embêtant
* si ça se trouve on devra refaire plein de choses car un bug en aura entraîné un autre et tout un tas de fonctions seront à corriger. En faisant les tests dès que la méthode est écrite, on gagne du temps
* si c'est quelqu'un d'autre qui les fait, comment être sûr que ce soit les bons tests ? Qu'ils couvrent bien tout le fonctionnement du code ? Il faut que l'autre personne comprenne également le code. On perd donc du temps puisqu'il faut faire 2 fois le boulot de compréhension.

### Programme principal

Faisons notre première tentative de programme principal. On va demander directement à l'utilisateur de rentrer un nombre écrit en binaire.

#### Un premier jet

{% exercice %}

Pour interagir avec l'utilisateur, vous utiliserez la fonction [input](https://docs.python.org/fr/3/library/functions.html#input) de python pour cela. Répondez aux questions :

* de quel type est le résultat de la fonction `input`{.language-} ?
* pourquoi ?

{% endexercice %}
{% details "solution" %}

Le retour de la fonction `input`{.language-} est une chaîne de caractères. C'est normal car l'utilisateur a tapé des caractères sur son clavier.

Toute interaction avec l'utilisateur est par défaut considéré comme une chaîne de caractères. C'est au programme de faire la conversion si nécessaire.

{% enddetails %}

{% exercice %}

Dans  le fichier `main.py`{.fichier}, créez un programme principal qui demande à l'utilisateur d'écrire un nombre en binaire, puis qui rende le pourcentage de "0" de ce nombre.

Faite le programme le plus simple possible.

{% endexercice %}

A priori,comme le code est simple on ne vérifie pas que :

* c'est bien un nombre binaire : que donne le code si on ne met pas un nombre binaire ?
* il a une longueur non vide : que fait le programme si on appuie sur la touche entrée sans rien écrire ?

#### Vérification des entrées utilisateurs

Quand je vous avais dit de ne pas faire de vérification, c'est vrai pour tout ce qui a trait au code utilisé par l'ordinateur. Dès qu'un humain utilise du code, il faut **TOUT** vérifier et faire en sorte qu'il ait la meilleure expérience possible.

{% note %}

Tout ce que fait l'utilisateur doit être vérifié avant d'être injecté dans le programme. C'est la [loi de Murphy](https://fr.wikipedia.org/wiki/Loi_de_Murphy) : si on laisse la possibilité de se tromper, quelqu'un va forcément le faire à un moment.

{% endnote %}

Donc ici on pourrait :

* faire rentrer à l'utilisateur un nombre en base 10,
* ne pas planter et redemander à l'utilisateur de taper un nombre si ce n'est pas un nombre en base 10
* lui montrer son nombre en base 2 puis donner son pourcentage

On utilise la [gestion des erreurs de python](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) pour ça (Cela dépasse un peu le cadre de ce cours, on ira donc pas plus loin que vous montrer que ça existe)

{% faire %}
Mettez le code suivant dans `main.py`{.fichier} :

```python
from pourcentage import pourcent

correct = False
entier = 0

while not correct:
    correct = True
    chaîne = input('Donnez un nombre écrit en base 10 :')
    try:
        entier = int(chaîne)
    except ValueError:
        correct = False
        print("ce n'est pas un nombre. Essayez encore une fois.")

nombre_binaire = bin(entier)[2:]

print("Votre nombre",
      chaîne, "contient ", pourcent(nombre_binaire),
      "pourcent de 0 en base 2 (" + nombre_binaire + ").")
```

Exécutez le code et comprenez comment il fonctionne. En particulier :

* comment fonctionne la boucle `while`{.language-} ?
* notre nombre a été converti en plein de types différents. Lesquels ?
* comment est géré l'erreur possible ?
* ..

Faites de petits bout de code qui isolent ces différents points et exécutez les pour comprendre comment cela fonctionne.
{% endfaire %}

Il faut toujours faire l'effort de comprendre le code que vous copiez/collez. Ce n'est que comme ça que vous progresserez. Pour cela, isolez la partie de code que vous voulez comprendre en refaisant un programme qui n'utilise que ça.

{% attention "**La magie n'existe pas**" %}
Du moins en informatique.
{% endattention %}
{% note %}
Dès qu'un bout de code vous semble magique, **il faut s'arrêter et essayer de le comprendre**. Quite à y passer du temps ! Ce temps n'est jamais perdu car il vous fait progresser et vous permettra de comprendre plus vite les prochains bouts de code.

De plus, n'oubliez pas qu'internet existe et est plein de ressources et enfin, que certains profs savent aussi des choses et peuvent peut-être vous aider :-)
{% endnote %}

## Les fichiers

les trois fichiers du projet final sont [disponibles](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/algorithme-code-th%C3%A9orie/code/projet-pourcentages/pourcentages)

---
layout: page
title:  "vsc et python : outils supplémentaires"
tags: 
    - installation 
    - configuration
    - python
---

Configuration d'outils supplémentaires pour [visual studio code](https://code.visualstudio.com/) et le développement en python.

<!--more-->

Ce tutoriel fait suite au [tutoriel python et vscode]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-python.md %}). Il se consacre à l'installation d'extension non fondamentales mais bien sympathique pour le développement python. avec vscode.

## tests

> [tests avec vscode](https://code.visualstudio.com/docs/python/testing). Nous allons utiliser [pytest](https://docs.pytest.org/) comme bibliothèque de test.

### installation {#installation-pytest}

{% details sous linux et mac %}

```shell
python3 -m pip install pytest
```

{% enddetails %}

{% details sous windows %}

```shell
python -m pip install pytest
```

{% enddetails %}

### configuration {#configuration-pytest}

1. dans les préférences (*menu file/code > Préferences > settings*) tapez `python.testing.pytestEnabled`  dans la barre de recherche et cochez la case. Ceci dit à vscode que notre framework de test est pytest (il y en a d'autres possible comme [unittest](https://docs.python.org/fr/3.9/library/unittest.html) ou encore [nosetests](https://nose.readthedocs.io/en/latest/), mais on ne va pas les utiliser. Assurez vous cependant qu'un seul framework de test soit utilisé à la fois. Ca devrait être le cas si vous n'avez pas cliqué un peu partout).
2. on configure les tests de notre projet en tapant la commande (dans la [palette de commande]({% link _tutoriels/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main.md %}#palette-de-commande)) : *python : Configure tests* on choisit *pytest* puis *. (root)* qui donne le dossier de départ où aller chercher nos tests

### utilisation {#utilisation-pytest}

#### avec l'interface

On ouvre la fenêtre de tests avec *Menu Affichage testing* (le petit erlenmeyer de la [barre d'activité](https://code.visualstudio.com/docs/getstarted/userinterface)).

En suite le menu *TESTING* en haut de cette nouvelle fenêtre vous permet :

* redécouvrir les tests
* executez les tests.
* ...

![tests]({{ "/assets/tutos/vsc-python/python-pytest-env.png" | relative_url }}){:style="margin: auto;display: block}

#### avec le terminal

En tapant `pytest` alors que vous êtes dans le dossier du projet.

>si la commande `pytest` n'est pas reconnue, mais que `python` l'est vous pouvez exécuter `pytest`, via python en tapant la commande `python3 -m pytest`

## linter

Le [linting en python avec vscode](https://code.visualstudio.com/docs/python/linting) permet de souligner les fautes de style de python.

C'est une aide précieuse pour écrire du code qui est à la fois fonctionnel et lisible. Cela permet de supprimer la majorité des problèmes avant l'exécution.

Il faut installer des plugins pythons spécifiques pour le linting. Il en existe de nombreux. On vous propose ici d'utiliser [pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html) qui permet de respecter la [PEP8](https://www.python.org/dev/peps/pep-0008/).

### installation {#installation-pycodestyle}

Dans un [terminal]({% link _tutoriels/systeme/2021-08-24-terminal.md %}),
qui peut être [celui de vscode]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-terminal.md %}#terminal-integre) tapez la commande :

{% details sous linux et mac %}

```shell
python3 -m pip install pycodestyle
```

{% enddetails %}

{% details sous windows %}

```shell
python -m pip install pycodestyle
```

{% enddetails %}

Une fois ce module python installé, on va pouvoir l'utiliser dans vscode

### configuration {#configuration-pycodestyle}

Pour mettre en route le linting via pycodestyle, deux paramètres sont à positionner :

* `python.linting.enabled` doit être coché pour mettre en route le linting
* `python.linting.pycodestyleEnabled` doit être coché pour utiliser `pycodestyle` comme linter
* `python.linting.pycodestylePath` doit donner le chemin vers `pycodestyle`. Il est par défaut positionné sur `pycodestyle` ce qui devrait être correct.

> Notez que vous pouvez aussi accéder à ces commande via la [palette de commande]({% link _tutoriels/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main.md %}#palette-de-commande),par exemple avec la commande *python: enable/disable linting*.

### pycodestyle dans le terminal

Vous pouvez aussi toujours exécuter la commande `pycodestyle mon-fichier.py` dans un [terminal intégré]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-terminal.md %}#terminal-integre) pour obtenir le linting de votre fichier. C'est moins pratique que lorsque vscode le fait puisque la ligne en question n'est pas soulignée dans l'interface.

### style

Certaines erreurs de pycodestyle sont énervante, car ce n'en sont pas vraiment (comme le nombre maximum de caractère dans une ligne). On peut le configurer pour qu'il *oublie* ces erreurs.

La liste des différentes erreur est [disponible dans la doc](https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes). L'erreur de ligne trop longue est ainsi l'erreur `E501`.

Nous pouvons ajouter dans la configuration de pycodestyle pour vscode au paramètre `python.linting.pycodestyleArgs` la ligne `--ignore=E501`.

## black {#black}

[BLack](https://black.readthedocs.io/en/stable/index.html) est un bijou. Ne pas l'utiliser tout le temps est bête.

Son but est de re-formater sans faute de style tout programme python.

### installation {#installation-black}

Dans un [terminal]({% link _tutoriels/systeme/2021-08-24-terminal.md %}),
qui peut être [celui de vscode]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-terminal.md %}#terminal-integre) tapez la commande :

{% details sous linux et mac %}

```shell
python3 -m pip install black
```

{% enddetails %}

{% details sous windows %}

```shell
python -m pip install black
```

{% enddetails %}

Une fois ce module python installé, on va pouvoir l'utiliser dans vscode

### configuration {#configuration-black}

A priori tout est ok sans aucune autre configuration sous vscode. On peut lister deux paramètre auxquels faire attention :

* `python.formatting.blackPath`: qui vaut `black` par défaut
* `python.formatting.provider` : qui donne l'outil de formatage de fichier par défaut utilisé, et qui vaut `black` par défaut.

### utilisation

Si vous avez le paramètre `editor.formatOnSave` de coché à chaque sauvegarde de votre fichier, il sera reformaté. Notez que cela ne marche pas si votre fichier est sauvegardé automatiquement après un délai.

Vous pouvez aussi :

* exécuter directement la commande *format document* dans [palette de commande]({% link _tutoriels/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main.md %}#palette-de-commande).
* utiliser son [raccourci clavier](https://code.visualstudio.com/docs/editor/codebasics#_formatting)

### black dans le terminal

{% details sous linux et mac %}

```shell
python3 -m black mon-fichier.py
```

{% enddetails %}

{% details sous windows %}

```shell
python -m black mon-fichier.py
```

{% enddetails %}

## couverture de code {#code-coverage}

Permet de voir le code couvert par les tests.

### installation {#installation-coverage}

#### coverage pour pytest

On va utiliser le *code coverage* de pytest :

{% details sous linux et mac %}

```shell
python3 -m pip install pytest-cov
```

{% enddetails %}

{% details sous windows %}

```shell
python -m pip install pytest-cov
```

{% enddetails %}

#### extension vscode

Puis l'extension de vscode qui permet de rendre compte du coverage dans l'interface. Tapez [Coverage Gutters](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters) dans le *menu affichage > extensions*.

### utilisation {#code-coverge}

La documentation complète du module est disponible à cette adresse : <https://pytest-cov.readthedocs.io/en/latest/>.

Ce module utilise [coverage](https://coverage.readthedocs.io/en/6.3.1/index.html), qui est le module de couverture de code utilisé. Il est très configurable.

#### sans l'extension

Dans un terminal tapez `python3 -m pytest --cov=.`. Cela exécute les tests à partir du dossier courant (`.`) avec le coverage qui sera retourné au format texte.

Si l'on veut les ligne manquantes, on peut utiliser la commande : `--cov-report term-missing`

Enfin, pour avoir un rapport html complet on peut utiliser la ligne : `python3 -m pytest --cov=. --cov-report html`.

#### utilisation de l'extension

La commande `python3 -m pytest --cov=.` crée un fichier de coverage qui s'appelle `.coverage`. Il n'est cependant pas lisible dans ce format par défaut par l'extension. Il faut générer un format de sorti en [xml](https://fr.wikipedia.org/wiki/Extensible_Markup_Language) avec la commande : `python3 -m pytest --cov=.  --cov-report xml:cov.xml`

> Si le petit *watch* n'est pas visible dans la barre de status, vous pouvez le faire à la main dans avec la [palette de commande]({% link _tutoriels/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main.md %}#palette-de-commande))
 *Coverage Gutters: Display Coverage*.

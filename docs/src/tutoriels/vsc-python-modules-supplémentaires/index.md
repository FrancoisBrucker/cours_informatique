---
layout: layout/post.njk

title: Outils complémentaires pour Vsc et python
tags: ['tutoriel', 'vsc', 'python']
authors: 
    - François Brucker

eleventyNavigation:
  key: "Outils complémentaires pour Vsc et python"
  parent: Tutoriels

prerequis:
    - '../vsc-python/'
---

<!-- début résumé -->

Ce tutoriel se consacre à l'installation d'extensions non fondamentales mais bien sympathiques pour le développement en python avec vscode.

<!-- fin résumé -->

## <span id="pytest"></span> tests

{% lien %}
[tests avec vscode](https://code.visualstudio.com/docs/python/testing)
{% endlien %}

Nous utilisons [pytest](https://docs.pytest.org/) comme bibliothèque de test.

### <span id="installation-pytest"></span> Installation

{% details "sous linux et mac" %}

`python3 -m pip install pytest`

{% enddetails %}

{% details "sous windows" %}

`python -m pip install pytest`

{% enddetails %}

### <span id="configuration-pytest"></span> Configuration

1. dans les préférences (*menu file/code > Preferences > settings*) tapez `python.testing.pytestEnabled`  dans la barre de recherche et cochez la case. Ceci dit à vscode que notre bibliothèque de test est pytest (il y en a d'autres possible comme [unittest](https://docs.python.org/fr/3.9/library/unittest.html) ou encore [nosetests](https://nose.readthedocs.io/en/latest/), mais on ne va pas les utiliser. Assurez vous cependant qu'un seul framework de test soit utilisé à la fois. Ca devrait être le cas si vous n'avez pas cliqué un peu partout).
2. on configure les tests de notre projet en tapant la commande (dans la [palette de commande](../vsc-installation-et-prise-en-main#palette-de-commande)) : *python : Configure tests* on choisit *pytest* puis *. (root)* qui donne le dossier de départ où aller chercher nos tests

### <span id="utilisation-pytest"></span> Utilisation

{% faire %}
Créez un fichier que vous appellerez `test_projet.py`{.fichier} dans votre projet. Collez-y- le code suivant :

```python
def test_oui():
    assert 4 == 2 + 2


def test_non():
    assert "4" == 2 + 2
```

{% endfaire %}

Le fichier créé est un fichier de test. Il faut l'utiliser via la bibliothèque `pytest` que vous venez d'installer. Ceci peut se faire directement avec vscode en ouvrant la fenêtre de tests avec *Menu Affichage testing* (le petit erlenmeyer de la [barre d'activité](https://code.visualstudio.com/docs/getstarted/userinterface)).

En suite le menu *TESTING* en haut de cette nouvelle fenêtre vous permet :

* redécouvrir les tests
* exécutez les tests.
* ...

![tests](python-pytest-env.png)

On peut également directement utiliser pytest avec le terminal, en tapant `python -m pytest` (`python3 -m pytest` si votre interpréteur est `python3`) alors que vous êtes dans le dossier du projet.

## <span id="pycodestyle"></span> Linter

Le [linting en python avec vscode](https://code.visualstudio.com/docs/python/linting) permet de souligner les fautes de style de python.

C'est une aide précieuse pour écrire du code qui est à la fois fonctionnel et lisible. Cela permet de supprimer la majorité des problèmes avant l'exécution.

Il faut installer des plugins pythons spécifiques pour le linting. Il en existe de nombreux. On vous propose ici d'utiliser [pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html) qui permet de respecter la [PEP8](https://www.python.org/dev/peps/pep-0008/).

### <span id="installation-pycodestyle"></span> Installation

Dans un [terminal](../terminal),
qui peut être [celui de vscode](vsc-terminal#terminal-intégré) tapez la commande :

{% details "sous linux et mac" %}

`python3 -m pip install pycodestyle`

{% enddetails %}

{% details "sous windows" %}

`python -m pip install pycodestyle`

{% enddetails %}

Une fois ce module python installé, on va pouvoir l'utiliser dans vscode

### <span id="configuration-pycodestyle"></span> Configuration

Pour mettre en route le linting via pycodestyle, deux paramètres sont à positionner :

* `python.linting.enabled` doit être coché pour mettre en route le linting
* `python.linting.pycodestyleEnabled` doit être coché pour utiliser `pycodestyle` comme linter
* `python.linting.pycodestylePath` doit donner le chemin vers `pycodestyle`. Il est par défaut positionné sur `pycodestyle` ce qui devrait être correct.

{% info %}
Notez que vous pouvez aussi accéder à ces commande via la [palette de commande](../vsc-installation-et-prise-en-main#palette-de-commande),par exemple avec la commande *python: enable/disable linting*.
{% endinfo %}

### Pycodestyle dans le terminal

Vous pouvez aussi toujours exécuter la commande `pycodestyle mon-fichier.py` dans un [terminal intégré](../vsc-terminal#terminal-intégré) pour obtenir le linting de votre fichier. C'est moins pratique que lorsque vscode le fait puisque la ligne en question n'est pas soulignée dans l'interface.

### Style

Certaines erreurs de pycodestyle sont énervante, car ce n'en sont pas vraiment (comme le nombre maximum de caractère dans une ligne). On peut le configurer pour qu'il *oublie* ces erreurs.

La liste des différentes erreur est [disponible dans la doc](https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes). L'erreur de ligne trop longue est ainsi l'erreur `E501`.

Nous pouvons ajouter dans la configuration de pycodestyle pour vscode au paramètre `python.linting.pycodestyleArgs` la ligne `--ignore=E501`.

## <span id="black"></span> Black

[Black](https://black.readthedocs.io/en/stable/index.html) est un bijou. Ne pas l'utiliser tout le temps est bête.

Son but est de re-formater sans faute de style tout programme python.

### <span id="installation-black"></span> Installation

Dans un [terminal](../terminal),
qui peut être [celui de vscode](../vsc-terminal#terminal-intégré) tapez la commande :

{% details "sous linux et mac" %}

`python3 -m pip install black`

{% enddetails %}

{% details "sous windows" %}

`python -m pip install black`

{% enddetails %}

Une fois ce module python installé, on va pouvoir l'utiliser dans vscode

### <span id="configuration-black"></span> Configuration

A priori tout est ok sans aucune autre configuration sous vscode. On peut lister deux paramètre auxquels faire attention :

* `python.formatting.blackPath`: qui vaut `black` par défaut
* `python.formatting.provider` : qui donne l'outil de formatage de fichier par défaut utilisé, et qui vaut `black` par défaut.

### Utilisation

Si vous avez le paramètre `editor.formatOnSave` de coché à chaque sauvegarde de votre fichier, il sera reformaté. Notez que cela ne marche pas si votre fichier est sauvegardé automatiquement après un délai.

Vous pouvez aussi :

* exécuter directement la commande *format document* dans [palette de commande](../vsc-installation-et-prise-en-main#palette-de-commande).
* utiliser son [raccourci clavier](https://code.visualstudio.com/docs/editor/codebasics#_formatting)

### Black dans le terminal

{% details "sous linux et mac" %}

`python3 -m black mon-fichier.py`

{% enddetails %}

{% details "sous windows" %}

`python -m black mon-fichier.py`

{% enddetails %}

## <span id="code-coverage"></span> Couverture de code

Permet de voir le code couvert par les tests.

### <span id="installation-coverage"></span> Installation

#### Coverage pour pytest

On va utiliser le *code coverage* de pytest :

{% details "sous linux et mac" %}

`python3 -m pip install pytest-cov`

{% enddetails %}

{% details "sous windows" %}

`python -m pip install pytest-cov`

{% enddetails %}

#### Extension vscode

Puis l'extension de vscode qui permet de rendre compte du coverage dans l'interface. Tapez [Coverage Gutters](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters) dans le *menu affichage > extensions*.

### <span id="code-coverge"></span> Utilisation

La documentation complète du module est disponible à cette adresse : <https://pytest-cov.readthedocs.io/en/latest/>.

Ce module utilise [coverage](https://coverage.readthedocs.io/en/6.3.1/index.html), qui est le module de couverture de code utilisé. Il est très configurable.

#### Sans l'extension

Dans un terminal tapez `python3 -m pytest --cov=.`. Cela exécute les tests à partir du dossier courant (`.`) avec le coverage qui sera retourné au format texte.

Si l'on veut les ligne manquantes, on peut utiliser la commande : `--cov-report term-missing`

Enfin, pour avoir un rapport html complet on peut utiliser la ligne : `python3 -m pytest --cov=. --cov-report html`.

#### Utilisation de l'extension

La commande `python3 -m pytest --cov=.` crée un fichier de coverage qui s'appelle `.coverage`. Il n'est cependant pas lisible dans ce format par défaut par l'extension. Il faut générer un format de sorti en [xml](https://fr.wikipedia.org/wiki/Extensible_Markup_Language) avec la commande : `python3 -m pytest --cov=.  --cov-report xml:cov.xml`

{% info %}
Si le petit *watch* n'est pas visible dans la barre de status, vous pouvez le faire à la main dans avec la [palette de commande](../vsc-installation-et-prise-en-main#palette-de-commande))
 *Coverage Gutters: Display Coverage*.
{% endinfo %}

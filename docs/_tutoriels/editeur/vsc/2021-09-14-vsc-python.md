---
layout: page
title:  "vscode et python"
tags: 
    - installation 
    - configuration
    - python
---

Configuration de python avec vscode.

<!--more-->

> prérequis
>
> * [vscode]({% link _tutoriels/editeur/vsc/vsc-installation-et-prise-en-main.md %})
> * [python installation]({% link _tutoriels/python/2021-08-20-installation-de-python.md %})
>
{: .chemin}

configuration de  [visual studio code](https://code.visualstudio.com/) pour le développement en python.

<!--more-->

## extension python pour vscode

> La documentation officielle de vscode a [une partie consacrée à python](https://code.visualstudio.com/docs/languages/python).
{: .chemin}

La principale extension à installer lorsque l'on fait du python est [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) développée par microsoft. Il est également recommandé d'installer [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) (utilitaire puissant d'aide au code).

Pour installer ces package :

> Rendez vous dans la [gestion des extensions de vscode]({% link _tutoriels/editeur/vsc/vsc-installation-et-prise-en-main.md %}#extensions), puis tapez *python* dans la barre de recherche. Assurez vous d'installer les package créés par microsoft.
{: .a-faire}

## interpréteur python

> Si vous n'avez pas d'interpréteur python par défaut vscode vous demandera de le donner (il vous aide en cherchant lui même des possibilités) lors du premier chargement d'un fichier python.

Les paramètres de l'interpréteur se trouvent dans [les paramètres vscode](https://code.visualstudio.com/docs/getstarted/settings) :

{% details sous linux %}

*menu Fichier > préférences > paramètres*

{% enddetails %}

{% details sous mac %}

 *menu Code > préférences > paramètres*

{% enddetails %}

{% details sous windows %}

*menu Fichier > préférences > paramètres*

{% enddetails %}

Puis, une fois dans l'onglet paramètres allez dans *extensions > python* dans le menu de gauche. Les préférences vscode consistent en des variables (*ID du paramètre*) à positionner selon ses envies, chaque variable modifiant un comportement de vscode.

> Il y a deux fois les mêmes préférences : **utilisateur** et  **espace de travail**. Le premier concerne les préférences générales de vscode et le second les préférences du projet courant. Par défaut, modifiez les préférences **utilisateur**. Pour plus d'informations, lisez la [doc](https://code.visualstudio.com/docs/getstarted/settings).

Il y a deux préférences qu'ils faut a priori modifier :

* **Default Interpreter Path** dont l'ID est `python.defaultInterpreterPath`. C'est le chemin vers l'interpéteur python.
* **Conda Path** dont l'ID est `python.condaPath`. C'est le chemin vers le programme `conda` si vous utilisez la version anaconda de python.

Vous pouvez directement chercher le paramètre en tapant son nom dans la barre de recherche.

Si vous avez suivi le [tutoriel anaconda]({% link _tutoriels/python/2021-09-14-installation-anaconda.md %}), vérifiez ou faites en sorte que les paramètres soient :

{% details sous linux %}

> trouver un linux pour savoir
{: .tbd}

{% enddetails %}

{% details sous mac %}

* `python.defaultInterpreterPath` : `/opt/anaconda3/bin/python3`
* `python.condaPath` : `/opt/anaconda3/bin/conda`

{% enddetails %}

{% details sous windows %}

* `python.defaultInterpreterPath` : `C:\programData\Anaconda3\python.exe`
* `python.condaPath` : `C:\programData\Anaconda3\Scripts\conda.exe`

{% enddetails %}

> Faites en sorte que les paramètres python soient correct pour votre système.
{: .a-faire}

## exécuter du python {#execution-python}

Il y a deux façons principales d'exécuter du code python avec vscode. Chacune avec avantages et inconvénients. Il est donc recommandé de toutes les connaitre.

### triangle vert

Vous pouvez exécuter l'onglet courant en python en [cliquant sur le triangle en haut à droite de l'interface](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world).

### terminal

Vous pouvez utiliser [le terminal intégré]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-terminal.md %}#terminal-integre) pour exécuter vous programmes python comme vous le feriez avec un terminal externe.

## premier programme

### projet vscode

> Créez un dossier nommé *"cours-python"* sur votre ordinateur, et ouvrez le avec vscode (*menu Fichier > ouvrir le dossier...*).
{: .a-faire}

Une fois que vous avez dit que vous faisiez confiance au développeur de ce projet, fermez l'onglet *Welcome*. Vous pouvez même fermer l'explorer en cliquant sur l'icône en sur-brillance dans la barre d'activité de [l'interface vsc](https://code.visualstudio.com/docs/getstarted/userinterface).

Nous allons commencer par utiliser le [le terminal intégré]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-terminal.md %}#terminal-integre) de vscode pour exécuter nos premiers programmes python avant d'écrire nos programmes de plusieurs lignes.

### interpréteur python dans le terminal vscode

> Ouvrez un [terminal dans vscode]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-terminal.md %}) : *menu Affichage > Terminal*.
{: .a-faire}

Le [terminal]({% link _tutoriels/systeme/2021-08-24-terminal.md %}) permet d'exécuter des commandes de votre système.

> taper `python` sous windows ou `python3` sous linux et mac pour rentrer dans l'interpréteur python.
{: .a-faire}

![interpreteur]({{ "/assets/tutos/vsc-python/python-interpreteur.png" | relative_url }}){:style="margin: auto;display: block"}

#### une première ligne de python

Dans l'interpréteur (à côté des `>>>`, qu'on appelle [invite de commande ou prompt](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande)) :

> tapez :
>
>```python
>print("Bonjour monde !")
>```
>
> Puis appuyez sur la touche entrée.
{: .a-faire}

Vous devriez avoir quelque chose du genre à la sortie :

![hello world]({{ "/assets/tutos/vsc-python/python-hello-world-interpreteur.png" | relative_url }}){:style="margin: auto;display: block}

Ca a l'air d'avoir marché. La ligne de code a affiché à l'écran `Bonjour Monde`, puis l'invite de commande est revenue (une fois l'instruction exécutée, on attend la suivante).

#### quitter l'interpréteur

Pour quitter l'interpréteur python :

> Tapez `quit()` puis appuyez sur la touche entrée.
{: .a-faire}

### création d'un fichier

> Créez un fichier *"programme.py"* (*menu Fichier > New File* puis sauvez le immédiatement *menu Fichier > Save*).
{: .a-faire}

Si vous n'avez pas encore configuré python, vscode va vous demander le faire.

> Ecrivez dans le fichier ouvert dans vscode :
>
>```python
>print("Bonjour monde !")
>```
>
{: .a-faire}

Vous pouvez alors l'exécuter :

> * dans le terminal en tapant : `python programme.py` ou `python3 programme.py` selon le nom de votre interpréteur
> * en cliquant sur [le triangle en haut à droite de la fenêtre vsc](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world)
{: .a-faire}

Remarquez que lorsque vous exécutez votre programme via la seconde solution, cela crée un nouveau terminal qui s'appelle *Python*.

![hello world]({{ "/assets/tutos/vsc-python/python-interpreteur-execution-python.png" | relative_url }}){:style="margin: auto;display: block}

## outils indispensables

Il existe de nombreux plugins de vscode que l'on peut utiliser pour coder en python. Nous en montrerons deux ici, indispensables pour bien coder.

### tests

> [tests avec vscode](https://code.visualstudio.com/docs/python/testing)
{: .chemin}

Nous usilisons [pytest](https://docs.pytest.org/) comme bibliothèque de test.

#### installation {#installation-pytest}

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

#### configuration {#configuration-pytest}

1. dans les préférences (*menu file/code > Préferences > settings*) tapez `python.testing.pytestEnabled`  dans la barre de recherche et cochez la case. Ceci dit à vscode que notre framework de test est pytest (il y en a d'autres possible comme [unittest](https://docs.python.org/fr/3.9/library/unittest.html) ou encore [nosetests](https://nose.readthedocs.io/en/latest/), mais on ne va pas les utiliser. Assurez vous cependant qu'un seul framework de test soit utilisé à la fois. Ca devrait être le cas si vous n'avez pas cliqué un peu partout).
2. on configure les tests de notre projet en tapant la commande (dans la [palette de commande]({% link _tutoriels/editeur/vsc/vsc-installation-et-prise-en-main.md %}#palette-de-commande)) : *python : Configure tests* on choisit *pytest* puis *. (root)* qui donne le dossier de départ où aller chercher nos tests

#### utilisation {#utilisation-pytest}

> Créez un fichier que vous appellerez *"test_projet.py"* dans votre projet. Collez-y- le code suivant :
{: .a-faire}

```python

def test_oui():
    assert 4 = 2 + 2


def test_non():
    assert "4" == 2 + 2

```

Le fichier créé est un fichier de test. Il faut l'utiliser via la bibliothèque `pytest` que vous venez d'installer. Ceci peut se faire directement avec vscode en ouvrant la fenêtre de tests avec *Menu Affichage testing* (le petit erlenmeyer de la [barre d'activité](https://code.visualstudio.com/docs/getstarted/userinterface)).

En suite le menu *TESTING* en haut de cette nouvelle fenêtre vous permet :

* redécouvrir les tests
* exécutez les tests.
* ...

![tests]({{ "/assets/tutos/vsc-python/python-pytest-env.png" | relative_url }}){:style="margin: auto;display: block}

On peut également directement utiliser pytest avec le terminal, en tapant `python -m pytest` (`python3 -m pytest` si votre interpréteur est `python3`) alors que vous êtes dans le dossier du projet.

### linter

Le [linting en python avec vscode](https://code.visualstudio.com/docs/python/linting) permet de souligner les fautes de style de python.

C'est une aide précieuse pour écrire du code qui est à la fois fonctionnel et lisible. Cela permet de supprimer la majorité des problèmes avant l'exécution.

Il faut installer des plugins pythons spécifiques pour le linting. Il en existe de nombreux. On vous propose ici d'utiliser [pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html) qui permet de respecter la [PEP8](https://www.python.org/dev/peps/pep-0008/).

#### installation {#installation-pycodestyle}

Dans un [terminal]({% link _tutoriels/systeme/2021-08-24-terminal.md %}), qui peut être [celui de vscode]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-terminal.md %}#terminal-integre) tapez la commande :

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

#### configuration {#configuration-pycodestyle}

Pour mettre en route le linting via pycodestyle, deux paramètres sont à positionner :

* `python.linting.enabled` doit être coché pour mettre en route le linting
* `python.linting.pycodestyleEnabled` doit être coché pour utiliser `pycodestyle` comme linter
* `python.linting.pycodestylePath` doit donner le chemin vers `pycodestyle`. Il est par défaut positionné sur `pycodestyle` ce qui devrait être correct.

> Notez que vous pouvez aussi accéder à ces commande via la [palette de commande]({% link _tutoriels/editeur/vsc/vsc-installation-et-prise-en-main.md %}#palette-de-commande),par exemple avec la commande *python: enable/disable linting*.

#### pycodestyle dans le terminal

Vous pouvez aussi toujours exécuter la commande `pycodestyle mon-fichier.py`  dans un [terminal intégré]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-terminal.md %}#terminal-integre) pour obtenir le linting de votre fichier. C'est moins pratique que lorsque vscode le fait puisque la ligne en question n'est pas soulignée dans l'interface.

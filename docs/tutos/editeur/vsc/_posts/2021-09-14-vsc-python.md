---
layout: page
title:  "vsc et python"
categories: 
    - installation 
    - configuration
    - python
---

configuration de  [visual studio code](https://code.visualstudio.com/) pour le développement en python.

<!--more-->

> La documentation officielle a une partie consacrée à python : <https://code.visualstudio.com/docs/languages/python>

## extensions

La principale extension à installer lorsque l'on fait du python est [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) développée par microsoft. Il est également recommandé d'installer [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) (utilitaire puissant d'aide au code).

Pour installer ces package, rendez vous dans la [gestion des extensions de vscode]({% post_url tutos/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main %}#extensions), puis tapez *python* dans la barre de recherche. Assurez vous d'installer les package créez par microsoft.

## exécuter du python

### interpréteur

> si vous n'avez pas d'interpréteur python par défaut vscode vous demandera de le donner (il vous aide en cherchant lui même des possibilités) lors du premier chargement d'un fichier python.

Les paramètre de l'interpréteur se trouves dans les paramètres (*menu affichage > extensions*) puis, dans l'onglet paramètres, dans le menu *extensions > python*. Vous pouvez aussi directement chercher le paramètre dans la barre de recherche.

* `python.defaultInterpreterPath` : est le chemin vers l'interpéteur python.
* `python.condaPath` : est le chemin vers l'outils conda si vous utilisez la version anaconda de python.

> En jouant avec les paramètres *Users* et de *Workspace* vous pouvez avoir un interpréteur différent par projet si vous voulez.

Si vous avez suivi le [tutoriel anaconda]({% post_url tutos/python/2021-09-14-installation-anaconda %}) pour installer votre système python ces paramètres sont :

{% details sous linux %}

> TBD
{: .note}

{% enddetails %}

{% details sous mac %}

* `python.defaultInterpreterPath` : `/opt/anaconda3/bin/python3`
* `python.condaPath` : `/opt/anaconda3/bin/conda`

{% enddetails %}

{% details sous windows %}

* `python.defaultInterpreterPath` : `C:\programData\Anaconda3\python.exe`
* `python.condaPath` : `C:\programData\Anaconda3\Scripts\conda.exe`

{% enddetails %}

### triangle

Vous pouvez exécuter l'onglet courant en python en [cliquant sur le triangle en haut à droite de l'interface](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world).

### terminal

Vous pouvez utiliser [le terminal intégré]({% post_url tutos/editeur/vsc/2021-09-14-vsc-terminal %}#terminal-integre) pour exécuter vous programmes python comme vous le feriez avec un terminal externe.

## autres extensions et paramètres

### linter

Le [linting en python avec vscode](https://code.visualstudio.com/docs/python/linting) permet de souligner les fautes de style de python.

C'est une aide précieuse pour écrire du code qui est à la fois fonctionnel et lisible. Cela permet de supprimer la majorité des problèmes avant l'exécution.

Il faut installer des plugins pythons spécifiques pour le linting. Il en existe de nombreux. On vous propose ici d'utiliser [pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html) qui permet de respecter la [PEP8](https://www.python.org/dev/peps/pep-0008/).

#### pycodestyle : installation

Dans un [terminal]({% post_url tutos/systeme/2021-08-24-terminal %}), qui peut être [celui de vscode]({% post_url tutos/editeur/vsc/2021-09-14-vsc-terminal %}#terminal-integre) tapez la commande :

{% details sous linux et mac %}

```shell
pip3 install pycodestyle
```

{% enddetails %}

{% details sous windows %}

```shell
pip install pycodestyle
```

{% enddetails %}

Une fois ce module python installé, on va pouvoir l'utiliser dans vscode

#### pycodestyle : configuration

Pour mettre en route le linting via pycodestyle, deux paramètres sont à positionner :

* `python.linting.enabled` doit être coché pour mettre en route le linting
* `python.linting.pycodestyleEnabled` doit être coché pour utiliser `pycodestyle` comme linter
* `python.linting.pycodestylePath` doit donner le chemin vers `pycodestyle`. Il est par défaut positionné sur `pycodestyle` ce qui devrait être correct.

> Notez que vous pouvez aussi accéder à ces commande via la [palette de commande]({% post_url tutos/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main %}#palette-de-commande),par exemple avec la commande *python: enable/disable linting*.

#### pycodestyle dans le terminal@

Vous pouvez aussi toujours exécuter la commande `pycodestyle mon-fichier.py` dans un [terminal intégré]({% post_url tutos/editeur/vsc/2021-09-14-vsc-terminal %}#terminal-integre) pour obtenir le linting de votre fichier. C'est moins pratique que lorsque vscode le fait puisque la ligne en question n'est pas soulignée dans l'interface.

### black

[BLack](https://black.readthedocs.io/en/stable/index.html) est un bijou. Ne pas l'utiliser tout le temps est bête.

Son but est de re-formater sans faute de style tout programme python.

#### black : installation

Dans un [terminal]({% post_url tutos/systeme/2021-08-24-terminal %}), qui peut être [celui de vscode]({% post_url tutos/editeur/vsc/2021-09-14-vsc-terminal %}#terminal-integre) tapez la commande :

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

Une fois ce module python installé, on va pouvoir l'utiliser dans vscode

#### black : configuration

A priori tout est ok sans aucune autre configuration sous vscode. On peut lister deux paramètre auxquels faire attention :

* `python.formatting.blackPath`: qui vaut `black` par défaut
* `python.formatting.provider` : qui donne l'outil de formatage de fichier par défaut utilisé, et qui vaut `black` par défaut.

#### black : utilisation

Si vous avez le paramètre `editor.formatOnSave` de coché à chaque sauvegarde de votre fichier, il sera reformaté. Notez que cela ne marche pas si votre fichier est sauvegardé automatiquement après un délai.

Vous pouvez aussi exécuter la commande *format document* dans [palette de commande]({% post_url tutos/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main %}#palette-de-commande).

#### black : dans le terminal

{% details sous linux et mac %}

```shell
pip3 install black
```

{% enddetails %}

{% details sous windows %}

```shell
pip install black
```

{% enddetails %}

### coverage

> TBD
> <https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters>
> <https://github.com/ryanluker/vscode-coverage-gutters/tree/9e48acc88bb96e7d416c5e6529f507fc92b08f3a/example/python>
{: .note}

## tests

> TBD
>
> <https://code.visualstudio.com/docs/python/testing>
>
> * paramètres : `python.testing.pytestEnabled`
> * `pip3 install pytest` ou pip sous w10.
{: .note}

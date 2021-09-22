---
layout: page
title:  "vsc et python : outils supplémentaires"
categories: 
    - installation 
    - configuration
    - python
---

Configuration d'outils supplémentaires pour [visual studio code](https://code.visualstudio.com/) et le développement en python.

<!--more-->

Ce tutoriel fait suite au [tutoriel python et vscode]({% post_url tutos/editeur/vsc/2021-09-14-vsc-python %}). Il se consacre à l'installation d'extension non fondamentales mais bien sympathique pour le développement python. avec vscode.

## linter

Le [linting en python avec vscode](https://code.visualstudio.com/docs/python/linting) permet de souligner les fautes de style de python.

C'est une aide précieuse pour écrire du code qui est à la fois fonctionnel et lisible. Cela permet de supprimer la majorité des problèmes avant l'exécution.

Il faut installer des plugins pythons spécifiques pour le linting. Il en existe de nombreux. On vous propose ici d'utiliser [pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html) qui permet de respecter la [PEP8](https://www.python.org/dev/peps/pep-0008/).

### installation {#installation-pycodestyle}

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

### configuration {#configuration-pycodestyle}

Pour mettre en route le linting via pycodestyle, deux paramètres sont à positionner :

* `python.linting.enabled` doit être coché pour mettre en route le linting
* `python.linting.pycodestyleEnabled` doit être coché pour utiliser `pycodestyle` comme linter
* `python.linting.pycodestylePath` doit donner le chemin vers `pycodestyle`. Il est par défaut positionné sur `pycodestyle` ce qui devrait être correct.

> Notez que vous pouvez aussi accéder à ces commande via la [palette de commande]({% post_url tutos/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main %}#palette-de-commande),par exemple avec la commande *python: enable/disable linting*.

### pycodestyle dans le terminal

Vous pouvez aussi toujours exécuter la commande `pycodestyle mon-fichier.py` dans un [terminal intégré]({% post_url tutos/editeur/vsc/2021-09-14-vsc-terminal %}#terminal-integre) pour obtenir le linting de votre fichier. C'est moins pratique que lorsque vscode le fait puisque la ligne en question n'est pas soulignée dans l'interface.

## black

[BLack](https://black.readthedocs.io/en/stable/index.html) est un bijou. Ne pas l'utiliser tout le temps est bête.

Son but est de re-formater sans faute de style tout programme python.

### installation {#installation-black}

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

### configuration {#configuration-black}

A priori tout est ok sans aucune autre configuration sous vscode. On peut lister deux paramètre auxquels faire attention :

* `python.formatting.blackPath`: qui vaut `black` par défaut
* `python.formatting.provider` : qui donne l'outil de formatage de fichier par défaut utilisé, et qui vaut `black` par défaut.

### utilisation

Si vous avez le paramètre `editor.formatOnSave` de coché à chaque sauvegarde de votre fichier, il sera reformaté. Notez que cela ne marche pas si votre fichier est sauvegardé automatiquement après un délai.

Vous pouvez aussi exécuter la commande *format document* dans [palette de commande]({% post_url tutos/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main %}#palette-de-commande).

### black dans le terminal

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

## coverage

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

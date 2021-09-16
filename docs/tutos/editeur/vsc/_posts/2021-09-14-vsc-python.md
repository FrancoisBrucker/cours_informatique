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

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

## exécuter du python {#execution-python}

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

## premier programme

### projet vsc

Créez un dossier nommé *"cours-python"* sur votre ordinateur, et ouvrez le avec vscode (*menu Fichier > ouvrir...*). Une fois que vous avez dit que vous faisiez confiance au développeur de ce projet, fermez l'onglet *Welcome*. Vous pouvez même fermer l'explorer en cliquant sur l'icone en sur-brillance dans la barre d'activité de [l'interface vsc](https://code.visualstudio.com/docs/getstarted/userinterface).

Nous allons commencer par utiliser le [le terminal intégré]({% post_url tutos/editeur/vsc/2021-09-14-vsc-terminal %}#terminal-integre) de vscode pour exécuter nos premiers programmes python avant d'écrire nos programmes de plusieurs lignes.

### interpréteur python

Ouvrez un terminal dans vscode (le [terminal]({% post_url /tutos/systeme/2021-08-24-terminal %}) permet d'exéctuer des commandes de votre système) : *menu Affichage > Terminal*.

Vous pouvez ensuite taper `python` sous windows ou `python3` sous linux et mac pour rentrer dans l'interpréteur python :

![interpreteur]({{ "/assets/tutos/vsc-python/python-interpreteur.png" | relative_url }}){:style="margin: auto;display: block}

#### une première ligne de python

Dans l'interpréteur (à côté des `>>>`, qu'on appelle [invite de commande ou prompt](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande)), tapez :

```python
print("Bonjour monde !")
```

Puis appuyez sur la touche entrée. Vous devriez avoir quelque chose du genre à la sortie :

![hello world]({{ "/assets/tutos/vsc-python/python-hello-world-interpreteur.png" | relative_url }}){:style="margin: auto;display: block}

Ca a l'air d'avoir marché. La ligne de code a affiché à l'écran `Bonjour Monde`, puis l'invite de commande est revenue (une fois l'instruction exécutée, on attend la suivante).

#### quitter l'interpréteur

```python
`quit()`
```

### création d'un fichier

Créez un fichier *"programme.py"* (*menu Fichier > New File* puis sauvez le immédiatement *menu Fichier > Save*).

> Si vous n'avez pas encore configuré python, vscode va vous demander de configurer son [environnement python]({% post_url /tutos/systeme/2021-08-24-terminal %}).

Tapez dans le fichier ouvert  dans vscode :

```python
print("Bonjour monde !")
```

Vous pouvez alors l'exécuter :

* dans le terminal en tapant : `python programme.py` ou `python3 programme.py` selon le nom de votre interpréteur
* en cliquant sur [le triangle en haut à droite de la fenêtre vsc](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world)

Remarquez que lorsque vous exécutez votre programme via la seconde solution, cela crée un nouveau terminal qui s'appelle *Python*.

![hello world]({{ "/assets/tutos/vsc-python/python-interpreteur-execution-python.png" | relative_url }}){:style="margin: auto;display: block}

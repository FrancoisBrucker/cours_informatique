---
layout: page
title:  "vscode et python"
tags: 
    - installation 
    - configuration
    - python
    - vscode
---

Configuration de python avec vscode.

<!--more-->

> prérequis
>
> * [vscode]({% link _tutoriels/editeur/vsc/vsc-installation-et-prise-en-main.md %})
> * [python installation]({% link _tutoriels/python/installation-de-python.md %})
>
{.chemin}

configuration de  [visual studio code](https://code.visualstudio.com/) pour le développement en python.

<!--more-->

## extension python pour vscode

> La documentation officielle de vscode a [une partie consacrée à python](https://code.visualstudio.com/docs/languages/python).
{.chemin}

La principale extension à installer lorsque l'on fait du python est [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) développée par microsoft. Il est également recommandé d'installer [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) (utilitaire puissant d'aide au code).

Pour installer ces package :

> Rendez vous dans la [gestion des extensions de vscode]({% link _tutoriels/editeur/vsc/vsc-installation-et-prise-en-main.md %}#extensions), puis tapez *python* dans la barre de recherche. Assurez vous d'installer les package créés par microsoft.
{.a-faire}

## premier programme

Nous allons créer un premier fichier de code python pour permettre de finaliser l'installation des liens entre l'interpréteur python et vscode.

> Créez un dossier nommé *"cours-python"* sur votre ordinateur, et ouvrez le avec vscode (*menu Fichier > ouvrir le dossier...*).
{.a-faire}

Une fois que vous avez dit que vous faisiez confiance au développeur de ce projet, fermez l'onglet *Welcome*. Vous pouvez même fermer l'explorer en cliquant sur l'icône en sur-brillance dans la barre d'activité de [l'interface vsc](https://code.visualstudio.com/docs/getstarted/userinterface).

> Créez un fichier *"programme.py"* (*menu Fichier > nouveau fichier texte* puis sauvez le immédiatement *menu Fichier > Enregistrer*).
{.a-faire}

Si vous n'avez pas encore configuré python, vscode va vous demander le faire.

> Suivez les instructions de vscode (vous n'avez normalement pas grand chose à faire, vscode trouvera normalement les bons paramètres) pour faire le lien entre votre interpréteur python et lui.
{.a-faire}

Une fois la configuration terminée, écrivons notre code :

> Ecrivez dans le fichier ouvert dans vscode :
>
>```python
>print("Bonjour monde !")
>```
>
{.a-faire}

Vous pouvez alors l'exécuter :

> * en cliquant sur [le triangle en haut à droite de la fenêtre vsc](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world)
> * dans [le terminal intégré à vscode]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-terminal.md %}#terminal-integre) (*menu Affichage > Terminal*) en tapant : `python programme.py` (si vous êtes sous windows) ou `python3 programme.py` (si vous êtes sous unix ou mac).
{.a-faire}

Remarquez que lorsque vous exécutez votre programme via la première solution, cela crée un nouveau terminal qui s'appelle *Python* (le triangle vert est un raccourci pour appeler automatiquement un terminal) :

![hello world]({{ "/assets/tutos/vsc-python/python-interpreteur-execution-python.png" | relative_url }}){:style="margin: auto;display: block}

## paramètres

Le lien entre vscode et python se fait par l'intermédiaires de [paramètres](https://code.visualstudio.com/docs/getstarted/settings) :

{% details sous linux %}

*menu Fichier > préférences > paramètres*

{% enddetails %}

{% details sous mac %}

 *menu Code > préférences > paramètres*

{% enddetails %}

{% details sous windows %}

*menu Fichier > préférences > paramètres*

{% enddetails %}

Pour trouver les paramètres liés à python, une fois dans l'onglet paramètres, choisissez *extensions > python* dans le menu de gauche. Les préférences vscode consistent en des variables (*ID du paramètre*) à positionner selon ses envies, chaque variable modifiant un comportement de vscode.

> Il y a deux fois les mêmes préférences : **utilisateur** et  **espace de travail**. Le premier concerne les préférences générales de vscode et le second les préférences du projet courant. Par défaut, modifiez les préférences **utilisateur**. Pour plus d'informations, lisez la [doc](https://code.visualstudio.com/docs/getstarted/settings).

Il y a deux préférences qui sont liés à l'interpréteur python :

* **Default Interpreter Path** dont l'ID est `python.defaultInterpreterPath`. C'est le chemin vers l'interpéteur python.
* **Conda Path** dont l'ID est `python.condaPath`. C'est le chemin vers le programme `conda` si vous utilisez la version anaconda de python.

> Vous pouvez directement chercher le paramètre en tapant son nom dans la barre de recherche.

Si vous avez suivi le [tutoriel anaconda]({% link _tutoriels/python/installation-anaconda.md %}), vérifiez (ou faites en sorte) que les paramètres soient :

{% details sous linux %}

> trouver un linux pour savoir
{.tbd}

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
{.a-faire}

## exécuter du python {#execution-python}

Il y a deux façons principales d'exécuter du code python avec vscode. Chacune avec avantages et inconvénients. Il est donc recommandé de toutes les connaitre.

### triangle vert

On a déjà vu comment exécuter l'onglet courant en python en [cliquant sur le triangle en haut à droite de l'interface](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world).

### terminal

Vous pouvez utiliser [le terminal intégré]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-terminal.md %}#terminal-integre) pour exécuter vous programmes python comme vous le feriez avec un terminal externe.

> Ouvrez un [terminal dans vscode]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-terminal.md %}) : *menu Affichage > Terminal*.
{.a-faire}

Le [terminal]({% link _tutoriels/systeme/2021-08-24-terminal.md %}) permet d'exécuter des commandes de votre système.

> taper `python` sous windows ou `python3` sous linux et mac pour rentrer dans l'interpréteur python.
{.a-faire}

![interpreteur]({{ "/assets/tutos/vsc-python/python-interpreteur.png" | relative_url }}){:style="margin: auto;display: block"}

Dans l'interpréteur (à côté des `>>>`, qu'on appelle [invite de commande ou prompt](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande)) :

> tapez :
>
>```python
>print("Bonjour monde !")
>```
>
> Puis appuyez sur la touche entrée.
{.a-faire}

Vous devriez avoir quelque chose du genre à la sortie :

![hello world]({{ "/assets/tutos/vsc-python/python-hello-world-interpreteur.png" | relative_url }}){:style="margin: auto;display: block}

Ca a l'air d'avoir marché. La ligne de code a affiché à l'écran `Bonjour Monde`, puis l'invite de commande est revenue (une fois l'instruction exécutée, on attend la suivante).

Pour quitter l'interpréteur python :

> Tapez `quit()` puis appuyez sur la touche entrée.
{.a-faire}

## outils supplémentaires pour le développement

Il existe de nombreux plugins de vscode que l'on peut utiliser pour coder en python. Nous en montrerons deux ici, indispensables pour bien coder.

Vous pouvez consulter [ce tutoriel]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-python-modules-supplementaires.md %}) pour installer les plus utiles dans une optique de faire du développement python avec vscode.

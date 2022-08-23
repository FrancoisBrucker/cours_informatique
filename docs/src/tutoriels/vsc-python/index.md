---
layout: layout/post.njk 
title: Vsc et python
tags: ['tutoriel', 'vsc', 'python']

authors: 
    - François Brucker
---

{% chemin %}
[Tutoriels]({{ ".." }}) / [{{title}}]({{ "." }})
{% endchemin %}
{% prerequis "**Prérequis** :" %}

* [Installation et prise en main de vsc](../vsc-installation-et-prise-en-main)
* [Installation de python](../installation-python)

{% endprerequis %}

<!-- début résumé -->

configuration de  [visual studio code](https://code.visualstudio.com/) pour le développement en python.

<!-- fin résumé -->

## Extension python pour vscode

{% chemin "<https://code.visualstudio.com/docs/languages/python>" %}
La documentation officielle de vscode consacrée à python
{% endchemin %}

La principale extension à installer lorsque l'on fait du python est [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) développée par microsoft. Il est également recommandé d'installer [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) (utilitaire puissant d'aide au code).

Pour installer ces package :

{% faire %}
Rendez vous dans la [gestion des extensions de vscode](../vsc-installation-et-prise-en-main#extensions), puis tapez *python* dans la barre de recherche. Assurez vous d'installer les packages créés par microsoft.
{% endfaire %}

## Premier programme

Nous allons créer un premier fichier de code python pour permettre de finaliser l'installation des liens entre l'interpréteur python et vscode.

{% faire %}
Créez un dossier nommé `cours-python`{.fichier} sur votre ordinateur, et ouvrez le avec vscode (*menu Fichier > ouvrir le dossier...*).
{% endfaire %}

Une fois que vous avez dit que vous faisiez confiance au développeur de ce projet, fermez l'onglet *Welcome*. Vous pouvez même fermer l'explorer en cliquant sur l'icône en sur-brillance dans la barre d'activité de [l'interface vsc](https://code.visualstudio.com/docs/getstarted/userinterface).

{% faire %}
Créez un fichier *"programme.py"* (*menu Fichier > nouveau fichier texte* puis sauvez le immédiatement *menu Fichier > Enregistrer*).
{% endfaire %}

Si vous n'avez pas encore configuré python, vscode va vous demander le faire.

{% faire %}
Suivez les instructions de vscode (vous n'avez normalement pas grand chose à faire, vscode trouvera normalement les bons paramètres) pour faire le lien entre votre interpréteur python et lui.
{% endfaire %}

Une fois la configuration terminée, écrivons notre code :

{% faire "Écrivez dans le fichier ouvert dans vscode:" %}

```python
print("Bonjour monde !")
```

{% endfaire %}

Vous pouvez alors l'exécuter :

{% faire %}

* en cliquant sur [le triangle en haut à droite de la fenêtre vsc](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world)
* dans [le terminal intégré à vscode](../vsc-terminal#terminal-integre) (*menu Affichage > Terminal*) en tapant : `python programme.py` (si vous êtes sous windows) ou `python3 programme.py` (si vous êtes sous unix ou mac).
{% endfaire %}

Remarquez que lorsque vous exécutez votre programme via la première solution, cela crée un nouveau terminal qui s'appelle *Python* (le triangle vert est un raccourci pour appeler automatiquement un terminal) :

![hello world](python-interpreteur-execution-python.png)

## Paramètres

Le lien entre vscode et python se fait par l'intermédiaires de [paramètres](https://code.visualstudio.com/docs/getstarted/settings) :

{% details "sous mac" %}

Allez dans : *menu Code > préférences > paramètres*

{% enddetails %}
{% details "sous windows et linux" %}

Allez dans : *menu Fichier > préférences > paramètres*

{% enddetails %}

Pour trouver les paramètres liés à python, une fois dans l'onglet paramètres, choisissez *extensions > python* dans le menu de gauche. Les préférences vscode consistent en des variables (*ID du paramètre*) à positionner selon ses envies, chaque variable modifiant un comportement de vscode.

{% attention %}
Il y a deux fois les mêmes préférences : **utilisateur** et  **espace de travail**. Assurez vous de modifier les préférences **utilisateur**.
{% endattention %}

Il y a deux préférences qui sont liés à l'interpréteur python :

* **Default Interpreter Path** dont l'ID est `python.defaultInterpreterPath`. C'est le chemin vers l’interpréteur python.
* **Conda Path** dont l'ID est `python.condaPath`. C'est le chemin vers le programme `conda` si vous utilisez la version anaconda de python.

{% info %}
Vous pouvez directement chercher le paramètre en tapant son nom dans la barre de recherche.
{% endinfo %}

Si vous avez suivi le [tutoriel anaconda](../installation-anaconda), vérifiez (ou faites en sorte) que les paramètres soient :

{% details "sous mac" %}

* `python.defaultInterpreterPath` : `/opt/anaconda3/bin/python3`
* `python.condaPath` : `/opt/anaconda3/bin/conda`

{% enddetails %}

{% details "sous windows" %}

* `python.defaultInterpreterPath` : `C:\programData\Anaconda3\python.exe`
* `python.condaPath` : `C:\programData\Anaconda3\Scripts\conda.exe`

{% enddetails %}

{% faire %}
Faites en sorte que les paramètres python soient correct pour votre système.
{% endfaire %}

## Exécuter du python {#execution-python}

Il y a deux façons principales d'exécuter du code python avec vscode. Chacune avec avantages et inconvénients. Il est donc recommandé de toutes les connaître.

### Triangle vert

On a déjà vu comment exécuter l'onglet courant en python en [cliquant sur le triangle en haut à droite de l'interface](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world).

### terminal

Vous pouvez utiliser [le terminal intégré](../vsc-terminal#terminal-intégré) pour exécuter vous programmes python comme vous le feriez avec un terminal externe.

{% faire %}
Ouvrez un [terminal dans vscode](vsc-terminal) : *menu Affichage > Terminal*.
{% endfaire %}

{% faire %}
Taper `python` sous windows ou `python3` sous linux et mac pour rentrer dans l'interpréteur python.
{% endfaire %}

![interpreteur](python-interpreteur.png)

Dans l'interpréteur (à côté des `>>>`, qu'on appelle [invite de commande ou prompt](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande)) :

{% faire %}
Tapez :

```python
print("Bonjour monde !")
```

Puis appuyez sur la touche entrée.
{% endfaire %}

Vous devriez avoir quelque chose du genre à la sortie :

![hello world](python-hello-world-interpreteur.png)

Ca a l'air d'avoir marché. La ligne de code a affiché à l'écran `Bonjour Monde`, puis l'invite de commande est revenue (une fois l'instruction exécutée, on attend la suivante).

Pour quitter l'interpréteur python :

{% faire %}
Tapez `quit()` puis appuyez sur la touche entrée.
{% endfaire %}

## Outils supplémentaires pour le développement

Vous pouvez consulter [ce tutoriel](../vsc-python-modules-supplémentaires) pour installer les plus utiles dans une optique de faire du développement python avec vscode.

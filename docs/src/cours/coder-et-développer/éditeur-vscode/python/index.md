---
layout: layout/post.njk

title: Vsc et python

eleventyNavigation:
  prerequis:
      - '../../installer-python/'

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Configuration de  [visual studio code](https://code.visualstudio.com/) pour le développement en python.

<!-- fin résumé -->

## Extension python pour vscode

{% lien "**Documentation officielle de vscode consacrée à python**" %}
<https://code.visualstudio.com/docs/languages/python>
{% endlien %}

La principale extension à installer lorsque l'on fait du python est [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) développée par microsoft. Il est également recommandé d'installer [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) (utilitaire puissant d'aide au code).

Pour installer ces package :

{% faire %}
Rendez vous dans [la gestion des extensions de vscode](../prise-en-main#extensions){.interne}, puis tapez *python* dans la barre de recherche. Assurez vous d'installer les packages créés par microsoft.
{% endfaire %}

## Premier programme

Nous allons créer un premier fichier de code python pour permettre de finaliser l'installation des liens entre l'interpréteur python et vscode.

{% note %}
Avec vscode tout programme qu'on va coder **doit** dépendre d'un ***projet***. Ce projet est un **dossier** dans lequel seront placés nos fichiers.

Ceci est important car cela permet à vscode de lier les fichiers du projet entre eux (pour les tests par exemple) et nous aider.
{% endnote %}

{% faire %}
Créez un dossier nommé `hello-world-python`{.fichier} sur votre ordinateur, et ouvrez le avec vscode (*menu Fichier > ouvrir le dossier...*) pour le considérer comme un projet.
{% endfaire %}

Une fois que vous avez dit que vous faisiez confiance au développeur de ce projet, fermez l'onglet *Welcome*. Vous pouvez même fermer l'explorer en cliquant sur l'icône en sur-brillance dans la barre d'activité de [l'interface vsc](https://code.visualstudio.com/docs/getstarted/userinterface).

{% faire %}
Créez un fichier `main.py`{.fichier} (*menu Fichier > nouveau fichier texte* puis sauvez le immédiatement *menu Fichier > Enregistrer*).
{% endfaire %}

Si vous n'avez pas encore configuré python, vscode va vous demander le faire.

{% faire %}
Suivez les instructions de vscode (vous n'avez normalement pas grand chose à faire, vscode trouvera normalement les bons paramètres) pour faire le lien entre votre interpréteur python et lui.
{% endfaire %}

Une fois la configuration terminée, écrivons notre code :

{% faire "Écrivez dans le fichier ouvert dans vscode :" %}

```python
print("Bonjour monde !")
```

{% endfaire %}

### <span id="exécuter-programme"><span> Exécution du programme

1. assurez vous d'être dans l'onglet contenant le fichier `main.py`{.fichier} de vscode
2. cliquez sur le triangle en haut à droite de la fenêtre pour exécuter le programme.

Vous devriez obtenir quelque chose du genre :

![hello world](python-interpreteur-execution-python.png)

Pour exécuter du python, vscode écrit une *ligne de commande* dans le terminal. Dans l'exemple précédent, la ligne de code était :

```shell
/bin/python /home/fbrucker/Documents/code/hello-world-python/main.py
```

{% info %}
Ce qui est avant la ligne de code, c'est à dire `fbrucker@MV-ubuntu:~/Documents/code/hello-world-python$` dans l'exemple précédent est appelé le *prompt* et est ce que le terminal met au début de chaque ligne avant que l'on puisse taper des commandes.
{% endinfo %}

La ligne de commande d'un terminal est toujours composée de la même façon :

```shell
nom-du-programme paramètre-1-du-programme ... paramètre-n-du-programme 
```

Dans notre cas:

* nom du programme : `/bin/python` Qui est le chemin vers l'exécutable python
* un unique paramètre : `/home/fbrucker/Documents/code/hello-world-python/main.py` qui est le chemin vers le fichier à exécuter

{% info %}
Pour connaître le python utilisé, il suffit de cliquer en bas à droite de la fenêtre de vscode. On voit tout les pythons connus :

![quel python ?](./quel-python.png)

Celui utilisé est précédé d'une étoile.
{% endinfo %}

### <span id="quel-python"></span> Trouver le python utilisé par vscode

Pour accéder facilement à `nom-du-programme-python`. Cliquez sur le triangle vert pour exécuter le code. Dans le terminal, la ligne de code suivante est exécutée :

```
nom-du-programme-python fichier-exécuté
```

Une fois le programme exécuté, dans le terminal, tapez sur la flèche du haut pour rappeler la commande précédente. Il suffit ensuite de supprimer la fin de la commande (le nom du fichier à exécuter) pour ne garder que le programme python utilisé.

{% info %}
Pour connaître le chemin exact du programme appelé `python`, [utilisez la commande `which` du terminal](../../ordinateur-développement/terminal-utilisation#which){.interne}.
{% endinfo %}

### <span id="pip"></span> Installer des packages pour notre python

Il y a souvent beaucoup d'interpréteurs python d'installé sur un système et savoir lequel est utilisé peut être une gageure. Nous allons montrer ici comment utiliser l'interpréteur python choisi dns vscode.

Pour installer des modules pour notre python, il faut taper la commande :

```shell
python -m pip install nom-du-module-à-installer
```

Où :

* `python` est le python pour lequel on veut installer un package, c'est à dire la première partie de la ligne de commande écrite par vscode. Chez moi (sous mac avec brew), c'est : `/bin/python`{.fichier}. Chez vous c'est peut-être juste `python` (le plus probable), ou `python3``
* `nom-du-module-à-installer` est le nom de la bibliothèque à installer.

Cette ligne se comprend ainsi : pour mon python (`nom-du-programme-python`), je veux utiliser le module `pip` (`-m pip`) avec les paramètres `install nom-du-module-à-installer` (on veux installer un module)

Si je veux installer la bibliothèque `pytest` par exemple, ma ligne de commande (sous mac) à taper dans le terminal vscode sera :

```shell
python -m pip install pytest
```

Pour vous, ce sera peut-être différent car le `nom-du-programme-python` sera différent.

## Exécuter du python

Il y a deux façons principales d'exécuter du code python avec vscode. Chacune avec avantages et inconvénients. Il est donc recommandé de toutes les connaître.

### Via le triangle

On a déjà vu comment exécuter l'onglet courant en python en [cliquant sur le triangle en haut à droite de l'interface](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world).

### Via le terminal

Vous pouvez utiliser [le terminal intégré](../terminal#terminal-intégré){.interne} pour exécuter vous programmes python comme vous le feriez avec un terminal externe.

{% faire %}
Ouvrez un [terminal dans vscode](../terminal){.interne} : *menu Affichage > Terminal*.
{% endfaire %}

{% faire %}
Utilisez la [partie précédente](./#exécuter-programme){.interne} pour déterminer votre  `nom-du-programme-python`, puis exécutez le.
{% endfaire %}

![interpréteur](python-interpreteur.png)

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

l’intérêt d'utiliser le terminal est que l'on peut :

* utiliser la flèche du haut du clavier pour rappeler la commande précédente. Cela va plus vite que de se déplacer sur le triangle
* on peut exécuter le code sans être sur l'onglet du fichier à exécuter

## Paramètres

{% attention %}
Cette partie est optionnelle.

Elle n'est utile que si vous voulez changer le comportement par défaut de vscode et python.
{% endattention %}

Le lien entre vscode et python se fait par l'intermédiaires de [paramètres](https://code.visualstudio.com/docs/getstarted/settings) :

{% details "sous mac" %}

Allez dans : *menu Code > préférences > paramètres*

{% enddetails %}
{% details "sous windows et Linux" %}

Allez dans : *menu Fichier > préférences > paramètres*

{% enddetails %}

Pour trouver les paramètres liés à python, une fois dans l'onglet paramètres, choisissez *extensions > python* dans le menu de gauche. Les préférences vscode consistent en des variables (*ID du paramètre*) à positionner selon ses envies, chaque variable modifiant un comportement de vscode.

{% attention %}
Il y a deux fois les mêmes préférences : **utilisateur** et  **espace de travail**. Assurez vous de modifier les préférences **utilisateur**.
{% endattention %}

Il y a deux préférences qui sont liées à l'interpréteur python :

* **Default Interpreter Path** dont l'ID est `python.defaultInterpreterPath`. C'est le chemin vers l’interpréteur python.
* **Conda Path** dont l'ID est `python.condaPath`. C'est le chemin vers le programme `conda` si vous utilisez la version anaconda de python.

{% info %}
Vous pouvez directement chercher le paramètre en tapant son nom dans la barre de recherche.
{% endinfo %}

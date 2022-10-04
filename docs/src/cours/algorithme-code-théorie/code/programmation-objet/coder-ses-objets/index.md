---
layout: layout/post.njk 
title: Coder ses objets

eleventyNavigation:
  key: "Coder ses objets"
  parent: "Programmation Objet"
---

{% prerequis "**Prérequis** :" %}

* [classes et objets](../classes-et-objets)
* [vscode et python sont installés]({{ '/tutoriels/vsc-python' | url }})

{% endprerequis %}

<!-- début résumé -->

Exemple complet d'utilisation complet de vscode pour créer des objets en python.

<!-- end résumé -->

## Préparation

### Création du projet

On suit les directives du [projet hello-dev](../../projet-hello-dev) pour créer un nouveau projet :

1. on crée un dossier `coder-objets`{.fichier} dans un explorateur de fichier
2. on ouvre le dossier `coder-objets`{.fichier} avec vscode, ce qui crée notre projet
3. on crée un nouveau fichier `main.py`{.fichier} où l'on écrit `print("hello world !")`

### Exécution du projet

1. assurez vous d'être dans l'onglet contenant le fichier `main.py`{.fichier} de vscode
2. cliquez sur le triangle en haut à droite de la fenêtre pour exécuter le programme.

Vous devriez obtenir quelque chose du genre :

![exécution python](./exécution-python.png)

{% info %}
Pour connaître le python utilisé, il suffit de cliquer en bas à droite de la fenêtre de vscode. On voit tout les pythons connus :

![quel python ?](./quel-python.png)

Celui utilisé est précédé d'une étoile.
{% endinfo %}

Pour exécuter du python, vscode écrit une *ligne de commande* dans le terminal. Dans l'exemple précédent, la ligne de code était :

```shell
/usr/local/bin/python3 /Users/fbrucker/Documents/sous_git/cours_informatique/docs/src/cours/algorithme-code-théorie/code/programmation-objet/coder-ses-objets/coder-objets/main.py
```

{% info %}
Ce qui est avant la ligne de code, c'est à dire `fbrucker@macminibrucker coder-ses-objets/coder-objets ±main⚡ » ` dans l'exemple précédent est appelé le *prompt* et est ce que le terminal met au début de chaque ligne avant que l'on puisse taper des commandes.
{% endinfo %}

La ligne de commande d'un terminal est toujours composée de la même façon :

```shell
nom-du-programme paramètre-1-du-programme ... paramètre-n-du-programme 
```

Dans notre cas:

* nom du programme : `/usr/local/bin/python3` Qui est le chemin vers l'exécutable python
* un unique paramètre : `/Users/fbrucker/Documents/sous_git/cours_informatique/docs/src/cours/algorithme-code-théorie/code/programmation-objet/coder-ses-objets/coder-objets/main.py` qui est le chemin vers le fichier à exécuter

### Installer des packages pour notre python

Pour installer des modules pour notre python, il faut taper la commande :

```shell
nom-du-programme-python -m pip install nom-du-module-à-installer
```

Où :

* `nom-du-programme-python` est le python pour lequel on veut installer un package, c'est à dire la première partie de la ligne de commande écrite par vscode
* `nom-de-la-bibliothèque-à-installer` est le nom de la bibliothèque à installer.

Cette ligne se comprend ainsi : pour mon python (`nom-du-programme-python`), je veux utiliser le module `pip` (`-m pip`) avec les paramètres `install nom-du-module-à-installer` (on veux installer un module)

Si je veux installer la bibliothèque `pytest` par exemple, ma ligne de commande à taper dans le terminal vscode sera :

```shell
/usr/local/bin/python3 -m pip install pytest
```

Pour vous, ce sera différent car le `nom-du-programme-python` sera différent.

## Coder ses objets : le compteur

Nous allons reprendre l'exemple du cours [classes et objets](../classes-et-objets), avec le compteur. On sait que l'on veut arriver à la modélisation UML suivante :

![uml compteur](../../classes-et-objets/classes-2.png)

On va coder petit à petit la classe.

### Préparation

## Améliorer ses objets : le compteur avec paramètres


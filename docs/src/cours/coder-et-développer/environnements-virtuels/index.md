---
layout: layout/post.njk

title: Environnements virtuels

prerequis:
    - "../ordinateur-développement/fichiers-navigation/"
    - "../ordinateur-développement/terminal/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}

- <https://docs.python.org/fr/3.13/tutorial/venv.html#>
- [Virtual environments](https://realpython.com/python-virtual-environments-a-primer/)

{% endlien %}

Le but d'un environnement virtuel est de créer un environnement python complet (interpréteur et modules) différent par projet. Ceci permet de contrôler les modules installés et utilisés.

{% note %}
Il est fortement recommandé de créer un environnement virtuel pour **chaque** projet.
{% endnote %}

## Environnement python

[On a vu que l'interpréteur python était un fichier](../installer-python/#interpréteur-emplacement){.interne} sur notre ordinateur qui était exécuté pour interpréter du code, chacun pouvant avoir ses propres modules d'installés. L'ensemble python et module est appelé environnement python et est placé dans un dossier :

```python
import sys
print(sys.prefix)
```

Ce qui donne chez moi le dossier `/opt/homebrew/opt/python@3.13/Frameworks/Python.framework/Versions/3.13`{.fichier}. Ce dossier contient tout l'environnement python. En regardant cette arborescence avec la commande [tree](https://en.wikipedia.org/wiki/Tree_(command)), on voit qu'elle contient un grand nombre de dossiers et de fichiers :

```
❯ tree -L 2 /opt/homebrew/opt/python@3.13/Frameworks/Python.framework/Versions/3.13 
/opt/homebrew/opt/python@3.13/Frameworks/Python.framework/Versions/3.13
├── Headers -> include/python3.13
├── Python
├── Resources
│   ├── Info.plist
│   └── Python.app
├── _CodeSignature
│   └── CodeResources
├── bin
│   ├── idle3 -> idle3.13
│   ├── idle3.13
│   ├── pip3
│   ├── pip3.13
│   ├── pydoc3 -> pydoc3.13
│   ├── pydoc3.13
│   ├── python3 -> python3.13
│   ├── python3-config -> python3.13-config
│   ├── python3.13
│   └── python3.13-config
├── etc
│   └── jupyter
├── include
│   └── python3.13
├── lib
│   ├── libpython3.13.dylib -> ../Python
│   ├── pkgconfig
│   └── python3.13
└── share
    ├── doc
    └── jupyter

16 directories, 14 files

```

Chaque dossier a sa propre fonction, citons-en deux :

- `bin` contient les fichiers exécutables, dont `python`{.fichier} et `pip`{.fichier}
- `lib/python3.13`{.fichier} contient les modules. Baladez-vous y, vous y retrouverez de vieilles connaissances comme `random.py` par exemple

{% info %}
Vous n'y trouverez en revanche pas `math.py` et `sys.py` car ces deux modules sont spéciaux car très souvent utilisés : ils sont directement inclus dans l'interpréteur (bien qu'il faille tout de même les importer).

```python
import sys
for nom_module in sorted(sys.stdlib_module_names):
  print(nom_module)
```

{% endinfo %}

C'est toute cette architecture que l'on veut dupliquer dans chacun de nos projet.

## Création d'un environnement

Nous utiliserons le module [`venv`](https://docs.python.org/fr/3/library/venv.html).

{% details "installation sous Linux" %}
Le module venv n'est habituellement pas installé sous Linux/Ubuntu. Il faut l'installer en plus avec la commande :

```shell
sudo apt install python3-venv
```

{% enddetails %}

Le but de ce module est d'installer un environnement python vierge (sans aucun autre module que les modules essentiels) dans un dossier.

Par défaut, ce dossier s'appelle `.venv`{.fichier} (il est donc caché) et est placé à la racine de votre site.

### Avec vscode

{% lien %}
<https://code.visualstudio.com/docs/python/environments#_creating-environments>
{% endlien %}

> TBD `.venv` caché sous unix (sous windows on le voit). Je préfère utiliser `venv` comme ça on le voit et on sait ce que c'est.
> TBD certains mettent l'env dans un dossier de la maison `~/.env/`{.fichier} et réutilisent les env pour plusieurs projets. C'est une utilisation avancée que je déconseille pour commencer. Faites 1 python par projet avec un fichier requirement pour tout installer en bloc : c'est plus clair

### À la main

> TBD interpréteur + modules
> TBD voir où ils sont terminal + env pythons.

Pour connaître l'emplacement de ce fichier vous pouvez 

> TBD plusieurs pythons
> 
Ce programme n'est pas seul, il nécessite tout un tas d'autres programmes pour fonctionner (c'est pourquoi l'installation de python ne consiste pas juste à télécharger un unique fichier `python.exe`{.fichier} sous windows par exemple). En particulier tous ses modules

> TBD modules. Voir les fichiers où ils sont
> TBD voir le dossier

## Usage

{% lien %}
<https://docs.python.org/fr/3.13/library/venv.html>
{% endlien %}

> TBD venv

> TBD usage avec le nom

### Activation

> TBD terminal
> TBD usage avec vscode

### Modules

> TBD à la main, avec requirements.txt
> récupérer les packages installés dans un fichier pur le donner aux autres utilisant le projet.

## Gestion des environnements virtuels

> TBD où ranger ses environnements virtuels
> TBD dans son projet par défaut mais peut y avoir des exceptions.

### Poetry

> TBD

### Différentes versions de python

> TBD

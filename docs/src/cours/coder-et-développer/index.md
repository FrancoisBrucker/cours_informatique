---
layout: layout/post.njk

title: Coder et développer
tags: ["cours", "code", "python"]
authors:
  - François Brucker

resume: "Ce cours est dédié au code informatique. Comment l'écrire, le tester et l'exécuter."

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Ce cours est dédié au code informatique. On utilisera le language python comme support car c'est un langage très utilisé et qui permet de mettre en lumière tous les aspects du développement d'un code informatique. La très grande majorité des concepts que l'on verra seront cependant transposables dans d'autres langages (comme le javascript ou encore ruby par exemple).

On supposera que vous avez des connaissances scientifiques de base (ie. mathématiques de Lycée) et que vous disposer d'un ordinateur dont vous êtes administrateur.

Aucune compétences en informatique préalable n'est nécessaire.

<!-- fin résumé -->

## <span id="bases"></span>Bases

{% aller %}
[Bases de la programmation](bases-programmation){.interne}
{% endaller %}

### Tutoriel python

Une fois les bases acquises, terminez cette partie en faisant le tutoriel de python qui reprend tout ce que nous avons vu de façon plus détaillée :

{% lien %}
<https://docs.python.org/fr/3/tutorial/index.html>
{% endlien %}

### On s'entraîne

{% aller %}
[Petits projets de code](projet-codes){.interne}
{% endaller %}
{% aller %}
[100 mono-lignes](./mono-lignes){.interne}
{% endaller %}

## <span id="développer"></span>Gestion des données

Avant de pouvoir écrire des programmes conséquents il faut comprendre comment est organisé votre ordinateur et pouvoir minimalement interagir avec son système d'exploitation. Donc lisez la partie consacrée aux bases d'un système d'exploitation avant de continuer :

{% prerequis "**Connaissances système minimales**" %}

[Utiliser son système d'exploitation](/cours/système-et-réseau/bases-système){.interne}

{% endprerequis %}
{% info "**Etape optionnelle**"%}

L'installation d'un nouveau système est une étape optionnelle, mais si vous avez votre ordinateur depuis longtemps sans vraiment vous en occuper, ou que vous avez des erreurs étranges, il peut-être nécessaire de faire une nouvelle installation.

{% endinfo %}

### Installer des modules externes

Même si python vient avec de nombreux modules d'installés il arrive toujours un moment où l'on devra installer des modules développés par d'autres personnes :

{% aller %}
[Installer des modules](./modules-externes-python/){.interne}
{% endaller %}

#### Tutoriel matplotlib

Le module matplotlib est devenu un standard de fait (pour le meilleur et surtout le pire) pour représenter des graphiques.

{% aller %}
[Tutoriel Matplotlib](tutoriel-matplotlib){.interne}
{% endaller %}

Si vous avez le choix, je conseille plutôt d'utiliser [le module seaborn](https://seaborn.pydata.org/) pour dessiner vos graphique. Mais comme ce module est basé sur matplotlib, une connaissance minimale de matplotlib, comme le donne le tutoriel précédent est tout de même nécessaire.

#### Tutoriel numpy

{% aller %}
[Tutoriel Numpy](tutoriel-numpy){.interne}
{% endaller %}

### Stockage des données

#### En mémoire

{% aller %}
[Données en mémoire](données-mémoire){.interne}
{% endaller %}

#### Chaîne de caractères

{% aller %}
[Encodage Unicode](encodage-unicode){.interne}
{% endaller %}

#### Sur des fichiers

{% aller %}
[Fichiers](fichiers){.interne}
{% endaller %}

## Écrire du code

### Corriger son code

Le débogueur, qui permet d'exécuter ligne à ligne du code python est non seulement un excellent outil pour corriger son code, mais également un très bon outil d'apprentissage puisqu'il vous permettra d'assimiler plus rapidement ces notions de variables, d'objets et d'espaces de noms :

{% aller %}
[Déboguer son code](débogueur){.interne}
{% endaller %}

### Écrire du code maintenable

Il faut essayer de limiter au maximum la création de bug et, surtout, éviter qu'ils réapparaissent à la suite d'une modification de code.

Mais plutôt que de corriger il vaut mieux éviter que les bugs arrivent

{% aller %}
[Tester son code](tests-unitaires){.interne}
{% endaller %}

### Écrire du code lisible

{% aller %}
[Écrire et exécuter du code](écrire-code){.interne}
{% endaller %}

### On s'entraîne

#### Un projet complet

{% aller %}
[Projet pourcentage](projet-pourcentages){.interne}
{% endaller %}

#### Écrire des tests

{% aller %}
[On s’entraîne : écrire des tests](projet-codes-tests){.interne}
{% endaller %}

#### On vérifie qu'on sait faire

{% aller %}
[exercices](exercices-tests){.interne}
{% endaller %}

## Programmation objet

La programmation objet est un principe de programmation utilisé par la quasi-totalité des langages de programmation. Nes nuances existent bien sur, la programmation objet en rust n'est pas la même qu'en java par exemple, mais quelques principes fondateurs sont utilisés partout.

Nous allons dans cette partie du cours nous atteler à montrer ces principes et leur utilité dans le cadre du langage python.

{% aller %}
[Programmation objet](programmation-objet){.interne}
{% endaller %}

## Maintenir et développer du code sûr

### <span id="gestion-dépendances"></span>Gestion des dépendances

Lorsque l'on veut utiliser l'interpréteur python exécuter un programme informatique que l'on aura développé, il faut s'assurer que chaque exécution du programme soit identique.
Pour éviter les effets de bords (anciennes variables déclarées, modules importées, etc) Il est indispensable de pouvoir :

1. créer un nouvel interpréteur python pour **_chaque_** exécution du programme.
2. écrire notre programme en-dehors de tout interpréteur

{% aller %}
[Version de l'interpréteur python](version-python){.interne}
{% endaller %}

#### Dépendances de l'interpréteurs

Les dossiers où python va cherchez les modules sont listés dans la variable `sys.path` et dépendent de l'interpréteur utilisé :

{% attention %}
Il faut installer les modules en utilisant `python -m pip` et non directement le programme `pip`, car l'interpréteur pour lequel sera installé le module est ainsi explicite.
{% endattention %}

vous pouvez le voir en exécutant le code :

```python
import sys
for dossier in sys.path:
   print(dossier)
```

Chez moi, sur un mac où python est installé avec [brew](https://brew.sh/) ce programme rend :

```shell
/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python311.zip
/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11
/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload
/Users/fbrucker/Library/Python/3.11/lib/python/site-packages
/opt/homebrew/lib/python3.11/site-packages
/opt/homebrew/lib/python3.11/site-packages/gpg-1.22.0-py3.11-macosx-13-arm64.egg
/opt/homebrew/opt/python-tk@3.11/libexec
```

Il y a plusieurs dossiers :

- `/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11`{.fichier} contient les packages de bibliothèque standard (il contient par exemple un fichier _"random.py"_ qui contient le code du package `random`)
- `/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload`{.fichier} contient les packages python qui ne sont pas écrit en python mais en C
- `/opt/homebrew/lib/python3.11/site-packages`{.fichier} qui contient les packages qui seront installés par pip.

{% attention %}
La gestion des packages peut être compliquée. Normalement, si vous vous y prenez comme indiqué ici et en utilisant votre ordinateur personnel, tout devrait bien se passer. Si cela commence à ne plus aller, vous pouvez essayer d'installer les packages à un autre en endroit en suivant [ce tuto](https://opensource.com/article/19/4/managing-python-packages), ou, comme on le fera plus tard en utilisant un environnement virtuel. Mais, dans le doute, consultez un prof qui s'y connaît.
{% endattention %}

#### Un interpréteur par projet

{% aller %}
[Environnements virtuels](environnements-virtuels){.interne}
{% endaller %}

### Couverture de code

La couverture de code est un outils essentiel lorsque l'on programme par les tests et plus généralement lorsque l'on code tout court. Cet outil permet de vérifier les lignes de codes qui sont testées (_ie._ couvertes).

{% aller %}
[Couverture de code](couverture-de-code){.interne}
{% endaller %}

### Programmation par les tests

> TBD ajouter couverture du code.

On a pris l'habitude d'écrire des tests pour se rassurer quant à l'exactitude de nos fonctions. Mais pourquoi pas ne pas écrire les tests avant ? C'est le parti pris osé (mais très efficace) de la [programmation par les tests (_Test Driven Development_, ou _TDD_)](https://fr.wikipedia.org/wiki/Test_driven_development) que l'on vous propose d'essayer dans le projet ci-après.

{% aller %}
[Projet de programmation par les tests](projet-TDD){.interne}
{% endaller %}

### Packages

Lorsqu'un module devient important, il devient compliqué de mettre tout son code dans un seul fichier. On a alors coutume de rassembler tout le code du module dans un dossier que python appelle _package_. Ces packages pourront ensuite être réutilisés dans d'autres projets, voir être directement placés sur <https://pypi.org/> pour être utilisés par d'autres.

{% lien %}
[package en python](https://docs.python.org/fr/3/tutorial/modules.html#packages)
{% endlien %}

Comme l'import d'un module revient à exécuter un fichier et qu'importer un package revient à importer un dossier, python exécute le fichier `__init__.py`{.fichier} présent dans le dossier.

{% note %}
Un _package_ est un dossier contenant un fichier `__init__.py`{.fichier}.

- importer le dossier revient à exécuter le fichier `__init__.py`{.fichier}.

- exécuter le dossier avec l'interpréteur revient à exécuter le fichier `__main__.py`{.fichier}.

{% endnote %}

Enfin, on peut faire en sorte que nos modules/packages soient exécutables directement avec un interpréteur :

{% aller %}
[Exécuter des modules python](exécution-modules){.interne}
{% endaller %}

## Programmation évènementielle

> TBD mettre un environnement virtuel

La programmation évènementielle est un principe de développement très utilisé dans le développement de [GUI](https://fr.wikipedia.org/wiki/Interface_graphique). Le principe est de coder des _réactions_ qui seront exécutées lorsqu'un utilisateur effectuera une action spécifique (générant un _évènement_) comme cliquer sur quelque chose, appuyer sur une touche, etc.

{% aller %}
[Programmation évènementielle](programmation-évènementielle){.interne}
{% endaller %}

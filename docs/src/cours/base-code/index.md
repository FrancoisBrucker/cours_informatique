---
layout: layout/post.njk 
title: Bases en code et python

tags: ['cours', 'débutant', 'code', 'python']

authors:
    - François Brucker
    - Pierre Brucker

eleventyNavigation:
  key: "Bases en code et python"
  parent: Cours
---

<!-- début résumé -->

Nous montrerons dans ce cours les bases du codage en utilisant le langage de programmation [python](https://fr.wikipedia.org/wiki/Python_(langage)) dont le site est : <https://www.python.org/>

Nous verrons comment est structuré un langage informatique et comment écrire puis exécuter du code.

Ce n'est pas un cours d'informatique proprement dit, nous ne ferons quasiment pas d'algorithmie par exemple et il n'y a aucun prérequis informatique à avoir. Le but est de pouvoir exécuter (de la façon la plus optimale possible) des lignes de code pour obtenir un résultat concret (qui n'aura souvent rien à voir avec de l'informatique).

<!-- fin résumé -->

## Principes de python

*python* est un [langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation) inventé en 1991 par [Guido van Rossum](https://fr.wikipedia.org/wiki/Guido_van_Rossum). C'est comme une langue mais en beaucoup plus simple car :

* il n'y a pas d'exception
* il y a très peu de vocabulaire de base
* il est structuré en lignes et non en phrase

Son but est de faire faire des choses à un ordinateur.

On ne peut cependant pas directement donner un texte écrit en python (qu'on appelle ***code*** ou ***programme***) à un ordinateur pour qu'il l'exécute car celui-ci ne comprend que le [langage machine](https://fr.wikipedia.org/wiki/Langage_machine), on passe par un intermédiaire, un programme nommé ***interpréteur python***

### Interpréteur python

L'interpréteur python comme intermédiaire entre le code python et son exécution.

{% chemin %}
[Interpréteur](interpréteur)
{% endchemin %}

### Objets

Tout sur les objets courant que vous manipulerez en python.

{% chemin %}
[Objets types et types d'objets](objets-types)
{% endchemin %}

### Variables

Principe de l'affectation des variables en python.

{% chemin %}
[Variables](variables)
{% endchemin %}

### Conteneurs

En plus des 5 types de bases, python met à notre disposition plusieurs objets qui *contiennent* d'autres objets. Parmi ces conteneurs, la ***liste*** est la plus utilisée.

{% chemin %}
[Structure de liste](listes)
{% endchemin %}

### Opérations sur les objets

Créer de nouveaux objets avec d'autres objets.

{% chemin %}
[Opérations sur les objets](operations)
{% endchemin %}

### Fonctions et méthodes

Les fonctions et méthodes permettent d'utiliser les objets de python de façon pratique et puissante.

{% chemin %}
[Fonctions et Méthodes](fonctions-méthodes)
{% endchemin %}

## Code python

### Jupiter notebooks

Une manière plus conviviale que la console d'accéder à l'interpréteur python. L'utilisation des [Notebooks](https://jupyter.org/) est particulièrement adaptée pour rédiger et partager des comptes-rendus.

{% chemin %}
[Notebooks](notebooks)
{% endchemin %}

### Modules

les [modules python](https://docs.python.org/fr/3/tutorial/modules.html) permettent de se faciliter la vie dans l'écriture des programmes grâces aux méthodes qu'ils définissent.

{% chemin %}
[Modules](modules)
{% endchemin %}

Certains modules sont très utiles en python scientifique :

* [numpy](https://numpy.org/) : très utilisé pour ses structures de matrices et tableaux
* [matplotlib](https://matplotlib.org/) : pour créer des graphiques en python (allez voir ce [tutoriel]({{ "/tutoriels/matplotlib" | url }}) pour une introduction à matplotlib)
* [scipy](https://scipy.org/) : résolution d'équations différentielles
* [pillow](https://pillow.readthedocs.io/en/stable/) : gestion d'images
* [sklearn](https://scikit-learn.org/stable/) : machine learning

Ils ne viennent pas automatiquement lorsque l'on installe python, mais ils sont installés si vous utilisez <https://notebook.basthon.fr/#> ou encore <https://colab.research.google.com>.

{% info %}
Avec <https://colab.research.google.com> il est même possible d'[installer ses propres modules](https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb#scrollTo=kDn_lVxg3Z2G).
{% endinfo %}

### Blocs

Les blocs python permettent de grouper un ensemble de lignes de codes ensemble. On verra les blocs `while`{.language-}, `for`{.language-} et les blocs `if/elif/else`{.language-}.

{% chemin %}
[Blocs](blocs)
{% endchemin %}

### Créer ses propres fonctions

Si un bloc de code est exécuté plusieurs fois à l'identique, on aimerait aussi pouvoir nommer ce groupe pour **pouvoir le réutiliser juste en appelant son nom**. C'est possible avec les fonctions.

{% chemin %}
[Créer ses fonctions](creation-fonctions)
{% endchemin %}

## Notation `.`

On l'a vue pour les méthodes et les modules. De façon générale la notation `A.B` : se lit ainsi on cherche le nom `B` dans l'espace de nom `A`.

{% note %}
Une méthode n'est rien d'autre qu'un nom appelable dans l'espace de nom de l'objet à gauche du point
{% endnote %}

## Pour aller plus loin

### Installer python chez soit

Avoir une installation de python chez vous permet de plus facilement installer ses propre modules et de créer sereinement des programme plus important qu'avec des notebooks.

Cependant, ceci nécessite  quelques connaissances système et l'installation outils sur votre ordinateur.

#### Connaissances système minimale

Connaître les bases d'un système d'exploitation :
{% chemin %}
savoir [Naviguer dans un système de fichiers]({{ "/tutoriels/fichiers-navigation" | url }})
{% endchemin %}

Avoir accès à un terminal (aucune autre compétence en terminal n'est requise) :

{% chemin %}
[terminal]({{ "/tutoriels/terminal" | url }})
{% endchemin %}

#### Ordinateur pour le développement

Il n'est pas nécessaire d'avoir un ordinateur très performant pour faire du python. En revanche, il faut que votre ordinateur soit bien administré (ce qui n'est **pas** le cas si vous n'avez jamais pensé à le faire). De plus, vous devez dans l'idéal être administrateur de votre ordinateur et avoir fait

Pour garantir cela, le plus simple est de faire une installation fraîche de votre système. Rassurez vous :

1. ça ne prend pas beaucoup de temps (une 1/2 journée de devrait suffire)
2. vous allez gagner beaucoup de temps plus tard

{% chemin %}
[Nouvelle installation de son système]({{ "/tutoriels/installation-système" | url }})
{% endchemin %}

#### Installation de python

Vous pouvez consulter le [tutoriel d'installation de python]({{ "/tutoriels/installation-python" | url }}) pour voir plusieurs façons d'installer python, mais si vous ne savez pas trop quel python installer, nous vous conseillons d'installer une distribution générique comme celle d'[anaconda](https://www.anaconda.com/products/distribution) :

{% chemin %}
[Installation de la distribution anaconda de python]({{ "/tutoriels/installation-anaconda" | url }})
{% endchemin %}

La distribution d'anaconda vous permettra d'utiliser python ou via un notebook ou la console.

#### Installation d'un éditeur

Écrire et exécuter du python via un notebook est pratique lorsque l'on ne veut pas écrire de programme long ou que l'on utilise le code comme support à un rapport (le notebook fait alors office de rapport). De façon générale cependant, le code python est contenu dans un fichier de code écrit dans un éditeur. Nus vous conseillons [vscode](https://code.visualstudio.com/) qui est pratique et très utilisé.

{% chemin %}
[Installation et prise en main de vsc]({{ "/tutoriels/vsc-installation-et-prise-en-main" | url }})
{% endchemin %}

Une fois l'éditeur vscode et l'interpréteur python installés, on peut les configurer pour qu'ils puissent parler ensemble. Cette étape n'est pas indispensable mais elle permet de gagner du temps pour les développements futur et rend l'étape de développement bien plus agréable.

{% chemin %}
[Vsc et python]({{ "/tutoriels/vsc-python" | url }})
{% endchemin %}

### Tutoriel python

Vous pourrez terser votre installation en faisant le tutoriel python du site : <https://docs.python.org/fr/3/tutorial/index.html>

C'est un incontournable  pour qui veut faire du python.

### Installer et créer ses modules

Suivez le [tutorial des packages]({{ "/tutoriels/installation-python" | url }}#packages) dans le guide d'installation de python.

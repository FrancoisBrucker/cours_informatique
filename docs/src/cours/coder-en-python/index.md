---
layout: layout/post.njk

title: Coder en Python
tags: ['cours', 'code', 'python']
authors:
    - François Brucker
    - Pierre Brucker

eleventyNavigation:
  key: "Coder en Python"
  parent: Cours
---

<!-- début résumé -->

Nous montrerons dans ce cours les bases du codage en utilisant le langage de programmation [python](https://fr.wikipedia.org/wiki/Python_(langage)) dont le site est : <https://www.python.org/>

Nous verrons comment est structuré un langage informatique et comment écrire puis exécuter du code.

Ce n'est pas un cours d'informatique proprement dit, nous ne ferons quasiment pas d'algorithmie par exemple et il n'y a aucun prérequis informatique à avoir. Le but est de pouvoir exécuter (de la façon la plus optimale possible) des lignes de code pour obtenir un résultat concret (qui n'aura souvent rien à voir avec de l'informatique).

<!-- fin résumé -->

## Principes de Python

*Python* est un [langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation) inventé en 1991 par [Guido van Rossum](https://fr.wikipedia.org/wiki/Guido_van_Rossum). C'est comme une langue mais en beaucoup plus simple car :

* il n'y a pas d'exception
* il y a très peu de vocabulaire de base
* il est structuré en lignes et non en phrase

Son but est de faire faire des choses à un ordinateur.

On ne peut cependant pas directement donner un texte écrit en python (qu'on appelle ***code*** ou ***programme***) à un ordinateur pour qu'il l'exécute car celui-ci ne comprend que le [langage machine](https://fr.wikipedia.org/wiki/Langage_machine), on passe par un intermédiaire, un programme nommé ***interpréteur python***

### Interpréteur python

L'interpréteur python comme intermédiaire entre le code python et son exécution.

{% aller %}
[Cours sur l'interpréteur](interpréteur)
{% endaller %}

### Commentaires

Commençons par ne **pas** écrire du python. Dans une ligne de code python, tout ce qui suit un `#`{.language-} n'est pas lu.

Par exemple, le code suivant écrit dans une console ne produit pas d'erreur (il n'est même pas lu...) :

```python
>>> # coucou python !
```

Alors que le même code sans `#` est interprété par python et comme ce n'est pas du python cela produit une erreur :

```python
>>> coucou python !
  File "<stdin>", line 1
    coucou python !
           ^
SyntaxError: invalid syntax
```

### Objets

Tout sur les objets courant que vous manipulerez en python.

{% aller %}
[Cours sur les objets types et les types d'objets](objets-types)
{% endaller %}

### Variables

Principe de l'affectation des variables en python.

{% aller %}
[Cours sur les variables](variables)
{% endaller %}

### Opérations sur les objets

Créer de nouveaux objets avec d'autres objets.

{% aller %}
[Cours sur les opérations sur les objets](opérations)
{% endaller %}

### Fonctions et méthodes

Les fonctions et méthodes permettent d'utiliser les objets de python de façon pratique et puissante.

{% aller %}
[Cours sur les fonctions et les méthodes](fonctions-méthodes)
{% endaller %}

### Notebooks

C'est une manière plus conviviale que la console d'accéder à l'interpréteur python. L'utilisation des [Notebooks](https://jupyter.org/) est particulièrement adaptée pour rédiger et partager des comptes-rendus.

{% aller %}
[Cours sur les notebooks](notebooks)
{% endaller %}

### Spyder

{% lien %}
<https://www.spyder-ide.org/>
{% endlien %}

Spyder est un éditeur lié à un interpréteur python. L'application est très utilisée lorsque l'on commence à apprendre la programmation. Et permet d'écrire des programmes tout en conservant un unique interpréteur accessible par une console.

{% info %}
Si vous voulez faire sérieusement de l'informatique ou que vous voulez installer des modules python spécifiques, je vous conseille fortement d'installer votre propre interpréteur et votre propre éditeur (voir [ci-après](./#pour-aller-plus-loin)).
{% endinfo %}

> TBD : un petit tuto.

## Blocs

Pour l'instant nous avons envoyé chaque ligne de python que nous avons écrite directement à l'interpréteur pour être exécuté. Les *blocs* de python permettent de grouper un ensemble de lignes de code pour être exécutés sous certaines conditions.

{% aller %}
[Cours sur les blocs](blocs)
{% endaller %}

## <span id="conteneurs"></span> Conteneurs

En plus des 6 types de bases, python met à notre disposition plusieurs objets qui peuvent *contenir* d'autres objets.

Un conteneur est un objet itérable et possède l'opérateur `in`{.language-} (comme on l'a déjà vu avec les [chaînes de caractères](./opérations#chaines-in)). On pourra ainsi toujours utiliser `x in C`{.language-} pour savoir si l'objet `x`{.language-} est dans le conteneur `C`{.language-}.

### Listes

Parmi ces conteneurs, la ***liste*** est certainement la plus utilisée.

{% aller %}
[Cours sur la structure de liste](listes)
{% endaller %}

### Ensembles et dictionnaires

Les deux autres conteneurs à connaître sont les ***ensembles*** et les ***dictionnaires***. Ces deux structures sont très utiles lorsque l'on manipule des données mais sont plus complexes à manipuler que des listes. Prenez le temps d'apprendre à utiliser leurs nombreux avantages.

{% aller %}
[Cours sur les ensembles et les dictionnaires](ensembles-dictionnaires)
{% endaller %}

## Mutable vs non-mutable

Les 5 type d'objets de base (`int`{.language-}, `float`{.language-}, `complex`{.language-}, `bool`{.language-} et `str`{.language-}) sont **non modifiables** (python dira ***non mutables***). Ceci signifie que les méthodes et opérations sur ces objets ne peuvent les modifier :

* si `i`{.language-} contient un entier, `i = i + 1`{.language-} créera un nouvel entier qui sera associé à la variable `i`
* `"coucou".replace{"c", "b"}`{.language-} créera une nouvelle chaîne de caractères

Les liste, ensembles et dictionnaires sont eux **modifiables** (python dira ***mutables***), c'est à dire que leurs méthodes peuvent les modifier :

* `l.append("x")`{.language-} modifiera la liste `l`{.language-}
* `d["un"] = 1`{.language-} modifiera le dictionnaire `d`{.language-} en lui ajoutant une clé
* `e.add("un")`{.language-} modifiera l'ensemble `e`{.language-} en lui ajoutant un élément

Il est **crucial** de comprendre cela car les variables ne sont que des associations à des objets, et plusieurs variables différentes peuvent être associée à un même objet. Vérifions cela avec la fonction [`id`{.language-}](https://docs.python.org/fr/3/library/functions.html#id).

Si on crée deux listes, elles seront différentes, donc leur `id`{.language-} le sera aussi, même si leur contenu est identique :

```python
>>> x = [1, 2]
>>> y = [1, 2]
>>> id(x)
4381752640
>>> id(y)
4381751744
```

L'id sera certainement différent chez vous, mais les deux `id`{.language-} seront différents.

En revanche, associer une liste à une variable ne change pas la liste :

```python
>>> x = [1, 2]
>>> id(x)
4381803264
>>> y = x
>>> id(y)
4381803264
```

L'id sera certainement différent chez vous, mais il sera identique. Les variables `x`{.language-} et `y`{.language-} sont associées à la **même** liste :

```python
>>> x.append('?')
>>> print(x)
[1, 2, '?']
>>> print(y)
[1, 2, '?']
```

En conclusion, il faut faire **très attention** lorsque l'on passe des listes en paramètres de fonction.

{% info %}
Si vous jouez avec la fonction `id`{.language-} vous serez certainement surpris de constater que :

```python
>>> x = 1
>>> y = 1
>>> id(x)
4378755312
>>> id(y)
4378755312
```

Ceci est une optimisation de l'interpréteur python. Comme les entiers sont non modifiables, on peut associer le même entier à plusieurs variables sans soucis.
{% endinfo %}

La remarque précédente montre tout l'intérêt d'utiliser des objets non mutables. Il 'y aura jamais d'effet de bords lors de passage de paramètres. En revanche, à chaque modification, il faudra recréer un objet, ce qui peut être long. C'est un compromis à avoir : la sécurité vs la rapidité. C'est pourquoi par défaut :

* une chaîne de caractère est non modifiables (elles sont souvent crées une fois pour toute dans un programme)
* une liste est modifiable. L'utilisation des listes dans un programme nécessite souvent de la modifier.

Il existe des objets non modifiable pouvant être utilisé à la place des listes et des ensembles :

* un [`tuple`{.language-}](https://docs.python.org/fr/3/tutorial/datastructures.html#tuples-and-sequences) pour une liste. Elle se crée en remplaçant les `[]` d'une liste par des `()` : `(1, 2, 3)` crée un tuple à 3 éléments. Il pourra être utilisé comme une liste mais on ne pourra jamais lui ajouter ou modifier ses éléments.
* un [`frozenset`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#frozenset) sera le pendant non mutable d'un ensemble. On place les éléments directement à la création et ils ne peuvent plus être modifiés ensuite.

On peut alors utiliser des tuples et des frozenset comme éléments d'un ensemble ou comme clé de dictionnaires.

Par exemple l'ensemble de tous les sous-ensemble de ${1, 2}$ s'écrira :

```python
>>> x = {frozenset(), frozenset([1]), frozenset([2]), frozenset([1, 2])} 
>>> x
{frozenset(), frozenset({2}), frozenset({1}), frozenset({1, 2})}
```

{% info %}
Le tuple vide s'écrira `(,)`{.language-} (ou `tuple()`) pour la différentier la notation `()` qui est la parenthèse vide.
{% endinfo %}

## Modules

les [modules python](https://docs.python.org/fr/3/tutorial/modules.html) permettent de se faciliter la vie dans l'écriture des programmes grâces aux méthodes qu'ils définissent.

{% aller %}
[Cours sur les modules](modules)
{% endaller %}

Certains modules sont très utiles en python scientifique :

* [numpy](https://numpy.org/) : très utilisé pour ses structures de matrices et tableaux
* [matplotlib](https://matplotlib.org/) : pour créer des graphiques en python (allez voir ce [tutoriel]({{ "/tutoriels/matplotlib"  }}) pour une introduction à matplotlib)
* [scipy](https://scipy.org/) : résolution d'équations différentielles
* [pillow](https://pillow.readthedocs.io/en/stable/) : gestion d'images
* [sklearn](https://scikit-learn.org/stable/) : machine learning

Ils ne viennent pas automatiquement lorsque l'on installe python, mais ils sont installés si vous utilisez <https://notebook.basthon.fr/#> ou encore <https://colab.research.google.com>.

{% info %}
Avec <https://colab.research.google.com> il est même possible d'[installer ses propres modules](https://colab.research.google.com/notebooks-analyse/snippets/importing_libraries.ipynb#scrollTo=kDn_lVxg3Z2G).
{% endinfo %}

### Notation `.`

On l'a vue pour les méthodes et les modules. De façon générale la notation `A.B` : se lit ainsi on cherche le nom `B` dans l'espace de nom `A`.

{% note %}
Une méthode n'est rien d'autre qu'un nom appelable dans l'espace de nom de l'objet à gauche du point
{% endnote %}

## Créer ses propres fonctions

Si un bloc de code est exécuté plusieurs fois à l'identique, on aimerait aussi pouvoir nommer ce groupe pour **pouvoir le réutiliser juste en appelant son nom**. C'est possible avec les fonctions.

{% aller %}
[Comment créer ses fonctions](creation-fonctions)
{% endaller %}

## <span id="pour-aller-plus-loin"></span> Pour aller plus loin

### Installer python chez soit

Avoir une installation de python chez vous permet de plus facilement installer ses propre modules et de créer sereinement des programme plus important qu'avec des notebooks.

Cependant, ceci nécessite  quelques connaissances système et l'installation outils sur votre ordinateur.

#### Connaissances système minimale

Connaître les bases d'un système d'exploitation :
{% aller %}
Savoir [Naviguer dans un système de fichiers]({{ "/tutoriels/fichiers-navigation"  }})
{% endaller %}

Avoir accès à un terminal (aucune autre compétence en terminal n'est requise) :

{% aller %}
[Utiliser le terminal]({{ "/tutoriels/terminal"  }})
{% endaller %}

#### Ordinateur pour le développement

Il n'est pas nécessaire d'avoir un ordinateur très performant pour faire du python. En revanche, il faut que votre ordinateur soit bien administré (ce qui n'est **pas** le cas si vous n'avez jamais pensé à le faire). De plus, vous devez dans l'idéal être administrateur de votre ordinateur et avoir fait

Pour garantir cela, le plus simple est de faire une installation fraîche de votre système. Rassurez vous :

1. ça ne prend pas beaucoup de temps (une 1/2 journée de devrait suffire)
2. vous allez gagner beaucoup de temps plus tard

{% aller %}
[Faire une nouvelle installation de son système]({{ "/tutoriels/installation-système"  }})
{% endaller %}

#### Installation de python

Il y a plusieurs façons d'installer python, mais si vous ne savez pas trop quel python installer, il y a essentiellement trois choix, dans l'ordre :

1. vous voulez programmer avec python en utilisant un éditeur de texte : téléchargez python via le [Microsoft store](https://learn.microsoft.com/fr-fr/windows/python/beginners) (sous unix et mac python est déjà installé)
2. vous voulez utiliser python avec l'aide de notebooks : installez la distribution d'[anaconda]({{ "/tutoriels/installation-anaconda"  }})
3. avoir un environnement tout intégré et configurer pour un usage d'apprentissage (attention, cela va vous donner de mauvaises habitudes), vous pouvez [spyder](https://www.spyder-ide.org/)

Pour plus d'information, vous pouvez consulter le  tutoriel d'installation de python :

{% aller %}
[Comment installer python sur son ordinateur]({{ "/tutoriels/installation-python"  }})
{% endaller %}

#### Installation d'un éditeur

Écrire et exécuter du python via un notebook est pratique lorsque l'on ne veut pas écrire de programme long ou que l'on utilise le code comme support à un rapport (le notebook fait alors office de rapport). De façon générale cependant, le code python est contenu dans un fichier de code écrit dans un éditeur. Nus vous conseillons [vscode](https://code.visualstudio.com/) qui est pratique et très utilisé.

{% aller %}
[Comment Installer et prendre en main Vsc]({{ "/tutoriels/vsc-installation-et-prise-en-main"  }})
{% endaller %}

Une fois l'éditeur vscode et l'interpréteur python installés, on peut les configurer pour qu'ils puissent parler ensemble. Cette étape n'est pas indispensable mais elle permet de gagner du temps pour les développements futur et rend l'étape de développement bien plus agréable.

{% aller %}
[Comment utiliser Vsc et Python]({{ "/tutoriels/vsc-python"  }})
{% endaller %}

### Tutoriel python

Vous pourrez terser votre installation en faisant le tutoriel python du site : <https://docs.python.org/fr/3/tutorial/index.html>

C'est un incontournable  pour qui veut faire du python.

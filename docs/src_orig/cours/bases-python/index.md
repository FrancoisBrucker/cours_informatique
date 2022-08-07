---
layout: page
title:  "Bases de python"
authors: 
    - François Brucker
    - Pierre Brucker
---

> [bases de python]({% link cours/bases-python/index.md %})
{.chemin}

Un court cours sur les bases de la programmation en utilisant le langage de programmation [python](https://fr.wikipedia.org/wiki/Python_(langage)) dont le site est : <https://www.python.org/>

Nous verrons dans ce cours comment est structuré un langage informatique et comment écrire puis exécuter du code. Ce n'est pas un cours d'informatique proprement dit, nous ne ferons quasiment pas d'algorithmie par exemple : le but est de pouvoir exécuter (de la façon la pus optimale possible) des lignes de code pour obtenir un résultat concret (qui n'aura souvent rien à voir avec de l'informatique).

## Prérequis

Les connaissances et les outils que vous devez avoir pour commencer le cours.

### Un ordinateur pour le développement

Pour développer, il faudra coder et exécuter du code. Il vous faut donc un ordinateur (portable ou tour) en état de marche. Il devra être sous un des trois systèmes d'exploitation suivant windows, macos ou linux.

Vous devez dans l'idéal être administrateur de votre ordinateur et avoir fait [une installation fraîche de tout votre système]({% link _tutoriels/systeme/2021-09-01-installation-ordinateur.md %}) pour éviter toutes interférences lors de nos installations.

### Connaissances système minimale

* connaître les bases d'un système d'exploitation, [les fichiers et les dossiers]({% link _tutoriels/systeme/fichiers-navigation.md %})
* avoir accès à un [terminal]({% link _tutoriels/systeme/2021-08-24-terminal.md %}) (aucune autre copmpétence en terminal n'est requise)

## Installations

Nous allons avoir besoin de deux programmes essentiels pour ce cours :

* un programme nous permettant d'exécuter du code python
* un programme nous permettant d'écrire du code python

### Exécuter du python

Il y a plusieurs moyens d'exécuter du code python, selon les usages voulus. Nous allons en utiliser deux :

* exécution de *cellules de code* via un notebook
* exécution de *fichiers de code* en ligne de commande

#### Python sur internet

La solution la plus simple si vous voulez juste tester python ou si vous ne voulez pas utiliser des modules spécifiques de python qui nécessiteraient une installation c'est d'utiliser python directement sur internet. Deux solutions principales s'offrent à vous :

* <https://basthon.fr/> (utilisée dans les collèges et lycées français. L'installation de modules spécifiques est cependant impossible).
* <https://colab.research.google.com/?hl=fr> (utilisé de façon professionnelle, mais nécessite un compte google pour être utilisé)

Les deux solutions ci-dessus vous permettent d'exécuter du code python sous la forme de notebook.

#### Installer une distribution python sur son ordinateur

Vous pouvez consulter le [tutoriel d'installation de python]({% link _tutoriels/python/installation-de-python.md %}) pour voir plusieurs façons d'installer python, mais si vous ne savez pas trop quel python installer, nous vous conseillons d'installer une distribution générique comme celle d'[anaconda](https://www.anaconda.com/products/distribution) :

> Suivez [ce tutoriel]({% link _tutoriels/python/installation-anaconda.md %}) pour installer la distribution Anaconda.
{.a-faire}

La distribution d'anaconda vous permettra d'utiliser python ou via un notebook ou en ligne de commande.

#### Installer uniquement l'interpréteur python

Si vous préférez installer uniquement l'interpréteur python — ce qui est recommandé si vous voulez faire du développement et controller précisément ce qui est installé — vous pouvez suivre [ce tutoriel]({% link _tutoriels/python/installation-de-python.md %}#gestionnaire-package-id). Mais ceci dépasse le cadre de ce cours introductif à la programmation.

### Écrire

Écrire et exécuter du python via un notebook est pratique lorsque l'on ne veut pas écrire de programme long ou que l'on utilise le code comme support à un rapport (le notebook fait alors office de rapport). De façon générale cependant, le code python est contenu dans un fichier de code écrit dans un éditeur. Nus vous conseillons [vscode](https://code.visualstudio.com/) qui est pratique et très utilisé.

> En suivant [ce tutoriel]({% link _tutoriels/editeur/vsc/vsc-installation-et-prise-en-main.md %}) installez vscode sur votre ordinateur.
{.a-faire}

### Configuration

Une fois l'éditeur vscode et l'interpréteur python installés, on peut les configurer pour qu'ils puissent parler ensemble. Cette étape n'est pas indispensable mais elle permet de gagner du temps pour les développements futur et rend l'étape de développement bien plus agréable.

> Suivez [ce tutoriel]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-python.md %}) pour lier vscode à python.
{.a-faire}

## Interpréteur python

L'installation des plugins vscode pour python vous a fait écrire et exécuter votre 1er programme python. Tout code python est exécuté par un programme nommé **interpréteur python**. Tout code python (un fichier ou une cellule) est exécuté de la même manière :

1. on entre une ligne de code dans l'interpréteur
2. l'interpréteur exécute cette ligne
3. une fois la ligne exécutée, l'interpréteur redonne la main à l'utilisateur
4. retour à l'étape 1.

Tant que l'interpréteur est actif (c'est à dire tant que le notebook est ouvert ou tant que le fichier de code n'est pas entièrement lu) un mécanisme de stockage permet de conserver des **objets** pour une utilisation future via des **variables**.

L'interpréteur python est toujours présent lorsque l'on exécute du python, quelque soit la forme utilisée :

* via un [IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement) comme vscode et son *triangle vert*
* via la console et le programme python
* en utilisant un notebook

La façon la plus explicite d'utiliser l'interpréteur python est de le faire en console où l'on tape chaque ligne avant de l'exécuter.

> Utilisez <https://basthon.fr/> en console pour exécuter l'instruction `print("Bonjour monde !")`.
>
> Cette instruction affiche la chaîne de caractère *Bonjour monde !* à l'écran.
{.a-faire}

![hello world](./assets/console-1.png){:style="margin: auto;display: block}

Nous allons utiliser la console et l'accès direct à l'interpréteur pour comprendre les principes de bases de python, à savoir les objets et les variables.

## commentaires

Commençons par ne **pas** écrire du python. Dans une ligne de code python, tout ce qui suit un `#` n'est pas lu.

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

## objets et variables en python

1. La partie [objets types et types d'objets]({% link cours/bases-python/objets-types.md %}) vous dira tout sur les objets courant que vous manipulerez en python.
2. La partie [variables]({% link cours/bases-python/variables.md %}) vous montrera le principe de l'affectation des variables en python.
3. conteneurs d'objets. En plus des 5 types de bases, python met à notre disposition plusieurs objets qui *contiennent* d'autres objets. Parmi ces conteneurs, la [structure de liste]({% link cours/bases-python/listes.md %}) est la plus utilisée.

## opérations sur les objets

On peut facilement faire des [opérations sur les objets]({% link cours/bases-python/operations.md %}).

## fonctions et méthodes

Les [fonctions et méthodes]({% link cours/bases-python/fonctions-methodes.md %}) permettent d'utiliser les objets de python de façon pratique et puissante.

## modules

les [modules python]({% link cours/bases-python/modules.md %}) permettent de se faciliter la vie dans l'écriture des programmes grâces aux méthodes qu'ils définissent.

Si vous n'avez pas installé de distribution (par exemple anaconda) pour python, il vous sera sûrement nécessaire d'installer à la main certains modules pythons très utiles en python scientifique :

* [numpy](https://numpy.org/)
* [matplotlib](https://matplotlib.org/)
* [scipy](https://scipy.org/)
* [pillow](https://pillow.readthedocs.io/en/stable/)
* [sklearn](https://scikit-learn.org/stable/)

Si vous voulez apprendre les bases de la bibliothèque de dessin [matplotlib](https://matplotlib.org), vous pouvez suivre cette [courte introduction à matplotlib]({% link cours/bases-python/module-matplotlib.md %}).

## blocs de code

Si python ne pouvait qu'exécuter ligne à ligne un code on ne pourrait pas faire grand chose. Le principe des programmes est de pouvoir grouper les instructions en bloc.

En python, un bloc est toujours défini de la même manière  :

* Ce qui va identifier le bloc pour son exécution (une condition, son nombre d'exécution, son nom) et se finit par un `:`
* Les instructions le constituant.

Pour séparer les blocs les un des autres, et savoir ce qui le définit, le langage Python utilise l'indentation (4 espaces par défaut): un bloc est donc une suite d'instructions ayant la même indentation.

```text
type de bloc:
    instruction 1
    instruction 2
    ...
    instruction n
```

Ces différents blocs sont pratiques car ils vont nous permettre :

* d'**exécuter un certain nombre de fois un bloc donné** grâce aux [boucles]({% link cours/bases-python/boucles.md %}).
* d'**exécuter si une condition est vraie** grâce aux [conditions]({% link cours/bases-python/conditions.md %})

## créer ses propres fonctions

Si un bloc de code est exécuté plusieurs fois à l'identique, on aimerait aussi pouvoir nommer ce groupe pour **pouvoir le réutiliser juste en appelant son nom**, ce sont les [fonctions]({% link cours/bases-python/creation-fonctions.md %})

## notation `.`

On l'a vue pour les méthodes et les modules. De façon générale la notation `A.B` : se lit ainsi on cherche le nom `B` dans l'espace de nom `A`.

> une méthode n'est rien d'autre qu'un nom appelable dans l'espace de nom de l'objet à gauche du point

## tutoriel python

Incontournable pour qui veut faire du python, il est plus que recommandé que vous suiviez le tutoriel python du site : <https://docs.python.org/fr/3/tutorial/index.html>

## pour aller plus loin

>
> * mutable et non mutable
> * itérateurs ?
> * dictionnaires
> * lambda
> * list comprehension
>
{.tbd}
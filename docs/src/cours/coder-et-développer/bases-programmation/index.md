---
layout: layout/post.njk

title: Bases de programmation et du langage python
authors:
  - François Brucker
  - Pierre Brucker

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous montrerons dans ce cours les bases du codage en utilisant le langage de programmation [python](<https://fr.wikipedia.org/wiki/Python_(langage)>) dont le site est : <https://www.python.org/>

Nous verrons comment est structuré un langage informatique et comment écrire puis exécuter du code.

Ce n'est pas un cours d'informatique proprement dit, nous ne ferons quasiment pas d'algorithmie par exemple et il n'y a aucun prérequis informatique à avoir. Le but est de pouvoir exécuter (de la façon la plus optimale possible) des lignes de code pour obtenir un résultat concret (qui n'aura souvent rien à voir avec de l'informatique).

## Partie I

### Principes

Avant d'écrire des programmes en python, on commence par s'intéresser à ses mécanismes internes en comprenant ce qu'est une instruction python et ce que'on peut faire avec.

{% aller %}
[Principes](principes){.interne}
{% endaller %}

### Exécuter du code python

Écrire directement à l'interpréteur comme on l'a fait jusqu'à présent est faisable lorsque l'on a besoin de n'écrire qu'une ligne de python à la fois, mais lorsque l'on veut faire des choses plus compliquées comme créer des tests ou effectuer des boucles, il faut des outils plus perfectionnés.

Nous allons montrer trois outils pour faire cela : les notebooks, [Spyder](https://www.spyder-ide.org/) et [vscode](https://code.visualstudio.com/).

#### Notebooks

Ce sont des solutions pratiques lorsque l'on veut exécuter rapidement un petit bout de code ou une série de bouts de codes plus ou moins indépendant : lorsque l'on utilise l'outil informatique pour faire des maths ou de la physique par exemple ; ou encore lorsque l'on fait de la data science.

C'est une manière plus conviviale que la console d'accéder à l'interpréteur python. L'utilisation des [Notebooks](https://jupyter.org/) est particulièrement adaptée pour rédiger et partager des comptes-rendus.

{% aller %}
[Notebooks](notebooks){.interne}
{% endaller %}

#### Spyder

{% lien %}
<https://www.spyder-ide.org/>
{% endlien %}

Spyder est un éditeur lié à un interpréteur python. L'application est très utilisée lorsque l'on commence à apprendre la programmation. Et permet d'écrire des programmes tout en conservant un unique interpréteur accessible par une console.

Il fonctionne à la fois comme un notebook ou comme un interpréteur.

{% attention %}
La commande `Run file` exécute son code dans un nouvel interpréteur **puis** le fusionne avec l'interpréteur courant.

Ce fonctionnement est déroutant...
{% endattention %}

Si vous voulez faire du développement sérieusement, je vous conseille d'utiliser plutôt la combinaison éditeur + interpréteur ci-dessous.

#### Vscode

> TBD installer vscode et exécuter du python avec le triangle.
> à la différence de spyder le code est réinitialisé à chaque exécution.
> montrer comment avec l'interpréteur.

### <span id="installation-développement"></span>Installer et utiliser un interpréteur

{% aller %}
[Installer et utiliser un interpréteur](interpréteur){.interne}
{% endaller %}

## Partie II: structurer son code

> module de python. Matplotlib et spyder
> conditions, boucles et fonctions avec spyder.
>
> montrer qu'une fonction est toujours là après avoir été crée. Faire une fonction avec spyder, l'envoyer dans l'interpréteur puis l'utiliser.

### Utiliser le module matplotlib

> TBD à déplacer, cela utilise des choses non vues.

Installé avec la plupart des environnements fournissant un interpréteur, le module matplotlib est devenu un standard de fait (pour le meilleur et surtout le pire) pour représenter des graphiques.

{% aller %}
[Tutoriel Matplotlib](matplotlib){.interne}
{% endaller %}

Si vous avez le choix, je conseille plutôt d'utiliser [le module seaborn](https://seaborn.pydata.org/) pour dessiner vos graphique. Mais comme ce module est basé sur matplotlib, une connaissance minimale de matplotlib, comme le donne le tutoriel précédent est tout de même nécessaire.

## <span id="coder-en-python"></span>Partie III : coder en python

Nous avons pour l'instant utilisé python pour exécuter des instructions ou des fonctions. Ceci permet déjà d'utiliser python mais va se révéler rapidement limitant lorsque l'on voudra effectuer des tâches plus complexes ou tout simplement non prévue par les modules.

Coder en python (ou en tout autre langage) ce cependant nécessiter des connaissances (un peu) plus poussées et des outils dédiées au code. Nous irons plus loin plus tard.

> TBD Ici prérequis base système.

> TBD Ici ajouter plusieurs fichier pour créer ses propres modules.
> séparer main de fct.py

### Structurer du code

Lorsque l'on veut plus que juste utiliser des méthodes et fonctions déjà existante, il faut structurer son code en parties utilisables indépendamment, que ce soit sous la forme de code (bloc, fonctions, modules).

{% aller %}
[Structurer son code](structurer-son-code){.interne}
{% endaller %}

## <span id="conteneurs"></span> Partie III : Conteneurs

### Liste, ensembles et dictionnaire

Les conteneurs sont des objets contenant d'autres objets. Ils permettent de structurer ses données.

{% aller %}
[Conteneurs](conteneurs){.interne}
{% endaller %}

### Mutable et non mutable

Les 5 type d'objets de base (`int`{.language-}, `float`{.language-}, `complex`{.language-}, `bool`{.language-} et `str`{.language-}) sont **non modifiables** (python dira **_non mutables_**). Ceci signifie que les méthodes et opérations sur ces objets ne peuvent les modifier :

- si `i`{.language-} contient un entier, `i = i + 1`{.language-} créera un nouvel entier qui sera associé à la variable `i`{.language-}
- `"coucou".replace("c", "b")`{.language-} créera une nouvelle chaîne de caractères

Les listes, ensembles et dictionnaires sont eux **modifiables** (python dira **_mutables_**), c'est à dire que leurs méthodes peuvent les modifier :

- `l.append("x")`{.language-} modifiera la liste `l`{.language-}
- `d["un"] = 1`{.language-} modifiera le dictionnaire `d`{.language-} en lui ajoutant une clé
- `e.add("un")`{.language-} modifiera l'ensemble `e`{.language-} en lui ajoutant un élément

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

- une chaîne de caractère est non modifiables (elles sont souvent crées une fois pour toute dans un programme)
- une liste est modifiable. L'utilisation des listes dans un programme nécessite souvent de la modifier.

Il existe des objets non modifiable pouvant être utilisé à la place des listes et des ensembles :

- un [`tuple`{.language-}](https://docs.python.org/fr/3/tutorial/datastructures.html#tuples-and-sequences) pour une liste. Elle se crée en remplaçant les `[]`{.language-} d'une liste par des `()`{.language-} : `(1, 2, 3)`{.language-} crée un tuple à 3 éléments. Il pourra être utilisé comme une liste mais on ne pourra jamais lui ajouter ou modifier ses éléments.
- un [`frozenset`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#frozenset) sera le pendant non mutable d'un ensemble. On place les éléments directement à la création et ils ne peuvent plus être modifiés ensuite.

{% info %}
Il n'existe pas d'équivalent non mutable aux dictionnaires.
{% endinfo %}

On peut alors utiliser des tuples et des `frozenset`{.language-} comme éléments d'un ensemble ou comme clé de dictionnaires.

Par exemple l'ensemble de tous les sous-ensemble de ${1, 2}$ s'écrira :

```python
>>> x = {frozenset(), frozenset([1]), frozenset([2]), frozenset([1, 2])}
>>> x
{frozenset(), frozenset({2}), frozenset({1}), frozenset({1, 2})}
```

{% info %}
Le tuple vide s'écrira `(,)`{.language-} (ou `tuple()`{.language-}) pour la différentier la notation `()`{.language-} qui est la parenthèse vide.
{% endinfo %}


## Espace de nommage

<!-- 
> TBD à déplacer, après avoir vu les structures de dictionnaires et de listes. à mettre dans la partie débuggeur, bien plus tard

> TBD reprendre avec la partie variable qui commence à en parler. Le mettre après coder ses fonctions/modules.
>
> Le voir avec le débogeur : stackframe = espace de nommage.
> 
 -->

Certains modules sont très utiles en python scientifique :

- [numpy](https://numpy.org/) : très utilisé pour ses structures de matrices et tableaux
- [matplotlib](https://matplotlib.org/) : pour créer des graphiques en python
- [scipy](https://scipy.org/) : résolution d'équations différentielles
- [pillow](https://pillow.readthedocs.io/en/stable/) : gestion d'images
- [sklearn](https://scikit-learn.org/stable/) : machine learning

Ils ne viennent pas automatiquement lorsque l'on installe python, mais beaucoup sont déjà installés si vous utilisez l'interpréteur de [spyder](https://www.spyder-ide.org/) ou encore les notebooks de <https://colab.research.google.com>. Nous plus tard comment installer ses propres modules, pour l'instant nous allons uniquement utiliser ceux fournis par python (et ils sont déjà nombreux).

On a vu que les variables étaient des noms permettant d'acceder aux objets, qui sont les seules choses que l'on peut manipuler en python. Python stocke ces variables dans des [espaces de nommage](https://docs.python.org/fr/3.13/glossary.html#term-namespace) (_namespace_ en anglais)

{% aller %}
[Espace de nommage](espace-nommage){.interne}
{% endaller %}

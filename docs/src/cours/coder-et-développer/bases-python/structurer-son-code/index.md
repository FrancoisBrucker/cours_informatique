---
layout: layout/post.njk

title: Structurer son code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Lorsque l'on veut plus que juste utiliser des méthodes et fonctions déjà existante, il faut structurer son code en parties utilisables indépendamment, que ce soit sous la forme de code (bloc, fonctions, modules) ou de données (conteneurs).

Nous n'utiliserons plus directement l'interpréteur pour nos futurs code. En effet, créer des bloc directement avec l'interpréteur est un calvaire car il est fait pour exécuter une ligne après l'autre alors qu'un bloc nécessite plusieurs lignes.

{% info %}
Utilisez un notebook ou spyder pour exécuter les divers exemples et exercices.
{% endinfo %}

## Blocs

Pour l'instant nous avons envoyé chaque ligne de python que nous avons écrite directement à l'interpréteur pour être exécuté. Les *blocs* de python permettent de grouper un ensemble de lignes de code pour être exécutés sous certaines conditions.

{% aller %}
[Blocs](blocs){.interne}
{% endaller %}

## <span id="conteneurs"></span> Conteneurs

Les conteneurs sont des objets contenant d'autres objets. Ils permettent de structurer ses données.

{% aller %}
[Conteneurs](conteneurs){.interne}
{% endaller %}

## Modules

Structurer son code vient en groupant les diverses fonctions et méthodes en groupes homogènes, appelés bibliothèque ou [modules](https://docs.python.org/fr/3/tutorial/modules.html) en python.

{% aller %}
[Modules](modules){.interne}
{% endaller %}

## Créer ses propres fonctions

Si un bloc de code est exécuté plusieurs fois à l'identique, on aimerait aussi pouvoir nommer ce groupe pour **pouvoir le réutiliser juste en appelant son nom**. C'est possible avec les fonctions.

{% aller %}
[Création de fonctions](creation-fonctions){.interne}
{% endaller %}

## Mutable vs non-mutable

Les 5 type d'objets de base (`int`{.language-}, `float`{.language-}, `complex`{.language-}, `bool`{.language-} et `str`{.language-}) sont **non modifiables** (python dira ***non mutables***). Ceci signifie que les méthodes et opérations sur ces objets ne peuvent les modifier :

- si `i`{.language-} contient un entier, `i = i + 1`{.language-} créera un nouvel entier qui sera associé à la variable `i`
- `"coucou".replace{"c", "b"}`{.language-} créera une nouvelle chaîne de caractères

Les liste, ensembles et dictionnaires sont eux **modifiables** (python dira ***mutables***), c'est à dire que leurs méthodes peuvent les modifier :

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

- un [`tuple`{.language-}](https://docs.python.org/fr/3/tutorial/datastructures.html#tuples-and-sequences) pour une liste. Elle se crée en remplaçant les `[]` d'une liste par des `()` : `(1, 2, 3)` crée un tuple à 3 éléments. Il pourra être utilisé comme une liste mais on ne pourra jamais lui ajouter ou modifier ses éléments.
- un [`frozenset`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#frozenset) sera le pendant non mutable d'un ensemble. On place les éléments directement à la création et ils ne peuvent plus être modifiés ensuite.

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

### Notation `.`

On l'a vue pour les méthodes et les modules. De façon générale la notation `A.B` : se lit ainsi on cherche le nom `B` dans l'espace de nom `A`.

{% note %}
Une méthode n'est rien d'autre qu'un nom appelable dans l'espace de nom de l'objet à gauche du point
{% endnote %}

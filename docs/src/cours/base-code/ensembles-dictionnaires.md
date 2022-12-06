---
layout: layout/post.njk 
title: Ensembles et dictionnaires

eleventyNavigation:
  key: "Ensembles et dictionnaires"
  parent: "Bases en code et python"
---

<!-- début résumé -->

Les ensembles et les dictionnaires sont des structures de données très utiles si on sait les utiliser.

<!-- end résumé -->

Les structures d'ensemble et de dictionnaire partagent beaucoup de chose. Ils sont en particulier créés de la même manière (en utilisant des [fonctions de hash]({{ "/cours/algorithme-code-théorie/théorie/fonctions-hash" | url }})).

## Ensembles

Les structure ensemblistes permettent de répondre facilement à des problématiques du genre :

* est-ce un de mes contact qui appelle ?
* est-ce que cette lettre est une majuscule ?
* est-ce un mot que j'ai déjà vu ?

Gérer des ensembles rapidement et avec peu de place en mémoire :

* ajouter un élément à un ensemble (on ne rajoute pas un élément qui y est déjà)
* supprimer un élément à un ensemble
* savoir si un élément est déjà dans un ensemble

### Dictionnaires

Un dictionnaire, aussi appelé [tableau associatif](https://fr.wikipedia.org/wiki/Tableau_associatif) associe une clé à une valeur. On peut voir les listes comme un tableau associatif où les clés sont des entiers allant de 0 à la longueur de la liste moins 1.

Mais cela peut être bien plus général que ça :

* les clés peuvent être de mots et les valeur un nombre. Cela permet par exemple de compter le nombre de fois où un chaque mot d'un texte apparaît.
* associer un nom (valeur) à un numéro de téléphone (clé) sans avoir besoin d'une liste allant de 0 à numéro max de téléphone.

{% info %}
Un ensemble peut être codé en utilisant la structure de dictionnaire en considérant que les valeurs sont toutes les mêmes. On ne considère que les clés qui représentent les éléments de l'ensemble.
{% endinfo %}

## En python

ce que c'est :

* ensemble : [`set`](https://docs.python.org/fr/3/tutorial/datastructures.html#sets)
* dictionnaires : [`dict`](https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries)

Les éléments pouvant être stockés dans des ensemble ou les clés des dictionnaires doivent être des objets **non modifiables**. Comme par exemple :

* des entiers
* des réels
* des chaines de caractères
* des tuples
* ...

Les éléments modifiables ne peuvent **pas** être des clés. Par exemple :

* des listes
* des ensembles
* des dictionnaires

### Ensemble

{% chemin %}
<https://realpython.com/python-sets/>
{% endchemin %}

```python
>>> S = set()
>>> S.add(123)
>>> S.add("une chaîne de caractères")
>>> S
{'une chaîne de caractères', 123}
```

N'hésitez pas à regarder les méthodes associées aux ensembles et à les utiliser dans vos programmes. Ils sont très pratiques !

Il existe de ensemble non modifiable, nommé [`frozenset`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#frozenset) (on place les éléments directement à la création et ils ne peuvent plus être modifiés ensuite). Les ensembles non modifiables peuvent alors être placés dans des ensemble ou être des clés de dictionnaires.

### <span id="dictionnaire"></span> Dictionnaire

{% chemin %}
<https://realpython.com/python-dicts/>
{% endchemin %}

Les clés ne doivent pas changer une fois créées, sinon la serrure fabriquée dans le dictionnaire ne fonctionne plus. On ne doit donc utiliser que des objets **non modifiable** pour créer des clés d'un dictionnaire python.

#### Création

```python
d = {} #identique à d = dict()
d = {"un":1, "deux":2} #identique à d = dict([("un", 1), ("deux", 2)])
```

#### Obtention, modification, ajout et suppression d'un élément

Identique à une liste, mais on utilise les clés plutôt que les indices :

avec `d = {"un":1, "deux":2}`{.language-} :

* `d["un"]`{.language-}  retourne 1
* `d["trois"]`{.language-} retourne une erreur : la clé "trois" n'existe pas.
* Ajout d'un élément :  `d["trois"] = 3`{.language-}
* Suppression d'un élément :  `del d["deux"]`{.language-}

#### itération

supposons que l'on ait le dictionnaire :

```python
d = {
    "a": 1,
    "b": 2,
}
```

Le code suivant :

```python
for x in d:
    print(x) # affichera les clés
```

Affichera les clés du dictionnaires. On affichera donc :

* peut être 'a' puis 'b'
* peut être 'b' puis 'a'

L'ordre d'itération des clés n'est **PAS** connu à l'avance : il peut changer d'une ordinateur à l'autre, et même d'une exécution à l'autre. Un dictionnaire  contient des éléments stockés sans ordre particulier.

On peut aussi itérer sur les clés en utilisant la méthode `keys`{.language-} :

```python
for x in d.keys():
    print(x) # affichera les clés
```

On peut aussi itérer sur les valeurs en utilisant la méthode `values`{.language-} :

```python
for x in d.values():
    print(x) # affichera les valeurs
```

Ou encore itérer sur les couples (clé, valeur) avec la méthode `items`{.language-} :

```python
for x in d.items():
    print(x) # affichera les couples (clé, valeur)
     
```

### Exercices

{% exercice %}
Combien de mots différents contient le texte `"coucou les gars coucou les filles"`{.language-} ?

Vous pourrez utiliser la méthode [split des ``str`](https://docs.python.org/fr/3/library/stdtypes.html#str.split)
{% endexercice %}
{% details "solution" %}

```python
texte = "coucou les gars coucou les filles"

mots = set()
for x in texte.split():
    mots.add(x)

print(len(mots))
```

Attention cependant aux caractères de ponctuation lors du `split`{.language-}. `"x, x. x ?".split()` donne  `['x,', 'x.', 'x', '?']`{.language-})

{% enddetails %}

{% exercice %}
Comptez les occurrences de chaque mot du texte `"coucou les gars coucou les filles"`{.language-} ?

Vous pourrez utiliser la méthode [split des ``str`](https://docs.python.org/fr/3/library/stdtypes.html#str.split)
{% endexercice %}
{% details "solution" %}

```python
texte = "coucou les gars coucou les filles"

mots = dict()
for x in texte.split():
    if x in mots:
        mots[x] += 1
    else:
        mots[x] = 1

print(mots)
```

{% enddetails %}

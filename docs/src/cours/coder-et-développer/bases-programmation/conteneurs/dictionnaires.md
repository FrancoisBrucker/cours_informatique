---
layout: layout/post.njk
title: Dictionnaires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les dictionnaires sont des structures de données très utiles si on sait les utiliser.

Un dictionnaire, aussi appelé [tableau associatif](https://fr.wikipedia.org/wiki/Tableau_associatif) associe une clé à une valeur. On peut voir les listes comme un tableau associatif où les clés sont des entiers allant de 0 à la longueur de la liste moins 1.

Mais cela peut être bien plus général que ça :

- les clés peuvent être de mots et les valeur un nombre. Cela permet par exemple de compter le nombre de fois où un chaque mot d'un texte apparaît.
- associer un nom (valeur) à un numéro de téléphone (clé) sans avoir besoin d'une liste allant de 0 à numéro max de téléphone.

{% info %}
Un ensemble peut être codé en utilisant la structure de dictionnaire en considérant que les valeurs sont toutes les mêmes. On ne considère que les clés qui représentent les éléments de l'ensemble.
{% endinfo %}

{% lien %}

- <https://realpython.com/python-dicts/>
- [`dict`{.language-}](https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries)

{% endlien %}

On peut créer des dictionnaires de multiples manières. Les 3 façons ci-dessous créent le même dictionnaire :

- directe : `{"un": 1, "deux": 2}`{.language-}
- via un itérable de couples `[clé, valeur]`{.language-} : `dict([["un", 1], ["deux", 2]])`{.language-}
- via une list compréhension : `{clé: valeur for clé, valeur in [["un", 1], ["deux", 2]]}`{.language-}

Les clés ne doivent pas changer une fois créées, sinon la serrure fabriquée dans le dictionnaire ne fonctionne plus. On ne doit donc utiliser que des objets **non modifiable** pour créer des clés d'un dictionnaire python. Les valeurs en revanche peuvent être modifiables. Par exemple `{"l": [1, 2]}`{.language-} est une définition correcte d'un dictionnaire, alors que `{[1, 2]: "liste"}`{.language-} ne l'est pas.

## Obtention, modification, ajout et suppression d'un élément

Identique à une liste, mais on utilise les clés plutôt que les indices :

avec `d = {"un":1, "deux":2}`{.language-} :

- `d["un"]`{.language-} retourne 1
- `d["trois"]`{.language-} retourne une erreur : la clé "trois" n'existe pas.
- Ajout d'un élément : `d["trois"] = 3`{.language-}
- Suppression d'un élément : `del d["deux"]`{.language-}

## Itération

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
    print(x)
```

Affichera les clés du dictionnaires. On affichera donc :

- peut être `'a'`{.language-} puis `'b'`{.language-}
- peut être `'b'`{.language-} puis `'a'`{.language-}

{% attention %}

L'ordre d'itération des clés n'est **PAS** connu à l'avance : il peut changer d'une ordinateur à l'autre, et même d'une exécution à l'autre. Un dictionnaire contient des éléments stockés sans ordre particulier.

{% endattention %}

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

## Présence

L'opérateur `in`{.language-} appliquée à un dictionnaire vérifie si une clé est dans le dictionnaire, elle ne s'occupe pas des valeurs :

```python
>>> d = {"réponse": 42, "utile": "serviette"}
>>> "utile" in d
True
>>> 42 in d
False
```

On peut aussi utiliser les résultats des méthodes `.keys()`{.language-} et `.values()`{.language-} avec l'opérateur `in`{.language-}

```python
>>> d = {"réponse": 42, "utile": "serviette"}
>>> 42 in d.values()
True
>>> "utile" in d.keys()
True
```

---
layout: layout/post.njk
title: Ensembles

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Les structure ensemblistes permettent de répondre facilement à des problématiques du genre :

- est-ce un de mes contacts qui appelle ?
- est-ce que cette lettre est une majuscule ?
- est-ce un mot que j'ai déjà vu ?

Gérer des ensembles rapidement et avec peu de place en mémoire :

- ajouter un élément à un ensemble (on ne rajoute pas un élément qui y est déjà)
- supprimer un élément à un ensemble
- savoir si un élément est déjà dans un ensemble

{% lien %}

- <https://realpython.com/python-sets/>
- [`set`{.language-}](https://docs.python.org/fr/3/tutorial/datastructures.html#sets)

{% endlien %}

On peut créer des ensemble de multiples manières :

- directe : `{1, 2, 3}`{.language-}
- avec un itérable `set("coucou")`{.language-}
- avec une list comprehension : `{x for x in range(10) if x % 2 == 0}`{.language-}

{% attention %}
L'ensemble vide se crée avec l'instruction `set()`{.language-}. L'instruction `{}`{.language-} rend un dictionnaire vide.
{% endattention %}

Leur utilisation est très simple :

```python
>>> S = set()
>>> S.add(123)
>>> S.add("une chaîne de caractères")
>>> S
{'une chaîne de caractères', 123}
```

On peut itérer sur les éléments d'un ensemble :

```python
for x in {"pomme", "poire", "scoubidou"}:
    print(x)
```

{% attention %}
L'ordre d'itération n'est **PAS** connu à l'avance : il peut changer d'une ordinateur à l'autre, et même d'une exécution à l'autre.
{% endattention %}

Ou savoir si un élément est dans l'ensemble :

```python
>>> "poire" in {"pomme", "poire", "scoubidou"}
True
>>> "scoubidou" in {"pomme", "poire", "scoubidou"}
False
```

N'hésitez pas à regarder les méthodes associées aux ensembles, ils permettent de réaliser toutes les opérations courantes sur les ensembles et vous permettrons de gagner un temps fou dans vos programmes.

Attention cependant, un ensemble ne peut être constitué que d'objets qui ne peuvent pas être modifié, comme les nombres (entiers, réels ou complexe) ou encore les chaînes de caractères. Il est ainsi impossible de constituer un ensemble de listes :

```python
>>> set([[1, 3], [2, 4]])
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    set([[1, 3], [2, 4]])
    ~~~^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'
>>>
```

L'erreur semble étrange `unhashable type: 'list'`{.language-}. On y reviendra mais retenez pour l'instant que ceci signifie qu'on ne peut hasher qu'un objet non modifiable.

## Exercice

{% exercice %}
Combien de mots différents contient le texte `"coucou les gars coucou les filles"`{.language-} ?

Vous pourrez utiliser la méthode [split des `str`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.split)
{% endexercice %}
{% details "solution" %}

```python
texte = "coucou les gars coucou les filles"

mots = set()
for x in texte.split():
    mots.add(x)

print(len(mots))
```

Attention cependant aux caractères de ponctuation lors du `split`{.language-}. `"x, x. x ?".split()`{.language-} donne `['x,', 'x.', 'x', '?']`{.language-}.

{% enddetails %}

{% exercice %}
Comptez les occurrences de chaque mot du texte `"coucou les gars coucou les filles"`{.language-} ?

Vous pourrez utiliser la méthode [split des `str`](https://docs.python.org/fr/3/library/stdtypes.html#str.split)
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

---
layout: layout/post.njk

title: Conteneurs

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

En plus des 6 types de bases, python met à notre disposition plusieurs objets qui peuvent _contenir_ des variables. On appelle ces objets des **_conteneurs_** et ils possèdent de nombreuses propriétés :

- ils sont itérables et peuvent donc être associé à [une boucle for](../fondements-programmation/structure-code/#for)
- ils possèdent l'opérateur `in`{.language-}. On pourra ainsi toujours utiliser `x in C`{.language-} pour savoir si l'objet `x`{.language-} est dans le conteneur `C`{.language-}.

## Listes et tuples

Parmi tous les conteneurs de python, la **_liste_** est certainement la plus utilisée.

{% aller %}
[Listes](listes){.interne}
{% endaller %}

La plupart des conteneurs possèdent deux formes : l'une mutable l'autre non mutable. Le tuple est la version non mutable des listes :

{% aller %}
[Tuples](tuples){.interne}
{% endaller %}

## <span id="ensembles-dictionnaires"></span>Ensembles et dictionnaires

Les deux autres conteneurs à connaître sont les **_ensembles_** et les **_dictionnaires_**. Ces deux structures sont très utiles lorsque l'on manipule des données mais sont plus complexes à manipuler que des listes. Prenez le temps d'apprendre à utiliser leurs nombreux avantages.

Les ensembles et les dictionnaires sont tous deux des conteneurs, donc itérables mais contrairement aux listes, leur ordre d'itération est **inconnu**. Il peut changer d'une itération à l'autre.

### Ensembles

{% aller %}
[Ensembles](ensembles){.interne}
{% endaller %}

Le pendant non mutable d'un ensemble est le [`frozenset`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#frozenset). Par exemple :

```python

f = frozenset({1, 2, 3})
```

qui transforme l'ensemble `{1, 2, 3}`{.language-} en un `frozenset`{.language-}.

### Dictionnaires


{% aller %}
[Dictionnaires](dictionnaires){.interne}
{% endaller %}

Les dictionnaires possèdent [depuis python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html#whatsnew315-frozendict) leur pendant non mutable sous la forme d'un `frozendict`{.language-}

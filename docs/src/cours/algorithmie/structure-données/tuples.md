---
layout: layout/post.njk 
title:  "Tuples"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Les tuples permettent de créer des types composés. C'est un regroupement d'objets qu'on représente en algorithmie avec des parenthèses :

```pseudocode
p ← (34, 25)  # tuple de 2 entiers
```

Un tuple peut être composé de types différents :

```pseudocode
anniversaire ← (10, "janvier", 1938)  # tuple composé de deux entiers et d'une chaîne de caractères
```

On peut accéder à chaque élément du tuple comme un tableau :

```pseudocode
p ← (34, 25)  # tuple de 2 entiers
affiche à l'écran p[0]  # va afficher 34
affiche à l'écran p[1]  # va afficher 25
```

Enfin, un tuple peut bien sur être composé d'autres tuples :

```pseudocode
ps ← ((0, 0), "origine")  # tuple composé d'un tuple et d'une chaîne de caractères
affiche à l'écran p[0]  # va afficher 34
affiche à l'écran p[1]  # va afficher 25
```

En revanche, il est impossible de modifier un tuple une fois créé.

{% attention "**À retenir**" %}
Un **_tuple_** est un regroupement fini d'objets de types pouvant être différent.

Ce n'est **pas** un tableau même si on peut accéder à chaque élément d'un tuple par son indice.
{% endattention %}

Un tuple est un type utilisable par un algorithme. Par exemple, le type de [l'algorithme de la division euclidienne](../../prouver-un-algorithme/#algorithme-division-euclidienne) `algorithme division_euclidienne(a: entier, b: entier) → [entier]`{.language-} est bien plus explicite si on l'écrit :

```pseudocode
algorithme division_euclidienne(a: entier, b: entier) → (entier, entier)
```

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
p := (entier, entier) # tuple de 2 entiers
p ← (34, 25)  
```

Un tuple peut être composé de types différents :

```pseudocode
anniversaire ← (entier, chaîne, entier))  # tuple composé de deux entiers et d'une chaîne de caractères
anniversaire ← (10, "janvier", 1938)
```

On peut accéder à chaque élément du tuple comme un tableau :

```pseudocode
(p := (entier, entier)) ← (34, 25)  # tuple de 2 entiers
affiche à l'écran p[0]  # va afficher 34
affiche à l'écran p[1]  # va afficher 25
```

Enfin, un tuple peut bien sur être composé d'autres tuples :

```pseudocode
ps := ((entier, entier), chaîne)  # tuple composé d'un tuple et d'une chaîne de caractères
ps ← ((0, 0), "origine") 
affiche à l'écran p[0]  # va afficher (0, 0)
affiche à l'écran p[1]  # va afficher 25
```

En revanche, il est impossible de modifier un tuple une fois créé. 

{% note2 "**Définition**" %}
Un **_tuple_** est un regroupement fini et ordonné d'objets de types pouvant être différent.

- Son type est composé des types des différents objets le contenant entre parenthèses et séparé par des virgules. Ce n'est **pas** un tableau même si on peut accéder à chaque élément d'un tuple par son indice.
- Un tuple est **non mutable** : il est impossible de changer l'objet associé à un élément du tuple. 
{% endnote2 %}

Un tuple est un type utilisable par un algorithme. Par exemple, le type de [l'algorithme de la division euclidienne](../../prouver-un-algorithme/#algorithme-division-euclidienne) `algorithme division_euclidienne(a: entier, b: entier) → [entier]`{.language-} est bien plus explicite si on l'écrit :

```pseudocode
algorithme division_euclidienne(a: entier, b: entier) → (entier, entier)
```

Attention cependant :


{% attention2 "**À retenir**" %}
Ce n'est pas parce que l'on ne peut pas changer d'objet que l'objet lui même ne peut pas être modifié.
{% endattention2 %}

Par exemple :

```pseudocode
p := ([entier], entier)  # tuple composé d'un tuple et d'une chaîne de caractères
p ← ([0, 0], 2) 
affiche à l'écran p[0]  # va afficher [0, 0]
p[0][0] ← 12
affiche à l'écran p[0]  # va afficher [12, 0]
```


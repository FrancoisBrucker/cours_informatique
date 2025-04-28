---
layout: layout/post.njk 
title:  "Structures de données"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les variables dans un algorithme ou un programme sont souvent liées. Un nombre complexe par exemple est composée d'une partie réelle et d'une partie imaginaire. Pour rendre compte de ces liens on peut grouper les variables en tuples, voir les structurer en leur ajoutant ds fonctions particulières appelée méthodes.

## Matrices

La plus simple des structures : les tableaux de tableaux.

{% aller %}
[Manipuler des matrices](./matrices){.interne}
{% endaller %}

## Tuples

Les tuples permettent de créer des types composés. C'est un regroupement d'objets qu'on représente en algorithmie avec des parenthèses :

```pseudocode
p ← (34, 25)  # tuple de 2 entiers
```

Un tuple peut être composé de types différent :

```pseudocode
anniversaire ← (11, "avril")  # tuple composé d'un entier et d'une chaîne de caractères
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
Un **_tuple_** est un regroupement fini d'objets de types pouvant être différent. On peut accéder à chaque élément d'un tuple par son indice.

Un tuple est non modifiable une fois crée.
{% endattention %}

Lorsque l'on a besoin de fonctions spécifiques pour des tuples particuliers on préférera utiliser des structures de données, plus lourde mais dont le but est la création de nouveaux types algorithmiques.

## Structures

Les tuples permettent de gérer des groupements informels d'objets en créant des types nouveaux par produit cartésien d'anciens types. Si l'on veut aller plus loin et créer des fonctions spécifiquement utilisable pour ces groupement, on utilise [une structure de données](https://fr.wikipedia.org/wiki/Structure_de_donn%C3%A9es) :

{% aller %}
[Créer une structure de données](./structures){.interne}
{% endaller %}

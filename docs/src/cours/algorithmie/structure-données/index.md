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

La plus simple des structures. On compose le type de base tableau :

{% aller %}
[Manipuler des matrices](./matrices){.interne}
{% endaller %}

## Tuples

Les tuples permettent de créer des types composés.

{% aller %}
[Tuples](./tuples){.interne}
{% endaller %}

## Structures

Les tuples permettent de gérer des groupements informels d'objets en créant des types nouveaux par produit cartésien d'anciens types. Si l'on veut aller plus loin et créer des fonctions spécifiquement utilisable pour ces groupements, on utilise [une structure de données](https://fr.wikipedia.org/wiki/Structure_de_donn%C3%A9es) :

{% aller %}
[Créer une structure de données](./structures){.interne}
{% endaller %}

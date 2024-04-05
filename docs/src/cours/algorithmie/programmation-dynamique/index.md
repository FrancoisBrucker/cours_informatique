---
layout: layout/post.njk

title: Programmation dynamique

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La programmation dynamique est un principe de création d'algorithme très général permettant de résoudre de nombreux problèmes de façon efficace, voir même optimale.

## Principe

{% aller %}
[Principe](./principe){.interne}
{% endaller %}

## Exemple de l'alignement de séquences

Le problème de l'alignement de séquences et l'utilisation de la programmation dynamique pour le résoudre est un classique indémodable.

{% aller %}
[Alignement de séquences](./alignement-séquences){.interne}
{% endaller %}

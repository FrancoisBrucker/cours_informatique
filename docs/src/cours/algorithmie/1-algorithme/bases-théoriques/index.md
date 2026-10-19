---
layout: layout/post.njk

title: Bases théoriques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On va définir dans cette partie ce que sont des programmes et des algorithmes.

{% aller %}
1. [Qu'est-ce qu'un algorithme ?](./définition)
2. [Problème de l'arrêt d'un programme](./arrêt-rice)
{% endaller %}

Enfin, on montrera qu'un algorithme ne peut pas tout faire et que savoir ce que fait un algorithme n'est pas un problème simple (c'est pour ça qu'il existe des algorithmiciens) :

{% aller %}

[Que peut faire un algorithme ?](./calculabilité)

{% endaller %}
  
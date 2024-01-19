---
layout: layout/post.njk

title: Algorithmie
tags: ['cours', 'algorithmie']
authors:
    - François Brucker

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Cours d'algorithmie.

{% info %}
*L'informatique n'est pas plus la science des ordinateurs que l'astronomie n'est celle des télescopes* [E. Dijkstra](https://fr.wikipedia.org/wiki/Edsger_Dijkstra)
{% endinfo %}

1. [Qu'est-ce qu'un algorithme ?](./définition){.interne}
2. [Que peut faire un algorithme ?](./calculabilité){.interne}
3. [Arrêt d'un algorithme](./arrêt-rice){.interne}
4. [Que ne peut pas faire un algorithme ?](./non-calculabilité){.interne}

1. [pseudo-code](./pseudo-code){.interne}
2. problème
3. décidabilité

1. Turing

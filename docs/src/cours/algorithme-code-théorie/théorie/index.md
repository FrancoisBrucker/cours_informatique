---
layout: layout/post.njk 
title: Théorie

eleventyNavigation:
    order: 3

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Que peut ou pas faire un algorithme.

<!-- fin résumé -->

{% note %}
*L'informatique n'est pas plus la science des ordinateurs que l'astronomie n'est celle des télescopes* [E. Dijkstra](https://fr.wikipedia.org/wiki/Edsger_Dijkstra)
{% endnote %}

<div class="interne">
{{ collections.all | eleventyNavigation(eleventyNavigation.key) | eleventyNavigationToHtml() | safe }}
</div>

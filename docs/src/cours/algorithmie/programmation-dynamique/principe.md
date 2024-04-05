---
layout: layout/post.njk

title: Principe

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


{% lien %}
[Page Wikipedia](https://fr.wikipedia.org/wiki/Programmation_dynamique)
{% endlien %}

Le principe de la programmation dynamique est simple :

{% note "**Principe**" %}
Une solution optimale est constituée de sous-solutions elles-mêmes optimales.
{% endnote  %}

Illustrons ce principe avec la recherche de chemins le plus rapide.


> TBD : dessin du chemin

faire le sac à dos. sera le fil rouge : glouton puis NP-dur


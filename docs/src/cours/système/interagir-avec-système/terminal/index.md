---
layout: layout/post.njk

title: Terminal
tags: ['tutoriel']

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Qu'est-ce que le terminal ? Comment le trouver et taper des commandes.

{% aller %}
[Terminal, les bases](bases)
{% endaller %}

{% aller %}
[Utilisation courante du terminal](utilisation)
{% endaller %}

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

## Application terminal

{% aller %}
[Terminal, les bases](bases){.interne}
{% endaller %}

{% aller %}
[Utilisation courante du terminal](utilisation){.interne}
{% endaller %}

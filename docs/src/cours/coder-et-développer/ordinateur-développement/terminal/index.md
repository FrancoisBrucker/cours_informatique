---
layout: layout/post.njk

title: Terminal

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Qu'est-ce que le terminal ? Comment le trouver et taper des commandes.

## Bases

{% aller %}
[Terminal, les bases](bases){.interne}
{% endaller %}

## Utilisation courante

{% aller %}
[Utilisation courante du terminal](utilisation){.interne}
{% endaller %}

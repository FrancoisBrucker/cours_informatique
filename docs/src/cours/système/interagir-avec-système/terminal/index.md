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
[Terminal, les bases](bases){.interne}
{% endaller %}

{% aller %}
[Utilisation courante du terminal](utilisation){.interne}
{% endaller %}

{% aller %}
[Utiliser le terminal de vscode](terminal-vscode){.interne}
{% endaller %}

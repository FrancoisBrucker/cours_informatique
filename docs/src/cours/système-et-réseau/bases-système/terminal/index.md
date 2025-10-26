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

## Terminal et vscode

Une des particularités de vscode est son intégration avec le terminal : il est très facile de l'utiliser et vscode l'utilise souvent (exécutez un programme python avec le triangle, vous verrez qu'il exécute une commande du terminal).

{% aller %}
[Vscode et le terminal](terminal-vscode){.interne}
{% endaller %}

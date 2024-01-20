---
layout: layout/post.njk

title: Bases théoriques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Définitions et premières propriétés d'un algorithme et d'un programme.

1. [Qu'est-ce qu'un algorithme ?](./définition){.interne}
2. [Problème de l'arrêt d'un programme](./arrêt-rice){.interne}
3. [Que peut faire un algorithme ?](./calculabilité){.interne}

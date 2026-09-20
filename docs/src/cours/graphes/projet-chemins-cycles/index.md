---
layout: layout/post.njk
title: Chemins et cycles

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Utilisation d'algorithmes gloutons pour résoudre des problèmes de cheminement.

- [étude](./étude){.interne}
- [Projet](./projet){.interne}

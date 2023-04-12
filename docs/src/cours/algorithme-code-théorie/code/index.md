---
layout: layout/post.njk 
title: Code

eleventyNavigation:
    order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "Algorithme, code et théorie"

---

<!-- début résumé -->

Comment coder, maintenir et aimer ses programmes.

<!-- fin résumé -->

Les projets constituent une progression, il est conseillé de les suivre dans l'ordre.

{{ collections.all | eleventyNavigation(eleventyNavigation.key) | eleventyNavigationToMarkdown() | safe }}
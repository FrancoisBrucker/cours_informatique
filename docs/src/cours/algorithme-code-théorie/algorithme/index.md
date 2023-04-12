---
layout: layout/post.njk 
title: Algorithme

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "Algorithme, code et théorie"
---

<!-- début résumé -->

Création, preuve et complexité des algorithmes.

<!-- fin résumé -->

{{ collections.all | eleventyNavigation(eleventyNavigation.key) | eleventyNavigationToMarkdown() | safe }}

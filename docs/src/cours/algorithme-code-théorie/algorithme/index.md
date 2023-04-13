---
layout: layout/post.njk 
title: Algorithme

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Création, preuve et complexité des algorithmes.

<!-- fin résumé -->

{{ collections.all | eleventyNavigation(eleventyNavigation.key) | eleventyNavigationToMarkdown() | safe }}

---
layout: layout/post.njk 
title: Programmation Objet

authors: 
  - François Brucker
  - Célia Châtel

eleventyNavigation:
    order: 8
    prerequis:
        - "/cours/coder-en-python/"
        - "../mémoire-espace-noms/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Bases de programmation objet.

<!-- end résumé -->

{{ collections.all | eleventyNavigation(eleventyNavigation.key) | eleventyNavigationToMarkdown() | safe }}
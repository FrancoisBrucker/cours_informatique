---
layout: layout/post.njk

title: Bases Linux

eleventyNavigation:
    order: 1
    prerequis:
        - "../fonctions/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Bases d'un système Linux.

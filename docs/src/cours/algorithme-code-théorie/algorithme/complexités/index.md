---
layout: layout/post.njk 
title: Complexités

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Différents tyopes de complexités

<!-- fin résumé -->

{{ collections.all | eleventyNavigation(eleventyNavigation.key) | eleventyNavigationToMarkdown() | safe }}

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

Différents types de complexités

<!-- fin résumé -->

<div class="interne">
{{ collections.all | eleventyNavigation(eleventyNavigation.key) | eleventyNavigationToHtml() | safe }}
</div>

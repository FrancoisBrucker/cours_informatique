---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: Data viz
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 0

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD

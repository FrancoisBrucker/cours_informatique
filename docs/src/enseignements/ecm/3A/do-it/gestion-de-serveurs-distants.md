---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: "Gestion de serveurs distants"
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD

---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: Analyse des données
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 0

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% aller %}
[Cours analyse des données](/cours/analyse-données)
{% endaller %}

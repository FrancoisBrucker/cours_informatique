---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: "Web front/back"
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Web front et back (avec node).

<!-- fin résumé -->

## Programme

{% aller %}
[Cours de web]({{ "/cours/web" }})
{% endaller %}

## Projet final

Il doit avoir :

* une partie back
* une partie front
* des données

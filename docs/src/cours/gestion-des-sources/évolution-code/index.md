---
layout: layout/post.njk

title: Gestion de l'évolution de son code source
tags: ["cours", "projet"]

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Comment gérer l'évolution de son code source au quotidien, sans avoir peur de modifier son code.

## Besoins pour une gestion des sources locale

{% aller %}
[Besoins](./besoins-gestion-sources){.interne}
{% endaller %}

## Projet : gestion des sources

{% aller %}
[Projet uniquement avec github](./github-projet){.interne}
{% endaller %}


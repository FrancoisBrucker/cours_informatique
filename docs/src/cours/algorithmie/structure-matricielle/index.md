---
layout: layout/post.njk 
title:  "Structures de données"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



La plus simple des structures, la composition de tableaux :

{% aller %}
[Types matriciels](./matrices)
{% endaller %}

On s'entraîne :

{% aller %}
[Projet matrices](./projet-matrices)
{% endaller %}

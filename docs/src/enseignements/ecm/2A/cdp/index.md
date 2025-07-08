---
layout: layout/post.njk
templateEngineOverride: njk, md

title: "Coder et développer en python"
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 0

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

24 heures de cours pour apprendre le python objet, les bases de la gestion des sources avec git et la programmation par les tests.

Basé sur le cours :

{% aller %}
[Coder et développer en python](/cours/coder-et-développer){.interne}
{% endaller %}

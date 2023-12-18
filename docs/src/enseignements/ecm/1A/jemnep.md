---
layout: layout/post.njk
templateEngineOverride: njk, md

title: "J'aimerais être moins nul en python"
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 0

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Une semaine pour comprendre le fonctionnement de python et l'utiliser pour développer ses propres programmes comme le ferai un informaticien.

<!-- fin résumé -->

Basé sur le cours :

{% aller %}
[Coder et développer en python](/cours/coder-et-développer){.interne}
{% endaller %}

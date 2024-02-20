---
layout: layout/post.njk

title: Algorithmes classiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Algorithmes classiques dont l'intérêt est à la fois esthétique (ce sont de jolis algorithmes),
pratiques (ils mettent en oeuvre des techniques facilement réutilisables) et didactiques (trouver et prouver leurs fonctionnement vous fera progresser).

{% aller %}
[sujets](exercices-sujets){.interne}
{% endaller %}
{% details "corrigé", "open" %}
[corrigés](exercices-corrigés){.interne}
{% enddetails %}

---
layout: layout/post.njk
templateEngineOverride: njk, md

title: "Jolis Algorithmes Classiques"
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 0

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Enveloppes convexes :

{% aller %}
[Problème de l'enveloppe convexe](/cours/algorithmie/enveloppes-convexes/){.interne}
{% endaller %}

Partie code :

{% aller %}
[Coder et développer en python](/cours/coder-et-développer){.interne}
{% endaller %}

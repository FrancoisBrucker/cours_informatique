---
layout: layout/post.njk

title: Principe

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


{% lien %}
[Page Wikipedia](https://fr.wikipedia.org/wiki/Programmation_dynamique)
{% endlien %}

Le principe de la programmation dynamique est simple :

{% note "**Principe**" %}
Une solution optimale est constituée de sous-solutions elles-mêmes optimales.
{% endnote  %}

Illustrons ce principe avec la recherche de chemins le plus rapide.

![opti A˜B](opti-1)
> TBD : dessin du chemin

Pour toute ville sur ce chemin, par exemple la ville C, le chemin est également optimal pour aller de A à C et pour aller de C à B :

![opti A˜C˜B](opti-2)

En effet, s'il existait un chemin plus rapide (le rouge) :

![opti A-C˜B](opti-3)

On peut donc construire petit à petit les solutions en allant de plus en plus loin  en conservant tous les résultat intermédiaires :

> RBD algo croissance chemin

faire le sac à dos. sera le fil rouge : glouton puis NP-dur


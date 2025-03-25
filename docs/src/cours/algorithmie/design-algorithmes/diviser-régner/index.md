---
layout: layout/post.njk

title: Diviser pour régner

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Principe

{% aller %}
[Principe](./principe){.interne}
{% endaller %}

## Exemple du calcul de la médiane

Un calcul optimal en temps linéaire. Fait parti selon moi des résultats les plus surprenant (et beau) en algorithmie.

{% aller %}
[Calcul de la médiane](./médiane){.interne}
{% endaller %}

---
layout: layout/post.njk

title: Alignement de séquences

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---
{% lien %}
[Page Wikipedia](https://fr.wikipedia.org/wiki/Alignement_de_s%C3%A9quences)
{% endlien %}

## Étude algorithmique du problème

{% aller %}
[Étude](./étude){.interne}
{% endaller %}

## Projet de code

{% aller %}
[Projet](./projet){.interne}
{% endaller %}


---
layout: layout/post.njk

title: Gestion des données

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons voir deux types de données : les chaines de caractères et les fichiers texte.

## Chaîne de caractères

{% aller %}
[Encodage Unicode](encodage-unicode){.interne}
{% endaller %}

## Fichiers

{% aller %}
[Fichiers](fichiers){.interne}
{% endaller %}


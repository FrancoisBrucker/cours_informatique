---
layout: layout/post.njk 
title: "Fichiers"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


<!-- début résumé -->

Qu'est-ce qu'un fichier et comment l'utiliser.

{% aller %}
[Qu'est-ce qu'un fichier](structure){.interne}
{% endaller %}

## Fichiers texte

{% aller %}
[fichiers texte](fichiers-texte){.interne}
{% endaller %}

{% aller %}
[projet fichiers texte](fichiers-binaire){.interne}
{% endaller %}

## Fichiers binaire

{% aller %}
[fichiers binaire](fichiers-binaire){.interne}
{% endaller %}

## Dossiers et chemins

{% aller %}
[dossiers et chemins en python](dossiers-et-chemins){.interne}
{% endaller %}


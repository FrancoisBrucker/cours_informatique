---
layout: layout/post.njk 
title: "Fichiers"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Qu'est-ce qu'un fichier et comment l'utiliser.

## Définition

{% aller %}
[Qu'est-ce qu'un fichier](structure)
{% endaller %}

## Fichiers texte

{% aller %}
[fichiers texte](fichiers-texte)
{% endaller %}

{% aller %}
[projet fichiers texte](projet-texte)
{% endaller %}

Stocker des données dans un fichier :

{% aller %}
[fichiers texte pour stocker des données](projet-données)
{% endaller %}

## Fichiers binaire

{% aller %}
[fichiers binaire](fichiers-binaire)
{% endaller %}

## Dossiers et chemins

{% aller %}
[dossiers et chemins en python](dossiers-et-chemins)
{% endaller %}


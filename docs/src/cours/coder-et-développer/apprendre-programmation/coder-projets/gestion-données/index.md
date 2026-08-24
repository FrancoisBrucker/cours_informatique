---
layout: layout/post.njk

title: Gestion des données

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Avant de pouvoir écrire des programmes conséquents il faut comprendre comment est organisé votre ordinateur et pouvoir minimalement interagir avec son système d'exploitation. Donc lisez la partie consacrée aux bases d'un système d'exploitation avant de continuer :

## En mémoire

{% aller %}
[Données en mémoire](données-mémoire){.interne}
{% endaller %}

## Chaîne de caractères

{% aller %}
[Encodage Unicode](encodage-unicode){.interne}
{% endaller %}

## Sur des fichiers

{% aller %}
[Fichiers](fichiers){.interne}
{% endaller %}


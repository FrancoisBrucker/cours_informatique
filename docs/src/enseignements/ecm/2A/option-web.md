---
layout: layout/post.njk
templateEngineOverride: njk, md

title: "Web front/back"
tags: ["enseignement", "ECM"]

eleventyNavigation:
  order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Web front et back (avec node).

<!-- fin résumé -->

## Programme

{% aller %}
[Cours de web](/cours/web){.interne}
{% endaller %}

## cours 1

A faire : une page avec son animal favori. Cette page doit contenir :

1. deux images de celui-ci :
   - une depuis internet
   - une depuis votre disque dur appelée avec une adresse relative
2. le lien Wikipédia
3. deux paragraphes de pourquoi c'est votre animal favori

Cette page doit être validée par le W3C

## Projet final

Il doit avoir :

- une partie back
- une partie front
- des données

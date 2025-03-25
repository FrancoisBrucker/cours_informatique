---
layout: layout/post.njk
title: Design d'algorithmes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD donner des exemples du discours de la méthode (cf. poly PP)

## Diviser pour régner

{% aller %}
[Diviser pour régner](./diviser-régner){.interne}
{% endaller %}

## Programmation dynamique

{% aller %}
[Programmation dynamique](./programmation-dynamique){.interne}
{% endaller %}

## Algorithmes gloutons

{% aller %}
[Algorithmes gloutons](./algorithmes-gloutons){.interne}
{% endaller %}

## Recherche exhaustive

{% aller %}
[Énumération de toutes les solutions](./algorithmes-énumération){.interne}
{% endaller %}

## Méta-heuristiques

> TBD partie approximation et performances garanties

Méthode générale de création d'algorithmes heuristiques sans garantie de performance mais souvent efficace en pratique. Un peu oublié de part la prépondérance des méthodes à base de réseau de neurones, mais peut-être utile si on ne peut pas entraîner un réseau et certaines méthodes sont très efficaces.

> <https://fr.wikipedia.org/wiki/M%C3%A9taheuristique>
> <https://www.techno-science.net/glossaire-definition/Probleme-du-sac-a-dos-page-4.html>
> <https://fr.wikipedia.org/wiki/M%C3%A9taheuristique>

- recuit simulé
- tabou
- algorithme génétiques
- fourmi

---
layout: layout/post.njk

title: Dépot du code source
tags: ["cours", "projet"]

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Après avoir examiné les besoins qui impliquent l'utilisation d'un SCM, on en verra une implémentation possible sur une structure distribuée et l'usage qu'on peut en faire au quotidien.

## Besoins pour un dépôt

{% aller %}
[Besoins](./besoins-dépôt/){.interne}
{% endaller %}

## Projet : dépôt github

Nous allons utiliser <https://github.com/> comme dépôt commun de nos projet. Le site fonctionne avec logiciel de gestion de sources [git](https://fr.wikipedia.org/wiki/Git). Il en existe d'autres, comme <https://gitlab.com/> par exemple.

{% aller %}
[Création d'un compte github](./github-compte){.interne}

{% endaller %}


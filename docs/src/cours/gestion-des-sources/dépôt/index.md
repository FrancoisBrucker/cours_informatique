---
layout: layout/post.njk

title: Dépôt du code source

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons voir les besoins minimum pour stocker et distribuer un code source. Pour cela il nous fout un lieu sur internet où l'on pourra déposer son code.

## Création d'un compte github

Nous avons chois d'utiliser la plateforme [github](https://github.com/), donc commençons par nous y créer un compte :

{% aller %}
[Création d'un compte github](./github-compte){.interne}
{% endaller %}

Après avoir examiné les besoins qui impliquent l'utilisation d'un SCM, on en verra une implémentation possible sur une structure distribuée et l'usage qu'on peut en faire au quotidien.

## Besoins pour un dépôt

{% aller %}
[Besoins](./besoins-dépôt/){.interne}
{% endaller %}

## Projet 

Un projet pour apprendre à créer un projet sous github :

{% aller %}
[Projet Numérologie](./projet-dépot/){.interne}
{% endaller %}




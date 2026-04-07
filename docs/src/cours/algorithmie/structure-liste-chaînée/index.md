---
layout: layout/post.njk
title: "Liste Chaînée"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Liste chaînée](https://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e)
{% endlien %}

## Listes chaînées

Très utilisé en programmation fonctionnelle, la liste chaînée est une structure pouvant théoriquement ˆ´tre de taille infinie :

{% aller %}
[La liste chaînée](liste-chaînée){.interne}
{% endaller %}


## Listes doublement chaînées

En algorithmie, on utilise souvent une variante de la liste chaînée, la liste doublement chaînée :

{% aller %}
[La liste doublement chaînée](liste-doublement-chaînée){.interne}
{% endaller %}


## On s'entraîne

{% aller %}
[Projet : listes chaînées](./projet-listes-chaînées){.interne}
{% endaller %}

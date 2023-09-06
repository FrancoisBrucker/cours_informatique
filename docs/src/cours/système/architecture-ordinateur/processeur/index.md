---
layout: layout/post.njk

title: Processeur

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un processeur est composé de deux parties :

- les cores
- le system agent

{% info %}
Certains processeur possèdent également une carte graphique intégrée.
{% endinfo %}

![processeur](processeur.png)

Ces deux éléments communiquent via des bus permettant de transmettre 64b en parallèle (parfois plus).

{% aller %}
[Anatomie d'un bus](./bus){.interne}
{% endaller %}

Chaque core est une unité dont le but est de procéder à des calculs.

{% aller %}
[core](./core){.interne}
{% endaller %}

Les cores travaillent indépendamment mais nécessitent d'être au courant des voisins pour que tout fonctionne :

{% aller %}
[Interaction entre cores](./core){.interne}
{% endaller %}

> TBD redécouper [CPU](./CPU){.interne} ce qui précède.

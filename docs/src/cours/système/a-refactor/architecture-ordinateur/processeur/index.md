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

- les cores, liées entre eux par le ring (un bus de communication)
- le system agent

{% info %}
Certains processeurs possèdent également une carte graphique intégrée.
{% endinfo %}

![processeur](processeur.png)

Ces deux éléments communiquent via un bus permettant de transmettre 64b en parallèle (parfois plus).

{% aller %}
[Anatomie d'un bus](./bus)
{% endaller %}

Chaque [core](https://fr.wikipedia.org/wiki/Core_(microarchitecture)){.externe} est une unité de calcul dont le but est d'exécuter des instructions.

{% aller %}
[Anatomie d'un core](./core)
{% endaller %}

Les cores travaillent indépendamment mais nécessitent d'être au courant de ce que font les autres core pour que tout fonctionne :

{% aller %}
[Interaction entre cores](./plusieurs-cores)
{% endaller %}

> TBD redécouper [CPU](./CPU) ce qui précède.

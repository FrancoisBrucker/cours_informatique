---
layout: layout/post.njk 
title: Théorie

eleventyNavigation:
  key: Théorie
  parent: "Algorithme, code et théorie"
---

{% chemin %}
{%- for page in collections.all | eleventyNavigationBreadcrumb(eleventyNavigation.key, { includeSelf: true}) -%}
{% if not loop.first %} / {%endif%} [{{page.title}}]({{ page.url | url }})
{%- endfor -%}
{% endchemin %}

<!-- début résumé -->

Que peut ou pas faire un algorithme.

<!-- fin résumé -->

{% note %}
*L'informatique n'est pas plus la science des ordinateurs que l'astronomie n'est celle des télescopes* [E. Dijkstra](https://fr.wikipedia.org/wiki/Edsger_Dijkstra)
{% endnote %}

* [fonctions](fonctions)
* [complexité d'un problème](complexité-problème)
* [fonctions de hash](fonctions-hash)
* [machine de Turing](machine-turing)
* [décidabilité](decidabilite)
* [calculabilité](calculabilite)

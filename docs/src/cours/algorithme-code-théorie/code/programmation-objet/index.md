---
layout: layout/post.njk 
title: Programmation Objet

authors: 
  - François Brucker
  - Célia Châtel

eleventyNavigation:
  key: "Programmation Objet"
  parent: Code
---

{% chemin %}
{%- for page in collections.all | eleventyNavigationBreadcrumb(eleventyNavigation.key, { includeSelf: true}) -%}
{% if not loop.first %} / {%endif%} [{{page.title}}]({{ page.url | url }})
{%- endfor -%}
{% endchemin %}
{% prerequis "**Prérequis** :" %}

* [Base de la programmation]({{ "/cours/base-code/" | url }})
* [Mémoire et espace de noms](../mémoire-espace-noms/)

{% endprerequis %}

<!-- début résumé -->

Bases de programmation objet.

<!-- end résumé -->

1. [classes et objets](classes-et-objets)
2. [composition et agrégation](composition-agrégation)
3. [projet : composition et agrégation](projet-composition-agrégation)
4. [héritage](héritage)
5. [projet : héritage](projet-héritage)
6. [projet : TDD](projet-tdd)

---
layout: layout/post.njk 
title: Code

eleventyNavigation:
  key: Code
  parent: "Algorithme, code et théorie"
---

{% chemin %}
{%- for page in collections.all | eleventyNavigationBreadcrumb(eleventyNavigation.key, { includeSelf: true}) -%}
{% if not loop.first %} / {%endif%} [{{page.title}}]({{ page.url | url }})
{%- endfor -%}
{% endchemin %}

<!-- début résumé -->

Comment coder, maintenir et aimer ses programmes.

<!-- fin résumé -->

Les projets constituent une progression, il est conseillé de les suivre dans l'ordre.

1. [coder](coder)
2. [projet : hello dev](projet-hello-dev)
3. [projet : pourcentages](projet-pourcentages)
4. [projet : exponentiation](projet-exponentiation)
5. [projet : tris](projet-tris)
6. [mémoire et espace de noms](mémoire-espace-noms)
7. [programmation objets](programmation-objet)
8. [projet : programmation événementielle](projet-programmation-évènementielle)
9. [fichiers](fichiers)
10. [projet : alignement de séquences](projet-alignement-sequences)

---
layout: layout/post.njk 
title:  "Penser l'algorithmie"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD chapeau
>
> TBD chapeau commençons par un cas particulier, correspondant à l'arithmétique de Peano et utilisé par Godel pour démontrer ses théorèmes d'incomplétude.

{% aller %}
[Fonctions récursives primitives](./récursive-primitive){.interne}
{% endaller %}

Nous avons vu que les fonctions primitives récursives étaient des fonctions calculable. Nous allons montrer ici qu'un modèle plus générale, les fonctions récursives, sont équivalentes au pseudo-code ! Ceci montre que l'algorithmie peut posséder de nombreuses formes, toutes équivalentes.

{% aller %}
[Fonctions récursives](./fonctions-récursives){.interne}
{% endaller %}

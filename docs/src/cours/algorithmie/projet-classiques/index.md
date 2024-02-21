---
layout: layout/post.njk

title: Algorithmes classiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Algorithmes classiques dont l'intérêt est à la fois esthétique (ce sont de jolis algorithmes),
pratiques (ils mettent en oeuvre des techniques facilement réutilisables) et didactiques (trouver et prouver leurs fonctionnement vous fera progresser).

{% aller %}
[Suite de Fibonacci](fibonacci){.interne}
{% endaller %}

{% aller %}
[Noob trap](noob-trap){.interne}
{% endaller %}

{% aller %}
[Tours de Hanoi](tours-hanoi){.interne}
{% endaller %}

{% aller %}
[Suppression de valeurs](suppression-valeurs){.interne}
{% endaller %}

{% aller %}
[Suppression des doublons](suppression-doublons){.interne}
{% endaller %}

{% aller %}
[Compteur binaire](compteur-binaire){.interne}
{% endaller %}

{% aller %}
[Cols de listes et de matrices](cols){.interne}
{% endaller %}

{% aller %}
[Tris spéciaux](tris-spéciaux){.interne}
{% endaller %}

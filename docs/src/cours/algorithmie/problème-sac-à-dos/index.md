---
layout: layout/post.njk
title: Problème du sac à dos

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le problème du sac à dos est un problème fondamental en algorithmie, nombre de problèmes courant pouvant se modéliser sous cette forme.

> TBD mettre le python uniquement dans le projet et tout mettre en pseudo-code dans l'étude.
>
> TBD attention au départ de matrice à 0 pour dire aucun objet dans la programmation dynamique.
> faire la remontée propre car ils n'ont pas forcément vu l'alignement de séquences.
> TBD ecrire matrice et sous matrices optimales
> écrire les algos de remontée

## Étude

{% aller %}
[Étude](./étude){.interne}
{% endaller %}

## Projet

{% aller %}
[Projet](./projet){.interne}
{% endaller %}

## Pour aller plus loin

> TBD : cas particuliers simple : super croissant
>
> TBD : sac à dos avec répétition = programmation en nombre entier != de fractionnel car que des entiers comme découpage

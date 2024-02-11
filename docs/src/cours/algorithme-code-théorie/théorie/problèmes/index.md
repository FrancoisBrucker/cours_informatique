---
layout: layout/post.njk 
title:  "Problèmes"

eleventyNavigation:
    order: 3
    prerequis:
        - "../machine-turing/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> ici parler de pseudo-code (équivalent à machine de Turing)
> dire que selon thèse turing/church équivalent à algorithme

5. [Problèmes soluble par une machine de Turing](./problèmes-décidable){.interne}
6. [problèmes et complexité](./problèmes-NP){.interne}


> 1. ce à quoi sert un algorithme = résoudre un Problème
> 2. définition d'un problème
> 3. quels sont les problèmes que peut résoudre une machine ?
> décidable = problème
> problème vérifiable = ceux qui sont utiles
>
> pb vérifiable ont toujours une solution (une MT qui résout le problème) s'il existe un nombre infini de solutions possible (ie. s'il existe toujours une solution/certificat plus grand).

<https://perso.ens-lyon.fr/pierre.lescanne/PUBLICATIONS/calculabilite.pdf>

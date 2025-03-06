---
layout: layout/post.njk
title: "Structures de dictionnaires"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Tableau associatifs

Aussi appelé dictionnaires

{% aller %}
[fonction de hachage](fonctions-hash){.interne}
{% endaller %}
{% aller %}
[tableau associatif](tableau-associatif){.interne}
{% endaller %}

## Variantes

> TBD ensembles

## Exercices

> TBD ajouter exos pour dictionnaires.
> TBD 2-SUM $T[i] + T[j] = 0$ en $\mathcal{O}(n)$ en moyenne avec dico. Ne change rien pour 3-SUM, il faut le faire n fois.
>
> TBD pas toujours la meilleur solution le dico : faire lièvre et lapin (qu'on aura vu dans algo classiques) pour deux tableaux avec égalité mieux que dictionnaire.

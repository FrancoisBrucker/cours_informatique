---
layout: layout/post.njk 
title:  "Machine de Turing"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La [machine de Turing](https://fr.wikipedia.org/wiki/Machine_de_Turing) est une façon simple d'implémenter les [4 règles générales d'un algorithme](../../définition#règles-générales){.interne}, vous verrez que supprimer une des possibilités de la machine et plus rien ne fonctionne.
Cependant,  Turing lui-même a montré que sa machine permettait exactement de calculer tout ce qu'on peut faire avec un [pseudo-code](../pseudo-code){.interne} (on en donnera une idée de preuve).
Enfin, toutes les tentatives de généralisation de son modèle se sont révélés infructueuses : on arrive pas à calculer plus de choses qu'avec la machine de Turing (c'est juste plus simple de le faire).

{% lien %}
[L'article où d'Allan Turing décrit cette machine](https://www.espace-turing.fr/IMG/pdf/turing_paper_1936.pdf)
{% endlien %}

## Définitions

[définition](./définition){.interne}

## Compositions de machines

[Composition de machine](./composition){.interne}

## Définitions alternatives

2. [définitions alternatives](./définitions-alternatives){.interne}

## MTU

Machine de Turing universelle

1. [Équivalence entre pseudo-code et machine de Turing](./pseudo-code){.interne}
2. [Castors affairés](./castors-affairés){.interne}

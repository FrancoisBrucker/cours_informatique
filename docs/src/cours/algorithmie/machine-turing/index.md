---
layout: layout/post.njk 
title:  "Machine de Turing"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La [machine de Turing](https://fr.wikipedia.org/wiki/Machine_de_Turing) est une façon simple d'implémenter les [4 règles générales d'un algorithme](../définition#règles-générales){.interne}. Turing lui-même a montré que sa machine permettait exactement de calculer tout ce qu'on peut faire avec un [pseudo-code](../pseudo-code){.interne} (on en donnera une idée de preuve). De plus, toutes les tentatives de généralisation de son modèle se sont révélés infructueuses : on arrive pas à calculer plus de choses qu'avec la machine de Turing (c'est juste plus simple de le faire).

On peut même montrer qu'une machine de Turing est elle même équivalent à un ordinateur !

La force d'une machine de Turing est qu'il n'y a rien (modèle très simple) et pourtant il y a tout (on peut tout calculer).

{% lien %}
L'article où d'Allan Turing décrit cette machine est [là](https://www.espace-turing.fr/IMG/pdf/turing_paper_1936.pdf)
{% endlien %}

1. [définition et premières manipulations](./définition){.interne}
2. [définitions alternatives](./définitions-alternatives){.interne}
3. [Équivalence entre pseudo-code et machine de Turing](./pseudo-code){.interne}
4. [Castors affairés](./castors-affairés){.interne}
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

{% aller %}
[définitions](./définitions){.interne}
{% endaller %}

## Compositions de machines

Écrire un programme en machine de Turing (c'est à dire écrie des fonctions de transitions) peut être pénible, nous décrivons dans cette partie quelques [sucres syntaxiques](https://fr.wikipedia.org/wiki/Sucre_syntaxique) permettant d'obtenir toutes les structures de contrôle d'un pseudo-assembleur (séquentialité, saut et saut conditionnel) :

{% aller %}
[Composition de machines](./composition){.interne}
{% endaller %}

## Définitions alternatives

La machine de Turing permet, avec son fonctionnement très simple sous la forme de fonction de transition, d'avoir autant de structures de contrôle que le pseudo-assembleur. Pour terminer de montrer que la machine de Turing permet de faire tout ce que le pseudo-assembleur permet il faut montrer que le ruban et le fait de ne pouvoir bouger que d'une seule case à la fois  n'est pas gênant.

{% aller %}
[Définitions alternatives](./définitions-alternatives){.interne}
{% endaller %}

## MTU

La machine de Turing vient avec son propre processeur. C'est à la fois un programme et un ordinateur. La machine qui fait office d'ordinateur est appelé machine de Turing universelle :

{% aller %}
[Machine de Turing Universelle](./mtu){.interne}
{% endaller %}

## Castors affairés

La plus célèbre des fonctions non calculables. On n'en parle que maintenant parce qu'elle est définie grâce aux Machines de Turing.

{% aller %}
[Castors affairés](./castors-affairés){.interne}
{% endaller %}

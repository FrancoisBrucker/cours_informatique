---
layout: layout/post.njk 
title:  "Penser l'algorithmie"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Playlist sur la _theory of computation_](https://www.youtube.com/watch?v=bP1lOm5rLsI&list=PLwF3A0R8OzMpO6_9WbT1kK16akYFh3_Nt&index=1) et [le livre associé](https://hefferon.net/computation/)

{% endlien %}

## Fonctions récursives

{% aller %}
[Fonctions récursives primitives](./récursive-primitive){.interne}
{% endaller %}

Nous avons vu que les fonctions primitives récursives étaient des fonctions calculable. Nous allons montrer ici qu'un modèle plus générale, les fonctions récursives, sont équivalentes au pseudo-code ! Ceci montre que l'algorithmie peut posséder de nombreuses formes, toutes équivalentes.

{% aller %}
[Fonctions récursives](./fonctions-récursives){.interne}
{% endaller %}

## Lambda calcul

Le lambda calcul est encore une autre forme de calcul équivalent aux machines de Turing. On doit ce modèle à Church, qui était le directeur de thèse de Turing. C'est une version bien plus _matheuse_ de l'algorithmie puisqu'elle ne s'intéresse qu'aux fonctions et ne parle jamais d'algorithme.

On peut cependant coder en lambda calcul, c'est ce qu'on appelle la programmation fonctionnelle et elle est possible avec des langages comme le [Haskell](https://www.haskell.org/) (il en existe d'autres, comme le [Ocaml](https://ocaml.org/) par exemple).

{% lien %}

Pour apprendre Haskell et les langages fonctionnels :

1. <https://github.com/system-f/fp-course>
2. <https://haskell.mooc.fi/>
3. <https://www.youtube.com/playlist?list=PLF1Z-APd9zK7usPMx3LGMZEHrECUGodd3>
4. [introduction au langage Haskell](https://www.youtube.com/watch?v=UhM_H3lFk_Q) et au [lambda calcul](https://www.youtube.com/watch?v=_n4LIt2WPzE)
5. [playlist](https://www.youtube.com/watch?v=Vgu82wiiZ90&list=PLe7Ei6viL6jGp1Rfu0dil1JH1SHk9bgDV)
6. <https://learnyouahaskell.com/>

{% endlien %}

Cette façon de programmer est très liée aux types et a permis quelques avancées dans la vérification automatique des types.

{% lien %}

- [Catégories et types](https://bartoszmilewski.com/2014/10/28/category-theory-for-programmers-the-preface/)
- [preuve de programme et types](https://ncatlab.org/nlab/show/computational+trilogy)
{% endlien %}

## Automates cellulaires

La plupart des [automates cellulaires](https://fr.wikipedia.org/wiki/Automate_cellulaire) sont Turing-complet. C'est le cas du célèbre [jeu de la vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie), mais aussi d'automates bien plus simple :

{% lien %}
L'exemple de système Turing complet le plus simple que je connaisse est l'automate uni-dimensionnel respectant la [règle 110](https://en.wikipedia.org/wiki/Rule_110).

Jetez-y un coup d'œil, c'est assez bluffant.
{% endlien %}

## Langages exotiques

Si la plupart des langages informatiques sont clairement Turing complet, il existe des langages bizarres, nommé [langages de programmation exotiques](https://fr.wikipedia.org/wiki/Langage_de_programmation_exotique), qui sont aussi Turing complet. Ces langages tendent à être minimalistes et cherchent à posséder soit le nombre minimal d'instruction, comme le célèbre [brainfuck](https://www.google.com/search?q=brainfuck), ou à être marrant, comme le [Piet](https://www.dangermouse.net/esoteric/piet.html) dont le but est de créer des programmes sous la forme d'un tableau de [Piet Mondrian](https://fr.wikipedia.org/wiki/Piet_Mondrian).

## Autres trucs

{% lien %}
- [Legend of Zelda: Tears of the Kingdom](https://www.youtube.com/watch?v=5u6BN1p0Uo8)
- [Powerpoint](https://www.youtube.com/watch?v=uNjxe8ShM-8)
- [règle 110 avec Factorio (et des trains)](https://www.youtube.com/watch?v=NCC2Fd8qxv4)
{% endlien %}

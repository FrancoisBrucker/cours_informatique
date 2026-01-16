---
layout: layout/post.njk 
title:  "Autres modèles de création d'algorithme"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous ne rentrerons pas dans les détails ici, nous voulons juste montrer que l'on peut très bien écrire des algorithmes en utilisant autre chose que du pseudo-code. En revanche tous les modèles que nous verrons ne peuvent pas coder plus de choses, ils permettent juste d'écrire différemment les mêmes algorithmes.

Les algorithmes écrit sous la forme de pseudo-code sont équivalents (on le verra) aux algorithmes écrits grâce à une machine de Turing. Les modèles équivalents sont alors dit **_Turing complet_** :

{% note "**définition**" %}
Un système est dit [Turing complet](https://fr.wikipedia.org/wiki/Turing-complet) s'il permet de faire tout ce qu'un pseudo-code peut faire.
{% endnote %}

Avoir un modèle Turing Complet nous assure, en suivant la thèse de Church-Turing, que ce modèle peut calculer tous les algorithmes.

## Lambda calcul

Le lambda calcul est une autre forme d'écriture équivalent au pseudo-code. On doit ce modèle à Church, qui était le directeur de thèse de Turing. C'est une version bien plus _matheuse_ de l'algorithmie puisqu'elle ne s'intéresse qu'aux fonctions et ne parle jamais d'algorithme.

On peut cependant coder en lambda calcul, c'est ce qu'on appelle la programmation fonctionnelle et elle est possible avec des langages comme le [Haskell](https://www.haskell.org/) (il en existe d'autres, comme le [Ocaml](https://ocaml.org/) par exemple (n')utilisé (qu')en prépa).

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

Ne nombreuses applications ou jeux sont Turing-complet par inadvertence. Par exemple :

- [Legend of Zelda: Tears of the Kingdom](https://www.youtube.com/watch?v=5u6BN1p0Uo8)
- [Powerpoint](https://www.youtube.com/watch?v=uNjxe8ShM-8)
- [règle 110 avec Factorio (et des trains)](https://www.youtube.com/watch?v=NCC2Fd8qxv4)
- [fractran](https://www.youtube.com/watch?v=GIPtnEIQCBM) et <https://fr.wikipedia.org/wiki/FRACTRAN>

> TBD faire un dm Fractran : <https://math.univ-lyon1.fr/~roblot/resources/factorisation.pdf> <https://www.math.univ-paris13.fr/~boyer/enseignement/crypto/Chap6.pdf>(avec dichotomie) et division euclidienne. Voir si ça fonctionne en python avant des entiers aussi grand qu'on veut
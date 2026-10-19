---
layout: layout/post.njk

title: "Thèse de Church-Turing"

eleventyComputed:  
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Le pseudo-code permet d'écrire des programmes sur papier que l'on peut exécuter dans sa tête aidé d'un papier et d'un crayon. Les langages de programmation permettent d'exécuter du code sur un ordinateur un utilisant [un langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation){.externe}.

Pour la plupart d'entre eux, il est facile de transcrire le pseudo-code en code pouvant être exécuté, on a alors l'implication suivante :

{% note "**Proposition**" %}
Tout ce qui peut s'écrire en pseudo-code peut s'exécuter sur un ordinateur.
{% endnote %}

La réciproque n'est pas prouvée mais de nombreux indices (nous en verrons plusieurs dans la seconde partie de ce cours) tendent à penser que c'est vrai. On supposera donc vrai la proposition suivante, communément admise :

{% note "**Thèse de Church-Turing**" %}
Les notions d'algorithme et de pseudo-code sont équivalentes : tout algorithme peut être écrit en pseudo-code.
{% endnote %}
{% lien %}
[Thèse de Church-Turing](https://fr.wikipedia.org/wiki/Th%C3%A8se_de_Church){.externe}.
{% endlien %}

La thèse de Church-Turing a été initialement formulée pour les Machines de Turing mais (nous le verrons bien plus tard) pseudo-code et machines de Turing sont deux notions équivalentes. Notez que cette affirmation n'est pas démontrée mais que toutes les tentatives (et il y en a eu) pour infirmer cette affirmation ont été des échecs.

{% lien %}

Voir [cette excellente vidéo d'Arte](https://www.youtube.com/watch?v=Zci9m08HQws){.externe} pour une introduction en douceur à la problématique.

{% endlien %}

Le modèle du pseudo-code n'est pas la seule façon d'écrire des algorithmes. La célèbre machine de Turing que l'on verra bien plus tard en est un exemple. Mais il y en a beaucoup, beaucoup d'autres tous équivalent entre eux. Nous ne rentrerons pas dans les détails ici, nous voulons juste montrer que l'on peut très bien écrire des algorithmes en utilisant autre chose que du pseudo-code. En revanche tous les modèles que nous verrons ne peuvent pas coder plus de choses, ils permettent juste d'écrire différemment les mêmes programmes.

Les programmes écrit sous la forme de pseudo-code sont équivalents (on le verra) aux algorithmes écrits grâce à une machine de Turing. Les modèles équivalents sont alors dit **_Turing complet_** :

{% definition %}
Un système est dit [Turing complet](https://fr.wikipedia.org/wiki/Turing-complet){.externe} si tout programme du système peut s'écrire en pseudo-code et réciproquement.
{% enddefinition %}

Avoir un modèle Turing Complet nous assure, en suivant la thèse de Church-Turing, que ce modèle peut calculer tous les algorithmes.

## Lambda calcul

Le lambda calcul est une autre forme d'écriture équivalent au pseudo-code. On doit ce modèle à Church, qui était le directeur de thèse de Turing. C'est une version bien plus _matheuse_ de l'algorithmie puisqu'elle ne s'intéresse qu'aux fonctions et ne parle jamais d'algorithme.

On peut cependant coder en lambda calcul, c'est ce qu'on appelle la programmation fonctionnelle et elle est possible avec des langages comme le [Haskell](https://www.haskell.org/){.externe} (il en existe d'autres, comme le [Ocaml](https://ocaml.org/){.externe} par exemple (n')utilisé (qu')en prépa).

{% lien %}

Pour apprendre Haskell et les langages fonctionnels :

1. <https://github.com/system-f/fp-course>{.externe}
2. <https://haskell.mooc.fi/>{.externe}
3. <https://www.youtube.com/playlist?list=PLF1Z-APd9zK7usPMx3LGMZEHrECUGodd3>{.externe}
4. [introduction au langage Haskell](https://www.youtube.com/watch?v=UhM_H3lFk_Q){.externe} et au [lambda calcul](https://www.youtube.com/watch?v=_n4LIt2WPzE){.externe}
5. [playlist](https://www.youtube.com/watch?v=Vgu82wiiZ90&list=PLe7Ei6viL6jGp1Rfu0dil1JH1SHk9bgDV){.externe}
6. <https://learnyouahaskell.com/>{.externe}

{% endlien %}

Cette façon de programmer est très liée aux types et a permis quelques avancées dans la vérification automatique des types.

{% lien %}

- [Catégories et types](https://bartoszmilewski.com/2014/10/28/category-theory-for-programmers-the-preface/){.externe}
- [preuve de programme et types](https://ncatlab.org/nlab/show/computational+trilogy){.externe}
{% endlien %}

## Automates cellulaires

La plupart des [automates cellulaires](https://fr.wikipedia.org/wiki/Automate_cellulaire){.externe} sont Turing-complet. C'est le cas du célèbre [jeu de la vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie){.externe}, mais aussi d'automates bien plus simple :

{% lien %}
L'exemple de système Turing complet le plus simple que je connaisse est l'automate uni-dimensionnel respectant la [règle 110](https://en.wikipedia.org/wiki/Rule_110){.externe}.

Jetez-y un coup d'œil, c'est assez bluffant.
{% endlien %}

## Langages exotiques

Si la plupart des langages informatiques sont clairement Turing complet, il existe des langages bizarres, nommé [langages de programmation exotiques](https://fr.wikipedia.org/wiki/Langage_de_programmation_exotique){.externe}, qui sont aussi Turing complet. Ces langages tendent à être minimalistes et cherchent à posséder soit le nombre minimal d'instructions comme le célèbre [Brainfuck](https://www.google.com/search?q=brainfuck){.externe}, à être marrant comme le [Piet](https://www.dangermouse.net/esoteric/piet.html){.externe} dont le but est de créer des programmes sous la forme d'un tableau de [Piet Mondrian](https://fr.wikipedia.org/wiki/Piet_Mondrian){.externe} ou encore à faire des ponts entre disciplines comme le [Fractran](https://www.youtube.com/watch?v=GIPtnEIQCBM){.externe}.

## Turing complet par inadvertence

Ne nombreuses applications ou jeux sont Turing-complet par inadvertence. Par exemple :

- [Legend of Zelda: Tears of the Kingdom](https://www.youtube.com/watch?v=5u6BN1p0Uo8){.externe}
- [Powerpoint](https://www.youtube.com/watch?v=uNjxe8ShM-8){.externe}
- [Les trains de Factorio](https://www.youtube.com/watch?v=NCC2Fd8qxv4){.externe}





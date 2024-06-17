---
layout: layout/post.njk

title: Algorithmie
tags: ["cours", "algorithmie"]
authors:
  - François Brucker

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Cours d'algorithmie.

{% info %}
_L'informatique n'est pas plus la science des ordinateurs que l'astronomie n'est celle des télescopes_ [E. Dijkstra](https://fr.wikipedia.org/wiki/Edsger_Dijkstra)
{% endinfo %}

Il est conseillé pour ce cours d'avoir des bases de programmation en python. Pour apprendre vous pouvez vous reporter au cours [coder et développer](/cours/coder-et-développer).

## Algorithmes et programmes

### <span id="bases-théoriques"></span>Bases théoriques

{% aller %}
[Bases théoriques](./bases-théoriques){.interne}
{% endaller %}

### <span id="écrire-algorithmes"></span>Écrire des algorithmes pour résoudre des problèmes

{% aller %}
[Écrire des algorithmes](./écrire-algorithmes){.interne}
{% endaller %}

{% aller %}
[Écrire du code](./écrire-code){.interne}
{% endaller %}

### Autres modèles

L'écriture d'algorithmes sous la forme de pseudo-code n'est qu'une des nombreuses façon d'en écrire. Nous allons en voir 4 toutes équivalentes les unes avec les autres !

>
> TBD : Turing vers formule SAT.
> donc algorithme = formule logique.

> TBD en pratique : Algo = ordinateur = modèle de von Neumann
>
> TBD : séparer modèle et MTU qui permet de simuler dans le modèle. C'est le principe d'un ordinateur.
> TBD encore d'autres ! jeu de la vie, ...

#### Machines de Turing

> TBD :
>
> 1. pseudo-code = algorithme : thèse de Church/Turing
> 2. uniquement binaire
> 3. pas besoin de :
>   - séparer variables et mémoire
>   - de RAM juste se déplacer de 1
>   - code, juste des états
> 4. on est arrivé à la Machine de Turing. Donc code ≤ Turing
> 5. comme on peut simuler ue machine de Turing avec un algo : Turing ≤ code

> TBD : ne garder que la machine à 1 ruban ici.

Cette partie est là pour vous montrer que pseudo-code et machines de Turing sont deux notions équivalentes. On aura également besoin des machines de Turing bien plus tard, lorsque nous rencontrerons les classes de problèmes.

{% aller %}
[Machines de Turing](./machine-turing){.interne}
{% endaller %}

#### Lambda calcul

> TBD : pour les matheux qui veulent s'encanailler à faire de l'informatique
> Catégories et types : <https://bartoszmilewski.com/2014/10/28/category-theory-for-programmers-the-preface/>, <https://ncatlab.org/nlab/show/computational+trilogy>
> <https://www.youtube.com/watch?v=_n4LIt2WPzE>
> Maths : <https://www.paultaylor.eu/~pt/prafm/index.html>
> <https://www.haskell.org/> :
>
> - intro : <https://www.youtube.com/watch?v=UhM_H3lFk_Q>
> - playlist <https://www.youtube.com/watch?v=Vgu82wiiZ90&list=PLe7Ei6viL6jGp1Rfu0dil1JH1SHk9bgDV>
> - livre : <https://learnyouahaskell.com/>

#### Automates cellulaires

> TBD : Jeu de la vie
> TBD : <https://fr.wikipedia.org/wiki/Automate_cellulaire#R%C3%A8gle_110>

#### Équivalence des différentes approches

> TBD : à supprimer de la partie sur les machines de Turing et à mettre ici.
> TBD MTU = langage universel
> TBD : brainfuck et interpréteur en python. Permet de parler de machine de Turing universelle

## On s’entraîne

> TBD : écrire des algos pour résoudre des problèmes.
> TBD essence même d'un algorithme c'est la boucle et les if/them/else
> sinon fait tout le temps la même chose (addition, etc). Le problème est de transformer une idée en code et en succession logique d'arguments (conditions) et d'action (instruction) tant que ce n'est pas résolu (boucles).
>
>
> 1. exos simples avec 1 boucle puis 2 boucles imbriquées (compter le nb d’occurrences,  suppression de doublons, etc)
> 2. dichotomie
> 3. récursion et pile d'appel (tours de hanoï ; min et max d'un tableau)
> 4. plusieurs boucles a la suite
> 5. récursion et boucles
>
> exemples :
>
> - <https://www.youtube.com/watch?v=pKO9UjSeLew>
>

## Complexités

Cette partie s'intéresse à la notion de complexités pour un algorithme et un problème.

{% aller %}
[Calcul de complexité d'un algorithme](./complexité-calculs){.interne}
{% endaller %}
{% aller %}
[Complexité d'un problème algorithmique](./complexité-problème){.interne}
{% endaller %}

La notion de complexité est centrale en algorithmie, nous en reparlerons encore plus tard dans le cours.

## On s'entraîne : problèmes liés à l'exponentiation

{% aller %}
[Calculer $x^y$](./projet-exponentiation){.interne}
{% endaller %}
{% aller %}
[Les suites additives](./projet-suite-additive){.interne}
{% endaller %}

## Complexité en moyenne

{% aller %}
[Complexité en moyenne](./complexité-moyenne){.interne}
{% endaller %}

## Problème du tri

{% aller %}
[Problème du tri](./problème-tris){.interne}
{% endaller %}

## On s'entraîne : exercices de complexité et de preuve

{% aller %}
[Algorithmes classiques](./projet-classiques){.interne}
{% endaller %}

## Structures linéaires

{% aller %}
[Chaines de caractères](./structure-chaine-de-caractères){.interne}
{% endaller %}
{% aller %}
[Conteneurs](./structure-conteneurs){.interne}
{% endaller %}

> TBD ajouter exos pour dictionnaires.

## Complexité amortie

> TBD A déplacer plus tard. Attention à l'amortie des dict/liste.

{% aller %}
[Complexité amortie](./complexité-amortie){.interne}
{% endaller %}

## Design d'algorithmes

{% aller %}
[Design d'algorithmes](./design-algorithmes){.interne}
{% endaller %}

## Problème du "sac à dos"

> TBD Intro NP et NPC. Doit tenir 2h pour montrer pourquoi NP = problème algo et réduction simple (max ≤ tri ≤ SAT (admis) = 3-sat (le faire)).
> TBD : Laisser les démos pour plus tard.

{% aller %}
[Problème du sac à dos](./problème-sac-à-dos){.interne}
{% endaller %}

> TBD : ici stop partie I. Ensuite Partie II.

## Classes de Problèmes Algorithmiques

> TBD A déplacer plus tard.

{% aller %}
[Classes de problèmes algorithmiques](./classes-problèmes){.interne}
{% endaller %}

## Désordre et hasard

{% aller %}
[Mélanger un tableau](./projet-mélange){.interne}
{% endaller %}

> TBD nombre aléatoires

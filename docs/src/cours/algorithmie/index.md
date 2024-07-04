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

> Dire que algo = au tableau/papier et pour les humains. Deux branches ensuite : exécution sur un ordinateur/réfléchir à la nature même de l'algorithmie (Turing). Selon ce qu'on voudra faire on utilisera l'un ou l'autre des formalismes. Nous Algo et on laisse la machine (le python) transcrire en langage machine pour être exécuté. Penser les algo se fera plus tard, mais on vous montre juste le modèle, archi connu : la machine de Turing.

### Exécuter des programmes

{% aller %}
[Exécuter des programmes](./exécuter-code){.interne}
{% endaller %}

### Penser l'algorithmie

> TBD : Turing.
> faire Fibonacci avec une machine de Turing.
> dire que structure de donnée = code et que l'on a besoin de rien comme outil pour exécuter du code : juste une façon de stocker et une façon d'écrire conditionnellement. Le code est LOCAL.

{% aller %}
[Penser l'algorithmie](){.interne}
{% endaller %}

## On s'entraîne

Écrire des algorithmes simples en pseudo-code (ou en python) pour résoudre des problèmes algorithmiques.

> TBD : écrire des algos pour résoudre des problèmes.
> TBD essence même d'un algorithme c'est la boucle et les if/them/else
> sinon fait tout le temps la même chose (addition, etc). Le problème est de transformer une idée en code et en succession logique d'arguments (conditions) et d'action (instruction) tant que ce n'est pas résolu (boucles).
>
>
> 1. exos simples avec 1 boucle puis 2 boucles imbriquées (compter le nb d’occurrences,  suppression de doublons, max tableau, etc)
> 2. dichotomie
> 3. récursion et pile d'appel (tours de hanoï ; min et max d'un tableau)
> 4. plusieurs boucles a la suite
> 5. récursion et boucles
>
> voir les parties complexité et remettre si possible les réponse dans cette partie.
>
> exemples :
>
> - <https://www.youtube.com/watch?v=pKO9UjSeLew>

### Algorithmes itératif

### Algorithmes récursif

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

> TBD Intro NP et NPC. Doit tenir 2h pour montrer pourquoi NP = problème algo et réduction simple (max ≤ tri ; en trouver un autre.
> on a égalité si ≤ et ≥. Faire exemple simple puis faire SAT = 3-sat (le faire)).
>
> question P ≤ NP ouverte.
> 
> TBD : Dire, mais laisser la démo pour plus tard, que SAT est supérieur à tout.
> tbf montrer dans la partie sac à dos qu'il est inf à sat.
> ici exemple de problème pas dans P (on ne sais pas)

{% aller %}
[Problème du sac à dos](./problème-sac-à-dos){.interne}
{% endaller %}

> TBD : ici stop partie I. Ensuite Partie II.

## Classes de Problèmes Algorithmiques

> TBD Nouvelle partie en algo.

{% aller %}
[Classes de problèmes algorithmiques](./classes-problèmes){.interne}
{% endaller %}

> Ici fion théorique = Turing et NPC avec SAT.

#### Machines de Turing

> TBD :
> passer de pseudo-assembleur à turing :
>
> - opérations (ok, juste bits)
> - code vers transitions
> - ruban unique (registre)
> - pointeur unique
> - RAM vers décalage de 1
>
> Code de Von Neuman = MTU
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

## Autres modèles

L'écriture d'algorithmes sous la forme de pseudo-code n'est qu'une des nombreuses façon d'en écrire. Nous allons en voir 4 toutes équivalentes les unes avec les autres !

>
> TBD : Turing vers formule SAT.
> donc algorithme = formule logique.

>
> TBD : séparer modèle et MTU qui permet de simuler dans le modèle. C'est le principe d'un ordinateur.
> TBD encore d'autres ! jeu de la vie, ...


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

## Désordre et hasard

{% aller %}
[Mélanger un tableau](./projet-mélange){.interne}
{% endaller %}

> TBD nombre aléatoires

## Enveloppes convexes

{% aller %}
[Problème de l'enveloppe convexe](./enveloppes-convexes){.interne}
{% endaller %}

> TBD nombre aléatoires

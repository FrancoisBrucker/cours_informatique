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

### Autres modèles

L'écriture d'algorithmes sous la forme de pseudo-code n'est qu'une des nombreuses façon d'en écrire. Nous allons en voir 4 toutes équivalentes les unes avec les autres !

> TBD : séparer modèle et MTU qui permet de simuler dans le modèle. C'est le principe d'un ordinateur.

#### Langages informatiques

> TBD : le plus clair car le pseudo code s'écrit presque directement, par exemple en python
> TBD pas exécuté directement. Traduit en un autre langage compréhensible par ce qui va l'exécuter. 
> TBD : compilé en langage machine (montrer des exemples). Souvent actuellement en byte code (module dis en python pour le voir <https://docs.python.org/fr/3/library/dis.html> ou <https://www.fevrierdorian.com/carnet/pages/python-sous-le-capot-chapitre-1-fonctionnement-de-la-vm-cpython.html>) qui est lui-même exécuté par une machine virtuelle.

#### Circuits logique

> tout est basé sur les opérations booléennes, logiques car algorithme = fonction booléenne.

> <https://people.csail.mit.edu/rrw/week1.pdf>
> <https://cs.brown.edu/people/jsavage/book/pdfs/ModelsOfComputation_Chapter9.pdf>
> sert pour la dé-randomisation : <https://www.youtube.com/watch?v=mZck0N_T9Cs>
> 
> Gros : <https://en.wikipedia.org/wiki/Circuit_complexity#History>
> TBD circuit logiques ?

#### Modèle de Von Neumann

> TBD : le langage de la machine
>

#### Machines de Turing

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
> - intro : <https://www.youtube.com/watch?v=UhM_H3lFk_Q>
> - playlist <https://www.youtube.com/watch?v=Vgu82wiiZ90&list=PLe7Ei6viL6jGp1Rfu0dil1JH1SHk9bgDV>
> - livre : <https://learnyouahaskell.com/>

#### Automates cellulaires

> TBD : Jeu de la vie
> TBD : <https://fr.wikipedia.org/wiki/Automate_cellulaire#R%C3%A8gle_110>

#### Équivalence des différentes approches

> TBD : à supprimer de la partie sur les machines de Turing et à mettre ici.
> TBD MTU = langage universel
> TBD : brainfuck et interpréteur en python. Permet de parler de machine de turing universelle

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

## Complexité amortie

{% aller %}
[Complexité amortie](./complexité-amortie){.interne}
{% endaller %}

## Design d'algorithmes

{% aller %}
[Design d'algorithmes](./design-algorithmes){.interne}
{% endaller %}

## Problème du "sac à dos"

{% aller %}
[Problème du sac à dos](./problème-sac-à-dos){.interne}
{% endaller %}

## Classes de Problèmes Algorithmiques

{% aller %}
[Classes de problèmes algorithmiques](./classes-problèmes){.interne}
{% endaller %}


## Désordre et hasard

{% aller %}
[Mélanger un tableau](./projet-mélange){.interne}
{% endaller %}

> TBD nombre aléatoires


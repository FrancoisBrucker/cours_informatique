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

Commençons par définir ce qu'est un algorithme et ce qu'il peut ou ne peut pas faire :

{% aller %}
[Bases théoriques](./bases-théoriques){.interne}
{% endaller %}

On peut maintenant définir une grammaire permettant décrire des algorithmes sous la forme de pseudo-code et s'en servir pour résoudre des problèmes :

{% aller %}
[Écrire des algorithmes](./écrire-algorithmes){.interne}
{% endaller %}

Le pseudo-code ressemble à un langage de programmation comme le python que l'on peut exécuter sur un ordinateur. Voyons comment ceci est possible :

{% aller %}
[Exécuter du code](./exécuter-code){.interne}
{% endaller %}

Maintenant que l'on sait comment écrire des algorithmes en pseudo-code et que l'on peut les compiler (automatiquement) en assembleur pour être (également automatiquement) exécuté sur un ordinateur. Il nous reste une voie à explorer, la voie théorique qui nous permettra d'extraire les lois fondamentale de l'algorithmique pour penser l'informatique :

{% aller %}
[Penser l'algorithmie](./penser-algorithmie){.interne}
{% endaller %}

## On s'entraîne : itératif vs récursif

> TBD : à faire propre

{% aller %}
[exercices : itératif et récursif](./projet-itératif-récursif){.interne}
{% endaller %}

## Complexités

Cette partie s'intéresse à la notion de complexités pour un algorithme et un problème.

{% aller %}
[Calcul de complexité d'un algorithme](./complexité-calculs){.interne}
{% endaller %}
{% aller %}
[Complexité d'un problème algorithmique](./complexité-problème){.interne}
{% endaller %}

La notion de complexité est centrale en algorithmie, nous en reparlerons encore plus tard dans le cours.

## On s'entraîne

> TBD reprendre les exos d'avant avec calcul de complexité.

## projet : problèmes liés à l'exponentiation

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

> TBD faire un lien avec les exos vu en écriture d'algo + complexité pour que tout soit aussi là.

## Structures linéaires

### Conteneurs

{% aller %}
[Conteneurs](./structure-conteneurs){.interne}
{% endaller %}

> TBD ajouter exos pour dictionnaires.

### Chaînes de caractères

> TBD on a déjà utilisé les chaines de caractères à de nombreuses reprise. Nous allons maintenant pouvoir étudier plus attentivement. Comme les algo sont de 01* à 01*, c'est une structure fondamentale pour penser l'algorithmie et comme tout est écrit, en particulier le code, elles sont au centre de nombreux problèmes courant.

{% aller %}
[Chaines de caractères](./structure-chaine-de-caractères){.interne}
{% endaller %}

## Design d'algorithmes

> TBD reprendre les algos d'avant et les classer dans les cases.

{% aller %}
[Design d'algorithmes](./design-algorithmes){.interne}
{% endaller %}

## Enveloppes convexes

{% aller %}
[Problème de l'enveloppe convexe](./enveloppes-convexes){.interne}
{% endaller %}

## Réductions : passer d'un problème à un autre

> TBD dire qu'on a vue que tri est plus simple que l'enveloppe donc de complexité supérieure. On explore ces transformations de problèmes algo en d'autres.

{% aller %}
[réduction de problèmes](./problème-réduction){.interne}
{% endaller %}

## Problème du "sac à dos"

> TBD premier problème dur : montrer que plus dur que SAT. Le rajouter.

{% aller %}
[Problème du sac à dos](./problème-sac-à-dos){.interne}
{% endaller %}

## Classes de Problèmes Algorithmiques

> tbd montrer dans la partie sac à dos qu'il est inf à sat.
> ici exemple de problème pas dans P (on ne sait pas)
> pb de décision
> question P (soluble) ≤ NP (vérifiable) ouverte.

> TBD cook
> TBD pbs de décision
> TBD 2-sat facile et 3-sat impossible.

{% aller %}
[Classes de problèmes algorithmiques](./classes-problèmes){.interne}
{% endaller %}

> TBD : montrer l'algorithme universel qui résout tout en temps optimal si on a un certificat. <https://www.youtube.com/watch?v=9ONm1od1QZo>
> 
> TBD : ici stop partie I. Ensuite Partie II.

## Complexité amortie

> TBD A déplacer plus tard. Attention à l'amortie des dict/liste.

{% aller %}
[Complexité amortie](./complexité-amortie){.interne}
{% endaller %}

## Désordre et hasard

{% aller %}
[Mélanger un tableau](./projet-mélange){.interne}
{% endaller %}

> TBD nombre aléatoires

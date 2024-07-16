---
layout: layout/post.njk 
title:  "Penser l'algorithmie"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le pseudo-code permet de concevoir des algorithmes pouvant être exécutés au tableau par des humains. L'assembleur quant à lui, language de la machine, permet d'exécuter des algorithmes sur des processeurs.
Pseudo-code et assembleurs sont équivalents : les problèmes que l'on peut résoudre avec l'un sont également résoluble avec l'autre (et réciproquement). On peut même transcrire en assembleur un programme écrit en pseudo-code de façon automatique (on a évoqué sans rentrer dans les détails les moyens d'y parvenir) il est donc courant d'écrire son code en pseudo-code, facile à lire et à maintenir, puis de laisser un compilateur le transcrire en assembleur pour être exécuté.

Cependant pour penser l'algorithmie, c'est à dire étudier ce qui peut ou ne peut pas être résoluble par le calcul, pseudo-code et assembleur sont encore trop _riches_ (on peut aller n'importe où dans la mémoire par exemple, on suppose l'existence de la fonction `NAND`{.language-}, etc). Il ne faut conserver que les éléments indispensables pour pouvoir écrire tout ce que l'on peut faire en pseudo-code.

C'est ce que propose Turing avec sa célèbre Machine : une base théorique minimale de ce qu'est l'informatique.

## Machine de Turing

{% aller %}
[Machine de Turing](./machine-turing){.interne}
{% endaller %}

> equivalence assembleur = turing
> thèse de church-turing revisités

### Penser l'informatique

> TBD partial recursive function : <https://www.youtube.com/watch?v=yaDQrOUK-KY&list=PLC-8dKj3F0NUnR8LeBGH3utAI9aQjFbi5> comme tout ce qui peut être calculer avec une machine de Turing.
> cdans la partie fonction juste dire que les primitive recursives sont calculables, mais pqs que elle : ackerman et o le démontre.
> 
> TBD : Turing.
> faire factorielle avec une machine de Turing.
> dire que structure de donnée = code et que l'on a besoin de rien comme outil pour exécuter du code : juste une façon de stocker et une façon d'écrire conditionnellement. Le code est LOCAL.

> TBD le plus minimal c'est la machine de Turing, mais d'un point de vue opérationnel il est minimal car c'est ce qui est appelé assembleur.
> faire les call avec des jump
> à la fin dire qu'il y a souvent plusieurs autres méthodes dans les langages machines pour aider (donner exemple, sub, mul, gestion approximation de réel, call/ret et surtout la pile qu'on verra bien plus tard.), mais on peut tout faire avec ce qu'on a la.
> 
> Passer d'un pseudo code à un langage machine simple et montrer sn équivalence. Ceci permettra de montrer plus facilement que des langages sont équivalents.
> Langage simplifié où les variables n'existent pas et le boucles sont remplacés par des saut. Tout langage informatique peut être transcrit en langage machine
> instructions finie et 1 ou deux paramètres et une sortie dans des variables fixées et de taille fixé disons 64bits appelées registres.
> variables = un grand tableaux de cases de taille fixée. Disons 64bits

## Autres modèles

> Turing complet
>
> Lambda calcul
> ...
> <https://www.youtube.com/watch?v=jUnbX27jbvY>
> <https://en.wikipedia.org/wiki/General_recursive_function>
> <https://en.wikipedia.org/wiki/Computable_function>
> bijection recursive et Turing <https://www.irif.fr/~carton/Enseignement/Complexite/ENS/Cours/funrec.html>
>
> dire que recursion = boucle for
> reduction = boucle while.
> 
> Enfin, puisque nos algorithmes pour la composition et la récursion n'utilisent que des boucles de type _"pour chaque"_ :

{% note "**Proposition**" %}
Les fonctions récursives primitives sont les fonctions calculables avec des algorithmes utilisant uniquement des boucles de type _"pour chaque"_ (des boucles `for`{.language-}).
{% endnote %}
{% details "preuve" %}
un coté clair nos algos sont fait avec des compositions finies de boucle for.

réciproquement : <https://ai.dmi.unibas.ch/_files/teaching/fs16/theo/slides/theory-d05.pdf>
{% enddetails %}

fonctions vs algorithmes :

- Turing : algorithme par de x pour le transformer en f(x)
- fonction/lambda calcul part de f et l'applique en x pour trouver f(x)
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

{% lien %}
[Playlist sur la _theory of computation_](https://www.youtube.com/watch?v=bP1lOm5rLsI&list=PLwF3A0R8OzMpO6_9WbT1kK16akYFh3_Nt&index=1) et [le livre associé](https://hefferon.net/computation/)

{% endlien %}

## Machine de Turing

{% aller %}
[Machine de Turing](./machine-turing){.interne}
{% endaller %}

## Équivalences

Nous allons agrandir dans cette partie les différents modèles de création de programmes qui produisent des résultats équivalents. On sait déjà que les programmes crées en pseudo-codes sont équivalents à ceux crées en pseudo-assembleur, eux même équivalents à ceux que l'on peut exécuter sur un processeur suivant l'architecture de Von Neumann (tous les processeurs la suive).

Pour montrer qu'un modèle de création de programme $A$ est plus riche qu'un modèle $B$, il suffit de montrer que l'on peut soit :

- simuler $B$ dans $A$,
- convertir un programme du modèle $B$ en un programme du modèle $A$

On notera alors $A \geq B$. Si on peut aussi faire la réciproque ($B \geq A$), alors les deux modèles sont équivalent et peuvent faire les mêmes programmes.

### Machines de Turing

En deux temps, aussi aisé l'un que l'autre pour obtenir le résultat :

{% note "**Théorème**" %}

Pseudo-code et machine de Turing sont deux notions équivalentes.

{% endnote %}
{% details "preuve", "open" %}

- **Machines de Turing $\leq$ pseudo-assembleur** :
  Clair puisque l'on peut simuler l'exécution d'une machine de Turing universelle en pseudo-code. Le site <https://turingmachine.io/> en est un exemple.
- **Machines de Turing $\geq$ pseudo-assembleur** :
  1. les [compositions de machines](./machine-turing/composition){.interne} montrent que l'on peut avoir les mêmes structures de contrôle qu'en pseudo-assembleur (exécution séquentielle et saut conditionnels)
  2. il est facile de faire une fonction de transition qui simule l'opération `NAND`{.language-}
  3. on peut avoir autant de ruban qu'on le veut et écrire où on veut en mémoire : on peut utiliser le modèle de von Neumann avec une machine de Turing

{% enddetails %}

### Fonctions récursives

Nous avons vu que les fonctions primitives récursives étaient des fonctions calculable. Nous allons montrer ici qu'un modèle plus générale, les fonctions récursives, sont équivalentes au pseudo-code ! Ceci montre que l'algorithmie peut posséder de nombreuses formes, toutes équivalentes.

{% aller %}
[Fonctions récursives](./fonctions-récursives){.interne}
{% endaller %}

### Lambda calcul

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

## Penser l'informatique

Nous avons montré que de nombreux modèles de calculs très différents sont équivalents. Toutes les tentatives d'étendre ou de trouver des modèles différents ont tous échoué : on a l'impression que le modèle de la machine de Turing est indépassable et qu'il capture l'essence même de ce qui est un algorithme. C'est pourquoi il est communément admis que :

{% note "**Thèse de Church-Turing**" %}
Les notions d'algorithme et de machine de Turing sont équivalentes.

Tout algorithme peut être écrit avec une machine de Turing.
{% endnote %}

En bon informaticien, on considérera la thèse de Church-Turing vérifiée et, comme pseudo-code et machines de Turing sont équivalents :

- on écrira tous nos algorithmes en pseudo-code
- pseudo-code et algorithme seront considérés comme synonyme.

Le calcul est donc quelque chose d’éminemment local : une tête de lecture et un état, c'est la succession de ces modifications locales qui produit un résultat global. De plus, on a pas besoin de types ou de structures de données compliquées dans le modèle : seul le bit et la fonction NAND sont indispensable. Toutes les autres structures de données comme les listes, les piles, et autres dictionnaires sont géré par du code.

{% lien %}

- <https://plato.stanford.edu/entries/turing-machine/#ThesDefiAxioTheo>
- <https://www.youtube.com/watch?v=jUnbX27jbvY>

{% endlien %}

De part les nombreuses équivalences, lorsque l'on cherchera à démontrer des résultats sur les algorithmes en général on se ramènera aux machines de Turing, au pseudo-code ou aux fonctions récursives.

Enfin, pour savoir si un modèle donné est général, il suffit de montrer qu'il peut simuler une machine de Turing. C'est ce qu'on appelle être Turing complet.

## Turing complet

Grâce à la machine de Turing universelle, démontrer qu'un langage est [Turing complet](https://fr.wikipedia.org/wiki/Turing-complet) c'est à dire qu'il permet de calculer tout ce qu'une machine de Turing peut calculer revient à montrer qu'on peut simuler une machine de Turing.

{% note "**définition**" %}
Un système est dit [Turing complet](./https://fr.wikipedia.org/wiki/Turing-complet) s'il permet de faire tout ce qu'une machine de Turing peut faire.
{% endnote %}

Avoir un modèle Turing Complet nous assure, en suivant la thèse de Church-Turing que ce modèle peut calculer tous les algorithmes. Pour montrer qu'un modèle est Turing-complet, on peut soit écrire un simulateur de machine de Turing (pour un langage comme python par exemple) ou, comme on l'a vu avec le pseudo-assembleur, montrer que l'on possède :

- de la mémoire
- un saut conditionnel à un endroit donnée du code
- la fonction `NAND` (ou la fonction `XOR`)

Cette preuve permet de montrer que les systèmes suivant sont Turing complet :

- un processeur
- la quasi-totalité des langages de programmation
- excel
- Factorio
- Minecraft
- ...

Ce qu'il faut retenir de tout ça, c'est qu'il est très facile d'être Turing Complet mais impossible d'être plus !

Finissons par quelques exemples non triviaux de modèles Turing complet.

### Automates cellulaires

La plupart des [automates cellulaires](https://fr.wikipedia.org/wiki/Automate_cellulaire) sont Turing-complet. C'est le cas du célèbre [jeu de la vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie), mais aussi d'automates bien plus simple :

{% lien %}
L'exemple de système Turing complet le plus simple que je connaisse est l'automate uni-dimensionnel respectant la [règle 110](https://en.wikipedia.org/wiki/Rule_110).

Jetez-y un coup d'œil, c'est assez bluffant.
{% endlien %}

### Langages exotiques

Si la plupart des langages informatiques sont clairement Turing complet, il existe des langages bizarres, nommé [langages de programmation exotiques](https://fr.wikipedia.org/wiki/Langage_de_programmation_exotique), qui sont aussi Turing complet. Ces langages tendent à être minimalistes et cherchent à posséder soit le nombre minimal d'instruction, comme le célèbre [brainfuck](https://www.google.com/search?q=brainfuck), ou à être marrant, comme le [Piet](https://www.dangermouse.net/esoteric/piet.html) dont le but est de créer des programmes sous la forme d'un tableau de [Piet Mondrian](https://fr.wikipedia.org/wiki/Piet_Mondrian).

### Autres trucs

{% lien %}
- [Legend of Zelda: Tears of the Kingdom](https://www.youtube.com/watch?v=5u6BN1p0Uo8)
- [Powerpoint](https://www.youtube.com/watch?v=uNjxe8ShM-8)
- [règle 110 avec Factorio (et des trains)](https://www.youtube.com/watch?v=NCC2Fd8qxv4)
{% endlien %}

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

fonctions récursives > fonctions primitives récursives

> TBD partial recursive function : <https://www.youtube.com/watch?v=yaDQrOUK-KY&list=PLC-8dKj3F0NUnR8LeBGH3utAI9aQjFbi5> comme tout ce qui peut être calculer avec une machine de Turing.
> cdans la partie fonction juste dire que les primitive recursives sont calculables, mais pqs que elle.

{% note "**Proposition**" %}
Les fonctions récursives primitives sont les fonctions calculables avec des algorithmes utilisant uniquement des boucles de type _"pour chaque"_ (des boucles `for`{.language-}).
{% endnote %}
{% details "preuve" %}
un coté clair nos algos sont fait avec des compositions finies de boucle for.

réciproquement : <https://ai.dmi.unibas.ch/_files/teaching/fs16/theo/slides/theory-d05.pdf>
{% enddetails %}

En déduire que [la fonction de couplage de Cantor](https://fr.wikipedia.org/wiki/Fonction_de_couplage) est primitive récursive :

{% exercice %}
Montrez que la fonction $f(x, y) = (x + y + 1)(x+y)/2 + y$ est primitive récursive.
{% endexercice %}
{% details "corrigé" %}

> TBD avec diviser par 2.

{% enddetails %}

{% exercice %}
Montrez que la fonction
[Théorème montrant qu'il y a strictement plus de réels que d'entiers](../définition/#diagonale-cantor)

{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

### Lambda calcul

- Turing : algorithme par de x pour le transformer en f(x)
- fonction/lambda calcul part de f et l'applique en x pour trouver f(x)

> Lambda calcul
> ...
> <https://www.youtube.com/watch?v=jUnbX27jbvY>
> <https://en.wikipedia.org/wiki/General_recursive_function>
> <https://en.wikipedia.org/wiki/Computable_function>
> bijection recursive et Turing <https://www.irif.fr/~carton/Enseignement/Complexite/ENS/Cours/funrec.html>
>
> dire que recursion = boucle for
> reduction = boucle while.
> TBD : pour les matheux qui veulent s'encanailler à faire de l'informatique
> Catégories et types : <https://bartoszmilewski.com/2014/10/28/category-theory-for-programmers-the-preface/>, <https://ncatlab.org/nlab/show/computational+trilogy>
> <https://www.youtube.com/watch?v=_n4LIt2WPzE>
> Maths : <https://www.paultaylor.eu/~pt/prafm/index.html>
> <https://www.haskell.org/> :
>
> - intro : <https://www.youtube.com/watch?v=UhM_H3lFk_Q>
> - playlist <https://www.youtube.com/watch?v=Vgu82wiiZ90&list=PLe7Ei6viL6jGp1Rfu0dil1JH1SHk9bgDV>
> - livre : <https://learnyouahaskell.com/>

## Penser l'informatique

> TBD comment tout faire avec le ;oins de choses possible. Que l'on puisse facilement tout appréhender. 
> TBD comment ponctionne l'algorithmie en principe.
> TBD dire que code = local et que les structures de données peutvent être gérée avec du code. 
> 
## <span id="thèse-Church-Turing"></span>Thèse de Church-Turing

Une machine de Turing (et donc le pseudo-code) est a priori un cas particulier d'algorithme puisque l'on se limite à un nombre fixé d'instructions et à une construction rigide et normée de ceux ci. Mais toutes les tentatives de généralisation ont échoués : elle n'ont jamais permis de faire des algorithmes impossible à réaliser en pseudo-code.

{% lien %}
Si ces considérations vous intéressent, n'hésitez pas à jeter un coup d'œil à ce lien :
<https://plato.stanford.edu/entries/turing-machine/#ThesDefiAxioTheo>

C'est en Anglais, mais c'est très bien.
{% endlien %}

On pense donc (mais ce n'est pas démontré) que :

{% note "**Thèse de Church-Turing**" %}
Les notions d'algorithme et de pseudo-code sont équivalentes.

Tout algorithme peut être écrit en pseudo-code.
{% endnote %}

En bon informaticien, on considérera la thèse de Church-Turing vérifiée et :

- on écrira tous nos algorithmes en pseudo-code
- pseudo-code et algorithme seront considérés comme synonyme.


> Algo = machine de Turing.
> TBD : Turing.
> dire que structure de donnée = code et que l'on a besoin de rien comme outil pour exécuter du code : juste une façon de stocker et une façon d'écrire conditionnellement. Le code est LOCAL.

> TBD le plus minimal c'est la machine de Turing, mais d'un point de vue opérationnel il est minimal car c'est ce qui est appelé assembleur.
> faire les call avec des jump
> à la fin dire qu'il y a souvent plusieurs autres méthodes dans les langages machines pour aider (donner exemple, sub, mul, gestion approximation de réel, call/ret et surtout la pile qu'on verra bien plus tard.), mais on peut tout faire avec ce qu'on a la.
> 
> Passer d'un pseudo code à un langage machine simple et montrer sn équivalence. Ceci permettra de montrer plus facilement que des langages sont équivalents.
> Langage simplifié où les variables n'existent pas et le boucles sont remplacés par des saut. Tout langage informatique peut être transcrit en langage machine
> instructions finie et 1 ou deux paramètres et une sortie dans des variables fixées et de taille fixé disons 64bits appelées registres.
> variables = un grand tableaux de cases de taille fixée. Disons 64bits

## Turing complet

> Thèse de Church-Turing : machine de turing = algorithmie. donc on adment qu'une machine de turing peut tout faire. Un langage ne peut donc pas faire plus qu'une machine. Il en fait autant si on peut simuler une machine dans le langage.
> Turing complet = on peut simuler


Grâce à la machine de Turing universelle, démontrer qu'un langage est [Turing complet](https://fr.wikipedia.org/wiki/Turing-complet) c'est à dire qu'il permet de calculer tout ce qu'une machine de Turing peut calculer revient à montrer qu'on peut simuler une machine de Turing. Comme il est facile de simuler une MTU en pseudo-code (on l'a fait [juste avant](./#pseudo-code-MTU)){.interne} on en conclut :

{% note "**Proposition**" %}
Tout ce qui peut s'écrire avec une machine de Turing peut s'écrire avec un pseudo-code.
{% endnote %}



{% note "**définition**" %}
Un système est dit [Turing complet](./https://fr.wikipedia.org/wiki/Turing-complet) s'il permet de faire tout ce qu'une machine de Turing peut faire.
{% endnote %}

Une façon de montrer qu'un système est Turing complet est de faire ce qu'on a fait pour le pseudo--code, montrer qu'il peut simuler l'exécution d'une machine de Turing. De là il peut simuler l'exécution d'une machine de Turing Universelle et donc faire tout ce que peut faire une machine de Turing.

Cette preuve permet de montrer que les systèmes suivant sont Turing complet :

- un processeur
- la quasi-totalité des langages de programmation
- excel
- Factorio
- Minecraft
- ...

Ce qu'il faut retenir de tout ça, c'est qu'il est très facile d'être Turing Complet !

{% lien %}
L'exemple de système Turing complet le plus simple que je connaisse est l'automate uni-dimensionnel respectant la [règle 110](https://en.wikipedia.org/wiki/Rule_110).

Jetez-y un coup d'œil, c'est assez bluffant.
{% endlien %}

Bien qu'il soit très facile pour un système d'être Turing Complet, toute les tentatives de généralisation  se sont révéler vaines.
La notion de Machine de Turing semble capturer l'essence même de ce qu'est un algorithme.

### Automates cellulaires

> TBD : Jeu de la vie
> TBD : <https://fr.wikipedia.org/wiki/Automate_cellulaire#R%C3%A8gle_110>

### Langages exotiques

brainfuck

### Autres trucs

powerpoint
factorio
...
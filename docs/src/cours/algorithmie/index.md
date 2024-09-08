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

## <span id="partie-2"></span>Partie I

Tout ce que devrait connaître tout ingénieur de l'informatique.

### Algorithmes et programmes

Commençons par définir ce qu'est un algorithme et ce qu'il peut ou ne peut pas faire :

{% aller %}
[Bases théoriques](./bases-théoriques){.interne}
{% endaller %}

On peut maintenant définir une grammaire permettant décrire des algorithmes sous la forme de pseudo-code et s'en servir pour résoudre des problèmes :

{% aller %}
[Écrire des algorithmes](./écrire-algorithmes){.interne}
{% endaller %}

Le [pseudo-code](./écrire-algorithmes/pseudo-code/) permet d'écrire des programmes sur papier que l'on peut exécuter dans sa tête aidé d'un papier et d'un crayon. Les langages de programmation permettent d'exécuter du code sur un ordinateur un utilisant un [langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation).

Pour la plupart d'entre eux, il est facile de transcrire le pseudo-code en code pouvant être exécuté, on a alors l'implication suivante :

{% note "**Proposition**" %}
Tout ce qui peut s'écrire en pseudo-code peut s'exécuter sur un ordinateur.
{% endnote %}

La réciproque n'est pas prouvée mais de nombreux indices (nous en verrons plusieurs dans la seconde partie de ce cours) tendent à penser que c'est vrai. On supposera donc vrai la proposition suivante, communément admise :

{% note "**Thèse de Church-Turing**" %}
Les notions d'algorithme et de pseudo-code sont équivalentes :

Tout algorithme peut être écrit en pseudo-code et réciproquement.
{% endnote %}
{% lien %}
La thèse de Church-Turing est intimement lié aux démonstrations mathématiques, un algorithme étant une preuve et réciproquement (les mathématiques sont donc une branche de l'informatique, et réciproquement ?).

Voir [cette excellente vidéo d'Arte](https://www.youtube.com/watch?v=Zci9m08HQws) pour une introduction en douceur de la problématique.
{% endlien %}

### Algorithmes itératifs et récursifs

> TBD : à faire propre et ne garder que le simple. En donnant une définition de récursif.
> TBD Supprimer la pile. Ne montrer que dans les cas simples, récursion terminal, que l'on peut rendre le tout itératif. S'intéresser uniquement à la finitude et la preuve.

{% aller %}
[Itératif et récursif](./projet-itératif-récursif){.interne}
{% endaller %}

### Complexités

{% lien %}
[une intro très bien faite sur la complexité des problèmes algorithmiques](https://www.youtube.com/watch?v=n8Z7v09zrl0&list=PLF0b3ThojznQJ6u4FUcpyzi0it5EpR3dh&index=12)
{% endlien %}

Cette partie s'intéresse à la notion de complexités pour un algorithme et un problème.

{% aller %}
[Calcul de complexité d'un algorithme](./complexité-calculs){.interne}
{% endaller %}
{% aller %}
[Complexité d'un problème algorithmique](./complexité-problème){.interne}
{% endaller %}

La notion de complexité est centrale en algorithmie, nous en reparlerons encore plus tard dans le cours.

### On s'entraîne

> TBD reprendre les exos d'avant avec calcul de complexité.

### projet : problèmes liés à l'exponentiation

{% aller %}
[Calculer $x^y$](./projet-exponentiation){.interne}
{% endaller %}
{% aller %}
[Les suites additives](./projet-suite-additive){.interne}
{% endaller %}

### Complexité en moyenne

{% aller %}
[Complexité en moyenne](./complexité-moyenne){.interne}
{% endaller %}

### Problème du tri

{% aller %}
[Problème du tri](./problème-tris){.interne}
{% endaller %}

### On s'entraîne : exercices de complexité et de preuve

{% aller %}
[Algorithmes classiques](./projet-classiques){.interne}
{% endaller %}

> TBD faire un lien avec les exos vu en écriture d'algo + complexité pour que tout soit aussi là.
> TBD exos : <https://www.inf.usi.ch/carzaniga/edu/algo19s/exercises.pdf>

> TBD 2-SUM $T[i] + T[j] = 0$ en $\mathcal{O}(n^2)$
> 3-SUM $T[i] + T[j] + T[k] = 0$ en $\mathcal{O}(n^3)$ (en modifiant 2-sum avec $T[i] + T[j] = K$) puis en $\mathcal{O}(n^2)$ (avec tri). Faire tout est tout aussi rapide que faire 1.

> TBD lièvre et lapin.

### Structures linéaires

#### Conteneurs

{% aller %}
[Conteneurs](./structure-conteneurs){.interne}
{% endaller %}

> TBD ajouter exos pour dictionnaires.
> TBD 2-SUM $T[i] + T[j] = 0$ en $\mathcal{O}(n)$ en moyenne avec dico. Ne change rien pour 3-SUM, il faut le faire n fois.
>
> TBD pas toujours la meilleur solution le dico : faire lièvre et lapin (qu'on aura vu dans algo classiques) pour deux tableaux avec égalité mieux que dictionnaire.

#### Chaînes de caractères

> TBD on a déjà utilisé les chaines de caractères à de nombreuses reprise. Nous allons maintenant pouvoir étudier plus attentivement. Comme les algo sont de $\\{0, 1\\}^\star$ à $\\{0, 1\\}^\star$, c'est une structure fondamentale pour penser l'algorithmie et comme tout est écrit, en particulier le code, elles sont au centre de nombreux problèmes courant.

{% aller %}
[Chaines de caractères](./structure-chaine-de-caractères){.interne}
{% endaller %}

### Design d'algorithmes

> TBD reprendre les algos d'avant et les classer dans les cases.

{% aller %}
[Design d'algorithmes](./design-algorithmes){.interne}
{% endaller %}

On s'entraîne avec le problème de l'enveloppe convexe qui peut se résoudre en utilisant de nombreux design :

{% aller %}
[Problème de l'enveloppe convexe](./enveloppes-convexes){.interne}
{% endaller %}

### Réductions : passer d'un problème à un autre

{% aller %}
[réduction de problèmes](./problème-réduction){.interne}
{% endaller %}

On a vu au début de ce cours que certains problèmes [ne pouvaient pas être résolu par un algorithme](./bases-théoriques/calculabilité){.interne} (certains réels ne sont pas calculables, le problème de l'arrêt, etc) : certaines questions resteront sans réponse. De plus, on a vu également que même s'il existe un algorithme pour résoudre un problème mais que si [sa complexité est exponentielle](./complexité-calculs/importance){.interne} le temps de calcul sera rédhibitoire : certaines questions resteront sans réponses en pratique.

Pouvoir séparer les problèmes selon la facilité de leurs résolutions semble une bonne approche. On sait par exemple que le [problème du tri](./problème-tris){.interne} est de complexité $\mathcal{O}(n\ln(n))$ où $n$ est la taille du tableau d'entiers à trier ou encore que la complexité du [problème de l'exponentiation](./projet-exponentiation){.interne} est en $\mathcal{O}(\ln(n))$ où $n$ est l'exposant. Mais qu'en est-il d'un problème quelconque ? Cela nécessite quelques investigations avant de pouvoir ne serait-ce que poser le problème.

> TBD voir si cohérent avec NP-optimization problem de A.3 de "Approximation Algorithms". Ajouter une partie pour l'approximation.

{% aller %}
[Problèmes NP](./problèmes-NP){.interne}
{% endaller %}

Un problème NP-complet, le sac à dos :

{% aller %}
[Problème du sac à dos](./problème-sac-à-dos){.interne}
{% endaller %}

## Intermède

Avant de finir cette première partie du cours, accordons nous un intermède en regardant une petite bizarrerie algorithmique :

Il existe un algorithme optimal pour résoudre tous les problèmes de NP ! Il suffit juste pour cela de connaître un de ses vérifieurs efficaces.

{% lien %}
<https://www.youtube.com/watch?v=9ONm1od1QZo> et son algo universel pour tous les problèmes NP. <https://steemit.com/steemstem/@markgritter/leonid-levin-s-universal-algorithm>

{% endlien %}

> TBD on se demande si NP vaut NP-complet. Même si c'est le cas la constante devant peut être giganteste pour empêcher de l'utiliser en pratique. Ce n'est vrai qu'asymptotiquemet. Cela ne vous dispense donc pas d'écrire devrais algorithmes


## <span id="partie-2"></span>Partie II

Tout ce que devrait connaître tout ingénieur aimant l'informatique.

### Modèle de calculs

Nous avons jusqu'à présent utilisé le modèle du pseudo-code pour créer des algorithmes.

Le pseudo-code est la partie émergée de l'algorithmie. Il permet de créer efficacement des programmes et des algorithmes. Ils sont cependant peu pratiques pour deux cas d'intérêt :

- exécuter des programmes avec un ordinateur
- penser l'algorithmie

Commençons par comprendre comment exécuter du code :

{% aller %}
[Exécuter du code](./exécuter-code){.interne}
{% endaller %}

Le pseudo-code permet de concevoir des algorithmes pouvant être exécutés au tableau par des humains. L'assembleur quant à lui, language de la machine, permet d'exécuter des algorithmes sur des processeurs.
Pseudo-code et assembleurs sont équivalents : les problèmes que l'on peut résoudre avec l'un sont également résoluble avec l'autre (et réciproquement). On peut même transcrire en assembleur un programme écrit en pseudo-code de façon automatique (on a évoqué sans rentrer dans les détails les moyens d'y parvenir) il est donc courant d'écrire son code en pseudo-code, facile à lire et à maintenir, puis de laisser un compilateur le transcrire en assembleur pour être exécuté.

Cependant pour penser l'algorithmie, c'est à dire étudier ce qui peut ou ne peut pas être résoluble par le calcul, pseudo-code et assembleur sont encore trop _riches_ (on peut aller n'importe où dans la mémoire par exemple, on suppose l'existence de la fonction `NAND`{.language-}, etc). Il ne faut conserver que les éléments indispensables pour pouvoir écrire tout ce que l'on peut faire en pseudo-code.

C'est ce que propose Turing avec sa célèbre Machine : une base théorique minimale de ce qu'est l'informatique :

{% aller %}
[Machine de Turing](./machine-turing){.interne}
{% endaller %}

Nous allons agrandir dans cette partie les différents modèles de création de programmes qui produisent des résultats équivalents. On sait déjà que les programmes crées en pseudo-codes sont équivalents à ceux crées en pseudo-assembleur, eux même équivalents à ceux que l'on peut exécuter sur un processeur suivant l'architecture de Von Neumann (tous les processeurs la suive). C'est aussi le cas pour les machines de Turing :

{% note "**Théorème**" %}

Pseudo-code et machine de Turing sont deux notions équivalentes.

{% endnote %}
{% details "preuve", "open" %}

- **On peut simuler une Machines de Turing avec du pseudo-assembleur** :
  Clair puisque l'on peut simuler l'exécution d'une machine de Turing universelle en pseudo-code. Le site <https://turingmachine.io/> en est un exemple.
- **On peut simuler du pseudo-assembleur avec une Machines de Turing** :
  1. les [compositions de machines](./machine-turing/composition){.interne} montrent que l'on peut avoir les mêmes structures de contrôle qu'en pseudo-assembleur (exécution séquentielle et saut conditionnels)
  2. il est facile de faire une fonction de transition qui simule l'opération `NAND`{.language-}
  3. on peut avoir autant de ruban qu'on le veut et écrire où on veut en mémoire : on peut utiliser le modèle de von Neumann avec une machine de Turing

{% enddetails %}

#### Algorithme et machine de Turing

Toutes les tentatives de généraliser le modèle de la machine de Turing ont été vains. Il semble que ce modèle capte exactement ce qu'est un algorithme. C'est pourquoi les informaticiens sont intimement convaincu que la thèse de Turing-Church est vraie :

{% note "**Thèse de Church-Turing**" %}
Les notions d'algorithme et de machine de Turing sont équivalentes.

Tout algorithme peut être écrit avec une machine de Turing.
{% endnote %}

En bon informaticien, on considérera la thèse de Church-Turing vérifiée et, comme pseudo-code et machines de Turing sont équivalents :

- on écrira tous nos algorithmes en pseudo-code
- pseudo-code et algorithme seront considérés comme synonyme.

Le calcul est donc quelque chose d’éminemment local : une tête de lecture et un état, c'est la succession de ces modifications locales qui produit un résultat global. De plus, on a pas besoin de types ou de structures de données compliquées dans le modèle : seul le bit et la fonction `NAND` sont indispensable. Toutes les autres structures de données comme les listes, les piles, et autres dictionnaires sont géré par du code.

{% lien %}

- <https://plato.stanford.edu/entries/turing-machine/#ThesDefiAxioTheo>
- <https://www.youtube.com/watch?v=jUnbX27jbvY>

{% endlien %}

De part les nombreuses équivalences, lorsque l'on cherchera à démontrer des résultats sur les algorithmes en général on se ramènera aux machines de Turing, au pseudo-code ou aux fonctions récursives.

Enfin, pour savoir si un modèle donné est général, il suffit de montrer qu'il peut simuler une machine de Turing. C'est ce qu'on appelle être Turing complet.

#### Turing complet

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

#### Autres modèles

Finissons par quelques exemples non triviaux de modèles Turing complet :

{% aller %}
[Autres modèles](./modèles-turing-complet){.interne}
{% endaller %}

### Problèmes de décisions

> TBD refaire NP-complet et le prouver
> TBD reprendre ici langage et mots.
> 
{% aller %}
[Classes de problèmes algorithmiques](./décision-problèmes){.interne}
{% endaller %}

> mettre Turing ici et Cook.
> Fin de la partie 1 juste donner NP et dire qu'il y a des NP-complet et le prouver ici.

## Désordre et hasard

{% aller %}
[Mélanger un tableau](./projet-mélange){.interne}
{% endaller %}

> TBD nombre aléatoires

## Complexité amortie

> TBD A déplacer plus tard. Attention à l'amortie des dict/liste.

{% aller %}
[Complexité amortie](./complexité-amortie){.interne}
{% endaller %}

> TBD : [projet Multiplication de matrices](./multiplication-matrices){.interne}

Un problème particulier :

{% aller %}
[problème SAT](./problème-SAT){.interne}
{% endaller %}

## Sac à dos

> TBD deuxième problème dur : montrer que plus dur que SAT, donc équivalent.
> TBD réduction sac a dos à bi-partition : <https://datamove.imag.fr/denis.trystram/SupportsDeCours/2017KnapSack.pdf>
> <https://people.orie.cornell.edu/dpw/orie6300/Lectures/lec25.pdf>

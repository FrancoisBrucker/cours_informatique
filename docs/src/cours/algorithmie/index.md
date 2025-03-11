---
layout: layout/post.njk

title: Algorithmie
tags: ["cours", "algorithmie"]

authors:
  - François Brucker
resume: "Un cours d'algoritmie"

eleventyNavigation:
  prerequis:
    - "/cours/coder-et-développer/bases-programmation/"

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

Il est conseillé pour ce cours d'avoir des bases de programmation en python. Pour apprendre vous pouvez vous reporter au prérequis.

## <span id="partie-1"></span>Partie I

Tout ce que devrait connaître tout ingénieur de l'informatique.

### Algorithmes et programmes

Commençons par définir ce qu'est un algorithme et ce qu'il peut ou ne peut pas faire :

{% aller %}
[Bases théoriques](./bases-théoriques){.interne}
{% endaller %}

On peut maintenant définir une grammaire permettant décrire des algorithmes sous la forme de pseudo-code et s'en servir pour résoudre des problèmes :

{% aller %}
[Écrire les algorithmes en pseudo code](./pseudo-code){.interne}
{% endaller %}

Le pseudo-code permet d'écrire des programmes sur papier que l'on peut exécuter dans sa tête aidé d'un papier et d'un crayon. Les langages de programmation permettent d'exécuter du code sur un ordinateur un utilisant un [langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation).

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

Le modèle du pseudo-code n'est pas la seule façon d'écrire des algorithmes. La célèbre machine de Turing que l'on verra en partie II en est un exemple. Mais il y en a beaucoup, beaucoup d'autres :

{% aller %}
[Autres modèles](./autres-modèles){.interne}
{% endaller %}

### Problème algorithmique et preuve

Un algorithme est sensé faire quelque chose : à partir de données passées en entrée (ses paramètre) il va produire une sortie. Cette sortie dépend de ses paramètres et répond à une question ou plus généralement résout un problème. Mais comment prouver qu'un algorithme répond bien au problème posé ?

{% aller %}
[Problème algorithmique](./probleme-algorithmique){.interne}
{% endaller %}

Mais même si on a un problème algorithmique et un algorithme, comment prouver que le second résout le premier puisqu'il n'existe [aucune méthode générale pour savoir ce que fait un algorithme](bases-théoriques/arrêt-rice/#théorème-rice){.interne} ? Il faut le faire au cas par cas. Mais rassurez-vous, selon le type d'algorithme il existe des méthodes qui fonctionnent souvent :

{% aller %}
[Prouver des algorithmes](./prouver-un-algorithme){.interne}
{% endaller %}

### <span id="entrainement-preuve"></span>On s’entraîne : algorithmes itératifs et récursifs

Une série de problème algorithmique à résoudre par des algorithmes simples et clairs. Le but d'un algorithme papier est d'être compris. Faites l'effort de préférer des noms de variables explicites et n'hésitez pas à séparer votre pseudo-code en fonctions pour qu'il soit plus clair.

{% aller %}
[Projet : Écrire et prouver des algorithmes itératifs et récursifs](./projet-itératif-récursif){.interne}
{% endaller %}

### Complexités

{% lien %}
[une intro très bien faite sur la complexité des problèmes algorithmiques](https://www.youtube.com/watch?v=n8Z7v09zrl0&list=PLF0b3ThojznQJ6u4FUcpyzi0it5EpR3dh&index=12)
{% endlien %}

Cette partie s'intéresse à la notion de complexités pour un algorithme.

{% aller %}
[Calcul de complexité d'un algorithme](./complexité-calculs){.interne}
{% endaller %}

Cette notion est centrale en algorithmie, nous en reparlerons encore tout au log de ce cours.

{% aller %}
[Complexité d'un problème algorithmique](./complexité-problème){.interne}
{% endaller %}

### <span id="entrainement-complexite"></span>On s'entraîne : calcul de complexité

Maintenant que l'on peut calculer les complexités, on peut reprendre les algorithmes itératifs et récursifs que [nous avons crées précédemment](./#entrainement-preuve) :

{% aller %}
[Projet : calculer des complexités d'algorithmes itératifs et récursifs](./projet-calcul-complexite){.interne}
{% endaller %}

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

### Structures de données

Comment créer de nouveaux types d'objets utilisable pour nos algorithmes.

{% aller %}
[Structures de données](structure-données){.interne}
{% endaller %}

Nous allons définir et utiliser ici des structures de données très utiles dans de nombreux problèmes. Ces structures sont dites linéaires car elles permettent de gérer des listes ordonnées d'éléments

{% lien %}
[Structures linéaires](https://www.youtube.com/watch?v=kPqk07Gpj0A)
{% endlien %}

#### Gestion de flux

Lorsqu'un algorithme doit gérer un _flux_ de données, il doit être capable de stocker les données arrivante avant de pouvoir les traiter une à une. Les deux structures fondamentales pour cela sont les piles, les files et leurs dérivés :

{% aller %}
[Structure de gestion de flux](./structure-flux){.interne}
{% endaller %}

#### Structures dynamiques

La [structure de tableau](pseudo-code/briques-de-base/#tableaux){.interne} est l'élément élémentaire de toute structure permettant de stocker des objets. Elle est puissante car elle permet d'accéder en temps constant à tout élément qu'elle stocke (via son index) mais également limitée car le nombre d'objet qu'un tableau peut stocker (sa taille) est déterminé à sa création et est non modifiable. Enfin, l'index pour retrouver l'objet stocké est forcément un entier entre 0 et sa taille moins un. Nous verrons dans cette partie que l'on peut faire sauter toutes les limitations d'un tableau au prix d'un coût en complexité, souvent acceptable au vu du gain en maniabilité :

{% aller %}
[Les listes](./structure-liste){.interne}
{% endaller %}

Enfin, très utilisée dans les langages fonctionnels et le cas o`u l'on doit supprimer rapidement un élément en milieu de liste, la _liste chaînée_ :

{% aller %}
[Les listes chaînées](./structure-liste-chaînée){.interne}
{% endaller %}

#### Table de hashage et structures associées

Une autre structure fondamentale en algorithmie :

{% aller %}
[Tables de hashage et dictionnaires](./structure-dictionnaire){.interne}
{% endaller %}

#### Comparaisons des structures de conteneurs

> Structure génériques
> ajout/suppression :
>
> - liste : O(1) à la fin (amorti) ; O(n) autre part
> - dictionnaire : O(1) en moyenne
> - liste chaînée : O(1) partout
>
> recherche :
>
> - liste : O(1) avec indice
> - dictionnaire : O(1) en moyenne avec clé
> - liste chaînée : O(n) (il faut tout traverser)
>
>
> Cas d'utilisation :
>
> - liste : tout le temps à la place d'un tableau
> - dictionnaire : tout le temps si on ne manipule pas d'indices mais des objets
> - liste chaînée : si veut supprimer/ajouter un élément donné en O(1) mais pas besoin de trouver un élément quelconque (uniquement le premier)
>
> Gestion de flux : pile, file
>
> - push/pop : O(1) si taille fixe, sinon O(1) en amorti
> - recherche : via indice (avec le tableau sous-jacent) en O(1).

### Complexité amortie

Formalisation de ce que l'n a vu avec les listes. Certaines opérations n'ont pas toujours la même complexité mais la complexité importante n'arrive que rarement.

{% aller %}
[Complexité amortie](./complexité-amortie){.interne}
{% endaller %}

### On s'entraîne

#### Résolution d'algorithmiques classiques

{% aller %}
[Algorithmes classiques](./projet-classiques){.interne}
{% endaller %}

#### Résolution de problèmes algorithmiques classiques

{% aller %}
[Problèmes classiques](./projet-problemes-classiques){.interne}
{% endaller %}

## <span id="partie-2"></span>Partie II

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

### Design d'algorithmes

> TBD reprendre les algos d'avant et les classer dans les cases.

{% aller %}
[Design d'algorithmes](./design-algorithmes){.interne}
{% endaller %}

On s'entraîne avec le problème de l'enveloppe convexe qui peut se résoudre en utilisant de nombreux design :

{% aller %}
[Problème de l'enveloppe convexe](./enveloppes-convexes){.interne}
{% endaller %}

## Intermède : recherche universelle

Avant de finir cette première partie du cours, accordons nous un intermède en regardant une petite bizarrerie algorithmique. L'Algorithme pour tout résoudre :

{% aller %}
[L'algorithme de la recherche universelle](./recherche-universelle){.interne}
{% endaller %}

## <span id="partie-3"></span>Partie III

Tout ce que devrait connaître tout ingénieur aimant l'informatique.

### Chaînes de caractères

> TBD on a déjà utilisé les chaines de caractères à de nombreuses reprise. Nous allons maintenant pouvoir étudier plus attentivement. Comme les algo sont de $\\{0, 1\\}^\star$ à $\\{0, 1\\}^\star$, c'est une structure fondamentale pour penser l'algorithmie et comme tout est écrit, en particulier le code, elles sont au centre de nombreux problèmes courant.

{% aller %}
[Chaines de caractères](./structure-chaine-de-caractères){.interne}
{% endaller %}

### <span id="modèle-calculs"></span>Modèle de calculs

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

### Algorithme et machine de Turing

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

#### Algorithmes et fonctions

> TBD uniquement fonctions récursives.

Finissons par quelques exemples non triviaux de modèles Turing complet :

{% aller %}
[Algorithmes et fonctions](./fonctions-récursives){.interne}
{% endaller %}

### Problème SAT

> TBD on vu que toute fonction est un sat et que tout circuit logique est un sat. Le problème SAT va être fondamental.

{% aller %}
[problème SAT](./problème-SAT){.interne}
{% endaller %}

### Problèmes de décisions

Nous allons dans cette partie approfondir et démontrer proprement des choses que nous avons laissées en suspend à la fin de la partie I, à savoir les classes de problèmes NP et les problèmes NP-complets.

{% aller %}
[Problèmes de décision](./décision-problèmes){.interne}
{% endaller %}

> TBD dire que les deux vision des problèmes NP sont équivalentes. La solution des problèmes est le certificat des problèmes de décision. Le non déterminisme c'est trouver la solution, puis la vérification est est déterministe.

{% aller %}
[Exemples de problèmes NP complets](./exemples-problèmes-NPC){.interne}
{% endaller %}

### Désordre et hasard

{% aller %}
[Mélanger un tableau](./projet-mélange){.interne}
{% endaller %}

> TBD nombre aléatoires : <https://xkcd.com/221/> et <https://imgur.com/random-number-generator-bwFWMqQ>

> TBD : [projet Multiplication de matrices](./multiplication-matrices){.interne}

> TBD SAC à dos deuxième problème dur : montrer que plus dur que SAT, donc équivalent.
> TBD réduction sac a dos à bi-partition : <https://datamove.imag.fr/denis.trystram/SupportsDeCours/2017KnapSack.pdf>
> TBD subsetsum ≤ bi-partition : <https://gnarlyware.com/blog/proving-set-partition-problem-is-np-complete-using-reduction-from-subset-sum/>

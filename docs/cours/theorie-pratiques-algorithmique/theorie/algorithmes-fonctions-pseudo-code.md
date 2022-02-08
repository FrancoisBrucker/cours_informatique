---
layout: page
title:  "Algorithmes, fonctions et pseudo-code"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [théorie]({% link cours/theorie-pratiques-algorithmique/theorie/index.md %}) / [Algorithmes, fonctions et pseudo-code]({% link cours/theorie-pratiques-algorithmique/theorie/algorithmes-fonctions-pseudo-code.md %})
>
> prérequis :
>
>* [fonctions]({% link cours/theorie-pratiques-algorithmique/theorie/fonctions.md %})
>* [pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %})
{: .chemin}

La partie [fonctions]({% link cours/theorie-pratiques-algorithmique/theorie/fonctions.md %}) montre qu'un algorithme peut être vu comme une fonction particulière de $\mathbb{N}$ dans $\mathbb{N}$, indépendamment des instructions utilisées.

La partie [pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}) quant-a-elle défini un jeu d'instruction utilisable pour créer des algorithmes mais ne dit rien sur l'exhaustivité de ce jeu d'instruction. Existe-t-il des algorithmes que l'on ne peut pas écrire sous la forme d'un pseudo-code ?

La réponse est : *on ne sait pas mais on pense que ce n'est pas possible*:

> [la thèse de Church-Turing](https://plato.stanford.edu/entries/turing-machine/#ThesDefiAxioTheo) stipule que pseudo-code et algorithmes sont deux notions équivalentes.
{: .note}

Nous ne démontrerons bien sur pas dans cette partie la thèse de Church-Turing, mais nous essayerons d'en détailler un peu plus les contours.

Et au final, dans la suite de ce cours :

> On supposera la thèse de Church-Turing vraie et on parlera indifféremment d'algorithme, de pseudo-code ou encore de machine de Turing de façon équivalente.
{: .attention}

## les multiples faces d'un algorithme

On montre ici que tout code ou pseudo-code est équivalent à une machine de Turing et qu'on se demande très fort si ce n'est pas aussi le cas pour les fonctions.

### algorithmes et fonctions

En utilisant juste la définition d'un algorithme, [on a vu]([fonctions]({% link cours/theorie-pratiques-algorithmique/theorie/fonctions.md %})) qu'un algorithme est : une fonction particulière de $\mathbb{N}$ dans $\mathbb{N}$.

Il y a même bien plus de fonctions qui ne sont pas des algorithmes que de fonctions qui le sont. Il est cependant difficile d'en exhiber une car montrer un objet c'est le caractériser, donc bien souvent le construire : c'est à dire le produire à partir d'un algorithme.

Notre quotidien est remplie de fonctions calculable par un algorithme.

### algorithmes et pseudo-code

Un algorithme, [on l'a aussi vu]({% link cours/theorie-pratiques-algorithmique/algorithmie/algorithmes.md %}#algorithme), c'est  :

> Un **algorithme** est une succession d'instructions simples et clairement définies. A partir d'entrées, il produit une sortie en un nombre fini d'instructions.
{: .note}

Un [pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#regles) est ainsi un algorithme particulier, ses [instructions]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#regles) respectant bien la définition générale ci-dessus.

On peut même montrer que les règles d'un pseudo-code peuvent être réduites à un ensemble bien plus petit :

> On peut ramener l'ensemble des [instructions d'un pseudo-code](https://en.wikipedia.org/wiki/Structured_program_theorem) (même si ce sera plus compliqué d'écrire le code) à trois types d'instructions et à trois façon de les exécuter.
>
> Une **instruction**  est soit :
>
> * une affectation d'un entier (voir même juste un bit) à une variable
> * une lecture d'une variable
> * un test d'égalité entre deux variables
>
> Un pseudo-code doit pouvoir :
>
> * exécuter une instruction puis une autre, **séquentiellement**
> * exécuter une instruction si un test d'égalité est vrai
> * exécuter un bloc d'instructions tant qu'un test d'égalité est vrai
{: .note}

Tous les pseudo-codes utilisant les 6 règles ci-dessus auront alors la même expressivité (on pourra faire exactement les mêmes choses) que ceux utilisant [les instruction d'un pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#regles), ce sera juste plus long et compliqué à écrire, c'est pourquoi leur intérêt est uniquement théorique.

### algorithmes et code

Il existe de nombreux langages de programmation, allant de [l'assembleur](https://fr.wikipedia.org/wiki/Assembleur) compréhensible par les processeurs de nos ordinateurs au [python](https://fr.wikipedia.org/wiki/Python_(langage)) que tout le monde connait, en passant par le [haskell](https://fr.wikipedia.org/wiki/Haskell) ou encore le [C](https://fr.wikipedia.org/wiki/C_(langage)).

On trouve même des langages désignées pour être les plus simples possibles (appelés [turing tarpit](https://fr.wikipedia.org/wiki/Langage_de_programmation_exotique)) tout en étant aussi expressif que le python. Le plus célèbre d'entre eux est le [brainfuck](https://fr.wikipedia.org/wiki/Brainfuck).

> *fun fact* : on peut utiliser aussi certains jeu comme langage de programmation comme [factorio](https://www.factorio.com/) (l'algorithme de tri [quicksort](https://www.youtube.com/watch?v=ts5EKp9w4TU)), ou encore [minecraft](https://www.minecraft.net/) ([une calculatrice](https://www.youtube.com/watch?v=uGug-4xkw6M)).

Tous ces langages respectent les 6 règles ci-dessus :

> On peut faire exactement la même chose avec chacun de ces langages et avec tout algorithme décrit par son pseudo-code
{: .note}

### algorithme et machine de Turing

Le jeu d'instruction minimale qui permet d'obtenir les 6 règles ci-dessus est la [machine de Turing]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %}) :

> On peut écrire tout pseudo-code en utilisant une machine de Turing et réciproquement
{: .note}

C'est ainsi un outil simple qui capture merveilleusement les différentes possibilités d'écrire un algorithme. On ne l'utilisera presque jamais directement (autant utiliser un pseudo-code puisque c'est équivalent) mais la machine de Turing est à la fois :

* un outil puissant de démonstration
* un jeu d'instruction pour créer des algorithmes
* un ensemble minimal permettant de créer tous les pseudo-code

### thèse de Church-Turing {#church-turing}

Toutes les tentatives de généraliser le modèle (essayer de calculer plus de fonctions que celle atteignable pas un pseudo-code) ou de supprimer des règles tout en en conservant l'expressivité ont échouées. Ceci conforte l'idée selon la quelle :

> Algorithme et machine de Turing sont deux modèles équivalents
{: .note}

C'est ce qu'on appelle [la thèse de Church-Turing](https://plato.stanford.edu/entries/turing-machine/#ThesDefiAxioTheo) : tout ce qu'un humain, une machine, ou encore un système physique peut calculer  est exactement égal à ce qu'une machine de Turing peut calculer.

## algorithmes et démonstration mathématiques

On n'en parlera pas trop dans ce cours (à moins que vous me le demandiez très fort) mais, en gros, les mathématiques sont une partie de l'informatique (certains diraient même, et réciproquement. Des mathématiciens certainement...).

De façon plus précise on a la suite d'équivalences :

1. faire une démonstration consiste — à partir d'une série finie d'axiomes — à effectuer une suite finie de déductions pour parvenir à un résultat. ([Aristote](https://fr.wikipedia.org/wiki/Aristote#Enqu%C3%AAte,_d%C3%A9monstration_et_syllogisme), en -350 environ)
2. (1) est équivalent à démontrer à l'aide d'une suite finie de déductions qu'une proposition logique est vraie ([Hilbert](https://fr.wikipedia.org/wiki/Syst%C3%A8me_%C3%A0_la_Hilbert), début XXe siècle)
3. (en passant, [Gödel](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8mes_d%27incompl%C3%A9tude_de_G%C3%B6del), en 1931, démontre qu'il existe des propositions logiques qui sont vraies mais qu'il est impossible de démontrer)
4. [Curry puis Howard qui généralise](https://fr.wikipedia.org/wiki/Correspondance_de_Curry-Howard), en 1950 et 1980, montrent que (2) est équivalent à écrire en terme de [$\lambda$-calcul](https://fr.wikipedia.org/wiki/Lambda-calcul)
5. [Turing](https://fr.wikipedia.org/wiki/Alan_Turing) démontre en 1937, que (4) est équivalent à écrire une machine de Turing.
6. (en passant, Turing démontre qu'il existe des machines de Turing qui ne s'arrêtent jamais et que savoir si une machine de Turing va s'arrêter est [indécidable](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt), ce qui est équivalent à (3))

## Conclusion

Code, pseudo-code et machine de Turing sont un seul et même modèle.

On pense même très fort que c'est exactement la même chose qu'un algorithme ([la thèse de Church-Turing](https://plato.stanford.edu/entries/turing-machine/#ThesDefiAxioTheo)) : tout ce qui peut se décrire de façon finie peut se décrire comme une machine de Turing ou un pseudo-code.

> En bons informaticiens, c'est exactement ce que l'on supposera par la suite : on utilisera indifféremment les notions d'algorithme, de pseudo-code, de code ou encore de machine de Turing.
{: .attention}

Enfin, cette équivalence  signifie que l'on doit toujours utiliser le formalisme (ou langage) qui est le plus simple pour résoudre le problème qu'on s'est fixé :

* d'algorithmie : on utilisera les mots du pseudo-code les plus adaptés, dans le respect des 4 règles fondamentales (chaque instruction doit être simple ou explicitée)
* de code : on utilisera le langage qui est plus adapté à notre problème car ils ont tous leurs spécificités. Il est donc impératif d'apprendre plus d'un langage et surtout d'apprendre à en changer quand on change de problème à résoudre.
* théorique : on utilisera [la machine de Turing]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %}), modèle théorique simple qui permet d'appréhender tout ce qui est calculable.

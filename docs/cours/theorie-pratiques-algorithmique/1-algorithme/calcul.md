---
layout: page
title:  "Algorithme : calcul"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithme]({% link cours/theorie-pratiques-algorithmique/1-algorithme/index.md %}) / [calcul]({% link cours/theorie-pratiques-algorithmique/1-algorithme/calcul.md %})
{: .chemin}

Dans [la partie précédente]({% link cours/theorie-pratiques-algorithmique/1-algorithme/pseudo-code.md %}), on a donné une façon d'écrire des pseudo-codes. Mais est-ce la seule façon de faire ? Et, au final, que peut-on réellement faire avec un algorithme ?

## calcul ?

Un algorithme, [on l'a vu]({% link cours/theorie-pratiques-algorithmique/1-algorithme/index.md %}#algorithme), est un ensemble de règles propre à un **calcul**. La [définition de calcul](https://dictionnaire.lerobert.com/definition/calcul) du Petit Robert est cependant très générale et ne pose pas vraiment la question du choix des règles, de comment réaliser effectivement ce calcul. On s'accorde (voir [la page wikipedia sur la calculabilité](https://fr.wikipedia.org/wiki/Th%C3%A8se_de_Church#Formulation_de_la_th%C3%A8se)) à garder **4 règles générales** :

1. un algorithme possède un ensemble fini de règles, décrites avec un nombre fini de symboles
2. si l'algorithme produit un résultat cela doit être fait après un nombre fini d'étapes
3. un humain doit pouvoir suivre chaque étape avec un papier et un crayon
4. exécuter une règle ne doit pas nécessiter d'intelligence (à part celle pour comprendre la règle)

Tout ça est un peu plus précis. On constate que c'est le terme **fini** qui revient constamment : pour qu'un humain comprenne, et surtout puisse agir, il faut pas qu'il y ait un nombre infini de choses à regarder (chaque chose à faire prend un temps de réflexion non nulle, une instruction contenant un nombre infini n'est humainement pas réalisable).

Cette remarque, évidente, a une conséquence fondamentale : on ne peut pas manipuler de réels en tant que tels ! On ne peut considérer un réel dans un algorithme que comme une abstraction (un symbole particulier) ou une approximation (on ne considère qu'un nombre fini de décimale).

> Prenons $\pi$ par exemple. On peut le considérer de deux manières : comme le symbole $\pi$ et de là faire de opérations sur lui (comme $2 \cdot \pi$, ou $\frac{3\pi}{3}$, ...) de façon formelle, c'est à dire sans jamais connaitre sa valeur ou comme une valeur approchée de lui (3.1415 par exemple) et ainsi rendre des valeurs approchées des différentes opérations. On ne pourra cependant **jamais** avoir la valeur exacte de $\pi$ avec un algorithme (et ce même s'il avait une mémoire infinie).

Lorsque dans un algorithme on utilise des réels ce seront toujours des approximations (on utilise la norme [IEEE 754](https://fr.wikipedia.org/wiki/IEEE_754) la plupart du temps). Ce n'es pas bien grave dans la plupart du temps puisque les lois physiques sont presque tout le temps stables (de petits effets impliquent de petites causes) mais, parfois, c'est problématique pour le calcul d'effets chaotiques comme la météo où [de petits effets produisent de grandes causes](https://fr.wikipedia.org/wiki/Effet_papillon).

> fini ne veut pas dire petit. Un algorithme peut utiliser des nombres entiers aussi grand qu'il le veut, du moment qu'ils ne soient pas infini
{: .attention}

Si c'est embêtant pour les réels, ce ne l'est pas pour les chaines de caractères qu'on a également utilisé dans la partie précédente pour définir un pseudo-code, car on peut facilement associer un entier à toute lettre. C'est le but du [codage unicode](https://fr.wikipedia.org/wiki/Unicode) par exemple.

Les règles que l'on a défini [précédemment]({% link cours/theorie-pratiques-algorithmique/1-algorithme/pseudo-code.md %}#regles) pour écrire un pseudo-code respectent alors les règles ci-dessus si on enlève les réels comme objets basique. On peut même se restreindre [sans perte de généralité](https://en.wikipedia.org/wiki/Structured_program_theorem) (même si ce sera plus compliqué d'écrire le code) aux règles suivantes (il n'y a même pas besoin de récursivité) :

* de lire et d'affecter des entiers à des variables
* d'avoir un test d'égalité entre deux variables
* d'exécuter une instruction puis un autre, séquentiellement
* exécuter une instruction si un test d'égalité est vraie
* exécuter un bloc d'instructions tant qu'un test d'égalité est vraie

Tous les pseudo-code utilisant les 5 règles ci-dessus auront la même expressivité (on pourra faire exactement les même choses) que ceux utilisant [les règles]({% link cours/theorie-pratiques-algorithmique/1-algorithme/pseudo-code.md %}#regles) utilisées couramment.

On pense même (c'est ce qu'on appelle la [thèse de Church-Turing](https://fr.wikipedia.org/wiki/Th%C3%A8se_de_Church)) que quelque soit les règles qu'on va se donner, du moment qu'elles respectent les 4 règles générales, alors on ne pourra pas calculer plus de choses.

## systèmes de règles équivalents

Les règles qu'on s'est donné pour écrire du pseudo-code vont être pratique pour décrire un algorithme pour un humain. Le fait qu'une fois posées, les règles ne nécessitent pas d'intelligence pour être exécutées, les rendent même accessible à des étudiants ! Mais elles sont encore un peut trop vagues pour être utilisées comme outils de preuve ou comme programme informatique.

Il existent heureusement de nombreuses façons d'interpréter les 4 règles générales d'un calcul. On peut déjà le voir dans la multitude de langages informatiques qui existent, allant de [l'assembleur](https://fr.wikipedia.org/wiki/Assembleur) compréhensible par les processeurs de nos ordinateurs au [python](https://fr.wikipedia.org/wiki/Python_(langage)) que tout le monde connait, en passant par le [haskell](https://fr.wikipedia.org/wiki/Haskell) ou encore le [C](https://fr.wikipedia.org/wiki/C_(langage)). Et bien tous ces langages calculent exactement la même chose (mais de façon différente) ! On trouve même des langages désignées pour être les plus simples possibles (appelés [turing tarpit](https://fr.wikipedia.org/wiki/Langage_de_programmation_exotique)) et permettant de calculer tout ce qu'on peut faire en python par exemple, comme le [brainfuck](https://fr.wikipedia.org/wiki/Brainfuck) qui est le plus célèbres d'entres eux.

> fun fact, on peut utiliser aussi certains jeu comme langage de programmation comme factorio ([l'algorithme de tri [quicksort](https://www.youtube.com/watch?v=ts5EKp9w4TU)), ou encore minecraft ([algorithme](https://www.youtube.com/watch?v=SrExOQ1yqgw) qui calcule $\sqrt{2}$).

Cette diversité de réponses est aussi vrai d'un point de vue théorique avec les modèles de [la machine de Turing](https://fr.wikipedia.org/wiki/Machine_de_Turing) ou encore le [$\lambda$-calcul](https://fr.wikipedia.org/wiki/Lambda-calcul) qui, et c'est prouvé, calculent exactement les mêmes choses.

Tous ces exemples, plus bien d'autres essais, tendent à [accréditer la thèse de church-turing](https://plato.stanford.edu/entries/church-turing/#ReasForAcceThes) selon laquelle tout ce qu'un humain, une machine, ou encore un système physique peut calculer est exactement égal à ce qu'une machine de Turing peut calculer.

Pour répondre à notre question initiale, *que peut-on calculer ?*, on peut alors étudier ce que peut calculer la machine de Turing.

## machine de Turing

Il existe plusieurs définition équivalente d'une machine de turing. Nous allons utiliser [celle de wikipedia](https://fr.wikipedia.org/wiki/Machine_de_Turing#D%C3%A9finition_formelle) :

Une **machine de Turing** est un quintuplet $(Q, \Gamma, q_0, \delta, F)$ où :

* $Q$ est un ensemble fini d'**état**
* $\Gamma$ est l'**alphabet de travail**. Il contient un symbole spécial $B$, dit **blanc**, avec $B \in \Gamma$
* $q_0 \in Q$ est l'**état initial** de la machine
* $\delta : Q \times \Gamma \rightarrow Q \times \Gamma \times \\{ \leftarrow, \rightarrow \\}$ est la **fonction de transition**
* $F \subset Q$ est l'ensemble des **états finaux**.

> On appelle cette machine, machine de Turing déterministe car $\delta$ est une fonction.

Pour fonctionner la machine nécessite un **ruban** constitué de cases contiguës pouvant chacune contenir un élément de $\Gamma$ et un **curseur** qui est positionné sur une case du ruban. Initialement toutes les cases du ruban contiennent le symbole `B`.

L'exécution d'un programme est alors comme suit :

1. on place la tête de lecture sur une case du ruban
2. on initialise si besoin le ruban avec une chaine de caractères (finie) contenant des caractères de $\Gamma$ et on place le curseur sur la première case de la chaine.
3. si l'état de la machine est un élément de $F$, on stoppe le programme.
4. on lit le caractère $a$ sous le curseur, et l'état $q$ de la machine et on note $(a', q', f) = \delta(a, q)$
5. on écrit $q'$ dans la case du ruban pointé par le curseur, on place la machine dans l'état $q'$ et on déplace le curseur vers la gauche si $f$ vaut $\leftarrow$ et vers la droite sinon ($f$ vaut $\rightarrow$)
6. retour en 3.

### exemples de programmes

#### doublement des bâtons

Exemple classique des machines de Turing, le doublement des bâtons s'écrit comme ça :

* $Q = \\{ s, e, l, g, d\\}$
* $\Gamma = \\{ 1, B\\}$
* $q_0 = s$
* $F = \\{ e \\}$
* $\delta(s, 1) = (B, l, \leftarrow)$
* $\delta(l, B) = (1, g, \leftarrow)$
* $\delta(g, 1) = (1, g, \leftarrow)$
* $\delta(g, B) = (1, d, \rightarrow)$
* $\delta(d, 1) = (1, d, \rightarrow)$
* $\delta(d, B) = (B, s, \rightarrow)$
* $\delta(s, B) = (B, e, \rightarrow)$

On initialise cette machine avec une chaine de 1.

Si vous ne voulez pas tester votre machine à la main, vous pouvez utiliser <https://turingmachine.io/>. Le code précédent a été traduit dans leur formalisme ci-dessous :

```text
input: '1111'
blank: 'B'
start state: start
table:
  start:
    1: {write: 'B', L: lien}
    'B': {R: done}
  lien:
    'B': {write: 1, L: gauche}
  gauche:
    1: {write: 1, L: gauche}
    'B': {write: 1, R: droite}
  droite:
    1: {write: 1, R: droite}
    'B': {write: 'B', R: start}
  done:
```

Son fonctionnement est le suivant. On commence par remplacer le premier 1 par un blanc. Puis on se déplace de une case sur la gauche et on écrit 1, puis on se déplace encore une fois à gauche. Une fois là, on se déplace autant de fois que nécessaire sur la gauche jusqu'à arriver sur une case avec B (au début, on a pas besoin de bouger). Arrivé là on écrit 1, puis on se déplace autant de fois que nécessaire sur la droite jusqu'à arriver sur une case B. Arrivé là, on se déplace à droite et on replace la machine de Turing à son été initial pour recommencer si nécessaire.

Félicitations ! Vous venez d'implémenter la fonction $f(n) = 2n$ dans une machine de Turing.

#### autres exemples

Le site <https://turingmachine.io/> contient plusieurs exemple de programmes. Testez les et essayer de les comprendre.

### modèles équivalents

Il existent de nombreuses variations des machines de Turing qui sont toutes équivalentes. Par exemple on peut dissocier le fait de se déplacer et d'écrire des caractères (comme [ici](http://zanotti.univ-tln.fr/turing/)), on peut même utiliser plusieurs rubans et/ou plusieurs curseurs, ça revient au même on ne calculera pas plus de choses. Ce sera juste plus simple à programmer.

Enfin, [la machine de Turing non déterministe](https://fr.wikipedia.org/wiki/Machine_de_Turing_non_d%C3%A9terministe), même si elle a l'air très puissante, ne change rien à ce qu'on peut calculer. On peut juste le faire plus vite.

### équivalence pseudo-code et machine de Turing

Ce qui est magnifique, c'est que le modèle très simple de la machine de Turing permet de calculer tout ce qu'on peut faire avec nos pseudo-code. On ne démontrera pas ce fait, on va juste montrer comment on peut montrer que nos pseudo-code et la machine travaillent sur les mêmes objets.

entier, chaine de caractères c'est des entiers. Donc u pseudo code est une fonction de f(n1, ..., nk) dans n.

### fonctions calculables

### nombres calculables




* que peut-on calculer ? 
* de pseudo code à calcul de f(N) -> N

## turing complet
si on peut faire une machine de turing dans notre programme on est turing complet.

machine de turing universelle

> TBD
> * turing : pb de l'arrêt de la machine ?
> 

pour l'instant tous les pseudo-code qu'on a écrit s'arrêtent tout le temps. Mais celui là ? syracuse. On ne sais pas. 

## arrêt de la machine



des actions sussessivent qui ment au résultat : ce n'est pas immédiat ! Et on ne sais pas si ça s'arrête.

passer d'un pseudo code à la machine. entier/réels/chaine de caractères. Permet de voir théoriquement ce qu'on peut faire.


## logique, démonstrations mathématiques et calculabilité


démonstation = pseudo-code

## refs

<https://plato.stanford.edu/entries/church-turing/>
<http://pageperso.lif.univ-mrs.fr/~kevin.perrot/documents/2016/calculabilite/Cours_16.pdf>
<https://www.cs.odu.edu/~zeil/cs390/latest/Public/turing-complete/index.html>
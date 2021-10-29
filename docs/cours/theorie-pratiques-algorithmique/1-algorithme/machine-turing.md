---
layout: page
title:  "Algorithme : machine de Turing"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithme]({% link cours/theorie-pratiques-algorithmique/1-algorithme/index.md %}) / [machine de turing]({% link cours/theorie-pratiques-algorithmique/1-algorithme/machine-turing.md %})
{: .chemin}

> TBD :
> blanc = #
> rpond à la question que'est-ce qu'un ordnateur
{: .attention}


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

> L'article fondateur d'Allan Turing est [là](http://www.espace-turing.fr/IMG/pdf/turing_oncomputablenumbers_1936.pdf)

### exemples de programmes

#### répéteur

Répète des suite de 0 et 1 :



TBD : les lignes pour voir ce que ça fait

C'est le premier exemple de <https://turingmachine.io/> (repeat 0 1)

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

TBD : montrer sur des schémas.


Félicitations ! Vous venez d'implémenter la fonction $f(n) = 2n$ dans une machine de Turing.

#### premier programme (au monde)

L'exemple suivent est le [premier programme](https://machinedeturing.com/exemple.php?page=9) donné par Allan Turing lorsqu'il décrivit sa machine.



#### autres exemples

Le site <https://machinedeturing.com/> contient de nombreux exemples de programmes de machine de Turing

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

<https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Rice>
<https://en.wikipedia.org/wiki/List_of_undecidable_problems>

démonstation = pseudo-code

## refs

<https://plato.stanford.edu/entries/church-turing/>
<http://pageperso.lif.univ-mrs.fr/~kevin.perrot/documents/2016/calculabilite/Cours_16.pdf>
<https://www.cs.odu.edu/~zeil/cs390/latest/Public/turing-complete/index.html>
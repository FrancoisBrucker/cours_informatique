---
layout: page
title:  "Algorithme : machine de Turing"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithme]({% link cours/theorie-pratiques-algorithmique/1-algorithme/index.md %}) / [machine de turing]({% link cours/theorie-pratiques-algorithmique/1-algorithme/machine-turing.md %})
{: .chemin}

Pour répondre à notre question initiale, *que peut-on calculer ?*, on peut alors étudier ce que peut calculer la machine de Turing.

## définition

Il existe plusieurs définition équivalente d'une machine de Turing. Nous allons utiliser [celle de wikipedia](https://fr.wikipedia.org/wiki/Machine_de_Turing#D%C3%A9finition_formelle) :

Une **machine de Turing** est un quintuplet $(Q, \Gamma, q_0, \delta, F)$ où :

* $Q$ est un ensemble fini d'**état**
* $\Gamma$ est l'**alphabet de travail**. Il contient un symbole spécial $\sharp$, dit **blanc**, avec $\sharp \in \Gamma$
* $q_0 \in Q$ est l'**état initial** de la machine
* $\delta : Q \times \Gamma \rightarrow Q \times \Gamma \times \\{ \leftarrow, \rightarrow \\}$ est la **fonction de transition**
* $F \subset Q$ est l'ensemble des **états finaux**.

> On appelle cette machine, machine de Turing déterministe car $\delta$ est une fonction.

Pour fonctionner, la machine nécessite :

* un **ruban** constitué de cases contiguës pouvant chacune contenir un élément de $\Gamma$
* un **curseur** qui est positionné sur une case du ruban

Initialement toutes les cases du ruban contiennent le symbole $\sharp$.

L'exécution d'un programme est alors comme suit :

1. on place la tête de lecture sur une case du ruban
2. on initialise si besoin le ruban avec une chaine de caractères (finie) contenant des caractères de $\Gamma$ et on place le curseur sur la première case de la chaine.
3. si l'état de la machine est un élément de $F$, on stoppe le programme.
4. on lit le caractère $a$ sous le curseur, et l'état $q$ de la machine et on note $(a', q', f) = \delta(a, q)$
5. on écrit $q'$ dans la case du ruban pointé par le curseur, on place la machine dans l'état $q'$ et on déplace le curseur vers la gauche si $f$ vaut $\leftarrow$ et vers la droite sinon ($f$ vaut $\rightarrow$)
6. retour en 3.

> L'article où d'Allan Turing décrit cette machine est [là](http://www.espace-turing.fr/IMG/pdf/turing_oncomputablenumbers_1936.pdf)

## exemples de programmes

### répéteur

Le premier exemple donné par Allan Turing est celui-ci :

* $Q = \\{ a, b, c, d \\}$
* $\Gamma = \\{ 0, 1, \sharp \\}$
* $q_0 = a$
* $F = \emptyset$
* $\delta(a, \sharp) = (0, b, \rightarrow)$
* $\delta(b, \sharp) = (\sharp, c, \rightarrow)$
* $\delta(c, \sharp) = (1, d, \rightarrow)$
* $\delta(d, \sharp) = (\sharp, a, \rightarrow)$

La fonction $\delta$ est ici partielle, avec la convention que si l'on arrive dans une configuration non décrite, on stoppe la machine (on peut donc étendre $\delta$ à tout $Q \times \Gamma$ si on le voulait).

Allons-y. Essayons ce code. On considère la machine de Turing ci-après :

![turing 1]({{ "/assets/cours/algorithmie/turing-1.png" | relative_url }}){:style="margin: auto;display: block;"}

On est à l'état $a$ et on lit $\sharp$ dans la machine : la table de transition nous indique qu'il faut :

* écrire $0$
* passer dans l'état $b$
* aller à droite

![turing 2]({{ "/assets/cours/algorithmie/turing-2.png" | relative_url }}){:style="margin: auto;display: block;"}

On est à l'état $b$ et on lit $\sharp$ dans la machine : la table de transition nous indique qu'il faut :

* écrire $\sharp$
* passer dans l'état $c$
* aller à droite

![turing 3]({{ "/assets/cours/algorithmie/turing-3.png" | relative_url }}){:style="margin: auto;display: block;"}

On est à l'état $c$ et on lit $\sharp$ dans la machine : la table de transition nous indique qu'il faut :

* écrire $1$
* passer dans l'état $d$
* aller à droite

![turing 4]({{ "/assets/cours/algorithmie/turing-4.png" | relative_url }}){:style="margin: auto;display: block;"}

On est à l'état $d$ et on lit $\sharp$ dans la machine : la table de transition nous indique qu'il faut :

* écrire $\sharp$
* passer dans l'état $a$
* aller à droite

![turing 5]({{ "/assets/cours/algorithmie/turing-5.png" | relative_url }}){:style="margin: auto;display: block;"}

Et ainsi de suite. On voit que cette machine ne va jamais s'arrêter et qu'elle écrit continuellement 0 puis 1 sur le ruban.

Si vous voulez le voir en action, allez sur <https://turingmachine.io/>. C'est le premier exemple (repeat 0 1).

Le site représente la machine sous la forme de son diagramme de transition. Les nœuds représentent l'état de la machine et sur l'arc est représenté la transition selon selon la lecture sur le ruban.

### doublement des bâtons

Exemple classique des machines de Turing, le doublement des bâtons s'écrit comme ça :

|      | 1                         | $\sharp$                   |
|------|---------------------------|----------------------------|
|**s** | $(\sharp, l, \leftarrow)$ | $(\sharp, e, \rightarrow)$ |
|l     |                           | $(1, g, \leftarrow)$       |
|g     | $(1, g, \leftarrow)$      | $(1, d, \rightarrow)$      |
|d     | $(1, d, \rightarrow)$     | $(\sharp, s, \rightarrow)$ |

On a représenté la machine sous la forme d'un tableau où les état sont des lignes et chaque colonne est un élément de l'alphabet. L'état initial est la première ligne et les états finaux sont ceux qui n'ont pas de ligne (ici $e$).

On initialise cette machine avec une chaine de 1.

Si vous ne voulez pas tester votre machine à la main, Le code précédent a été traduit ci-dessous dans le formalisme de <https://turingmachine.io/> :

```text
input: '1111'
blank: '#'
start state: start
table:
  start:
    1: {write: '#', L: lien}
    '#': {R: done}
  lien:
    '#': {write: 1, L: gauche}
  gauche:
    1: {write: 1, L: gauche}
    '#': {write: 1, R: droite}
  droite:
    1: {write: 1, R: droite}
    '#': {write: '#', R: start}
  done:
```

Son fonctionnement est le suivant. On commence par remplacer le premier 1 par un blanc. Puis on se déplace de une case sur la gauche et on écrit 1, puis on se déplace encore une fois à gauche (l'état $l$ ne sert qu'à ça). Une fois là, on se déplace autant de fois que nécessaire sur la gauche jusqu'à arriver sur une case avec $\sharp$ (au début, on a pas besoin de bouger). Arrivé là on écrit 1, puis on se déplace autant de fois que nécessaire sur la droite jusqu'à arriver sur une case $\sharp$. Arrivé là, on se déplace à droite et on replace la machine de Turing à son été initial pour recommencer si nécessaire.

A chaque itération, la machine supprime un 1 et en écrit 2 nouveaux : un à droite et un à gauche des nouveaux 1 inscrits. Les étapes de cette itération poeut être décrite comme suit :

![turing 6]({{ "/assets/cours/algorithmie/turing-6.png" | relative_url }}){:style="margin: auto;display: block;"}

On aura toujours une configuration où les nouveaux 1 seront à gauche des anciens 1 (ceux initialement sur le ruban) et séparé par **un unique caractère blanc** :

![doublement de batons]({{ "/assets/cours/algorithmie/turing-7.png" | relative_url }}){:style="margin: auto;display: block;"}

Le programme de la machine de Turing a machine va donc ici s'arrêter puisqu'à un moment tous les anciens $1$ auront-été effacés et on se retrouvera à l'état initial avec le curseur placé sur un $\sharp$ , ce qui enverra vers l'état final.

> Félicitations ! Vous venez d'implémenter la fonction $f(n) = 2n$ dans une machine de Turing.

### autres programmes

Le site <https://turingmachine.io/> contient bien d'autres programmes à essayer. Vous pouvez aussi aller du côté de <https://machinedeturing.com/> pour aller voir le programme donné par Turing pour [générer tous les entiers](https://machinedeturing.com/exemple.php?page=9).

## substantifique moelle de la machine de Turing

> TBD :
> Qu'est ce qui est vraiment important dans la définition d'une machine de Turing ?
> nb de ruban, curseurs, alphabet et fonction de transition.

### généralisation du modèle : inutile

Il existent de nombreuses généralisations des machines de Turing, mais elles ne permettent pas de calculer plus de choses :

* par exemple des machines utilisant [plusieurs rubans et/ou plusieurs curseurs](https://perso.liris.cnrs.fr/sylvain.brandel/wiki/lib/exe/fetch.php?media=ens:m1if09:m1if09-cm03.pdf). L'intérêt de ces machines est qu'elle sont plus facilement programmables.
* Il existe aussi, [la machine de Turing non déterministe](https://fr.wikipedia.org/wiki/Machine_de_Turing_non_d%C3%A9terministe), qui n'utilise pas une fonction de transition mais une relation. Même si elle a l'air très puissante, ne change rien à ce qu'on peut calculer, elles permettent juste de le faire plus vite.

> On est intimement persuadé (c'est [la thèse de Church-Turing](https://plato.stanford.edu/entries/church-turing/#ReasForAcceThes)) que tout ce qu'un humain, une machine, ou encore un système physique peut calculer (c'est à dire en suivant les 4 règles générales) est exactement égal à ce qu'une machine de Turing peut calculer.
{: .note}

### alphabet : inutile

Diminuer ou agrandir l'alphabet d'une machine de Turing ne permet pas de calculer plus de choses :

> On peut simuler toute machine de Turing par une machine de Turing sur un alphabet $\\{\sharp, 1\\}$.
{: .note}

Idée de la preuve. Comme l'alphabet $\Gamma$ d'une machine de Turing est fini, on peut associer à chaque lettre non blanc un numéro allant de $1$ à $\vert \Gamma \vert$, puis coder celui-ci par le mot $\sharp\sharp\sharp \dots \sharp\sharp\sharp 111 \dots 111$ de longueur $\vert \Gamma \vert$ et ayant autant de $1$ que la valeur de son numéro. On termine par coder le caractère blanc par uen suite de $\Gamma$ caractères $\sharp$. Une fois cette traduction d'alphabet effectué, on modifie les transitions pour qu'elles se déplacent de $\vert \Gamma \vert$ cases à chaque fois en utilisant des états transitoires (voir par exemple la [partie 14.4.1. de ce document](http://math.univ-lyon1.fr/~blossier/odi2009/chap14.pdf)).

On montre par là que :

> Une machine de Turing est un fonction  $f: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}$ (de l'ensemble des mots formées de suite de $0$ et de $1$) dans $\\{0, 1\\}$).
{: .note}

### fonction de transition : inutile

Ce qui différentie une machine de Turing d'une autre c'est l'alphabet et la fonction de transition. On a vu qu'on pouvait utiliser un alphabet commun ($\\{ \sharp, 1\\}$$), peut-on faire la même chose avec la fonction de transition ?

La réponse es surprenante, mais c'est oui ! On peut créer une [Machine de Turing universelle](https://fr.wikipedia.org/wiki/Machine_de_Turing_universelle) qui, calcule tout ce que peut calculer les machines de Turing.

Une machine Turing est dédiée à faire un calcul précis, déterminé par la fonction de transition et l'entrée. Il nous faut en plus un opérateur qui exécute la machine de Turing pas à pas.

En appliquant notre formalisme à un ordinateur, la machine de Turing est le programme. Turing montre qu'en fait ces deux choses ne sont qu'une seule et même entité :

## équivalences

Le modèle de la machine de Turing est important car, malgré sa simplicité, il permet de capturer tout ce que peu faire un ordinateur. De plus, de nombreux modèle plus compliqué n'arrivent pas à calculer plus.

On peut même montrer qu'une machine de Turing est elle même équivalent à un ordinateur !

### pseudo-code et machine de Turing

[On l'a vu]({% link cours/theorie-pratiques-algorithmique/1-algorithme/calcul.md %}), les algorithmes décrits par leur [pseudo-code]({% link cours/theorie-pratiques-algorithmique/1-algorithme/pseudo-code.md %}#regles) permettent de calculer certaines fonctions de $f: \mathbb{N} \rightarrow \mathbb{N}$.

Ce que Turing a montré c'est que :

> le modèle très simple de la machine de Turing permet exactement de calculer tout ce qu'on peut faire avec un pseudo-code [tel qu'on l'a défini ]({% link cours/theorie-pratiques-algorithmique/1-algorithme/pseudo-code.md %}#regles).
{: .note}

On admettra ce fait, mais l'idée de la preuve est de montrer que l'on peut avec une machine de Turing :

* faire de boucles
* évaluer des expressions logiques
* stocker et lire des entiers

### ordinateur et machine de Turing

avec la MTU

## problème de l'arrêt


## fonctions calculables



## nombres calculables




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
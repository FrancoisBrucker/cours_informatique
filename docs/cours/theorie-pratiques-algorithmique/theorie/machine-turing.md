---
layout: page
title:  "Algorithme : machine de Turing"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [théorie]({% link cours/theorie-pratiques-algorithmique/theorie/index.md %}) / [machine de Turing]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %})
>
>prérequis :
>
>* [algorithmie/pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %})
{: .chemin}

Pour répondre à notre question initiale, *que peut-on calculer ?*, on peut alors étudier ce que peut calculer la machine de Turing. Le modèle de la machine de Turing est important car, malgré sa simplicité, il permet de capturer tout ce que peu faire un ordinateur. De plus, de nombreux modèle plus compliqué n'arrivent pas à calculer plus.

On peut même montrer qu'une machine de Turing est elle même équivalent à un ordinateur !

[On l'a vu]({% link cours/theorie-pratiques-algorithmique/theorie/calcul.md %}), les algorithmes décrits par leur [pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#regles) permettent de calculer certaines fonctions de $f: \mathbb{N} \rightarrow \mathbb{N}$.

Ce que Turing a montré c'est que :

> le modèle très simple de la machine de Turing permet exactement de calculer tout ce qu'on peut faire avec un pseudo-code [tel qu'on l'a défini]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#regles).
{: .note}

L'idée de la preuve est de montrer que l'on peut avec une machine de Turing :

* faire de boucles
* évaluer des expressions logiques
* stocker et lire des entiers

## définition

Il existe plusieurs définition équivalente d'une machine de Turing. Nous allons utiliser [celle de wikipedia](https://fr.wikipedia.org/wiki/Machine_de_Turing#D%C3%A9finition_formelle) :

Une **machine de Turing** est un quintuplet $(Q, \Gamma, q_0, \delta, F)$ où :

* $Q$ est un ensemble fini d'**état**
* $\Gamma$ est l'**alphabet de travail**. Il contient un symbole spécial $\sharp$, dit **blanc**, avec $\sharp \in \Gamma$
* $q_0 \in Q$ est l'**état initial** de la machine
* $\delta : Q \times \Gamma \rightarrow Q \times \Gamma \times \\{ \leftarrow, \rightarrow \\}$ est la **fonction de transition**
* $F \subset Q$ est l'ensemble des **états finaux**.

> On appelle cette machine, machine de Turing **déterministe** car $\delta$ est une fonction.

Pour fonctionner, la machine nécessite :

* un **ruban** constitué de cases contiguës pouvant chacune contenir un élément de $\Gamma$
* un **curseur** qui est positionné sur une case du ruban

Initialement toutes les cases du ruban contiennent le symbole $\sharp$.

Voici la représentation d'une machine à la fin de la $i$ème instruction. Son état est $q$ et son curseur est positionné sur la case d'indice $j$ :

![machine]({{ "/assets/cours/algorithmie/machine-Turing.png" | relative_url }}){:style="margin: auto;display: block;"}

Par convention, on considérera que le ruban initial aura comme numéro d'instruction 0 et que l'indice de la case où est initialement le curseur sera d'indice 0.

L'exécution d'un programme est alors comme suit :

1. on place la tête de lecture sur une case du ruban
2. on initialise si besoin le ruban avec une chaine de caractères (finie) contenant des caractères de $\Gamma$ et on place le curseur sur la première case de la chaine.
3. si l'état de la machine est un élément de $F$, on stoppe le programme.
4. on lit le caractère $a$ sous le curseur, et l'état $q$ de la machine et on note $(a', q', f) = \delta(a, q)$
5. on écrit $q'$ dans la case du ruban pointé par le curseur, on place la machine dans l'état $q'$ et on déplace le curseur vers la gauche si $f$ vaut $\leftarrow$ et vers la droite sinon ($f$ vaut $\rightarrow$)
6. retour en 3.

> L'article où d'Allan Turing décrit cette machine est [là](http://www.espace-Turing.fr/IMG/pdf/Turing_oncomputablenumbers_1936.pdf)

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

![Turing 1]({{ "/assets/cours/algorithmie/Turing-1.png" | relative_url }}){:style="margin: auto;display: block;"}

Par convention, on considérera que le ruban initial aura comme numéro d'instruction 0 et que l'indice de la case où est initialement le curseur sera d'indice 0.

On est à l'état $a$ et on lit $\sharp$ dans la machine : la table de transition nous indique qu'il faut :

* écrire $0$
* passer dans l'état $b$
* aller à droite

![Turing 2]({{ "/assets/cours/algorithmie/Turing-2.png" | relative_url }}){:style="margin: auto;display: block;"}

On est à l'état $b$ et on lit $\sharp$ dans la machine : la table de transition nous indique qu'il faut :

* écrire $\sharp$
* passer dans l'état $c$
* aller à droite

![Turing 3]({{ "/assets/cours/algorithmie/Turing-3.png" | relative_url }}){:style="margin: auto;display: block;"}

On est à l'état $c$ et on lit $\sharp$ dans la machine : la table de transition nous indique qu'il faut :

* écrire $1$
* passer dans l'état $d$
* aller à droite

![Turing 4]({{ "/assets/cours/algorithmie/Turing-4.png" | relative_url }}){:style="margin: auto;display: block;"}

On est à l'état $d$ et on lit $\sharp$ dans la machine : la table de transition nous indique qu'il faut :

* écrire $\sharp$
* passer dans l'état $a$
* aller à droite

![Turing 5]({{ "/assets/cours/algorithmie/Turing-5.png" | relative_url }}){:style="margin: auto;display: block;"}

Et ainsi de suite. On voit que cette machine ne va jamais s'arrêter et qu'elle écrit continuellement 0 puis 1 sur le ruban.

Si vous voulez le voir en action, allez sur <https://Turingmachine.io/>. C'est le premier exemple (repeat 0 1).

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

On initialise cette machine avec une chaine de 1. Par exemple, en commençant par un ruban valant `11`, on obtient la résolution suivante (la position du curseur est en orange) :

| instruction| ruban ||||||| état |
| ^^   |-3|-2|-1|0|1|2|3| ^^|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|----|--|--|--|-|-|-|-|----|
|0   |  #  |  #  |  #  | **1** {: .cls style=";background: orange" }|  1  |  #  |  #  | s  |
|1   |  #  |  #  | **#** {: .cls style=";background: orange" }|  #  |  1  |  #  |  #  | l  |
|2   |  #  | **#** {: .cls style=";background: orange" }|  1  |  #  |  1  |  #  |  #  | g  |
|3   |  #  |  1  | **1** {: .cls style=";background: orange" }|  #  |  1  |  #  |  #  | d  |
|4   |  #  |  1  |1| **#** {: .cls style=";background: orange" }|  1  |  #  |  #  | d  |
|5   |  #  |  1  |1|#| **1** {: .cls style=";background: orange" }|  #  |  #  | s  |
|6   |  #  |  1  |1| **#** {: .cls style=";background: orange" }|#|  #  |  #  | l |
|7   |  #  |  1  | **1** {: .cls style=";background: orange" }|1|#|  #  |  #  | g |
|8   |  #  | **1** {: .cls style=";background: orange" }|1|1|#|  #  |  #  | g |
|9   | **#** {: .cls style=";background: orange" }|1|1|1|#|  #  |  #  | g |
|10   |1| **1** {: .cls style=";background: orange" }|1|1|#|  #  |  #  | d |
|11   |1|1| **1** {: .cls style=";background: orange" }|1|#|  #  |  #  | d |
|12   |1|1|1| **1** {: .cls style=";background: orange" }|#|  #  |  #  | d |
|13   |1|1|1|1| **#** {: .cls style=";background: orange" }|  #  |  #  | d |
|14   |1|1|1|1|#| **#** {: .cls style=";background: orange" }|   #  | s |
|15   |1|1|1|1|#| #| **#** {: .cls style=";background: orange" } | e |

La machine s'arrête ! Avant de voir exactement pourquoi cette machine s'arrête, essayer de comprendre son fonctionnement. Si vous ne voulez pas tester votre machine à la main, Le code précédent a été traduit ci-dessous dans le formalisme de <https://Turingmachine.io/> avec une entrée de `1111` :

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

![Turing 6]({{ "/assets/cours/algorithmie/Turing-6.png" | relative_url }}){:style="margin: auto;display: block;"}

On aura toujours une configuration où les nouveaux 1 seront à gauche des anciens 1 (ceux initialement sur le ruban) et séparé par **un unique caractère blanc** :

![doublement de batons]({{ "/assets/cours/algorithmie/Turing-7.png" | relative_url }}){:style="margin: auto;display: block;"}

Le programme de la machine de Turing a machine va donc ici s'arrêter puisqu'à un moment tous les anciens $1$ auront-été effacés et on se retrouvera à l'état initial avec le curseur placé sur un $\sharp$ , ce qui enverra vers l'état final.

> Félicitations ! Vous venez d'implémenter la fonction $f(n) = 2n$ dans une machine de Turing.

Remarquez que par construction de la machine de Turing, le nombre d'opérations nécessaires pour exécuter le programme correspond aussi au nombre maximum de cases différentes du ruban qui ont peu être parcourues :

> Le nombre de cases du ruban parcouru par une machine de Turing est plus petit ou égal aux nombres d'instructions effectuées.
{: .note}

### autres programmes

Le site <https://Turingmachine.io/> contient bien d'autres programmes à essayer. Vous pouvez aussi aller du côté de <https://machinedeTuring.com/> pour aller voir le programme donné par Turing pour [générer tous les entiers](https://machinedeTuring.com/exemple.php?page=9).

Notez qu'il est facile de composer des machines de Turing ensemble en *concaténant* les paramètres (alphabets, fonction de compositions, états). On peut ainsi créer des gros programmes en assemblant des machines de Turing toutes simples. On peut ainsi plus ou moins facilement créer des machines de Turing qui :

* déplacent un caractère sur le ruban vers la gauche ou la droite
* mettent des bornes à gauche et à droite du rubans pour délimiter l'intervalle des cases modifiées par le programme à tout moment de son exécution
* cherchent une case contenant un caractère en particulier
* ...

## substantifique moelle de la machine de Turing

Le modèle de la machine de Turing admet quatre paramètres :

* un ruban
* un curseur
* l'alphabet
* une fonction de transitions

On peut se demander ce qui est vraiment utile là-dedans (peut-on simplifier le modèle sans perdre en expressivité ?) ou au contraire si complexifier le modèle permet de calculer plus de chose.

> On est intimement persuadé (c'est [la thèse de Church-Turing](https://plato.stanford.edu/entries/church-Turing/#ReasForAcceThes)) que tout ce qu'un humain, une machine, ou encore un système physique peut calculer (c'est à dire en suivant les 4 règles générales) est exactement égal à ce qu'une machine de Turing peut calculer.
{: .note}

### généralisation du modèle : inutile

Commençons par répondre à la seconde question : *est-ce que complexifier le modèle permet de calculer plus de chose ?* La réponse est **non**.

Il existent de nombreuses généralisations des machines de Turing, elles ne permettent pas de calculer plus de choses, mais sont utiles car elle permettent de calculer plus facilement/rapidement. Ces généralisations nous permettent d'écrire rapidement des programmes en sachant qu'on pourrait (si on en avait très envie) les écrire avec une machine de Turing normale.

#### machines à plusieurs rubans

Une machine de Turing à $k$ rubans peut être définie comme suit.

Une **machine de Turing à $k$ rubans** est un quintuplet $(Q, \Gamma, q_0, \delta_k, F)$ où :

* $Q$ est un ensemble fini d'**état**
* $\Gamma$ est l'**alphabet de travail**. Il contient un symbole spécial $\sharp$, dit **blanc**, avec $\sharp \in \Gamma$
* $q_0 \in Q$ est l'**état initial** de la machine
* $\delta_k : Q \times \Gamma^k \rightarrow Q \times \Gamma^k \times \\{ \leftarrow, \rightarrow \\}^k$ est la **fonction de transition**
* $F \subset Q$ est l'ensemble des **états finaux**.

Pour fonctionner, la machine nécessite :

* $k$ **rubans** constitués de cases contiguës pouvant chacune contenir un élément de $\Gamma$
* $k$ **curseurs**, un pour chaque ruban

Tout se passe comme pour la machine de Turing mais on lit la valeur des $k$ rubans, puis la fonction de transition écrit une valeur sur chaque ruban et déplace les curseurs de chaque ruban.

> On peut toujours transformer une machine à plusieurs rubans en une machine de Turing normale équivalente.
{: .note}

Nous n'allons pas donner la preuve complète de ceci, mais juste une idée de la preuve de comment simuler une machine à 2 rubans avec une machine avec un seul ruban.

Lorsque l'on a une machine à 2 rubans, on a un curseur pour chaque ruban. A chaque instruction on lit le contenu de chaque ruban sous le curseur et selon l'état de la machine on écrit su les 2 rubans puis on déplace chaque curseur vers la gauche ou la droite. On peut alors simuler les 2 rubans en un seul ruban en ajoutant une lettre $\bigtriangledown$ à l'alphabet et en découpant le ruban en paquets de 4 cases :

* la première case valant soit $\bigtriangledown$ si le curseur du premier ruban est sur cette case, soit $\sharp$ sinon,
* la deuxième case valant le caractère de la case sur le premier ruban
* la troisième case valant soit $\bigtriangledown$ si le curseur du second ruban est sur cette case, soit $\sharp$ sinon,
* la deuxième case valant le caractère de la case sur le second ruban

Enfin, on peut toujours s'arranger pour qu'au départ, le curseur du premier ruban et du second ruban soient sur le même paquet de 4 cases.

De là, à chaque itération de la machine à 1 seul ruban, on commence par chercher les paquets de 4 cases contenant les curseurs de chaque ruban et on lit leurs valeurs (on peut faire ça en parcourant le ruban jusqu'à trouver $\bigtriangledown$ en premier ou en troisième position d'un paquet à 4 cases) puis on effectue la fonction de transition de la machine à 2 rubans et on écrit les nouvelles valeurs en recherchant les positions respectives des curseurs dans les paquets à 4 cases.

#### machines à plusieurs curseurs

Plutôt que de multiplier les rubans, on peut aussi multiplier les curseurs :

Une **machine de Turing à $k$ curseurs** est un quintuplet $(Q, \Gamma, q_0, \delta_k, F)$ où :

* $Q$ est un ensemble fini d'**état**
* $\Gamma$ est l'**alphabet de travail**. Il contient un symbole spécial $\sharp$, dit **blanc**, avec $\sharp \in \Gamma$
* $q_0 \in Q$ est l'**état initial** de la machine
* $\delta_k : Q \times \Gamma^k \rightarrow Q \times \Gamma^k \times \\{ \leftarrow, \rightarrow \\}^k$ est la **fonction de transition**
* $F \subset Q$ est l'ensemble des **états finaux**.

Pour fonctionner, la machine nécessite :

* un **ruban** constitués de cases contiguës pouvant chacune contenir un élément de $\Gamma$
* $k$ **curseurs**, sur le ruban

Elle fonctionne de la même manière que la machine à $k$ rubans sauf qu'on lit les valeurs sur le même rubans.

> On peut toujours transformer une machine à plusieurs curseurs en une machine de Turing normale équivalente.
{: .note}

#### machines à plusieurs curseurs et rubans

On peut bien sur combiner les deux approches et construire une machine de Turing à $k$ rubans et $k'$ curseurs réparis sur les rubans. Mais, comme vous devers vous en douter :

> On peut toujours transformer une machine à plusieurs rubans et plusieurs curseurs en une machine de Turing normale équivalente.
{: .note}

#### machines de Turing non déterministe

Il existe aussi, [la machine de Turing non déterministe](https://fr.wikipedia.org/wiki/Machine_de_Turing_non_d%C3%A9terministe), qui se définit comme suit :

Une **machine de Turing non déterministe** est un quintuplet $(Q, \Gamma, q_0, \delta_k, F)$ où :

* $Q$ est un ensemble fini d'**état**
* $\Gamma$ est l'**alphabet de travail**. Il contient un symbole spécial $\sharp$, dit **blanc**, avec $\sharp \in \Gamma$
* $q_0 \in Q$ est l'**état initial** de la machine
* $\delta : Q \times \Gamma \rightarrow 2^{Q \times \Gamma \times \\{ \leftarrow, \rightarrow \\}}$ est la **fonction de transition**
* $F \subset Q$ est l'ensemble des **états finaux**.

Cette machine se distingue de la machine de Turing normale parce que la fonction de transition rend un sous ensemble fini de $Q \times \Gamma \times \\{ \leftarrow, \rightarrow \\}$ et non juste un élément de $Q \times \Gamma \times \\{ \leftarrow, \rightarrow \\}$. Cette machine donne un ensemble de transitions possible pour chaque transition.

Ce qui nous intéresse ici ce n'est plus le calcul effectif mais **s'il existe pour une entrée donnée une suite de transitions emmenant à un état final**. C'est à dire qu'il existe une suite de nombres $(t_1, \dots, t_k)$ telle que à chaque instruction $i$  on ait pu choisir le $t_i$ème choix pour que la $k$ instruction mêne à un état final.

En représentant les choix sous la forme d'un arbre, on peut représenter $\delta$ comme ça :

![Turing non déterministe arbre]({{ "/assets/cours/algorithmie/Turing-nd-arbre.png" | relative_url }}){:style="margin: auto;display: block;"}

Une exécution de la machine revient à suivre un chemin dans cet arbre, donc qu'à partir de l'état initial $e$ et du caractère $a$ sous le curseur, on a :

* $(e_{t_1}, a_{t_1}, f_{t_1}) \in \delta(e, a)$
* $(e_{t_1\dots t_i}, a_{t_1\dots t_i}, f_{t_1\dots t_i}) \in \delta(e_{t_1t_2\dots t_{i-1}}, a_{t_1t_2\dots t_1i-1})$

C'est un outil théorique très puissant car il permet de démontrer simplement beaucoup de théorème d'informatique théorique. Cependant, **elle ne permet pas de faire plus de chose qu'une machine normale** :

> Pour toute machine de Turing non déterministe, on peut créer une machine de Turing *normale* qui s'arrêtera sur les même entrées.
{. note}

Juste une idée de la preuve. En utilisant la représentation arborée, en regardant chaque possibilité *couche par couche* (on appelle ça faire un [parcours en largeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur)), on construit une machine de Turing *simple* qui s'arrête bien si et seulement si la machine de Turing non déterministe s'arrête.

#### autres variantes

par exemple des machines utilisant [plusieurs rubans et/ou plusieurs curseurs](https://perso.liris.cnrs.fr/sylvain.brandel/wiki/lib/exe/fetch.php?media=ens:m1if09:m1if09-cm03.pdf). L'intérêt de ces machines est qu'elle sont plus facilement programmables.

### simplification de l'alphabet

Diminuer ou agrandir l'alphabet d'une machine de Turing ne permet pas de calculer plus de choses non plus. On peut se restreindre à un alphabet à 2 lettres :

> On peut simuler toute machine de Turing par une machine de Turing sur un alphabet $\\{\sharp, 1\\}$.
{: .note}

Idée de la preuve. Comme l'alphabet $\Gamma$ d'une machine de Turing est fini, on peut associer à chaque lettre non blanc un numéro allant de $1$ à $\vert \Gamma \vert$, puis coder celui-ci par le mot $\sharp\sharp\sharp \dots \sharp\sharp\sharp 111 \dots 111$ de longueur $\vert \Gamma \vert$ et ayant autant de $1$ que la valeur de son numéro. On termine par coder le caractère blanc par une suite de $\Gamma$ caractères $\sharp$. Une fois cette traduction d'alphabet effectué, on modifie les transitions pour qu'elles se déplacent de $\vert \Gamma \vert$ cases à chaque fois en utilisant des états transitoires (comme dans la partie précédente).

On montre par là que :

> Une machine de Turing calcule un fonction  $f: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}$ (de l'ensemble des mots formées de suite de $0$ et de $1$) dans $\\{0, 1\\}$).
{: .note}

### machine de Turing universelle

Ce qui différentie une machine de Turing d'une autre c'est l'alphabet et la fonction de transition. On a vu qu'on pouvait utiliser un alphabet commun ($\\{ \sharp, 1\\}$), les différences entre machines sont donc uniquement à la fonction de transition.

Un des résultat les plus surprenant de Turing est qu'en fait on ne peut construire qu'**une seule machine** qui simulera toutes les autres. Cette machine est appelée [Machine de Turing universelle](https://fr.wikipedia.org/wiki/Machine_de_Turing_universelle) et possède deux paramètres, le premier, $M$ représentant le programme d'une machine de Turing et le second $E$ une entrée. Le résultat de cette machine est le calcul de la machine $M$ avec l'entrée $E$.

> Il existe une machine de Turing $U$ à 2 rubans sur l'alphabet $\\{ \sharp, 1\\}$ telle que pour une machine de Turing $M$ et une entrée $E$ donnée, $U(M, E)$ calculera ce que calcule $M$ pour l'entée $E$.
{: .note}

Nous ne démontrerons pas ce résultat que l'on doit à Turing lui-même, contentons nous de voir comment on peut encoder une Machine de Turing $M$ sur l'alphabet $\\{ \sharp, 1\\}$ en une chaine de $\sharp$ et de $1$ pour en faire un paramètre d'entrée possible d'une machine de Turing.

Il y a bien des façon de faire. Nous prendrons ici celle utilisée dans la partie 3.3.4 de [ce document](http://pageperso.lif.univ-mrs.fr/~kevin.perrot/documents/2016/calculabilite/Cours_16.pdf). L'idée est de pouvoir :

* encoder chaque transition
* avoir des séparateur nous permettant de délimiter chaque transition les unes des autres

Soit $M$ une machine de Turing à $n$ états ($q_1$ à $q_{n}$ et l'état initial est $q_1$) et $m$ caractères (de $c_1$ à $c_m$) Une transition est alors $\delta(q_i, c_j) = (q_k, c_l, D)$  où $D$ est soit $\leftarrow$ soit $\rightarrow$.

En codant :

* $q_i$ par $i$ $\sharp$,
* $c_j$ par $j$ $\sharp$,
* $\leftarrow$ par $\sharp$,
* $\leftarrow$ par $\sharp\sharp$
* le séparateur par $1$

La transition $\delta(q_i, c_j) = (q_k, c_l, \leftarrow)$ se code alors :

$${
\underbrace{\sharp \cdots \sharp}_{i}{1} \underbrace{\sharp \cdots \sharp}_{j}{1} \underbrace{\sharp \cdots \sharp}_{k}{1} \underbrace{\sharp \cdots \sharp}_{l}{1} \underbrace{\sharp}_{\leftarrow}
}$$

On sépare ensuite toutes les transitions par $11$ :

$
\mbox{transition}_111\cdots11\mbox{transition}_i11\cdots11\mbox{transition}_N
$

Il nous reste à renseigner le nombre d'états et de caractères en début de code et de donner un début et une fin à ce code ($111$) pour finaliser notre encodage $\langle M \rangle$ de la machine de Turing $M$ :

$
\langle M \rangle = 111\underbrace{\sharp \cdots \sharp}_{n}11\underbrace{\sharp \cdots \sharp}_{m}11\mbox{transition}_111\cdots11 \mbox{transition}_i11\cdots11\mbox{transition}_N111
$

> Félicitations, vous venez de créer votre 1er ordinateur ! La machine de Turing universelle permet en effet d'exécuter n'importe quelle machine $M$ : c'est un ordinateur dont le langage machine est l'encodage $\langle M \rangle$.

C'est un résultat extrêmement puissant. On a besoin que d'une machine de Turing pour exécuter toutes les machines de Turing. Attention cependant, On a l'impression qu'on a besoin de rien, que toutes les machines de Turing sont en faite une seule. Ce n'est pas exactement le cas car l'encodage cache la machine. C'est un petit peu comme dans la blague ci-dessous. Un numéro n'est drôle que parce qu'il code une blague !

```text
Une famille qui connaît toutes les blagues de la planète 
les a classées et numérotées. Ainsi, le seul numéro suffit 
à les faire rire.

Lors d' un repas le père s'exclame : "12" !
Tout le monde pouffe de rire.
La mère dit : "32" !
Et ils éclatent de rire.
Le petit sort alors : "104" !
Et personne ne rit.
Son frère lui dit alors : " Tu la racontes mal !"
```

Grâce à la machine de Turing universelle, démontrer qu'un langage est [Turing complet](https://fr.wikipedia.org/wiki/Turing-complet) c'est à dire qu'il permet de calculer tout ce qu'une machine de Turing peut calculer revient à montrer qu'on peut simuler une machine de Turing. C'est comme ça par exemple qu'on a démontrer que la [règle 110](https://en.wikipedia.org/wiki/Rule_110) est un ordinateur.

## conclusion

* une machine de Turing est un outil théorique permettant de calculer exactement ce que peut calculer un ordinateur.
  * toutes les généralisations des machines de Turing ne permettent pas de calculer plus de chose que la machine toute simple.
  * on peut se restreindre à une machine à une entrée sur un alphabet à 2eux lettres sans perte de généralité
* on peut encoder une machine de Turing $M$ sous la forme d'une chaîne de caractère $\langle M \rangle$
* il existe une machine de Turing universelle qui permet de simuler toutes les machine de Turing existentes

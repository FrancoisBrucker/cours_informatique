---
layout: page
title:  "Machine de Turing"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [théorie]({% link cours/theorie-pratiques-algorithmique/theorie/index.md %}) / [machine de Turing]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %})
>
> prérequis :
>
> * [calculabilité]({% link cours/theorie-pratiques-algorithmique/theorie/calculabilite.md %})
> * [algorithmie/pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %})
>
{: .chemin}

La [machine de Turing](https://fr.wikipedia.org/wiki/Machine_de_Turing) est une façon simple d'implémenter les [4 règles générales d'un algorithme]({% link cours/theorie-pratiques-algorithmique/theorie/calcul.md %}#regles-generales). Turing lui-même a montré que :

> La machine de Turing permet exactement de calculer tout ce qu'on peut faire avec un [pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#regles).
{: .note}

De plus, toutes les tentatives de généralisation de son modèle se sont révélés infructueuses : on arrive pas à calculer plus de choses qu'avec la machine de Turing (c'est juste plus simple de le faire).

On peut même montrer qu'une machine de Turing est elle même équivalent à un ordinateur !

La force d'une machine de Turing est qu'il n'y a rien (modèle très simple) et pourtant il y a tout (on peut tout calculer).

> L'article où d'Allan Turing décrit cette machine est [là](https://www.espace-turing.fr/IMG/pdf/turing_paper_1936.pdf)

## définition

Il existe plusieurs définitions équivalentes d'une machine de Turing. Nous allons utiliser une variation de [celle de wikipedia](https://fr.wikipedia.org/wiki/Machine_de_Turing#D%C3%A9finition_formelle), que l'on va pouvoir utiliser tout au long de ce cours :

Une **machine de Turing** est un 6-uplet $(Q, \Gamma, \Sigma, \delta, q_0, q_a)$ où :

* $Q$ est un ensemble fini d'**état**
* $\Gamma$ est un ensemble fini nommé **alphabet de travail**. Il contient un symbole spécial $\sharp$, dit **blanc**.
* $\Sigma$ est un ensemble fini nommé **alphabet d'entré**. C'est un sous ensemble de $\Gamma$ ne contenant pas $\sharp$
* $\delta : Q \times \Gamma \rightarrow Q \times \Gamma \times \\{ \leftarrow, \rightarrow \\}$ est la **fonction de transition**
* $q_0 \in Q$ est l'**état initial** de la machine
* $q_a \in Q$ est l'**état d'acceptation** de la machine

> On appelle cette machine **déterministe** car $\delta$ est une fonction.

Pour fonctionner, la machine nécessite :

* un **ruban** constitué de cases contiguës pouvant chacune contenir un élément de $\Gamma$
* un **curseur** qui est positionné sur une case du ruban

Initialement toutes les cases du ruban contiennent le symbole $\sharp$.

Voici la représentation d'une machine à la fin de la $i$ème instruction. Son état est $q$ et son curseur est positionné sur la case d'indice $j$ :

![machine]({{ "/assets/cours/algorithmie/machine-turing.png" | relative_url }}){:style="margin: auto;display: block;"}

Par convention, on considérera que le ruban initial aura comme numéro d'instruction 0 et que l'indice de la case où est initialement le curseur sera d'indice 0.

> L'**exécution** d'une machine de Turing $(Q, \Gamma, \Sigma, \delta, q_0, q_a)$ se déroule comme suit :
>
> 1. on place la tête de lecture sur une case du ruban
> 2. on initialise si besoin le ruban avec une chaine de caractères (finie) contenant des caractères de $\Sigma$ et on place le curseur sur la première case de la chaine.
> 3. si l'état de la machine est $q_a$ on stoppe le programme.
> 4. on lit le caractère $a$ sous le curseur, l'état $q$ de la machine et on note $\delta(a, q) = (a', q', d)$
> 5. on écrit $a'$ dans la case du ruban pointé par le curseur, on place la machine dans l'état $q'$ et on déplace le curseur vers la gauche si $d$ vaut $\leftarrow$ et vers la droite sinon ($d$ vaut $\rightarrow$)
> 6. retour en 3.
>
{: .note}

> L'exécution d'une machine de Turing, n'est pas forcément finie. Elle ne s'arrête que si elle atteint l'état $q_a$, ce qui peut ne jamais arriver.

Remarquez la minimalité du fonctionnement :

* on ne peut déplacer la tête de lecture que d'une case vers la gauche ou vers la droite (il est impossible d'écrire ou l'on veut dans la mémoire comme on peut le faire avec un ordinateur classique)
* on ne peut écrire qu'une lettre à la fois (pas d'entier, de réel, rien que des lettres)
* pas de variables
* pas de boucle for ni de saut
* un unique test entre un état et une case du tableau
* ...

Et pourtant, elle capte toutes les possibilités d'un algorithme.

Essayez de supprimer une règle et plus rien ne marche et en ajouter ne sert à rien, comme on le verra dans la partie [substantifique moelle](#substantifique-moelle)

## machine de Turing, algorithmes et fonctions

Une machine de Turing peut être vue comme un algorithme dont l'entrée et la sortie sont écrits sur le ruban. Pour préciser cela, il faut commencer par définir clairement entrées et sorties.

> Un **mot** $\omega$ d'un ensemble fini $\Sigma$ est une suite fini d'éléments de $\Sigma$, que l'on note : $\omega = \omega_1 \cdots \omega_n$ . La **longueur** d'un mot est la longueur de la suite (le mot de longueur 0 est la suite vide).
> On appelle alors $\Sigma$ l'**alphabet** et **caractère** un élément de la suite d'un mot.
> On note $\Sigma^\star$ l'ensemble des mots de $\Sigma$ et $\Sigma^+$ l'ensemble des mots non vide (de longueur strictement positive)
{: .note}

A chaque étape de l'exécution du programme d'une machine le ruban contient des caractères de $\Gamma$. On sait de plus que les bords du rubans sont constituées de $\sharp$.

> Une **configuration** d'une machine de Turing $M = (Q, \Gamma, \Sigma, \delta, q_0, q_a)$ est un triplet $(m_1, q, m_2)$ de $\Gamma^\star \times Q \times \Gamma^+$ tel que :
>
> * l'état de la machine soit $q$
> * le mot $m_1$ suivi directement du mot $m_2$ est sur le ruban
> * le curseur est placé sur le premier caractère de $m_2$
>
{: .note}

Par exemple, la figure suivante correspond par exemple aux configurations $(1011, b, 010)$, $(11, b, 0)$ ou encore $(1011, b, 010\sharp\sharp)$ :

![configuration]({{ "/assets/cours/algorithmie/turing-configuration.png" | relative_url }}){:style="margin: auto;display: block;"}

On peut maintenant préciser l'entrée et la sortie (si elle existe) de l'exécution d'une machine de Turing.

> L'**entrée** d'une exécution est un mot $m \in \Sigma^\star$ telle que la **configuration initiale** de l'exécution de la machine (l'étape 2 lors de l'exécution) soit $(\emptyset, q_0, m)$ avec des blancs partout ailleurs sur le ruban.
{: .note}

Si l'exécution d'une machine s'arrête, on peut lire la **sortie** de la machine :

> La **sortie** de l'exécution d'une machine de Turing est la concaténation des mots $m_1$ et $m_2$ où la machine est dans la configuration  $(\sharp m_1, q_a, m_2\sharp)$ avec $m_1, m_2 \in \Sigma^*$.
{: .note}

En reprenant la machine de la figure précédente et un considérant que $b$ est son état d'acceptation. La sortie de la machine serait : $1011010$.

> Notez que la sortie de l'exécution d'une machine de Turing est définie de façon unique (c'est les cases autour du curseur qui contiennent des caractères de l'alphabet d'entrée).

Finissons par quelques définitions qui précisent des différents résultats de l'exécution d'une machine $M = (Q, \Gamma, \Sigma, \delta, q_0, q_a)$.

> Un mot $\mu$ de $\Sigma^\star$ est **accepté** par $M$ si l'exécution de $M$ pour l'entrée $\mu$ se termine sur l'état $q_a$. L'ensemble des mots acceptés par $M$ est le **langage** de $M$ et est noté $\mathcal{L}(M)$.
{: .note}

## exemples de programmes

### répéteur

Le premier exemple donné par Allan Turing est celui-ci :

* $Q = \\{ a, b, c, d \\}$
* $\Gamma = \\{ 0, 1, \sharp \\}$ et $\Sigma = \\{ 0, 1 \\}$
* $q_0 = a$
* on aura pas besoin d'état final
* $\delta(a, \sharp) = (0, b, \rightarrow)$
* $\delta(b, \sharp) = (\sharp, c, \rightarrow)$
* $\delta(c, \sharp) = (1, d, \rightarrow)$
* $\delta(d, \sharp) = (\sharp, a, \rightarrow)$

La fonction $\delta$ est ici partielle, avec la convention que si l'on arrive dans une configuration non décrite, on stoppe la machine (on peut donc étendre $\delta$ à tout $Q \times \Gamma$ si on le voulait).

Allons-y. Essayons ce code. On considère la machine de Turing ci-après, avec l'entrée vide :

![Turing 1]({{ "/assets/cours/algorithmie/turing-1.png" | relative_url }}){:style="margin: auto;display: block;"}

Par convention, on considérera que le ruban initial aura comme numéro d'instruction 0 et que l'indice de la case où est initialement le curseur sera d'indice 0.

On est à l'état $a$ et on lit $\sharp$ dans la machine : la table de transition nous indique qu'il faut :

* écrire $0$
* passer dans l'état $b$
* aller à droite

![Turing 2]({{ "/assets/cours/algorithmie/turing-2.png" | relative_url }}){:style="margin: auto;display: block;"}

On est à l'état $b$ et on lit $\sharp$ dans la machine : la table de transition nous indique qu'il faut :

* écrire $\sharp$
* passer dans l'état $c$
* aller à droite

![Turing 3]({{ "/assets/cours/algorithmie/turing-3.png" | relative_url }}){:style="margin: auto;display: block;"}

On est à l'état $c$ et on lit $\sharp$ dans la machine : la table de transition nous indique qu'il faut :

* écrire $1$
* passer dans l'état $d$
* aller à droite

![Turing 4]({{ "/assets/cours/algorithmie/turing-4.png" | relative_url }}){:style="margin: auto;display: block;"}

On est à l'état $d$ et on lit $\sharp$ dans la machine : la table de transition nous indique qu'il faut :

* écrire $\sharp$
* passer dans l'état $a$
* aller à droite

![Turing 5]({{ "/assets/cours/algorithmie/turing-5.png" | relative_url }}){:style="margin: auto;display: block;"}

Et ainsi de suite. On voit que cette machine ne va jamais s'arrêter et qu'elle écrit continuellement 0 puis 1 sur le ruban. Cette machine n'a pas d'entrée ni de sortie.

Si vous voulez le voir en action, allez sur <https://Turingmachine.io/>. C'est le programme "repeat 0 1".

> Si vous avez trifouillé le code sur <https://Turingmachine.io/> et que vous ne retrouvez pas vos petits, recommencez en ouvrant une nouvelle fenêtre de navigation privée pour supprimer les données conservées.

Le site représente la machine sous la forme de son diagramme de transition. Les nœuds représentent l'état de la machine et sur l'arc est représenté la transition selon selon la lecture sur le ruban.

### doublement des bâtons {#exemple-doublement-batons}

Autre exemple classique des machines de Turing, le doublement des bâtons. Elle s'écrit comme ça :

|      | 1                         | $\sharp$                   |
|------|---------------------------|----------------------------|
|**s** | $(\sharp, l, \leftarrow)$ | $(\sharp, e, \leftarrow)$ |
|l     |                           | $(1, g, \leftarrow)$       |
|g     | $(1, g, \leftarrow)$      | $(1, d, \rightarrow)$      |
|d     | $(1, d, \rightarrow)$     | $(\sharp, s, \rightarrow)$ |

On a représenté la machine sous la forme d'un tableau où les état sont des lignes et chaque colonne est un élément de l'alphabet. L'état initial est la première ligne et l'état final n'a pas de ligne, c'est $e$.

On initialise cette machine avec une chaine de 1 : $\Sigma = \\{ 1 \\}$ (et $\Gamma = \\{ 1, \sharp \\}$).

Suivons l'exécution de cette machine avec l'entrée `11` (la position du curseur est en orange) :

| # instruction| ruban ||||||| état |
| ^^   |-3|-2|-1|0|1|2| ^^|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|----|--|--|--|-|-|-|-|----|
|0   |  #  |  #  |  #  | **1** {: .cls style=";background: orange" }|  1  |  #  | s  |
|1   |  #  |  #  | **#** {: .cls style=";background: orange" }|  #  |  1  |  #  | l  |
|2   |  #  | **#** {: .cls style=";background: orange" }|  1  |  #  |  1  |  #   | g  |
|3   |  #  |  1  | **1** {: .cls style=";background: orange" }|  #  |  1  |  #   | d  |
|4   |  #  |  1  |1| **#** {: .cls style=";background: orange" }|  1  |  #   | d  |
|5   |  #  |  1  |1|#| **1** {: .cls style=";background: orange" }|  #   | s  |
|6   |  #  |  1  |1| **#** {: .cls style=";background: orange" }|#|  #   | l |
|7   |  #  |  1  | **1** {: .cls style=";background: orange" }|1|#|  #    | g |
|8   |  #  | **1** {: .cls style=";background: orange" }|1|1|#|  #   | g |
|9   | **#** {: .cls style=";background: orange" }|1|1|1|#|  #    | g |
|10   |1| **1** {: .cls style=";background: orange" }|1|1|#|  #    | d |
|11   |1|1| **1** {: .cls style=";background: orange" }|1|#|  #    | d |
|12   |1|1|1| **1** {: .cls style=";background: orange" }|#|  #    | d |
|13   |1|1|1|1| **#** {: .cls style=";background: orange" }|  #    | d |
|14   |1|1|1|1|#| **#** {: .cls style=";background: orange" }  | s |
|15   |1|1|1|1|**#** {: .cls style=";background: orange" }| # | e |

La machine s'arrête ! Avant de voir exactement pourquoi cette machine s'arrête, essayer de comprendre son fonctionnement.

> Testez la machine avec <https://Turingmachine.io/> en utilisant le code ci-dessous, traduction de la machine, avec une entrée de `1111` :
{: .a-faire}

```text
input: '1111'
blank: '#'
start state: start
table:
  start:
    1: {write: '#', L: lien}
    '#': {L: done}
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

Son fonctionnement est le suivant :

1. on remarque qu'au départ on est placé sur un `1`
2. de là, on va effectuer deux instructions à la suite (l'état $l$ ne sert qu'à ça) :
   1. on remplace le premier 1 par un $\sharp$ et on se déplace à gauche
   2. on écrit 1, puis on se déplace encore une fois à gauche
3. Une fois là, on se déplace autant de fois que nécessaire sur la gauche jusqu'à arriver sur une case avec $\sharp$ (au début, on a pas besoin de bouger).
4. Arrivé là on écrit 1, puis on se déplace autant de fois que nécessaire sur la droite jusqu'à arriver sur une case $\sharp$.
5. Arrivé là, on se déplace à droite et on replace la machine de Turing à son été initial pour recommencer en 1. si on est placé sur un 1.

A chaque itération, la machine supprime un 1 et en écrit 2 nouveaux : un à droite et un à gauche des nouveaux 1 inscrits. Les étapes de cette itération peut être décrite comme suit :

![Turing 6]({{ "/assets/cours/algorithmie/turing-6.png" | relative_url }}){:style="margin: auto;display: block;"}

On aura toujours une configuration où les nouveaux 1 seront à gauche des anciens 1 (ceux initialement sur le ruban) et séparé par **un unique caractère blanc** :

![doublement de batons]({{ "/assets/cours/algorithmie/turing-7.png" | relative_url }}){:style="margin: auto;display: block;"}

Le programme de la machine de Turing a machine va donc ici s'arrêter puisqu'à un moment tous les anciens $1$ auront-été effacés et on se retrouvera à l'état initial avec le curseur placé sur un $\sharp$ , ce qui enverra vers l'état final.

On remarque que la configuration de sortie est $(1111,e, \emptyset)$. : la sortie de l'exécution de la machine avec en entrée $11$ est $1111$.

**Félicitations** ! Vous venez d'implémenter la fonction $f(n) = 2n$ dans une machine de Turing.

Remarquez que par construction de la machine de Turing, le nombre d'opérations nécessaires pour exécuter le programme correspond aussi au nombre maximum de cases différentes du ruban qui ont put être parcourues :

> Le nombre de cases du ruban parcouru par une machine de Turing est plus petit ou égal aux nombres d'instructions effectuées.
{: .note}

### autres programmes

Le site <https://Turingmachine.io/> contient bien d'autres programmes à essayer. Vous pouvez aussi aller du côté de <https://machinedeTuring.com/> pour aller voir le programme donné par Turing pour [générer tous les entiers](https://machinedeTuring.com/exemple.php?page=9).

Notez qu'il est facile de composer des machines de Turing ensemble en *concaténant* les paramètres (alphabets, fonction de compositions, états). On peut ainsi créer des gros programmes en assemblant des machines de Turing toutes simples. On peut ainsi plus ou moins facilement créer des machines de Turing qui :

* déplacent un caractère sur le ruban vers la gauche ou la droite
* mettent des bornes à gauche et à droite du rubans pour délimiter l'intervalle des cases modifiées par le programme à tout moment de son exécution
* cherchent une case contenant un caractère en particulier
* ...

## substantifique moelle de la machine de Turing {#substantifique-moelle}

Le modèle de la machine de Turing admet quatre paramètres :

* un ruban
* un curseur
* l'alphabet
* une fonction de transitions

On peut se demander ce qui est vraiment utile là-dedans (peut-on simplifier le modèle sans perdre en expressivité ?) ou au contraire si complexifier le modèle permet de calculer plus de chose.

### généralisation du modèle : inutile

Commençons par répondre à la seconde question : *est-ce que complexifier le modèle permet de calculer plus de chose ?* La réponse est **non**.

Il existent de nombreuses généralisations des machines de Turing, elles ne permettent pas de calculer plus de choses, mais sont utiles car elle permettent de calculer plus facilement/rapidement. Ces généralisations nous permettent d'écrire rapidement des programmes en sachant qu'on pourrait (si on en avait très envie) les écrire avec une machine de Turing normale.

#### machines à plusieurs rubans

Une machine de Turing à $k$ rubans peut être définie comme suit.

Une **machine de Turing à $k$ rubans** est un 6-uplet $(Q, \Gamma, \Sigma, \delta_k, q_0, q_a)$ où :

* tout est identique à la machine de Turing classique à part $\delta_k$
* $\delta_k : Q \times \Gamma^k \rightarrow Q \times \Gamma^k \times \\{ \leftarrow, \rightarrow \\}^k$ est la **fonction de transition**

Pour fonctionner, la machine nécessite :

* $k$ **rubans** constitués de cases contiguës pouvant chacune contenir un élément de $\Gamma$
* $k$ **curseurs**, un pour chaque ruban

Tout se passe comme pour la machine de Turing mais on lit la valeur des $k$ rubans, puis la fonction de transition écrit une valeur sur chaque ruban et déplace les curseurs de chaque ruban.

> On peut toujours transformer une machine à plusieurs rubans en une machine de Turing normale équivalente.
{: .note}

Nous n'allons pas donner la preuve complète de ceci, mais juste une idée de la preuve de comment simuler une machine à 2 rubans avec une machine avec un seul ruban.

Lorsque l'on a une machine à 2 rubans, on a un curseur pour chaque ruban. A chaque instruction on lit le contenu de chaque ruban sous le curseur et selon l'état de la machine on écrit sur les 2 rubans puis on déplace chaque curseur vers la gauche ou la droite. On peut alors simuler les 2 rubans en un seul ruban en ajoutant une lettre $\bigtriangledown$ à l'alphabet et en découpant le ruban en paquets de 4 cases :

* la première case valant soit $\bigtriangledown$ si le curseur du premier ruban est sur cette case, soit $\sharp$ sinon,
* la deuxième case valant le caractère de la case sur le premier ruban
* la troisième case valant soit $\bigtriangledown$ si le curseur du second ruban est sur cette case, soit $\sharp$ sinon,
* la deuxième case valant le caractère de la case sur le second ruban

Enfin, on peut toujours s'arranger pour qu'au départ, le curseur du premier ruban et du second ruban soient sur le même paquet de 4 cases.

De là, à chaque itération de la machine à 1 seul ruban, on commence par chercher les paquets de 4 cases contenant les curseurs de chaque ruban et on lit leurs valeurs (on peut faire ça en parcourant le ruban jusqu'à trouver $\bigtriangledown$ en premier ou en troisième position d'un paquet à 4 cases) puis on effectue la fonction de transition de la machine à 2 rubans et on écrit les nouvelles valeurs en recherchant les positions respectives des curseurs dans les paquets à 4 cases.

#### machines à plusieurs curseurs

Plutôt que de multiplier les rubans, on peut aussi multiplier les curseurs :

Une **machine de Turing à $k$ curseurs** est un 6-uplet $(Q, \Gamma, \Sigma, \delta_k, q_0, q_a)$ où :

* tout est identique à la machine de Turing classique à part $\delta_k$
* $\delta_k : Q \times \Gamma^k \rightarrow Q \times \Gamma^k \times \\{ \leftarrow, \rightarrow \\}^k$ est la **fonction de transition**

Pour fonctionner, la machine nécessite :

* un **ruban** constitués de cases contiguës pouvant chacune contenir un élément de $\Gamma$
* $k$ **curseurs**, sur le ruban

Elle fonctionne de la même manière que la machine à $k$ rubans sauf qu'on lit les valeurs sur le même ruban.

> On peut toujours transformer une machine à plusieurs curseurs en une machine de Turing normale équivalente.
{: .note}

La preuve est identique à celle pour simuler une machine à $k$ rubans sur une machine à 1 ruban.

#### machines à plusieurs curseurs et rubans

On peut bien sur combiner les deux approches et construire une machine de Turing à $k$ rubans et $k'$ curseurs répartis sur les rubans. Mais, comme vous devez vous en douter :

> On peut toujours transformer une machine à plusieurs rubans et plusieurs curseurs en une machine de Turing normale équivalente.
{: .note}

#### machines de Turing non déterministe

Il existe aussi, [la machine de Turing non déterministe](https://fr.wikipedia.org/wiki/Machine_de_Turing_non_d%C3%A9terministe), qui se définit comme suit :

Une **machine de Turing non déterministe** est un 6-uplet $(Q, \Gamma, \Sigma, \delta, q_0, q_a)$ où :

* tout est identique à la machine de Turing classique à part $\delta$
* $\delta : Q \times \Gamma \rightarrow 2^{Q \times \Gamma \times \\{ \leftarrow, \rightarrow \\}}$ est la **fonction de transition**

Cette machine se distingue de la machine de Turing normale parce que la fonction de transition rend un sous ensemble fini de $Q \times \Gamma \times \\{ \leftarrow, \rightarrow \\}$ et non juste un élément de $Q \times \Gamma \times \\{ \leftarrow, \rightarrow \\}$. Cette machine donne un ensemble de transitions possible pour chaque transition.

Ce qui nous intéresse ici ce n'est plus le calcul effectif mais **s'il existe pour une entrée donnée, une suite de transitions emmenant à l'état final**. C'est à dire qu'il existe une suite de nombres $(t_1, \dots, t_k)$ telle que à chaque instruction $i$  on ait pu choisir le $t_i$ème choix pour que la $k$ instruction mêne à un état final.

En représentant les choix sous la forme d'un arbre, on peut représenter $\delta$ comme ça :

![Turing non déterministe arbre]({{ "/assets/cours/algorithmie/Turing-nd-arbre.png" | relative_url }}){:style="margin: auto;display: block;"}

Une exécution de la machine revient à suivre un chemin dans cet arbre, donc qu'à partir de l'état initial $e$ et du caractère $a$ sous le curseur, on a :

* $(e_{t_1}, a_{t_1}, f_{t_1}) \in \delta(e, a)$
* $(e_{t_1\dots t_i}, a_{t_1\dots t_i}, f_{t_1\dots t_i}) \in \delta(e_{t_1t_2\dots t_{i-1}}, a_{t_1t_2\dots t_1i-1})$

C'est un outil théorique très puissant car il permet de démontrer simplement beaucoup de théorèmes d'informatique théorique. Cependant, **elle ne permet pas de faire plus de chose qu'une machine normale** :

> Pour toute machine de Turing non déterministe, on peut créer une machine de Turing *normale* qui s'arrêtera sur les même entrées.
{: .note}

Idée de la preuve. En utilisant la représentation arborée, en regardant chaque possibilité *couche par couche* (on appelle ça faire un [parcours en largeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur)), on construit une machine de Turing *simple* qui s'arrête bien si et seulement si la machine de Turing non déterministe s'arrête.

#### autres variantes

par exemple des machines utilisant [plusieurs rubans et/ou plusieurs curseurs](https://perso.liris.cnrs.fr/sylvain.brandel/wiki/lib/exe/fetch.php?media=ens:m1if09:m1if09-cm03.pdf). L'intérêt de ces machines est qu'elle sont plus facilement programmables.

### simplification de l'alphabet {#alphabet-01}

Diminuer ou agrandir l'alphabet d'une machine de Turing ne permet pas de calculer plus de choses non plus. On peut se restreindre à un alphabet à 2 lettres :

> On peut simuler toute machine de Turing par une machine de Turing sur un alphabet $\\{\sharp, 0, 1\\}$, avec $\\{0, 1\\}$ comme alphabet d'entrée.
{: .note}

Idée de la preuve. Comme l'alphabet $\Gamma$ d'une machine de Turing est fini, on peut associer à chaque lettre non blanc un numéro allant de $1$ à $\vert \Gamma \vert$, puis coder celui-ci par le mot $0 \cdots 0 1 \cdots 1$ de longueur $\vert \Gamma \vert$ et ayant autant de $1$ que la valeur de son numéro.

On termine par coder le caractère blanc par une suite de $\Gamma$ caractères $\sharp$. Une fois cette traduction d'alphabet effectué, on modifie les transitions pour qu'elles se déplacent de $\vert \Gamma \vert$ cases à chaque fois en utilisant des états transitoires (comme l'état $l$ dans l'exemple du [doublement des bâtons](#exemple-doublement-batons)).

On montre par là que :

> Une machine de Turing $M$ calcule un fonction  $f: \mathcal{L}(M) \rightarrow \\{0, 1\\}^\star$ où $f(\mu)$ est la sortie de $M$ pour l'entrée $\mu$.
{: .note}

Si l'on considère des machines de Turing sans alphabet d'entrée (c'est à dire que l'alphabet de travail est aussi l'alphabet d'entrée, on peut simuler toute machine de Turing sur uniquement $\\{\sharp, 1\\}$ (on remplace les $0$ par des $\sharp$ dans l'encodage).

## machine de Turing universelle {#mtu}

Ce qui différentie une machine de Turing d'une autre c'est l'alphabet et la fonction de transition. On a vu qu'on pouvait utiliser un alphabet commun ($\\{ \sharp, 0, 1\\}$), les différences entre machines sont donc uniquement dues à la fonction de transition.

Un des résultat les plus surprenant de Turing est qu'en fait on ne peut construire qu'**une seule machine** qui simulera toutes les autres. Cette machine est appelée [Machine de Turing universelle](https://fr.wikipedia.org/wiki/Machine_de_Turing_universelle) et possède deux paramètres, le premier, $M$ représentant le programme d'une machine de Turing et le second $E$ une entrée.

> Il existe une machine de Turing $U$ à 2 rubans sur l'alphabet d'entrée $\\{ 0, 1\\}$ (et $\\{\sharp, 0, 1\\}$ comme alphabet de traval) telle que pour une machine de Turing $M$ et une entrée $\mu$ donnée, $U(M, \mu)$ calculera ce que calcule $M$ pour l'entrée $\mu$ :
>
> * elle accepte $\mu$ si $M$ l'accepte et sa sortie est celle de $M$ pour l'entrée $\mu$.
> * elle ne s'arrête pas si l'exécution de $M$ avec $\mu$ comme entrée ne s'arrête pas,
>
{: .note}

Nous ne démontrerons pas ce résultat que l'on doit à Turing lui-même, contentons nous de voir comment on peut encoder une Machine de Turing $M$ sur l'alphabet $\\{ 0, 1\\}$ pour en faire un paramètre d'entrée possible d'une machine de Turing.

Il y a bien des façons de faire. Nous prendrons ici celle utilisée dans la partie 3.3.4 de [ce document](http://pageperso.lif.univ-mrs.fr/~kevin.perrot/documents/2016/calculabilite/Cours_16.pdf). L'idée est de pouvoir :

* encoder chaque transition
* avoir des séparateurs nous permettant de délimiter chaque transition

Soit $M$ une machine de Turing à $n$ états (de $q_0$ à $q_{n-1}$) et $m$ caractères (de $c_1$ à $c_m$). Une transition est alors $\delta(q_i, c_j) = (q_k, c_l, D)$  où $D$ est soit $\leftarrow$ soit $\rightarrow$.

On code :

* $q_i$ par $\underbrace{0 \cdots 0}_{i}{}$
* $c_j$ par $\underbrace{0 \cdots 0}_{j}{}$,
* $\leftarrow$ par $0$,
* $\leftarrow$ par $00$
* le séparateur par $1$

La transition $\delta(q_i, c_j) = (q_k, c_l, \leftarrow)$ est alors :
$${
\underbrace{0 \cdots 0}_{i}{1} \underbrace{0 \cdots 0}_{j}{1} \underbrace{0 \cdots 0}_{k}{1} \underbrace{0 \cdots 0}_{l}{1} \underbrace{0}_{\leftarrow}
}$$

On sépare ensuite toutes les transitions par $11$ :
$$
cdots11\mbox{transition}11\cdots
$$

Il nous reste à renseigner le nombre d'états et de caractères en début de code et de donner un début et une fin à ce code ($111$) pour finaliser notre encodage $\langle M \rangle$ de la machine de Turing $M$ :

$$
\langle M \rangle = 111\underbrace{0 \cdots 0}_{n}11\underbrace{0 \cdots 0}_{m}11\mbox{transition}_111\cdots11 \mbox{transition}_i11\cdots11\mbox{transition}_N111
$$

**Félicitations !** : vous venez de créer votre 1er ordinateur !

> La machine de Turing universelle $U$ permet d'exécuter n'importe quelle machine $M$ : c'est un ordinateur dont le langage machine est l'encodage $\langle M \rangle$.
{: .note}

C'est un résultat extrêmement puissant. On a besoin que d'une machine de Turing pour exécuter toutes les machines de Turing.

Attention cependant, On a l'impression qu'on a besoin de rien, que toutes les machines de Turing sont en faite une seule. Ce n'est pas exactement le cas car l'encodage cache la machine. C'est un petit peu comme dans la blague ci-dessous. Un numéro n'est drôle que parce qu'il code une blague !

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

> Grâce à la machine de Turing universelle, démontrer qu'un langage est [Turing complet](https://fr.wikipedia.org/wiki/Turing-complet) c'est à dire qu'il permet de calculer tout ce qu'une machine de Turing peut calculer revient à montrer qu'on peut simuler une machine de Turing. C'est comme ça par exemple qu'on a démontrer que la [règle 110](https://en.wikipedia.org/wiki/Rule_110) est un ordinateur.

## conclusion

* une machine de Turing est un outil théorique permettant de calculer exactement ce que peut calculer un ordinateur (ce n'est ni moins ni plus puissant).
  * toutes les généralisations des machines de Turing ne permettent pas de calculer plus de chose que la machine toute simple.
  * on peut se restreindre à une machine à une entrée sur un alphabet à 2 lettres sans perte de généralité
* on peut encoder une machine de Turing $M$ sous la forme d'un mot de $\\{0, 1 \\}$ noté $\langle M \rangle$
* il existe une machine de Turing universelle $U$ qui permet de simuler toutes les machine de Turing existantes : $U(M, \mu)$ sera égal à $M(\mu)$

Enfin :

> la simplicité de son fonctionnement et la puissance de ce qu'elle calcule convainc (les informaticiens de tous les pays) que tout ce qu'un humain, une machine, ou encore un système physique peut calculer (c'est à dire en suivant des opérations que l'on peut décrire en un nombre fini d'opérations) est exactement égal à ce qu'une machine de Turing peut calculer. C'est ce qu'on appelle [la thèse de Church-Turing](https://plato.stanford.edu/entries/church-Turing/#ReasForAcceThes).
{: .note}

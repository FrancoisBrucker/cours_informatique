---
layout: page
title:  "Décidabilité et calculabilité"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [théorie]({% link cours/theorie-pratiques-algorithmique/theorie/index.md %}) / [décidabilité et calculabilité]({% link cours/theorie-pratiques-algorithmique/theorie/decidabilite_calculabilite.md %})
>
> prérequis :
>
> * [machine de Turing]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %})
{: .chemin}

> voir si on peut supprimer la machine de turing du cours
> dire qu'on utilisera des machines que si on en a besoin et que sinon on décrira tout sous la forme d'un pseudo-code (qui est de toute façon équivalent)
{: .tbd}

La machine de Turing est un modèle permettant de rendre compte d'un algorithme. Tout ce qu'on peut écrire avec un pseudo-code Soit $M$ une machine de Turing et considérons son exécution pour l'entrée $\mu$. La machine va alors soit :

* ne pas s'arrêter (elle n'arrivera jamais à l'état final)
* s'arrêter et sortir un résultat.

Connaitre l'algorithme de la machine correspond ainsi à **deux** problèmes :

1. connaitre les mots d'entrée qui vont faire stopper la machine : c'est la *décidabilité*
2. connaitre la sortie de la machine pour un mot d'entrée qui la fait s'arrêter : c'est la *calculabilité*

Aucun de ces deux problèmes n'est simple.

> Dans la suite, une machine de Turing sera **toujours** une machine sur un alphabet $\\{\sharp, 0, 1\\}$, avec $\\{0, 1\\}$ comme alphabet d'entrée.
> Ceci, [On l'a vu]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %}#alphabet-01), se fait sans perte de généralité et va grandement nous simplifier les notations.
{: .attention}

Comme l'utilisation d'un machine de Turing est équivalente à l'utilisation d'un [pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}) nous décrirons nos machines en python on en pseudo-code, pour plus d'accessibilité. Enfin, nous ne nous contenterons pas de machines à 1 seule entrée, nous prendrons autant de paramètres que nécessaire pour rendre l'algorithme facile à comprendre. Ceci se fait bien sur [sans perte de généralité]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %}#plusieurs-rubans).

Ce qui faut retenir de cette partie :

* un décideur est un algorithme spécifique à un problème de décision donné. Il répond oui si l'entrée admet une réponse au problème et non sinon
* savoir si un algorithme va s'arrêter est un problème indécidable
* il existe des fonctions ou des nombres qu'on ne peut pas calculer avec un algorithme (même beaucoup) mais ceux qu'on utilise couramment le sont

## décidabilité

Commençons par définir un *décideur* :

> Un **décideur** est une machine de Turing qui accepte tous les mots et dont la sortie est soit $1$ (on dit alors que la sortie est *Vraie*) soit $0$ (la sortie est *fausse*).
{: .note}

On associe un décideur à un *problème de décision*, c'est à dire un problème qui correspond à une question qui ne peut avoir que deux réponses *vrai* ou *faux* selon l'entrée donnée. Par exemple le problème suivant :

* nom : premier
* entrée : un nombre $n$
* question : $n$ est-il un nombre premier ?

Le problème de décision *premier* admet un décideur (il suffit de tester tous les entier plus petit que $n$ pour voir si le reste de la division entière vaut 0), mais ce n'est pas de tous les les problèmes. Par exemple le problème suivant n'admet pas de décideur (on va le démontrer), ce problème est indécidable :

* nom : arrêt
* entrées : une machine de Turing M, et une entrée $E$
* question : La machine de Turing $M$ accepte-t-elle $E$ ?

La décidabilité est donc le fait de savoir si on peut résoudre un problème de décision par un algorithme. Dans le cadre des machines de Turing cela se traduit par savoir si, pour un ensemble de mots $L$, il existe une machine de Turing $M$ telle que $\mathcal{L}(M) = L$ (la machine s'arrête exactement sur les mots de $L$)

On finira cette partie en montrant deux problèmes de décision d'interêts le premier historique et le second théorique.

### langage reconnaissables et décidable

Pour un problème de décision donné, soit $L$ l'ensemble des mots en entrée pour lesquels il va répondre *vrai*. S'il existe un pseudo-code pour le résoudre, c'est que $L$ doit être le langage d'une machine de Turing.

Cela se formalise ainsi :

> Un ensemble de mots $L$ est **reconnaissable** s'il existe une machine de Turing $M$ d'alphabet d'entrée $\Sigma$ tel que $L = \mathcal{L}(M)$
{: .note}

{% details  Par exemple, le problème de décision de savoir si un mot donné est un palindrome est un problème reconnaissable. %}

Soit $L$ l'ensemble des palindromes. On utilise le fait qu'on mot $m$ est un palindrome si :

* le mot vide est un palindrome
* le mot d'un caractère est un palindrome
* le premier et le dernier caractère doivent être identique
* le mot privé de son premier et dernier caractères doit être un palindrome

On ne décrit pas précisément les différents états, mais on va décrire sont fonctionnement assez précisément pour que ce soit faisable :

1. lit le 1er caractère :
   * si c'est $0$ on place la machine dans l'état $a$
   * si c'est $1$ on place la machine dans l'état $b$
   * si c'est $\sharp$ : on écrit $\sharp 1 \sharp$ sur le ruban, on place le curseur sur le $1$ et l'état de la machine sur l'état d'acceptation : **on a un palindrome** (c'est le mot vide)
2. on remplace le caractère par $\sharp$ on se déplace à droite jusqu'à arriver sur un $\sharp$, on déplace d'un cran à gauche et on lit le caractère :
   * s'il est vide : on écrit $\sharp 1 \sharp$ sur le ruban, on place le curseur sur le $1$ et l'état de la machine sur l'état d'acceptation : **on a un palindrome** (c'est le mot d'un caractère)
   * si c'est $0$ et qu'on est dans l'état $b$ : on écrit $\sharp 0 \sharp$ sur le ruban, on place le curseur sur le $0$ et l'état de la machine sur l'état d'acceptation : **on a pas un palindrome** (le mot ne commence et ne fini pas avec la même lettre)
   * si c'est $1$ et qu'on est dans l'état $a$ : on écrit $\sharp 0 \sharp$ sur le ruban, on place le curseur sur le $0$ et l'état de la machine sur l'état d'acceptation : **on a pas un palindrome** (le mot ne commence et ne fini pas avec la même lettre)
3. on remplace le caractère par $\sharp$ on se déplace à gauche jusqu'à arriver sur un $\sharp$, on déplace d'un cran à droite et on se place dans l'état initial : **on revient à l'étape 1 en ayant supprimer le premier et dernier caractère de l'entrée**

{% enddetails %}

La machine précédente (dans la partie initialement cachée) qui prouve que l'ensemble des palindromes est reconnaissable fait même plus, si le mot n'est pas un palindrome elle rend faux : cette machine est un décideur pour l'ensemble des palindromes. Le problème de décision de savoir si un mot donné est un palindrome est ainsi *décidable*

> Un ensemble de mots $L$ est **décidable** s'il existe un décideur qui rend $1$ si l'entrée est dans $L$ et $0$ sinon.
{: .note}

Pour le problème de décision *premier*, le langage $L$ serait l'ensemble des entiers premiers.

Notez que *décidable* est bien plus fort que *reconnaissable*. En effet, si un langage est juste reconnaissable on ne saura pas si l'exécution de la machine avec une entrée donnée met juste longtemps à répondre oui ou si le mot n'est pas accepté et donc que la machine boucle indéfiniment.

Plus généralement, on a  :

> Savoir s'il existe un algorithme permettant de répondre *Vrai* si un élément $A$ à la propriété $P$ et *faux* sinon, est équivalent à savoir si l'ensemble des éléments $A$ ayant la propriété $P$ est décidable.
{: .note}

### exemple des polynômes à coefficients dans $\mathbb{Z}$

Soit le problème de décision suivant : Soit $P(X)$ un [polynôme](https://fr.wikipedia.org/wiki/Polyn%C3%B4me) à coefficients dans $\mathbb{Z}$. Possède-t-il une [racine](https://fr.wikipedia.org/wiki/Racine_d%27un_polyn%C3%B4me) dans $\mathbb{N}$ (un entier $a$ tel que $P(a) = 0$) ?

{% details ce problème est reconnaissable %}

On peut facilement créer un algorithme qui, à partir d'un polynôme $P(x)$ à coefficients dans $\mathbb{Z}$ et d'un entier $a$ calcule $P(a)$ (on peut donc aussi fabriquer une machine de Turing qui le fait).

Il suffit ensuite d'essayer tous les entiers un à un. Si le polynôme en entrée admet une racine entière, on va bien tomber dessus à un moment donné.

{% enddetails %}

{% details il est même décidable %}

On peut borner les racines d'un polynôme. Voir par exemple [le corollaire de ce lien](https://fr.wikipedia.org/wiki/Racine_d%27un_polyn%C3%B4me_r%C3%A9el_ou_complexe#Une_premi%C3%A8re_estimation). On aura donc pour chaque polynôme qu'un nombre fini de possibilités à examiner avant de donner la réponse.

{% enddetails %}

Il existe bien sûr des langages qui sont reconnaissables et non décidables, par exemple une généralisation du problème précédent :

> Savoir si un [polynôme à plusieurs variables](https://fr.wikipedia.org/wiki/Polyn%C3%B4me_en_plusieurs_ind%C3%A9termin%C3%A9es) à coefficients dans $\mathbb{Z}$ admet une racine dans $\mathbb{N}$ est un problème indécidable.
{: .note}

**Félicitations !** Vous venez de rencontrer votre premier problème que ne pourra pas résoudre un ordinateur.

> Ce cas est historiquement important car il correspond au [dixième problème de Hilbert](https://fr.wikipedia.org/wiki/Dixi%C3%A8me_probl%C3%A8me_de_Hilbert). Il a été prouvé indécidable par Matiiassevitch en 1970 en montrant qu'on ne pouvait pas borner les racine d'un polynôme à plusieurs variables.

### arrêt d'un algorithme {#arret}

Savoir si un algorithme (ou une machine de Turing puisque c'est équivalent) va s'arrêter, ou pas, sur une entrée est un problème compliqué. Prenez par exemple l'[algorithme suivant](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) :

```python

def syracuse(n):
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

```

L'algorithme est très simple : à partir d'un entier $n$, il le divise par 2 s'il est pair ou le multiplie par 3 et ajoute 1 s'il est impair et recommence tant que ce nombre est strictement plus grand que 1.

> Testez chez vous pour plusieurs nombres, c'est assez bluffant.
>
> Affichez également la suite de nombre ou la représenter graphiquement pour voir l'évolution de votre nombre d'entrée jusqu'à 1.
{: .a-faire}

Personne ne sait (à l'heure où je tape ces caractères) si cet algorithme s'arrête pour tout $n$.

De façon plus générale :

> [Le problème](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt) de décision de savoir si une machine de Turing $M$ va s'arrêter sur l'entrée $E$ est indécidable.
{: .note}
{% details preuve %}

On doit la preuve à Turing lui-même.

Commençons par remarquer que comme une machine de Turing peut s'[encoder sous la forme d'une suite de 0 et de 1]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %}#mtu), on peut bien encoder la paire consituée de la machine de Turing et d'un mot (l'entrée) sous la forme d'un unique mot qui sera l'entrée du décideur s'il existe.

On va maintenant supposer qu'un tel décideur existe et notons le `halt(<M>, E)` avec `<M>` le mot encodant la machine `M`. Cet encodeur rend `1` si l'exécution de `M` avec `E` va s'arrêter et `0` sinon.

On peut alors créer une autre machine dont le pseudo-code est :

```text
def diag(x):
    if halt(x, x) == 1:
        boucle infinie
    else:
        return 1
```

Tout comme [la preuve du théorème de Cantor]({% link cours/theorie-pratiques-algorithmique/theorie/calcul.md %}#nombre-fonction) cette nouvelle machine va tout casser :

1. `diag(x)` ne va s'arrêter que si `halt(x, x)` est faux
2. `halt(<diag>, x)` va répondre 1 que si `diag(x)` s'arrête
3. `halt(<diag>, <diag>)` va répondre 1 si `diag(<diag>)` s'arrête or `diag(<diag>)` ne peut s'arrêter que si `halt(<diag>, <diag>)` ne s'arrête pas
4. contradiction

{% enddetails %}

>faire pareil pour l'entrée vide. il existe les machine M(E) = M'()
{: .tbd}

Il faut bien comprendre l'énoncé ci-dessus. Il n'existe pas de décideur qui prend comme entrée **et** une machine de Turing **et** un mot et qui rend *Vrai* si la machine va s'arrêter : la machine et le mot d'entrée sont les paramètres du décideur.

Cela ne contredit pas le fait qu'on puisse créer un décideur spécifique à une machine qui réponde *vrai* ou *faux* selon le paramètre d'entrée de celle-ci. C'est l'algorithme général, indépendant de la machine, qui n'existe pas.

> lorsque l'on parle de décidabilité ou de problème il faut toujours bien faire attention à ce qui est un paramètre d'entrée et ce qui est donné.

Le théorème d'indécidabilité de l'arrêt de machine de Turing est fondamental théoriquement. Il est à la base de nombreux contre-exemples et :

* il exhibe le fait qu'il existe des choses que l'on ne peut pas calculer avec un ordinateur
* en creux, il montre qu'on peut tout de même faire beaucoup de choses avec des algorithmes puisqu'il faut chercher des exemples bien tordus pour que ça ne marche pas

## calculabilité

La décidabilité cherche à reconnaitre des solutions d'un problème avec un algorithme. La calculabilité utilise la sortie d'une machine pour calculer des valeurs.

[On l'a vu]({% link cours/theorie-pratiques-algorithmique/theorie/calcul.md %}#nombre-fonction), il existe bien plus de fonctions que d'algorithmes. On peut maintenant essayer d'y voir un peu plus clair.

### fonctions calculables

> Un fonction de $f: \mathcal{F} \rightarrow \\{0, 1\\}^\star$, avec $\mathcal{F} \in \\{0, 1\\}^\star$ ($f$ prend en entrée un mot d'un sous-ensemble de $\\{0, 1\\}^\star$ et redonne un mot en sortie) est **calculable** s'il existe une machine de Turing $M$ telle que :
>
> * $M(\mu) = f(\mu)$ si $\mu \in \mathcal{F}$
> * $\mathcal{L}(M) = \mathcal{F}$
>
{: .note}

[Par exemple](https://en.wikipedia.org/wiki/Computable_function#Examples) :

* les fonctions constantes sont calculables
* si $f$ et $g$ sont deux fonctions calculables, alors $f+g$, $f \cdot g$ et $f \circ g$ sont calculables
* les fonctions dont le domaine de définition est fini, sont calculables
* ...

Beaucoup, beaucoup, beaucoup de fonctions sont calculables, il suffit d'exhiber un algorithme pour le prouver. De façon plus bizarre, il existe aussi des fonctions, que l'on sait calculable, mais dont on ne connait pas l'algorithme pour le calculer :

```text
def f(n):
    si il existe n "5" consécutifs dans les décimals de π:
        rend 1
    sinon:
        rend 0
```

La fonction ci-dessus est :

* soit constante et $f(n) = 1$ pour tout $n$ (ce qui est calculable)
* soit il existe $n_0$ tel que pour tout $n \geq n_0$ ont ait $f(n) = 0$ et avant $f(n) = 1$ ($f$ revient à faire un test sur $n$, ce qui est aussi calculable).

Elle est donc calculable, mais on ne sait pas quel algorithme c'est (cas on ne sais pas si π est [un nombre univers](https://fr.wikipedia.org/wiki/Nombre_univers)).

Enfin, finissons cette partie en remarquant que décidabilité et calculabilité sont les deux faces d'une même pièce en remarquant que :

> Si une fonction $f: \mathcal{F} \rightarrow \\{0, 1\\}^\star$ est **calculable** alors $\\{ (a, f(a) \mid a \in \mathcal{F}\\}$ est **reconnaissable**.
{: .note}
{% details preuve %}

Si $f: \mathcal{F} \rightarrow \\{0, 1\\}^\star$ est calculable, la machine de Turing $M$ prenant en entrée deux mots $a$ et $b$ et qui rend 1 si $f(a) = b$ et ne s'arrête pas sinon  est bien telle que $\mathcal{L}(M) = \\{ (a, f(a) \mid a \in \mathcal{F}\\}$.

{% enddetails %}

Et si $f$ est défini sur tout mot (ce qui est très souvent le cas) on a même :

> Une fonction $f: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^\star$ est **calculable** si et seulement si $\\{ (a, f(a) \mid a \in \\{0, 1\\}^\star\\}$ est **décidable**.
{: .note}
{% details preuve %}

Si $f: \mathcal{F} \rightarrow \\{0, 1\\}^\star$ est calculable, la machine de Turing $M$ prenant en entrée deux mots $a$ et $b$ et qui rend 1 si $f(a) = b$ et 0 sinon est bien un décideur sur $\\{ (a, f(a) \mid a \in \\{0, 1\\}^\star\\}$

Réciproquement, soit $M$ un décideur sur $\\{ (a, f(a) \mid a \in \\{0, 1\\}^\star\\}$, la machine $M'$ qui prend itérativement tous les mots $b$ et qui rend $b$ lorsque $M(a, b)$ rend $1$ est bien fini pour tout $a$ et calcule bien $f(a)$.

{% enddetails %}

### fonctions non calculables

Comme il suffit d'exhiber un algorithme pour montrer qu'une fonction est calculable, presque toutes les fonctions auxquelles on peut penser le sont. Pour trouver des fonctions non calculables, il faut chercher des exemples tordus, le plus plus souvent en lien avec le problème de l'arrêt de la machine.

Nous en donnons une ici, la plus célèbre : [les castors affairés](https://fr.wikipedia.org/wiki/Castor_affair%C3%A9) (*busy beavers* dans la verion originale):

> On définit le **score** $\rho(M)$ d'une machine de Turing $M$ acceptant le mot vide comme étant le nombre de $1$ de $M()$.
>
> La fonction du **castor affairé** $\Sigma : \mathbb{N} \rightarrow \mathbb{N}$ est définie telle que $\beta(n)$ vaut le score maximal pour toutes les machine de Turing à $n$ états acceptant le mot vide.
>
{: .note}

La fonction est bien définie pour tout $n>0$ puisqu'il n'y a qu'un nombre fini de machine de Turing à $n$ états : la valeur $\beta(n)$ est un maximum d'un ensemble fini, ce nombre existe.

> $\beta(n) \geq n - 1$ pour tout $n >0$
{: .note}
{% details  preuve %}

Considérons la machine $M_n$ à $n$ états $(q_0, \dots, q_{n-1}) telle que :

* $q_0$ est l'état initial
* $q_{n-1}$ l'état d'acceptation
* la fonction de transition $\delta$ telle que $\delta(q_i, \sharp) = (q_{i+1}, 1, \rightarrow)$

On a $M_n() = \underbrace{1\cdots 1}_{n-1}{}$.
{% enddetails %}

> $\beta(n)$ est strictement croissante
{: .note}
{% details  preuve %}
Soit $B_n$ une machine à $n$ états telle que $\rho(B_n) = \beta(n)$. La machine obtenue en enchaînant $B_n$ et $M_1$ (voir preuve précédente) en associant l'état final de $B_n$ à l'état initial de $M_1$ a $n+1$ états (les état de B_n$ plus l'état d'acceptation de $M_1$) et sa sorite produit un 1 de plus que $\beta_n$ : $\beta(n+1) \geq \beta(n) + 1$.

{% enddetails %}

Ce qui nous permet de prouver que :

> La fonction $\beta$ est non calculable.
{: .note}
{% details  preuve %}

Supposons que $\beta$ soit calculable. Il existe alors une machine $F$ de pseudo code :

```text
def F(n):

efface l'entrée du ruban

i = 0
tant que i < 2 * β(n):
    écrire 1 sur le ruban et décaler le curseur un cran à droite
    i = i + 1
```

On peut supposer, sans perte de généralité, que l'entrée de $F$ soit uniquement composée de $1$(donc $n$ signifie que l'entrée est composée de n $1$ consécutifs).

De là, on peut également construire la machine $M$ :

```text
def M():
    M_n()
    déplace le curseur à gauche jusqu'à obtenir un blanc puis déplace le curseur d'un cran à droite
    F(n)
```

Cette machine enchaîne $M_n$ à $F$. Pour la sorite de $M_n()$ soit l'entrée de $F$, il faut décaler le ruban pour le placer jusqu'au premier 1 (ceci se fait avec une machine à 3 états). Cette machine à un nombre d'états égal au nombre d'état de $M_n$ plus le nombre d'état de la machine qui déplace le ruban (3) plus le nombre d'état de $F$ (disons $k$) moins les liants entre les machines (les états finaux des machines intermédiaires sont les états initiaux des machines suivantes), c'est à dire 2. Au final, la machine $M$ à : $n + 3 + k - 2 = n + k +1$ états et est telle que $\rho(M) = \beta(2n)$.

On en déduit l'inégalité : $\beta(n + k + 1) \geq \beta(2n)$ et comme $\beta$ est strictement croissante on a l'inégalité : $2n \leq n + k + 1$ pour tout $n > 0$ ce qui est impossible.

{% enddetails %}

> L'[article](https://www.gwern.net/docs/cs/1962-rado.pdf) de Tibor Radò où les busy beavers sont définis.

### réels calculables

Tous les entiers sont calculables, il suffit de créer une machine qui écrit l'entier désiré sur le ruban. Comme les réels ont une notation décimale avec ne infinité de chiffre, on ne peut de toute façon  pas les écrire sur le ruban en temps fini. Certains d'entre eux sont cependant approchable d'aussi prêt que l'on veut à partir d'une machine de Turing :

> Un réel $x$ est calculable s'il existe une machine de Turing $X$ à un paramètre tel que :
>
> * $X(0)$ rend la partie entière de $x$
> * $X(i)$ rend la $i$-ème décimale de $x$, pour tout $i > 0$
>
{: .note}

Il existe d'autres définitions équivalentes, voir [cette page wikipédia](https://fr.wikipedia.org/wiki/Nombre_r%C3%A9el_calculable), des nombres calculable. Un cas particulier important est lorsque le nombre est la limite d'une suite $u_n$ :

> Si $x$ est la limite d'une suite $(u_n)_{n \geq 0}$ et qu'il existe une machine de Turing $M$ telle que $M(n) = u_n$ pour tout $n$, alors $x$ est calculable.
{: .note}
{% details preuve %}

Comme $u_n$ converge vers $x$, pour tout $i> 0$, il existe $N_i$ tel que $\mid x - u_n\mid < 10^{-i}$ pour tout $n > N_i$. Si l'on veut calculer la $i$-ème décimale de $x$, Il suffit de calculer $u_{N_{i}}$ et de prendre sa $i$-ème décimale

{% enddetails %}

Par exemple, $\pi$ est calculable en utilisant [la série de Leibniz de $\pi$](https://fr.wikipedia.org/wiki/Formule_de_Leibniz#S%C3%A9rie_altern%C3%A9e). De la même manière, on peut calculer $cos(x)$, $sin(x) ou encore $\sqrt{x}$ pour tout $x$ calculable grâce à leur [développement en séries entières](https://fr.wikipedia.org/wiki/Formulaire_de_d%C3%A9veloppements_en_s%C3%A9ries).

> Si l'on pense à un réel calculé à partir d'une fonction mathématique usuelle, il y a toute les chance qu'il soit calculable
{: .note}

### réels non calculables

On l'[a démontré]({% link cours/theorie-pratiques-algorithmique/theorie/calcul.md %}#r-et-n), il y a beaucoup plus de réels que de nombres entiers et il y a au plus autant d'algorithmes différents que de nombres entiers. Il y a donc de très nombreux réels qu'on ne peut pas calculer, et beaucoup plus qu'on ne peux en calculer.

Il est cependant dur d'en trouver un car tout ceux auxquels on peut penser sont soit des limites de suites, soit combinaison de fonctions calculables... Les exemples de nombres non calculables sont donc tordus.

> pour montrer quelqeu chose il faut le construire, le décrire : donc utiliser un algorthme pour le faire...
{: .tbd}

Nous allons en montrer un nombre non calculable, le [nombre de Turing](https://fr.wikipedia.org/wiki/Om%C3%A9ga_de_Chaitin#Le_%C2%AB_nombre_de_Turing_%C2%BB), dérivé du célèbre[nombre oméga de Chaitin](https://fr.wikipedia.org/wiki/Om%C3%A9ga_de_Chaitin), lui aussi non dénombrable.

Comme il n'existe qu'un nombre dénombrable de machine de Turing (moins ou égal aux nombres d'entiers), on peut les ranger selon un ordre : $M_1$ première machine de Turing, $M_2$ deuxième machine de Turing, etc.

Le nombre de Turing $T$ est un réel entre 0 et 1 tel que sa $i$-ème décimal soit :

* égale à 1 si la machine $M_i$ s'arrête pour une entrée vide
* égale à 0 si la machine $M_i$ se s'arrête pas pour une entrée vide

Ce nombre n'est évidemment pas calculable car si on pouvait le faire, le problème de l'[arrêt de la machine de Turing](#arret) serait décidable.

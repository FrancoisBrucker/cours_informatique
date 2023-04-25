---
layout: layout/post.njk 
title: Calculabilité

eleventyNavigation:
    order: 6
    prerequis:
        - "../décidabilité/"
        - "../machine-turing/"
        - "../../algorithme/pseudo-code/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On a vu dans la partie [fonctions](../fonctions){.interne} qu'un algorithme ne pouvait pas tout calculer, qu'il y a avait même bien plus de choses qu'on ne pouvait pas faire avec un algorithme que de chose qu'on pouvait faire avec.

Nous allons ici, enfin, exhiber de tels exemples.

{% info %}
Tout comme dans la partie [décidabilité](../décidabilité){.interne}, on utilisera indifféremment des pseudo-codes, code ou machine de Turing pour décrire nos algorithmes, puisque ces trois notions sont équivalentes (on fait nôtre [la thèse de Church-Turing](../../algorithme/pseudo-code/#church-turing){.interne}).
{% endinfo %}

## Fonctions calculables

{% note "**définition**" %}
Un fonction de $f: \mathcal{F} \rightarrow \\{0, 1\\}^\star$, avec $\mathcal{F} \in \\{0, 1\\}^\star$ ($f$ prend en entrée un mot d'un sous-ensemble de $\\{0, 1\\}^\star$ et redonne un mot en sortie) est **calculable** s'il existe un algorithme $A$ telle que :

* $A(\mu) = f(\mu)$ si $\mu \in \mathcal{F}$
* $\mathcal{L}(M) = \mathcal{F}$

{% endnote %}

### Exemples de fonctions calculables

[Quelques exemples](https://en.wikipedia.org/wiki/Computable_function#Examples) :

* les fonctions constantes sont calculables
* si $f$ et $g$ sont deux fonctions calculables, alors $f+g$, $f \cdot g$ et $f \circ g$ sont calculables
* les fonctions dont le domaine de définition est fini, sont calculables
* ...

Beaucoup, beaucoup, beaucoup de fonctions sont calculables, il suffit d'exhiber un algorithme pour le prouver.

De façon plus bizarre, il existe aussi des fonctions, que l'on sait calculable, mais dont on ne connaît pas l'algorithme pour les calculer. Par exemple :

```text
def f(n):
    si il existe n "5" consécutifs dans les décimales de π:
        rend 1
    sinon:
        rend 0
```

La fonction ci-dessus est :

* soit constante et $f(n) = 1$ pour tout $n$ (ce qui est calculable)
* soit il existe $n_0$ tel que pour tout $n \geq n_0$ ont ait $f(n) = 0$ et avant $f(n) = 1$ ($f$ revient à faire un test sur $n$, ce qui est aussi calculable).

Elle est donc calculable, mais on ne sait pas quel algorithme c'est (cas on ne sais pas si π est [un nombre univers](https://fr.wikipedia.org/wiki/Nombre_univers)).

### Calculabilité et décidabilité

Décidabilité et calculabilité sont les deux faces d'une même pièce :

{% note "**proposition**" %}
Si une fonction $f: \mathcal{F} \rightarrow \\{0, 1\\}^\star$ est **calculable** alors $\\{ (a, f(a) \mid a \in \mathcal{F}\\}$ est **reconnaissable**.
{% endnote %}
{% details "preuve" %}

Si $f: \mathcal{F} \rightarrow \\{0, 1\\}^\star$ est calculable, l'algorithme $M$ prenant en entrée deux mots $a$ et $b$ et qui rend *Vrai* si $f(a) = b$ et ne s'arrête pas sinon est bien tel que $\mathcal{L}(M) = \\{ (a, f(a) \mid a \in \mathcal{F}\\}$.

{% enddetails %}

Et si $f$ est défini sur tout mot (ce qui est très souvent le cas) on a même :

{% note "**proposition**" %}
Une fonction $f: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^\star$ est **calculable** si et seulement si $\\{ (a, f(a) \mid a \in \\{0, 1\\}^\star\\}$ est **décidable**.
{% endnote %}
{% details "preuve" %}

Si $f: \mathcal{F} \rightarrow \\{0, 1\\}^\star$ est calculable, l’algorithme $M$ prenant en entrée deux mots $a$ et $b$ et qui rend *vrai* si $f(a) = b$ et *faux* sinon est bien un décideur sur $\\{ (a, f(a) \mid a \in \\{0, 1\\}^\star\\}$

Réciproquement, soit $M$ un décideur sur $\\{ (a, f(a) \mid a \in \\{0, 1\\}^\star\\}$, l'algorithme $M'$ qui prend itérativement tous les mots $b$ et qui rend $b$ lorsque $M(a, b)$ rend *vrai* est bien fini pour tout $a$ et calcule bien $f(a)$.

{% enddetails %}

### <span id="fct-non-calculable"></span>Fonctions non calculables

Comme il suffit d'exhiber un algorithme pour montrer qu'une fonction est calculable, presque toutes les fonctions auxquelles on peut penser le sont. Pour trouver des fonctions non calculables, il faut chercher des exemples tordus.

Nous en donnons une ici, la plus célèbre : [les castors affairés](https://fr.wikipedia.org/wiki/Castor_affair%C3%A9) (*busy beavers* dans la version originale):

{% note "**définition**" %}
On définit le ***score*** $\rho(M)$ d'une machine de Turing $M$ acceptant le mot vide comme étant le nombre de $1$ de $M()$.

La fonction du **castor affairé** $\Sigma : \mathbb{N} \rightarrow \mathbb{N}$ est définie telle que $\beta(n)$ vaut le score maximal pour toutes les machine de Turing à $n$ états acceptant le mot vide.
{% endnote %}

La fonction est bien définie pour tout $n>0$ puisqu'il n'y a qu'un nombre fini de machine de Turing à $n$ états : la valeur $\beta(n)$ est un maximum d'un ensemble fini, ce nombre existe.

{% note "**proposition**" %}
$\beta(n) \geq n - 1$ pour tout $n >0$
{% endnote %}
{% details "preuve" %}

Considérons la machine $M_n$ à $n$ états $(q_0, \dots, q_{n-1}) telle que :

* $q_0$ est l'état initial
* $q_{n-1}$ l'état d'acceptation
* la fonction de transition $\delta$ telle que $\delta(q_i, \sharp) = (q_{i+1}, 1, \rightarrow)$

On a $M_n() = \underbracket{1\cdots 1}_{n-1}{}$.
{% enddetails %}

{% note "**proposition**" %}
$\beta(n)$ est strictement croissante
{% endnote %}
{% details "preuve" %}
Soit $B_n$ une machine à $n$ états telle que $\rho(B_n) = \beta(n)$. La machine obtenue en enchaînant $B_n$ et $M_1$ (voir preuve précédente) en associant l'état final de $B_n$ à l'état initial de $M_1$ a $n+1$ états (les état de B_n$ plus l'état d'acceptation de $M_1$) et sa sorite produit un 1 de plus que $\beta_n$ : $\beta(n+1) \geq \beta(n) + 1$.

{% enddetails %}

Ce qui nous permet de prouver que :

{% note "**proposition**" %}
La fonction $\beta$ est non calculable.
{% endnote %}
{% details "preuve" %}

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

{% lien %}
L'[article](https://www.gwern.net/docs/cs/1962-rado.pdf) de Tibor Radò où les busy beavers sont définis.
{% endlien %}

## Réels calculables

Tous les entiers sont calculables, il suffit de créer une machine qui écrit l'entier désiré sur le ruban. Comme les réels ont une notation décimale avec ne infinité de chiffre, on ne peut de toute façon  pas les écrire sur le ruban en temps fini. Certains d'entre eux sont cependant approchable d'aussi prêt que l'on veut à partir d'une machine de Turing :

{% note "**définition**" %}
Un réel $x$ est ***calculable*** s'il existe une machine de Turing $X$ à un paramètre tel que :

* $X(0)$ rend la partie entière de $x$
* $X(i)$ rend la $i$-ème décimale de $x$, pour tout $i > 0$

{% endnote %}

Il existe d'autres définitions équivalentes, voir [cette page Wikipédia](https://fr.wikipedia.org/wiki/Nombre_r%C3%A9el_calculable), des nombres calculable.

### Exemples de réels calculables

Un cas particulier important est lorsque le nombre est la limite d'une suite $u_n$ :

{% note "**proposition**" %}
Si $x$ est la limite d'une suite $(u_n)_{n \geq 0}$ et qu'il existe une machine de Turing $M$ telle que $M(n) = u_n$ pour tout $n$, alors $x$ est calculable.
{% endnote %}
{% details "preuve" %}

Comme $u_n$ converge vers $x$, pour tout $i> 0$, il existe $N_i$ tel que $\mid x - u_n\mid < 10^{-i}$ pour tout $n > N_i$. Si l'on veut calculer la $i$-ème décimale de $x$, Il suffit de calculer $u_{N_{i}}$ et de prendre sa $i$-ème décimale

{% enddetails %}

Par exemple, $\pi$ est calculable en utilisant [la série de Leibniz de $\pi$](https://fr.wikipedia.org/wiki/Formule_de_Leibniz#S%C3%A9rie_altern%C3%A9e). De la même manière, on peut calculer $cos(x)$, $sin(x)$ ou encore $\sqrt{x}$ pour tout $x$ calculable grâce à leur [développement en séries entières](https://fr.wikipedia.org/wiki/Formulaire_de_d%C3%A9veloppements_en_s%C3%A9ries).

{% note %}
Si l'on pense à un réel calculé à partir d'une fonction mathématique usuelle, il y a toute les chances qu'il soit calculable
{% endnote %}

### Exemples de réels non calculables

On l'[a démontré](../fonctions#r-et-n){.interne}, il y a beaucoup plus de réels que de nombres entiers et il y a au plus autant d'algorithmes différents que de nombres entiers. Il y a donc de très nombreux réels qu'on ne peut pas calculer, et beaucoup plus qu'on ne peux en calculer.

Il est cependant dur d'en trouver un car tout ceux auxquels on peut penser sont soit des limites de suites, soit combinaison de fonctions calculables... Les exemples de nombres non calculables sont donc tordus.

Nous allons en montrer un nombre non calculable, le [nombre de Turing](https://fr.wikipedia.org/wiki/Om%C3%A9ga_de_Chaitin#Le_%C2%AB_nombre_de_Turing_%C2%BB), dérivé du célèbre [nombre oméga de Chaitin](https://fr.wikipedia.org/wiki/Om%C3%A9ga_de_Chaitin), lui aussi non dénombrable.

Comme il n'existe qu'un nombre dénombrable de machine de Turing (moins ou égal aux nombres d'entiers), on peut les ranger selon un ordre : $M_1$ première machine de Turing, $M_2$ deuxième machine de Turing, etc.

Le nombre de Turing $T$ est un réel entre 0 et 1 tel que sa $i$-ème décimal soit :

* égale à 1 si la machine $M_i$ s'arrête pour une entrée vide
* égale à 0 si la machine $M_i$ se s'arrête pas pour une entrée vide

Ce nombre n'est évidemment pas calculable car si on pouvait le faire, le problème de l'[arrêt](./#arret){.interne} serait décidable.

## Fonctions calculable rigolotes

On va montrer deux exemples de fonctions calculables. L'une qui grossi très très vite (la fonction d'Ackermann) et l'autre (la fonction de Takeuchi) qui calcule des choses simples de façon compliquées.

Ces deux fonctions sont parfois utilisées pour des tests de performance d'ordinateurs car est sont très  gourmandes en temps de calcul.

### Fonction d'Ackermann

La [fonction d'Ackermann](https://fr.wikipedia.org/wiki/Fonction_d%27Ackermann), outre le fait qu'elle est rigolote car elle croît très très rapidement (plus que factoriel, c'est dire), est importante théoriquement car c'est la première fonction connue que l'on ne peut pas écrire avec des boucles `for`{.language-}. On est obligé d'utiliser soit des boucles `while`{.language-} pour écrire son pseudo-code de façon itérative, soit d'utiliser la récursivité (ce que l'on va faire).

{% info %}
Notez que tout algorithme récursif peut s'écrire de façon itérative. C'est ce quel'on appelle la dé-curryfication.
{% endinfo %}

Elle se définit de la manière suivante, pour tous entiers m et n positifs :

<div>
$$
A(m, n) = \left\{
    \begin{array}{ll}
        n + 1 & \mbox{si } m = 0 \\
        A(m - 1, 1) & \mbox{si } n = 0 \\
        A(m - 1, A(m, n - 1)) & \mbox{sinon.}
    \end{array}
\right.
$$
</div>

{% note "**Proposition**" %}
La fonction d'Ackermann est bien définie pour tout $m$ et $n$ entiers.
{% endnote %}
{% details "preuve" %}
Pour chaque appel récursif de la fonction d'Ackermann, soit m, soit $n$ est strictement plus petit dans la fonction appelée que dans la fonction appelante. On arrivera donc toujours à $m = 0$ qui stoppera la récursion ou $n = 0$ qui fera baisser la valeur de $m$.
{% enddetails %}

Le nombre de récursion est très très important. Pour calculer $A(2, 3)$ par exemple, on a les récurrences suivantes :

* $A(2, 3) = A(1, A(2, 2))$
* $A(2, 2) = A(1, A(2, 1))$
* $A(2, 1) = A(1, A(2, 0))$
* $A(2, 0) = A(1, 1)$
* $A(1, 1) = A(0, A(1, 0))$
* $A(1, 0) = A(0, 1) = 2$
* puis on remonte d'un cran et les récursions recommencent...

Au final on trouve $A(2, 3) = 9$. La fonction croît très très vite. Par exemple $A(5, 0) = A (4, 1) = 65533$ et $A(4, 2) = $2^{65536} - 3$.

Sa complexité est de plus supérieure : il faut plus de $A(m, n)$ opérations pour calculer $A(m, n)$ puisque l'on ne fait qu'ajouter 1 à n comme calcul et les valeurs de n sont modifiées de +1 ou -1.

### Fonction de Takeuchi

La [fonction de Takeuchi](https://fr.wikipedia.org/wiki/Fonction_de_Takeuchi) peut être vue comme une illustration du [Théorème de Rice](../décidabilité#théorème-rice){.interne}, bien malin qui sait ce qu'elle fait juste ne la regardant.

Elle est définie pour tous entiers $x$, $y$ et $z$ telle que :

<div>
$$
\tau(x, y, z) = \left\{
    \begin{array}{ll}
         y & \mbox{si } x \leq y\\
        \tau(\tau(x-1, y, z), \tau(y-1, z, x), \tau(z-1, x, y)) & \mbox{sinon.}
    \end{array}
\right.
$$
</div>

Le nombre de récurrence est très élevé et pourtant, on peut montrer qu'elle calcule :

<div>
$$
\tau(x, y, z) = \left\{
    \begin{array}{ll}
        y & \mbox{si } x \leq y\\
        z & \mbox{si } x > y \mbox{ et } y \leq z\\
        x & \mbox{si } x > y \mbox{ et } y > z\\
    \end{array}
\right.
$$
</div>
{% details "preuve" %}

Par récurrence sur $x+y+z= k$.

Si $x+y+z=0$, on a  $x=y=z=0$ et $\tau(0, 0, 0) = 0$, la récurrence est vérifiée. On suppose la récurrence vraie pour $x+y+z=k$.

Pour $x+y+z=k+1$, on analyse tous les cas possibles :

* $x \leq y$ : Ok
* $x > y$ et $y \leq z$ : On a $\tau(x, y, z) = \tau(\tau(x-1, y, z), \tau(y-1, z, x), \tau(z-1, x, y))$ :
  * on a $y-1 \leq z$ donc (par hypothèse de récurrence) $\tau(y-1, z, x) = z$
  * soit $x-1 > y$ et $y \leq z$ et alors (par hypothèse de récurrence) $\tau(x-1, y, z) = z$ : $\tau(x, y, z) = \tau(z, z, ?) = z$
  * soit $x-1 \leq y$ et alors (par hypothèse de récurrence) $\tau(x-1, y, z) = y$ : $\tau(y, z, ?) = z$ (puisque $y \leq z$)
* $x > y > z$ : On a $\tau(x, y, z) = \tau(\tau(x-1, y, z), \tau(y-1, z, x), \tau(z-1, x, y))$
  * on a $z-1 < y< x$ et donc $\tau(x, y, z) =  \tau(\tau(x-1, y, z), \tau(y-1, z, x), x)$
  * on procède de même que précédemment en analysant tous les cas
    * $x-1 > y$ et $y-1>z$ : $\tau(x, y, z) = \tau(x-1, x, x) = x$
    * $x-1 > y$ et $y-1=z$ : $\tau(x, y, z) = \tau(x-1, z, x) = x$
    * $x-1 = y$ et $y-1>z$ : $\tau(x, y, z) = \tau(y, x, x) = x$
    * $x-1 = y$ et $y-1=z$ : $\tau(x, y, z) = \tau(y, z, x) = x$
{% enddetails %}

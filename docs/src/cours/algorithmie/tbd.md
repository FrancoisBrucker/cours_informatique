---
layout: layout/post.njk 
title: Calculabilité fin à remettre autrepart

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



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

### Exemples de réels non calculables

On l'[a démontré](../fonctions#r-et-n){.interne}, il y a beaucoup plus de réels que de nombres entiers et il y a au plus autant d'algorithmes différents que de nombres entiers. Il y a donc de très nombreux réels qu'on ne peut pas calculer, et beaucoup plus qu'on ne peux en calculer.

Il est cependant dur d'en trouver un car tout ceux auxquels on peut penser sont soit des limites de suites, soit combinaison de fonctions calculables... Les exemples de nombres non calculables sont donc tordus.

Nous allons en montrer un nombre non calculable, le [nombre de Turing](https://fr.wikipedia.org/wiki/Om%C3%A9ga_de_Chaitin#Le_%C2%AB_nombre_de_Turing_%C2%BB), dérivé du célèbre [nombre oméga de Chaitin](https://fr.wikipedia.org/wiki/Om%C3%A9ga_de_Chaitin), lui aussi non dénombrable.

Comme il n'existe qu'un nombre dénombrable de machine de Turing (moins ou égal aux nombres d'entiers), on peut les ranger selon un ordre : $M_1$ première machine de Turing, $M_2$ deuxième machine de Turing, etc.

Le nombre de Turing $T$ est un réel entre 0 et 1 tel que sa $i$-ème décimal soit :

* égale à 1 si la machine $M_i$ s'arrête pour une entrée vide
* égale à 0 si la machine $M_i$ se s'arrête pas pour une entrée vide

Ce nombre n'est évidemment pas calculable car si on pouvait le faire, le problème de l'[arrêt](./#arret){.interne} serait décidable.


## TBD


Montrons tout de suite que cette définition à du sens :


> TBD c'est pas une bêtise car il y a plus de fonction que d'algorithmes...

> TBD f(n) -> n. 
> 
> puis exemple.

> TBD partie sur : et marche aussi pour f(n1, ..., nn) -> n
> on peut aussi faire f(n) = {0, 1} si on a envie.
> encore une fois c'est pas tout le monde car il y a

---
layout: layout/post.njk
title: Fonctions récursives primitives 

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Les [fonctions récursives primitives](https://fr.wikipedia.org/wiki/Fonction_r%C3%A9cursive_primitive) sont un cas particulier important des fonctions calculables. La plupart des fonction mathématiques usuelles en sont !

{% lien %}

- <https://www.andrew.cmu.edu/user/kk3n/recursionclass/chap2.pdf>
- <https://www.youtube.com/watch?v=yaDQrOUK-KY&list=PLC-8dKj3F0NUnR8LeBGH3utAI9aQjFbi5&index=1>

{% endlien %}

Elles sont définies à partir de trois fonctions de base :

{% note "**Définition**" %}

Les _**fonctions récursives primitives de bases**_ sont :

- _**les fonctions zéro**_ $\mathbb{0}^n$ ($0 \leq n$) :

    <div>
    $$
    \begin{align*}
    \mathbb{N}^n &\to \mathbb{N}\\
    (x_1, \dots, x_n)  &\mapsto 0
    \end{align*}
    $$
    </div>
- _**les fonctions projections**_ $\pi^n_i$ ($0 \leq i \leq n$) :

    <div>
    $$
    \begin{align*}
    \mathbb{N}^n &\to \mathbb{N}\\
    (x_1, \dots, x_n)  &\mapsto x_i
    \end{align*}
    $$
    </div>

- _**la fonctions successeur**_ $\text{succ}$ :

    <div>
    $$
    \begin{align*}
    \mathbb{N}&\to \mathbb{N}\\
    x &\mapsto x+1
    \end{align*}
    $$
    </div>

{% endnote %}

Dont il est clair qu'elles sont calculables, au moins pour les fonctions zéro et les projections.

{% exercice %}
Exhibez un algorithme permettant de calculer $\text{succ}$ lorsque les entiers sont codées sous forme binaire $x = x_p\dots x_0$ avec $x_i \in \{ 0, 1\}$ et $x = \sum_{0\leq i \leq p}x_i2^i$.
{% endexercice %}
{% details "corrigé" %}

>TBD addition binaire avec retenue.

{% enddetails %}

Les fonctions primitives récursives sont alors toutes les fonctions que l'on peut obtenir en combinant les fonctions de base en utilisant les règles de **_composition_** et de **_récursion_**.

La règle de composition est classique :

<div id="composition"></div>
{% note "**Définition**" %}
Soient :

- $f: \mathbb{N}^n \to \mathbb{N}$
- $g_i: \mathbb{N}^m \to \mathbb{N}$ pour $1 \leq i \leq n$.

La **_composition_** de $f$ par $(g_i)_{1\leq i \leq n}$ est notée $f \circ [g_1, \dots, g_n]$ et vaut :

<div>
$$
\begin{align*}
    \mathbb{N}^m &\to \mathbb{N}\\
    (x_1, \dots, x_m)  &\mapsto f(g_1(x_1, \dots, x_m), \dots, g_n(x_1, \dots, x_m))
\end{align*}
$$
</div>

{% endnote %}

Il est clair que s'il existe un algorithme pour créer $f$ et $g$, l'algorithme suivant fonctionne pour créer la composition :

```text
Nom : composition
Entrées :
    n, m : entiers
    x[] : un tableau de m entiers
    f : une fonction à n paramètres
    g[i] : un tableau de n fonctions à m paramètres
Programme :
    soit y[] un tableau à n entiers
    pour chaque i allant de 1 à n:
        y[i] = g[1](x[])
    rendre f(y[])
```

Remarquez que la composition dépend des domaines de validité des fonctions $f$ et $g[i]$, on passe donc un tableau en paramètre de la fonction pour que l'appel de la fonction soit identique quelque soit $n$ et $m$. La composition permet déjà de créer des choses nouvelles, en particulier les fonctions constantes, par exemple la fonction : $\mathbb{1}^n = \text{succ} \circ [\mathbb{0}^n]$ est la fonction rendant tout le temps 1.

{% exercice %}
Montrez que la fonction $\mathbb{k}^n(x_1, \dots, x_n) = k$ existe pour tout $n\geq 0$ et tout $k \geq 0$.
{% endexercice %}
{% details "corrigé" %}
On le montre par récurrence sur $k$.

- initialisation : Pour $k=0$ la propriété est vraie
- on suppose que pour $k\geq 0$ la fonction $\mathbb{k}^n(x_1, \dots, x_n) = k$ est primitive récursive.
- la fonction $\text{succ} \circ [\mathbb{k}^n]$ est alors également primitive récursive et vaut $k+1$ tout le temps ce qui conclut la preuve.

{% enddetails %}

Ou encore l'ajout d'une constante :

{% exercice %}
Montrez que la fonction $f_k(x) = x + k$ est primitive récursive, pour tout entier $k\geq 0$.
{% endexercice %}
{% details "corrigé" %}

Par récurrence sur $k$. On a $f_0(x) = \pi^1_1$. Si on suppose que $f_k$ existe alors $f_{k+1} = f_k \circ [\text{succ}]$.

{% enddetails %}

On ne peut utiliser que cette règle car elle ne permet pas de créer des fonctions toutes simples (et calculable) comme $\text{add}(x, y) = x + y$. On a besoin pour cela de pouvoir itérer le processus d'ajouter 1 un nombre quelconque de fois, bref de simuler une boucle. Pour cela, on utilise... la récursion :

{% note "**Définition**" %}
Soit :

- $f: \mathbb{N}^n \to \mathbb{N}$
- $g: \mathbb{N}^{n+2} \to \mathbb{N}$

La **_récursion_** de $f$ par $g$ est une fonction de $\mathbb{N}^{n+1} \to \mathbb{N}$, notée $\rho^n(f, g)$, et définie récursivement telle que :

<div>
$$
\begin{align}
    \begin{cases}
     \rho^n(f, g)(0, x_1, \dots, x_n)&= f(x_1, \dots, x_n) \\
     \rho^n(f, g)(x+1, x_1, \dots, x_n)&= g(x, \rho^n(f, g)(x, x_1, \dots, x_n), x_1, \dots, x_n)
\end{cases}
\end{align}
$$
</div>

{% endnote %}

Dans la définition de la récursion, la fonction $g$ fait office d'algorithme permettant d'ajouter par récurrence un paramètre à $f$.

{% exercice %}
Exhibez un algorithme sans récursion permettant de calculer $\rho^n(f, g)$.
{% endexercice %}
{% details "corrigé" %}

```text
Nom : récursion
Entrées :
    x[] : un tableau de n+1 entiers
    f : une fonction à n paramètres
    g[] : un tableau de n fonctions à n+2 paramètres
Programme :
    h = f(x[2:])
    pour chaque i allant de 0 à x[1] - 1:
        h = g(i, h, x[2:])

    rendre h
```

On a la aussi supposé que les fonctions prenaient des tableaux en paramètre pour ne pas se préoccuper du nombre de paramètres lors de l'appel.
{% enddetails %}

Le simple ajout de cette règle permet de créer l'addition :

<div>
$$
\begin{align}
    \begin{cases}
     \text{add}(0, y)&= y \\
     \text{add}(x+1, y)&= \text{succ}(\text{add}(x, y)) \\
\end{cases}
\end{align}
$$
</div>

On a utilisé un petit raccourci d'écriture qui la rend plus lisible. La fonction $g$ de la définition de la récursion explicite juste le fait que la valeur en $x+1$ dépend de la valeur en $x$, de $x$ ainsi que des autres paramètres :

<div>
$$
\begin{align}
    \begin{cases}
     f&= \pi^2_2 \\
     g(x, y) &= \text{succ} \circ [\pi^3_2] \\
\end{cases}
\end{align}
$$
</div>

L'ajout de cet opérateur permet d'ajouter tout un tas de fonctions. La fonction prédécesseur par exemple:

<div>
$$
\begin{align}
    \begin{cases}
     \text{pred}(0)&= 0 \\
     \text{pred}(x+1)&= x \\
\end{cases}
\end{align}
$$
</div>

Ou encore la soustraction et la multiplication :

{% exercice %}
Écrivez la soustraction :

$$
\text{sub}(x, y) = x-y \text{ si } x> y \text{ et } 0 \text{ sinon}
$$

{% endexercice %}
{% details "corrigé" %}

<div>
$$
\begin{align}
    \begin{cases}
     \text{sub}(x, 0)&= x \\
     \text{sub}(x, y + 1)&= \text{pred}(\text{sub}(x, y)) \\
\end{cases}
\end{align}
$$
</div>

{% enddetails %}
{% exercice %}
Montrez que la fonction $\text{mul}(x, y) = x \times y$ est primitive récursive.
{% endexercice %}
{% details "corrigé" %}

<div>
$$
\begin{align}
    \begin{cases}
     \text{mul}(0, y)&= \pi^2_2 \\
     \text{mul}(x+1, y)&= \text{add}(x, \text{mul}(x, y)) \\
\end{cases}
\end{align}
$$
</div>

{% enddetails %}

Comme toute composition finie d'algorithme reste un algorithme, on a la proposition suivante :

{% note "**Proposition**" %}
Les fonctions récursives primitives sont calculables.
{% endnote %}

Ca n'a pas l'air comme ça, mais les fonctions récursives primitives permettent de créer toutes les fonctions arithmétiques usuelles (voir [arithmétique de Peano](https://fr.wikipedia.org/wiki/Axiomes_de_Peano)) et ont été utilisées par Gödel pour montrer son [célèbre théorème d'incomplétude](https://perso.ens-lyon.fr/natacha.portier/enseign/logique/GoedelParAlex.pdf).

{% attention "**À retenir**" %}
Ce type de construction où l'on combine simplement des éléments basiques pour produire des choses complexes est l'essence même de l'informatique et de l'algorithmie.

**Nous n'allons cesser de le montrer dans ce cours.**
{% endattention %}

On peut aussi faire des fonctions plus logiques comme le maximum ou le minimum, ou encore la valeur absolue... Bref, il y a de quoi s'amuser. Par exemple la fonction $\text{eq}_0(x) = 1 \text{ si } x = 0 \text{ et } \text{eq}_0(x) = 0 \text{ sinon}$ est primitive récursive puisque :

<div>
$$
\begin{align}
    \begin{cases}
     \text{eq}_0(0)&= 1 \\
     \text{eq}_0(x+1)&= 0 \\
\end{cases}
\end{align}
$$
</div>

Ce qui va permet de montrer que l'égalité  l'est aussi :

{% exercice %}
Montrez que la fonction égalité : $\text{eq}(x, y) = 1 \text{ si } x = y \text{ et } 0 \text{ sinon}$ est récursive primitive.
{% endexercice %}
{% details "corrigé" %}

C'est la fonction :

<div>
$$
\text{eq}_0(\text{sub}(x,y)) + \text{eq}_0(\text{sub}(y, x)) - 1
$$
</div>

{% enddetails %}

Si ce genre d'exemples vous intéresse, allez jeter un œil au lien suivant :

{% lien %}

- [exemples de fonctions primitives récursives](https://www.michaelbeeson.com/teaching/StanfordLogic/Lecture4Slides.pdf)
- [logique et fonctions primitives récursives](https://www.cs.utep.edu/vladik/cs5315.21/pr2.pdf)

{% endlien %}

On ne peut qu'être ébahi par le fait qu'il ne faut vraiment rien (trois fonctions ridiculement simples) et deux fonctions (naturelles) de composition pour créer toutes ces fonctions très différentes les unes des autres.

{% exercice %}
Montrez que si $f$, $g$ et $h$ sont trois fonctions primitives récursives de $\mathbb{N}^p \rightarrow \mathbb{N}$ alors la fonction "$\text{si } (f(x) = 0) \text{ alors } g(x) \text{ sinon } h(x)$" l'est aussi.
{% endexercice %}
{% details "corrigé" %}

C'est la fonction :

<div>
$$
\text{eq}_0(f(x)) \times g(x) + \text{eq}_0(\text{eq}_0(f(x))) \times h(x)
$$
</div>

{% enddetails %}

{% attention "**À retenir**" %}
La quasi totalité des fonctions mathématiques usuelles sont primitives récursives, donc calculables uniquement en utilisant des boucles de type _"pour chaque"_.
{% endattention %}

C'est pourquoi on s'est longtemps demandé si calculabilité et fonctions récursives primitives n'étaient pas synonymes. Ce n'est pas le cas, comme nous allons tout de suite le voir.

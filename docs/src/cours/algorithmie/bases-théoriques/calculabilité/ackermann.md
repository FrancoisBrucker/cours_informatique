---
layout: layout/post.njk
title: Fonction d'Ackermann

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La [fonction d'Ackermann](https://fr.wikipedia.org/wiki/Fonction_d%27Ackermann), outre le fait qu'elle est rigolote car elle croît très très rapidement (plus que factoriel, c'est dire), est importante théoriquement car c'est le premier exemple connu de fonction calculable mais non primitive récursive.

Elle se définit de la manière suivante, pour tous entiers $m$ et $n$ positifs :

<div>
$$
\text{Ack}(m, n) = \left\{
    \begin{array}{ll}
        n + 1 & \mbox{si } m = 0 \\
        \text{Ack}(m - 1, 1) & \mbox{si } n = 0 \\
        \text{Ack}(m - 1, \text{Ack}(m, n - 1)) & \mbox{sinon.}
    \end{array}
\right.
$$
</div>

Nous allons dans cette partie montrer que la définition précédente est bien calculable, puis donner une idée de ses valeurs.

## Existence

Pour chaque appel récursif de la fonction d'Ackermann, soit $m$, soit $n$ est strictement plus petit dans la fonction appelée que dans la fonction appelante. On arrivera donc toujours à $m = 0$ qui stoppera la récursion ou $n = 0$ qui fera baisser la valeur de $m$. Il n'y aura donc toujours qu'un nombre finie de récursion pour tout couple $(m, n)$.

Montrons le formellement :

{% note "**Proposition**" %}
La fonction d'Ackermann est bien définie (nécessite un nombre fini de recursion pour être calculée) pour tous $m$ et $n$ entiers positifs.
{% endnote %}
{% details "preuve", "open" %}

On va montrer par récurrence sur $m$ que la fonction $A_m(n) = \text{Ack}(m, n)$ se calcule en un nombre fini de recursion pour tout $n$.

**Initialisation (1) :$ m = 0$**. Puisque $A_0(n) = n+1$, la proposition est vérifiée.

**Soit un entier $m\geq 0$ et supposons que $A_{m'}(x)$ se calcule en un nombre fini de récursion pour tout $m'\leq m$ et tout $x\geq 0$.**. Démontrons que $A_{m+1}(n)$ se calcule en un nombre fini de recursion pour pour tout $n\geq 0$. On va le faire également par récurrence, mais sur $n$.

**Initialisation (2) :$ n = 0$**. On a $A_{m+1}(0) = A_{m}(1)$ qui se calcule en un nombre fini de récursion par l'hypothèse de récurrence sur $m$.

**Soit un entier $n\geq 0$ et supposons que $A_{m+1}(n')$ se calcule en un nombre fini de récursion pour tout $n'\leq n$**. Comme on a $A_{m+1}(n+1) = A_{m}(A_{m+1}(n))$ et que :

- par hypothèse de récurrence sur $n$, $A_{m+1}(n)$ se calcule en un nombre fini de recursion,
- par hypothèse de récurrence sur $m$, $A_{m}(x)$ se calcule en un nombre fini de recursion pour tout $x$.

Le nombre total de récursions est fini, ce qui conclut la preuve par récurrence sur $n$ : **fin de la récurrence (2)**.

On a donc que $A_{m+1}(n')$ se calcule en un nombre fini de récursion pour tout $n'\leq n$, ce qui conclut la preuve par récurrence sur $m$ : **fin de la récurrence (1)** et donc de la preuve.

{% enddetails %}

La fonction étant définie on peut écrire l'algorithme suivant, qui va bien fonctionner :

```text
Nom : Ack
Entrées :
    m, n : entiers
Programme :
    Si m = 0:
        rendre l'entier n + 1
    Si n = 0:
        rendre Ack(m-1, 1)
    Sinon:
        calculer n' = Ack(m, n-1)
        rendre Ack(m-1, n')
```

Le calcul de la fonction en utilisant l'algorithme précédent est possible, mais le nombre de récursions est très très important. Pour calculer $\text{Ack}(2, 3)$ par exemple, on a les récurrences suivantes :

- $\text{Ack}(2, 1) = \text{Ack}(1, \text{Ack}(2, 0))$
  - $\text{Ack}(2, 0) = \text{Ack}(1, 1)$
    - $\text{Ack}(1, 1) = \text{Ack}(0, \text{Ack}(1, 0))$
      - $\text{Ack}(1, 0) = \text{Ack}(0, 1) = 2$
    - $\text{Ack}(1, 1) = \text{Ack}(0, 2) = 3$
  - $\text{Ack}(2, 0) = \text{Ack}(1, 1) = 3$
- $\text{Ack}(2, 1) = \text{Ack}(1, 3)$
  - $\text{Ack}(1, 3) = \text{Ack}(0, \text{Ack}(1, 2))$
    - $\text{Ack}(1, 2) = \text{Ack}(0, \text{Ack}(1, 1))$
      - $\text{Ack}(1, 1) = \text{Ack}(0, \text{Ack}(1, 0))$
        - $\text{Ack}(1, 0) = \text{Ack}(0, 1)= 2$
      - $\text{Ack}(1, 1) = \text{Ack}(0, 2) = 3$
    - $\text{Ack}(1, 2) = \text{Ack}(0, 3) = 4$
  - $\text{Ack}(1, 3) = \text{Ack}(0, 4) = 5$
- $\text{Ack}(2, 1) = \text{Ack}(1, 3) = 5$

Au final on trouve $\text{Ack}(2, 1) = 5$. Toutes ces récursions pour ça. Attention cependant, ces nombres vont grossir très très vite.

### Valeurs

Donnons une valeur à la fonction d'Ackermann. On doit cette évaluation à [D. Knuth](https://fr.wikipedia.org/wiki/Donald_Knuth) qui pour cela a inventé une nouvelle opération mathématique, l'opération $x \uparrow y$ :

{% lien %}
[Puissances itérées de Knuth](https://fr.wikipedia.org/wiki/Notation_des_puissances_it%C3%A9r%C3%A9es_de_Knuth)
{% endlien %}

On définit cette opération comme suit :

{% note "**Définition**" %}
Soient $a$ et $b$ deux entiers strictement positif. On note :

<div>
$$
\left\{
    \begin{array}{ll}
        a \uparrow^{(0)} b & = & \underbrace{a+ \cdots + a}_\textrm{b fois} & = & a \times b\\
        a \uparrow^{(1)} b & = & \underbrace{a \times \cdots \times a}_\textrm{b fois} & = & a^b\\
        a \uparrow^{(k)} b & = & \underbrace{a \uparrow^{(k-1)} \cdots \uparrow^{(k-1)} a}_\textrm{b fois}& = & a \uparrow^{(k-1)} (a \uparrow^{(k)} (b-1)) & \textrm{pour } k>1
    \end{array}
\right.
$$
</div>

On notera aussi le cas limite $a \uparrow^{(k)} 0 = 1$ pour tout entier $k$.
{% endnote %}

C'est une notation extrêmement compacte pour écrire des monstres. Par exemple :

- $2 \uparrow^{(0)} 4 = 2+ 2+ 2+ 2= 8$ (ce qui est petit)
- $2 \uparrow^{(1)} 4 = 2\times 2\times 2\times 2 = 2^4 = 16$ (ce qui va),
- $2 \uparrow^{(2)} 4 = 2^{2^{2^2}} = 2^{16} = 65536$ (ce qui fait soudain beaucoup),
- $2 \uparrow^{(3)} 4 = 2 \uparrow^{(2)} 2 \uparrow^{(2)} 2 \uparrow^{(2)} 2 = 2 \uparrow^{(2)} (2 \uparrow^{(2)} 2 \uparrow^{(2)} 2) = 2 \uparrow^{(2)} (2 \uparrow^{(2)} 4) = 2 \uparrow^{(2)} 65536 = 2 \uparrow^{(1)} (2 \uparrow^{(1)} 65535) =2^{2^{65535}}$ (ce qui fait beaucoup trop)

Ces nombres sont énormes ! Rien que les écrire va prendre du temps. Si l'on suppose que l'on peut écrire le chiffre `1` ou `0` en .1s, l'écriture en base 2 des nombres ci-dessus (ce sont tous des puissances de 2) prendra :

- .3s pour $2 \uparrow^{(0)} 4$
- .4s pour $2 \uparrow^{(1)} 4$
- 1.6s pour $2 \uparrow^{(2)} 4$
- $2^{65500}$ millénaires pour $2 \uparrow^{(3)} 4$

{% note "**À retenir**" %}
Ce n'est pas parce que l'on peut calculer quelque chose qu'on peut le faire en pratique, du moins si on est pas immortel.
{% endnote %}
{% info %}
Lorsque l'on vous donne ce genre de grandeurs, ayez à l'esprit qu'il n'y a que de l'ordre de $10^{80}$ particules dans l'univers, ce qui est bien plus petit que $2^{65500}$.

cf. <https://fr.wikipedia.org/wiki/Ordres_de_grandeur_de_nombres#1039_%C3%A0_10100>
{% endinfo %}

Les nombres $2 \uparrow^{(m)} n$ vont être liés à la fonction d'Ackermann. Commençons donc par nous familiariser avec :

{% exercice %}
Montrez que pour tout $m\geq 0$ on a :

1. $2 \uparrow^{(m)} 1 = 2$
2. $2 \uparrow^{(m)} 2 = 4$
3. $2 \uparrow^{(m)} n > m + n$ pour $n \geq 3$
4. $2 \uparrow^{(m)} (n+1) \leq 2 \uparrow^{(m + 1)} (n)$ pour $n \geq 3$
{% endexercice %}
{% details "corrigé" %}

> TBD 1. et 2. en appliquant la formule.
>
> TBD 3. par récurrence sur m et par croissance de la fonction.
>
> TBD 4. Par récurrence sur $n$. Pour $n=3$ on a : $2 \uparrow^{(k)} (3+1) = 2 \uparrow^{(k)} (2 \uparrow^{(k+1) 2}) = 2 \uparrow^{(k+1)} (3)$
>

{% enddetails %}

On peut maintenant montrer la valeur (presque) explicite de la fonction d'Ackermann :

{% note "**Proposition**" %}

<div>
$$
\left\{
    \begin{array}{ll}
        \text{Ack}(0, n) = n+1&\\
        \text{Ack}(1, n) = 2 + (n+3) - 3&\\
        \text{Ack}(m, n) = 2 \uparrow^{(m-2)} (n+3) - 3&\text{pour }m>1\\
    \end{array}
\right. %}
$$
</div>

{% endnote %}
{% details "preuve", "open" %}
Commençons par traiter les 2 premiers cas :

- $\text{Ack}(0, n) = n+1$ est vrai par définition
- Comme $\text{Ack}(1, n) = \text{Ack}(0, \text{Ack}(1, n-1)) = \text{Ack}(1, n-1) + 1$ et que $\text{Ack}(1, 0) = \text{Ack}(0, 1) = 2$, une récurrence triviale sur $n$ nous donne $\text{Ack}(1, n) = n+2 = 2 + (n+3) - 3$

Pour le dernier cas, commençons par montrer par récurrence sur $n$ que $\text{Ack}(2, n) = 2 \uparrow^{(0)} (n+3) - 3$ :

- $\text{Ack}(2, 0) = \text{Ack}(1, 1) = 3 = 2 \uparrow^{(0)} (0+3) - 3$
- on suppose la propriété vraie pour $n$. Pour $n+1$ on a $\text{Ack}(2, n+1) = \text{Ack}(1, \text{Ack}(2, n)) = \text{Ack}(2, n) + 2 = 2 \uparrow^{(0)} (n+3) - 1 = 2n + 5$ par hypothèse de récurrence. Comme $2 \uparrow^{(0)} (n+1+3) - 3 = 2n + 5$, ceci conclut la preuve par récurrence.

On peut terminer la preuve en prouvant par récurrence sur $m > 1$ que $\text{Ack}(m, n) = 2 \uparrow^{(m-2)} (n+3) - 3$. On vient de le montrer pour $m=2$, supposons la vraie pour $m$ et prouvons le $m+1$.

Ce que l'on va faire par sur $n$ :

- $\text{Ack}(m+1, 0) = \text{Ack}(m, 1) = 2 \uparrow^{(m-2)} (1+3) - 3$. Comme l'exercice nous a montré que $4 = 2 \uparrow^{(m-1)} (2)$ et comme $2 \uparrow^{(m-2)} (2 \uparrow^{(m-1)} (2)) = 2 \uparrow^{(m-1)} (0+3)$ on a bien $\text{Ack}(m+1, 0) =  2 \uparrow^{(m-1)} (0+3) - 3$
- on suppose la propriété vraie pour $n$. Pour $n+1$ on a $\text{Ack}(m+1, n+1) = \text{Ack}(m, \text{Ack}(m+1, n)) = 2 \uparrow^{(m-2)} (2 \uparrow^{(m-1)} (n+3) - 3+3) - 3$. On conclut en appliquant la formule pour obtenir $\text{Ack}(m+1, n+1) = 2 \uparrow^{(m+1-2)} (n+1 + 3) - 3$
{% enddetails %}

La fonction d'Ackermann produit donc des nombres proprement gigantesques et est strictement croissante en ses deux variables :

- $\text{Ack}(m, n) < \text{Ack}(m, n + 1)$
- $\text{Ack}(m, n) < \text{Ack}(m + 1, n)$

De plus la proposition précédente nous permet d'écrire :

- $\text{Ack}(2, n) > 2n$
- $\text{Ack}(m, n) > m + n$
- $\text{Ack}(m, n+1) \leq \text{Ack}(m+1, n)$

L'exercice précédent montre que la fonction d'Ackermann croit très vite en $m$ puisque toute somme ou composition de fonction d'Ackermann va être borné à un moment par une autre fonction d'Ackermann.

## Nombre de récursion

Intuitivement, le nombre de récursions nécessaire pour effectuer le calcul de la valeur de la fonction d'Ackermann est de l'ordre de sa valeur puisque les appels récursif se font en décrémentant les valeurs des paramètres de 1. Formalisons ceci :

{% note "**Proposition**" %}

Le nombre de récursion nécessaire pour calculer la fonction d'Ackermann en utilisant la définition est définie telle que :

<div>
$$
\left\{
    \begin{array}{ll}
        \text{R}(0, n) = 0&\\
        \text{R}(m, 0) = 1 + \text{R}(m-1, 1)&\text{pour }m>0\\
        \text{R}(m, n) =  \text{R}(m, n - 1) + 1 + \text{R}(m - 1, \text{Ack}(m, n - 1)) &\text{pour }m, n>0\\
    \end{array}
\right. %}
$$
</div>

{% endnote %}
{% details "preuve", "open" %}

Clair en utilisant la définition de la fonction :

- le cas $m=0$ est un cas terminal,
- le cas $m>0$ et $n=0$ fait une récursion puis calcule $\text{Ack}(m-1, 1)$,
- le cas $m, n>0$ doit commencer par calculer $\text{Ack}(m, n - 1)$ (il faut $\text{R}(m, n - 1)$ récursions) fait une recursion pour calculer $\text{Ack}(m - 1, \text{Ack}(m, n - 1))$ (il faut $\text{R}(m - 1, \text{Ack}(m, n - 1))$ récursions)
{% enddetails %}

Ce nombre peut facilement être majoré :

{% exercice %}
Montrez que pour tout $m, n > 0$, on a $R(m,n) \geq  R(m,n-1) + 1$ et en déduire que pour $m, n > 1$:

<div>
$$
R(m,n) \geq  \text{Ack}(m, n - 1)
$$
</div>
{% endexercice %}
{% details "Corrigé" %}

La première inégalité est évidente puisque pour $m, n > 0$ on a $\text{R}(m, n) =  \text{R}(m, n - 1) + 1 + \text{R}(m - 1, \text{Ack}(m, n - 1))$ et que $\text{R}(m - 1, \text{Ack}(m, n - 1)) \geq 0$.

Pour en déduire la seconde, il suffit de remarquer que l'on a aussi, pour $m, n > 0$, que $\text{R}(m, n) \geq \text{R}(m - 1, \text{Ack}(m, n - 1))$ et donc que pour $m, n > 1$ on a :

<div>
$$
$R(m,n) \geq  \text{R}(m-1, 0) + \text{Ack}(m, n - 1) \geq \text{Ack}(m, n - 1)
$$
</div>

{% enddetails %}

Il faut donc (plus que) de l'ordre de de la valeur de la fonction d'Ackermann récursions pour  la calculer, ce qui est astronomique !

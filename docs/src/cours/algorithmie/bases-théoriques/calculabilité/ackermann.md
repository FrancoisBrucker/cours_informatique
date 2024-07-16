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

## Définition

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

{% note "**Proposition**" %}
La fonction d'Ackermann est bien définie pour tout $m$ et $n$ entiers.
{% endnote %}
{% details "preuve", "open" %}
Pour chaque appel récursif de la fonction d'Ackermann, soit $m$, soit $n$ est strictement plus petit dans la fonction appelée que dans la fonction appelante. On arrivera donc toujours à $m = 0$ qui stoppera la récursion ou $n = 0$ qui fera baisser la valeur de $m$. Il n'y aura donc toujours qu'un nombre finie de récursion pour tout couple $(m, n)$.

{% enddetails %}

La fonction étant définie on peut écrire l'algorithme suivant, qui va bien fonctionner :

```text
Nom : Ack
Entrées :
    m, n : entiers
Programme :
    Si m = 0:
        rend n + 1
    Si n = 0:
        rend Ack(m-1, 1)
    Sinon:
        n' = Ack(m, n-1)
        rend Ack(m-1, n')
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

Au final on trouve $\text{Ack}(2, 1) = 5$. Toutes ces récursions pour ça.

La fonction d'Ackermann n'est pas primitive récursive, on va le voir, mais si on fixe son premier paramètre fixé, elle l'est :

{% note "**Proposition**" %}
La fonction $A_m(n) = \text{Ack}(m, n)$ est primitive récursive pour tout $n$.
{% endnote %}
{% details "preuve", "open" %}
Par récurrence sur $m$.

1. $A_0(n) = \text{Ack}(0, n) = n+1$
2. si $A_m(n)$ est primitive récursive, $A_{m+1}(n)$ l'est également puisqu'elle est définie par l'opération de récurrence :
   - $A_{m+1}(0) = A_{m}(1)$
   - $A_{m+1}(n+1) = A_{m}(A_{m+1}(n))$

{% enddetails %}

Retenez bien ce résultat qui peut paraître surprenant, ce n'est pas parce que $A_m(x)$ est primitive récursive pour tout $n$ que $\text{Ack}(m, n)$ l'est. Chaque $A_m(x)$ est construit différemment, on ne peut pas en déduire un schéma général pour construire $\text{Ack}(m, n)$. On retrouvera ce comportement étrange lorsque l'on cherchera à calculer des réels.

### Croissance

Donnons une valeur à la fonction d'Ackermann. On doit évaluation à D. Knuth qui pour cela a inventé une nouvelle opération mathématique, l'opération $x \uparrow y$ :

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
- ...

Ces nombres sont énormes ! Rien que les écrire va prendre du temps. Si l'on suppose que l'on peut écrire le chiffre `1` ou `0` en .1s, l'écriture en base 2 des nombres ci-dessus (ce sont tous des puissances de 2) prendra :

- .3s pour $2 \uparrow^{(0)} 4$
- .4s pour $2 \uparrow^{(1)} 4$
- 1.6s pour $2 \uparrow^{(2)} 4$
- $2^{65500}$ millénaires pour $2 \uparrow^{(3)} 4$

{% note "**À retenir**" %}
Ce n'est pas parce que l'on peut calculer quelque chose qu'on peut le faire en pratique, du moins si on est pas immortel.
{% endnote %}

Les nombres $2 \uparrow^{(m)} n$ vont être liés à la fonction d'Ackermann. Commençons donc par nous familiariser avec :

{% exercice %}
Montrez que pour tout $m\geq 0$ on a :

1. $2 \uparrow^{(m)} 1 = 2$
2. $2 \uparrow^{(m)} 2 = 4$
3. $2 \uparrow^{(m)} n > m + n$ pour $n \geq 3$
4. $2 \uparrow^{(m)} (n+1) \leq 2 \uparrow^{(m + 1)} (n)$ pour $n \geq 3$
{% endexercice %}
{% details "corrigé" %}

> TBD 1. et 2. en appliquant la formule
> TBD 3. par récurrence sur m et par croissance de la fonction.
> TBD 4. Par récurrence sur $n$. Pour $n=3$ on a : $2 \uparrow^{(k)} (3+1) = 2 \uparrow^{(k)} (2 \uparrow^{(k+1) 2}) = 2 \uparrow^{(k+1)} (3)$

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
{% details "preuve" %}
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

De plus l'exercice précédent nous permet d'écrire :

- $\text{Ack}(2, n) > 2n$
- $\text{Ack}(m, n) > m + n$
- $\text{Ack}(m, n+1) \leq \text{Ack}(m+1, n)$

Ces trois inégalités permettent d'en déduire les 2 inégalités fondamentales suivantes :

{% exercice %}
Pour tous entiers $(m_i)_{1\leq i \leq k}$ ($k\geq 2$), il existe un entier $m$ tel que :

1. $\text{Ack}(m_1, \text{Ack}(m_2, n)) \leq \text{Ack}(m, n)$ pour tout $n \geq 0 $
2. $\sum_i\text{Ack}(m_i, n) \leq \text{Ack}(m, n)$ pour tout $n\geq 0$
{% endexercice %}
{% details "corrigé" %}

Pour la première partie, si $n=0$ on a $\text{Ack}(m_1, \text{Ack}(m_2, 0)) = \text{Ack}(m_1, \text{Ack}(m_2-1, 1))$. On peut donc toujours se ramener au cas où $n>0$. De là, par croissance de la fonction d'Ackermann dans ses deux variables, on a : $\text{Ack}(m_1, \text{Ack}(m_2, n)) \leq \text{Ack}(\max(m_1, m_2), \text{Ack}(\max(m_1, m_2), n))$. En posant $m_0 = \max(m_1, m_2)$, on a pour $n\geq 0$:

<div>
$$
\text{Ack}(m_1, \text{Ack}(m_2, n+1))\leq  \text{Ack}(m_0, \text{Ack}(m_0, n+1))\leq  \text{Ack}(m_0, \text{Ack}(m_0+1, n)) = \text{Ack}(m_0+1, n+1)
$$
</div>

Pour la seconde partie, on a :

<div>
$$
\text{Ack}(m_1, n) + \text{Ack}(m_2, n) \leq 2\cdot \text{Ack}(\max(m_1, m_2), n) < \text{Ack}(2, \text{Ack}(\max(m_1, m_2), n)) \leq \text{Ack}(m, n)
$$
</div>

Comme $\sum_i\text{Ack}(m_i, n) = \text{Ack}(m_1, n) + \text{Ack}(m_2, n) + \sum_{i>2}\text{Ack}(m_i, n) \leq \text{Ack}(m, n) + \sum_{i>2}\text{Ack}(m_i, n) \leq \text{Ack}(m, n)$ une récurrence triviale permet de conclure.

{% enddetails %}

L'exercice précédent montre que la fonction d'Ackermann croit très vite en $m$ puisque toute somme ou composition de fonction d'Ackermann va être borné à un moment par une autre fonction d'Ackermann.

### La fonction d'Ackermann n'est pas primitive récursive

La preuve que la fonction d'Ackermann n'est pas récursive primitive est éclairante : on montre qu'elle croit trop vite pour être primitive récursive.

{% note "**Proposition**" %}
Pour toute fonction récursive primitive $f(x_1, \dots, x_n)$ il existe $K_f$ tel que pour tous $(x_1, \dots, x_n) \in \mathbb{R}^n$ :

<div>
$$
f(x_1, \dots, x_n) \leq \text{Ack}(K_f, \sum_{1\leq i \leq n}x_i)
$$
</div>

{% endnote %}
{% details "preuve", "open" %}

Comme l'ensemble des fonctions récursives primitives est l'ensemble minimum des fonctions contenant les fonctions primitives de base et stable par composition et récursion, il suffit de montrer que :

1. la propriété est vérifiée pour les fonctions primitives de base
2. la propriété est conservée par composition et récursion

La première partie de la preuve est claire puisque les fonctions zéros, projections et successeurs sont toutes plus petites que $\text{Ack}(0, \sum_{1\leq i \leq n}x_i) = \sum_{1\leq i \leq n}x_i + 1$

Pour la seconde partie, commençons par montrer que la propriété est stable par composition.

Soient $f: \mathbb{N}^n \to \mathbb{N}$ et $(g_i)_{1 \leq i \leq n}: \mathbb{N}^m \to \mathbb{N}$ des fonctions primitives récursives satisfaisant la propriété. On a alors :

<div>
$$
\begin{array}{rl}
    f \circ [g_1, \dots, g_n](x_1, \dots, x_m) \leq & \text{Ack}(M_f, \sum_{1\leq i \leq n} g_i(x_1, \dots, x_m))\\
    \leq & \text{Ack}(M_f, \sum_{1\leq i \leq n} \text{Ack}(M_{g_i}, \sum_{1\leq j \leq m} x_j))\\
    \leq & \text{Ack}(M_f, \text{Ack}(m, \sum_{1\leq j \leq m} x_j))\\
    \leq & \text{Ack}((m', \sum_{1\leq j \leq m} x_j))\\
\end{array}
$$
</div>

Et finissons par la récursion.

Soient $f: \mathbb{N}^n \to \mathbb{N}$ et $g: \mathbb{N}^{n+2} \to \mathbb{N}$ des fonctions primitives récursives satisfaisant la propriété. Il existe alors $m$ tel que $\text{Ack}(M_g,\text{Ack}(2,n)) \leq \text{Ack}(m,n)$ et on note $M_{\rho^n(f, g)} = \max(m, M_f, M_g) + 1$.

On a alors : $\rho^n(f, g)(0, x_1, \dots, x_n) \leq \text{Ack}(M_f, 0+\sum_{1\leq i \leq n}x_i) \leq \text{Ack}(M_{\rho^n(f, g)}, 0+\sum_{1\leq i \leq n}x_i)$

De là, en supposant que $\rho^n(f, g)(x, x_1, \dots, x_n) \leq \text{Ack}(M_{\rho^n(f, g)}, x+\sum_{1\leq i \leq n}x_i)$ on a :

<div>
$$
\begin{array}{rl}
    \rho^n(f, g)(x+1, x_1, \dots, x_n) = & g(x, \rho^n(f, g)(x, x_1, \dots, x_n), x_1, \dots, x_n)\\
    \leq & \text{Ack}(M_g, x+\sum_{1\leq i \leq n}x_i + \rho^n(f, g)(x, x_1, \dots, x_n))\\
    \leq & \text{Ack}(M_g, x+\sum_{1\leq i \leq n}x_i + \text{Ack}(M_{\rho^n(f, g)}, x+\sum_{1\leq i \leq n}x_i))\\
\end{array}
$$
</div>

Comme $ n\leq m+n < \text{Ack}(m, n)$ (on n'avait pas encore utilisé cette inégalité, il fallait bien un jour qu'elle serve) on a :

<div>
$$
\begin{array}{rl}
    \rho^n(f, g)(x+1, x_1, \dots, x_n) \leq & \text{Ack}(M_g, x+\sum_{1\leq i \leq n}x_i + \text{Ack}(M_{\rho^n(f, g)}, x+\sum_{1\leq i \leq n}x_i))\\
    \leq & \text{Ack}(M_g, 2\cdot \text{Ack}(M_{\rho^n(f, g)}, x+\sum_{1\leq i \leq n}x_i))\\
  \leq & \text{Ack}(m, \text{Ack}(M_{\rho^n(f, g)}, x+\sum_{1\leq i \leq n}x_i))\\
\leq & \text{Ack}(M_{\rho^n(f, g)}-1, \text{Ack}(M_{\rho^n(f, g)}, x+\sum_{1\leq i \leq n}x_i))\\
\leq & \text{Ack}(M_{\rho^n(f, g)}, x+\sum_{1\leq i \leq n}x_i +1)\\
\end{array}
$$
</div>
{% enddetails %}

La proposition précédente montre que toute fonction récursive primitive est majorée par une fonction d'Ackermann, ce qui va nous permettre de conclure la preuve :

{% note "**Proposition**" %}
La fonction d'Ackermann n'est pas récursive primitive.
{% endnote %}
{% details "preuve", "open" %}
Si la fonction d'Ackermann était primitive récursive, la fonction : $A(n) = \text{Ack}(n, n) = \text{Ack} \circ [\pi^1_1, \pi^1_1]$ l'est aussi.

Il existe alors $M_A$ tel que $A(n) \leq \text{Ack}(M_A, n)$ pour tout $n$. Ceci est impossible car pour $n = M_A + 1$ on aurait : $A(M_A + 1) \leq \text{Ack}(M_A, M_A + 1) \leq \text{Ack}(M_A + 1, M_A)$ mais comme $A(M_A + 1) = \text{Ack}(M_A + 1, M_A + 1)$ ceci impliquerait $A(M_A + 1) = \text{Ack}(M_A + 1, M_A + 1) \leq \text{Ack}(M_A + 1, M_A)$ ce qui contredit la stricte croissance de la fonction d'Ackermann.

{% enddetails %}

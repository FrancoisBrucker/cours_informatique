---
layout: layout/post.njk 
title:  "Penser l'algorithmie"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD chapeau
>
> TBD chapeau commençons par un cas particulier, correspondant à l'arithmétique de Peano et utilisé par Godel pour démontrer ses théorèmes d'incomplétude.

{% aller %}
[Fonctions récursives primitives](./récursive-primitive){.interne}
{% endaller %}

Nous avons vu que les fonctions primitives récursives étaient des fonctions calculable. Nous allons montrer ici qu'un modèle plus générale, les fonctions récursives, sont équivalentes au pseudo-code ! Ceci montre que l'algorithmie peut posséder de nombreuses formes, toutes équivalentes.

{% aller %}
[Fonctions récursives](./fonctions-récursives){.interne}
{% endaller %}

## Ackermann le retour

> TBD à refaire propre
> TBD Rappeler l'endroit ou est Ackermann dans le cours
> TBD en faire une partie à part.

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

### La fonction d'Ackermann n'est pas primitive récursive

> TBD à refaire.

Ces trois inégalités permettent d'en déduire les 2 inégalités fondamentales suivantes qui montre que la fonction s'emballe très vite calculer les valeurs précédentes d'Ackermann est négligeable par rapport aux valeurs plus grandes :

{% exercice %}
Montrez que pour tous entiers $(m_i)_{1\leq i \leq k}$ ($k\geq 2$), il existe un entier $m$ tel que :

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

Ce type de récurrence est nommée [récurrence structurelle](https://fr.wikipedia.org/wiki/Induction_structurelle)

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

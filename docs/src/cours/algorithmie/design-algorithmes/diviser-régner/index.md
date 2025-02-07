---
layout: layout/post.njk
title: Diviser pour régner

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD : mettre le master theorem ici.
> 
> TBD. Dire qu'on a vue ça dans les tris.
> TBD Reprendre le master theorem et le démontrer ici.
> TBD autres exemples
> TBD transformée de Fourier
> TBD exo <https://wkerl.me/#teaching>
> TBD médiane en temps linéaire en moyenne. en vrai.
> <https://wkerl.me/cours/ouv_td.pdf>
> <https://www.normalesup.org/~simonet/teaching/caml-prepa/tp-caml-2001-02.pdf> et <https://fr.wikipedia.org/wiki/Recherche_des_deux_points_les_plus_rapproch%C3%A9s>



Son énoncé nous permet de déterminer aisément la complexité de nombreux algorithmes récursifs :

<span id="master-theorem"></span>
{% note "**Forme O [du master theorem](https://fr.wikipedia.org/wiki/Master_theorem)**" %}

Une complexité de la forme :

<div>
$$
C(n) = a \cdot C(\frac{n}{b}) + \mathcal{O}(n^d)
$$
</div>

Est en :

- $C(n)  = \mathcal{O}(n^d \cdot \ln(n))$ si $a=b^d$ (équivalent à $d = \log_b(a)$)
- $C(n)  = \mathcal{O}(n^{\log_b(a)})$ si $a>b^d$
- $C(n)  = \mathcal{O}(n^d)$ si si $a<b^d$

{% endnote %}
{% details "preuve", "open" %}
Comme $C(n) = a \cdot C(\frac{n}{b}) + \mathcal{O}(n^d)$, il existe $N_0$ tel que pour tout $n \geq N_0$, on a :

<div>
$$
C(n) \leq a \cdot C(\frac{n}{b}) + n^d
$$
</div>

On en conclut que si $C'(n) = a \cdot C'(\frac{n}{b}) + n^d$ alors $C(n) \leq C'(n)$ pour tout $n$ et donc si $C'(n)$ est en $\mathcal{O}(g(n))$, alors $C(n)$ le sera aussi.

<div>
$$
\begin{array}{lcl}
C'(n) &=&a \cdot C'(\frac{n}{b}) + n^d \\
&=& a\cdot (a \cdot C'(\frac{n}{b^2}) + (\frac{n}{b})^d) + n^d\\
&=& a^2 \cdot C'(\frac{n}{b^2}) + n^d \cdot (1 + \frac{a}{b^d})\\
&=& a^2 \cdot (a \cdot C'(\frac{n}{b^3}) + (\frac{n}{b^2})^d) + n^d \cdot (1 + \frac{a}{b^d})\\
&=& a^3 \cdot C'(\frac{n}{b^3}) + n^d \cdot (1 + \frac{a}{b^d} + (\frac{a}{b^d})^2)\\
&=& \dots \\
&=& a^{\log_b(n)}C'(1) + n^d \cdot (\sum_{i=0}^{\log_b(n)}(\frac{a}{b^d})^i)\\
\end{array}
$$
</div>

Comme $a^{\log_b(n)} = \exp(\ln(a) \cdot \frac{\ln(n)}{\ln(b)} ) = \exp(\ln(n) \cdot \frac{\ln(a)}{\ln(b)} ) = n^{\log_b(a)}$ on en conclut, en posant $C'(1) = K$, que :

<div>
$$
C'(n) = K \cdot n^{\log_b(a)} + n^d \cdot \sum_{i=0}^{\log_b(n)}(\frac{a}{b^d})^i
$$
</div>

Il y a alors plusieurs cas. Commençons par étudier le cas où $\frac{a}{b^d} = 1$ (équivalent à $d = \log_b(a)$). Dans ce cas, on a :

<div>
$$
C'(n) = K \cdot n^d + n^d \cdot \sum_{i=0}^{\log_b(n)}1 = n^d(\log_b(n) + K) = \mathcal{O}(n^d \cdot \ln(n))
$$
</div>

Si $\frac{a}{b^d} \neq 1$, on peut utiliser le fait que $\sum_{i=0}^kx^k = \frac{x^{k+1} -1}{x-1}$ (cette formule  se démontre aisément par récurrence  sur $k$ et est super utile dans plein de calculs de complexité, il est bon de la connaître) pour obtenir :

<div>
$$
\begin{array}{lcl}
C'(n) &=& K \cdot n^{\log_b(a)} + n^d \cdot \frac{(\frac{a}{b^d})^{\log_b(n) +1} -1}{\frac{a}{b^d}-1}\\
& = & K \cdot n^{\log_b(a)} + n^d \cdot \frac{\frac{a}{b^d}\cdot\frac{n^{\log_b(a)}}{n^d} -1}{\frac{a}{b^d}-1}\\
& =& K \cdot n^{\log_b(a)} + \frac{\frac{a}{b^d}\cdot n^{\log_b(a)} - n^d}{\frac{a}{b^d}-1} \\
& = & (K + \frac{\frac{a}{b^d}}{\frac{a}{b^d} - 1}) \cdot n^{\log_b(a)} - \frac{1}{\frac{a}{b^d} - 1} \cdot n^d
\end{array}
$$
</div>

On en déduit facilement que :

- $\frac{a}{b^d} < 1$ (équivalent à $\log_b(a) < d$) implique $C'(n) = \mathcal{O}(n^d)$
- $\frac{a}{b^d} > 1$ (équivalent à $\log_b(a) > d$) implique $C'(n) = \mathcal{O}(n^{\log_b(a)})$

{% enddetails %}
{% info %}
Le master theorem est la raison pour laquelle vous verrez parfois des complexités avec des exposants non entiers
{% endinfo %}
Dans le cas du tri fusion on a $a = 2$, $b = 2$  et $d = 1$ donc $a=b^d$ :

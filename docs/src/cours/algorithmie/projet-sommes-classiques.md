---
layout: layout/post.njk 
title:  "Calcul de sommes classiques"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Lors de calculs de complexité, on va de nombreuses fois avoir les mêmes sommes à estimer, voir à calculer.

Cette série d'exercice va vous montrer les plus classiques et leur usage dans les calculs de complexité. On aura presque jamais besoin de les calculer explicitement, seul les équivalence en $\Theta$ ou en $\mathcal{O}$ vont nous intéresser.

{% lien %}
[Séries](https://fr.wikipedia.org/wiki/S%C3%A9rie_(math%C3%A9matiques))
{% endlien %}

## Séries des premiers entiers

Classiques et se démontrent aisément par récurrence (mais faite tout de même les calculs pour vous en rendre compte). Montrez que :

{% exercice %}
<div>
$$
\sum_{i=0}^{n}i = \frac{n(n+1)}{2} = \Theta(n^2)
$$
</div>
{% endexercice %}
{% exercice %}
<div>
$$
\sum_{i=0}^{n}i^2 = \frac{n(n+1/2)(n+1)}{3}=\frac{n(n+1)(2n+1)}{6}= \Theta(n^3)
$$
</div>
{% endexercice %}

{% exercice %}
<div>
$$
\sum_{i=0}^{n}i^3 = (\sum_{i=0}^{n}i)^2 = \frac{n^2(n+1)^2}{4} = \Theta(n^4)
$$
</div>
{% endexercice %}

Et pour finir :

{% exercice %}
<div>
$$
\sum_{i=0}^{n}i^k = \Theta(n^{k+1})
$$
</div>
{% endexercice %}
{% details "corrigé" %}

Par récurrence. On suppose $\sum_{i=0}^{n}i^{k-1} = \Theta(n^{k}) = \Omega(n^{k})$.

Puis :

- $\sum_{i=0}^{n}i^k\leq n \cdot \sum_{i=0}^{n}i^{k-1} = n \mathcal{O}(n^k) = \mathcal{O}(n^{k+1})$
- $\sum_{i=0}^{n}i^{k} \geq \sum_{i=n/2}^{n}i^k \geq \frac{n}{2}\sum_{i=n/2}^{n}i^{k-1} = \frac{n}{2}\sum_{i=0}^{n/2}(i+n/2)^{k-1} \geq \frac{n}{2} \cdot \sum_{i=0}^{n/2}(i)^{k-1} = \frac{n}{2}\Omega((n/2)^k) = \Omega(n^{k+1})$

{% enddetails %}

## Séries géométriques

On considère la série suivante :

Montrez que :

{% exercice %}
<div>
$$
S_n = \sum_{i=0}^{n}r^i = \frac{1-r^{n+1}}{1-r}
$$
</div>
Si $r \neq 1$.
{% endexercice %}
{% details "corrigé" %}

Trivial par récurrence.

{% enddetails %}

En déduire que :

{% exercice %}
<div>
$$
S_n = \begin{cases}
\mathcal{O}(1) \text{ si } |r| < 1\\
\Theta(r^n) \text{ si } |r| > 1\\
\end{cases}
$$
</div>
{% endexercice %}

En complexité c'est souvent avec des puissance de 2 que l'on va jouer. Por le coup, il est utile de connaître les valeurs des sommes car elles sont souvent des calculs intermédiaires :

{% exercice %}
Montrez que :

<div>
$$
\sum_{i=0}^{n}2^i = 2^{n+1} - 1
$$
</div>

et que :

<div>
$$
\lim_{n\to +\infty} \sum_{i=0}^{n}\frac{1}{2^i} = 2
$$
</div>

{% endexercice %}
{% details "corrigé" %}

La première égalité est uniquement une application numérique et la seconde résulte de $\frac{1}{2^n} \to_{+\infty} 0$.

{% enddetails %}
{% info %}
La seconde série a [une interprétation géométrique](https://fr.wikipedia.org/wiki/1/2_%2B_1/4_%2B_1/8_%2B_1/16_%2B_%E2%8B%AF)
{% endinfo %}

Une variation classique de la série géométrique, vue par exemple dans le calcul du tri rapide pour $r=2$ est :

<div>
$$
S'_n = \sum_{i=1}^{n}i\cdot r^i
$$
</div>

{% exercice %}
Montrez que :

<div>
$$
S'_n = \sum_{i=1}^{n}i\cdot r^i = \frac{r^{n+1}(n(r-1) - 1) + r}{(1-r)^2}
$$
</div>

{% endexercice %}
{% info %}
Vous pourrez utiliser le polynôme $P(x) = \sum_{i=1}^nx^i$ et le dériver.
{% endinfo %}
{% details "corrigé" %}

On a : $S'_n = rP'(r)$ et donc e n utilisant la formule de l'exercice précédent :

<div>
$$
\begin{array}{lcl}
S'_n &=& r\cdot \frac{-(n+1)r^n(1-r)+(1-r^{n+1})}{(1-r)^2}\\
&=& r\cdot \frac{r^{n}((n+1)(r-1) -r^{n+1} + 1) + r}{(1-r)^2}\\
&=& r\cdot \frac{r^{n}((n+1)(r-1)-r) + 1}{(1-r)^2}\\
&=& \frac{r^{n+1}(n(r-1)-1) + r}{(1-r)^2}\\
\end{array}
$$
</div>

{% enddetails %}

En déduire que :

{% exercice %}
<div>
$$
S'_n = \begin{cases}
\mathcal{O}(1) \text{ si } |r| < 1\\
\Theta(r^n) \text{ si } |r| > 1\\
\end{cases}
$$
</div>
{% endexercice %}

Et pour le cas souvent intéressant en complexité :

{% exercice %}
Montrez que :

<div>
$$
\sum_{i=0}^{n}i2^i = (n-1)2^{n+1} + 2
$$
</div>

et que :

<div>
$$
\lim_{n\to +\infty} \sum_{i=0}^{n}\frac{i}{2^i} = 2
$$
</div>

{% endexercice %}
{% info %}
Avez vous remarqué que :

<div>
$$
\lim_{n\to +\infty} \sum_{i=0}^{n}\frac{1}{2^i} = \lim_{n\to +\infty} \sum_{i=0}^{n}\frac{i}{2^i} = 2
$$
</div>

Surprenant, non ?
{% endinfo %}

## Série harmonique

On définie [la série harmonique](https://fr.wikipedia.org/wiki/S%C3%A9rie_harmonique) comme :

<div>
$$
H(n) = \sum_{i=1}^{n}\frac{1}{i}
$$
</div>

{% exercice %}

Montrez que $H(2^n) \geq 1 + \frac{n}{2}$
{% endexercice %}
{% details "corrigé" %}

<div>
$$
\begin{array}{lcl}
H(2^{n+1}) &=& H(2^{n}) + \sum_{i=2^n+1}^{2^{n+1}}\frac{1}{i}\\
&=& H(2^{n}) + \sum_{i=1}^{2^{n}}\frac{1}{2^n+i} = H(2^{n}) + \frac{1}{2^n}\sum_{i=1}^{2^{n}}\frac{1}{1 + \frac{i}{2^n}} \\
&\geq& H(2^{n}) + \frac{1}{2^n}\sum_{i=1}^{2^{n}}\frac{1}{2}\\
&\geq& H(2^{n}) + \frac{1}{2}
\end{array}
$$
</div>

Et on conclut par une récurrence (devenue) triviale.

{% enddetails %}

{% exercice %}

En déduire que $H(n)$ diverge lorsque $n$ tend vers $+\infty$.

{% endexercice %}
{% details "corrigé" %}

Si $H(n)$ converge, alors toute suite extraite également. Cela n'est donc pas possible puisque l'exercice précédent montre que $H(2^n)$ diverge en $+\infty$.

{% enddetails %}

Si la série harmonique arrive dans le calcul des complexités c'est que l'on cherche à montrer que cette dernière va se comporter comme une fonction logarithmique (ou plus généralement [polylogarithmique](https://fr.wikipedia.org/wiki/Polylogarithmique)).

Montrons le en utilisant le fait que comme $f(x) = \frac{1}{x}$ est une fonction décroissante sur $\mathbb{R}^+$ on a pour tout entier $i> 1$ :

<div>
$$
\frac{1}{i} \leq \int_{i-1}^{i}\frac{1}{x}dx
$$
</div>

Et a pour tout entier $i> 0$ :
<div>
$$
\int_{i}^{i+1}\frac{1}{x}dx \leq \frac{1}{i}
$$
</div>

En déduire pour tout $n> 0$ :

{% exercice %}

<div>
$$
\ln(n) \leq H(n) \leq \ln(n) + 1
$$
</div>

{% endexercice %}
{% details "corrigé" %}

L'inégalité de droite est claire en sommant de $i=2$ à $i=n$.

Pour l'inégalité de gauche, la première inégalité donne en sommant  de $i=1$ à $i=n$ : $\ln(n+1)  \leq H(n)$ et on conclut puisque $\ln$ est une fonction croissante.

{% enddetails %}

Ce qui doit amener à :

{% exercice %}

<div>
$$
H(n) = \Theta(\ln(n))
$$
</div>

{% endexercice %}
{% details "corrigé" %}

L'encadrement de l'exercice précédent montre que $H(n) / \ln(n) \to_{+\infty} 1$ [les deux fonctions sont donc équivalentes](https://fr.wikipedia.org/wiki/%C3%89quivalent) en $+\infty$ (ce qui est plus fort que ce qu'on demande)
{% enddetails %}

## Problème de Bâle et variante

{% lien %}
[Problème de Bâle](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_B%C3%A2le)
{% endlien %}

La somme suivante à un nom car le calcul exact de sa limite elle a résisté pendant plusieurs années avant qu'Euler n'en vienne à bout. Son résultat est diablement surprenant :

<div>
$$
\lim_{n \to {+\infty}}\sum_{i=1}^{n}\frac{1}{i^2} = \frac{\pi^2}{6}
$$
</div>

{% lien %}

[5 preuves différentes du résultat](https://www.youtube.com/watch?v=1hJji-zgS00) et les détails dans [voyage en Analystan](https://math.univ-lyon1.fr/irem/IMG/pdf/analysie.pdf)

{% endlien %}

On ne va pas ici démontrer la valeur exacte de la limite (qui a plus sa place dans un cours d'analyse), juste qu'elle converge et que c'est donc un $\mathcal{O}(1)$.

On va utiliser [la comparaison série-intégrale](https://fr.wikipedia.org/wiki/Comparaison_s%C3%A9rie-int%C3%A9grale) qu'il est utile d'avoir dans son arsenal (on verra en fin d'exercice un autre moyen de faire, avec une petite astuce bien sympathique) :

{% exercice %}
Montrez que  :

<div>
$$
\int_{1}^{n+1}\frac{1}{x^2}dx \leq \sum_{i=1}^n\frac{1}{i^2} \leq 1 + \int_{1}^{n}\frac{1}{x^2}dx
$$
</div>

{% endexercice %}
{% details "corrigé" %}

La preuve vient directement du fait que la fonction $f(x) = \frac{1}{x^2}$ est décroissante sur $[1, +\infty]$ et donc pour tout $i>1$ :

<div>
$$
\int_{i}^{i+1}\frac{1}{x^2}dx \leq \frac{1}{i^2} \leq \int_{i-1}^{i}\frac{1}{x^2}dx
$$
</div>

Ce qui emmène à :

<div>
$$
\int_{2}^{n+1}\frac{1}{x^2}dx \leq \sum_{i=2}^n\frac{1}{i^2} \leq \int_{1}^{n}\frac{1}{x^2}dx
$$
</div>

Et donc :

<div>
$$
\int_{1}^{n+1}\frac{1}{x^2}dx \leq \sum_{i=1}^n\frac{1}{i^2} \leq 1 + \int_{1}^{n}\frac{1}{x^2}dx
$$
</div>

{% enddetails %}
{% exercice %}
En déduire que la série est convergente et que :

<div>
$$
1 \leq lim_{n\to +\infty} \sum_{i=1}^n\frac{1}{i^2} \leq 2
$$
</div>

{% endexercice %}
{% details "corrigé" %}
Vient directement de l'encadrement précédent et que :

<div>
$$
\int_1^{+\infty}\frac{1}{x^2}dx = \left [-\frac{1}{x}\right ]_1^{+\infty} =1
$$
</div>

Comme la série est croissante et bornée, elle converge.

{% enddetails %}
{% exercice %}
Et donc que :

<div>
$$
\sum_{i=1}^n\frac{1}{i^2} = \mathcal{O}(1)
$$
</div>
{% endexercice %}
{% details "corrigé" %}

Clair puisque la série est croissante et possède une limite.
{% enddetails %}

Contrairement au problème de Bâle, cette variante est toute simple :

{% exercice %}
Montrez que :

<div>
$$
\sum_{i=1}^n\frac{1}{i(i+1)} = \frac{n}{n+1} = \mathcal{O}(1)
$$
</div>
{% endexercice %}
{% details "corrigé" %}

Clair par récurrence :

<div>
$$
\sum_{i=1}^{n+1}\frac{1}{i(i+1)} = \frac{n}{n+1} + \frac{1}{(n+1)(n+2)} = \frac{n(n+2) + 1}{(n+1)(n+2)} = \frac{(n+1)^2}{(n+1)(n+2)}
$$
</div>

{% enddetails %}

Remarquez qu'on aurait aussi pu utiliser l'encadrement suivant pour prouver la convergence de la série initiale :

<div>
$$
\sum_{i=1}^{n}\frac{1}{i(i+1)} \leq \sum_{i=1}^{n}\frac{1}{i^2} \leq 1 + \sum_{i=2}^{n}\frac{1}{i(i-1)}
$$
</div>

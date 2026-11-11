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

Cette série d'exercice va vous montrer les plus classiques (on en a d'ailleurs déjà vu certaines) et leur usage dans les calculs de complexité. On aura presque jamais besoin de les calculer explicitement, seul les équivalence en $\Theta$ ou en $\mathcal{O}$ vont nous intéresser.

{% lien %}
[Séries](https://fr.wikipedia.org/wiki/S%C3%A9rie_(math%C3%A9matiques)){.externe}
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

<div id="problème-r^i"></div>
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

<div id="problème-1/2^i"></div>
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
La seconde série a [une interprétation géométrique](https://fr.wikipedia.org/wiki/1/2_%2B_1/4_%2B_1/8_%2B_1/16_%2B_%E2%8B%AF){.externe}
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
S'_n = \sum_{i=1}^{n}i\cdot r^i = \frac{r^{n+1}}{n+2} \cdot \frac{r + (1+1/n)/(1+2/n)}{(1-r)^2} + \frac{r}{(1-r)^2}
$$
</div>

{% endexercice %}
{% info %}
Vous pourrez utiliser le polynôme $P(x) = \sum_{i=1}^nx^i$ et le dériver.
{% endinfo %}
{% details "corrigé" %}

On a : $S'_n = rP'(r)$ et donc e n utilisant [la formule explicite de $P(x) = \frac{1-x^{n+1}}{1-x}$](./#problème-r^i), on a :

<div>
$$
\begin{array}{lcl}
P'(x) &=& \frac{-(n+1)r^n(1-r)-(1-r^{n+1})}{(1-r)^2}\\
&=& \frac{(n+2)\cdot r^{n+1} + (n+1)\cdot r^{n} + 1}{(1-r)^2}\\
\end{array}
$$
</div>

Et donc :
 
<div>
$$
\begin{array}{lcl}
S'_n &=& r\cdot \frac{(n+2)\cdot r^{n+1} + (n+1)\cdot r^{n} + 1}{(1-r)^2}\\
\end{array}
$$
</div>

Ce qui mène au résultat attendu.

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
{% details "corrigé" %}

Clair car $\frac{r^{n+1}}{n+2}$ tend vers 0 lorsque $n$ tend vers l'infini si $r < 1$

{% enddetails %}
Et pour le cas souvent intéressant en complexité :

<div id="problème-i/2^i"></div>

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

On définie [la série harmonique](https://fr.wikipedia.org/wiki/S%C3%A9rie_harmonique){.externe} comme :

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

Si la série harmonique arrive dans le calcul des complexités c'est que l'on cherche à montrer que cette dernière va se comporter comme une fonction logarithmique (ou plus généralement [polylogarithmique](https://fr.wikipedia.org/wiki/Polylogarithmique){.externe}).


[On a déjà utilisé ce résultat](../../2-complexités/projet-calcul-max-min-moy/#Hn-équivalent). On le remet ici pour référence.

<div id="Hn-équivalent"></div>

{% note "**Proposition**" %}
<div>
$$
\ln(n + 1) \leq H(n) \leq \ln(n) + 1
$$
</div>

{% endnote %}
{% details "preuve", "open"%}

Soit $f(x) = \ln(1+x) - x$ définie sur $]-1, +\infty[$. Comme $f'(x) = \frac{1}{1+x} -1 = \frac{-x}{1+x}$, on a que $f$ atteint son minimum en 0 : $f(x) \geq f(0) = 0$ pour tout $x$ de $]-1, +\infty[$ : $x \geq \ln(1+x)$ sur $]-1, +\infty[$.

De là pour tout entier $i > 1$ : 

- $-\frac{1}{i} \geq \ln(1-\frac{1}{i}) = \ln(i-1) - \ln(i)$
- $\frac{1}{i} \geq \ln(1+\frac{1}{i}) = \ln(i+1) - \ln(i)$

Ce qui donne l'encadrement pour $i > 1$ : 

<div>
$$
\ln(i+1) - \ln(i) \leq \frac{1}{i} \leq \ln(i) - \ln(i-1)
$$
</div>

En sommant le tout on obtient une série télescopique :

<div>
$$
\begin{array}{c}
\sum\limits_{2\leq i \leq n} (\ln(i+1) - \ln(i)) \leq \sum\limits_{2\leq i \leq n}\frac{1}{i} \leq \sum\limits_{2\leq i \leq n} (\ln(i) - \ln(i-1))
\end{array}
$$
</div>

Qui se simplifie en :
<div>
$$
\begin{array}{c}
\ln(n+1) - \ln(2) \leq \sum\limits_{2\leq i \leq n}\frac{1}{i} \leq \ln(n) - \ln(1)
\end{array}
$$
</div>

On en déduit donc l'encadrement :

<div>
$$
\begin{array}{c}
\ln(n+1) \leq \sum\limits_{i=1}^n\frac{1}{i} \leq \ln(n) + 1
\end{array}
$$
</div>

{% enddetails %}

Ce qui amène directement à :

{% note "**Corollaire**" %}
<div>
$$
\sum\limits_{i=1}^{n} \frac{1}{i} \underset{+\infty}{\sim} \ln(n)
$$
</div>

{% endnote %}

Et à ça :


{% note "**Corollaire**" %}

<div>
$$
H(n) = \Theta(\ln(n))
$$
</div>

{% endnote %}

## <span id="problème-Bâle"></span>Problème de Bâle

<!-- 

> TBD <https://www.youtube.com/watch?v=CC2DG391HmA>{.externe} en Anglais avec une façon rigolote de dire Bernouilli, mais c'est bien fait.

> TBD une démonstration <https://www.youtube.com/watch?v=JZiDuryIMQE>{.externe}
 -->


{% lien %}
[Problème de Bâle](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_B%C3%A2le){.externe}
{% endlien %}

La somme suivante à un nom car le calcul exact de sa limite elle a résisté pendant plusieurs années avant qu'Euler n'en vienne à bout. Son résultat est diablement surprenant :

<div>
$$
\lim\limits_{n \to {+\infty}}\sum_{i=1}^{n}\frac{1}{i^2} = \frac{\pi^2}{6}
$$
</div>

### Utilisation en algorithmie

On ne va pas ici démontrer la valeur exacte de la limite (regardez le premier lien si vous en voulez une), juste qu'elle converge et que c'est donc un $\mathcal{O}(1)$. On va pour cela utiliser une série proche mais admirablement facile à calculer.

{% exercice %}
Montrez que :

<div>
$$
\sum_{i=1}^n\frac{1}{i(i+1)} = \frac{n}{n+1}
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
{% exercice %}
En déduire que pour tout $n$ :

<div>
$$
1 \leq \sum_{i=1}^n\frac{1}{i^2} \leq 2
$$
</div>
{% endexercice %}

{% details "corrigé" %}

Pour $i> 1$ on a clairement $\frac{1}{i(i+1)} \leq \frac{1}{i^2} \leq \frac{1}{i(i-1)}$, et donc en sommant l'indice on obtient :
<div>
$$
\sum_{i=1}^{n}\frac{1}{i(i+1)} \leq \sum_{i=1}^{n}\frac{1}{i^2} \leq 1 + \sum_{i=2}^{n}\frac{1}{i(i-1)}
$$
</div>

Et l'encadrement final vient du fait que :

<div>
$$
\lim_{n\to +\infty}\frac{n}{n+1} = \lim_{n\to +\infty}\frac{n+1}{n+1} - \frac{1}{(n+1)} = 1
$$
</div>

{% enddetails %}

{% exercice %}
En déduire que :

<div>
$$
\sum_{i=1}^n\frac{1}{i^2} = \mathcal{O}(1)
$$
</div>

{% endexercice %}
{% details "corrigé" %}
La série est croissante et bornée, elle converge.
{% enddetails %}

### Preuve

{% lien %}

[une preuve de Ioannis Papadimitriou](https://www.math.uwaterloo.ca/~krdavids/M148/Papadimitriou.pdf)

{% endlien %}

On va donner la preuve du lien ci-dessus, que l'on doit à Papadimitriou (1973). Son intérêt est qu'elle n'a pas besoin d'intégrale ou de méthodes d'analyse, juste un petit polynôme et l'utilisation de fonction trigonométriques simple.

{% note "proposition" %}

Pour tout $0 < x < \frac{\pi}{2}$ on a :
<div>
$$
\sin(x) < x < \tan(x)
$$
</div>
{% endnote %}
{% details "preuve","open" %}

Soient les deux fonctions définies sur $[0, \frac{\pi}{2}[$ :

- $f(x) =  x- \sin(x)$,
- $g(x) =  \tan(x) - x$.

On a :

- $f'(x) =  1 - cos(x) > 0$ sur $]0, \frac{\pi}{2}[$ donc $f(x) > f(0) = 0$ sur $]0, \frac{\pi}{2}[$
- $g'(x) =  (1+\tan^2(x)) -1 = \tan^2(x) > 0$ sur $]0, \frac{\pi}{2}[$ $g(x) > g(0)$ = 0 sur $]0, \frac{\pi}{2}[$.

On en conclut que sur $]0, \frac{\pi}{2}[$ :

- $\sin(x) < x$
- $x < \tan(x)$

{% enddetails %}

On a alors sur $]0, \frac{\pi}{2}[$ :

<div>
$$
\begin{align*}
\sin(x) < x < \tan(x)\\
\frac{1}{\sin(x)} > \frac{1}{x} > \frac{1}{\tan(x)}\\
\frac{1}{\sin^2(x)} > \frac{1}{x^2} > \frac{1}{\tan^2(x)}\\
\end{align*}
$$
</div>

Comme $1 + \cot^2(x) = \frac{1}{\sin^2(x)}$ ($\cot(x) = \frac{1}{tan(x)}$) sur $]0, \frac{\pi}{2}[$, l'encadrement précédent s'écrit :

<div>
$$
\begin{align*}
\cot^2(x) < \frac{1}{x^2} < 1 + \cot^2(x)\\
\end{align*}
$$
</div>

En posant $x_k = \frac{k\pi}{2n+1}$ pour $1\leq k \leq n$, on a $0< x_k <\frac{\pi}{2}$ et on l'injecter dans l'équation précédente :

<div>
$$
\begin{align*}
\sum\limits_{k=1}^n\cot^2(x_k) < \frac{(2n+1)^2}{\pi^2}\sum\limits_{k=1}^n\frac{1}{k^2} < m + \sum\limits_{k=1}^n\cot^2(x_k)\\
\end{align*}
$$
</div>

On utilise alors le fait que :

{% note "proposition" %}

<div>
$$
\sum\limits_{k=1}^n\cot^2(\frac{k\pi}{2n+1}) = \frac{n(2n-1)}{3}
$$
</div>
{% endnote %}
{% details "preuve","open" %}

<div>
$$
\begin{array}{lcl}
\cos(m\theta) + i\sin(m\theta) 
&=& (e^{im\theta}) \\
&=& (e^{i\theta})^m \\
&=& (\cos(\theta) + i\sin(\theta))^m \\
&=& \sin^m(\theta)\cdot (\cot(\theta) + i)^m\\
&=& \sin^m(\theta)\cdot (\sum\limits_{k=0}^m(\binom{m}{k}i^k\cot^{m-k}(\theta))
\end{array}{lcl}
$$
</div>

On pose maintenant $m = 2n + 1$ :

<div>
$$
\sin((2n+1)\theta) = \sin^{2n+1}(\theta)\cdot (\sum\limits_{k=0}^m(\binom{2n+1}{k}i^k\cot^{2n+1-k}(\theta))
$$
</div>

Et on n'en garde que la partie imaginaire pour obtenir :

<div>
$$
\sin((2n+1)\theta) = \sin(\theta)^{2n+1} \cdot (\sum\limits_{k=0}^{n}(\binom{2n+1}{2k + 1}(-1)^k\cot^{k}(\theta))
$$
</div>

Puisque $\sin(\theta) \neq 0$ pour $0 < \theta < \frac{\pi}{2}$, l'équation précédente prouve que les $n$ racines du polynôme $P(x) = \sum\limits_{i=0}^{n}(\binom{2n+1}{2i + 1}(-1)^ix^{i})$ sont les $n$ valeurs $\cot^2(x_k)$ avec $x_k = \frac{k\pi}{2n + 1}$, $1\leq k \leq n$.

La somme des $n$ racines $r_i$ d'un polynôme $\sum\limits_{k=0}^{n}a_kx^k$ valant $-\frac{a_{n-1}}{a_n}$ (puisque $\sum\limits_{k=0}^{n}a_kz^k = \prod\limits_{k=1}^{n}(x-r_i)$) on en déduit la relation demandée :

<div>
$$
\sum\limits_{k=1}^{n}\cot^2(x_k) = \frac{n(2n -1)}{3}
$$
</div>

{% enddetails %}

Pour obtenir :

<div>
$$
\begin{align*}
\frac{n(2n-1)}{3} < \frac{(2n+1)^2}{\pi^2}\sum\limits_{k=1}^n\frac{1}{k^2} < n + \frac{n(2n-1)}{3}\\
\frac{\pi^2}{6}\frac{2n(2n-1)}{(2n+1)^2} < \sum\limits_{k=1}^n\frac{1}{k^2} < \frac{n}{(2n+1)^2} + \frac{\pi^2}{6}\frac{2n(2n-1)}{(2n+1)^2}\\
\end{align*}
$$
</div>

Comme : $\lim\limits_{n\to +\infty} \frac{2n(2n-1)}{(2n+1)^2} = 1$ et $\lim\limits_{n\to +\infty} \frac{n}{(2n+1)^2} = 0$ on a bien le résultat attendu :

{% note "Théorème" %}
<div>
$$
\lim\limits_{n\to +\infty} \frac{1}{k^2} = \frac{\pi^2}{6}
$$
</div>

{% endnote %}
---
layout: layout/post.njk 
title:  "Calcul d'équations classiques"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Lors de calculs récursif de complexité, on va de nombreuses fois avoir les mêmes équations à résoudre. Cette série d'exercices va vous montrer les plus classiques et leur usage dans les calculs de complexité. Quelques équations de récurrences sont à connaître car elles donnent de complexités très différentes.

{% exercice %}
Que vaut $C(n)$ si :

<div>
$$
\begin{cases}
C(n) = \mathcal{O}(1) + C(n - K)\\
C(1) = \mathcal{O}(1)
\end{cases}
$$
</div>

{% endexercice %}
{% details "corrigé" %}

On réitère l'équation de récursion jusqu'à trouver une suite générale avec un paramètre décroissant pour le terme de droite :
<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(1) + C(n - K)\\
     &=& \mathcal{O}(1) + \mathcal{O}(1) + C(n - 2\cdot K)\\
     &=& \mathcal{O}(1) + \mathcal{O}(1) + (\mathcal{O}(1) + C(n - 2\cdot K - K))\\
     &=& 3\cdot \mathcal{O}(1) + C(n - 3\cdot K)\\
     &=& \dots\\
     &=& p\cdot \mathcal{O}(1) + C(n - p\cdot K)\\
     &=& \mathcal{O}(p) + C(n - p\cdot K)\\
\end{array}
$$
</div>

La formule ci-dessus est vraie **quelque soit** $p$. On peut donc prendre la valeur qui nous arrange. Comme on connaît $C(1)$, si on prend $p$ tel que $n - p\cdot K = 1$, c'est à dire $p = \frac{n-1}{K}$, on a plus d'inconnue à droite de l'égalité :

<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(\frac{n-1}{K}) + C(1)\\
     &=& \mathcal{O}(n)
\end{array}
$$
</div>

{% enddetails %}
{% exercice %}
Que vaut $C(n)$ si :

<div>
$$
\begin{cases}
C(n) = \mathcal{O}(n) + C(n - K)\\
C(1) = \mathcal{O}(1)
\end{cases}
$$
</div>

{% endexercice %}
{% details "corrigé" %}

On fait de même que pour l'exercice précédent, on cherche une suite générale avec un paramètre décroissant pour le terme de droite :

<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(n) + C(n - K)\\
     &=& \mathcal{O}(n) + \mathcal{O}(n - K) + C(n - 2\cdot K)\\
     &=& \mathcal{O}(n) + \mathcal{O}(n - K) + (\mathcal{O}(n - 2\cdot K) + \mathcal{O}(n - 2\cdot K - K))\\
     &=& \mathcal{O}(n) + \mathcal{O}(n - K) + \mathcal{O}(n - 2\cdot K) + \mathcal{O}(n - 3\cdot K)\\
     &=& \dots\\
     &=& \sum\limits_{i=0}^{p-1} \mathcal{O}(n - iK) + C(n - p\cdot K)\\
     &=& \mathcal{O}(n\cdot p- K\sum\limits_{i=0}^{p-1} i) + C(n - p\cdot K)\\
     &=& \mathcal{O}(n\cdot p- K\frac{p(p-1)}{2}) + C(n - p\cdot K)\\
     &=& \mathcal{O}(n\cdot p) +\mathcal{O}(p^{2}) + C(n - p\cdot K)\\
\end{array}
$$
</div>

Comme on connaît $C(1)$m on prend $p$ tel que $n - p\cdot K = 1$, c'est à dire : $p = \frac{n-1}{K}$ :

<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(n\cdot \frac{n-1}{K}) +\mathcal{O}((\frac{n-1}{K})^{2}) + C(1)\\
     &=& \mathcal{O}(n^2)
\end{array}
$$
</div>

{% enddetails %}

{% exercice %}
Que vaut $C(n)$ si :

<div>
$$
\begin{cases}
C(n) = \mathcal{O}(1) + C(\frac{n}{2})\\
C(1) = \mathcal{O}(1)
\end{cases}
$$
</div>

{% endexercice %}
{% details "corrigé" %}

<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(1) + C(\frac{n}{2})\\
     &=& \mathcal{O}(1) + \mathcal{O}(1) + C(\frac{n}{4})\\
     &=& \dots\\
     &=& p\cdot \mathcal{O}(1) + C(\frac{n}{2^p})\\
     &=& \mathcal{O}(p) + C(\frac{n}{2^p})\\
\end{array}
$$
</div>

Si $p=\log_2(n)$, on a $\frac{n}{2^p} = \frac{n}{2^{\log_2(n)}} = \frac{n}{n} =1$, donc :

<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(\log_2(n)) + C(1)\\
     &=& \mathcal{O}(\ln(n))
\end{array}
$$
</div>

{% enddetails %}
{% exercice %}
Que vaut $C(n)$ si :

<div>
$$
\begin{cases}
C(n) = \mathcal{O}(n) + C(\frac{n}{2})\\
C(1) = \mathcal{O}(1)
\end{cases}
$$
</div>

{% endexercice %}
{% details "corrigé" %}

<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(n) + C(\frac{n}{2})\\
     &=& \mathcal{O}(n) + \mathcal{O}(\frac{n}{2}) + C(\frac{n}{4})\\
     &=& \dots\\
     &=& \sum\limits_{0\leq i < p} \mathcal{O}(\frac{n}{2^i}) + C(\frac{n}{2^p})\\
     &=& \mathcal{O}(n\sum\limits_{0\leq i < p}\frac{1}{2^i}) + C(\frac{n}{2^p})\\
\end{array}
$$
</div>

[On a vu précédemment](../projet-sommes-classiques/#problème-1/2^i){.interne} que la série $\sum\limits_{0\leq i < p}\frac{1}{2^i}$ était plus petite que 2, donc : $\mathcal{O}(n\sum\limits_{0\leq i < p}\frac{1}{2^i}) = \mathcal{O}(n)$, ce qui simplifie beaucoup notre équation :

<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(n\sum\limits_{0\leq i < p}\frac{1}{2^i}) + C(\frac{n}{2^p})\\
     &=& \mathcal{O}(n) + C(\frac{n}{2^p})\\
\end{array}
$$
</div>

On peut ici tranquillement prendre $p=\log_2(n)$ pour obtenir :

<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(n)
\end{array}
$$
</div>

{% enddetails %}

{% exercice %}
Que vaut $C(n)$ si :

<div>
$$
\begin{cases}
C(n) = \mathcal{O}(1) + 2\cdot C(\frac{n}{2})\\
C(1) = \mathcal{O}(1)
\end{cases}
$$
</div>

{% endexercice %}
{% details "corrigé" %}

<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(1) + 2\cdot C(\frac{n}{2})\\
     &=& \mathcal{O}(1) + 2\cdot \mathcal{O}(1) + 4\cdot C(\frac{n}{4})\\
     &=& \dots\\
     &=& \sum\limits_{0\leq i < p} (2^i \cdot \mathcal{O}(1)) + 2^p \cdot C(\frac{n}{2^p})\\
     &=& \mathcal{O}(\sum\limits_{0\leq i < p}2^i) + 2^p \cdot C(\frac{n}{2^p})\\
     &=& \mathcal{O}(2^{p}-1) + 2^p \cdot C(\frac{n}{2^p})\\
     &=& \mathcal{O}(2^{\log_2(n)}-1) + 2^{\log_2(n)} \cdot C(1)\\
     &=& \mathcal{O}(n) + n \cdot C(1)\\
     &=& \mathcal{O}(n) + n \cdot \mathcal{O}(1)\\
     &=& \mathcal{O}(n)
\end{array}
$$
</div>

{% enddetails %}
{% exercice %}
Que vaut $C(n)$ si :

<div>
$$
\begin{cases}
C(n) = \mathcal{O}(n) + 2\cdot C(\frac{n}{2})\\
C(1) = \mathcal{O}(1)
\end{cases}
$$
</div>

{% endexercice %}
{% details "corrigé" %}

<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(n) + 2\cdot C(\frac{n}{2})\\
     &=& \mathcal{O}(n) + 2\cdot \mathcal{O}(\frac{n}{2}) + 4\cdot C(\frac{n}{4})\\
     &=& \mathcal{O}(n) + \mathcal{O}(n) + 4\cdot C(\frac{n}{4})\\
     &=& 2 \mathcal{O}(n) + 2^2\cdot C(\frac{n}{2^2})\\
     &=& \dots\\
     &=& p\cdot \mathcal{O}(n) + 2^p \cdot C(\frac{n}{2^p})\\
     &=& \mathcal{O}(p\cdot n) + 2^p \cdot C(\frac{n}{2^p})\\
     &=& \mathcal{O}(\log_2(n)\cdot n) + 2^{\log_2(n)} \cdot C(1)\\
     &=& \mathcal{O}(n\ln(n)) + n \cdot C(1)\\
     &=& \mathcal{O}(n\ln(n)) + n \cdot \mathcal{O}(1)\\
     &=& \mathcal{O}(n\ln(n))
\end{array}
$$
</div>

{% enddetails %}

Terminons cette partie avec un piège classique dans lequel tombent (pratiquement tous) les débutants :

{% exercice %}

Quelle équation de complexité $C(n)$ vérifie l'algorithme suivant ?

```pseudocode
algorithme f(n: entier) → entier:
    si n < 2:
        rendre 1
    rendre f(n // 2) * f(n // 4)
```

Calculer sa complexité via un encadrement et en utilisant les équations précédentes
{% endexercice %}
{% details "corrigé" %}

Le piège se trouve dans la troisième ligne de l'algorithme. Elle consiste en :

- le calcul de $f(n//2)$
- le calcul de $f(n//4)$
- la multiplication des deux valeurs obtenues

Cette ligne est donc de complexité $C(n//2) + C(n//4) + \mathcal{O}(1)$.

On a donc l'équation suivante à résoudre :

<div>
$$
\begin{cases}
C(n) = \mathcal{O}(1) + C(\frac{n}{2}) + C(\frac{n}{4})\\
C(1) = \mathcal{O}(1)
\end{cases}
$$
</div>

La complexité est croissante, on peut donc écrire :

<div>
$$
\begin{array}{lcl}
\mathcal{O}(1) + 2C(\frac{n}{4}) &\leq C(n) \leq& \mathcal{O}(1) + 2C(\frac{n}{2})
\end{array}
$$
</div>

L'équation de gauche se résolvant exactement de la même manière que celle de droite on obtient $\mathcal{O}(n)  \leq C(n) \leq \mathcal{O}(n)$, donc : $C(n) = \mathcal{O}(n)$.
{% enddetails %}

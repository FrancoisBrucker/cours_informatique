---
layout: layout/post.njk

title: Fibonacci

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Corrigé](./corrigé){.interne}
{% endlien %}

[La suite de Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci) est définie par l'équation de récurrence :

<div>
$$
F(n) =
\begin{cases}
F(n-1) + F(n-2) \text{ si }n> 2\\
F(1) = F(2) = 1
\end{cases}
$$
</div>

Nous allons utiliser cette suite pour donner des techniques utiles pour l'étude d'algorithmes récursifs

## Valeurs

{% faire %}
En utilisant l'équation de récurrence, montrez que :

<div>
$$
\begin{array}{ccccc}
\Omega((\sqrt{2})^n)&=&F(n)&=& \mathcal{O}(2^n)
\end{array}
$$
</div>

{% endfaire %}

En utilisant le fait que la suite de Fibonacci est [une suite récurrente linéaire](https://fr.wikipedia.org/wiki/Suite_r%C3%A9currente_lin%C3%A9aire), on peut même donner une valeur explicite de chaque valeur. Démontrons le :

{% faire %}
En utilisant le fait que les deux racines du polynôme $P(X) = X^2 -X-1$ sont $\phi_+ = \frac{1 + \sqrt{5}}{2}$ et $\phi_- = \frac{1 - \sqrt{5}}{2}$, montrez que pour $n>0$ :

<div>
$$
F(n) = \frac{\phi_+^n - \phi_-^n}{\sqrt{5}}
$$
</div>

{% endfaire %}

## Fibonacci récursif

<span id="algorithme-fibonacci-rec"></span>

```pseudocode/
algorithme fibonacci_rec(n: entier) → entier:
    si n ≤ 2:
        rendre 1
    rendre fibonacci_rec(n-1) + fibonacci_rec(n-2)
```

{% faire %}
Montrez que le programme précédent est bien un algorithme qui calcule la valeur de Fibonacci.
{% endfaire %}

{% faire %}
Montrez que la complexité de l'algorithme `fibonacci_rec(n)`{.language-} est en $\Omega(F(n))$.
{% endfaire %}

Sa complexité est rédhibitoire.

## Récursif terminal

L'algorithme récursif est sous optimal car il recalcule plein de fois la même chose. Pour calculer $F(n)$ il calcule deux fois $F(n-2)$, une fois dans la somme et une fois dans le calcul de $F(n-1)$.

{% faire %}

Utilisez [la transformation en récursion terminale](../../projet-itératif-récursif/#transformer-rec-terminale){.interne} pour améliorer la complexité de cet algorithme récursif.
{% endfaire %}

## Fibonacci Itératif

{% faire %}
Créez un algorithme itératif calculant $F(n)$ avec une complexité de $\mathcal{O}(n)$
{% endfaire %}

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
F(n) = F(n-1) + F(n-2)
$$
</div>

Si $n > 2$ et $F(1) = F(2) = 1$

Nous allons utiliser cette suite pour donner des techniques utiles pour l'étude d'algorithmes récursifs

### Fibonacci récursif

```python
def fibonacci_rec(n):
    if n < 3:
        return 1
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)
```

Cette partie vous donne le principe général lorsque l'on calcule des complexités d'algorithmes récursifs.

1. Donnez l'équation de récurrence permettant de calculer le nombre $A(n)$ d'appels à la fonction dans l'exécution de `fibonacci_rec(n)`. Montrer que cette valeur est égale à $F(n)$.
2. Donnez l'équation de récurrence permettant de calculer la complexité $C(n)$ de l'exécution de `ma_fonction(n)`.
3. Montrez que $\mathcal{O}(1) + 2\cdot C(n-2) \leq C(n) \leq \mathcal{O}(1) + 2\cdot C(n-1)$
4. En déduire que :
   1. $C(n) \leq \mathcal{O}(1)\cdot (\sum_{i=0}^{n-3}2^i) + 2^{n-2} \cdot C(2)$
   2. $C(n) \geq  \mathcal{O}(1)\cdot (\sum_{i=0}^{(n-4)/2}2^i) + {(\sqrt{2})}^{n-2} \cdot C(2)$
5. en conclure que :
   1. $C(n) =\mathcal{O}(2^n)$
   2. $C(n) =\Omega((\sqrt{2})^n)$

{% info %}
La valeur d'[une série géométrique](https://fr.wikipedia.org/wiki/S%C3%A9rie_g%C3%A9om%C3%A9trique) est à connaitre. On en a souvent besoin en algorithmie.
{% endinfo %}

### Valeur de $F(n)$

Montrez (par récurrence) que :

<div>
$$
F(n) = \frac{1}{\sqrt{5}}(\varphi^n-\frac{1}{(-\varphi)^n})
$$
</div>

Où $\varphi = \frac{1+\sqrt{5}}{2}$ qui est le nombre d'or et une racine du polynôme $P(X) = X^2 - X - 1$. Vous pourrez utiliser le fait que $-\frac{1}{\varphi}= \frac{1-\sqrt{5}}{2}$ et est l'autre racine de $P(X)$.

{% info %}
C'est hors programme, mais c'est la façon de résoudre [les suite linéaires récurrentes](https://fr.wikipedia.org/wiki/Suite_r%C3%A9currente_lin%C3%A9aire)
{% endinfo %}

En déduire que le nombre d'appels de la fonction récursive de la partie précédente vaut : $A(n) = \Theta(\varphi^n)$

### Itératif

Donnez un algorithme itératif de complexité $\mathcal{O}(n)$ pour calculer $F(n)$

### Récursif terminal

L'algorithme récursif est sous optimal car il recalcule plein de fois la même chose. Pour calculer $F(n)$ il calcule deux fois $F(n-2)$, une fois dans la somme et une fois dans le calcul de $F(n-1)$.

L'algorithme itératif ne fait pas la même chose car il stocke les valeurs intermédiaires. Une technique puissante pour accéder à la même chose récursivement est de passer les variables en paramètres :

Démontrer que :

- `fibo_rec_terminal(n, 1, 1)`{.language-} calcule bien $F(n)$ :
- sa complexité est $\mathcal{O}(n)$

```python
def fibo_rec2(n, a=1, b=1):
    if n <= 1:
        return b
    elif n <= 2:
        return a
    else:
        return fibo_rec2(n - 1, a + b, a)
```

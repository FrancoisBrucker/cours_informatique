---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Récursif

En notant $A(n)$ le nombre d'appels à la fonction, on a :

- l'appel proprement dit,
- le nombre d'appel à `fibonacci_rec(n-1)`{.language-}
- le nombre d'appel à `fibonacci_rec(n-2)`{.language-}

Ce qui donne l'équation suivante :

<div>
$$
A(n) = 1 + A(n-1) + A(n-2)
$$
</div>

En notant $C(n)$ la complexité de la fonction, on a l'équation de récurrence suivante :

<div>
$$
C(n) = \mathcal{O}(1) + C(n-1) + C(n-2)
$$
</div>

La complexité étant croissante, on a que : $C(n-1) \geq C(n-2)$ et on a bien l'inégalité :

<div>
$$
\mathcal{O}(1) + 2 \cdot C(n-2) \leq C(n) \leq \mathcal{O}(1) + 2 \cdot C(n-1)
$$
</div>

<div>
$$
\begin{array}{ccll}
C(n) &\leq & \mathcal{O}(1) + 2 \cdot C(n-1)&\\
     &\leq & \mathcal{O}(1) + 2 \cdot (\mathcal{O}(1) + 2 \cdot C(n-2)) & \text{en réapplicant l'inégalité pour } C(n-1)\\
     &\leq & \mathcal{O}(1)\cdot (1 + 2) + 4 \cdot C(n-2)&\\
     &\leq & \mathcal{O}(1)\cdot (1 + 2) + 4 \cdot (\mathcal{O}(1) + 2 \cdot C(n-3)) & \text{en réapplicant l'inégalité pour } C(n-2)\\
     &\leq & \mathcal{O}(1)\cdot (1 + 2 + 4) + 8 \cdot C(n-3)&\\
\end{array}
$$
</div>

On peut réappliquer l'inégalité de récurrence autant de fois que l'on veut ce qui donne, en l'appliquant $K$ fois :

<div>
$$
\begin{array}{ccll}
C(n) &\leq & \mathcal{O}(1)\cdot (\sum_{i=0}^{K-1}2^i) + 2^K \cdot C(n-K)&\\
\end{array}
$$
</div>

Les seules valeurs de $C(n)$ connues sont celles pour $n=1$ ou $n=2$. Il faut donc appliquer notre formule pour $K=n-2$, ce qui donne l'inégalité :

<div>
$$
\begin{array}{ccll}
C(n) &\leq & \mathcal{O}(1)\cdot (\sum_{i=0}^{n-3}2^i) + 2^{n-2} \cdot C(2)&\\
\end{array}
$$
</div>

De même, en utilisant l'inégalité $\mathcal{O}(1) + 2 \cdot C(n-2) \leq C(n)$, on obtient :

<div>
$$
\begin{array}{ccll}
C(n) &\geq & \mathcal{O}(1) + 2 \cdot C(n-2)&\\
     &\geq & \mathcal{O}(1) + 2 \cdot (\mathcal{O}(1) + 2 \cdot C(n-4)) & \text{en réappliquant l'inégalité pour } C(n-2)\\
     &\geq & \mathcal{O}(1)\cdot (1 + 2) + 4 \cdot C(n-4)&\\
     &\geq & \mathcal{O}(1)\cdot (1 + 2) + 4 \cdot (\mathcal{O}(1) + 2 \cdot C(n-6)) & \text{en réappliquant l'inégalité pour } C(n-4)\\
     &\geq & \mathcal{O}(1)\cdot (1 + 2 + 4) + 8 \cdot C(n-6)&\\
\end{array}
$$
</div>

De même que précédemment, en applicant l'inégalité de récurrence $K$ fois :

<div>
$$
\begin{array}{ccll}
C(n) &\geq & \mathcal{O}(1)\cdot (\sum_{i=0}^{K-1}2^i) + 2^K \cdot C(n-2\cdot K)&\\
\end{array}
$$
</div>

Les seules valeurs de $C(n)$ connues sont celles pour $n=1$ ou $n=2$. Il faut donc appliquer notre formule pour $K=\frac{n-2}{2}$, ce qui donne l'inégalité :

<div>
$$
\begin{array}{ccll}
C(n) &\geq & \mathcal{O}(1)\cdot (\sum_{i=0}^{(n-4)/2}2^i) + {(\sqrt{2})}^{n-2} \cdot C(2)&\\
\end{array}
$$
</div>

La fin est facile en utilisant le fait que $\sum_{i=0}^{K}2^i = 2^{K+1} - 1$

## Valeur de $F(n)$

On prouve la propriété par récurrence.

Initialisation :

- $F(1) = 1 = \frac{1}{\sqrt{5}}(\frac{1+\sqrt{5}}{2} - \frac{1-\sqrt{5}}{2}) = \frac{1}{\sqrt{5}}(\varphi - \frac{1}{-\varphi})$
- $F(2) = \frac{1}{\sqrt{5}}(\varphi^2-\frac{1}{(-\varphi)^2}) = \frac{1}{\sqrt{5}}(\varphi + 1 -(\frac{1}{(-\varphi)} + 1) = \frac{1}{\sqrt{5}}(\varphi + \frac{1}{\varphi}) = F(1)$

On suppose la propriété vrai jusqu'à $n-1$. Pour $n$ :

$F(n) = F(n-1) + F(n-2) = \frac{1}{\sqrt{5}}(\varphi^{n-1}-\frac{1}{(-\varphi)^{n-1}}) + \frac{1}{\sqrt{5}}(\varphi^{n-2}-\frac{1}{(-\varphi)^{n-2}}) = \frac{1}{\sqrt{5}}(\varphi^{n-2}(1 + \varphi) - \frac{1}{(-\varphi)^{n-2}}(1+ \frac{1}{\varphi}))$

Comme $\varphi$ et $-\frac{1}{\varphi}$ sont les racines du polynôme $P(X) = X^2 - X -1$ on a :

$F(n) = \frac{1}{\sqrt{5}}(\varphi^{n-2}(\varphi^2) - \frac{1}{(-\varphi)^{n-2}}(\frac{1}{\varphi^2})) = \frac{1}{\sqrt{5}}(\varphi^n-\frac{1}{(-\varphi)^n})$

## Récursif terminal

La complexité étant terminale, il y a $\mathcal{O}(n)$ appels récursifs. Comme le reste de la fonction est en $\mathcal{O}(1)$ la complexité totale est en $\mathcal{O}(n)$.

Le fait que la fonction calcule bien la suite de Fibonacci se fait par récurrence. On va montrer par récurrence que `fibo(n, a, b)` rend la valeur de la suite pour $F(1) = b$ et $F(2) = a$.

- Initialisation : `fibo(1, a, b) = b` et `fibo(2, a, b) = a`
- On suppose la propriété vraie pour `fibo(n-1, a, b)`. Comme `fibo(n, a, b) = fibo(n-1,a+b , a)`, la propriété est vérifiée.

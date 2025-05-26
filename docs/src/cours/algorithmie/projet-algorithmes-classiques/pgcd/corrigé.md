---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


<span id="algorithme-pgcd-modulo"></span>

```pseudocode
algorithme pgcd_mod(a: entier, b: entier) → entier:  # a, b ≥ 0
    si b == 0:
        rendre a
    si a < b:
        a, b ← b, a
    
    rendre pgcd_mod(b, a % b)
```

{% note "**Propriété**" %}

## Complexité

Pour tous entiers $a \geq b \geq 0$ on a :

<div>
$$
a \mathbin{\small\%} b < \frac{a}{2}
$$
</div>

{% endnote %}
{% details "preuve", "open" %}
Comme $a \mathbin{\small\\%} b < b$, si $b \leq \frac{a}{2}$ la propriété est démontrée et si $b > \frac{a}{2}$ on a $a // b = 1$ et donc $a \mathbin{\small\\%} b = a - b < \frac{a}{2}$

{% enddetails %}

Rappelez vous de cette propriété, elle peut se révéler extrêmement utile pour le calcul de complexité. Par exemple pour notre cas, le nombre de récursions ne peut excéder le nombre de fois où l'on peut diviser $a$ ou $b$ par 2 : il est inférieur à $\log_2(a)$. Si le calcul du modulo s'effectue en $\mathcal{O}(1)$ opérations, la complexité totale de l'algorithme est en $\mathcal{O}(\ln(\max(a, b)))$, ce qui est très bon !

## Pgcd et Fibonacci

Par définition, on a $F(n+1) = F(n) + F(n-1)$ et comme $F(n) > F(n-1)$, cette équation est aussi la division euclidienne de $F(n)$ par $F(n-1)$ puisqu'elle est unique.

La propriété précédente nous montre que `pgcd_mod(F(n+1), F(n))`{.language-} va appeler `pgcd_mod(F(n), F(n+1) % F(n)) = pgcd_mod(F(n), F(n-1))`{.language-}. Il va donc y avoir $n$ récursion jusqu'à arriver à l'appel de `pgcd_mod(F(1), 0)`{.language-} qui va conclure la récursion.

Montrer que ces nombres sont minimaux se fait simplement par récurrence sur le nombre  de récursions.

- **initialisation**. Pour qu'il y ait qu moins 1 récursion, il faut que $a \geq b \geq 1 = F(2) = F(1) > 0$.
- **récursion**. On suppose que pour faire au moins $k$ itérations il faut que  $a \geq F(k+1)$ et  $b \geq F(k)$. Soit $a \geq b$ deux entiers tels que `pgcd_mod(a, b)`{.language-} effectue $k+1$ itérations. Ceci implique que `pgcd_mod(b, a % b)`{.language-} effectue $k$ itérations, par hypothèse de récursion on a alors que $b \geq F(k+1)$ et $a {\small \\%} b \geq F(k)$ et donc $a \geq F(k+1) + F(k) = F(k+2)$.

Cette propriété permet que l'on peut borner le nombre de récursions par $b$ ! Pour qu'il y ait au moins $n$ récursion, il faut que $a \geq b \geq F(n)$. Comme, [on a vu](../fibonacci/){.interne}, $F(n) = \mathcal{O}(2^n)$ on en déduit que le nombre de récursions et donc la complexité de `pgcd_mod(a, b)`{.language-} est en $\mathcal{O}(\ln(\min(a, b)))$. Ce qui est à comparer à l'algorithme avec des soustractions dont la complexité était $\mathcal{O}(\min(a, b))$.

## ggcd binaire

{% lien %}
<https://fr.wikipedia.org/wiki/Algorithme_binaire_de_calcul_du_PGCD>
{% endlien %}

Les propriétés utilisées conservent clairement le pgcd et, comme pour l'algorithme du pgcd initial, à chaque récursion le max de $a$ et $b$ sera strictement plus petit : on arrivera forcément à la condition d'arrêt ce qui en fait bien un algorithme.

Le calcul de sa complexité se fait comme pour [l'exponentiation indienne](../../../projet-exponentiation/étude-algorithmique/#complexité-rapide){.interne} et permet de prouver qu'elle est en $\mathcal{O}(\max(a, b))$. L'intérêt de cette version est qu'elle se fait tres simplement en machine où les entiers sont codés par des tableaux de bits et où la multiplication et la division d'un nombre par 2 revient à décaler sa représentation binaire d'un bit vers la droite ou la gauche respectivement.

Il n'y a pas à calculer le modulo, opération plus complexe.

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

Pour tous entiers $a \geq b \geq 0$ on a "

<div>
$$
a \mathbin{\small\\%} b < \frac{a}{2}
$$
</div>

{% endnote %}
{% details "preuve", "open" %}
Comme $a \mathbin{\small\\%} b < b$, si $b \leq \frac{a}{2}$ la propriété est démontrée et si $b > \frac{a}{2}$ on a $a // b = 1$ et donc $a \mathbin{\small\\%} b = a - b < \frac{a}{2}$

{% enddetails %}

Rappelez vous de cette propriété, elle peut se révéler extrêmement utile pour le calcul de complexité. Par exemple pour notre cas, le nombre de récursions ne peut excéder le nombre de fois où l'on peut diviser $a$ ou $b$ par 2 : il est inférieur à $\log_2(a)$. Si le calcul du modulo s'effectue en $\mathcal{O}(1)$ opérations, la complexité totale de l'algorithme est en $\mathcal{O}(\ln(\max(a, b)))$, ce qui est très bon !

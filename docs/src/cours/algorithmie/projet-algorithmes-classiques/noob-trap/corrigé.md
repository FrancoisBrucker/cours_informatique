---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

C'est bien la troisième proposition qui est la bonne !

La troisième ligne de l'algorithme a pour complexité :

- le calcul de $f(n//2)$
- le calcul de $f(n//4)$
- la multiplication des deux valeurs obtenues

En reprenant ce que l'on a fait pour Fibonacci, on a l'inégalité :

<div>
$$
C(n) \leq \mathcal{O}(1) + 2 \cdot C(n/2)
$$
</div>

Ce qui donne en réitérant cette inégalité :

<div>
$$
C(n) \leq \mathcal{O}(1)(\sum_{i=0}^K2^i) + 2^K \cdot C(n/2^K)
$$
</div>

Comme la seule complexité que l'on connait est $C(1) = \mathcal{O}(1)$, on doit prendre $K$ tel que $2^K \simeq n$, c'est à dire $k = \log_2(n)$. On a alors :

<div>
$$
C(n) \leq \mathcal{O}(1)(\sum_{i=0}^{\log_2(n)}2^i) + 2^{\log_2(n)} \cdot C(1)
$$
</div>

Et donc :

<div>
$$
C(n) \leq \mathcal{O}(1)(2^{\log_2(n) +1}) + 2^{\log_2(n)} \cdot C(1)
$$
</div>

Et comme $2^{\log_2(n)} = n$, on trouve bien $C(n) \leq \mathcal{O}(n)$.

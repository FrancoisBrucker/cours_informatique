---
layout: layout/post.njk

title: Triangle de Pascal

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Corrigé](./corrigé){.interne}
{% endlien %}

Le calcul du coefficient binomial se fait en utilisant [le triangle de Pascal](https://fr.wikipedia.org/wiki/Triangle_de_Pascal).

Pour $n > p > 0$ :

<div>
$$
C(n, p) = C(n-1, p-1) + C(n-1, p)
$$
</div>

et $C(n, 1) = C(n, n) = 1$

On vous demande de créer un algorithme :

1. récursif pour calculer $C(n, p)$, et d'en donner la complexité.
2. itératif pour calculer $C(n, p)$ en utilisant une variable matricielle $M[i][j]$ qui stocke toutes les valeurs de $C(i, j)$ intermédiaires, et d'en donner la complexité en mémoire et en nombre d'opérations.
3. itératif avec une complexité en mémoire de $\mathcal{O}(n)$ en remarquant qu'il suffit de conserver une seule ligne de a matrice.

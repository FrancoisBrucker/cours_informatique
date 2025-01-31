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
\binom{n}{k} = \binom{n-1}{k-1} \mathrel{+} \binom{n-1}{k}
$$
</div>

et :

<div>
$$
\binom{n}{1} = \binom{n}{n} = 1
$$
</div>

## Récursif

```pseudocode
algorithme binom_rec(n: entier, k: entier) → entier:
    si (n == k) ou (k == 1):
        rendre 1
    sinon:
        rendre binom_rec(n-1, k-1) + binom_rec(n - 1, k)
```

{% exercice %}
Quelle est la complexité de l'algorithme `binom_rec`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

{% enddetails %}

## Itératif v1

```pseudocode/
fonction binom_matrice(n: entier) → [[entier]]:
    matrice ← un tableau de [entier] de taille n

    pour chaque i de [1, n]:
        ligne ← un tableau d'entiers de taille i

        matrice[i-1] ← ligne
        pour chaque j allant de 1 à i:
            si (j == i) ou (j == 1):
                ligne[j - 1] ← 1
            sinon:
                précédent ← matrice[i-2]
                ligne[j - 1] ← précédent[j-2] + précédent[j - 1]

    rendre matrice
```

{% exercice %}
Utilisez la fonction `binom_matrice(n: entier) → [[entier]]`{.language-} pour rendre la valeur de 
{% endexercice %}
{% details "corrigé" %}

{% enddetails %}

> TBD faire binom

## Itératif v2

> TBD O(n) en mémoire avec 2 tableau ligne courante et ligne précédente

## Itératif v3

> TBD O(n) en mémoire avec 1 seul tableau

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

> TBD ajouter jusqu'a k et pas demis matrice. Est ce que ça change la complexité ?
> idem pour 3.
>
> Puis on optimise puisque l'on peut juste s'arrêter à k :

```pseudocode
algorithme binom(n: entier, k: entier) → entier:
    matrice ← un tableau de [entier] de taille n

    
    pour chaque i de [1, n]:
        k' ← min(i, k)

        ligne ← un tableau d'entiers de taille k'
        matrice[i-1] ← ligne
        pour chaque j allant de 1 à k':
            si (j == i) ou (j == 1):
                ligne[j - 1] ← 1
            sinon:
                précédent ← matrice[i-2]
                ligne[j - 1] ← précédent[j-2] + précédent[j - 1]

    ligne ← matrice[n-1]
    rendre ligne[k - 1]
```

Remarquez que le tableau précédent est obligatoire et se remplit au fur et à mesure, à chaque incrément de i
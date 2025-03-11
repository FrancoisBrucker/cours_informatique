---
layout: layout/post.njk

title: Triangle de Pascal optimisé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


L'algorithme suivant est le dernier algorithme que nous avons créé pour calculer $\binom{n}{k}$.

On va créer un algorithme qui rend uniquement la dernière ligne de la matrice :

```pseudocode/
algorithme binom_ligne(n: entier, k: entier) → [[entier]]:
    courante ← un tableau d'entiers de taille k+1
    précédente ← un tableau d'entiers de taille k+1

    pour chaque i de [0, n]:
        pour chaque j de [0, min(i, k)]:
            précédente[j] ← courante[j]

        pour chaque j allant de 0 à min(i, k):
            si (j == i) ou (j == 0):
                courante[j] ← 1
            sinon:
                courante[j] ← précédent[j-1] + précédent[j]

    rendre courante[k]
```

Sa complexité temporelle est $\mathcal{O}(nk)$ et il nécessite deux tableaux de taille $k$ pour fonctionner.

{% exercice %}
En remplissant la ligne courante de droite à gauche montrez que l'on peut se passer de la ligne `précédente`{.language-} et n'utiliser qu'un seul tableau  de taille $k$.

{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme binom_ligne(n: entier, k: entier) → [[entier]]:
    courante ← un tableau d'entiers de taille k+1

    pour chaque i de [0, n]:
        de j=min(i, k) à j=0 par pas de -1:
            si (j == i) ou (j == 0):
                courante[j] ← 1
            sinon:
                courante[j] ← courante[j-1] + courante[j]

    rendre courante[k]
```

L'algorithme devient _joli_, avec une seule boucle et un seul tableau.

{% enddetails %}

---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Tours de Hanoï sur Wikipédia](https://fr.wikipedia.org/wiki/Tours_de_Hano%C3%AF)
{% endlien %}

On suppose que l'on a les trois emplacements de tours A, B et C ; et que l'on veuille déplacer les disques de la tours A vers la tour C.

1. pour pouvoir déplacer le plus grand disque de la tour A, il faut avoir déplacé tous les disques au-dessus de lui. Comme c'est le plus grand disque, il est de plus seul sur son emplacement
2. une fois le plus grand disque seul sur sa tour, il faut le déplacer en C. Ceci n'est possible que si tous les autres disques sont en B. Il donc de plus qu'ils forment une tour
3. une fois le plus grand disque à sa place, il convient de déplacer la tour formée des autres disques, en B, sur l'emplacement C.

Donc si on possède un algorithme optimal, disons `hanoï(départ, arrivée, intermédiaire, n-1)`{.language-} pour une tour de taille $n-1$, alors l'algorithme optimal pour déplacer une tour de taille $n$ de A à C sera :

1. `hanoï(A, B, C, n-1)`{.language-}
2. déplace le disque restant en A sur l'emplacement C
3. `hanoï(B, C, A, n-1)`{.language-}

On obtient alors l'algorithme optimal suivant, en considérant que les tours sont des listes :

```python
A = list(range(5, -1, -1))
B = []
C = []

def hanoi(départ, arrivée, intermédiaire, n):
    if n == 0:
        return
    hanoi(départ, intermédiaire, arrivée, n-1)
    disque = départ.pop()
    arrivée.append(disque)
    print(A, B, C)
    hanoi(intermédiaire, arrivée, départ, n-1)

print(A, B, C)
hanoi(A, C, B, len(A))
```

On a montré que notre stratégie était optimale. Comptons le nombre d'appels récursif. Il suit l'équation de récurrence :

<div>
$$
C(n) = 2 + C(n-1) + C(n-1) = 2 + 2\cdot C(n-1)
$$
</div>

Et la terminaison : $C(0) = 0$

On obtient facilement l'expression, pour $n\geq 1$ :

<div>
$$
C(n) = \sum_{i=1}^n2^i + 2\cdot C(0) = \sum_{i=1}^n2^i
$$
</div>

La somme des $n>0$ premières puissances de 2 est à savoir facilement retrouver (c'est [une série géométrique](https://fr.wikipedia.org/wiki/S%C3%A9rie_g%C3%A9om%C3%A9trique#Terme_g%C3%A9n%C3%A9ral)) et vaut $2^{n+1}-2$.

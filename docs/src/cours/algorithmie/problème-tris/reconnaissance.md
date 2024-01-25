---
layout: layout/post.njk 
title: "Reconnaissance d'un tableau trié"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Définissions le problème de décision associé au problème de savoir si oui ou non un tableau d'entiers est trié :

{% note "**Problème de décision**" %}

- **nom** : est trié ?
- **données** : un tableau $T$ d'entiers
- **réponse** : $T$ est-il trié de façon croissante ?

{% endnote %}

Il existe un algorithme très simple pour le résoudre.

## <span id="algo-est-trie"></span> Algorithme

```python#
def est_trie(T):

    for i in range(1, len(T)):
        if T[i] < T[i-1]:
            return False
    return True
```

### Tests de Fonctionnement

L'algorithme rend bien :

- `True`{.language-} pour `est_trie([42])`{.language-}
- `False`{.language-} pour `est_trie([4, 2])`{.language-}
- `True`{.language-} pour `est_trie([2, 4])`{.language-}

### Preuve

La finitude de l'algorithme est claire puisqu'il n'y a qu'une boucle for avec autant d'itérations que la taille du tableau passé en paramètre.

La preuve va être aisée si l'on démontre l'invariant suivant :

{% note "**Invariant de boucle**" %}
À la fin d'un itération, les $i + 1$ premiers éléments du tableau sont triés.
{% endnote %}

1. à la fin de la première itération, si l'on est pas sorti de la boucle c'est que $T[i] \geq T[i-1]$ pour $i=1$ : les 2 premiers éléments du tableau sont bien triés.
2. Si l'invariant est vrai à la fin de l'itération $i-1$, à la fin de l'itération $i$ on à $T[i] \geq T[i-1]$ et comme les $i + 1$ premiers éléments du tableau sont triés : les $i + 1$ premiers éléments du tableau sont triés.

Au final :

- L'invariant prouve que : si on arrive à la ligne 6 de l'algorithme c'est que les $n$ premiers éléments du tableau sont triés.
- si on utilise le retour de la ligne 5 c'est qu'il existe $i$ avec $T[i] < T[i-1]$, donc $T$ ne peut être trié.

{% note "**Proposition**" %}
L'algorithme `est_trie`{.language-} est une solution au problème *"est trié ?"*
{% endnote %}

### Complexité

Ligne à ligne :

1. définition de la fonction $\mathcal{O}(1)$
2. —
3. une boucle for de $k$ itérations
4. un tests de deux valeurs dans un tableau : $\mathcal{O}(1)$
5. un retour de fonction $\mathcal{O}(1)$
6. un retour de fonction $\mathcal{O}(1)$

Que l'on sorte par le retour de la ligne 5 ou 6, le complexité est : $\mathcal{O}(k)$. Dans le cas le pire, on parcourt tout le tableau, donc :

{% note %}
La complexité de l'algorithme `est_trie`{.language-} est $\mathcal{O}(n)$ avec $n$ la taille du tableau en entrée.
{% endnote %}

## Complexité du problème de la reconnaissance

Comme toute case du tableau peut rendre le tableau non trié, on utilise l'argument de [la complexité du problème de la *"recherche"*](../../complexité-problème/#complexité-recherche){.interne}, un algorithme résolvant ce problème doit considérer toutes les cases du tableau et donc une borne min du problème *"est trié ?"* est $\Omega(n)$ où $n$ est la taille du tableau en entrée. Comme la complexité de `est_trie`{.language-}  est de $\mathcal{O}(n)$. On en conclut :

{% note "**Proposition**" %}
La complexité du problème *"est trié ?"* est de $\Theta(n)$ où $n$ est la taille du tableau en entrée.
{% endnote %}

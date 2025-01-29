---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Coefficient binomiaux récursif

```python
def comb_rec(n, p):

    if p <= 1 or n ==p :
        return 1
    else:
        return comb_rec(n-1, p-1) + comb_rec(n-1, k)
```

## Coefficient binomiaux itératif et $\mathcal{O}(n^2)$ en mémoire

On stocke une matrice triangulaire inférieure que l'on construit ligne à ligne.

```python
def comb_iter(n, p):
    C = [[1]]

    for i in range(1, n):
        C.append([])
        for j in range(i):
            c_i_j = C[i-1][j-1] + C[i-1][j]
            C[-1].append(c_i_j)

    return C[-1][p-1]
```

## Coefficient binomiaux itératif et $\mathcal{O}(n)$ en mémoire

On remarque que seule la dernière ligne est importante dans le calcul.

```python
def comb_iter2(n, p):
    C = [1]
    for i in range(1, n):
        C.append(0)
        r = C[0]
        for j in range(1, i):
            tempo = C[j]
            C[j] += r
            r = tempo

    return C[p-1]
```

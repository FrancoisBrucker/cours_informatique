---
layout: layout/post.njk

title:  "sujet Test 2 : complexité"
authors:
    - François Brucker
---

Calculez la complexité des algorithmes suivant :

Répondez aux questions dans l'ordre, si possible.

## 1. itératif

```python
def factorielle( n ):
    f = 1
    while n > 1:
        f = f * n
        n = n - 1
    return f
```

## 2. récursif

```python
def factorielle( n ):
    if n <= 1:
        return 1
    return n * factorielle(n-1)
```

## 3. puissance

```python
def puissance(nombre, exposant):
    résultat = 1
    compteur = exposant
    while compteur > 0:
        résultat *= nombre
        compteur -= 1
    return résultat
```

## 4. tris

```python
def selection(tab):
    for i in range(len(tab) - 1):
        min_index = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[min_index]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]
```

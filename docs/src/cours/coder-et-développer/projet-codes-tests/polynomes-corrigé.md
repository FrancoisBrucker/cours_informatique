---
layout: layout/post.njk

title: "Corrigé : Somme et produit de polynômes"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## `polynome.py`{.fichier}

```python

def valeur(coefficients, x):
    resultat = 0

    for i in range(len(coefficients)):
        resultat += coefficients[i] * x ** i
    return resultat


def somme(coefficients1, coefficients2):
    longueur1 = len(coefficients1)
    longueur2 = len(coefficients2)

    resultat = []
    for i in range(max(longueur1, longueur2)):
        resultat.append(0)

    for i in range(longueur1):
        resultat[i] += coefficients1[i]
    for i in range(longueur2):
        resultat[i] += coefficients2[i]

    return resultat


def produit(coefficients1, coefficients2):
    longueur1 = len(coefficients1)
    longueur2 = len(coefficients2)

    resultat = []

    for k in range(longueur1 + longueur2 - 1):
        i = min(longueur1 - 1, k)
        j = max(k - i, 0)

        valeur_k = 0
        while (i >= 0) and (j < longueur2):
            valeur_k += coefficients1[i] * coefficients2[j]
            i -= 1
            j += 1
        resultat.append(valeur_k)

    return resultat

```

## `test_polynome.py`{.fichier}

```python

from polynome import valeur, somme, produit

def test_valeur_constante():
    assert valeur([1], 4) == 1 * 4 ** 0


def test_valeur_vide():
    assert valeur([], 4) == 0


def test_valeur_polynome():
    assert valeur([1, 2, 3], 2) == 1 + 2 * 2 + 3 * 4


def test_somme_un_vide():
    assert somme([1, 2, 3], []) == [1, 2, 3]
    assert somme([], [1, 2, 3]) == [1, 2, 3]


def test_somme_egale():
    assert somme([1, 2, 3], [3, 2, 1]) == [4, 4, 4]


def test_somme_diferent():
    assert somme([1, 2, 3], [3]) == [4, 2, 3]
    assert somme([3], [1, 2, 3]) == [4, 2, 3]


def test_produit_longueur1():
    assert produit([1, 2, 3], [2]) == [2, 4, 6]
    assert produit([2], [1, 2, 3]) == [2, 4, 6]


def test_produit_egale():
    assert produit([2, 3], [3, 2]) == [6, 13, 6]

```

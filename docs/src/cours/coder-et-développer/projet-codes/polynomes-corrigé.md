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
    résultat = 0

    for i in range(len(coefficients)):
        résultat += coefficients[i] * x ** i
    return résultat


def somme(coefficients1, coefficients2):
    longueur1 = len(coefficients1)
    longueur2 = len(coefficients2)

    résultat = []
    for i in range(max(longueur1, longueur2)):
        résultat.append(0)

    for i in range(longueur1):
        résultat[i] += coefficients1[i]
    for i in range(longueur2):
        résultat[i] += coefficients2[i]

    return résultat


def produit(coefficients1, coefficients2):
    longueur1 = len(coefficients1)
    longueur2 = len(coefficients2)

    résultat = []

    for k in range(longueur1 + longueur2 - 1):
        i = min(longueur1 - 1, k)
        j = max(k - i, 0)

        valeur_k = 0
        while (i >= 0) and (j < longueur2):
            valeur_k += coefficients1[i] * coefficients2[j]
            i -= 1
            j += 1
        résultat.append(valeur_k)

    return résultat

```

> TBD il faut encore faire la question 4.
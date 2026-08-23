---
layout: layout/post.njk

title: Polynômes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD : faire bien.

> TBD : attention aux polynômes creux

## questions

Un polynôme peut être vu comme une liste de ses coefficients. Le polynôme $P(x) = 1 + 3x^2$ s'écrira ainsi avec la liste $[1, 0, 3]$ et plus généralement, le polynôme $P(x) = \sum_{i=0}^n a_ix^i$ s'écrira sous la forme d'une liste $L$ à $n+1$ éléments telle que $L[i] = a_i$.

Manipulons cette structure.

## Écrivez une fonction _somme_

Écrivez une fonction permettant de rendre le polynôme $R(x) = P(x) + Q(x)$, somme des 2 polynômes $P(x)$ et $Q(x)$ passés en paramètres.

Vous pourrez utiliser la méthode `append`{.language-} des listes qui ajoute un élément en fin de liste (si `l= [1, 2]`{.language-}, l'instruction `l.append(3)`{.language-} **modifie** `l`{.language-}, pour qu'elle soit égale à `l= [1, 2, 3]`{.language-})

## Écrivez une fonction _produit_

Écrivez une fonction permettant de rendre le produit le polynôme $R(x) = P(x) \cdot Q(x)$, produit des 2 polynômes $P(x)$ et $Q(x)$ passés en paramètres.

## Écrivez une fonction _valeur_

Écrivez une fonction prenant un polynôme $P(x)$ et un réel $r$ et rendant l'évaluation $P(r)$ de $P(x)$ en $r$.

Vous pourrez utiliser le fait que `x ** i`{.language-} en python soit égal à $x^i$

L'exonentiation est une opération couteuse en multiplications. Combien en avez-vous eu besoin pour exécuter votre fonction ?

## Amélioration

Si on note :

- $A(x) = a_0$
- $X(x) = x$
- $P(x) = \sum_{i=0}^n a_ix^i$
- $Q(x) = \sum_{i=0}^{n-1} a_{i+1}x^i$

On a clairement que : $P(x) = A(x) + X(x) \cdot R(x)$.

En déduire une méthode d'évaluation de polynômes moins gourmande en multiplications.

## réponses

L'exercice portait sur la structure de [polynômes](https://fr.wikipedia.org/wiki/Polyn%C3%B4me).

Un polynôme est défini mathématiquement par la fonction :

$$
P(x) = \sum_{i=0}^n a_i x^i
$$

Et informatiquement par une liste à $n+1$ éléments.

$$
[a_0, \dots, a_n]
$$

### $P(x) + Q(x)$

```python
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

```

## $P(x) \cdot Q(x)$

```python
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

## $P(A)$

```python
def valeur(coefficients, x):
    résultat = 0

    for i in range(len(coefficients)):
        résultat += coefficients[i] * x ** i
    return résultat

```

En utilisant l'exponentiation rapide, le calcul de $x^i$ prend $\log(i)$ multiplications. On effectue donc au total de l'ordre $n\log(n)$ multiplications pour calculer tous les $x^i$, $0 \leq i \leq n$.

## Méthode de Horner

L'optimisation proposée est dite [de Horner](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Ruffini-Horner#Valeur_d'un_polyn%C3%B4me_en_un_point). Comme beaucoup d'optimisation, elle cherche à ne pas recalculer plein de fois la même chose, ici $x^i$ dans le calcul de $x^k$ lorsque $i < j$.

En utilisant l'optimisation de Horner, on effectue au total de l'ordre $n$ multiplications pour calculer tous les $x^i$, $0 \leq i \leq n$.
i

```python
def evaluation(P, v):
    eval = P[-1]

    for i in range(len(P) - 2, -1, -1):
        eval = P[i] + v * eval

    return eval
```

---
layout: layout/post.njk

title:  "corrigé Test 1 : code"
authors:
    - François Brucker
---


L'exercice portait sur la structure de [polynômes](https://fr.wikipedia.org/wiki/Polyn%C3%B4me).

Un polynôme est défini mathématiquement par la fonction :

$$
P(x) = \sum_{i=0}^n a_i x^i
$$

et informatiquement par une liste à $n+1$ éléments.

$$
[a_0, \dots, a_n]
$$

## Barème

La note est sur 5.

1. code + test : 2pt
2. code : 1pt
3. code + test : 2pt
4. code + test : pas notée

{% info %}
Une seule personne a fait la question 4 (et tout le reste) et c'était juste ! Elle a donc eu 6 sur 5
{% endinfo %}

La ventilation des notes est :

|note  | 0.5  | 1   | 1.5 | 2   | 2.5 | 3 | 3.5 | 4 | 5 | 6 |
-------|------|-----|-----|-----|-----|---|-----|---|---|---|
|nombre|2     |2    |7    |3    |7    |13 |  3  | 2 | 2 | 1 |
|rang  | 42   | 40  | 33  | 30  | 23  |10 | 7   | 5 | 2 | 1 |

Pour une moyenne de 2.7 et un écart-type de 1.2.

## Erreurs fréquemment rencontrées

### Les tests

Beaucoup, beaucoup de flottement dans les tests. Pour que les tests soient utiles à votre pratique de code, il faut de l'habitude et comprendre ce que l'on fait.

Si vous ne faites pas l'effort d'intégrer vos tests à votre pratique du code vous n'allez jamais en comprendre l'utilité (et ce serait vraiment trop triste).

### Noms de fichiers

On doit facilement se retrouver dans le code, les noms des fichiers sont donc **important** et doivent être **informatifs**.

* `main.py`{.fichier} contient votre programme principal et rien d'autre. En particulier il ne doit **jamais** être importé
* vos fichiers de tests commencent tous par *"test_"* suivi du nom du fichier dont vous testez les fonctions
* pas d'accent et pas d'espace dans les noms de fichiers. Vous pouvez remplacer les espaces par `_`{.language-} (underscore)

### Ajout d'éléments à une liste

J'ai vu beaucoup de `L = L + [a]`{.language-} alors que `L.append(a)`{.language-} est meilleur en complexité ($\mathcal{O}(\mbox{len}(L))$ vs. $\mathcal{O}(1)$ !).

J'ai aussi vu beaucoup de `L = L + a`{.language-} qui est faux. Pour additionner deux objets ils faut qu'ils aient le même type. Là vous essayer d'additionner une liste et un entier.

### Soyez prêt

Beaucoup de flottement en début de test. Vous ne pouvez pas tester vos outils (vscode, python et pytest) la veille au soir si vous n'êtes pas sur de vous : les probabilités que ça ne fonctionne pas sont trop grande...

Vous avez une semaine pour vous préparer donc faites en sorte de ne pas être pris de court.

## 1

On cherche à évaluer $P(x)$ en un point.

### <span id="code-1"></span> code

```python
def valeur(coefficients, x):
    résultat = 0

    for i in range(len(coefficients)):
        résultat += coefficients[i] * x ** i
    return résultat

```

### <span id="tests-1"></span> tests

```python
def test_valeur_constante():
    assert valeur([1], 4) == 1 * 4 ** 0


def test_valeur_vide():
    assert valeur([], 4) == 0


def test_valeur_polynôme():
    assert valeur([1, 2, 3], 2) == 1 + 2 * 2 + 3 * 4

```

## 2

```python
    x = int(input("Donnez un entier : "))
    print("La valeur est : ", valeur([1, 1, 1, 1, 1], x))

```

## 3

On cherche le polynôme $P(x) + Q(x)$

### <span id="code-3"></span> code

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

### <span id="tests-3"></span> tests

```python
def test_somme_un_vide():
    assert somme([1, 2, 3], []) == [1, 2, 3]
    assert somme([], [1, 2, 3]) == [1, 2, 3]


def test_somme_égale():
    assert somme([1, 2, 3], [3, 2, 1]) == [4, 4, 4]


def test_somme_différent():
    assert somme([1, 2, 3], [3]) == [4, 2, 3]
    assert somme([3], [1, 2, 3]) == [4, 2, 3]

```

## 4

On cherche le polynôme $P(x) \cdot Q(x)$

### <span id="code-4"></span> code

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

### <span id="tests-4"></span> tests

```python
def test_produit_longueur1():
    assert produit([1, 2, 3], [2]) == [2, 4, 6]
    assert produit([2], [1, 2, 3]) == [2, 4, 6]


def test_produit_égale():
    assert produit([2, 3], [3, 2]) == [6, 13, 6]

```

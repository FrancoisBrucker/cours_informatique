---
layout: layout/post.njk

title: "Corrigé : Syracuse"
---

## Fichier `syracuse.py`{.fichier}

```python
def syracuse(x):
    if x % 2 == 0:
        return x / 2
    else:
        return 3 * x + 1


def suite(u_0):
    sortie = [u_0]

    u_n = u_0
    while u_n != 1:
        u_n = syracuse(u_n)
        sortie.append(u_n)

    return sortie

```

## Fichier `test_syracuse.py`{.fichier}

```python
from syracuse import syracuse, suite

def test_syracuse_pair():
    assert syracuse(2) == 1


def test_syracuse_impair():
    assert syracuse(1) == 4


def test_suite_u_0_1():
    assert suite(1) == [1]


def test_suite_u_0_5():
    assert suite(5) == [5, 16, 8, 4, 2, 1]

```

## Fichier `main.py`{.fichier}

```python
from syracuse import suite

sortie_utilisateur = input("Donnez un entier : ")

u_0 = int(sortie_utilisateur)

print("suite de Syracuse associée : ", suite(u_0))

```

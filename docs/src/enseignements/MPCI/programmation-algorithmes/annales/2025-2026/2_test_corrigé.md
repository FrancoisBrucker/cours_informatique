---
layout: layout/post.njk

title: "sujet Test 2 : programmation
authors:
  - François Brucker
---

## Barème

> TBD


## Erreurs fréquemment rencontrées

> TBD

## Corrigé

Je joins les 3 fichiers de code que j'ai écris.

### `main.py`{.language-}

```python
from fonctions import parenthèses, suite, bon_parenthésage

s = input("Entrez une chaîne de caractères : ")
s_restriction = parenthèses(s)
print("La chaîne contient la suite de parenthèses :", s_restriction)

suite_1 = suite(s_restriction)
print("La suite associée est : , ", suite_1)

if bon_parenthésage(suite_1):
    print("La suite correspond à un bon parenthésage")
else:
    print("La suite ne correspond pas à un bon parenthésage")

```

### `fonctions.py`{.language-}

```python
def parenthèses(chaîne):
    parenthèses = ""

    for c in chaîne:
        if c in "()":
            parenthèses += c
    return parenthèses


def suite(chaîne_de_parenthèses):
    suite = []

    for c in chaîne_de_parenthèses:
        if c == "(":
            suite.append(1)
        elif c == ")":
            suite.append(-1)
    return suite


def bon_parenthésage(suite_de_0_1):
    somme = 0

    for c in suite_de_0_1:
        somme += c

        if somme < 0:
            return False

    return True

```

### `test_fonctions.py`{.language-}


```python
from fonctions import parenthèses, suite, bon_parenthésage

def test_parenthèses():
    assert "()" == parenthèses("(1+2)-3")
    assert "" == parenthèses("coucou !")
    assert "())" == parenthèses("coucou (toi) :)")

def test_suite():
    assert [1, -1] == suite("()")
    assert [] == suite("")
    assert [1, -1, -1] == suite("())")    

def test_bon_parenthésage():
    assert bon_parenthésage([1, -1])
    assert bon_parenthésage([])
    assert not bon_parenthésage([1, -1, -1, 1])

```

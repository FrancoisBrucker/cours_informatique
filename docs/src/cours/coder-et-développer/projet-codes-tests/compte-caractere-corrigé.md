---
layout: layout/post.njk

title: "Corrigé : le compte est bon"
---

## Question 1

Fichier `main.py`{.fichier} :

```python
chaine_entrée = ""

while chaine_entrée != "sortie":
    chaine_entrée = input("Entre une chaîne de caractères : ")
    caractère_entrée = input("Entre un caractère : ")

    index_caractère = chaine_entrée.find(caractère_entrée)
    print("Premier index du caractère :", index_caractère)
```

## Question 2

### `fonctions.py`{.fichier}

```python
def donne_prochain_indice(chaine, indice):
    possible_suivant = chaine.find(chaine[indice], indice + 1)

    if possible_suivant > -1:
        return possible_suivant
    return None

```

### `test_fonctions.py`{.fichier}

```python
from fonctions import donne_prochain_indice


def test_donne_prochain_indice():
    assert donne_prochain_indice("bxaaxaaaxax", 4) == 8
    assert donne_prochain_indice("bxaaxaaaxax", 0) == None
```

### `main.py`{.fichier}

On ajoute à la fin du fichier `main.py`{.fichier} les lignes suivantes, dans le bloc `while`{.language-} :

```python
    if index_caractère == -1:
        print("Il n'apparaît pas")
    elif donne_prochain_indice(chaine_entrée, index_caractère) != None:
        print("Il apparaît plusieurs fois")
    else:
        print("Il apparaît une fois")
```

## Question 3

### `fonctions.py`{.fichier}

```python
def compte_caractère(chaine, indice):
    compte = 0

    while indice != None:
        compte += 1
        indice = donne_prochain_indice(chaine, indice)

    return compte
```

### `test_fonctions.py`{.fichier}

```python
from fonctions import compte_caractère 


def test_compte_caractère():
    assert compte_caractère("bxaaxaaaxax", 0) == 1
    assert donne_prochain_indice("bxaaxaaaxax", 1) == 4
```

### `main.py`{.fichier}

On ajoute à la fin du fichier `main.py`{.fichier} les lignes suivantes, dans le bloc `while`{.language-} :

```python
    if index_caractère > -1:
        print("caractère apparaît", compte_caractère(chaine_entrée, index_caractère), "fois.")
```

## Question 4

### `fonctions.py`{.fichier}

```python
def donne_max_doublon(chaine):
    nombre_max = 0

    for i in range(len(chaine)):
        nombre_max = max(nombre_max, compte_caractère(chaine, i))

    return nombre_max
```

### `test_fonctions.py`{.fichier}

```python
from fonctions import donne_max_doublon


def test_donne_max_doublon():
    assert donne_max_doublon("bxaaxaaaxax") == 6
```

### `main.py`{.fichier}

On ajoute à la fin du fichier `main.py`{.fichier} les lignes suivantes, dans le bloc `while`{.language-} :

```python
    if index_caractère > -1:
        if index_caractère == donne_max_doublon(chaine_entrée):
            print("c'est le max !")
```

## Fichiers complets

### `fonctions.py`{.fichier}

```python
def donne_prochain_indice(chaine, indice):
    possible_suivant = chaine.find(chaine[indice], indice + 1)

    if possible_suivant > -1:
        return possible_suivant
    return None


def compte_caractère(chaine, indice):
    compte = 0

    while indice != None:
        compte += 1
        indice = donne_prochain_indice(chaine, indice)

    return compte


def donne_max_doublon(chaine):
    nombre_max = 0

    for i in range(len(chaine)):
        nombre_max = max(nombre_max, compte_caractère(chaine, i))

    return nombre_max

```

### `test_fonctions.py`{.fichier}

```python
from fonctions import compte_caractère, donne_prochain_indice, donne_max_doublon


def test_donne_prochain_indice():
    assert donne_prochain_indice("bxaaxaaaxax", 4) == 8
    assert donne_prochain_indice("bxaaxaaaxax", 0) == None


def test_compte_caractère():
    assert compte_caractère("bxaaxaaaxax", 0) == 1
    assert donne_prochain_indice("bxaaxaaaxax", 1) == 4

def test_donne_max_doublon():
    assert donne_max_doublon("bxaaxaaaxax") == 6

```

### `main.py`{.fichier}

```python
from fonctions import donne_prochain_indice, compte_caractère, donne_max_doublon

chaine_entrée = ""

while chaine_entrée != "sortie":
    chaine_entrée = input("Entre une chaine de caractères : ")
    caractère_entrée = input("Entre un caractère : ")

    index_caractère = chaine_entrée.find(caractère_entrée)
    print("Premier index du caractère :", index_caractère)

    if index_caractère == -1:
        print("Il n’apparaît pas")
    elif donne_prochain_indice(chaine_entrée, index_caractère) != None:
        print("Il apparaît plusieurs fois")
    else:
        print("Il apparaît une fois")

    if index_caractère > -1:
        print("caractère apparaît", compte_caractère(chaine_entrée, index_caractère), "fois.")

        if index_caractère == donne_max_doublon(chaine_entrée):
            print("c'est le max !")

```

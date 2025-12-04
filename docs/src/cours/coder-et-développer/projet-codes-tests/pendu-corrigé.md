---
layout: layout/post.njk

title: "Corrigé : pendu"
---


## Corrigé de la question 1. Fonction `est_une_lettre(lettre, mot)`{.language-}

### tests de `est_une_lettre(lettre, mot)`{.language-}

Commençons par les tests. Ils vous étaient donnés dans l'énoncé. Il suffisait de les écrire. Par exemple :

```python
def test_est_une_lettre():
    assert est_une_lettre("i", "victoire")
    assert not est_une_lettre("e", "la disparition")
```

{% info %}
Pas besoin d'écrire `assert est_une_lettre("i", "victoire") == True`{.language-}, c'est équivalent à `assert est_une_lettre("i", "victoire")`{.language-}.
{% endinfo %}

### fonction `est_une_lettre(lettre, mot)`{.language-}

Plusieurs possibilités. Commençons par la plus simple, que **tout le monde** devrait arriver à faire, c'est une retranscription directe d'un algorithme du cours :

```python
def est_une_lettre(lettre, mot):
    for c in mot:
        if lettre == c:
            return True
    return False
```

On pouvait aussi utiliser le mot clé `in`{.language-} de python (supposé connu de tous), pour une solution écrite en 30 secondes chrono :

```python
def est_une_lettre(lettre, mot):
    if lettre in mot:
        return True
    else:
        return False
```

Notez que la version précédente est identique à la version ci-dessous, bien plus élégante :

```python
def est_une_lettre(lettre, mot):
    return lettre in mot
```

## Corrigé de la question 2. Fonction `caractères(lettre, mot)`{.language-}

### tests de `caractères(lettre, mot)`{.language-}

Encore une fois les tests étaient donnés. Il suffisait de les re-écrire :

```python
def test_caractères():
    assert [1, 5] == caractères("i", "victoire")
    assert [] == caractères("e", "la disparition")
```

### fonction `caractères(lettre, mot)`{.language-}

```python
def caractères(lettre, mot):
    position = []

    for i in range(len(mot)):
        if mot[i] == lettre:
            position.append(i)

    return position
```

On utilise ici la fonction `range`{.language-} pour itérer sur les indices du tableau plutôt que sur ses valeurs.

Encore une fois, **tout le monde** devrait arriver à faire cette fonction d'une seule traite, sans réfléchir.

## Corrigé de la question 3. Fonction `découvre(mot_caché, lettre, positions)`{.language-}

### tests de `découvre(mot_caché, lettre, positions)`{.language-}

Comme d'habitude, les tests étaient donnés dans l'énoncé :

```python
def test_découvre():
    assert ".rr..r" == découvre("......", "r", [1, 2, 5])
    assert "erreur" == découvre("erre.r", "u", [4])
    assert "erre.r" == découvre("erre.r", "u", [])

```

### fonction `découvre(mot_caché, lettre, positions)`{.language-}

La fonction que j'attends est :

```python
def découvre(mot_caché, lettre, positions):
    mot = ""

    for i in range(len(mot_caché)):
        if i in positions:
            mot += lettre
        else:
            mot += mot_caché[i]

    return mot
```

En utilisant les caractéristiques de la liste `positions`{.language-} trié par ordre croissant, on aurait pu forger la fonction ci-dessous de complexité $\mathcal{O}(n)$ (pourquoi est-ce que ça marche ?):

```python
def découvre(mot_caché, lettre, positions):
    mot = ""

    if len(positions) == 0:
        return mot_caché

    pos = 0
    for i in range(len(mot_caché)):
        if i == positions[pos]:
            mot += lettre
            pos = min(pos + 1, len(positions) - 1)
        else:
            mot += mot_caché[i]

    return mot

```

## Corrigé de la question 4. Fonction `caché(mot)`{.language-}

Comme toujours, les tests sont donnés dans l'énoncé :

```python
def test_caché():
    assert "" == caché("")
    assert "........................." == caché("anticonstitutionnellement")
```

En utilisant la multiplications des chaînes de caractères, la fonction est triviale :

```python
def caché(mot):
    return "." * len(mot)
```

## Corrigé de la question 5. Programme principal

Une proposition de programme principal :

```python
    mot_à_trouver = "table"
    mot_caché = caché(mot_à_trouver)

    print("mot à trouver :", mot_caché)
    nombre_essai = 0

    while est_une_lettre(".", mot_caché):
        lettre = input("Donnez une lettre : ")
        mot_caché = découvre(mot_caché, lettre, caractères(lettre, mot_à_trouver))
        print("mot à trouver :", mot_caché)

        nombre_essai += 1

    print("Victoire !, vous avez gagné en", nombre_essai, "essais.")
```

## Fichiers finaux

### `pendu.py`{.fichier}

```python/
def est_une_lettre(lettre, mot):
    return lettre in mot


def caractères(lettre, mot):
    position = []

    for i in range(len(mot)):
        if mot[i] == lettre:
            position.append(i)

    return position


def découvre(mot_caché, lettre, positions):
    mot = ""

    for i in range(len(mot_caché)):
        if i in positions:
            mot += lettre
        else:
            mot += mot_caché[i]

    return mot


def caché(mot):
    return "." * len(mot)

```

### `test_pendu.py`{.fichier}

```python/
from pendu import est_une_lettre, caractères, découvre, caché


def test_est_une_lettre():
    assert est_une_lettre("i", "victoire")
    assert not est_une_lettre("e", "la disparition")


def test_caractères():
    assert [1, 5] == caractères("i", "victoire")
    assert [] == caractères("e", "la disparition")


def test_découvre():
    assert ".rr..r" == découvre("......", "r", [1, 2, 5])
    assert "erreur" == découvre("erre.r", "u", [4])
    assert "erre.r" == découvre("erre.r", "u", [])


def test_caché():
    assert "" == caché("")
    assert "........................." == caché("anticonstitutionnellement")

```

### `main.py`{.fichier}

```python/
from pendu import caché, est_une_lettre, découvre, caractères


mot_à_trouver = "table"
mot_caché = caché(mot_à_trouver)


print("mot à trouver :", mot_caché)
nombre_essai = 0

while est_une_lettre(".", mot_caché):
    lettre = input("Donnez une lettre : ")
    mot_caché = découvre(mot_caché, lettre, caractères(lettre, mot_à_trouver))
    print("mot à trouver :", mot_caché)

    nombre_essai += 1

print("Victoire !, vous avez gagné en", nombre_essai, "essais.")

```

## Fichiers

### `pendu.py`{.language-}

```python

def est_une_lettre(lettre, mot):
    return lettre in mot


def caractères(lettre, mot):
    position = []

    for i in range(len(mot)):
        if mot[i] == lettre:
            position.append(i)

    return position


def découvre(mot_caché, lettre, positions):
    mot = ""

    for i in range(len(mot_caché)):
        if i in positions:
            mot += lettre
        else:
            mot += mot_caché[i]

    return mot


def caché(mot):
    return "." * len(mot)

```

### `test_pendu.py`{.language-}

```python
from pendu import est_une_lettre, caractères, découvre, caché


def test_est_une_lettre():
    assert est_une_lettre("i", "victoire")
    assert not est_une_lettre("e", "la disparition")


def test_caractères():
    assert [1, 5] == caractères("i", "victoire")
    assert [] == caractères("e", "la disparition")


def test_découvre():
    assert ".rr..r" == découvre("......", "r", [1, 2, 5])
    assert "erreur" == découvre("erre.r", "u", [4])
    assert "erre.r" == découvre("erre.r", "u", [])


def test_caché():
    assert "" == caché("")
    assert "........................." == caché("anticonstitutionnellement")
```

### `main.py`{.language-}

```python
from pendu import caché, est_une_lettre, découvre, caractères


mot_à_trouver = "table"
mot_caché = caché(mot_à_trouver)


print("mot à trouver :", mot_caché)
nombre_essai = 0

while est_une_lettre(".", mot_caché):
    lettre = input("Donnez une lettre : ")
    mot_caché = découvre(mot_caché, lettre, caractères(lettre, mot_à_trouver))
    print("mot à trouver :", mot_caché)

    nombre_essai += 1

print("Victoire !, vous avez gagné en", nombre_essai, "essais.")

```

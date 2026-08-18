---
layout: layout/post.njk

title: "Programme : pendu"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Fichier `pendu.py`{.fichier}

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

## Fichier `main.py`{.fichier}

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

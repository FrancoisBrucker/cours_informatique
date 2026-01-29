---
layout: layout/post.njk

title: "Programme : le compte est bon"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Fichier `fonctions.py`{.fichier}

```python
def donne_prochain_indice(chaîne, indice):
    possible_suivant = chaîne.find(chaîne[indice], indice + 1)

    if possible_suivant > -1:
        return possible_suivant
    return None


def compte_caractère(chaîne, indice):
    compte = 0

    while indice != None:
        compte += 1
        indice = donne_prochain_indice(chaîne, indice)

    return compte


def donne_max_doublon(chaîne):
    nombre_max = 0

    for i in range(len(chaîne)):
        nombre_max = max(nombre_max, compte_caractère(chaîne, i))

    return nombre_max

```

## Fichier `main.py`{.fichier}

```python
from fonctions import donne_prochain_indice, compte_caractère, donne_max_doublon

chaîne_entrée = ""

while chaîne_entrée != "sortie":
    chaîne_entrée = input("Entre une chaîne de caractères : ")
    caractère_entrée = input("Entre un caractère : ")

    index_caractère = chaîne_entrée.find(caractère_entrée)
    print("Premier index du caractère :", index_caractère)

    if index_caractère == -1:
        print("Il n’apparaît pas")
    elif donne_prochain_indice(chaîne_entrée, index_caractère) != None:
        print("Il apparaît plusieurs fois")
    else:
        print("Il apparaît une fois")

    if index_caractère > -1:
        print("caractère apparaît", compte_caractère(chaîne_entrée, index_caractère), "fois.")

        if index_caractère == donne_max_doublon(chaîne_entrée):
            print("c'est le max !")

```

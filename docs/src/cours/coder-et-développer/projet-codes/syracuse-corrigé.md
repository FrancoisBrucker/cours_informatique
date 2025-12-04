---
layout: layout/post.njk

title: "Corrigé : Syracuse"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
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

## Fichier `main.py`{.fichier}

```python
from syracuse import suite

sortie_utilisateur = input("Donnez un entier : ")

u_0 = int(sortie_utilisateur)

print("suite de Syracuse associée : ", suite(u_0))

```

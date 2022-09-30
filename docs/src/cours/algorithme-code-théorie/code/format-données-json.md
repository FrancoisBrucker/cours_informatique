---
layout: layout/post.njk 
title: "Formats de données : json"

eleventyNavigation:
  key: "Formats de données : json"
  parent: Code
---

{% prerequis "**Prérequis** :" %}

* [Fichiers](../fichiers)
* [Dictionnaires](../../algorithme/structure-dictionnaire#dictionnaire)

{% endprerequis %}

{% note %}

Le format [json](https://www.json.org/json-fr.html) vient du web. C'est le format idéal pour transférer des données sous la forme d'un texte. Il a de nombreux avantages, citons en deux :

* aisé à lire et modifier sous la forme d'un fichier : pas besoin d'un outil spécial, un simple éditeur de texte suffit.
* aisé à lire et modifier en python : les données json se manipulent sous la forme d'un dictionnaire en python.

{% endnote %}

Ci-après, un exemple de fichier json contenant des super-héros (pris de <https://developer.mozilla.org/fr/docs/Learn/JavaScript/Objects/JSON>) :

```text
[
  {
    "name": "Molecule Man",
    "age": 29,
    "secretIdentity": "Dan Jukes",
    "powers": [
      "Radiation resistance",
      "Turning tiny",
      "Radiation blast"
    ]
  },
  {
    "name": "Madame Uppercut",
    "age": 39,
    "secretIdentity": "Jane Wilson",
    "powers": [
      "Million tonne punch",
      "Damage resistance",
      "Superhuman reflexes"
    ]
  }
]
```

C'est une liste de deux éléments, chaque élément étant composée de *clés* et de *valeurs* comme dans un dictionnaire python. La seule différence est qu'une clé est **toujours** une chaîne de caractère.

## json et dictionnaires en python

Un json c'est **une chaîne de caractère** qui est transformée en données (de type entier, réel, etc). Python utilise nativement le json via sa [bibliothèque json](https://docs.python.org/fr/3/library/json.html).

Un dictionnaire python :

```python
mes_donnees_dictionnaire = {
    "x": [1, 2, 3, 4, 5],
    "y": [-1, -2, -3, -4, -5]
}
```

Se transforme en json (une chaîne de caractère) avec [`json.dumps`](https://docs.python.org/fr/3/library/json.html#json.dumps) :

```python

import json

texte_json = json.dumps(mes_donnees_dictionnaire)

```

Pour le représenter de façon joli, on pourra ajouter les arguments :

```python
print(json.dumps(mes_donnees_dictionnaire, indent=4))
```

Cette chaîne peut à nouveau être transformée en dictionnaire grâce à [`json.loads`](https://docs.python.org/fr/3/library/json.html#json.loads) :

```python
donnees = json.loads(texte_json)

```

## Lecture de fichiers

Pour lire un fichier on utilise la méthode  [`json.load`](https://docs.python.org/fr/3/library/json.html#json.load) (à ne pas confondre avec `json.loads` qui est pour les chaines de caractères).

```python
f = open("data.json", "r")
data = json.load(f)
f.close()

```

Une fois lu, le fichier json est converti en objet python. L'objet `data` est donc une liste composée de deux dictionnaires.

## Écriture de fichiers

Pour lire un fichier on utilise la méthode  [`json.dump`](https://docs.python.org/fr/3/library/json.html#json.dump) (à ne pas confondre avec `json.dumps` qui est pour les chaines de caractères).
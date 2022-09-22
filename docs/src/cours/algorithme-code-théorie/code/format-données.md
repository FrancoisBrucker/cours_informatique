---
layout: layout/post.njk 
title: "Formats de données"

eleventyNavigation:
  key: "Formats de données"
  parent: Code
---

{% prerequis "**Prérequis** :" %}

* [Fichiers](../fichiers)

{% endprerequis %}

Lorsque l'on manipule des données, il vaut mieux **toujours** utiliser un format de stockage connu.

{% note %}
Plutôt que d'écrire simplement un fichier texte contenant nos données, on préférera les structurer dans un format permettant de les relire simplement. On en conseille deux :

* les fichiers csv pour des données de type tableaux excel
* les fichiers json pour des données structurées en fiches.

{% endnote %}

### Fes fichiers csv

Les fichiers [csv](https://fr.wikipedia.org/wiki/Comma-separated_values) sont des fichiers textes permettant de stocker des données structurées comme une feuille excel.

CSV signifie *comma separated values*, donc données séparées par des virgules. Exemple tiré de wikipedia :

```text

Sexe, Prénom, Année de naissance
M, Alphonse, 1932
F, Béatrice, 1964
F, Charlotte, 1988

```

{% faire %}
Créez un fichier nommé *"data.csv"* dans le quel vous copierez le texte précédent.
{% endfaire %}

La première ligne est souvent le noms des colonnes, chaque ligne représentant des données.

python permet de facilement lire des fichiers `csv` sans avoir besoin de tout faire à la main : <https://docs.python.org/fr/3/library/csv.html>

#### Lire un fichier csv

le code ci-après lit le fichier csv et le place dans une liste de listes si la ligne contient bien 3 champs. Puis on convertit le dernier élément en entier.

```python
import csv


donnees = []

f = open("data.csv", "r")
lecteur = csv.reader(f)
for ligne in lecteur:
    donnees.append(ligne)
```

1. `import csv` pour pouvoir utiliser le module `csv`
2. ouvrir le fichier à lire avec `open`
3. placez ce fichier dans un `reader` dont le but est de lire le fichier et de le structurer en utilisant ses paramètres. Il possède [plusieurs options](https://docs.python.org/fr/3/library/csv.html#csv-fmt-params) utiles :
    * `delimiter`. Par défaut c'est des `','`, mais on verra souvent en France des csv dont le délimiteur est un `';'` (car les virgules sont déjà utilisés pour les nombres réels)
    * `quotechar` : pour savoir ce qui est une chaîne de caractères, souvent des `"`. Si vous ne mettez rien, tout sera considéré comme des chaîne de caractères et il faudra convertir à la main chaque donnée si nécessaire
4. lire le fichier ligne à ligne. A chaque utilisation vous obtiendrez une liste contenant les différents champs de la ligne lue.

#### Lire une ligne d'un fichier csv

Pour lire une unique ligne, on peut utiliser la commande `next`. Le code suivant lit la première ligne, qui est un titre, puis lit les autres données en transformant le dernier champ en `int`.

{% note %}
Cette technique permet de séparer le traitement des *méta-données* (le nom des colonnes) du reste (les données). 
{% endnote %}

```python
import csv


donnees = []

f = open("data.csv", "r")
lecteur = csv.reader(f)
titres = next(lecteur)  # lit une unique ligne
for ligne in lecteur:    # continue la lecture
    ligne[2] = int(ligne[2])  # convertie l'année en entier.
    donnees.append(ligne)
```

#### Interpreter du texte comme du csv

Le lecteur de csv fonctionne avec tout [itérateur](https://docs.python.org/fr/3.7/glossary.html#term-iterator). Il fonctionne donc aussi avec une liste de chaînes de caractères.

L'exemple suivant, reprend notre exemple précédent mais suppose que l'on a un texte plutôt qu'un fichier.

```python
text = """
Sexe, Prénom, Année de naissance
M, Alphonse, 1932
F, Béatrice, 1964
F, Charlotte, 1988
"""

lignes = text.splitlines() # une autre méthode utiles des chaines de caractères
lecteur = csv.reader(lignes)

donnees = []
for ligne in lecteur:
    donnees.append(ligne)

```

#### Exercice

L'adresse <https://github.com/hbenbel/French-Dictionary/tree/master/dictionary> contient plusieurs fichiers csv contenant des mots français.

{% exercice %}

1. récupérez le fichier `dictionary.csv` (il est  l'adresse <https://raw.githubusercontent.com/hbenbel/French-Dictionary/master/dictionary/dictionary.csv>)
2. importez le au format csv
3. répondez à cette question existentielle : `nycthémères` est-il un mot français ?

{% endexercice %}
{% details "solution" %}

```python

import csv
import requests

page = requests.get("https://raw.githubusercontent.com/hbenbel/French-Dictionary/master/dictionary/dictionary.csv")
text = page.text

lignes = text.splitlines()

lecteur = csv.reader(lignes)

donnees = []
for ligne in lecteur:
    donnees.append(ligne)

for ligne in donnees:
    if ligne[1] == "nycthémères":
        print("Oui: ", ligne)
```

{% enddetails %}

### Le format json

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

#### json et dictionnaires en python

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

#### Lecture de fichiers

Pour lire un fichier on utilise la méthode  [`json.load`](https://docs.python.org/fr/3/library/json.html#json.load) (à ne pas confondre avec `json.loads` qui est pour les chaines de caractères).

```python
f = open("data.json", "r")
data = json.load(f)
f.close()

```

Une fois lu, le fichier json est converti en objet python. L'objet `data` est donc une liste composée de deux dictionnaires.

#### Écriture de fichiers

Pour lire un fichier on utilise la méthode  [`json.dump`](https://docs.python.org/fr/3/library/json.html#json.dump) (à ne pas confondre avec `json.dumps` qui est pour les chaines de caractères).

### Bibliothèque pandas

Nous ne l'étudierons pas ici, mais la plupart du temps, lorsque l'on utilise des données on ne le fait pas  la main, mais en utilisant une bibliothèque. En analyse des données, on utilise intensivement la bibliothèque [pandas](https://pandas.pydata.org/).

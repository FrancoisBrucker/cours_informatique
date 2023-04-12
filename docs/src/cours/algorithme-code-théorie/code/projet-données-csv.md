---
layout: layout/post.njk 
title: "Formats de données : csv"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "../fichiers/"
---

<!-- début résumé -->

Les fichiers [csv](https://fr.wikipedia.org/wiki/Comma-separated_values) sont des fichiers textes permettant de stocker des données structurées comme une feuille excel.

<!-- fin résumé -->

> TBD : en chantier.

Le format csv est utilisé pour stocker des données sous la forme d'une table où chaque ligne est une donnée composée d'une liste attributs (les colonnes).

{% attention %}
Toutes les données d'un fichier doivent avoir la même structure.
{% endattention %}

## Format csv

Chaque ligne du fichier
> parler des séparateurs, des chaines et des noms des lignes/colonnes

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

## Fichiers csv

CSV signifie *comma separated values*, donc données séparées par des virgules. Exemple tiré de Wikipedia :

```text

Sexe, Prénom, Année de naissance
M, Alphonse, 1932
F, Béatrice, 1964
F, Charlotte, 1988

```

{% faire %}
Créez un fichier nommé `data.csv`{.fichier} dans le quel vous copierez le texte précédent.
{% endfaire %}

La première ligne est souvent le noms des colonnes, chaque ligne représentant des données.

python permet de facilement lire des fichiers `csv` sans avoir besoin de tout faire à la main :

{% lien %}
[Documentation csv python](https://docs.python.org/fr/3/library/csv.html)

{% endlien %}

### Lire un fichier csv

> TBD : newline='' dans la doc ?
> parler du with


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

### Lire une ligne d'un fichier csv

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
    ligne[2] = int(ligne[2])  # convertit l'année en entier.
    donnees.append(ligne)
```

### Écrire des fichiers csv

> TBD : newline='' dans la doc ?
> parler du séparateurs, quotechar

## Exercices

### Dictionnaires

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

### codes postaux

> Téléchargez la base officielle des codes postaux au format csv à partir de la page : <https://www.data.gouv.fr/fr/datasets/base-officielle-des-codes-postaux/>.
{.faire}

En utilisant ce fichier csv :

> 1. Quel est le format de ce fichier ?
> 2. Ouvrez ce fichier et déterminez :
    * A quel code postal est associé la charmante bourgade d'OTTERSWILLER ?
    * donnez sa latitude et longitude (vous pourrez l'admirer en les copiant/collant dans [google maps](https://www.google.fr/maps))
{.faire}

En utilisant le fait que le numéro du département est présent dans le code postal :

> Créez un dictionnaire dont les clés sont le numéro de département et la clé le nombre code postaux différents de ce département.
{.faire}

Puis triez le tout :

> Classez les départements par nombre de code postal
{.faire}

Pour trier les éléments d'un tableau selon un autre ordre que l'ordre *naturel* des éléments d'un tableau, vous pourrez adapter le bout de code suivant :

```python
def trie(x):
    d = {"a": 5, "b": 1, "c": 3}
    return d[x]

l = ["a", "c", "b"]
l.sort()
print(l)

l.sort(key=trie)
print(l)
```

### prénoms

> En utilisant cette page : <https://www.insee.fr/fr/statistiques/2540004?sommaire=4767262>, récupérez le fichier des naissances en France (hors Mayotte) de 1900 à 2020.
{.faire}

En utilisant ce fichier :

>
> 1. Quel le prénom le plus donné chez les garçons et chez les filles en 2020 ?
> 2. Représentez graphiquement l'évolution au cours du temps (de l'année 1900 à 2020) de votre prénom (ou d'un prénom que vous aimez bien)
{.faire}

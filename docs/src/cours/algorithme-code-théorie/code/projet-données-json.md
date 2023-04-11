---
layout: layout/post.njk 
title: "Formats de données : json"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "../fichiers/"
    - "../../algorithme/structure-dictionnaire/"
---

<!-- début résumé -->

Utilisation du format json en python.

<!-- end résumé -->

> TBD : en chantier.

Le format [json](https://www.json.org/json-fr.html) vient du web. C'est le format idéal pour transférer des données sous la forme d'un texte. Il a de nombreux avantages, citons en deux :

* aisé à lire et modifier sous la forme d'un fichier : pas besoin d'un outil spécial, un simple éditeur de texte suffit.
* aisé à lire et modifier en python : les données json se manipulent sous la forme d'un dictionnaire en python.


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



### json

> Téléchargez Informations générales sur les Sénateurs au format json à partir de la page : <https://www.data.gouv.fr/fr/datasets/les-senateurs/>.
{.faire}

Examinez le fichier json :

> 1. Comment sont organisées les données ?
> 2. Quelles sont les données stockées pour chaque sénateur ?
> 3. Combien y a-t-il de sénateurs actifs ?
{.faire}

En utilisant la partie date ci-après :

> Déterminez l'âge moyen des sénateurs encore en activité.
{.faire}

#### dates en python

Lorsque l'on travaille avec des dates en informatique, il ne faut **JAMAIS** le faire à la main. On utilise toujours une bibliothèque pour cela car il y a trop de cas particulier.

En python, cette bibliothèque s'appelle [`datetime`](https://docs.python.org/fr/3.9/library/datetime.html). Pour le sujet qui nous intéresse, on a besoin de transformer une chaine de caractères en date. Ceci est possible avec la méthode [`strptime`](https://docs.python.org/fr/3.9/library/datetime.html#strftime-strptime-behavior).

Si on veut par exemple convertir la date "01/04/2020 à 14h34" en date python, on passe la chaine de caractère et le format à [`strptime`](https://docs.python.org/fr/3.7/library/datetime.html#strftime-strptime-behavior) :

```python
from datetime import datetime

date_en_chaine = "01/04/2020 à 14h34"
format = "%d/%m/%Y à %Hh%M"

date = datetime.strptime(date_en_chaine, format)
```

#### différences de date en python

En python la différence de 2 dates est un objet spécial de type [`timedelta`](https://docs.python.org/fr/3.7/library/datetime.html#timedelta-objects). Par exemple, la différence de temps entre le moment présent et la date précédemment calculée est :

```python

maintenant = datetime.now()  #  la date de maintenant

delta = maintenant - date
```

On peut ensuite connaître le nombre de secondes de cette différence :

```python
delta.total_seconds()
```

Ou le nombre de jours, secondes et microsecondes que cela représente :

```python
delta.days
delta.seconds
delta.microseconds
```
---
layout: layout/post.njk 
title: "Projet : json"

eleventyNavigation:
  key: "Projet : json"
  parent: Code

prerequis:
    - "../fichiers/"
    - "../../algorithme/structure-dictionnaire/"
---

<!-- début résumé -->

Utilisation du format json en python.

<!-- end résumé -->
## formats de données

### csv

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

> TBD : définition / à finaliser.
> faire un exemple plus simple au début.

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
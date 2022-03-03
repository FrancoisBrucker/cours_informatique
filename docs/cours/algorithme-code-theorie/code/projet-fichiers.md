---
layout: page
title:  "projet : fichiers"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [code]({% link cours/algorithme-code-theorie/code/index.md %}) / [projet : fichiers]({% link cours/algorithme-code-theorie/code/projet-fichiers.md %})
>
> **prérequis :**
>
> * [fichiers]({% link cours/algorithme-code-theorie/code/fichiers.md %})
>
{: .chemin}

## mise en place

> 1. créez un dossier nommé *"fichiers-donnees"* où vous placerez vos fichiers
> 2. créez un projet vscode dans ce dossier
>
{: .a-faire}

## texte

Utilisez python pour :

> 1. télécharger le comte de Monte-Cristo avec python (<http://www.gutenberg.org/cache/epub/17989/pg17989.txt>),
> 2. sauvegardez le dans un fichier sur votre ordinateur (toujours en utilisant python)
{: .a-faire}

Avec ce fichier :

> Combien de fois est-il question de `Marseille` dans le texte ?
{: A-faire}

## formats de données

### liste de mots

Le fichier `https://data.senat.fr/data/senateurs/ODSEN_GENERAL.json` contient des données générales relatives aux sénateurs (https://www.data.gouv.fr/fr/datasets/les-senateurs/).

> Téléchargez le fichier <https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words> (vient de [ce gist](https://gist.github.com/wchargin/8927565/)) et sauvegardez son contenu dans un fichier que vous nommerez *"words.txt".
{: .a-faire}

En utilisant le fichier *"words.txt*" :

>
> 1. créez une liste contenant tous les mots de ce fichier (vous pourrez utiliser la méthode [`strip`](https://docs.python.org/3/library/stdtypes.html#str.strip) des chaines de caractères pour supprimer les fin delignes à chaque mot.)
> 2. combien de mots du fichier contiennent la chaine de caractères `prout` ? (`"a" in "ab"` rendra `True` en pyhton)
> 3. quels sont ces mots ?
>
{: .a-faire}

### csv

> Téléchargez la base officielle des codes postaux  au format csv à partir de la page : <https://www.data.gouv.fr/fr/datasets/base-officielle-des-codes-postaux/#_>.
{: .a-faire}

En utilisant ce fichier csv :

> A quel code postal est associé la charmante bourgade d'OTTERSWILLER ?
{: .a-faire}

En utilisant le fait que le numéro du département est présent dans le code postal :

> Créez un dictionnaire dont les clés sont le numéro de département et la clé le nombre code postaux différents de ce département.
{: .a-faire}

Puis triez le tout :

>Classez les départements par nombre de code postal
{: .a-faire}

Pour trier les élément d'un tableau selon un autre ordre que l'ordre *naturel* des élément d'un tableau, vous pourrez adapter le bout de code suivant :

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

### json

> Téléchargez Informations générales sur les Sénateurs au format json à partir de la page : <https://www.data.gouv.fr/fr/datasets/les-senateurs/>.
{: .a-faire}

Examinez le fichier json :

> 1. comment sont organisés les données ?
> 2. quelles sont les données stockées pour chaque sénateur ?
> 3. combien y a-t-il de sénateurs actifs ?
{: .a-faire}

En utilisant la partie date ci-après :

> Déterminez l'âge moyen des sénateurs.
{: .a-faire}

#### dates en python

Lorsque l'on travaille avec des date en informatique, il ne faut **JAMAIS** le faire à la main. On utilise toujours une bibliothèque our cela car il y a trop de cas particulier.

En python, cette bibliothèque s'appelle [`datetime`](https://docs.python.org/fr/3.9/library/datetime.html). Pour le sujet qui nous intéresse, on a besoin de transformer une chaine de caractère en date. Ceci est possible avec la méthode [`strptime`](https://docs.python.org/fr/3.9/library/datetime.html#strftime-strptime-behavior).

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

On peut ensuite connaitre le nombre de secondes de cette différence :

```python
delta.total_seconds()
```

Ou le nombre de jours, secondes et microsecondes que cela représente :

```python
delta.days
delta.seconds
delta.microseconds
```

## prénoms

> En utilisant cette page : <https://www.insee.fr/fr/statistiques/2540004?sommaire=4767262>, récupérez le fichier des naissances en France (hors Mayotte) de 1900 à 2020.
{: .a-faire}

En utilisant ce fichier :

>
> 1. Quel le prénom le plus donné chez les garçons et chez les filles en 2020 ?
> 2. Représentez graphiquement l'évolution au cours du temps (de l'année 1900 à 2020) de votre prénom (ou d'un prénom que vous aimez bien) au cours du temps
>
{: .a-faire}

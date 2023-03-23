---
layout: layout/post.njk 
title:  "projet : fichiers"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-théorie/index.md %}) / [code]({% link cours/algorithme-code-théorie/code/index.md %}) / [projet : fichiers]({% link cours/algorithme-code-théorie/code/projet-fichiers.md %})
>
> **prérequis :**
>
> * [fichiers]({% link cours/algorithme-code-théorie/code/fichiers.md %})
>
{.chemin}

## mise en place

> 1. créez un dossier nommé *"fichiers-donnees"* où vous placerez vos fichiers
> 2. créez un projet vscode dans ce dossier
>
{.faire}

## texte

### jouons sur les mots

Utilisez python pour :

> 1. télécharger le fichier présent à cette adresse : <https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words>
> 2. sauvegardez le dans un fichier nommé *"words.txt"*  sur votre ordinateur (toujours en utilisant python), dans le dossier *"fichiers-donnees"*.
{.faire}

Le fichier contient une liste de mots, un mot par ligne.

> 1. Combien de mots contient ce fichier ?
> 2. Quel est le 42ème mot du dictionnaire ?
> 3. Combien de mots finissent par 'g' ?
{.faire}

Pour ne pas prendre en compte le caractère à la ligne, vous pourrez utiliser la méthode [strip](https://docs.python.org/fr/3/library/stdtypes.html#str.strip) des chaînes de caractères.

Enfin :

> 1. Combien de mots du fichier contiennent la chaîne de caractères `prout` ? (`"b" in "abc"` rendra `True` en pytnon)
> 2. Quels sont ces mots ?
{.faire}

### le compte de Monte-Cristo

Utilisez python pour :

> 1. Télécharger le comte de Monte-Cristo avec python (<http://www.gutenberg.org/cache/epub/17989/pg17989.txt>),
> 2. Sauvegardez le dans un fichier sur votre ordinateur (toujours en utilisant python)
{.faire}

Avec ce fichier :

> 1. Comptez le nombre de caractères différents utilisés (vous pourrez mettre chaque caractère dans un [ensemble](https://docs.python.org/fr/3/tutorial/datastructures.html#sets)), et affichez les.
> 2. Remplacez tous les caractères qui ne sont pas des lettres (c'est à dire qui ne sont pas dans : `"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÇÉÊÎÔàâçèéêëîïôùû"`) par des espaces (vous pourrez utiliser la méthode [replace](https://docs.python.org/fr/3/library/stdtypes.html#str.replace))
> 3. En déduire le nombre de mots utilisés (vous pourrez utiliser la méthode [split](https://docs.python.org/fr/3/library/stdtypes.html#str.split))
> 4. En déduire le nombre de mots **différents** utilisés (vous pourrez utiliser la méthode [split](https://docs.python.org/fr/3/library/stdtypes.html#str.split))
{.faire}

Comptons en utilisant ce que l'on a fait précédemment :

> 1. Combien de fois chaque mot est-il utilisé dans le texte (utilisez un dictionnaire où les mots seront les clés et la valeur le nombre de fois ou ce mot est vue)? 
> 2. Est-il question de `Marseille` dans le texte ? Et si oui, combien de fois ?
> 3. Quelle est le mot qui revient le plus souvent ?
> 4. Quels sont les mots qui reviennent au moins $\frac{n}{2}$ fois où $n$ est le nombre de fois où apparaît le mot le plus fréquent.
{.faire}

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

## prénoms

> En utilisant cette page : <https://www.insee.fr/fr/statistiques/2540004?sommaire=4767262>, récupérez le fichier des naissances en France (hors Mayotte) de 1900 à 2020.
{.faire}

En utilisant ce fichier :

>
> 1. Quel le prénom le plus donné chez les garçons et chez les filles en 2020 ?
> 2. Représentez graphiquement l'évolution au cours du temps (de l'année 1900 à 2020) de votre prénom (ou d'un prénom que vous aimez bien)
{.faire}

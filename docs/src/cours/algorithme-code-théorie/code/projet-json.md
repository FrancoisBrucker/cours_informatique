---
layout: layout/post.njk 
title: "Projet : json"

eleventyNavigation:
  key: "Projet : json"
  parent: Code
---

{% prerequis "**Prérequis** :" %}

* [fichiers](../fichiers)
* [dictionnaires](../../algorithme/structure-dictionnaire)

{% endprerequis %}

<!-- début résumé -->

Utilisation du format json en python.

<!-- end résumé -->

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

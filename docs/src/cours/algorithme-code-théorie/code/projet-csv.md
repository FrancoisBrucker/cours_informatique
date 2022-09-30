---
layout: layout/post.njk 
title: "Projet : csv"

eleventyNavigation:
  key: "Projet : csv"
  parent: Code
---

{% prerequis "**Prérequis** :" %}

* [fichiers](../projet-fichiers)

{% endprerequis %}

<!-- début résumé -->

Utilisation du format de données csv.

<!-- end résumé -->

> TBD : définition / à finaliser.


## csv

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

## prénoms

> En utilisant cette page : <https://www.insee.fr/fr/statistiques/2540004?sommaire=4767262>, récupérez le fichier des naissances en France (hors Mayotte) de 1900 à 2020.
{.faire}

En utilisant ce fichier :

>
> 1. Quel le prénom le plus donné chez les garçons et chez les filles en 2020 ?
> 2. Représentez graphiquement l'évolution au cours du temps (de l'année 1900 à 2020) de votre prénom (ou d'un prénom que vous aimez bien)
{.faire}

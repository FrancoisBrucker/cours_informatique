---
layout: layout/post.njk

title: Projet chemins de longueur minimum
authors: 
    - François Brucker

eleventyNavigation:
  key: "Projet chemins de longueur minimum"
  parent: "Graphes"
---

<!-- début résumé -->

Application du problème de la recherche de chemins de longueur minimum.

Nous allons dans ce projet utiliser deux bibliothèques d'analyse des données très utilisées :

* [pandas](https://pandas.pydata.org/) pour la gestion des données sous forme de matrices nommées [dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
* [geopandas](https://geopandas.org/en/stable/) qui ajoute à pandas la gestion de données géographiques

Nous n'allons pas expliquer tous les tenants et aboutissants de ces bibliothèques mais j'espère que le fait de les utiliser vous donnera envie d'en savoir plus.

<!-- fin résumé -->

Le but de ce projet est de créer un graphe regroupant de grandes villes françaises et de créer des arêtes entres elles par proximité. Une fois ce graphe créé, on pourra implémenter les algorithmes Dijkstra et $A^\star$ pour voir leurs différences de traitement des deux problèmes.

{% faire %}

1. Créer un dossier nommé `projet-chemin-min`{.fichier}. C'est là que nous allons mettre tous les fichiers du projet.
2. Ouvrez le projet soit :
   * dans vscode (`menu fichier > ouvrir le dossier...`)
   * dans un notebook

{% endfaire %}

## Les données

Nous utilisons le fichier [`villes_france_30000.csv`](./villes_france_30000.csv) qui contient une liste des 30000 plus grandes villes françaises au format csv.

{% faire %}
Téléchargez le fichier [`villes_france_30000.csv`](./villes_france_30000.csv) et placez le dans votre projet.

Vous pouvez regarder le fichier dans vscode (Installez le plugin [Rainbow csv](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) pour visualiser plus facilement les fichiers csv)
{% endfaire %}

{% attention %}
Si vous ouvrez ce fichier directement avec un excel français, cela ne fonctionnera pas correctement car le séparateur de champ est le `;` pour un excel en langue française (la `,` étant le séparateur de décimal). C'est en revanche bien la  `,` pour un excel en langue anglaise.

Ceci se produit également lorsque vous exportez des fichiers... Donc faites attention à ce que vos import/export soient correct.
{% endattention %}

### Installation des bibliothèques

Nous allons utiliser python pour lire et traiter ces données. Commençons donc par installer les bibliothèques qui nous serons nécessaires. Dans un terminal de vscode, tapez :

```
python -m pip install pandas geopandas
```

Dans les fichiers python utilisant pandas et geopandas, on commencera toujours par les importer avec les lignes suivantes :

```python
import geopandas as gpd
import pandas as pd
```

{% faire %}
Créez un fichier `main.py` où l'on placera tout le code. Copiez/collez y les deux lignes précédentes.
{% endfaire %}

### Lecture des données

{% faire %}
Testez les codes suivant pour vérifier que vous avez bien lu les données
{% endfaire %}

#### Lecture du fichier dans un data frame

```python
df = pd.read_csv("./villes_france_30000.csv")
```

#### Aperçu du contenu

```python
print(df)
```

{% info %}
Si vous voulez voir le fichier en entier `print(df.to_string())`{.language-}
{% endinfo %}

#### Types des colonnes

Un dataframe est une sorte de tableau excel où chaque ligne a un type. Il est crucial de toujours vérifier que les types des colonnes sont bien ce qu'ils devraient être. Un type incorrect est souvent le signe d'un mauvais chargement ds données :

```python
print(df.columns)
print(df.dtypes)
```

Vous devez obtenir le fait que :

* les colonnes `idx`, `INSEE` et `population` doivent être des entiers,
* les colonnes `latitude` et `longitude` doivent être des réels,
* la colonne `nom` doit être une chaine de caractère (nommé `object` en pandas)

```
idx              int64
 INSEE           int64
 nom            object
 latitude      float64
 longitude     float64
 population      int64
dtype: object
```

## Données géographiques

> TBD la suite
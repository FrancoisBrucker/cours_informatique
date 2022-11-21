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
import pandas as pd
import geopandas as gpd
```

{% faire %}
Créez un fichier `main.py` où l'on placera tout le code. Copiez/collez y les deux lignes précédentes.
{% endfaire %}

### Lecture des données

{% faire %}
Testez les codes suivants pour vérifier que vous avez bien lu les données
{% endfaire %}

#### Lecture du fichier dans un data frame

```python
df = pd.read_csv("./villes_france_30000.csv", skipinitialspace=True)
```

{% note %}
On a créé un *dataframe* pandas qui contient nos données.

On a utilisé le paramètre `skipinitialspace`{.language-}  de la méthode [`read_csv`{.language-} de pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) pour avoir bien des villes qui ne commencent pas par des espaces.
{% endnote %}

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
* la colonne `nom` doit être une chaîne de caractère (nommé `object` en pandas)

```
idx              int64
 INSEE           int64
 nom            object
 latitude      float64
 longitude     float64
 population      int64
dtype: object
```

{% info %}

Le [code INSEE](https://fr.wikipedia.org/wiki/Code_officiel_g%C3%A9ographique) n'est pas le code postal. Voir [ce lien](http://www.bevernage.com/curiosites/cp_insee.htm) par exemple pour en saisir les différences (et, au passage, faire un voyage dans le temps au niveau du site web).

{% endinfo %}

{% exercice %}
Quel est le code INSEE de la ville de Marseille ?
{% endexercice %}

{% details "solution" %}

Solution par morceaux :

1. récupérer une colonne avec pandas : `df["nom"]`{.language-}
2. afficher un résumé de la colonne : `print(df["nom"])`{.language-} (si on veut tout afficher, il faut commencer par transformer la colonne en chaîne de caractère : `print(df["nom"].to_string())`{.language-})
3. récupérer les colonnes dont le com est marseille : `df["nom"] == "Marseille"`{.language-}. C'est une liste de booléen
4. récupérer les lignes dont le nom est marseille : `df[df["nom"] == "Marseille"]`{.language-}

Solution finale :

```python
print(df[df["nom"] == "Marseille"])
```

{% enddetails %}

## Données géographiques

Nos données contiennent à la fois des données :

* *normales* comme le nom u la population pour chaque ville
* géographes avec la latitude et la longitude

Pour pouvoir utiliser les données géographiques de façon efficace, on a l'habitude de les regrouper en classes particulières. Toutes les classes et possibles et leurs utilisations sont décrites dans la bibliothèque [Shapely](https://shapely.readthedocs.io/). Citons en 3 parmi le plus utilisées :

* [des points](https://shapely.readthedocs.io/en/stable/manual.html#points) pour nos coordonnées GPS
* [des Polygones](https://shapely.readthedocs.io/en/stable/manual.html#polygons) pour des surfaces connexes comme des arrondissements (pour les pays non connexes comme la France on utilisera des [collections de polygone](https://shapely.readthedocs.io/en/stable/manual.html#collections-of-polygons))
* [lignes](https://shapely.readthedocs.io/en/stable/manual.html#linestrings) pour des chemins.

De plus, on utilise la bibliothèque GeoPandas (que vous avez déjà du installer) pour une utilisation aise de celle-ci.

### Points à partir des coordonnées

On va créer un *GeoDataFrame* qui contient nos données.

La différence avec un DataFrame pandas est l'ajout d'une colonne `geometry` (**obligatoire** en geopandas) qui contient... La géométrie de nos données. Dans notre cas :

* géométrie est un point (longitude, latitude)
* le système de coordonnée est le système gps : <https://epsg.io/4326>

Faisons ça :

```python
# ...

villes = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))
villes.set_crs("EPSG:4326")
```

{% attention %}
Il est crucial de toujours bien renseigner le système de coordonnées ([CRS](https://www.youtube.com/watch?v=xJyJlKbZFlc&list=PLewNEVDy7gq3DjrPDxGFLbHE4G2QWe8Qh&index=8) pour Coordinate Reference Systems) lorsque l'on traite de données géographiques.
{% endattention %}

### Représentation graphique

On utilise le [tutoriel matplotlib]({{ "/tutoriels/matplotlib" | url }}) pour représenter graphiquement nos villes :

```python
# ...

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))

villes.plot(ax=ax)

plt.show()
```

{% exercice %}
Représentez graphiquement les villes de plus de 50000 habitants.
{% endexercice %}
{% details "solution" %}

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))

villes[villes["population"] > 50000].plot(ax=ax)

plt.show()
```

{% enddetails %}

{% exercice %}
Combien y en a-t-il ?
{% endexercice %}
{% details "solution" %}

```python
print(len(villes[villes["population"] > 50000]))
```

{% enddetails %}

### Supprimons l'île de France

On le voit sur la représentation graphique, l'île de France regroupe trop de granges villes par rapport au reste de la France métropolitaine : on va supprimer toutes les villes de l'île de France sauf Paris.

Pour cela, commençons par trouver l'île de France.

{% exercice %}
Utilisez [cet outil](http://norbertrenner.de/osm/bbox.html) pour déterminer un rectangle (une *bounding box*) englobant l'île de France

{% endexercice %}
{% details "solution" %}

En très gros grain j'obtiens un polygone (avant dernier résultat) valant : `2.02,48.7,2.72,48.98`.

![bounding box de l'île de France](./bbox-île-defrance.png)

{% enddetails %}

Il faut transcrire ce rectangle en coordonnées géographique. Ceci est facile avec la bibliothèque shapely. On peut utiliser [`shapely.geometry.box`{.language-}](https://shapely.readthedocs.io/en/stable/manual.html#shapely.geometry.box) dont les paramètres correspondant à la deuxième ligne du site déterminant les bounding box. Avec mes coordonnées ça fait :

```python
import shapely.geometry

île_de_France = shapely.geometry.box(2.02, 48.7, 2.72, 48.98)

```

On peut maintenant utiliser la puissance de GeoPandas et de ses outils de gestion géographique. Ces outils sont principalement des méthodes de la classe [`GeoSeries`{.language-}](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries) qui correspond à la colonne geometry.

{% exercice %}

En utilisant la méthode [`GeoSeries.within()`](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.within.html), déterminez le nombre de villes de plus de 50000 habitants en île de France (ou tout du moins dans votre *bounding box*).
{% endexercice %}
{% details "solution" %}

```python
print(len(villes[villes["geometry"].within(île_de_France)]))
```

{% enddetails %}

{% exercice %}
En déduire le nombre (et les noms) des villes de plus de 50000 habitants de l'île de France.

{% endexercice %}
{% details "solution" %}

On peut procéder de 2 façons. La plus simple est de commencer par extraire les villes de l'île de france, puis de ne garder que celle de plus de 50000 habitants :

```python
v2 = villes[villes["geometry"].within(île_de_France)]
print(v2[v2["population"] > 50000])
print(len(v2[v2["population"] > 50000]))

```

Mais on peut aussi faire mieux et combien les 2 requêtes par un ET logique (qui se dit `&`{.language-} en pandas et geopandas) :

```python
print(villes[villes["geometry"].within(île_de_France) & (villes["population"] > 50000)])
print(len(villes[villes["geometry"].within(île_de_France) & (villes["population"] > 50000)]))
```

On retrouve bien les même villes, ouf.
{% enddetails %}

On finalise le tout en gardant Paris :

```
v2 = villes[(~villes.geometry.within(île_de_France)) | (villes["nom"] == "Paris")]
grandes_villes = v2[v2["population"] > 50000]
```

En les représentant graphique, j'obtiens :

![grosses_villes](./grandes_villes.png)

### Fond de cartes

> TBD : à faire ?

## Graphe des grandes villes

On va créer un graphe :

* dont les sommets sont les villes de Métropole (hors île de France) de plus de 50000 habitants
* il y a une arête entre la ville $x$ et la ville $y$ si la distance entre les deux est inférieure à `MAX_DIST`{.language-}


### connexité ?

### Dijkstra et $A^\star$

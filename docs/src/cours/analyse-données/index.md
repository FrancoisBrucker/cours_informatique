---
layout: layout/post.njk

title: Analyse de données
tags: ["cours", "données", "viz", "python"]
authors:
  - "François Brucker"
resume: "Cours d'analyse des données. Il comporte deux parties, l'une consacrée à l'analyse _classique_ de données décrites par des attributs réels et l'autre consacrée à la visualisation de données."

eleventyNavigation:
  prerequis:
    - "/cours/coder-et-développer/bases-python/"
    - "/tutoriels/matplotlib/"
    - "/cours/coder-et-développer/ordinateur-développement/terminal/"
    - "/cours/coder-et-développer/environnements-virtuels/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Cours d'analyse des données. Il comporte deux parties, l'une consacrée à l'analyse _classique_ de données décrites par des attributs réels et l'autre consacrée à la visualisation de données.

## Rappel

Il est important que vous ayez compris les bases sur lesquels nous allons coder nos analyses. Ce n'est pas un cours de code, mais comprendre ce que l'on fait vous permettra de créer des analyses plus fines.

{% attention %}
Vérifiez que vous avez bien les prérequis en les relisant.
{% endattention %}

En particulier on suppose que :

1. vous savez ce qu'est un interpréteur python et comment lui ajouter des modules
2. vous savez utiliser soit jupyterlab soit vscode

{% info %}
Ces bases vous seront suffisantes pour utiliser des méthodes d'analyses de données déjà codées et faire de toutes petites fonctions. Si avez besoin d'écrire des fonctions plus grosses, il vous faudra apprendre à écrire des tests et connaître l'outil de de debug de python. Toutes ces notions sont développées dans [le cours de développement](/cours/coder-et-développer/){.interne}

{% endinfo %}

## <span id="packages-nécessaires"></span>Installation des modules pythons

{% info %}
Il pourra être utile d'installer les différents modules python dans [un environnement virtuel](/cours/coder-et-développer/environnements-virtuels/){.interne}.
{% endinfo %}

Le cours est sous la forme de notebooks Jupyter. Téléchargez le fichier de cours et utilisez le via Jupyter notebook (avec vscode ou autre)

```shell
python -m pip install jupyterlab
```

{% info %}
Si la commande précédente ne fonctionne pas (sous mac avec brew par exemple), il vous faudra sûrement ajouter le paramètre `--break-system-packages`.
{% endinfo %}

Puis :

```shell
python -m jupyter lab
```

{% info %}
Si la commande précédente ne fonctionne pas (sous mac avec brew par exemple), il vous faudra sûrement commencer par construire jupyterlab : `python -m jupyter lab build`.
{% endinfo %}

Vous aurez besoin d'installer :

{% note "modules à installer" %}

- [pandas](https://pandas.pydata.org/) : `python -m pip install pandas`
- [seaborn](https://seaborn.pydata.org/) : `python -m pip install seaborn`
- [scikit-learn](https://scikit-learn.org/stable/) : `python -m pip install scikit-learn`

{% endnote %}
> TBD : `scikit-learn` et `statsmodels`. Autre truc ?

{% info %}

Si sous windows vous n'arrivez pas à faire fonctionner matplotlib malgré le fait que vous l'ayez installé, essayez d'installer les [bibliothèques DLL de visual C++](https://pypi.org/project/msvc-runtime/) : `python -m pip install msvc-runtime`.

{% endinfo %}

## <span id="pandas"></span>Utilisation de pandas

{% info %}
L'ensemble des notebooks est disponible à [cette adresse](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/analyse-donn%C3%A9es/notebooks-analyse).

Vous pouvez utiliser cette url <https://download-directory.github.io/> pour télécharger le dossier.
{% endinfo %}

> TBD : tuto jupyterlab

Quelques moyens utile de manipuler des jeux de données avec la [bibliothèque pandas](https://pandas.pydata.org/docs/index.html).

0. jeu de données utilisé [naissances en France en 2020](./notebooks-analyse/nat2020_csv.zip){.fichier}
1. [Premières manipulations](./notebooks-analyse/1_1_1_cours_premières_manipulations.ipynb){.fichier}
2. [Accéder à des données d'un dataframe](./notebooks-analyse/1_2_cours_acceder_aux_dataframe.ipynb){.fichier}
3. [Lecture de données](./notebooks-analyse/1_3_1_cours_lecture_données.ipynb){.fichier}

{% exercice "**A vous**" %}

Deux notebooks à remplir en utilisant ce que vous avez vu en cours :

1. [premières manipulations](./notebooks-analyse/1_1_2_à_vous_premières_manipulations.ipynb){.fichier}
2. [Lecture d'un dataframe](./notebooks-analyse/1_3_2_à_vous_lecture_données.ipynb){.fichier}

{% endexercice %}
{% details "corrigé" %}

1. [premières manipulations](./notebooks-analyse/1_1_3_corrigé_premières_manipulations.ipynb){.fichier}
2. [Lecture d'un dataframe](./notebooks-analyse/1_3_3_corrigé_lecture_données.ipynb){.fichier}

{% enddetails %}

## <span id="data-viz"></span>Visualisation de données

Cette partie du cours est consacrée aux données cartographiques, et comment les utiliser pour faire des visualisations de données.

{% info %}
L'ensemble des notebooks est disponible à [cette adresse](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/analyse-donn%C3%A9es/notebooks-dataviz).

Vous pouvez utiliser cette url <https://download-directory.github.io/> pour télécharger le dossier.
{% endinfo %}

Nous aurons besoin de plusieurs bibliothèques python pour cette partie du cours :
{% faire %}

Créez vous un environnement virtuel et, en plus [des packages précédents](./#packages-nécessaires){.interne} installez les packages suivants :

- [`geopandas`{.language}](https://geopandas.org/en/stable/) pour la gestion des données cartographiques : `python -m pip install geopandas`
- [`geodatasets`{.language}](https://geodatasets.readthedocs.io/) pour la gestion des données cartographiques : `python -m pip install geodatasets`
- [`contextily`{.language}](https://contextily.readthedocs.io/) pour les fond de cartes : `python -m pip install contextily`
- [`osmnx`{.language-}](https://github.com/gboeing/osmnx) qui permet de récupérer des données d'<https://www.openstreetmap.fr/> et de les structurer sous la forme d'un graphe en utilisant la biliothèque [`networkx`{.language-}](https://networkx.org) : `python -m pip install osmnx`
- [`scikit-learn`{.language-}](https://scikit-learn.org/) qui permettra de faire des calculs sur nos graphes: `python -m pip install scikit-learn`
- [`folium`{.language}](https://python-visualization.github.io/folium/) pour gérer rapidement des cartes : `python -m pip install folium`
- [`mapclassify`{.language}](https://pysal.org/mapclassify/) pour utiliser la méthode [`explore`{.language}](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.explore.html) de GeoPandas : `python -m pip install mapclassify`

{% endfaire %}

{% details "sous anaconda" %}
Pour installer tous les packages nécessaire pour ce cours (anaconda ne les connaît pas a priori), on va utiliser le terminal. Pour activer un terminal configuré pour fonctionner avec anaconda il faut :

1. dans anaconda-navigator allez dans la partie [environnement](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/)
2. ouvre un terminal en [cliquant sur le triangle vert](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/#using-an-environment) de l'environnement _base (root)_.

Une fois dans le terminal on peut installer nos packages :

1. _étape facultative_ : mettre à jour conda. Tapez la commande : `conda update --all`
2. installez les bibliothèques nécessaires avec `pip`.

{% enddetails %}

### <span id="data-viz-bases"></span>Base de la cartographie

{% lien %}
<https://geojson.io/>
{% endlien %}

1. [Cartes de géographie](./notebooks-dataviz/1_1_cours_cartes_de_géographies.ipynb){.fichier}
2. [CRS](./notebooks-dataviz/1_2_cours_crs.ipynb){.fichier}
3. [GeoPandas](./notebooks-dataviz/1_3_cours_geopandas_manipulations.ipynb){.fichier}

{% exercice %}

[carte chloroplète](1_4_a_vous_création_données_géographiques.ipynb){.fichier} (vous aurez besoin du jeu de données [villes_france_30000.csv](./notebooks-dataviz/villes_france_30000.csv){.fichier}).
{% endexercice %}
{% details "corrigé" %}

[carte chloroplète](1_5_corrigé_création_données_géographiques.ipynb){.fichier}
{% enddetails %}

### <span id="data-viz-OSM"></span>Données géographiques

{% lien %}
[OSM](https://www.openstreetmap.fr/)
{% endlien %}

1. [requêtes OSM](./notebooks-dataviz/2_1_cours_OSM_requêtes.ipynb){.fichier}
2. [réseau routier](./notebooks-dataviz/2_2_cours_OSM_réseau_routier.ipynb){.fichier}

<div id="data-viz-exercice"></div>

{% exercice "**A vous**" %}

[Données cartographiques](./notebooks-dataviz/2_3_a_vous_données_et_cartes.ipynb){.fichier} (vous aurez besoin du jeu de données [arrondissements.geojson](./notebooks-dataviz/arrondissements.geojson){.fichier})
{% endexercice %}

### <span id="data-viz-2D"></span>Autres représentations

1. [Réduction de dimensions](./notebooks-analyse/4_1_cours_reduction_de_dimensions.ipynb){.fichier}
2. [Méthode de partitionnement, les $k$-means](./notebooks-analyse/4_2_cours_partitionnement.ipynb){.fichier} (téléchargez [les données](./notebooks-analyse/ruspini.csv){.fichier})
3. [Méthodes hiérarchiques](./notebooks-analyse/4_4_cours_hierarchies.ipynb){.fichier} (téléchargez [les données](./notebooks-analyse/henley.mat){.fichier})

{% exercice "A vous" %}

1. [Méthode de partitionnement et réduction de dimensions](./notebooks-analyse/4_3_1_a_vous_kmeans.ipynb){.fichier}
2. [Hiérarchies et MDS](./notebooks-analyse/4_5_1_a_vous_hierarchies_et_mds.ipynb){.fichier}

{% endexercice %}
{% details "corrigé" %}

1. [Méthode de partitionnement et réduction de dimensions](./notebooks-analyse/4_3_2_corrigé_kmeans.ipynb){.fichier}
2. [Hiérarchies et MDS](./notebooks-analyse/4_5_2_corrigé_hierarchies_et_mds.ipynb){.fichier}
   {% enddetails %}

Les deux exercices suivant utilisent les méthodes de partitionnement, de MDS et hiérarchiques pour des données images ou textes. Ils montrent que l'on peut utiliser ces méthodes de façon astucieuses et/ou rigolotes.
{% exercice "Pour aller plus loin" %}

1. [$k$-means et images](./notebooks-analyse/4_6_1_a_vous_kmeans_et_images.ipynb){.fichier}
2. [Analyse de textes](./notebooks-analyse/4_7_1_a_vous_texte_et_distance_de_jaccard.ipynb){.fichier}

{% endexercice %}
{% details "corrigé" %}

1. [$k$-means et images](./notebooks-analyse/4_6_2_corrigé_kmeans_et_images.ipynb){.fichier}
2. [Analyse de textes](./notebooks-analyse/4_7_2_corrigé_texte_et_distance_de_jaccard.ipynb){.fichier}

{% enddetails %}

## Méthodes d'analyse des données

{% info %}
L'ensemble des notebooks est disponible à [cette adresse](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/analyse-donn%C3%A9es/notebooks-analyse)
{% endinfo %}

### Statistiques descriptives

0. jeu de données utilisé [épreuve d'analyse des données](./notebooks-analyse/épreuve.txt){.fichier}
1. [Statistiques descriptives](./notebooks-analyse/2_1_1_cours_statistiques_descriptives.ipynb){.fichier}
2. [Régression et corrélation](./notebooks-analyse/2_2_1_cours_régression_et_corrélation.ipynb){.fichier} ([télécharger](./notebooks-analyse/régression-opti.png){.fichier} l'image du notebook)
3. [Autres régressions](./notebooks-analyse/2_3_1_cours_autres_régressions.ipynb){.fichier}

> TBD attentions les nouvelles versions de pandas ne font plus la corrélation si une colonne non numérique. Il faut changer le corrigé en utilisant la dernière version de pandas.

{% exercice "A vous" %}

1. [Statistiques descriptives](./notebooks-analyse/2_1_2_à_vous_statistiques_descriptives.ipynb){.fichier}
2. [Régression et corrélation](./notebooks-analyse/2_2_2_à_vous_régression_et_corrélation.ipynb){.fichier}
3. [Autres régressions](./notebooks-analyse/2_3_2_à_vous_autres_régressions.ipynb){.fichier}

{% endexercice %}
{% details "corrigé" %}

1. [Statistiques descriptives](./notebooks-analyse/2_1_3_corrigé_statistiques_descriptives.ipynb){.fichier}
2. [Régression et corrélation Iris](./notebooks-analyse/2_2_3_corrigé_régression_et_corrélation_iris.ipynb){.fichier} et [Régression et corrélation crimes](./notebooks-analyse/2_2_3_corrigé_régression_et_corrélation_crimes.ipynb){.fichier}
3. [Autres régressions iris](./notebooks-analyse/2_3_3_corrigé_autres_régressions_iris.ipynb){.fichier} et [Autres régressions crimes](./notebooks-analyse/2_3_3°corrigé_autres_régressions_crimes.ipynb){.fichier}

{% enddetails %}

### Analyse en composantes principales

> TBD les preuves

1. [projection](./notebooks-analyse/3_1_cours_projections.ipynb){.fichier} (télécharger [l'image 1](./notebooks-analyse/projection-opti.png){.fichier} et [l'image 2](./notebooks-analyse/projection-données.png){.fichier} du notebook)
2. [ACP](./notebooks-analyse/3_2_1_cours_acp.ipynb){.fichier}
3. [On s'entraîne](./notebooks-analyse/3_2_2_a_vous_dépenses_état.ipynb){.fichier} (téléchargez [les données](./notebooks-analyse/dépense_état.csv){.fichier}) ([corrigé](./notebooks-analyse/3_2_3_corrigé_dépenses_état.ipynb){.fichier})

{% exercice "A vous" %}

1. [une étude fumeuse](./notebooks-analyse/3_3_1_à_vous_une_étude_fumeuse.ipynb){.fichier} (téléchargez [les données](./notebooks-analyse/fume.txt){.fichier})
2. [ACP d'images](./notebooks-analyse/3_3_3_a_vous_données_visages.ipynb){.fichier}

{% endexercice %}
{% details "corrigé" %}

1. [une étude fumeuse](./notebooks-analyse/3_3_2_corrigé_une_étude_fumeuse.ipynb){.fichier}
2. [ACP d'images](./notebooks-analyse/3_3_4_corrigé_données_visages.ipynb){.fichier}

{% enddetails %}

{% faire %}
Faite l'ACP :

- de deux de ses [jeux de données exercices](./notebooks-analyse/données_exercices.zip){.fichier} de ce dossier
- d'un jeu de données à vous.

{% endfaire %}

---
layout: layout/post.njk

title: Analyse de données
tags: ["cours", "données", "viz", "python"]
authors:
  - "François Brucker"

resume: "Cours d'analyse des données. Il comporte trois parties, la première consacrée à la visualisation de données, la seconde à la cartographie et la troisième à l'analyse _classique_ de données décrites par des attributs réels."

eleventyNavigation:
  prerequis:
    - "/cours/coder-et-développer/bases-programmation/"
    - "/cours/coder-et-développer/bases-programmation/notebooks/"
    - "/cours/coder-et-développer/tutoriel-matplotlib/"
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

<!-- 

> TBD : `scikit-learn` et `statsmodels`. Autre truc ?

 -->

{% info %}

Si sous windows vous n'arrivez pas à faire fonctionner matplotlib malgré le fait que vous l'ayez installé, essayez d'installer les [bibliothèques DLL de visual C++](https://pypi.org/project/msvc-runtime/) : `python -m pip install msvc-runtime`.

{% endinfo %}

{% info %}
Si vous avez des "sauts" dans la fenêtre Jupiter lorsque vous faites défiler votre écran : `Settings → Settings Editor → Notebook → Windowing mode → Defer.`
{% endinfo %}

## <span id="pandas"></span>Utilisation de pandas

{% info %}
L'ensemble des notebooks est disponible à [cette adresse](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/analyse-donn%C3%A9es/notebooks/notebooks-pandas).

Vous pouvez utiliser cette url <https://download-directory.github.io/> pour télécharger le dossier.
{% endinfo %}

<!-- 

> TBD : tuto jupyterlab

 -->

Quelques moyens utile de manipuler des jeux de données avec la [bibliothèque pandas](https://pandas.pydata.org/docs/index.html).

1. jeu de données utilisé [naissances en France en 2022](./notebooks/notebooks-pandas/nat2022_csv.zip){.fichier}
2. [Premières manipulations](./notebooks/notebooks-pandas/1_1_cours_premières_manipulations.ipynb){.fichier}
3. [Accéder à des données d'un dataframe](./notebooks/notebooks-pandas/2_cours_acceder_aux_dataframe.ipynb){.fichier}
4. [Lecture de données](./notebooks/notebooks-pandas/3_1_cours_lecture_données.ipynb){.fichier}

{% exercice "**A vous**" %}

Deux notebooks à remplir en utilisant ce que vous avez vu en cours :

1. [premières manipulations](./notebooks/notebooks-pandas/1_2_à_vous_premières_manipulations.ipynb){.fichier}
2. [Lecture d'un dataframe](./notebooks/notebooks-pandas/3_2_à_vous_lecture_données.ipynb){.fichier}

{% endexercice %}
{% details "corrigé" %}

1. [premières manipulations](./notebooks/notebooks-pandas/1_3_corrigé_premières_manipulations.ipynb){.fichier}
2. [Lecture d'un dataframe](./notebooks/notebooks-pandas/3_3_corrigé_lecture_données.ipynb){.fichier}

{% enddetails %}

## <span id="data-viz-pas-carto"></span>Visualisation de données

{% info %}
L'ensemble des notebooks est disponible à [cette adresse](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/analyse-donn%C3%A9es/notebooks/notebooks-dataviz-données).

Vous pouvez utiliser cette url <https://download-directory.github.io/> pour télécharger le dossier.
{% endinfo %}

### Graphiques

{% lien %}

- <https://clauswilke.com/dataviz/>
- <https://seaborn.pydata.org/index.html>

{% endlien %}

{% faire %}
Reprendre les données des naissances et en utilisant le lien ci-dessus représentez-les en utilisant d'autres types de graphique. Il faudra choisir un type de graphique adapté à ce que vous voulez représenter.
{% endfaire %}

<!-- > TBD 

Faire grossir cette partie.
Voir si le livre ci-dessous ne fonctionnerait pas aussi.

> - <https://www.oreilly.com/library/view/visualisation-de-donnees/9798341620735/>
> 
-->

### <span id="data-viz-2D"></span>Réduction de dimension

Représenter ses données en 2 dimensions.

[Réduction de dimensions](./notebooks/notebooks-dataviz-données/1_cours_reduction_de_dimensions.ipynb){.fichier}

L'exercice suivant utilise vise à créer une distance entre texte puis à la représenter en 2-dimensions.

{% exercice %}

1. [Henley et dépenses de l'état](./notebooks/notebooks-dataviz-données/2_1_a_vous_reduction_de_dimensions.ipynb){.fichier}
2. [Analyse de textes](./notebooks/notebooks-dataviz-données/2_3_a_vous_texte_et_distance_de_jaccard.ipynb){.fichier}

{% endexercice %}
{% details "corrigé" %}

1. [Henley et dépenses de l'état](./notebooks/notebooks-dataviz-données/2_2_corrigé_reduction_de_dimensions.ipynb){.fichier}
2. [Analyse de textes](./notebooks-analyse/2_4_corrigé_texte_et_distance_de_jaccard.ipynb){.fichier}

{% enddetails %}

## <span id="data-viz"></span>Visualisation de données cartographiques

{% info %}
L'ensemble des notebooks est disponible à [cette adresse](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/analyse-donn%C3%A9es/notebooks/notebooks-dataviz-cartes).

{% endinfo %}

Cette partie du cours est consacrée aux données cartographiques, et comment les utiliser pour faire des visualisations de données.

Nous aurons besoin de plusieurs bibliothèques python pour cette partie du cours :

{% note "modules" %}

Les modules classiques :

- [pandas](https://pandas.pydata.org/) : `python -m pip install pandas`
- [seaborn](https://seaborn.pydata.org/) : `python -m pip install seaborn`
- [scikit-learn](https://scikit-learn.org/stable/) : `python -m pip install scikit-learn`

Les modules spécifiques aux données cartographiques :

- [`geopandas`{.language}](https://geopandas.org/en/stable/) pour la gestion des données cartographiques : `python -m pip install geopandas`
- [`geodatasets`{.language}](https://geodatasets.readthedocs.io/) pour la gestion des données cartographiques : `python -m pip install geodatasets`
- [`contextily`{.language}](https://contextily.readthedocs.io/) pour les fond de cartes : `python -m pip install contextily`
- [`osmnx`{.language-}](https://github.com/gboeing/osmnx) qui permet de récupérer des données d'<https://www.openstreetmap.fr/> et de les structurer sous la forme d'un graphe en utilisant la biliothèque [`networkx`{.language-}](https://networkx.org) : `python -m pip install osmnx`
- [`folium`{.language}](https://python-visualization.github.io/folium/) pour gérer rapidement des cartes : `python -m pip install folium`
- [`mapclassify`{.language}](https://pysal.org/mapclassify/) pour utiliser la méthode [`explore`{.language}](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.explore.html) de GeoPandas : `python -m pip install mapclassify`

{% endnote %}

{% faire %}

Utilisez ce [fichier `requirement.txt`](./notebooks/notebooks-dataviz-cartes/requirements.txt){.fichier} pour créer [un environnement virtuel](/cours/coder-et-développer/environnements-virtuels/){.interne} contenant déjà tous les modules nécessaires.

{% endfaire %}

### <span id="data-viz-bases"></span>Base de la cartographie

{% lien %}
<https://geojson.io/>
{% endlien %}

1. [Cartes de géographie](./notebooks/notebooks-dataviz-cartes/1_cours_cartes_de_géographies.ipynb){.fichier}
2. [CRS](./notebooks/notebooks-dataviz-cartes/2_cours_crs.ipynb){.fichier}
3. [GeoPandas](./notebooks/notebooks-dataviz-cartes/3_cours_geopandas_manipulations.ipynb){.fichier}

{% exercice %}

[carte chloroplète](./notebooks/notebooks-dataviz-cartes/4_1_a_vous_création_données_géographiques.ipynb){.fichier} (vous aurez besoin du jeu de données [villes_france_métropole_30000.csv.zip](./notebooks/notebooks-dataviz-cartes/villes_france_métropole_30000.csv.zip){.fichier}).
{% endexercice %}
{% details "corrigé" %}

[carte chloroplète](./notebooks/notebooks-dataviz-cartes/4_2_corrigé_création_données_géographiques.ipynb){.fichier}
{% enddetails %}

À vous sans le corrigé :

{% faire %}
Utilisez les données des ressources suivantes :

- [coordonnées geojson de la Réunion](https://github.com/gregoiredavid/france-geojson/tree/master/departements/974-la-reunion)
- [population par canton](https://public.opendatasoft.com/explore/assets/demographyref-france-pop-legale-canton-millesime/)

Créez une carte chloroplète de la réunion avec le nombre d'habitants par canton.

{% endfaire %}

### <span id="data-viz-OSM"></span>Données géographiques

{% lien %}
[OSM](https://www.openstreetmap.fr/)
{% endlien %}

[requêtes OSM](./notebooks/notebooks-dataviz-OSM/1_1_cours_OSM_requêtes.ipynb){.fichier}

<div id="data-viz-exercice"></div>

{% faire %}

[Données cartographiques](./notebooks/notebooks-dataviz-OSM/1_2_a_vous_données_et_cartes.ipynb){.fichier}. {% endfaire %}

### <span id="data-viz-OSM"></span>Chemins

[réseau routier](./notebooks/notebooks-dataviz-OSM/2_1_cours_OSM_réseau_routier.ipynb){.fichier}

## Méthodes d'analyse des données

{% info %}
L'ensemble des notebooks est disponible à [cette adresse](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/analyse-donn%C3%A9es/notebooks-analyse)
{% endinfo %}

### Partitionnement et hiérarchies

1. [Méthode de partitionnement, les $k$-means](./notebooks/notebooks-analyse/4_2_cours_partitionnement.ipynb){.fichier} (téléchargez [les données](./notebooks/notebooks-analyse/ruspini.csv){.fichier})
2. [Méthodes hiérarchiques](./notebooks/notebooks-analyse/4_4_cours_hierarchies.ipynb){.fichier} (téléchargez [les données](./notebooks-analyse/henley.mat){.fichier})

{% exercice "A vous" %}

1. [Méthode de partitionnement et réduction de dimensions](./notebooks/notebooks-analyse/4_3_1_a_vous_kmeans.ipynb){.fichier}
2. [Hiérarchies et MDS](./notebooks/notebooks-analyse/4_5_1_a_vous_hierarchies_et_mds.ipynb){.fichier}

{% endexercice %}
{% details "corrigé" %}

1. [Méthode de partitionnement et réduction de dimensions](./notebooks/notebooks-analyse/4_3_2_corrigé_kmeans.ipynb){.fichier}
2. [Hiérarchies et MDS](./notebooks/notebooks-analyse/4_5_2_corrigé_hierarchies_et_mds.ipynb){.fichier}
   {% enddetails %}

Les deux exercices suivant utilisent les méthodes de partitionnement, de MDS et hiérarchiques pour des données images ou textes. Ils montrent que l'on peut utiliser ces méthodes de façon astucieuses et/ou rigolotes.
{% exercice "Pour aller plus loin" %}

1. [$k$-means et images](./notebooks/notebooks-analyse/4_6_1_a_vous_kmeans_et_images.ipynb){.fichier}
2. [Analyse de textes](./notebooks/notebooks-analyse/4_7_1_a_vous_texte_et_distance_de_jaccard.ipynb){.fichier}

{% endexercice %}
{% details "corrigé" %}

1. [$k$-means et images](./notebooks/notebooks-analyse/4_6_2_corrigé_kmeans_et_images.ipynb){.fichier}
2. [Analyse de textes](./notebooks/notebooks-analyse/4_7_2_corrigé_texte_et_distance_de_jaccard.ipynb){.fichier}

{% enddetails %}

### Statistiques descriptives

0. jeu de données utilisé [épreuve d'analyse des données](./notebooks/notebooks-analyse/épreuve.txt){.fichier}
1. [Statistiques descriptives](./notebooks/notebooks-analyse/2_1_1_cours_statistiques_descriptives.ipynb){.fichier}
2. [Régression et corrélation](./notebooks/notebooks-analyse/2_2_1_cours_régression_et_corrélation.ipynb){.fichier} ([télécharger](./notebooks/notebooks-analyse/régression-opti.png){.fichier} l'image du notebook)
3. [Autres régressions](./notebooks/notebooks-analyse/2_3_1_cours_autres_régressions.ipynb){.fichier}

> TBD attentions les nouvelles versions de pandas ne font plus la corrélation si une colonne non numérique. Il faut changer le corrigé en utilisant la dernière version de pandas.

{% exercice "A vous" %}

1. [Statistiques descriptives](./notebooks/notebooks-analyse/2_1_2_à_vous_statistiques_descriptives.ipynb){.fichier}
2. [Régression et corrélation](./notebooks/notebooks-analyse/2_2_2_à_vous_régression_et_corrélation.ipynb){.fichier}
3. [Autres régressions](./notebooks/notebooks-analyse/2_3_2_à_vous_autres_régressions.ipynb){.fichier}

{% endexercice %}
{% details "corrigé" %}

1. [Statistiques descriptives](./notebooks/notebooks-analyse/2_1_3_corrigé_statistiques_descriptives.ipynb){.fichier}
2. [Régression et corrélation Iris](./notebooks/notebooks-analyse/2_2_3_corrigé_régression_et_corrélation_iris.ipynb){.fichier} et [Régression et corrélation crimes](./notebooks/notebooks-analyse/2_2_3_corrigé_régression_et_corrélation_crimes.ipynb){.fichier}
3. [Autres régressions iris](./notebooks/notebooks-analyse/2_3_3_corrigé_autres_régressions_iris.ipynb){.fichier} et [Autres régressions crimes](./notebooks/notebooks-analyse/2_3_3°corrigé_autres_régressions_crimes.ipynb){.fichier}

{% enddetails %}

### Analyse en composantes principales

> TBD les preuves

1. [projection](./notebooks/notebooks-analyse/3_1_cours_projections.ipynb){.fichier} (télécharger [l'image 1](./notebooks-analyse/projection-opti.png){.fichier} et [l'image 2](./notebooks/notebooks-analyse/projection-données.png){.fichier} du notebook)
2. [ACP](./notebooks/notebooks-analyse/3_2_1_cours_acp.ipynb){.fichier}
3. [On s'entraîne](./notebooks/notebooks-analyse/3_2_2_a_vous_dépenses_état.ipynb){.fichier} (téléchargez [les données](./notebooks/notebooks-analyse/dépense_état.csv){.fichier}) ([corrigé](./notebooks/notebooks-analyse/3_2_3_corrigé_dépenses_état.ipynb){.fichier})

{% exercice "A vous" %}

1. [une étude fumeuse](./notebooks/notebooks-analyse/3_3_1_à_vous_une_étude_fumeuse.ipynb){.fichier} (téléchargez [les données](./notebooks/notebooks-analyse/fume.txt){.fichier})
2. [ACP d'images](./notebooks/notebooks-analyse/3_3_3_a_vous_données_visages.ipynb){.fichier}

{% endexercice %}
{% details "corrigé" %}

1. [une étude fumeuse](./notebooks/notebooks-analyse/3_3_2_corrigé_une_étude_fumeuse.ipynb){.fichier}
2. [ACP d'images](./notebooks/notebooks-analyse/3_3_4_corrigé_données_visages.ipynb){.fichier}

{% enddetails %}

{% faire %}
Faite l'ACP :

- de deux de ses [jeux de données exercices](./notebooks/notebooks-analyse/données_exercices.zip){.fichier} de ce dossier
- d'un jeu de données à vous.

{% endfaire %}

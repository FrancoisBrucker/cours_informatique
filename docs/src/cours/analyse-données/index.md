---
layout: layout/post.njk
title: Analyse de données
tags: ['cours', 'données', 'python']

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Analyse de données"
  parent: "Cours"

prerequis:
    - "/cours/base-code/"
---

<!-- début résumé -->

Cours d'analyse des données. Il comporte deux parties, l'une consacrée à l'analyse *classique* de données décrites par des attributs réels et l'autre consacrée à la visualisation de données.

<!-- fin résumé -->

Le cours est sous la forme de notebooks jupyter. Téléchargez le fichier de cours et utilisez le via jupyter notebook (avec anaconda, vscode ou autre)

## Analyse des données

### Utilisation de pandas

Quelques moyens utile de manipuler des jeux de données avec la [bibliothèque pandas](https://pandas.pydata.org/docs/index.html).

0. jeu de données utilisé [naissances en France en 2020](./notebooks/nat2020_csv.zip)
1. [Premières manipulations](./notebooks/1_1_1_cours_premières_manipulations.ipynb)
2. [Accéder à des données d'un dataframe](./notebooks/1_2_cours_acceder_aux_dataframe.ipynb)
3. [Lecture de données](./notebooks/1_3_1_cours_lecture_données.ipynb)

{% exercice "**A vous**" %}

Deux notebooks à remplir en utilisant ce que vous avez vu en cours :

1. [premières manipulations](./notebooks/1_1_2_à_vous_premières_manipulations.ipynb)
2. [Lecture d'un dataframe](./notebooks/1_3_2_à_vous_lecture_données.ipynb)

{% endexercice %}
{% details "corrigé" %}

1. [premières manipulations](./notebooks/1_1_3_corrigé_premières_manipulations.ipynb)
2. [Lecture d'un dataframe](./notebooks/1_3_3_corrigé_lecture_données.ipynb)

{% enddetails %}

### Statistiques descriptives

0. jeu de données utilisé [épreuve d'analyse des données](./notebooks/épreuve.txt)
1. [Statistiques descriptives](./notebooks/2_1_1_cours_statistiques_descriptives.ipynb)
2. [Régression et corrélation](./notebooks/2_2_1_cours_régression_et_corrélation.ipynb) ([télécharger](./notebooks/régression-opti.png) l'image du notebook)
3. [Autres régressions](./notebooks/2_3_1_cours_autres_régressions.ipynb)

{% exercice "A vous" %}

1. [Statistiques descriptives](./notebooks/2_1_2_à_vous_statistiques_descriptives.ipynb)
2. [Régression et corrélation](./notebooks/2_2_2_à_vous_régression_et_corrélation.ipynb)
3. [Autres régressions](./notebooks/2_3_2_à_vous_autres_régressions.ipynb)

{% endexercice %}
{% details "corrigé" %}

1. [Statistiques descriptives](./notebooks/2_1_3_corrigé_statistiques_descriptives.ipynb)
2. [Régression et corrélation Iris](./notebooks/2_2_3_corrigé_régression_et_corrélation_iris.ipynb) et [Régression et corrélation crimes](./notebooks/2_2_3_corrigé_régression_et_corrélation_crimes.ipynb)
3. [Autres régressions iris](./notebooks/2_3_3_corrigé_autres_régressions_iris.ipynb) et [Autres régressions crimes](./notebooks/2_3_3°corrigé_autres_régressions_crimes.ipynb)

{% enddetails %}

### Analyse en composantes principales

1. [projection](./notebooks/3_1_cours_projections.ipynb) (télécharger [l'image 1](./notebooks/projection-opti.png) et [l'image 2](./notebooks/projection-données.png) du notebook)
2. [ACP](./notebooks/3_2_cours_acp.ipynb)

### Clustering

## Visualisation de données

> TBD
>

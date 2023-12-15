---
layout: layout/post.njk

title: Analyse de données
tags: ['cours', 'données', 'viz', 'python']
authors:
    - "François Brucker"

eleventyNavigation:
  prerequis:
      - "/cours/utiliser-python/"

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Cours d'analyse des données. Il comporte deux parties, l'une consacrée à l'analyse *classique* de données décrites par des attributs réels et l'autre consacrée à la visualisation de données.

<!-- fin résumé -->

Le cours est sous la forme de notebooks jupyter. Téléchargez le fichier de cours et utilisez le via jupyter notebook (avec anaconda, vscode ou autre)

## Méthodes d'analyse des données

{% info %}
L'ensemble des notebooks est disponible à [cette adresse](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/analyse-donn%C3%A9es/notebooks-analyse)
{% endinfo %}

### Utilisation de pandas

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

* de deux de ses [jeux de données exercices](./notebooks-analyse/données_exercices.zip){.fichier} de ce dossier
* d'un jeu de données à vous.

A rendre sur [moodle](https://moodle.centrale-marseille.fr/mod/assign/view.php?id=36079).
{% endfaire %}

### Clustering

1. [Méthode de partitionnement, les $k$-means](./notebooks-analyse/4_1_cours_partitionnement.ipynb){.fichier} (téléchargez [les données](./notebooks-analyse/ruspini.csv){.fichier})
2. [Réduction de dimensions](./notebooks-analyse/4_2_cours_reduction_de_dimensions.ipynb){.fichier}
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

## Visualisation de données

> TBD
>

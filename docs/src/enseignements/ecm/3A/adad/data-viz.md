---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: Analyse des données
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 0

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le cours est basé sur le cours suivant :

{% aller %}
[Cours analyse des données](/cours/analyse-données){.interne}
{% endaller %}

Chaque semaine de cours, un travail est à rendre pour la semaine de cours prochaine (environ un mois après) les rendus sont à rendre sur moodle :

{% attention %}
[adresse des rendus moodle](https://moodle.centrale-med.fr/course/view.php?id=1221)
{% endattention %}

## Semaine 1

Deux cours d'introductions aux méthodes d'analyse des données en python en utilisant la bibliothèque pandas.

Basé sur [la partie utilisation de Panda](/cours/analyse-données/#pandas){.interne}.

### Cours 1

#### 1.1

On vérifie que l'on a les bases nécessaire en python :

- base du langage python
- notion d'interpréteur
- installation de modules
- utilisation de vscode et/ou de jupyterlab (affichage à l'écran et html)
- matplotlib et seaborn

{% aller %}
Vous serez amené à installer tout un tas de modules pour python. Donc ayez intégré comment on manipule un interpréteur :

- [Installer un interpréteur python](/cours/coder-et-développer/installer-python/){.interne}
- [travailler avec un environnement virtuel](/cours/coder-et-développer/environnements-virtuels/){.interne}

{% endaller %}

#### 1.2

Pandas et les premières analyses.

### Rendu

Basées sur les [à vous de la partie utilisation de Panda](/cours/analyse-données/#pandas){.interne}. Vous devrez rendre 2 notebooks :

1. **Premier notebook** : Utilisez un prénom que vous aimez (le votre ?) et procédez à cinq analyses similaires à celles du cours et la partie exercice. Vous devrez pour chaque analyse :
   1. explicitez clairement la question que vous cherchez à résoudre (_e.g._ combien de François par année ?)
   2. donnez le code de résolution
   3. conclure en utilisant le résultat donné par le code
2. **Second notebook** : prenez un jeu de données sur internet au format excel ou csv et importez le avec Pandas (par exemple un des autres jeux de l'Insee. Il en existe plein de différents sur les prénoms par exemple). Il vous faudra :
   1. importer le document sous la forme d'un data frame de la façon la plus claire possible
   2. donner quelques méthodes qui vous permettent de vérifier que vous avez bien importé les bonnes donnés (nombre de lignes, type des colonnes, etc)
   3. Montrer comment accéder à une donnée précise (ligne, colonne)
   4. faire une sélection pertinente de vos données. Pour cela :
      1. explicitez clairement la question que vous cherchez à résoudre (_e.g._ combien de François par année ?)
      2. donnez le code de résolution
      3. conclure en utilisant le résultat donné par le code

{% attention  %}
Le rendu est à rendre sur moodle **avant** le lundi 2 décembre à 9h.
{% endattention  %}

## Semaine 2

Visualisation de cartes. Basé sur [la partie visualisation de Panda](/cours/analyse-données/#data-viz){.interne}.

### Cours 2

#### Environnement virtuel

Commencez par télécharger les différents notebooks puis on va créer un environnement virtuel.

1. création de l'environnement
2. installation des modules classiques
3. installation des modules de dataviz

#### Cartes et CRS

- Qu'est-ce qu'une carte ? Qu'un CRS ?
- représenter graphiquement ses données

#### Trouver des données cartographiques

Utilisation de requêtes OpenStreetMap pour trouver des données géographiques.

### Rendu 2

Rendez **2 des 3 exercices** de [la section **A vous**](/cours/analyse-données/#data-viz-exercice){.interne} (Comptez des trucs à Marseille, France et monde) de la partie visualisation des données.

---
layout: layout/post.njk
title: "S2 : Programmation"

tags: ["formation", "MPCI"]

eleventyNavigation:
  order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Ce cours intitulé _Programmation_ est donné au second semestre de la licence MPCI ([lien AMeTICE AMU Informatique S2](https://ametice.univ-amu.fr/course/view.php?id=129120)). Il s'appuie sur le cours de _Programmation_ donné au S1 ([lien AMeTICE AMU Informatique S1](https://ametice.univ-amu.fr/course/view.php?id=125682)).

Ce cours donnera les bases de développement d'un projet informatique en s'appuyant sur le langage python.

## Note

La note de  l'UE résulte de cette formule :

$$
\max (\frac{CC+ DS + ET}{3}, ET)
$$

Avec :

- $CC = \frac{1}{4}(TUT + \sum TEST)$ où :
  - $TUT$ est la moyenne formée de la note des 2 tutorats
  - $\sum TEST$ est la somme des autres notes de contrôle continu
- $DS$ est la note du devoir surveillé
- $ET$ est l'examen terminal

## Prérequis

Il est nécessaire d'avoir quelques prérequis avant de commencer ce cours, en particulier vos cours d'informatique du S1, en particulier avoir des bases de programmation python.

## Cours

Le cours est disponible via le site d'AMeTICE et en suivant les liens de chaque partie ci-après. Cela ne vous dispense pas de prendre des notes, mais vous aide à la révision ou aux divers prérequis que vous aurez à préparer avant le cours.

## Plan

<!-- TBD 2026/27

Cours en 4 parties et 4 DM :

1. mettre 4h de rappel du semestre précédent pour le code
   1. import
   2. notation  pointée
   3. notion d'espace de nommage
2. cours intro : DM algo : écrire des algorithmes en python et vérifier expérimentalement leur véracité (faire les mono-lignes et des exercices sur les import)
   1. pseudo-code (6h)
   2. projets et tests (4h) 
3. cours algo (complexité) et DM code (test/projet/)
4. cours programmation (objet) et DM algo (et de l'année précédente)
   1. objets :
      1. 1h cours + 1h TD avec moi dés
      2. 2h TD cartes
   2. composition
      1. 1h cours + 1h TD avec moi dés
      2. 2h TD cartes
   3. héritage
      1. 1h cours + 1h TD avec moi dés
      2. 2h TD cartes
5. cours algo (structures de données) et DM code (bataille navale)

-->

### Partie 1


Il est **INDISPENSABLE** que vous ayez en tête ce que vous avez fait en développement au S1. Pour cela, suivez et faite la partie suivante du cours qui explicite les notions qui vous seront utiles pour débuter ce semestre :

{% prerequis "**PRÉREQUIS**" %}
1. [Utilisez le réseau EDUROAM](/enseignements/MPCI/outil-informatique/#eduroam){.interne}
2. [Bases de programmation en python](/cours/coder-et-développer/bases-programmation/){.interne}
{% endprerequis %}

#### Cours : projet de développement

> 2h

Notions abordées :

- base système : dossiers, fichiers et programmes
- utilisation du terminal
- écrire du code python utilisable et maintenable

{% aller %}
1. Rappels : [créer un projet python avec vscode](/cours/coder-et-développer/bases-programmation/éditeur-vscode/){.interne}
2. [Bases de système d'exploitation](/cours/système-et-réseau/bases-système/){.interne}
3. [Modules externes python](/cours/coder-et-développer/modules-externes-python/){.interne}
{% endaller %}

Si on a le temps, sinon à faire chez soit :

{% aller %}
[Tutorial matplotlib](/cours/coder-et-développer/tutoriel-matplotlib/){.interne}
{% endaller %}

> TBD Faire un DM bases python (basé sur les monolignes):
> - variables 
> - listes
> - dictionnaires

#### Exercices

> 4h

{% aller %}
1. [tester son code](/cours/coder-et-développer/tests-unitaires/){.interne}
2. [Développer un projet informatique](/cours/coder-et-développer/écrire-code/tutoriel-hello-dev/){.interne}
3. [Projet pourcentages](/cours/coder-et-développer/projet-pourcentages){.interne}
{% endaller %}

> TBD Supprimer le linter du cours, mais insister sur black.


On s'entraîne :

{% aller %}
[Petits programmes](/cours/coder-et-développer/projet-codes/){.interne} et [on leur ajoute des tests](/cours/coder-et-développer/projet-codes-tests/){.interne}
{% endaller %}

Pour aller plus loin :

{% aller %}
1. [écrire du code lisible et maintenable](/cours/coder-et-développer/écrire-code/coder/){.interne}
2. [déboguer son code](/cours/coder-et-développer/débogueur/){.interne}
{% endaller %}

### Partie 2

> 9/03 au 13/03
> Programmation

#### Cours : programmation objet

> 2h
>

Notions abordées :

- Qu'est-ce qu'un objet ?
- Modélisation UML et en python
- développer un objet grâce à des users stories

{% aller %}

1. [Tout est objet en python](/cours/coder-et-développer/programmation-objet/introduction/){.interne}
2. [Créer ses classes et leurs objets](/cours/coder-et-développer/programmation-objet/classes-et-objets/){.interne}
3. [Coder ses objets](/cours/coder-et-développer/programmation-objet/coder-ses-objets/){.interne}

{% endaller %}

#### On s'entraîne

> 4h
>

{% info %}
Je vous conseille très fortement de faire la séance de code en [pair-programming](https://fr.wikipedia.org/wiki/Programmation_en_bin%C3%B4me). **Lisez** le lien ci-après avant vendredi.
{% endinfo %}
{% lien %}
[comment coder en pair-programming](https://martinfowler.com/articles/on-pair-programming.html)
{% endlien %}

Au programme :

{% aller %}

- [Des dés](/cours/coder-et-développer/programmation-objet/projet-objets-dés/){.interne}
- [Jeu de cartes](/cours/coder-et-développer/programmation-objet/projet-objets-cartes/){.interne}

{% endaller %}
{% note %}
- [corrigé projet dé](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/coder-et-d%C3%A9velopper/programmation-objet/projet-objets-d%C3%A9s/code)
- [corrigé projet cartes](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/coder-et-d%C3%A9velopper/programmation-objet/projet-objets-cartes/code)

{% endnote %}


<!-- TBD 

Modifier les td précédent pour mettre les str et repr directement dans les améliorations.
-->

### Partie 3 : Développer un projet


#### Cours : Composition, agrégation et héritage

> 2h
>

Notions abordées :


- Composer des objet pour développer un projet
- Agrégation
- Composition
- Héritage

Composer des objets entre-eux :

{% aller %}
1. [Améliorer ses objets](/cours/coder-et-développer/programmation-objet/améliorer-ses-objets/){.interne}
2. [Composition et agrégation](/cours/coder-et-développer/programmation-objet/composition-agrégation){.interne}
3. [Héritage](/cours/coder-et-développer/programmation-objet/héritage){.interne}

{% endaller %}

> TBD en faire des DM.

À faire chez soit pour s'entraîner :

{% aller %}

1. [Améliorer les dés](projet-objets-dés-amélioration){.interne}
2. [Projet de compositions de dés](/cours/coder-et-développer/programmation-objet/projet-composition-dés){.interne}
{% endaller %}
{% note %}
- [corrigé d'amélioration des dés](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/coder-et-d%C3%A9velopper/programmation-objet/projet-objets-dés-amélioration/code)
- [corrigé composition de dés](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/coder-et-d%C3%A9velopper/programmation-objet/projet-composition-dés/code)

{% endnote %}


{% aller %}
1. [Améliorer les cartes](/cours/coder-et-développer/programmation-objet/projet-objets-cartes-amélioration/){.interne}
2. [Projet d'agrégation de cartes](/cours/coder-et-développer/programmation-objet/projet-agrégation-cartes){.interne}

{% endaller %}
{% note %}
- [corrigé d'amélioration des cartes](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/coder-et-d%C3%A9velopper/programmation-objet/projet-objets-cartes-amélioration/code)
- [corrigé agrégation de cartes](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/coder-et-d%C3%A9velopper/programmation-objet/projet-agrégation-cartes/code)

{% endnote %}

{% aller %}

[Projet héritage](/cours/coder-et-développer/programmation-objet/projet-héritage){.interne}

{% endaller %}
{% note %}
[corrigé projet héritage](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/coder-et-d%C3%A9velopper/programmation-objet/projet-h%C3%A9ritage/projet-heritage)

{% endnote %}

#### Projet

{% aller %}

1. [gestion des dépendances](/cours/coder-et-développer/gestion-dépendances/){.interne}
2. [gestion du code source](/cours/gestion-des-sources/){.interne} : mettre son code à disposition via un [Dépôt](/cours/gestion-des-sources/dépôt/besoins-dépôt/){.interne}

{% endaller %}

> TBD faire un environnement virtuel pour la bataille navale et trouver une lib à ajouter pour le requirement.txt

{% aller %}

[Bataille Navale](/cours/coder-et-développer/programmation-objet/projet-bataille-navale){.interne}

{% endaller %}
{% note %}
[corrigé projet bataille navale](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/coder-et-d%C3%A9velopper/programmation-objet/projet-bataille-navale/code)

{% endnote %}


Si on a le temps et puisque c'est la dernière séance, pour aller plus loin :

{% aller %}

1. [Gestion de l'évolution de son code source](/cours/gestion-des-sources/évolution-code/besoins-gestion-sources/){.interne}
2. [Partager du code source](/cours/gestion-des-sources/partage/besoins-origin/){.interne}
3. [Bonnes pratiques](/cours/gestion-des-sources/bonnes-pratiques/){.interne} et [outils](/cours/gestion-des-sources/outils){.interne}

{% endaller %}

> TBD à rendre plus propre et à laisser au plus fort.

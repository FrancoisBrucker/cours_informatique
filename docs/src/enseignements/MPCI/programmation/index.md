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

Il est nécessaire d'avoir quelques prérequis avant de commencer ce cours, en particulier vos cours d'informatique du S1, en particulier avoir des bases de programmation python. Tout ce dont on aura besoin est disponible dans le cours cours ci-après :

{% prerequis "**Acquis du S1**" %}
[Fondements de la programmation (avec Python)](/cours/coder-et-développer/apprendre-programmation/concepts/){.interne}
{% endprerequis %}

Programmer nécessite d'utiliser le web pour lire la doc, técharger des modules, etc. Configurez votre ordinateur pour qu'il puisse utiliser le réseau universitaire EDUROAM :

{% lien %}
[Utilisez le réseau EDUROAM](/enseignements/MPCI/outil-informatique/#eduroam){.interne}
{% endlien %}


## Cours

Le cours est disponible via le site d'AMeTICE et en suivant les liens de chaque partie ci-après. Cela ne vous dispense pas de prendre des notes, mais vous aide à la révision ou aux divers prérequis que vous aurez à préparer avant le cours.

## Plan

### Partie 0 : Vérification des acquis

Utilisez [un interpréteur en ligne](https://console.basthon.fr/) ou <[spyder](https://www.spyder-ide.org/)> pour vous rafraîchir la mémoire en python :

{% aller %}
[84 monolignes en python](/cours/coder-et-développer/apprendre-programmation/concepts/mono-lignes/){.interne}
{% endaller %}

Vous devriez être capable de comprendre toutes les solutions et (dans le meilleur des cas) d'en faire une grande partie.

### Partie I : Projets informatique 

#### Interpréteur python et IDE

> 2h cours

{% aller %}
1. Interagir avec le système :
   1. [Naviguer dans un système de fichiers](/cours/système/interagir-avec-système/fichiers-dossiers/){.interne}
   2. [Terminal](/cours/système/interagir-avec-système/terminal/){.interne}
2. [Installer un interpréteur et un IDE](/cours/coder-et-développer/apprendre-programmation/coder-projets/outils/){.interne}
{% endaller %}
{% info %}
[Installer des paquets](/cours/système/interagir-avec-système/gestionnaire-paquets/){.interne}
{% endinfo %}

#### Principe de conduite d'un projet informatique

> 2h TD

Le premier principe fondamental est de séparer le programme principal des fonctions :

{% aller %}
1. Séparer code et fonctions en [créant ses propres modules](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/création-modules/){.interne}
2. On s'entraîne : [Projet : création de modules](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/projet-création-modules/){.interne}

{% endaller %}

Le second principe fondamental est que les tests des fonctions fonts partie du projet :

{% aller %}
1. [Tester ses fonctions](/cours/coder-et-développer/apprendre-programmation/coder-projets/outils/){.interne}
2. [On s'entraîne à écrire des tests](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/projet-codes-tests/){.interne}
{% endaller %}

#### À vous

> 2h TP

{% aller %}
[Bonnes pratiques et mantra](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/bonnes-pratiques/){.interne}
{% endaller %}


{% aller %}
1. [Mise en œuvre d'un projet informatique](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/projet-informatique/){.interne}
2. [Projet pourcentage](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/projet-pourcentages/){.interne}
{% endaller %}

Pour aller plus loin :

{% aller %}
1. [Utiliser le débogueur pour corriger son code](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/débogueur/){.interne}
2. [exercices divers](/cours/coder-et-développer/apprendre-programmation/coder-projets/exercices-tests/){.interne}
{% endaller %}

### Partie II : Programmation Objet

La grosse partie de cette UE.

{% prerequis "**À lire avant la séance**" %}
[Tout est objet en python](/cours/coder-et-développer/apprendre-programmation/programmation-objet/introduction/){.interne}
{% endprerequis %}


#### Classes et objets

> 2h cours

{% aller %}
1. [Classes et objets](/cours/coder-et-développer/apprendre-programmation/programmation-objet/classes-et-objets/){.interne}
2. [Des dés](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-dés/){.interne}
{% endaller %}

> 2h TP

{% aller %}
[Projet cartes](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-cartes/){.interne}
{% endaller %}

#### DM 1 : améliorer ses objets

{% prerequis "**TRavail préparatoire**" %}
1. [Améliorer ses objets](/cours/coder-et-développer/apprendre-programmation/programmation-objet/améliorer-ses-objets/){.interne}
2. [Des dés améliorés](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-dés-amélioration/){.interne}

{% endprerequis %}
{% faire %}
[Cartes améliorées](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-cartes-amélioration/){.interne}
{% endfaire %}

#### Composition et agrégation

> 2h cours

{% aller %}
1. [Composition et agrégation](/cours/coder-et-développer/apprendre-programmation/programmation-objet/composition-agrégation/){.interne}
2. [Des compositions de dés](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-composition-aggrégation-dés/){.interne}
{% endaller %}

> 2h TP

{% aller %}
[Projet cartes et bataille](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-agrégation-cartes/){.interne}
{% endaller %}

#### Héritage

> 2h cours

{% aller %}
1. [Héritage](/cours/coder-et-développer/apprendre-programmation/programmation-objet/héritage/){.interne}
2. [Dés spécifiques](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-dés-héritage/){.interne}
{% endaller %}

> 2h TP

{% aller %}
[Projet Héritage](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-héritage/){.interne}
{% endaller %}

#### DM 2

{% prerequis "**Travail préparatoire**" %}
1. [création d'un environnement virtuel](/cours/coder-et-développer/apprendre-programmation/gestion-dépendances/environnements-virtuels/){.interne} pour ses projets
2. mettre son code à disposition via un [Dépôt](/cours/gestion-des-sources/dépôt/){.interne} sur github.

{% endprerequis %}


{% faire %}

Rendre le projet [Bataille Navale](/cours/coder-et-développer/programmation-objet/projet-bataille-navale){.interne}. 

Les consignes sont :

- le projet doit se trouver sur github
- mettre de la couleur dans vos sorties en utilisant le module <https://github.com/termcolor/termcolor>
- il doit fonctionner avec un environnement virtuel : le fichier `requirements.txt`{.fichier} est requis


{% endfaire %}


## Annales

Le cours était lié au cours d'algorithmie. Les annales concernent donc les 2 matières. Prenez celle qui concerne la programmation.

{% lien %}
[Annales du cours programmation et algorithmes](../programmation-algorithmes/annales/)
{% endlien %}



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

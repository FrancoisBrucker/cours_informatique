---
layout: layout/post.njk 
title: Programmation Orientée Objet en Python

tags: ['formation', 'ECC']

eleventyNavigation:
  key: ECC
  parent: Enseignements
  order: 2

---

Cet enseignement est organisé en 3 types d'enseignements :

* 1 séance d'autonomie pour s'auto-former
* 5 séances de cours pour acquérir de nouvelles connaissances
* 8 séances machines pour s'entraîner, accompagné d'un professeur ou d'un corrigé

A l'issue de cet enseignement, l'élève aura de solides connaissance en programmation orientée objet et saura mener à bien un projet de développement en python.

## Notation

La notation de cet enseignement sera composée d'un projet à rendre par équipe de 4 élèves maximum.

## Programme

En plusieurs parties.
<div id="partie-0"></div>

### Partie 0 : prérequis

{% note %}
Vérifiez que vous avez les prérequis pour suivre l'enseignement. S'il vous manque des connaissances, suivez les tutoriels et si vous avez encore des doutes après ça, n’hésitez pas à me contacter.
{% endnote %}

Les prérequis de ce cours sont minimaux, il faut avoir une connaissance moyenne du language python et des connaissances minimales de l'organisation de son ordinateur. Si vous n'avez pas ces prérequis ou que vous voulez vérifier que vous les avez suivez les tutoriels suivants :

1. [Avoir un système en état de marche]({{ '/tutoriels/installation-système' | url }})
2. [Savoir naviguer dans un système de fichiers]({{ '/tutoriels/fichiers-navigation' | url }})
3. Il pourra de plus être très utile de :
   * [Savoir ouvrir une fenêtre terminal]({{ '/tutoriels/terminal'  | url }})
   * [D'installez brew si vous êtes sous mac]({{ '/tutoriels/brew'  | url }})
4. [Connaissances minimales en python]({{ '/cours/base-code' | url }})

### Partie 1 : préparation <div id="partie-1"></div>

{% note %}
Le but de cette partie constituée d'**une séance d'autonomie** (le 23 septembre) est d'installer les différents logiciels nécessaires sur son ordinateur et de savoir les utiliser pour coder un projet un python.
{% endnote %}

Pour pouvoir écrire agréablement du code python qui fonctionne, il est nécessaire d'avoir des logiciels efficaces installés sur son ordinateur et — surtout — savoir s'en servir.

Programme de la séance :

1. [Installation de python]({{ '/tutoriels/installation-python' | url }}) et de [vscode]({{ '/tutoriels/vsc-installation-et-prise-en-main' | url }})
2. [Installer les plugins python de vscode]({{ '/tutoriels/vsc-python' | url }})
3. [Un projet pour s'entraîner]({{ '/cours/algorithme-code-théorie/code/projet-hello-dev' | url}})

### Partie 2 : Classes et objets <div id="partie-2"></div>

{% note %}
Le but de cette partie constituée de **deux séances de cours** (les 26 et 27 septembre) et d'**une séance machine** (le 27 septembre) est de comprendre les notions d'objets et de classes pour pouvoir les implémenter en python.
{% endnote %}

#### Cours <div id="partie-2-cours"></div>

Deux séances de cours pour couvrir trois sujets :

1. [Mémoire et espace de noms]({{ '/cours/algorithme-code-théorie/code/mémoire-espace-noms' | url}})
2. [Classes et objets]({{ '/cours/algorithme-code-théorie/code/programmation-objet/classes-et-objets' | url}})
3. [Coder ses objets]({{ '/cours/algorithme-code-théorie/code/programmation-objet/coder-ses-objets' | url}})

#### Séance machine

Première mise en œuvre des exemple du cours et premières expérimentations :

[projet : coder des objets]({{ '/cours/algorithme-code-théorie/code/programmation-objet/projet-code-objets' | url}})

### Partie 3 : héritage <div id="partie-3"></div>

{% note %}
Le but de cette partie constituée de **deux séances de cours** (les 11 et 12 octobre) et de **deux séances machines** (les 12 et 13 octobre).
{% endnote %}

#### Cours <div id="partie-3-cours"></div>

Deux séances de cours :

1. [Composition et agrégation]({{ '/cours/algorithme-code-théorie/code/programmation-objet/composition-agrégation' | url}})
2. [héritage]({{ '/cours/algorithme-code-théorie/code/programmation-objet/héritage' | url}})

#### Séances machine

1. [projet : composition et agrégation]({{ '/cours/algorithme-code-théorie/code/programmation-objet/projet-composition-agrégation' | url}})
2. [projet héritage]({{ '/cours/algorithme-code-théorie/code/programmation-objet/projet-héritage' | url}})

### Partie 4 : programmation événementielle

{% note %}
Le but de cette partie constituée de **deux séances machines** (du 22 novembre au 30 novembre).
{% endnote %}

> TBD : arkanoid

### Partie 5 : design pattern

{% note %}
Le but de cette partie constituée d'**une séance de cours** (le 5 décembre) et de **deux séances machines** (les 6 et 7 décembre).
{% endnote %}

> TBD : cours + td

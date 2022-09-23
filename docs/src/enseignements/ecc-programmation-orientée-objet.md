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

La notation de cet enseignement sera composée de deux parties :

1. une présentation d'un point de cours
2. un projet à rendre

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

<div id="partie-1"></div>

### Partie 1 : préparation

{% note %}
Le but de cette partie constituée d'**une séance d'autonomie** (le 23 septembre) est d'installer les différents logiciels nécessaires sur son ordinateur et de savoir les utiliser pour coder un projet un python.
{% endnote %}

Pour pouvoir écrire agréablement du code python qui fonctionne, il est nécessaire d'avoir des logiciels efficaces installés sur son ordinateur et — surtout — savoir s'en servir.

Programme de la séance :

1. Installation de python et de vscode
2. Installation des plugins python pour vscode
3. Deux projets pour s'entraîner

#### Python

Installez le logiciel python sur votre ordinateur et sachez où il est installé sur votre ordinateur.

{% faire "**Suivez le tutoriel :**" %}
[Installation de python]({{ '/tutoriels/installation-python' | url }}). Dans le doute installez la version anaconda de python.
{% endfaire %}

#### Vscode

Écrire du code se fait de façon agréable si on a un éditeur de texte performant. Nous utiliserons [vscode](https://code.visualstudio.com/) dans ce cours.

{% faire "**Suivez le tutoriel :**" %}
Installer et faire les premières paramétrisations de vscode : [Avoir un éditeur de texte opérationnel]({{ '/tutoriels/vsc-installation-et-prise-en-main' | url }})
{% endfaire %}

#### Vscode et python

L'éditeur vscode est un éditeur généraliste qui vous permettra d'écrire tout type de document texte. Pour écrire du python, il faut installez quelques plugins.

{% faire "**Suivez le tutoriel :**" %}
[Installer les plugins python de vscode]({{ '/tutoriels/vsc-python' | url }})
{% endfaire %}

#### Mise en pratique

On vérifie que tous les outils fonctionnent bien ensemble.

{% faire "**Suivez le projet :**" %}
[projet hello-dev]({{ '/cours/algorithme-code-théorie/code/projet-hello-dev' | url}})
{% endfaire %}

Une fois ce premier projet terminé, entraînez-vous à faire des tests de vos algorithmes avec le projet suivant :

{% faire "**Suivez le projet :**" %}
[projet pourcentages]({{ '/cours/algorithme-code-théorie/code/projet-pourcentages' | url}})
{% endfaire %}

<div id="partie-2"></div>

### Partie 2 : Classes et objets

{% note %}
Le but de cette partie constituée de **deux séances de cours** (les 26 et 27 septembre) et d'**une séance machine** (le 27 septembre) est de comprendre les notions d'objets et de classes pour pouvoir les implémenter en python.
{% endnote %}

<div id="partie-2-cours"></div>

#### Cours

Deux séances de cours pour couvrir trois sujets :

1. [Mémoire et espace de noms]({{ '/cours/algorithme-code-théorie/code/mémoire-espace-noms' | url}})
2. [Classes et objets]({{ '/cours/algorithme-code-théorie/code/programmation-objet/classes-et-objets' | url}})
3. [Composition et agrégation]({{ '/cours/algorithme-code-théorie/code/programmation-objet/composition-agrégation' | url}})

#### Séance machine

Première mise en œuvre des exemple du cours et premières expérimentations :

{% faire "**Suivez le projet :**" %}
[projet : composition et agrégation]({{ '/cours/algorithme-code-théorie/code/programmation-objet/projet-composition-agrégation' | url}})
{% endfaire %}

### Partie 3 : héritage et dictionnaires

{% note %}
Le but de cette partie constituée de **deux séances de cours** (les 11 et 12 octobre) et de **deux séances machines** (les 12 et 13 octobre) est de comprendre :

* la notion d'héritage, que l'on peut utiliser en programmation objet
* l'utilisation de la structure de dictionnaire, fondamentale en programmation objet
* mise en œuvre avec le format de données json

{% endnote %}

#### Cours { #cours-partie-2 }

Deux séances de cours pour couvrir trois sujets :

1. [héritage]({{ '/cours/algorithme-code-théorie/code/programmation-objet/héritage' | url}})
2. [fonctions de hash]({{ "/cours/algorithme-code-théorie/théorie/fonctions-hash" | url }})
3. [structure : dictionnaire]({{ "/cours/algorithme-code-théorie/algorithme/structure-dictionnaire" | url }})

#### Séances machine

* [projet héritage]({{ '/cours/algorithme-code-théorie/code/programmation-objet/projet-héritage' | url}})
* [projet json]()

### Partie 4 : programmation événementielle

{% note %}
Le but de cette partie constituée de **deux séances machines** (du 22 novembre au 30 novembre) est de montrer par l'exemple l’utilisation de la programmation évènementielle, utilisée — par exemple — pour les interfaces graphiques

{% endnote %}

### Partie 5 : design pattern

{% note %}
Le but de cette partie constituée d'**une séance de cours** (le 5 décembre) et de **deux séances machines** (les 6 et 7 décembre) est de connaître et de pouvoir implémenter des *design pattern*.

Les *design pattern* (ou *patron de conception* en français) sont des solutions objets permettant de résoudre nombre de problème courant classique.

{% endnote %}

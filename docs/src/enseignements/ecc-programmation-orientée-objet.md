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

### Partie 1 : préparation

{% note %}
Le but de cette partie constituée d'**une séance d'autonomie** (le 23 septembre) est d'installer les différents logiciels nécessaires sur son ordinateur et de savoir les utiliser pour coder un projet un python.
{% endnote %}

Pour pouvoir écrire agréablement du code python qui fonctionne, il est nécessaire d'avoir des logiciels efficaces installés sur son ordinateur et — surtout — savoir s'en servir.

Programme de la séance :

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

### Partie 2 : Classes et objets

{% note %}
Le but de cette partie constituée de **deux séances de cours** (les 26 et 27 septembre) et d'**une séance machine** (le 27 septembre) est de comprendre les notions d'objets et de classes pour pouvoir les implémenter en python.
{% endnote %}

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

### Partie 3 : héritage et design pattern

2 cours
4 td

### Partie 4 : programmation événementielle

1 cours
2 td
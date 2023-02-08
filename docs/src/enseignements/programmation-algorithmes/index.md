---
layout: layout/post.njk 
title: "MPCI S2 : Programmation et Algorithmes"

tags: ['formation', 'MPCI']

prerequis:
  - /cours/coder-en-python/
  - https://ametice.univ-amu.fr/course/view.php?id=97114

eleventyNavigation:
  key: MPCI
  parent: Enseignements
  order: 3
---

Les cours ont lieu les mardi (8h-10h) et vendredi (8h-12h).

{% info %}
Ce cours fait partie du cours [Algorithme, code et théorie]({{ "/cours/algorithme-code-théorie" | url }}), qui contient un peu plus de choses.
{% endinfo %}

## Plan

Le cours est composée de 3 parties de 3 semaines chacune, entre-coupées de devoirs surveillés de ... 3 heures :

0. [Mise en place](./#partie-0)
1. [Partie *complexité*](./#partie-1)
2. DS1 : sur la partie complexité. Sur table
3. [Partie *programmation objet*](./#partie-2)
4. DS2 : sur la partie programmation objet. Sur ordinateur
5. [Partie *résolution de problèmes*](./#partie-3)
6. ET : porte sur l'intégralité du programme, voir un peu plus.

Chaque **vendredi** à partir de la semaine 2 les 15 ($=3+3+3+3+3$ minutes) premières minutes du cours seront consacrées à un test portant sur le programme de la semaine précédente.

{% note %}
Les divers contrôles intermédiaires seront à rendre directement sur [AMeTICE](https://ametice.univ-amu.fr/course/view.php?id=101942)
{% endnote %}

## Note

La note de cette UE résulte de cette formule :

$$
\max (\frac{CC+ DS + ET}{3}, ET)
$$

Avec :

* $CC = \frac{1}{2}(TUT + TEST)$ où :
  * $TUT$  est la moyenne formée des 2 notes de tutorats
  * $TEST$ est la moyenne des tests de début de séances ($6 = 3 + 3$ tests).
* $DS$ est la moyenne des DS1 et DS2
* $ET$ est l'examen terminal

## <span id="partie-0"></span> Partie 0 : Mise en place

{% note %}
Faites les mises en place nécessaires pour suivre l'enseignement. S'il vous manque des connaissances, suivez les tutoriels et si vous avez encore des doutes après ça, n’hésitez pas à me contacter.
{% endnote %}

Nous allons coder tous nos algorithmes en python. Il est donc nécessaire d'avoir un système fonctionnel. Vérifiez donc avant le début du cours que :

1. [vous avez un système en état de marche]({{ '/tutoriels/installation-système' | url }})
2. [vous savez naviguer dans un système de fichiers]({{ '/tutoriels/fichiers-navigation' | url }})
3. Il pourra de plus être très utile de [savoir ouvrir une fenêtre terminal]({{ '/tutoriels/terminal'  | url }})

## <span id="partie-1"></span> Partie 1 : Complexité

Notions de complexité max/min et en moyenne d'un algorithme, ainsi que la complexité d'un problème.

Côté code, on insistera sur la méthode de développement d'un algorithme, en particulier la gestion des tests unitaires.

### <span id="partie-1.1"></span> Semaine 1

#### <span id="partie-1.1.1"></span> Mardi

1. [Un algorithme ?]({{ "/cours/algorithme-code-théorie/algorithme/définition" | url }})
2. [Pseudo-code]({{ "/cours/algorithme-code-théorie/algorithme/pseudo-code" | url }})
3. [Fonctions]({{ "/cours/algorithme-code-théorie/théorie/fonctions" | url }})

#### <span id="partie-1.1.2"></span> Vendredi

Nous allons utiliser vscode pour la première fois ce TD.

{% faire "**A faire pour vendredi**"%}
Installez vscode sur votre ordinateur en suivant le tutoriel ci-après
{% endfaire %}
{% aller %}
[Installation et prise en main de vsc]({{ '/tutoriels/vsc-installation-et-prise-en-main' | url }})
{% endaller %}

1. [Coder]({{ "/cours/algorithme-code-théorie/code/coder" | url }})
2. [Utiliser python avec vsc]({{ '/tutoriels/vsc-python' | url }}). Il pourra être utile de garder sous le coude le tutoriel d'[utilisation un terminal]({{ '/tutoriels/terminal-utilisation' | url }})
3. [Projet 1 : mise en œuvre d'un projet informatique]({{ "/cours/algorithme-code-théorie/code/projet-hello-dev" | url }})
4. [Projet 2 : pourcentage]({{ '/cours/algorithme-code-théorie/code/projet-pourcentages' | url}})

### <span id="partie-1.2"></span> Semaine 2

{% note %}
Le contrôle de vendredi portera sur la partie code. Il faudra rendre un (ou plusieurs) fichiers python sur AMeTICE.
{% endnote %}

#### <span id="partie-1.2.1"></span> Mardi

1. [Preuve d'algorithme]({{ "/cours/algorithme-code-théorie/algorithme/preuve-algorithme" | url }})
2. [Complexité max/min]({{ "/cours/algorithme-code-théorie/algorithme/complexité-max-min" | url }})

#### <span id="partie-1.2.2"></span> Vendredi

1. [Etude : exponentiation]({{ "/cours/algorithme-code-théorie/algorithme/étude-exponentiation" | url }})
2. [Projet : exponentiation]({{ "/cours/algorithme-code-théorie/code/projet-exponentiation" | url }})
3. Pour aller plus loin : [Projet : suite additive]({{ "/cours/algorithme-code-théorie/code/projet-suite-additive" | url }})

### <span id="partie-1.3"></span> Semaine 3

{% note %}
Le contrôle de vendredi portera sur la partie complexité et preuve d'algorithme. Il faudra rendre une copie.
{% endnote %}

#### <span id="partie-1.3.1"></span> Mardi

1. [Complexité d'un problème]({{ "/cours/algorithme-code-théorie/théorie/complexité-problème" | url }})
2. [Complexité en moyenne]({{ "/cours/algorithme-code-théorie/algorithme/complexité-moyenne" | url }})
3. [Etude : trier un tableau]({{ "/cours/algorithme-code-théorie/algorithme/étude-tris" | url }}) (début : problème de la reconnaissance d'un tableau trié et complexité du problème du tri)

#### <span id="partie-1.3.2"></span> Vendredi

1. [Etude : trier un tableau]({{ "/cours/algorithme-code-théorie/algorithme/étude-tris" | url }})
2. [Projet : tris]({{ "/cours/algorithme-code-théorie/code/projet-tris" | url }})
3. Pour aller plus loin : [Projet : suite additive]({{ "/cours/algorithme-code-théorie/code/projet-suite-additive" | url }})

## DS 1 (Semaine 4)

Devoir surveillé 1 : sur table.

Au programme :

* complexité (min/max/moyenne/problème)
* preuve d'algorithmes
* algorithmes de tris

## DM 1

Pour aller plus loin, vous pouvez faire le [DM 1](./annales/2022-2023/dm_1). Vous **pouvez le faire en binôme** et il est à rendre pour le premier vendredi de la semaine 5 (le 3 février).

## <span id="partie-2"></span> Partie 2 : Programmation Objet

Programmation objet tant théorique (modèle UML de classe) que pratique.

Côté code, on insistera sur la mise en forme automatisée du code et la notion de couverture de code.

### <span id="partie-2.1"></span> Semaine 5

{% info %}
Pas de contrôle cette semaine.
{% endinfo %}

{% attention %}
A partir de la partie 2, les contrôles de début séance seront à écrire en [markdown]({{ '/tutoriels/format-markdown' | url }}) et envoyé converti en html (ou pdf) sur AMeTICE.
{% endattention %}

#### <span id="partie-2.1.1"></span> Mardi

1. [Mémoire et espace de noms]({{ "/cours/algorithme-code-théorie/code/mémoire-espace-noms" | url }})
2. [Classes et objets]({{ "/cours/algorithme-code-théorie/code/programmation-objet/classes-et-objets" | url }})

#### <span id="partie-2.1.2"></span> Vendredi

1. [black et code coverage]({{ "/tutoriels/style-couverture" | url }})
2. [coder ses objets]({{ "/cours/algorithme-code-théorie/code/programmation-objet/coder-ses-objets" | url }}). C'est également une introduction aux tests, que vous connaissez déjà. Donc profitez-en pour mettre en pratique la couverture du code et au style automatique vec black
3. [projet : coder ses objets]({{ "/cours/algorithme-code-théorie/code/programmation-objet/projet-code-objets" | url }})

### <span id="partie-2.2"></span> Semaine 6

#### <span id="partie-2.2.1"></span> Mardi

1. [Composition et agrégation]({{ "/cours/algorithme-code-théorie/code/programmation-objet/composition-agrégation" | url }})
2. [Héritage]({{ "/cours/algorithme-code-théorie/code/programmation-objet/héritage" | url }})

#### <span id="partie-2.2.2"></span> Vendredi

1. [Projet : composition et agrégation]({{ "/cours/algorithme-code-théorie/code/programmation-objet/projet-composition-agrégation" | url }})
2. [Projet : héritage]({{ "/cours/algorithme-code-théorie/code/programmation-objet/projet-héritage" | url }})
3. Pour aller plus loin : [Projet : TDD]({{ "/cours/algorithme-code-théorie/code/programmation-objet/projet-TDD" | url }})

### <span id="partie-2.3"></span> Semaine 7

#### <span id="partie-2.3.1"></span> Mardi

1. [Programmation événementielle]({{ "/cours/algorithme-code-théorie/code/programmation-évènementielle" | url }})

#### <span id="partie-2.3.2"></span> Vendredi

1. [Projet : programmation événementielle]({{ "/cours/algorithme-code-théorie/code/projet-programmation-évènementielle" | url }})

## DS 2 (Semaine 8)

Devoir surveillé 2 : sur ordinateur.

Au programme :

* code

## <span id="partie-3"></span> Partie 3 : Résolution de Problèmes

> TBD : résolution de problème / structure de donnée et côté code : virtualenv

### <span id="partie-3.1"></span> Semaine 9

{% info %}
Pas de contrôle cette semaine.
{% endinfo %}

#### <span id="partie-3.1.1"></span> Mardi

> TBD : partie générale sur les structures de données. A quoi ça sert et comment s'en servir. Puis cas particulier des tableau/listes et des dictionnaires.
> TBD faire la complexité amortie de ajout/suppression dans une liste.

1. [Complexité amortie]({{ "/cours/algorithme-code-théorie/algorithme/complexité-amortie" | url }})
2. [Structure : liste]({{ "/cours/algorithme-code-théorie/algorithme/structure-liste" | url }})
3. [Fonctions de hash]({{ "/cours/algorithme-code-théorie/théorie/fonctions-hash" | url }})
4. [Structure : dictionnaire]({{ "/cours/algorithme-code-théorie/algorithme/structure-dictionnaire" | url }})

#### <span id="partie-3.1.2"></span> Vendredi

1. [Etude : mélanger un tableau]({{ "/cours/algorithme-code-théorie/algorithme/étude-mélange" | url }})
2. projet : hasard (avec code objet)

> TBD : virtualenv et poetry.

### <span id="partie-3.2"></span> Semaine 10

#### <span id="partie-3.2.1"></span> Mardi

gloutons

#### <span id="partie-3.2.2"></span> Vendredi

1. fichiers
2. projet gloutons (avec fichier texte et code objet)

### <span id="partie-3.3"></span> Semaine 11

#### <span id="partie-3.3.1"></span> Mardi

machine de Turing et np-complétude

#### <span id="partie-3.3.2"></span> Vendredi

> TBD : sac à dos ? fractionnaire. puis optimal 1, puis optimal mais exponentiel en mémoire puis gloutons.

### semaine 12

Contrôle final : sur table.

Au programme :

* tout
* voir un peu plus

## annales

Les [annales des tests et contrôle](./annales) de ce cours

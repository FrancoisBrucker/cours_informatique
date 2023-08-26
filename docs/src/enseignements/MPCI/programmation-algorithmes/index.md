---
layout: layout/post.njk 
title: "S2 : Programmation et Algorithmes"

tags: ['formation', 'MPCI']

eleventyNavigation:
  order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

  prerequis:
    - /cours/coder-en-python/
    - https://ametice.univ-amu.fr/course/view.php?id=97114

---

Les cours ont lieu les mardi (8h-10h) et vendredi (8h-12h).

{% info %}
Ce cours fait partie du cours [Algorithme, code et théorie]({{ "/cours/algorithme-code-théorie"  }}){.interne}, qui contient un peu plus de choses.
{% endinfo %}

## Plan

Le cours est composée de 3 parties de 3 semaines chacune, entre-coupées de devoirs surveillés de ... 3 heures :

0. [Mise en place](./#partie-0){.interne}
1. [Partie *complexité*](./#partie-1){.interne}
2. DS1 : sur la partie complexité. Sur table
3. [Partie *programmation objet*](./#partie-2){.interne}
4. DS2 : sur la partie programmation objet. Sur ordinateur
5. [Partie *résolution de problèmes*](./#partie-3){.interne}
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

1. [vous avez un système en état de marche]({{ '/tutoriels/installation-système'  }}){.interne}
2. [vous savez naviguer dans un système de fichiers]({{ '/tutoriels/fichiers-navigation'  }}){.interne}
3. Il pourra de plus être très utile de [savoir ouvrir une fenêtre terminal]({{ '/tutoriels/terminal'   }}){.interne}

## <span id="partie-1"></span> Partie 1 : Complexité

Notions de complexité max/min et en moyenne d'un algorithme, ainsi que la complexité d'un problème.

Côté code, on insistera sur la méthode de développement d'un algorithme, en particulier la gestion des tests unitaires.

### <span id="partie-1.1"></span> Semaine 1

#### <span id="partie-1.1.1"></span> Mardi

1. [Un algorithme ?]({{ "/cours/algorithme-code-théorie/algorithme/définition"  }}){.interne}
2. [Pseudo-code]({{ "/cours/algorithme-code-théorie/algorithme/pseudo-code"  }}){.interne}
3. [Fonctions]({{ "/cours/algorithme-code-théorie/théorie/fonctions"  }}){.interne}

#### <span id="partie-1.1.2"></span> Vendredi

Nous allons utiliser vscode pour la première fois ce TD.

{% faire "**A faire pour vendredi**"%}
Installez vscode sur votre ordinateur en suivant le tutoriel ci-après
{% endfaire %}
{% aller %}
[Installation et prise en main de vsc]({{ '/tutoriels/vsc-installation-et-prise-en-main' }}){.interne}
{% endaller %}

1. [Coder]({{ "/cours/algorithme-code-théorie/code/coder"  }}){.interne}
2. [Utiliser python avec vsc]({{ '/tutoriels/vsc-python' }}){.interne}. Il pourra être utile de garder sous le coude le tutoriel d'[utilisation un terminal]({{ '/tutoriels/terminal-utilisation' }}){.interne}
3. [Projet 1 (tutoriel) : mise en œuvre d'un projet informatique]({{ "/cours/algorithme-code-théorie/code/projet-hello-dev"  }}){.interne}
4. [Projet 2 (tutoriel) : pourcentage]({{ '/cours/algorithme-code-théorie/code/projet-pourcentages' }}){.interne}

> TBD un projet non tutoriel avec code + test à produire par eux même.

### <span id="partie-1.2"></span> Semaine 2

{% note %}
Le contrôle de vendredi portera sur la partie code. Il faudra rendre un (ou plusieurs) fichiers python sur AMeTICE.
{% endnote %}

#### <span id="partie-1.2.1"></span> Mardi

1. [Preuve d'algorithme]({{ "/cours/algorithme-code-théorie/algorithme/preuve-algorithme"  }}){.interne}
2. [Complexité max/min]({{ "/cours/algorithme-code-théorie/algorithme/complexités/max-min"  }}){.interne}

#### <span id="partie-1.2.2"></span> Vendredi

1. [Étude : exponentiation]({{ "/cours/algorithme-code-théorie/algorithme/étude-exponentiation"  }}){.interne}
2. [Projet : exponentiation]({{ "/cours/algorithme-code-théorie/code/projet-exponentiation"  }}){.interne}
3. Pour aller plus loin : [Projet : suite additive]({{ "/cours/algorithme-code-théorie/code/projet-suite-additive"  }}){.interne}

### <span id="partie-1.3"></span> Semaine 3

{% note %}
Le contrôle de vendredi portera sur la partie complexité et preuve d'algorithme. Il faudra rendre une copie.
{% endnote %}

#### <span id="partie-1.3.1"></span> Mardi

1. [Complexité d'un problème]({{ "/cours/algorithme-code-théorie/algorithme/complexités/problème"  }}){.interne}
2. [Complexité en moyenne]({{ "/cours/algorithme-code-théorie/algorithme/complexités/moyenne"  }}){.interne}
3. [Étude : trier un tableau]({{ "/cours/algorithme-code-théorie/algorithme/tris"  }}){.interne} (début : problème de la reconnaissance d'un tableau trié et complexité du problème du tri)

#### <span id="partie-1.3.2"></span> Vendredi

1. [Étude : trier un tableau]({{ "/cours/algorithme-code-théorie/algorithme/tris"  }}){.interne} (suite et fin)
2. [Projet : tris]({{ "/cours/algorithme-code-théorie/code/projet-tris"  }}){.interne}

## DS 1 (Semaine 4)

[Devoir surveillé 1](./annales/2022-2023/ds_1){.interne} : sur table.

Au programme :

* complexité (min/max/moyenne/problème)
* preuve d'algorithmes
* algorithmes de tris

## DM 1

Sujet du [DM 1](./annales/2022-2023/dm_1){.interne} à rendre pour le premier vendredi de la semaine 5 (le 3 mars).

{% attention %}
Vous pouvez faire le DM **en binôme**.
{% endattention %}

## <span id="partie-2"></span> Partie 2 : Programmation Objet

Programmation objet tant théorique (modèle UML de classe) que pratique.

Côté code, on insistera sur la mise en forme automatisée du code et la notion de couverture de code.

### <span id="partie-2.1"></span> Semaine 5

{% info %}
Pas de contrôle cette semaine. Mais il faut rendre le DM 1 pour vendredi.
{% endinfo %}

{% attention %}
A partir de la partie 2, les contrôles de début séance seront à écrire en [markdown]({{ '/tutoriels/format-markdown'  }}) et envoyé converti en html (ou pdf) sur AMeTICE.
{% endattention %}

#### <span id="partie-2.1.1"></span> Mardi

1. [Mémoire et espace de noms]({{ "/cours/algorithme-code-théorie/code/mémoire-espace-noms"  }}){.interne}
2. [Classes et objets (début)]({{ "/cours/algorithme-code-théorie/code/programmation-objet/classes-et-objets"  }}){.interne}

#### <span id="partie-2.1.2"></span> Vendredi

1. [Classes et objets (fin)]({{ "/cours/algorithme-code-théorie/code/programmation-objet/classes-et-objets"  }}#deuxième-exemple){.interne}
2. [coder ses objets]({{ "/cours/algorithme-code-théorie/code/programmation-objet/coder-ses-objets"  }}){.interne}
3. Outils de développement supplémentaires :
   * [installation de black]({{ "/tutoriels/vsc-python-modules-supplémentaires/black" }}){.interne} qui permet de faire du joli code tout seul.
   * [code coverage]({{ "/tutoriels/couverture-de-code" }}){.interne} pour vérifier que les tests passent par tout le code
4. [Projet : objets dés]({{ "/cours/algorithme-code-théorie/code/programmation-objet/projet-objets-dés"  }}){.interne}
5. [Projet : objets cartes]({{ "/cours/algorithme-code-théorie/code/programmation-objet/projet-objets-cartes"  }}){.interne}
6. Pour aller plus loin : [projet : bataille navale]({{ "/cours/algorithme-code-théorie/code/programmation-objet/projet-bataille-navale"  }}){.interne}

### <span id="partie-2.2"></span> Semaine 6

#### <span id="partie-2.2.1"></span> Mardi

1. [Composition et agrégation]({{ "/cours/algorithme-code-théorie/code/programmation-objet/composition-agrégation"  }}){.interne}
2. [Héritage]({{ "/cours/algorithme-code-théorie/code/programmation-objet/héritage"  }}){.interne}

#### <span id="partie-2.2.2"></span> Vendredi

1. [Projet composition : dés]({{ "/cours/algorithme-code-théorie/code/programmation-objet/projet-composition-dés"  }}){.interne}
2. [Projet : héritage]({{ "/cours/algorithme-code-théorie/code/programmation-objet/projet-héritage"  }}){.interne}
3. [Projet agrégation : cartes]({{ "/cours/algorithme-code-théorie/code/programmation-objet/projet-agrégation-cartes"  }}){.interne}
4. Pour aller plus loin : [projet : bataille navale]({{ "/cours/algorithme-code-théorie/code/programmation-objet/projet-bataille-navale"  }}){.interne}

### <span id="partie-2.3"></span> Semaine 7

#### <span id="partie-2.3.1"></span> Mardi

1. [Programmation événementielle]({{ "/cours/algorithme-code-théorie/code/programmation-évènementielle"  }}){.interne}

#### <span id="partie-2.3.2"></span> Vendredi

1. [Projet : programmation événementielle]({{ "/cours/algorithme-code-théorie/code/projet-programmation-évènementielle"  }}){.interne} ([éléments de corrigé](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/algorithme-code-th%C3%A9orie/code/projet-programmation-%C3%A9v%C3%A8nementielle/Arkanoid))

## <span id="ds-2"></span> DS 2 (Semaine 8)

[Devoir surveillé 2](./annales/2022-2023/ds_2){.interne} : sur ordinateur.

Au programme :

* programmation objet
* programmation évènementielle avec pyglet

## <span id="partie-3"></span> Partie 3 : Résolution de Problèmes

### <span id="partie-3.1"></span> Semaine 9

{% info %}
Pas de contrôle cette semaine.
{% endinfo %}

#### <span id="partie-3.1.1"></span> Mardi

1. [Structure de données]({{ "/cours/algorithme-code-théorie/algorithme/structure-de-données"  }}){.interne}
2. [Structure : tableaux]({{ "/cours/algorithme-code-théorie/algorithme/structure-de-données/tableau"  }}){.interne}
3. [Structure : liste]({{ "/cours/algorithme-code-théorie/algorithme/structure-de-données/liste"  }}){.interne}
4. Principes de la [complexité amortie]({{ "/cours/algorithme-code-théorie/algorithme/complexités/amortie"  }}){.interne}
5. [Fonctions de hash]({{ "/cours/algorithme-code-théorie/théorie/fonctions-hash"  }}){.interne}
6. [Structure : dictionnaire]({{ "/cours/algorithme-code-théorie/algorithme/structure-de-données/dictionnaire"  }}){.interne}

#### <span id="partie-3.1.2"></span> Vendredi

1. [étude de l'alignement de séquences]({{ '/cours/algorithme-code-théorie/algorithme/étude-alignement-séquences'  }}){.interne}
2. [code alignement de séquences]({{ '/cours/algorithme-code-théorie/code/projet-alignement-séquences'  }}){.interne}

### <span id="partie-3.2"></span> Semaine 10

#### <span id="partie-3.2.1"></span> Mardi

1. [Algorithmes gloutons]({{ '/cours/algorithme-code-théorie/algorithme/algorithmes-gloutons'  }}){.interne}

#### <span id="partie-3.2.2"></span> Vendredi

1. [étude : chemins et cycles]({{ '/cours/algorithme-code-théorie/algorithme/étude-chemins-cycles'  }}){.interne}
2. [projet : chemins et cycles]({{ '/cours/algorithme-code-théorie/code/projet-chemins-cycles'  }}){.interne}

### <span id="partie-3.3"></span> Semaine 11

#### <span id="partie-3.3.1"></span> Mardi

1. [Enveloppes convexes]({{ '/cours/algorithme-code-théorie/algorithme/enveloppes-convexes'  }}){.interne}

#### <span id="partie-3.3.2"></span> Vendredi

1. [structure : chaîne de caractères]({{ '/cours/algorithme-code-théorie/algorithme/structure-de-données/chaîne-de-caractères'}}){.interne}
2. [fichiers]({{ '/cours/algorithme-code-théorie/code/fichiers'}}){.interne}
3. [projet : fichiers]({{ '/cours/algorithme-code-théorie/code/projet-fichiers'}}){.interne}

Pour aller plus loin :

1. [projet : format de données]({{ '/cours/algorithme-code-théorie/code/fichiers/données'}}){.interne}

### semaine 12

Contrôle final : sur table.

Au programme :

* tout
* voir un peu plus

## annales

Les [annales des tests et contrôles](./annales){.interne} de ce cours

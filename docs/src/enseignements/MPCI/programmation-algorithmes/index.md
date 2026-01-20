---
layout: layout/post.njk
title: "S2 : Programmation et Algorithmes"

tags: ["formation", "MPCI"]

eleventyNavigation:
  order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Ce cours intitulé _Programmation et algorithmes_ est donné au second semestre de la licence MPCI ([lien AMeTICE AMU Informatique S2](https://ametice.univ-amu.fr/course/view.php?id=129120)). Il s'appuie sur le cours de _Programmation_ donné au S1 ([lien AMeTICE AMU Informatique S1](https://ametice.univ-amu.fr/course/view.php?id=125682)).

Ce cours montrera l'informatique sous trois aspects complémentaires — théorie, code et algorithmes — que tout [honnête informaticien](https://fr.wikipedia.org/wiki/Honn%C3%AAte_homme) devrait connaître. Il s'adresse à des personnes ayant des connaissances minimales en informatiques mais voulant (ou étant obligé d' 🙂) approfondir le sujet. Nous rentrerons dans les détails tant d'un point de vue algorithmique (Tout algorithme sera démontré) que d'un point de vue code (on montrera comment un programme s'exécute sur un ordinateur).

L'informatique est une science incarnée : elle nécessite à la fois de solides connaissances théoriques pour concevoir des algorithmes efficaces et des capacités d'expérimentation et de rigueur pour les mettre en oeuvre et les faire fonctionner sur un ordinateur.

Cela va vous demander un travail personnel important pour comprendre et assimiler les bases théoriques **et** un temps certain d’expérimentation pour faire fonctionner le tout sur votre ordinateur en comprenant pourquoi et comment cela fonctionne.

## Note

Le cours est composé de deux UEes, l'une consacrée à l'algorithmie, l'autre à la programmation. La note de chaque UE résulte de cette formule :

$$
\max (\frac{CC+ DS + ET}{3}, ET)
$$

Avec :

- $CC = \frac{1}{2}(TUT + TEST)$ où :
  - $TUT$ est la moyenne formée de la note de tutorat
  - $TEST$ est la moyenne des tests de débuts de séances.
- $DS$ est la note du devoir surveillé
- $ET$ est l'examen terminal

## Prérequis

Il est nécessaire d'avoir quelques prérequis avant de commencer ce cours.

### Algorithmie

Avoir une notion de ce qu'est une variable, une instruction et une fonction. Aucun autre prérequis algorithmique n'est nécessaire.

### Programmation

Il est nécessaire d'avoir des bases de python pour commencer ce cours. Il est **indispensable** que vous relisiez le cours ci-après pour s'assurer que vous avez bien les bases nécessaires en programmation python pour commencer ce cours :

{% aller %}
[Bases de python](/cours/coder-et-développer/bases-programmation/){.interne}
{% endaller %}

## Cours

Le cours est disponible via le site d'AMeTICE et en suivant les liens de chaque partie ci-après. Cela ne vous dispense pas de prendre des notes, mais vous aide à la révision ou aux divers prérequis que vous aurez à préparer avant le cours.

## Plan

Ce cours est composée de plusieurs parties :

- Notion d'algorithmie
- Complexité d'un complexité
- Structures de données
- Programmation objet

<!-- 

### Prérequis

> TBD pour s'assurer que les prérequis sont ok, faire un DM avant le début du semestre avec du code, du numpy et de la génération de listes. 

> TBD remplacer debugueur par TD listes et dictionnaires python.

-->

### Semaine 1

> 19/01 au 23/01
> Algorithmie

#### Mercredi : qu'est-ce qu'un algorithme

> 2h

Notions abordées :

- définition d'un programme et d'un algorithme
- savoir ce que fait un programme : 
  - il faut toujours démonter qu'un programme s'arrête
  - il faut toujours démontrer ce que fait un algorithme
- ce que ne peut pas faire un algorithme

{% aller %}
[bases théorique de l'algorithmie](/cours/algorithmie/bases-théoriques){.interne}
{% endaller %}

#### Vendredi : écrire des algorithmes

> 4h

Notions abordées :

- écrire des algorithme en pseudo-code (et thèse de Church-Turing)
- algorithmes itératif et récursifs
- prouver un algorithme

{% aller %}
[Écrire des algorithmes en pseudo-code](/cours/algorithmie/pseudo-code){.interne}
{% endaller %}
{% aller %}
[Prouver des algorithmes](/cours/algorithmie/prouver-un-algorithme/){.interne}
{% endaller %}
{% aller %}
[On s'entraîne](/cours/algorithmie/projet-itératif-récursif/){.interne}
{% endaller %}
  
Si on a le temps, sinon à faire chez soit :

{% aller %}
- [Projet : techniques de récursion](/cours/algorithmie/projet-techniques-de-récursion){.interne}
- [exercices non corrigés](/cours/algorithmie/exercices-itératif-récursif){.interne}
{% endaller %}

### Semaine 2

> 26/01 au 30/01
> Programmation

#### Mercredi : projet de développement

> 2h

{% attention %}
Test de 15min **sur feuille** en début de cours sur les thèmes de la semaine précédente.
{% endattention %}

- base système :
  - dossiers, fichiers
  - programmes
- terminal
- développement python :
  - interpréteur
  - ide vscode
  - tests

#### Vendredi : exercices

> 2h

- développer un algorithme
- on s'entraîne

### Semaine 3

> 02/02 au 06/02
> Algorithmie

#### Mercredi : complexité

> 2h

{% attention %}
Test de 15min **sur ordinateur** en début de cours sur les thèmes de la semaine précédente.
{% endattention %}

- définition
- complexité spatiale et temporelle
- calculs de $\mathcal{O}$
- complexité d'algorithmes itératifs et récursifs

#### Vendredi : exercices

> 2h

- mesure de complexité en code
- complexité en moyenne

### Semaine 4

> 09/02 au 13/02
> Algorithmie

#### Mercredi et vendredi : exercices

> 4h

Complexité et preuves d'algorithmes

<!-- TBD

- <https://efrei.poupa.net/Programmation%20en%20C++/Exercices_et_problemes_d_algorithme.pdf>
- <https://perso.liris.cnrs.fr/pierre-antoine.champin/enseignement/algo/exercices/>
- <https://imag.umontpellier.fr/~lacour/exo_algo.pdf>
- <https://wiki.sfeir.com/carriere/recrutement/evaluation-algo/exemple_exercices_algo/>
- <https://fabien-torre.fr/Enseignement/Exercices/algo-exos.php>
- <https://www.youtube.com/playlist?list=PLZpzLuUp9qXzOgDakYP0UAGIBNk0pPdvZ>

-->

<!-- 




### Semaine 1

> 20/01 au 24/01

#### Vendredi : qu'est-ce que le code

{% faire "**Prérequis**" %}

Avoir relu et compris [les bases de la programmation](/cours/coder-et-développer/bases-programmation/){.interne}. En particulier :

- [avoir python d'installé](/cours/coder-et-développer/bases-programmation/#installation-développement){.interne} et savoir s'en servir
- fait le tutoriel de [prise en main de l'éditeur vscode](/cours/coder-et-développer/bases-programmation/éditeur-vscode/prise-en-main/){.interne}

{% endfaire %}
{% info %}
N'hésitez pas à poser des questions en début de cours si vous avez des questions concernant les prérequis.
{% endinfo %}

Parties abordées :

{% aller %}

1. [Connaissances systèmes indispensables](/cours/coder-et-développer/connaissances-système-minimales/){.interne}
2. [écrire du code](/cours/coder-et-développer/développement/){.interne}, les parties :
   1. [coder](/cours/coder-et-développer/développement/coder){.interne}
   2. [projet `hello dev`](/cours/coder-et-développer/développement/tutoriel-hello-dev/){.interne}

{% endaller %}

### Semaine 2

> 27/01 au 31/01

#### Mercredi : écrire des algorithmes

{% aller %}

1. [Écrire des algorithmes en pseudocode](/cours/algorithmie/pseudo-code/){.interne}
2. [Problèmes algorithmique](/cours/algorithmie#problème-algorithmique){.interne}
3. [Prouver des algorithmes](/cours/algorithmie/prouver-un-algorithme/){.interne}

{% endaller %}

Si on a le temps, on le fait en cours sinon faites le chez vous :

{% aller %}

[On s'entraîne](/cours/algorithmie/projet-itératif-récursif/){.interne}

{% endaller %}

#### Vendredi : écrire du code

{% aller %}

1. [Projet pourcentages](/cours/coder-et-développer/développement/projet-pourcentages/){.interne}
2. [Déboguer ses programmes](/cours/coder-et-développer/debugger/){.interne}

{% endaller %}

Si on a le temps, on le fait en cours sinon faites le chez vous :

{% aller %}

[On s'entraîne](/cours/coder-et-développer/projet-codes/){.interne}

{% endaller %}

### Semaine 3

> 03/02 au 07/02

#### Mercredi : complexité algorithmique

{% attention %}
Test de 15min en début de cours sur **la partie preuve et création d'algorithmes**. Il faudra rendre une feuille de papier.
{% endattention %}
{% faire %}
[Sujet du test 1](./annales/2024-2025/1_test/){.interne}
{% endfaire %}

Ce cours est basé sur la notion de complexité algorithmique que vous avez du aborder au S1.

{% faire "**Prérequis**" %}
Reprendre la partie complexité de votre cours de S1.
  
{% endfaire  %}

{% info %}
N'hésitez pas à poser des questions en début de cours si vous avez des questions concernant les prérequis.
{% endinfo %}

Parties abordées :

{% aller %}

1. [Complexité d'un algorithme](/cours/algorithmie/complexité-calculs/){.interne}
2. [Complexité d'un problème](/cours/algorithmie/complexité-problème/){.interne}

{% endaller %}

Si on a le temps, on le fait en cours sinon faites le chez vous :

{% aller %}

[On s'entraîne](/cours/algorithmie/projet-calcul-complexite/){.interne}

{% endaller %}

#### Vendredi : stockage de données

{% attention %}
On vous remettra également le premier DM à rendre pour le **28 février 23h59** sur AMeTICE au format Markdown.
{% endattention %}
{% faire %}

[Sujet du DM](/enseignements/MPCI/programmation-algorithmes/annales/2024-2025/dm-doublons/){.interne}

Il faudra rendre un dossier contenant :

- un dossier contenant le rendu de la partie algorithmie. Il devra être sous la forme d'un fichier markdown et de sa conversion en html.
- un dossier contenant le rendu de la partie code contenant le projet vscode et les différents programmes.

{% endfaire %}
{% info %}
[Suivre le tutoriel Markdown](/tutoriels/format-markdown/){.interne}
{% endinfo %}

Comment conserver et accéder à des données :

{% aller %}

1. [Variables et objets en mémoire](/cours/coder-et-développer/données-mémoire/){.interne}
2. [Notion de fichier](/cours/coder-et-développer/fichiers/structure/){.interne}
{% endaller %}

Cas particulier du texte :

{% aller %}

1. [Coder des caractères avec Unicode](/cours/coder-et-développer/encodage-unicode/){.interne}
2. [Fichiers texte](/cours/coder-et-développer/fichiers/fichiers-texte/){.interne}

{% endaller %}

On s'entraîne :

{% aller %}

[Projet : fichiers textes](/cours/coder-et-développer/fichiers/projet-texte/){.interne}

{% endaller %}

Pour aller plus loin, vous pouvez regarder :

{% info %}

Le reste [du cours sur les fichier et dossiers](/cours/coder-et-développer/fichiers/){.interne}

{% endinfo %}

### Semaine 4

> 11/02 au 14/02

{% attention %}
Test de 15min en début de cours sur **la partie code (main/fonctions/tests)**. Il faudra rendre des fichiers sur AMeTICE.
{% endattention %}
{% faire %}
[Sujet du test 2](./annales/2024-2025/2_test/){.interne}
{% endfaire %}

Plan de la séance :

{% aller %}

[Projet : exponentiation](/cours/algorithmie/projet-exponentiation/){.interne}

{% endaller %}

Pour aller plus loin :

{% aller %}

[Projet : suites additives](/cours/algorithmie/projet-suite-additive/){.interne}

{% endaller %}

### Semaine 5

> 24/02 au 28/02

Semaine basée sur les tris.

{% info %}
Reprend de grandes parties [du cours d'algorithmie sur les tris](/cours/algorithmie/problème-tris/){,interne}, mais pour aller plus loin ou pour les révisions, n'hésitez pas à aller le lire.
{% endinfo %}

#### Mercredi : tris TD

{% attention %}
Test de 15min en début de cours sur **la partie complexité**.
{% endattention %}
{% faire %}
[Sujet du test 3](./annales/2024-2025/3_test/){.interne}
{% endfaire %}

Sujets abordés :

{% aller %}

Introduction aux algorithmes de tri :

1. [Problème du tri : définition et reconnaissance](/cours/algorithmie/problème-tris/){.interne}
2. [Complexité du problème du tri](/cours/algorithmie/problème-tris/complexité-problème/){.interne}
{% endaller %}

L'analyse de ces algorithme simple nous permettra de formaliser la notion de complexité en moyenne :

{% aller %}

1. [Algorithme de tris par  insertion](/cours/algorithmie/problème-tris/algorithme-insertion/){.interne}
2. [Complexité en moyenne](/cours/algorithmie/complexité-moyenne/){.interne}

{% endaller %}

Puis on abordera des notion plus avancées du tri :

{% aller %}

1. [Tri fusion : diviser pour régner](/cours/algorithmie/problème-tris//algorithme-fusion/){.interne}
2. [Tri rapide : calcul des complexités](/cours/algorithmie/problème-tris/algorithme-rapide/){.interne}

{% endaller %}

#### Vendredi : tris TP

{% attention %}
Rendre le DM 1.
{% endattention %}
{% attention %}
[Sujet DM2 : Palindromes](annales/2023-2024/palindromes/){.interne}
{% endattention %}

On code ce qu'on a vu mercredi :

{% aller %}

[Projet tri](/cours/algorithmie/problème-tris/projet-tris/){.interne}

{% endaller %}

### Semaine 6

> 03/03 au 07/03

#### Mercredi : Liste/dictionnaires et piles

{% attention %}
Test de 15min en début de cours sur **les tris et la complexité en moyenne**.
{% endattention %}
{% faire %}
[Sujet du test 4](./annales/2024-2025/4_test/){.interne}
{% endfaire %}

Analyse de structures de données fondamentales en algorithmie :

{% aller %}

1. [structures de données](/cours/algorithmie/structure-données/){.interne}
2. [file](/cours/algorithmie/structure-pile-file/file){.interne}
3. [pile](/cours/algorithmie/structure-pile-file/pile){.interne}
4. [listes](/cours/algorithmie/structure-liste/){.interne}

{% endaller %}

Un autre type de complexité, très utile pour l'analyse de structures complexes et que l'on a utilisé pour les listes :

{% aller %}

[La complexité amortie](/cours/algorithmie/complexité-amortie/){.interne}

{% endaller %}

N'hésitez pas à aller jeter eu coup d'œil aux exercices sur les piles et les files :

{% aller %}

[exercices](/cours/algorithmie/structure-pile-file/#exercices){.interne}

{% endaller %}

#### Vendredi : Fonctions de hachages et dictionnaires

{% aller %}

[Hash et dictionnaires](/cours/algorithmie/structure-dictionnaire/){.interne}

{% endaller %}

### Semaine 7

> 10/03 au 14/03

Venez avec vos questions d'algorithmie, de complexité et de preuves. On passera la séance à caler les notions du DS et à s'entraîner avec des exercices mercredi et vendredi.

{% info %}
Il n'y aura pas de tes cette semaine, cela vous permettra de commencer vos révisions et de venir avec vos questions algorithmique.

En particulier, lisez DS 1 des précédentes années...
{% endinfo %}

#### Mercredi : algorithmes classiques

On passera la séance de TD à résoudre des algorithmes classiques :
{% aller %}

[Algorithmes classiques](/cours/algorithmie/projet-algorithmes-classiques){.interne}

{% endaller %}

#### Vendredi : Jolis DS

Ayez déjà commencé vos révisions. On répondra aux questions que vous vous posez sur les anciens DS et ET (et il y en a des jolis) d'algorithmie.

{% aller %}

[Problèmes classiques](/cours/algorithmie/projet-problemes-classiques){.interne}

{% endaller %}

### Semaine 8

> 17/03 au 21/03

{% attention %}
**DS algorithmie 2h , mardi 18/03**.
{% endattention %}

#### Mercredi : classes et objets

{% aller %}

[Présentation du cours du 19 mars 2025](objets){.interne}

{% endaller %}

{% aller %}

[Classes et objets](/cours/coder-et-développer/programmation-objet#classes-objets){.interne}

{% endaller %}

#### Vendredi : on s'entraîne puis composition et agrégation

On s'entraîne :

{% aller %}

- [projet dé](/cours/coder-et-développer/programmation-objet/projet-objets-dés/){.interne}
- [projet cartes](/cours/coder-et-développer/programmation-objet/projet-objets-cartes/){.interne}

{% endaller %}

Puis :

{% aller %}

[Composition et agrégation](/cours/coder-et-développer/programmation-objet/composition-agrégation/){.interne}

{% endaller %}

### Semaine 9

> 24/03 au 28/03

{% attention %}
Rendre DM2 (vendredi)
{% endattention %}
{% attention %}
Sujet DM3 : [Bataille navale](/cours/coder-et-développer/programmation-objet/projet-bataille-navale/){.interne}

Il faudra rendre un dossier contenant le projet vscode et les différents programmes.

{% endattention %}

#### Mercredi : on s'entraîne

{% attention %}
Test de 15min en début de cours sur **les objets, UML et le python**.
{% endattention %}
{% faire %}
Sujet du test 5
{% endfaire %}

On s'entraîne :

{% aller %}

- [Projet composition d'objets : dés](/cours/coder-et-développer/programmation-objet/projet-composition-dés/){.interne}
- [Projet agrégation : cartes](/cours/coder-et-développer/programmation-objet/projet-agrégation-cartes/){.interne}

{% endaller %}

#### Vendredi : héritage

{% aller %}

[Présentation du cours du 28 mars 2025](heritage){.interne}

{% endaller %}
{% aller %}

1. [Héritage](/cours/coder-et-développer/programmation-objet/héritage/){.interne}
2. [Améliorer ses objets](/cours/coder-et-développer/programmation-objet/améliorer-ses-objets/){.interne}

{% endaller %}

Pour aller plus loin, amélioration des dès et des cartes :

{% aller %}

- [Accesseur et dés](/cours/coder-et-développer/programmation-objet/projet-objets-dés-accesseur){.interne}
- [protéger les attributs de cartes](/cours/coder-et-développer/programmation-objet/projet-objets-cartes-value-object){.interne}

{% endaller %}

### Semaine 10

> 31/03 au 04/04

#### Mercredi : projet héritage

On s'entraîne sur l'héritage :

{% aller %}
[Projet Héritage](/cours/coder-et-développer/programmation-objet/projet-héritage/){.interne}
{% endaller %}

#### Vendredi : Méthodes de résolution de problèmes

{% attention "Sujet DM4" %}
Pour ce DM, il vous faudra commencer par lire et comprendre le cours de  [programmation évènementielle](/cours/coder-et-développer/programmation-évènementielle/){.interne} :

- lisez (et **comprenez**) [la partie principes](/cours/coder-et-développer/programmation-évènementielle/principes){.interne}
- faites [le projet Arkanoïd](/cours/coder-et-développer/programmation-évènementielle/projet-arkanoid/){.interne} pour vous mettre dans le bain.

Ensuite, le sujet de DM proprement dit (c'est le DS de code de 2021/22) est là : [DM4 sujet](./annales/2021-2022/ds_2_sujet/){.interne}

Vous devrez rendre :

- votre code
- un fichier markdown avec l'explicitation des différentes étapes que vous avez effectuées

Enfin, pour bien faire (mais c'est optionnel), vous pouvez faire comme les grands et utiliser [un environnement virtuel](/cours/coder-et-développer/environnements-virtuels/){.interne} dans votre projet où vous placerez uniquement les modules nécessaires au projet. Si vous décidez de faire cette partie, il faudra ajouter à votre projet le fichier `requirement.txt`{.fichier}. **N'ajoutez pas l'interpréteur !** : le but est justement de pouvoir uniquement donner ce qui est nécessaire à sa création sur différentes environnements...

{% endattention %}

On refait de l'algorithmie :

{% aller %}

1. [Réduction de problèmes](/cours/algorithmie/problème-réduction/){.interne}
2. [Problèmes de NP](/cours/algorithmie/problèmes-NP/){.interne}
3. [Méthode de résolution de problème](/cours/algorithmie/design-algorithmes/){.interne}

{% endaller %}

### Semaine 11

> 14/04 au 18/04

{% attention %}
Test de 15min en début de cours sur **les objets, la composition, l' agrégation et l'héritage**.
{% endattention %}
{% faire %}
Sujet du test 6
{% endfaire %}

{% attention %}
Rendre DM3
{% endattention %}

On se focalise sur une méthode particulière de design d'algorithme, les algorithmes gloutons :

{% aller %}

[Algorithmes gloutons](/cours/algorithmie/design-algorithmes/algorithmes-gloutons/){.interne}

{% endaller %}

### Semaine 12

> 21/04 au 25/04

#### Mercredi : Sac à dos

Au programme, on prépare les vacances et son sac-à-dos :

{% aller %}

[Problème du sac à dos](/cours/algorithmie/problème-sac-à-dos/){.interne}

{% endaller %}

#### Vendredi : Enveloppe convexe

{% aller %}

[Problème de l'enveloppe convexe](/cours/algorithmie/enveloppes-convexes/){.interne}

{% endaller %}

### Semaine 13

{% attention %}
DS code 3h, lundi 05/05.

Sujet DS-C : [Big points](./annales/2024-2025/ds-code/){.interne}

{% endattention %}

### Semaine 14

{% attention %}
Rendre DM4 pour le vendredi 16 mai [sur amétice](https://ametice.univ-amu.fr/mod/assign/view.php?id=4081169).

{% endattention %} -->

## Annales

Les [annales des tests et contrôles](./annales){.interne} de ce cours

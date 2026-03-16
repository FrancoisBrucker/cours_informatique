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

Il est nécessaire d'avoir quelques prérequis avant de commencer ce cours, en particulier vos cours d'informatique du S1.

### Algorithmie

Avoir une notion de ce qu'est une variable, une instruction et une fonction. Aucun autre prérequis algorithmique n'est nécessaire.

### Programmation

Il est nécessaire d'avoir des bases de python pour commencer ce cours.

## Cours

Le cours est disponible via le site d'AMeTICE et en suivant les liens de chaque partie ci-après. Cela ne vous dispense pas de prendre des notes, mais vous aide à la révision ou aux divers prérequis que vous aurez à préparer avant le cours.

## Plan

Ce cours est composée de plusieurs parties :

- Notion d'algorithmie
- Complexité d'un complexité
- Structures de données
- Programmation objet

<!-- TBD 2026/27

Cours en 4 parties et 4 DM :

1. cours intro : DM algo : écrire des algorithmes en python et vérifier expérimentalement leur véracité (faire les monolignes et des exercices sur les import)
   1. pseudo-code (6h)
   2. projets et tests (4h) 
2. cours algo (complexité) et DM code (test/projet/)
3. cours programmation (objet) et DM algo (et de l'année précédente)
4. cours algo (structures de données) et DM code (bataille navale)

-->

### Semaine 1

> 19/01 au 23/01
>
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
[bases théoriques de l'algorithmie](/cours/algorithmie/bases-théoriques){.interne}
{% endaller %}


<!-- TBD 2026/27

Donner un premier DM avec les bases de python du S1.

Utilisations de :

- objets, fonctions (et lambdas)
- listes et dictionnaires

Avec de petits algos
-->

#### Vendredi : écrire des algorithmes

> 4h

Notions abordées :

- écrire des algorithme en pseudo-code (et thèse de Church-Turing)
- algorithmes itératif et récursifs
- prouver un algorithme

{% aller %}
1. [Écrire des algorithmes en pseudo-code](/cours/algorithmie/pseudo-code){.interne}
2. [Prouver des algorithmes](/cours/algorithmie/prouver-un-algorithme/){.interne}
{% endaller %}
  
Si on a le temps, sinon à faire chez soit :

{% aller %}
[On s'entraîne](/cours/algorithmie/projet-itératif-récursif/){.interne}
{% endaller %}

Pour aller plus loin :

{% aller %}

- [exercices non corrigés](/cours/algorithmie/exercices-itératif-récursif){.interne}
- [Projet : techniques de récursion](/cours/algorithmie/projet-techniques-de-récursion){.interne}

{% endaller %}

<!-- TBD année prochaine 

mettre un DM d'algo pour vérifier que Ok niveau algo base.

prog sur l'année en 4 séquences alternée :

1. code et DM algo  de production d'algorithmes idiots en python
2. algo et DM code  de bonnes pratiques avec tests/code etc.
3. code et DM algo  ET de l'année passée
4. algo et DM code  ET de l'année passée
-->

### Semaine 2

> 26/01 au 30/01
> 
> Programmation

Il est **INDISPENSABLE** que vous ayez en tête ce que vous avez fait en développement au S1. Pour cela, suivez et faite la partie suivante du cours qui explicite les notions qui vous seront utiles pour débuter ce semestre :

{% prerequis "**PRÉREQUIS**" %}
1. [Utilisez le réseau EDUROAM](/enseignements/MPCI/outil-informatique/#eduroam){.interne}
2. [Bases de programmation en python](/cours/coder-et-développer/bases-programmation/){.interne}
{% endprerequis %}

#### Mercredi : projet de développement

> 2h

{% attention %}
Test de 15min **sur feuille** en début de cours sur les bases théoriques d'un algorithme et la preuve d'algorithme.
{% endattention %}

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

<!-- TBD

Faire numpy

-->

#### Vendredi : exercices

> 2h

{% aller %}
1. [tester son code](/cours/coder-et-développer/tests-unitaires/){.interne}
2. [Développer un projet informatique](/cours/coder-et-développer/écrire-code/tutoriel-hello-dev/){.interne}
3. [Projet pourcentages](/cours/coder-et-développer/projet-pourcentages){.interne}
{% endaller %}

<!-- TBD

Supprimer le linter du cours, mais insister sur black.

-->


Si on a le temps, sinon à faire chez soit :

{% aller %}
[Petits programmes](/cours/coder-et-développer/projet-codes/){.interne} et [on leur ajoute des tests](/cours/coder-et-développer/projet-codes-tests/){.interne}
{% endaller %}

Pour aller plus loin :

{% aller %}
1. [écrire du code lisible et maintenable](/cours/coder-et-développer/écrire-code/coder/){.interne}
2. [déboguer son code](/cours/coder-et-développer/débogueur/){.interne}
{% endaller %}

### Semaine 3

> 02/02 au 06/02
> Algorithmie

#### Mercredi matin : complexité

> 2h

{% attention %}
Test de 15min **sur ordinateur** en début de cours sur l'écriture de projets informatique.
{% endattention %}

Notions abordées :

- définition
- complexité spatiale et temporelle
- calculs de $\mathcal{O}$ et cas particulier de $\mathcal{O}(1) = \Theta(1) = \Omega(1)$
- différence et usage de $\Theta$, $\Omega$ et $\mathcal{O}$
- règles pour calculer la complexité d'algorithmes itératifs et récursifs

{% aller %}

[Complexité d'un algorithme](/cours/algorithmie/complexité-calculs/){.interne}

{% endaller %}

#### mercredi après-midi : exercices

> 2h

{% aller %}

[Projet : calculs de complexité d'un algorithme](/cours/algorithmie/projet-calcul-complexite/){.interne}

{% endaller %}

<!-- TBD 

Faire une séance de code en pair programming pour mettre en place les mesures de temps d'exécution de code. Avec recherche dun élément dans un tableau :

1- max : O(n)
2- trié : O(1)
3- max et min : voir la différence physique mais pas en courbe

-->

### Semaine 4

> 16/02 au 20/02
> Algorithmie

#### Mercredi : complexité d'un problème

> 2h

{% attention %}
Test de 15min **sur feuille** en début de cours sur le calcul de complexités d'un algorithme.
{% endattention %}

Notions abordées :

- complexité d'un problème
- comment trouver une borne minimum

{% aller %}

[Complexité d'un problème](/cours/algorithmie/complexité-problème/){.interne}

{% endaller %}

Si on a le temps, sinon à faire chez soit :

{% aller %}

[Projet : Complexité d'un problème](/cours/algorithmie/projet-complexité-problème/){.interne}

{% endaller %}

Pour aller plus loin :

{% aller %}

[exercices sur le problème du doublon](/cours/algorithmie/exercices-problème-doublons/){.interne}

{% endaller %}

#### Jeudi : problème de l'exponentiation

> 2h

<!-- TBD 2026/2027

- faire tout en une fois cours théorique et TP sus la forme d'un cours en incorporant des bouts du tri pour les calculs. Le faire sous la forme d'un cours à copier/coller.
- ajouter la représentation graphique
- faire un DM simple de code + algo

 -->

{% aller %}

[Problème de l'exponentiation](/cours/algorithmie/projet-exponentiation/étude-algorithmique/){.interne}

{% endaller %}

Si on a le temps, on commencera le DM :

{% faire %}
DM1 : faire la partie [Implémentation de l'exponentiation](/cours/algorithmie/projet-exponentiation/implémentation-code/){.interne}

**Corrigé :** Le 20 février début d'après-midi.
{% endfaire %}
{% info %}
[Correction du projet de Code](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/algorithmie/projet-exponentiation/impl%C3%A9mentation-code/exponentiation)
{% endinfo %}


Pour aller plus loin :

{% aller %}
[Suite additives](/cours/algorithmie/projet-suite-additive/){.interne}
{% endaller %}

### Semaine 5

> 09/02 au 13/02
> Algorithmie

#### Mercredi : tris

> 4h

{% attention %}
Test de 15min **sur papier** en début de cours sur la complexité de problèmes informatique.
{% endattention %}


{% aller %}

1. [Complexité en moyenne](/cours/algorithmie/complexité-moyenne/){.interne}
2. [Problème du tri](/cours/algorithmie/problème-tris/){.interne}

{% endaller %}
{% info %}
[Correction du projet de Code](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/algorithmie/probl%C3%A8me-tris/projet-tris/tris)
{% endinfo %}

<!-- TBD 2026/2027

- faire une séance supplémentaire.
- complexité en moyenne
- uniquement tris basiques 
- TP tris basiques. Avec des rappels à l'exponentiation.
- ajouter une séance de :
  - calculs de sommes et de récursions
  - 1h sur les tris rapide et fusion 

 -->


#### Vendredi : correction du DM

> 2+h

{% attention %}
Cette séance n'est pas dans l'emploi du temps. **Elle commence à 13h30 dans votre salle** 
{% endattention %}

Séance facultative. Venez si vous voulez voir la correction du DM et/ou avez des questions d'ordre algorithmique/code.

### Semaine 6

> 2h
>

{% attention %}
Devoir surveillé d'algorithmie. Le programme est tout ce qu'on a vu jusqu'à présent
{% endattention %}

Pour accélérer vos calculs de complexité :

{% aller %}

1. [Calculer des sommes pour la complexité d'algorithmes itératifs](/cours/algorithmie/projet-sommes-classiques/){.interne}
2. [Calculer des équations pour la complexité d'algorithmes récursifs](/cours/algorithmie/projet-équations-classiques/){.interne}

{% endaller %}

Pour vous entraîner sur des exercices classiques :

{% aller %}

[Algorithmes classiques](/cours/algorithmie/projet-algorithmes-classiques/){.interne}

{% endaller %}

Enfin, pour aller plus loin, n'hésitez pas à vous entraîner sur les DS1 des années précédentes dans [les annales](./#annales){.interne}. Comme toujours, faites les exercices avant de regarder les corrigés et qui sait vous allez peut-être même y prendre du plaisir, certains exercices étant diablement jolis.


### Semaine 7

> 9/03 au 13/03
> Programmation


{% faire %}
DM2 : faire l'ET d'Algorithmie de l'année dernière : [sujet examen terminal algorithmie 2025](/enseignements/MPCI/programmation-algorithmes/annales/2024-2025/et-algo/){.interne}

{% endfaire %}
{% info %}
**Corrigé :** Le 3 avril 13h30.
{% endinfo %}

#### Mercredi : programmation objet

> 2h
>

{% aller %}

1. [Classes et objets](/cours/coder-et-développer/programmation-objet/classes-et-objets/){.interne}
2. [Coder ses objets](/cours/coder-et-développer/programmation-objet/coder-ses-objets/){.interne}

{% endaller %}


#### Vendredi : on s'entraîne

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

Si on a le temps, sinon à faire chez soit :

{% aller %}

- Cours : [Améliorer ses objets](/cours/coder-et-développer/programmation-objet/améliorer-ses-objets/){.interne}
- Projets associés :
  - [Améliorer les dés](/cours/coder-et-développer/programmation-objet/projet-objets-dés-accesseur/){.interne}
  - [Améliorer les cartes](/cours/coder-et-développer/programmation-objet/projet-objets-cartes-value-object/){.interne}

{% endaller %}

### Semaine 8

> 16/03 au 20/03
> Programmation

#### Mercredi : Composition et agrégation

> 2h
>

{% attention %}
Test de 15min **sur papier** en début de cours sur les classes et les objets.
{% endattention %}

#### Vendredi : on s'entraîne

> 2h
>

### Semaine 9

> 23/03 27/03
> Programmation

#### Mercredi : héritage

> 2h
>

{% attention %}
Test de 15min **sur ordinateur** en début de cours sur la composition et l'agrégation
{% endattention %}


Cours Valentin :
- [héritage](./heritage){.interne}

> pour aller plus loin : design pattern

#### Vendredi : on s'entraîne

> 2h
>

### Semaine 10

> 30/03 au 3/04
> Algorithmie


> TBD DM3 : et code de l'année dernière

#### Mercredi : structures de données

> 4h
>

- structures de données.


#### Vendredi : on s'entraîne

> 2h
>

- pile/file et listes chaînées. Cours puis exercices dessus.

> TBD correction DM2 séance facultative.

### Semaine 11

> 16/03 au 20/03
> Algorithmie

#### Mercredi : listes

> 2h
>

{% attention %}
Test de 15min **sur papier** en début de cours sur les structures de données.
{% endattention %}

#### Vendredi : dictionnaires

> 2h
>

### Semaine 11

> 13/04 au 17/04
> Algorithmie

#### Mercredi : Problème de l'enveloppe convexe

{% attention %}
Test de 15min **sur ordinateur** en début de cours sur la composition et l'agrégation.
{% endattention %}

#### Vendredi : on s'entraîne

> TBD avec pyglet et/matplotlib

> TBD DM3 et code de l'année dernière

### Semaine 12

> 2h
>

{% attention %}
Devoir surveillé de programmation. Le programme est tout ce qu'on a vu jusqu'à présent
{% endattention %}


### Semaine 13

> 04/05 au 08/05
> Programmation

> présrequis : avoir fait du html/css/js pendant les vacances. En faire un DM.

#### Mercredi : serveur web et réseau

#### Vendredi : on s'entraîne




<!-- TBD

Complexité et preuves d'algorithmes sur feuille et implémentation. On vérifie que la complexité est cohérente avec celle calculée.

- mesure de complexité en code
- complexité en moyenne

 -->




<!-- TBD

- <https://efrei.poupa.net/Programmation%20en%20C++/Exercices_et_problemes_d_algorithme.pdf>
- <https://perso.liris.cnrs.fr/pierre-antoine.champin/enseignement/algo/exercices/>
- <https://imag.umontpellier.fr/~lacour/exo_algo.pdf>
- <https://wiki.sfeir.com/carriere/recrutement/evaluation-algo/exemple_exercices_algo/>
- <https://fabien-torre.fr/Enseignement/Exercices/algo-exos.php>
- <https://www.youtube.com/playlist?list=PLZpzLuUp9qXzOgDakYP0UAGIBNk0pPdvZ>

-->

<!-- 


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

## <span id="annales"></span>Annales

Les [annales des tests et contrôles](./annales){.interne} de ce cours

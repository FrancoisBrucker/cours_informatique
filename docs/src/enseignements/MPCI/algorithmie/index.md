---
layout: layout/post.njk
title: "S2 : Algorithmie 1 (bases)"

tags: ["formation", "MPCI"]

eleventyNavigation:
  order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Ce cours intitulé _Algorithmie_ est donné au second semestre de la licence MPCI ([lien AMeTICE AMU Informatique S2](https://ametice.univ-amu.fr/course/view.php?id=129120){.externe}).

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

Il est nécessaire d'avoir quelques prérequis avant de commencer ce cours, en particulier vos cours d'informatique du S1 qui vous permettrons de coder en python les différents algorithme que ous allons étudier.

 Tout ce dont vous aurez besoin est également disponible dans le cours cours ci-après :

{% prerequis "**Acquis du S1**" %}
[Fondements de la programmation (avec Python)](/cours/coder-et-développer/apprendre-programmation/concepts/)
{% endprerequis %}

Programmer nécessite d'utiliser le web pour lire la doc, técharger des modules, etc. Configurez votre ordinateur pour qu'il puisse utiliser le réseau universitaire EDUROAM :

{% lien %}
[Utilisez le réseau EDUROAM](/enseignements/MPCI/outil-informatique/#eduroam)
{% endlien %}


## Cours

Le cours est disponible via le site d'AMeTICE et en suivant les liens de chaque partie ci-après. Cela ne vous dispense pas de prendre des notes, mais vous aide à la révision ou aux divers prérequis que vous aurez à préparer avant le cours.

## Plan

Ce cours est composée de plusieurs parties :

- Notion d'algorithmie
- Complexité d'un complexité
- Structures de données

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

### Semaine 1

#### Mercredi : qu'est-ce qu'un algorithme

> 2h

Notions abordées :

- définition d'un programme et d'un algorithme
- savoir ce que fait un programme : 
  - il faut toujours démonter qu'un programme s'arrête
  - il faut toujours démontrer ce que fait un algorithme
- ce que ne peut pas faire un algorithme

{% aller %}
[bases théoriques de l'algorithmie](/cours/algorithmie/bases-théoriques)
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
1. [Écrire des algorithmes en pseudo-code](/cours/algorithmie/pseudo-code)
2. [Prouver des algorithmes](/cours/algorithmie/prouver-un-algorithme/)
{% endaller %}
  
Si on a le temps, sinon à faire chez soit :

{% aller %}
[On s'entraîne](/cours/algorithmie/projet-itératif-récursif/)
{% endaller %}

Pour aller plus loin :

{% aller %}

- [exercices non corrigés](/cours/algorithmie/exercices-itératif-récursif)
- [Projet : techniques de récursion](/cours/algorithmie/projet-techniques-de-récursion)

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


{% prerequis %}

1. Rappels : [créer un projet python avec vscode](/cours/coder-et-développer/bases-programmation/éditeur-vscode/)
2. [Bases de système d'exploitation](/cours/système-et-réseau/bases-système/)
3. [Modules externes python](/cours/coder-et-développer/modules-externes-python/)
4. [tester son code](/cours/coder-et-développer/tests-unitaires/)
5. [Développer un projet informatique](/cours/coder-et-développer/écrire-code/tutoriel-hello-dev/)

{% endprerequis %}

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

[Complexité d'un algorithme](/cours/algorithmie/complexité-calculs/)

{% endaller %}

#### mercredi après-midi : exercices

> 4h

{% aller %}

1. [TD : calculs de complexité d'un algorithme](/cours/algorithmie/projet-calcul-complexite/)
2. TP ajouter des TP avec python pour vérifier la complexité.

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

[Complexité d'un problème](/cours/algorithmie/complexité-problème/)

{% endaller %}

Si on a le temps, sinon à faire chez soit :

{% aller %}

[Projet : Complexité d'un problème](/cours/algorithmie/projet-complexité-problème/)

{% endaller %}

Pour aller plus loin :

{% aller %}

[exercices sur le problème du doublon](/cours/algorithmie/exercices-problème-doublons/)

{% endaller %}

#### Jeudi : problème de l'exponentiation

> 2h

<!-- TBD 2026/2027

- faire tout en une fois cours théorique et TP sous la forme d'un cours en incorporant des bouts du tri pour les calculs. Le faire sous la forme d'un cours à copier/coller.
- ajouter la représentation graphique
- faire un DM simple de code + algo

 -->

{% aller %}

[Problème de l'exponentiation](/cours/algorithmie/projet-exponentiation/étude-algorithmique/)

{% endaller %}

Si on a le temps, on commencera le DM :

{% faire %}
DM1 : faire la partie [Implémentation de l'exponentiation](/cours/algorithmie/projet-exponentiation/implémentation-code/)

**Corrigé :** Le 20 février début d'après-midi.
{% endfaire %}
{% info %}
[Correction du projet de Code](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/algorithmie/projet-exponentiation/impl%C3%A9mentation-code/exponentiation){.externe}
{% endinfo %}


Pour aller plus loin :

{% aller %}
[Suite additives](/cours/algorithmie/projet-suite-additive/)
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

1. [Complexité en moyenne](/cours/algorithmie/complexité-moyenne/)
2. [Problème du tri](/cours/algorithmie/problème-tris/)

{% endaller %}
{% info %}
[Correction du projet de Code](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/algorithmie/probl%C3%A8me-tris/projet-tris/tris){.externe}
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

1. [Calculer des sommes pour la complexité d'algorithmes itératifs](/cours/algorithmie/projet-sommes-classiques/)
2. [Calculer des équations pour la complexité d'algorithmes récursifs](/cours/algorithmie/projet-équations-classiques/)

{% endaller %}

Pour vous entraîner sur des exercices classiques :

{% aller %}

[Algorithmes classiques](/cours/algorithmie/projet-algorithmes-classiques/)

{% endaller %}

Enfin, pour aller plus loin, n'hésitez pas à vous entraîner sur les DS1 des années précédentes dans [les annales](./#annales). Comme toujours, faites les exercices avant de regarder les corrigés et qui sait vous allez peut-être même y prendre du plaisir, certains exercices étant diablement jolis.

### Semaine 11

> 6/04 au 10/04
> Algorithmie

{% attention %}
La séance du mardi 7 avril pour le groupe B est reportée au vendredi 10 à 8h.
{% endattention %}

{% faire %}
DM3 : faire l'ET de programmation de l'année dernière : [sujet examen terminal programmation 2025](/enseignements/MPCI/programmation-algorithmes/annales/2024-2025/2025-05-26_L1S2_programmation_ET.pdf)

{% endfaire %}

#### Jeudi : structures de données

> 2h
>

{% aller %}

[Structures matricielles](/cours/algorithmie/structure-matricielle/)

{% endaller %}


#### Vendredi : structures linéaires

> 4h
>

{% aller %}

1. [Structures de données](/cours/algorithmie/structure-données/)
2. [pile et files](/cours/algorithmie/structure-pile-file/)
3. [listes chaînées](/cours/algorithmie/structure-liste-chaînée/)

{% endaller %}


### Semaine 12

> 13/04 au 17/04
> Algorithmie

{% info %}
La séance facultative de correction du DM prévue le 17 avril (à 13h30) est annulée.
{% endinfo %}

#### Mercredi : Listes


{% aller %}

1. [Structures de liste](/cours/algorithmie/structure-liste/)
2. [Complexité amortie](/cours/algorithmie/complexité-amortie/)

{% endaller %}

#### Vendredi : Dictionnaires

{% aller %}

1. [Structures de dictionnaire](/cours/algorithmie/structure-dictionnaire/)
2. [Comparaisons des complexités des structures](/cours/algorithmie/structures-complexité)

{% endaller %}

Si on a le temps, sinon à faire chez vous :

{% aller %}

[Projet Liste et dictionnaires](/cours/algorithmie/projet-liste-dictionnaire/)

{% endaller %}

### Semaine 13

> 27/04 au 1/05
> Programmation

{% attention %}
Devoir surveillé de programmation. Le programme est tout ce qu'on a vu jusqu'à présent
{% endattention %}


<!-- TBD

Complexité et preuves d'algorithmes sur feuille et implémentation. On vérifie que la complexité est cohérente avec celle calculée.

- mesure de complexité en code
- complexité en moyenne


- <https://efrei.poupa.net/Programmation%20en%20C++/Exercices_et_problemes_d_algorithme.pdf>{.externe}
- <https://perso.liris.cnrs.fr/pierre-antoine.champin/enseignement/algo/exercices/>{.externe}
- <https://imag.umontpellier.fr/~lacour/exo_algo.pdf>{.externe}
- <https://wiki.sfeir.com/carriere/recrutement/evaluation-algo/exemple_exercices_algo/>{.externe}
- <https://fabien-torre.fr/Enseignement/Exercices/algo-exos.php>{.externe}
- <https://www.youtube.com/playlist?list=PLZpzLuUp9qXzOgDakYP0UAGIBNk0pPdvZ>{.externe}

{% info %}
[Suivre le tutoriel Markdown](/tutoriels/format-markdown/)
{% endinfo %}

-->




## Annales

Le cours était lié au cours de programmation. Les annales concernent donc les 2 matières. Prenez celle qui concerne l'algorithmie.

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

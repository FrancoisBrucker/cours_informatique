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
    - /cours/utiliser-python/
    - https://ametice.univ-amu.fr/course/view.php?id=97114

---

Ce cours intitulé *Programmation et algorithmes* est donné au second semestre de la licence MPCI ([lien AMeTICE AMU Informatique S2](https://ametice.univ-amu.fr/course/view.php?id=119143)). Il s'appuie sur le  cours de *Programmation* donné au S1 ([lien AMeTICE AMU Informatique S1](https://ametice.univ-amu.fr/course/view.php?id=113169)).

Ce cours montrera l'informatique sous trois aspects complémentaires — théorie, code et algorithmes — que tout [honnête informaticien](https://fr.wikipedia.org/wiki/Honn%C3%AAte_homme) devrait connaître. Il s'adresse à des personnes ayant des connaissances minimales en informatiques mais voulant (ou étant obligé d' :-)) approfondir le sujet. Nous rentrerons dans les détails tant d'un point de vue algorithmique (Tout algorithme sera démontré) que d'un point de vue code (on montrera comment un programme s'exécute sur un ordinateur).

L'informatique est une science incarnée : elle nécessite à la fois de solides connaissances théoriques pour concevoir des des algorithmes efficaces et des capacités d'expérimentations et de rigueur pour les mettre en oeuvre et les faire fonctionner sur un ordinateur.

Cela va vous demander un travail personnel important pour comprendre et assimiler les bases théoriques **et** un temps certain d’expérimentation pour faire fonctionner le tout sur votre ordinateur en comprenant pourquoi et comment cela fonctionne.

## Note

La note de cette UE résulte de cette formule :

$$
\max (\frac{CC+ DS + ET}{3}, ET)
$$

Avec :

- $CC = \frac{1}{2}(TUT + TEST)$ où :
  - $TUT$  est la moyenne formée des 2 notes de tutorats
  - $TEST$ est la moyenne des tests de débuts de séances ($6$ tests).
- $DS$ est la moyenne des deux devoirs surveillées (DS1 et DS2)
- $ET$ est l'examen terminal

## Prérequis

Il est nécessaire d'avoir quelques prérequis avant de commencer ce cours.

### Algorithmie

Avoir une notion de ce qu'est une variable, une instruction et une fonction. Aucun autre prérequis algorithmique n'est nécessaire.

### Programmation

Il est nécessaire d'avoir des bases de python pour commencer ce cours. Il est **indispensable** que vous relisez le cours ci-après pour s'assurer que vous avez bien les bases nécessaires en programmation python pour commencer ce cours :

{% aller %}
[Bases de python](/cours/coder-et-développer/bases-python/){.interne}
{% endaller %}

## Cours

Le cours est disponible via le site d'AMeTICE et en suivant les liens de chaque partie ci-après. Cela ne vous dispense pas de prendre des notes, mais vous aide à la révision ou aux divers prérequis que vous aurez à préparer avant le cours.

## Plan

Ce cours est composée de plusieurs parties :

- Notion d'Algorithmie
- Complexité d'un complexité
- Structures de données
- Programmation objet
- Méthodes de résolution de problèmes

### Semaine 1

#### Mardi : qu'est-ce qu'un algorithme

{% aller %}
[bases théorique de l'algorithmie](/cours/algorithmie/bases-théoriques){.interne}
{% endaller %}

#### Vendredi : qu'est-ce que le code

{% faire "**Prérequis**" %}

- [avoir python d'installé](/cours/coder-et-développer/installer-python/#installation-développement){.interne} et savoir s'en servir (relisez la partie [bases de python](/cours/coder-et-développer/bases-python/){.interne})
- fait le tutoriel de [prise en main de l'éditeur vscode](/cours/coder-et-développer/éditeur-vscode/prise-en-main/){.interne}

{% endfaire %}
{% info %}
N'hésitez pas à poser des questions en début de cours si vous avez des questions concernant les prérequis.
{% endinfo %}

Parties abordées :

{% aller %}

1. [Connaissances indispensables](/cours/coder-et-développer/ordinateur-développement/#connaissances-indispensables){.interne}
2. [écrire du code](/cours/coder-et-développer/développement/){.interne}, les parties :
   1. [coder](/cours/coder-et-développer/développement/coder){.interne}
   2. [projet `hello dev`](/cours/coder-et-développer/développement/tutoriel-hello-dev){.interne}

{% endaller %}

### Semaine 2

#### Mardi : écrire des algorithmes

{% aller %}
[Écrire des algorithmes](/cours/algorithmie/écrire-algorithmes){.interne}{.interne}
{% endaller %}

#### Vendredi : écrire du code

{% faire "**Prérequis**" %}

Lire [Mémoire et espace de noms](/cours/coder-et-développer/mémoire-espace-noms/){.interne}

{% endfaire %}

{% aller %}

1. Fin de [la partie écrire du code](/cours/coder-et-développer/développement/){.interne} :
   3. [projet pourcentages](/cours/coder-et-développer/développement/projet-pourcentages/){.interne}
2. [Déboguer ses programmes](/cours/coder-et-développer/debugger/){.interne}
3. Pour aller plus loin : anales test code des années précédentes.

{% endaller %}

On vous remettra également le premier DM à rendre sur AMeTICE au format Markdown.

{% faire %}
[Sujet du DM](./annales/2023-2024/palindromes/)

Il faudra rendre un dossier contenant :

- un dossier contenant le rendu de la partie algorithmie. Il devra être sous la forme d'un fichier markdown et de sa conversion en html.
- un dossier contenant le rendu de la partie code contenant le projet vscode et les différents programmes.

{% endfaire %}
{% info %}
[Suivre le tutoriel Markdown](/tutoriels/format-markdown/){.interne}
{% endinfo %}

### Semaine 3

#### Mardi : complexité algorithmique

{% faire "**Prérequis**" %}
Reprendre la partie complexité de votre cours de S1. Ce dont nous aurons besoin est rassemblé là :

1. [définition de la complexité](/cours/algorithmie/complexité-calculs/définitions){.interne}
2. [comparaisons asymptotiques](/cours/algorithmie/complexité-calculs/comparaisons-asymptotiques){.interne}
{% endfaire  %}
{% info %}
N'hésitez pas à poser des questions en début de cours si vous avez des questions concernant les prérequis.
{% endinfo %}

Parties abordées :

{% aller %}

1. [$\mathcal{O}$ pour l'algorithmie](/cours/algorithmie/complexité-calculs/O-pour-l-algorithmie){.interne}
2. [règles de calculs](/cours/algorithmie/complexité-calculs/règles-de-calcul){.interne}
3. [complexités des structures et des méthodes](/cours/algorithmie/complexité-calculs/méthodes-structures-calcul){.interne}
4. [Complexité d'un problème Algorithmique](/cours/algorithmie/complexité-problème/){.interne}

{% endaller %}

#### Vendredi : étude de l'exponentiation

{% attention %}
Test de 15min en début de cours. Il faudra rendre plusieurs fichiers python (code et tests) sur AMeTICE.
{% endattention %}

{% aller %}

1. [Calculer $x^y$](/cours/algorithmie/projet-exponentiation){.interne}
2. Pour aller plus loin : [Les suites additives](/cours/algorithmie/projet-suite-additive){.interne}

{% endaller %}

### Semaine 4

{% attention %}
Test de 15min en début de cours. Il faudra rendre plusieurs fichiers python (code et tests) sur AMeTICE.
{% endattention %}

Semaine consacrée au tris :

{% aller %}

[Problème du tri](/cours/algorithmie/problème-tris){.interne}

{% endaller %}

### Semaine 5

- mardi :
  - début de la partie programmation objet
  - rendu du premier DM
- Vendredi : Premier DS sur table de 3h.

## Annales

Les [annales des tests et contrôles](./annales){.interne} de ce cours

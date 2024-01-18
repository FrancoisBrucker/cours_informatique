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

Ce cours intitulé *Programmation et algorithmes* est donné au second semestre de la licence MPCI ([lien AMeTICE AMU](https://ametice.univ-amu.fr/course/view.php?id=119143)). Il s'appuie sur le  cours de *Programmation* donné au S1 ([lien AMeTICE AMU](https://ametice.univ-amu.fr/course/view.php?id=113169)).

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

## Plan

Ce cours est composée de plusieurs parties :

- Notion d'Algorithme
- Complexité d'un complexité
- Structures de données
- Programmation objet
- Méthodes de résolution de problèmes

### Semaine 1

1. mardi : définition d'un algorithme
2. vendredi :
   1. **prérequis** :
      - Lire [Mémoire et espace de noms](/cours/coder-et-développer/mémoire-espace-noms/){.interne}
      - [avoir python d'installé](/cours/coder-et-développer/installer-python/#installation-développement){.interne}
      - fait le tutoriel de : [prise en main de l'éditeur vscode](/cours/coder-et-développer/éditeur-vscode/prise-en-main/){.interne}
   2. le code et comment coder :
      - questions sur les prérequis
      - [Connaissances indispensables](/cours/coder-et-développer/ordinateur-développement/#connaissances-indispensables){.interne}
      - [écrire du code](/cours/coder-et-développer/développement/){.interne}

### Semaine 2

1. mardi : Propriétés théoriques d'un algorithme
2. vendredi : [écrire du code](/cours/coder-et-développer/développement/){.interne}, fin

On vous remettra également le premier DM à rendre sur AMeTICE au format Markdown.

### Semaine 3

{% attention %}
Test de 15min en début de cours. Il faudra rendre plusieurs fichiers python (code et tests) sur AMeTICE.
{% endattention %}

- complexité
- étude et projet exponentiation rapide

### Semaine 4

{% attention %}
Test de 15min en début de cours. Il faudra rendre plusieurs fichiers python (code et tests) sur AMeTICE.
{% endattention %}

Semaine sur les tris.

### Semaine 5

- mardi :
  - début de la partie programmation objet
  - rendu du premier DM
- Vendredi : Premier DS sur table de 3h.

## Annales

Les [annales des tests et contrôles](./annales){.interne} de ce cours

---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: Méthode de développement
tags: ['enseignement', 'ECM']

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


(18 + 3)h heures de cours pour apprendre le python objet, les bases de la gestion des sources avec git et la programmation par les tests. C'est la suite de ce que vous avez fait en 1A avec JEMNEP et I1 de MIE en 2A. Donc revenez en arrière s'il vous manque des connaissances.

# Partie I : Travail préparatoire

> 6h

{% info %}
Cette partie est un condensé du cours de [MIE-I1](/enseignements/ecm/2A/cdp/){.interne}. Si vous voulez plus de contenu, n'hésitez pas à y jeter un coup d'œil.
{% endinfo %}

## Interpréteur, terminal et IDE

{% aller %}
1. Interagir avec le système :
   1. [Naviguer dans un système de fichiers](/cours/système/interagir-avec-système/fichiers-dossiers/){.interne}
   2. [Terminal](/cours/système/interagir-avec-système/terminal/){.interne}
2. [Installer un interpréteur et un IDE](/cours/coder-et-développer/apprendre-programmation/coder-projets/outils/){.interne}
{% endaller %}

## structure d'un projet informatique

{% aller %}
1. Séparer code et fonctions en [créant ses propres modules](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/création-modules/){.interne}
2. [Tester ses fonctions](/cours/coder-et-développer/apprendre-programmation/coder-projets/outils/){.interne}
{% endaller %}

## Gestion des dépendances

{% aller %}
1. [création d'un environnement virtuel](/cours/coder-et-développer/apprendre-programmation/gestion-dépendances/environnements-virtuels/){.interne} pour ses projets
2. mettre son code à disposition via un [Dépôt](/cours/gestion-des-sources/dépôt/){.interne} sur github.

{% endaller %}

## Programmation objet en python

{% aller %}
1. [Classes et objets](/cours/coder-et-développer/apprendre-programmation/programmation-objet/classes-et-objets/){.interne}
2. [Composition et agrégation](/cours/coder-et-développer/apprendre-programmation/programmation-objet/composition-agrégation/){.interne}
{% endaller %}

## Outils python de gestion de package

- [poetry](https://python-poetry.org/)
- [uv](https://docs.astral.sh/uv/)

# Partie II

> 6h

## Test Driven Development

{% aller %}
[Test Driven Development](/cours/coder-et-développer/Perfectionnement/TDD/){.interne}
{% endaller %}

<!-- TBD 

<https://www.youtube.com/watch?v=gnrBqLbj1_Q> 

-->

## À faire 

Pour la prochaine fois, trois groupes :

- tests dans d'autres langages (java, js ou ts, ...)
- test pattern et refactoring pattern
- mock et tests


# Partie III

> 3h

> Design Pattern

# Partie IV

> 3h

> git vscode et en ligne de commande

<!-- TBD 

> 3a docker <https://www.youtube.com/watch?v=b0HMimUb4f0> 

-->
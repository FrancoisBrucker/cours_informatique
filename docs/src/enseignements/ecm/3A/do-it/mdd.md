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

> 3+h

## Rappel

Remise en jambe de ce que vous avez du voir en I1-MIE. Si trop de personne n'ont pas suivi (ou ne se rappellent pas), cette partie prendra plus de temps.

{% aller %}
[Méthode de développement I1-MIE](/enseignements/ecm/2A/cdp/){.interne}
{% endaller %}

## Gestion des dépendances

{% aller %}
1. [création d'un environnement virtuel](/cours/coder-et-développer/apprendre-programmation/gestion-dépendances/environnements-virtuels/){.interne} pour ses projets
2. mettre son code à disposition via un [Dépôt](/cours/gestion-des-sources/dépôt/){.interne} sur github.

{% endaller %}

## À faire 

Pour la prochaine fois, trois groupes :

- [poetry](https://python-poetry.org/)
- [uv](https://docs.astral.sh/uv/)
- module et package python : comment les utiliser

Préparer un exposé de 5min chacun + support avec biblio et principales fonctionnalités.

# Partie II

> 6h

## Test Driven Development

> TDD

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

> 6h

> git vscode et en ligne de commande

<!-- TBD 

> 3a docker <https://www.youtube.com/watch?v=b0HMimUb4f0> 

-->
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

## Partie I : Travail préparatoire

> 3h

{% info %}
Cette partie est un condensé du cours de [MIE-I1](/enseignements/ecm/2A/cdp/). Si vous voulez plus de contenu, n'hésitez pas à y jeter un coup d'œil.
{% endinfo %}

### Interpréteur, terminal et IDE

{% aller %}
1. Interagir avec le système :
   1. [Naviguer dans un système de fichiers](/cours/système/interagir-avec-système/fichiers-dossiers/)
   2. [Terminal](/cours/système/interagir-avec-système/terminal/)
2. [Installer un interpréteur et un IDE](/cours/coder-et-développer/apprendre-programmation/coder-projets/outils/)
{% endaller %}

### Structure d'un projet informatique

{% aller %}
1. Séparer code et fonctions en [créant ses propres modules](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/création-modules/)
2. [Tester ses fonctions](/cours/coder-et-développer/apprendre-programmation/coder-projets/outils/)
{% endaller %}

### Gestion des dépendances

{% aller %}
1. [création d'un environnement virtuel](/cours/coder-et-développer/apprendre-programmation/gestion-dépendances/environnements-virtuels/) pour ses projets
2. mettre son code à disposition via un [Dépôt](/cours/gestion-des-sources/dépôt/) sur github.

{% endaller %}

## Partie II :  Test Driven Development

> 6h

{% prerequis %}
Vous devez pouvoir :

- utiliser un terminal
- créer et écrire  des projets en python avec la trilogie _main/fonction/tests_
- créer un environnement virtuel et d'exécuter le projet avec son python,
- ajouter des modules à l'environnement et créer son fichier `requirements.txt`{.fichier}

{% endprerequis %}

Le cours suivant va vous donner des bases de programmation objet en python :

{% aller %}
[Classes et objets](/cours/coder-et-développer/apprendre-programmation/programmation-objet/classes-et-objets/)
{% endaller %}

On va découvrir tous ces concepts via le TD suivant, dont le but est de vous former au TDD :

{% aller %}
[Test Driven Development](/cours/coder-et-développer/Perfectionnement/méthode-développement/TDD/)
{% endaller %}
{% info %}
Faite le TD de TDD dans un environnement virtuel.
{% endinfo %}

Dans un projet informatique de moyen/grand ampleur on utilisera plus que des tests unitaires. Voir par exemple le lien suivant pour une introduction aux différents tests utilisés :

{% lien %}
[Différents types de tests](https://www.youtube.com/watch?v=gnrBqLbj1_Q){.externe}
{% endlien %}


Entraînez vous :

{% faire %}

- [exercice de code](/cours/coder-et-développer/apprendre-programmation/concepts/projet-codes/)
- [advent of code](https://adventofcode.com/){.externe}

{% endfaire %}

<!-- 

Pour la prochaine fois, quatre groupes :


{% attention "**Travail à préparer**" %}


- [poetry](https://python-poetry.org/){.externe}
- [uv](https://docs.astral.sh/uv/){.externe}
- tests dans d'autres langages (java, js ou ts, ...)
- mock et tests

Préparer un exposé de 5min chacun + support avec biblio et principales fonctionnalités. 
{% endattention %}

 -->


## Partie III

> 3h

> Design Pattern

{% lien %}
- [design pattern](https://refactoring.guru/design-patterns){.externe}
- [refactoring pattern](https://refactoring.guru/refactoring){.externe}
{% endlien %}


On a vu le design pattern composite dans le projet TDD, il en existe de nombreux autres ! Découvrons en quelques uns souvent utiles :

{% aller %}
[Design pattern](/cours/coder-et-développer/Perfectionnement/méthode-développement/design-patterns/)
{% endaller %}

<!-- 

Pour la prochaine :

{% faire %}
Pour la prochaine fois, tous : choisissez un design pattern que l'on a pas  vu à présenter

Préparer un exposé de 5min chacun + support avec biblio et principales fonctionnalités. 

{% endfaire %} 

-->

## Partie IV

> 6h

> gestion du code source


{% aller %}
[Gestion du code source](/cours/gestion-des-sources/)
{% endaller %}

<!-- 
## Outils python de gestion de package

- [poetry](https://python-poetry.org/){.externe}
- [uv](https://docs.astral.sh/uv/){.externe}
 
 ->


# Partie IV

> 6h

> git vscode et en ligne de commande

<!-- TBD 

> 3a docker <https://www.youtube.com/watch?v=b0HMimUb4f0>{.externe} 

-->
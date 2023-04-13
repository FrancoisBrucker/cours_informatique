---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: "Programmation par les tests"
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 3

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD : reprendre le cours papier
> TBD : livre sur le refactoring
> TBD : livres récent ?

## Outils

### Avec python

* [Installation et prise en main de vsc]({{ '/tutoriels/vsc-installation-et-prise-en-main' | url }})
* [Utiliser python avec vsc]({{ '/tutoriels/vsc-python' | url }}). Il pourra être utile de garder sous le coude le tutoriel d'[utilisation un terminal]({{ '/tutoriels/terminal-utilisation' | url }})
* [black et code coverage]({{ "/tutoriels/style-couverture"  }})
* [Projet 1 : mise en œuvre d'un projet informatique]({{ "/cours/algorithme-code-théorie/code/projet-hello-dev"  }})

### Avec js

> TBD

## Organisation et conduite d'un projet informatique

* [Coder]({{ "/cours/algorithme-code-théorie/code/coder"  }})
* [Projet pourcentage]({{ '/cours/algorithme-code-théorie/code/projet-pourcentages' }})

## TDD

[Projet : TDD]({{ "/cours/algorithme-code-théorie/code/programmation-objet/projet-TDD"  }})

## Que tester

Tout sauf l'aléatoire (un test doit être répétable).

* mock pour les BDs ou les fonctions compliquées (TBD en pytest)
* `test_[nom du fichier que l'on teste].py`{.fichier}
  * `test_[nom de la fonction que l'on teste]`{.language-}
  * si plusieurs tests : `test_[nom de la fonction que l'on teste]_[ce que l'on teste]`{.language-}
* un test est unitaire : il doit tester une unique chose (donc si plusieurs assert, ils sot tous là pour tester une chose). Si le teste rate, son nom doit nous dire ce qui rate et la méthode et quoi dans la méthode.

## Pourquoi

* développement incrémental (code for today)
* refactoring aisé (le code évolue toujours)
* utiliser avant de créer (une fonction est là pour être utilisée)

## Comment

* il faut persévérer avant qu'on ne puisse plus s'en passer
* le faire sur tous les projets, le TDD aide même pour les petits projets, même s'il est crucial pour les gros

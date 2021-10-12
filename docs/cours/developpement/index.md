---
layout: page
title:  "Base du développement logiciel (en python)"
author: "François Brucker"
---

> [développement]({% link cours/developpement/index.md %})
{: .chemin}

On donnera ici les bases nécessaire au développement logiciel. On prendra comme langage d'application le python et on ne présupposera aucune autre connaissances que ceux en prérequis.

## Prérequis

Les connaissances et les outils que vous devez avoir pour commencer le cours.

### un ordinateur pour le développement

Pour développer, il faudra coder et exécuter du code. Il vous faut donc un ordinateur (portable ou tour) en état de marche. Il devra être sous un des trois systèmes d'exploitation suivant windows, macos ou linux.

Vous devez dans l'idéal être administrateur de votre ordinateur et avoir fait [une installation fraîche de tout votre système]({% post_url tutos/systeme/2021-09-01-installation-ordinateur %}) pour éviter toutes interférences lors de nos installations.

### connaissances système minimale

* connaitre les bases d'un système d'exploitation, [les fichiers et les dossiers]({% post_url tutos/systeme/2021-08-24-fichiers-navigation %})
* avoir accès à un [terminal]({% post_url tutos/systeme/2021-08-24-terminal %})

### base d'algorithmie

On considérera que vous avez des bases minimales en algorithmie. En particulier que vous savez ce qu'est une variable, une fonction ou un type de donnée et que vous ne vous enfuyez pas en courant quand on vous parle de faire une boucle *pour chaque* (*for*) ou *tant que* (*while*).

## Plan

### Première partie : outils de développement {#partie-1}

Langage, éditeur et petites habitude de bon code.

#### bases {#partie-1.1}

Bases du langage python et prise en main d'un éditeur de texte.

1. [installation python et vsc]({% link cours/developpement/installations.md %})
2. [bases de python]({% link cours/developpement/bases-python/index.md %})

#### méthode de développement {#partie-1.2}

Cette partie comporte deux projets pédagogique qui vous entraîneront à coder avec vscode.

1. [outils de développement]({% link cours/developpement/outils-de-developpement.md %})
2. [routine de développement]({% link cours/developpement/routine-developpement.md %})

### Deuxième partie : programmation objet

Créer et utiliser les objets et les classes en python. On montrera également les principes fondamentaux de la programmation objet que sont la composition et l'agrégation d'objet et on s'intéressera un peu à l'héritage.

1. [classes-et-objets]({% link cours/developpement/programmation-objet/classes-et-objets.md %})
2. [composition et agrégation]({% link cours/developpement/programmation-objet/composition-agregation.md %})
3. [on s'entraine]({% link cours/developpement/programmation-objet/objets-composition-agregation-exercices.md %}) ([le corrigé]({% link cours/developpement/programmation-objet/objets-composition-agregation-exercices-corrige.md %}))
4. [héritage]({% link cours/developpement/programmation-objet/heritage.md %})
5. [on s'entraine]({% link cours/developpement/programmation-objet/heritage-exercices.md %}) ([le corrigé]({% link cours/developpement/programmation-objet/heritage-exercices-corrige.md %}))
6. [programmation événementielle]({% link cours/developpement/programmation-objet/programmation-evenementielle.md %})

### Troisième partie : développement objet

1. [Test Driven Development et test pattern](tdd_et_test_pattern)
2. [design pattern]({% link cours/developpement/design-patterns.md %})

### autres

* structures avancées dict

## les références

* [installation complète de python]({% post_url /tutos/python/2021-08-20-installation-de-python %})
* [tutoriel python](https://docs.python.org/fr/3/tutorial/)
* [figures uml](./programmation-objet/plantuml.txt)

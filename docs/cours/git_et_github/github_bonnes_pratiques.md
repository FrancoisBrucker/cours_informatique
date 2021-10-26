---
layout: page
title: "git et github : les bonnes pratiques en équipe"
category: tutorial
tags: dev git github gitlab worflow
authors:
  - "Corentin Lange"
---

Ce cours suit directement celui de git et github. Une fois apte à tirer un repo, le modifier, faire des commits, il est bien de savoir comment bien le faire !

GitHub est très répandu pour le développement en équipe. Il peut-être une vraie aide à la productivité si il est bien utilisé, ou au contraire, rajouter une perte de temps et des nombreuses prises de têtes sans bonnes pratiques.

Ci-dessous quelques petits clés pour bien utiliser github ! Tout ces conseils sont fortements inspirés de projets open-source, ces derniers maintenant une relecture et des règles de participations très claires afin de permettre au maximum de personnes de participées. Un repo qui selon moi est très bien réalisé et celui du projet open-source Atom(un ide multi-languages personalisables) : [github.com/atom](https://github.com/atom/atom)

## -- Workflow --

Le "workflow", ou flux de travail en fançais (à bas les anglicismes) sont les petites règles à adopter pour avancer dans son travail dans de bonnes conditions en minimisant les potentiels pertes de temps créées par une mauvaise gestion.

Pour travailler en équipe, à l'aide de GitHub, il est bon de garder un schéma de travail harmonieux afin de faciliter la relecture des autres qui passeront derrière nous.

Je vous présente des méthodes de travaille que l'on peut retrouver afin de gagner du temps, avoir une meilleur lisibilité ainsi que une meilleure intégration continue.

### Le No-flow

C'est souvent ce qu'on utilise la première fois en se servant de git et gihub : chacun pousse sur la main lorsqu'il ou elle a rajouté une fonctionnalité, corrigé un bug, modifier une partie déjà existante.

Travailler de cette mmanière est très peu pratique pour :

- la relecture du code
- une intégration continue
- un nombre de personnes participant élevées
- éviter des conflits de merge (que l'on veut au plus souvent éviter)

Ce tutoriel est ici en grande partie pour vous montrer d'autres modes de travail afin de parfaire l'expérience et l'efficacité du travail à plusieurs sur un projet.

### Le Git Flow

## -- Les Branches --

Il existe une sémantique des branches, libre à chacun de se le réapproprier mais faire comme tout le monde ça aide souvent à la compréhension !

### main

Cette branche contient le code de production(celui actuellement utilisé sur votre produit/système fonctionnel).
Tout le code de développement(branch develop) est fusionné dans master au fur et à mesure que les features,etc... ont été dûment testées et validées.

### develop

Cette branche contient le code de pré-production. Lorsque les fonctionnalités sont terminées, elles sont fusionnées dans la branche de développement pour de futurs tests avant validation pour "partir en prod".

### feature/\*

Les branches feature sont utilisées pour développer de nouvelles fonctionnalités pour les prochaines versions. Elles peuvent être dérivées de develop et doivent être fusionnées avec develop(jamais main directement !).

On ajoute après le / le nom de la feature ajoutée, par exemple : feature/filter_dog pour l'ajout d'un filtre chien sur votre application.

### hotfix/\*

Les branches hotfix sont nécessaires pour agir immédiatement sur un statut non désiré de master. Peut se ramifier à partir de master et doit fusionner dans master et develop.

### release/\*

Les branches de version prennent en charge la préparation d'une nouvelle version de production. Elles permettent de corriger de nombreux bogues mineurs et de préparer les méta-données pour une version. Peut se ramifier à partir de develop et doit fusionner avec master et develop.

## -- Les commits --

Le nom de ses commits est aussi important, une liste de commits mals nommés peut devenir vite illisible et occasioner des pertes
de fluidité pour la relecture.

<<type>>(<<scope>>): <<subject>>
<<BLANK LINE>>

<<body>>
<<BLANK LINE>>
<<footer>>

**feature**: Ajout d’une nouvelle fonctionnalité
**bugfix**: Correction d’un bug
**hotfix**: Correction d’un bug critique
**chore**: Nettoyage du code
**experiment**: Expérimentation de fonctionnalités.

### Sémantique des commits

Pour les commits, afin de se retrouver dans cette soupe après avoir avancé longtemps dans le projet, on préfère aussi expliquer de manière très simple ce qu'un commit change.

Précédé d'un type, le tableau ci-dessous référencant les plus courants utilisés :

## -- Pull request (PR) --

Il est fortement conseillé de passer par une Pull Request à chaque fois que l'on souhaite ajouter une modification sur un projet. Il permet d'avoir une première relecture par un ou plusieurs relecteurs pouvant commenter votre code là où il ferait défaut.

Elles sont aussi un bon moyen d'apporter des infos sur une contribution, de définir à quelles issues elles répondent en les identifiants directement dans le commentaire.

## Gestion du repo - Documentation

Il est important de bien documenté son repository sur GitHub afin d'aidé à la compréhension de ce dernier : que ce soit pour un projet fermé si de nouveaux développeurs arrivent dans l'équipe, ou bien dans une dynamique open-source pour toute personne souhaitant participer au projet.

Les fichiers Markdown(.md) sont donc vos meilleurs amis pour aider à la compréhension du projet.

### Readme

On vous le suggère souvent à la création du repo, je ne vais pas m'étaler dessus ici et vous redirige vers ce site documentant bien comment faire un bon Readme -> [makeareadme.com](makeareadme.com)

### Contributing

Il est d'usage aussi de réaliser un Contributing afin d'expliquer à toutes personnes participant au code/projet comment :

- bien faire leur commits dans ce projet
- ce qui est authorisé ou non
- un "template" pour les issues
- un "template" pour les pull requests

Pour plus d'infos dessus je vous redirige vers le lien [makeareadme.com](makeareadme.com)

Je vous dirige aussi vers le CONTRIBUTING.md de Atom cité plus haut, ainsi que celui de GodotEngine(Moteur de jeux open-source) ces derniers sont très explicites et aident vraiment à obtenir des commits, pull requests de qualités étant une grande aide à toute personne souhaitant participer.

[Atom_contributing](https://github.com/atom/atom/blob/master/CONTRIBUTING.md)
[Godot_contributing](https://github.com/godotengine/godot/blob/master/CONTRIBUTING.md)

## Versioning - sémantique des versions

Pour les versions de votre projet il existe une sémantique précise.
On peut résumer cette sémantique à l'aide de ce graphe ci-dessous.

## SOURCES

https://docs.github.com/en/get-started/quickstart/github-flow
https://github.com/atom/atom
https://makeareadme.com
https://github.com/godotengine/godot/

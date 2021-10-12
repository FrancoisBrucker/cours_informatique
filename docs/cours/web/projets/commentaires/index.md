---
layout: page
title:  "Projet commentaires"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %})
{: .chemin}

Ce projet vise à munir nos serveur web de persistance de données. Côté front avec la gestion des cookies et côté back avec la mise œuvre d'une base de données.

## pré-requis

Il est recommandé d'avoir fait le niveau 1 [du projet numérologie]({% link cours/web/projets/numerologie/index.md %}) pour bien aborder ce projet.

## but du site

On va créer un site qui gère les commentaires. On va pouvoir :

* ajouter son commentaire
* consulter tous les commentaires
* consulter les commentaire d'un pseudo donné

## Plan

Ce projet va être séparé en trois parties :

1. [le site sans les données]({% link cours/web/projets/commentaires/partie-1-site/index.md %})
2. on [envoie les données]({% link cours/web/projets/commentaires/partie-2-requetes-post/index.md %}) vers le serveur
3. on ajoute une persistance front [avec des cookies]({% link cours/web/projets/commentaires/partie-3-cookies/index.md %})
4. on ajoute une persistance backend avec une [base de donnée]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/index.md %})
5. [structure]({% link cours/web/projets/commentaires/partie-5-structures/index.md %}) du site final

Chaque partie est organisée en niveaux. Chaque niveau refait la partie en ajoutant à chaque fois des outils de développements/code de plus en plus perfectionnés. Il est recommandé de faire tous les niveaux d'une partie.

## niveaux

Chaque partie est organisée en niveaux. Chaque niveau ajoutant des outils de développements/code de plus en plus perfectionnés. Ces outils seront différents selon la partie.

> TBD :
>
> * pas mettre de await dans le code de la gestion des données. Juste des then.
> * fetch qui marche pas sous firefox ?
> * environnements différents
> * scripts d'install et de run
> * utiliser une base de donnée serveur postgressql (3A)
> * test de routes avec [RESTer](https://github.com/frigus02/RESTer) (dans la partie tests, 3A)
> * séparer le serveur un plusieurs fichiers
> * séparer les routes du serveur
> * utiliser le dossier script pour la mise en prod.
> * compiler son bootstrap ?
> * gestion des routes.
{: .note}

## ressources

* <https://blog.logrocket.com/the-perfect-architecture-flow-for-your-next-node-js-project/>

---
layout: page
title:  "Projet commentaires"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %})
{: .chemin}

Ce projet vise à munir nos serveur web de persistance de données. Côté front avec la gestion des cookies et côté back avec la mise œuvre d'une base de données.

Le principe est de refaire plusieurs fois ce projet, en ajoutant petit à petit des notions de plus en plus perfectionnées de développement web.

## but du site

On va créer un site qui gère les commentaires. On va pouvoir :

* ajouter son commentaire
* consulter tous les commentaires

## Plan

Ce projet va être séparé en trois parties :

1. [le site sans les données]({% link cours/web/projets/commentaires/partie-1-site/index.md %})
2. on [envoie les données]({% link cours/web/projets/commentaires/partie-2-requetes-post/index.md %}) vers le serveur
3. on ajoute une persistance front [avec des cookies]({% link cours/web/projets/commentaires/partie-3-cookies/index.md %})
4. on ajoute une persistance back données avec une [base de donnée]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/index.md %})

Chaque partie est organisée en niveaux. Chaque niveau refait la partie en ajoutant à chaque fois des outils de développements/code de plus en plus perfectionnés. Il est recommandé de faire tous les niveaux d'une partie.

## niveaux

Chaque partie est organisée en niveaux. Chaque niveau ajoutant des outils de développements/code de plus en plus perfectionnés. Ces outils seront différents selon la partie.

## ressources

* <https://blog.logrocket.com/the-perfect-architecture-flow-for-your-next-node-js-project/>

> TBD
>
> * separer le serveur un plusieurs fichiers
> * variables d'environnement
> * config différentes en teste et en prod.
> * config différente pour la base. sqlite vs bd
> * require pas relu ?
> * séparer les routes du serveur
> * utiliser le dossier script pour la mise en prod.
> * compiler son bootstrap ?
> * gestion des routes.
{: .note}

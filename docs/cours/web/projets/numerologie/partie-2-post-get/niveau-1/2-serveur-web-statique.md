---
layout: page
title:  "Projet numérologie : partie 2 / niveau 1 / web statique"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 2]({% link cours/web/projets/numerologie/partie-2-post-get/index.md %}) / [niveau 1]({% link cours/web/projets/numerologie/partie-2-post-get/niveau-1/index.md %}) / [serveur web statique]({% link cours/web/projets/numerologie/partie-2-post-get/niveau-1/2-serveur-web-statique.md %})
{: .chemin}

On utilise node comme un serveur web de fichiers statiques.

> Il ne faut jamais servir de fichier statique en **production** avec node. C'est **mal** car il n'est pas fait pour ça. L'usage veut qu'on utilise un serveur dédié comme [nginx](https://www.nginx.com/) qui fait du cache, de la répartition de charge et tout ce genre de choses.
{: .attention}

## But

Le but d'un serveur web est de répondre quelque chose à partir d'une requête constituée d'une url et d'une méthode (GET ou POST). Certaines url vont nécessiter du travail comme faire une requête en base de données, calculer dez choses, etc, et d'autres consisteront seulement à rendre un fichier html, css ou encore javascript qui sera exécuté par le navigateur.

Ces fichiers qui seront pris sur le disque dur du serveur et envoyé au navigateur sont appelées **fichiers statiques**.

> Plus on a de fichiers statiques, mieux c'est puisque ces fichiers ne changent pas on peut utiliser des méthodes de [cache](https://fr.wikipedia.org/wiki/Cache_web) (côté client et serveur) ou de [load-balancing](https://fr.wikipedia.org/wiki/R%C3%A9partition_de_charge) pour accélérer le résultat (le réseau coute toujours du temps).
>
> De là, si vous avez le choix entre un serveur web ou juste des fichiers statiques, choisissez **toujours** la seconde possibilité.

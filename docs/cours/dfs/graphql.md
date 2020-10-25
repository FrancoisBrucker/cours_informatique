---
layout: page
title:  "GraphQL"
category: tutorial
tags: dev git 
authors: 
    - "Adèle Bourgeix"
    - "Fanis Michalakis"
---

## GraphQL qu'est ce que c'est ? 
GraphQL c'est en fait un langage de requête pour API ainsi qu’un environnement pour exécuter ces requêtes.

> **Nota Bene**: Une API c'est quoi ?  Une API permet à ton application de communiquer avec d'autres produits et services sans avoir exactement ça fonctionne ces autres produits ou services. 

Avant, on dessinait les API avec une architecture REST. Avec Rest, chaque ressource s'identifie avec une adresse URL à laquelle on fait appel par le protocole HTTP. 
Par exemple si je veux accéder au livre "Les Raisins de la Colère" il est trop probable que le chemin associé soit de la forme mon-application/livres/les-raisins-de-la-colère. Quand un client fait une requête en utilisant cette URL, le serveur récupère cette URL, identifie la nature et les détails de la requête, récupère les données et les renvoie au client. 
GraphQL ça fonctionne un peu pareil, la différence c'est dans la manière dont sont récupérées les données!

### Mais donc pourquoi on utilise GraphQL dans ce cas ?

Encore une fois, les développeurs utilisent maintenant GraphQL dans une optique d'optimisation. Il est maintenant vraiment importants que le temps de réponse des applications soit le plus court possible : un utilisateur qui ne peut pas acheter rapidement le produit qu'il veut va rapidement se laisser et ça peut faire perdre beaucoup beaucoup d'argent à une entreprise. 

Voilà pourquoi GraphQL c'est super top : GraphQL récupère exactement les données qu'on lui demande, ni plus ni moins. Par exemple, si on souhaite récupérer le titre d'un livre, on récupère seulement le titre et pas l'auteur, l'éditeur, l'identifiant, l'année de parution ou n'importe quel autre renseignement que l'on n'avait pas demandé. Ca peut paraître anodin mais si cela concerne un fichier JSON de plusieurs dizaines de paramètres et qu'on multiplie les requêtes, ça peut venir devenir long de récupérer trop de données inutiles.  

Une autre raison pour utiliser GraphQL c'est qu'on permet au client d'encapsuler les requêtes. On s'explique : si on récupère tous les livres de Steinbeck, on peut lui demander en même temps de récupérer leur titre et leur année de parution. Pas besoin de refaire une seconde requête pour chaque livre comme avec REST!



## Du côté serveur : schémas et types 

## Du côté clients: les opérations 
###Queries 
###Mutations 
###Validation des opérations


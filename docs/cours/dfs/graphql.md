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
Donc en fait, GraphQL nous permet de récupérer des données sous forme d'un graphe (d'ou ce fameux nom!). 


## Du côté serveur : schémas et types

Donc maintenant, comment ça marche ? Avant de pouvoir permettre au client de faire des requêtes, il faut définir l'environnement GraphQL du côté serveur. C'est à dire définir la structure des données qui peuvent être récupérées mais aussi les "opérations" qui vont pouvoir être récupérées par le client. 

### Définir les schémas 

Avec GraphQL, un schéma doit être écrit pour chaque entité de notre base de données. Dans le cadre d'une bibliothèque, on aura par exemple un schéma pour les livres et un autre pour les auteurs. 

> **Nota Bene**: l'environnement GraphQL peut se configurer dans plusieurs syntaxes de languages de programmation mais par la suite, les exemples seront écrit en JavaScript. Les module qui est utilisé est **graphql**. 

Voici comment pourrait s'écrire le schéma associés à nos livres: 

~~~
const BookType = new GraphQLObjectType({
    name: 'Book',
    fields: ( ) => ({
        id: { type: GraphQLID },
        name: { type: GraphQLString },
        genre: { type: GraphQLString },
      })
});

~~~

#### Champs et types de champs 

Chaque schéma contient des champs qui sont les attributs de nos objets. Chaque champ possède un type qui est soit un type défini par GraphQL: une chaîne de caractères, un nombre, un identifiant unique (ce qui est bien pratique parfois!), etc mais peut aussi être du type défini par un autre schéma.

On peut aussi que le champ ne peut être nul avec un **!** ou que c'est une liste avec des **[]**

Définissons par exemple le schéma de nos auteurs: 

~~~
const AuthorType = new GraphQLObjectType({
    name: 'Author',
    fields: ( ) => ({
        id: { type: GraphQLID },
        name: { type: GraphQLString },
        age: { type: GraphQLInt },
        books: {
            type: new GraphQLList(BookType),
            resolve(parent, args){
                return Book.find({authorId: parent.id})
            }
        }
    })
});
~~~

Notre auteur, possède un identifiant, un nom, un âge mais aussi une liste des livres qu'il a écrits. Pour trouver ces livres on a besoin d'une méthode qui s'appelle **resolve** et qui reçoit notamment un parent (qui est en fait ici l'auteur lui-même). 

On peut donc compléter le schéma pour nos livres : 

~~~
const BookType = new GraphQLObjectType({
    name: 'Book',
    fields: ( ) => ({
        id: { type: GraphQLID },
        name: { type: GraphQLString },
        genre: { type: GraphQLString },
        author: {
            type: AuthorType,
            resolve(parent, args){
                return Author.findById(parent.authorId)
            }
        }
    })
});
~~~

#### Et les opérations dans tout ça ? 

Nous avons donc fini de définir les modèles sur lesquels le client va pouvoir effectuer des opérations. D'ailleurs quelles sont ces opérations ? 
Les opérations peuvent être de deux types : 
1. Des _queries_: le client récupère des données qu'il a demandées. 
2. Des _mutations_: le client décide de faire une mutation sur la base de données (ajouter une instance, modifier une instance, supprimer une instance etc)



## Du côté clients: les opérations 
###Queries 
###Mutations 
###Validation des opérations


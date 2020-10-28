---
layout: page
title:  "les bases de données (relationnelles)"
category: tutorial
tags: dev git 
authors: 
    - "Adèle Bourgeix"
    - "Fanis Michalakis"
---

## Introduction

Le but de ce tuto est de couvrir le sujet des bases de données relationnelles, en voyant dans un premier temps ce dont il s'agit, puis en mettant en pratique au travers de l'utilisation de sqlite.

## Une base de donnée relationnelle ?

Une base de donnée, ce n'est rien d'autre qu'une collection de données. Et les données, ça peut être un peu tout et n'importe quoi : des mesures de distances, de températures, les résultats des matchs de Ligue 1, les livres présents dans une bibliothèque, et cetera, et cetera.

Une base de donnée **relationnelle**, c'est une base de données où les données sont organisées dans des tableaux à deux dimensions (des tableaux quoi) que l'on appelle *relations* (d'où le nom :wink: ).

| Titre | Auteur | Date de parution originale |
| :---: | :---: | :---: |
| Les Raisins de la colère | John Steinbeck | 1939 |
| Les Chemins de la faim | Jorge Amaldo | 1946 |
| Sur la Route | Jack Kerouac | 1957 |
*<center>Une exemple de relation</center>*

Une ligne d'une relation est appelée n-uplet ou enregistrement, et n'est donc rien d'autre qu'un ensemble de n valeurs. Dans l'exemple ci-dessus, n est égal 3.

Une colonne d'une relation est appelée un attribut. C'est une caractéristique des enregistrements. Dans notre exemple, le titre des livres est un attribut.

## La grammaire SQL

A partir d'une grammaire simple, composé de quelques prépositions et verbes, on construit un ensemble de relations à partir de nos données. Ce langage s'appelle SQL pour Structured Query Language, language de requête structurée en français.

Imaginons que ma base de données est composée de deux relation :
- une relation "livres", qui est celle de notre premier exemple,
- une relation "auteurs", qui a pour attribut le nom des auteurs, leur date de naissance, de mort, et leur nationalité :

| Auteur | Date de naissance | Date de décès | Nationalité |
| :-: | :-: | :-: | :-: |
| John Steinbeck | 1902-02-27 | 1968-12-20 | Américaine |
| Jorge Amado | 1912-08-10 | 2001-08-06 | Brésilienne |
| Jack Kerouac | 1922-03-12 | 1969-10-21 | Américaine |
*<center>la relation "auteurs"</center>*

Je peux alors construire une requête en langage SQL pour créer une nouvelle relation n'affichant que les livres des auteurs américains :

~~~ sql
SELECT Titre FROM (livres NATURAL JOIN auteurs) WHERE Nationalité = "Américaine"
~~~

| Titre | Auteur | Nationalité |
| :-: | :-: | :-: |
| Les Raisons de la colère | John Steinbeck | Américaine |
| Sur la Route | Jack Kerouac | Américaine |

## SQL et sqlite

Cette section propose de montrer comment créer une base de données et manipuler les enregistrements qu'elle contient avec la syntaxe SQL. Pour ce faire, nous utiliserons sqlite, qui présente l'avantage de n'avoir aucune administration ou paramétrage initial à effectuer, car la base de donnée n'est pas stockée dans un serveur distant mais localement, dans un fichier en extension `.db`.

### Installer sqlite

Le plus simple est d'utiliser un *package manager*, comme apt ou brew. Par exemple, avec brew :

~~~ shell
brew install sqlite3
~~~

ou avec apt :

~~~ shell
sudo apt-get install sqlite3
~~~

### Créer une base de données

Pour créer une base de données, il suffit de lancer la commande `sqlite3` suivie du nom de la base. Par exemple :

~~~ shell
sqlite3 bibli.db
~~~

Un nouveau fichier bibli.db va être créé, et vous serez automatiquement basculé dans la console sqlite. C'est depuis cette console que nous lancerons toutes les commandes suivantes.

### Créer une table "auteurs"

Nous allons commencer par créer une table "auteurs" dans laquelle nous enregistrerons le nom/prénom, la date de naissance, la date de décès et la nationalité de nos écrivains. Afin de pallier aux problèmes d'homonymie et autres, il est commun d'ajouter un attribut "id", qui est un entier sur lequel on itère et qui constituera une clé primaire de notre base.

~~~ sql
CREATE TABLE auteurs (id integer primary key, auteur VARCHAR(30), dateNaissance date, dateDeces date, nationalite VARCHAR(30));
~~~

### Créer une table "romans"

De même, nous créons une table "romans" pour y stocker les tites des ouvrages, ainsi que leur auteur et leur date de parution originale.

~~~ sql
CREATE TABLE romans (id integer primary key, titre VARCHAR(30), auteur VARCHAR(30), dateParution date);
~~~

### Voir les tables existantes

A ce stade, on peut vouloir visualiser les tables dont notre base de données dispose :

~~~ sql
.tables
~~~

Cette commande doit retourner les noms de nos deux tables : `auteurs` et `romans`.

### Enregistrer des données

On va maintenant ajouter nos enregistrements dans les tables :

~~~ sql
 INSERT INTO "auteurs" VALUES(1, "John Steinbeck", 1902-02-27, 1968-12-20, "Américaine");
 INSERT INTO "auteurs" VALUES(2, "Jorge Amado", "1912-08-10", "2001-08-06", "Brésilienne");
 INSERT INTO "auteurs" VALUES(3, "Jack kerouac", "1922-03-12", "1969-10-21", "Américaine");
~~~

et

~~~ sql
INSERT INTO romans VALUES(1, "Les Raisins de la colère", "John Steinbeck", "1939");
INSERT INTO romans VALUES(2, "Les Chemins de la faim", "Jorge Amado", "1946");
INSERT INTO romans VALUES(3, "Sur la Route", "Jack Keouac", "1957");
~~~

### Modifier un enregistrement

Pour modifier un enregistrement, par exemple si un auteur contemporain décède et qu'il faut donc ajouter sa date de décès à la table, on utilise la méthode `UPDATE` :

~~~ sql
UPDATE auteurs SET dateDeces = "1922-03-12" WHERE id=3;
~~~

### Visualiser nos tables

Pour visualiser nos tables, il faut passer par une requête sql demandant à sqlite de nous afficher tous les éléments. Par exemple, pour voir notre tableau d'auteurs, on utilisera :

~~~ sql
SELECT * FROM auteurs
~~~

On peut au passage changer l'affichage par défaut, ce qui est bien utile pour mieux visualiser les tables. On utilise courament un affichage avec en-têtes et en colonnes. Pour le mettre en place, il faut exécuter :

~~~ sql
.headers on
.mode column
~~~

Réessayez maintenant d'afficher la table des auteurs. C'est plus lisible, non ?

### Visualiser des relations composées

On aura souvent besoin d'afficher des tableaux composés à partir des tables initiales. Par exemple, on peut vouloir voir tous les restaurants proposant de la cuisine indienne. Ou encore, tous les romans de notre bibliothèque dont l'auteur est américain. Pour ce faire, on réalise une jointure de nos deux tables, et on récupère les titres des romans dont l'auteur est de nationalité américaine :

~~~ sql
SELECT titre FROM (romans NATURAL JOIN auteurs) WHERE nationalite = "Américaine";
~~~

NB : on doit ici réaliser une jointure car la donnée que l'on recherche (les titres des romans) et la donnée sur laquelle on discrimine (la nationalité de l'auteur) ne sont pas dans les mêmes tables. Ces deux tables sont ici jointes de manière "naturelle" car elles ont un champ "auteur" en commun.

On obtient en résultat le tableau suivant des romans écrit par un auteur américain :

| titre |
| :-: |
| Les Raisins de la colère |
| Sur la Route |
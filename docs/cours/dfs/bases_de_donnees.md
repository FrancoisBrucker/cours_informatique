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
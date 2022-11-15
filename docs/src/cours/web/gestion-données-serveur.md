---
layout: layout/post.njk

title: "Gestion des données côté serveur"

eleventyNavigation:
  key: "Gestion des données côté serveur"
  parent: "Web"
---

<!-- début résumé -->

Faire une API avec son serveur.

<!-- fin résumé -->

Gérer des données côté serveur nécessite deux actions bien distinctes :

1. permettre à un client d'accéder à des données via un système de requêtes, qu'on appelle API 
2. pouvoir accéder, conserver et mettre à jour un ensemble de données (doit survivre à un reboot serveur)

## API

<https://fr.wikipedia.org/wiki/Interface_de_programmation>

1. par url
    1. query
    2. rest
2. dans le corps de la requête : [graphql](https://graphql.org/)

## Sérialisation des données

La [sérialisation/désérialisation](https://fr.wikipedia.org/wiki/S%C3%A9rialisation) est l'opération consistant à transformer une donnée en un format facilement transportable/stockable et à procéder à l'opération inverse pour retrouver la donnée originelle.

Cette opération est cruciale dans toute gestion des données. Pour le web :

{% note %}

* les données : des dictionnaires javascript
* le format facilement transportable : le texte (utf8).

La façon de convertir les dictionnaires en texte et réciproquement est régie par le [json](https://www.json.org/json-fr.html)

{% endnote %}

Le json est tellement bien fait qu'il est utilisé partout ! Il est en effet très facile à lire, à modifier avec un simple éditeur de texte, et à transférer avec une simple requête http.

## Stockage de données

1. stockage dans une base + sequelize
2. serveur de bdd (TBD ? ou tuto élève)


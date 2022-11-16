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

Gérer des données côté serveur nécessite plusieurs actions bien distinctes :

1. organisation des requêtes possible sous la forme d'une API
2. manipulation d'une donnée : CRUD
3. transfert et stockage : sérialisation

## API

{% chemin %}
<https://fr.wikipedia.org/wiki/Interface_de_programmation>
{% endchemin %}

L'échange de données entre le client et le serveur se fait grâce à une API qui détermine les routes utilisables (en utilisant des routes paramétrables). Il existe plusieurs moyens d'organiser une API :

* par query : Une route générale est paramétrable par query. C'est la façon de faire de google maps par exemple (voir par exemple la [documentation pour choisir un chemin](https://developers.google.com/maps/documentation/directions/get-directions))
* sous la forme d'une URL. L'accès au données se fait sous la forme d'un chemin. C'est la [façon de faire REST](https://developer.mozilla.org/fr/docs/Glossary/REST) par exemple.
* requête dans le corps du massage. Plutôt que d'utiliser des query, on place directement la requête dans le corps du message. C'est la façon de faire de la populaire bibliothèque [graphql](https://graphql.org/) par exemple.

## CRUD

Cet acronyme signifie :

* **C**reate : création de la donnée
* **R**ead : lecture de la donnée
* **U**pdate : mise à jour de la donnée
* **D**elete : suppression de la donnée

Et rappelle le cycle de vie d'une donnée. Il faut que l'API puisse permettre au client d'effectuer ces actions CRUD pour chacune des données (si possible). On a coutume d'expliciter ces requêtes en utilisant des [méthodes HTTP](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol#M%C3%A9thodes) différentes :

* lire une donnée se fera en utilisant la méthode `GET` (c'est ce que l'on fait habituellement)
* créer une donnée se fera en utilisant la méthode `POST` (c'est ce que l'on fait habituellement)
* mettre à jour une donnée se fera en utilisant la méthode `PUT` (c'est ce que l'on fait habituellement)
* supprimer une donnée se fera en utilisant la méthode `DELETE` (c'est ce que l'on fait habituellement)

On ne peut via un navigateur qu'utiliser des méthode get. Pour utiliser les autres méthodes, on peut utiliser [fetch](https://developer.mozilla.org/en-US/docs/Web/API/fetch) en javascript en spécifiant la méthode à utiliser

{% info %}
POur tester les méthodes lorsque l'on est entrain de développer, on a coutume d'utiliser une application tierce, comme <https://www.postman.com/> par exemple (on peut l'utiliser de façon gratuite sans avoir besoin de s'inscrire)
{% endinfo %}

Souvent, on n'a besoin que des méthodes GET (pour lire) et POST (pour écrire et mettre à jour) la donnée. Par exemple, supposons que l'on veuille stocker une unique donnée. On veut pouvoir :

* lire la donnée avec la route : <http://127.0.0.1:3000/> en utilisant la méthode GET (la méthode utilisée par défaut par les navigateurs)
* écrire la données avec la route <http://127.0.0.1:3000/?valeur=12> en utilisant la méthode POST

On peut utiliser le code express suivant :

```javascript
const express = require('express')
const app = express()

const hostname = '127.0.0.1';
const port = 3000;

donnée = 42

app.get('/', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end(donnée.toString());

})


app.post('/', (req, res) => {

    donnée = req.query.valeur
    res.redirect('/')

})


app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);

```

Plusieurs remarques :

* vous voyez comment express permet facilement de différentier les méthodes : `app.get`{.language-} pour des méthodes `GET` et `app.post`{.language-} pour des méthodes `POST`
* à la fin de la méthode post la ligne `res.redirect('/')`{.language-} est importante. C'est le pattern [Post/Redirect/Get](https://en.wikipedia.org/wiki/Post/Redirect/Get) (aussi appelé *Redirect after post*) qu'il faut que vous utilisiez après chaque requête post. Elle permet de refaire une requête GET après la méthode post (dans notre exemple on refait une requête GET vers `/` mais cela peut différer selon ce que vous voulez faire). Ceci pour éviter — entre autre — de renvoyer une donnée lorsque l'on rafraîchit le navigateur.

{% faire %}
Utilisez <https://www.postman.com/> pour tester le serveur précédant.
{% endfaire %}

## JSON pour sérialiser ses données

La [sérialisation/désérialisation](https://fr.wikipedia.org/wiki/S%C3%A9rialisation) est l'opération consistant à transformer une donnée en un format facilement transportable/stockable et à procéder à l'opération inverse pour retrouver la donnée originelle.

Cette opération est cruciale dans toute gestion des données. Pour le web :

{% note %}

* les données : des dictionnaires javascript
* le format facilement transportable : le texte (utf8).

La façon de convertir les dictionnaires en texte et réciproquement est régie par le [json](https://www.json.org/json-fr.html)

{% endnote %}

Le json est tellement bien fait qu'il est utilisé partout ! Il est en effet très facile à lire, à modifier avec un simple éditeur de texte, et à transférer avec une simple requête http.

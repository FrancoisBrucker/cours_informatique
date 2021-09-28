---
layout: page
title:  "Projet commentaires : partie 2 / envoyer les donées"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 2]({% link cours/web/projets/commentaires/partie-2-requetes-post/index.md %}) / [envoyer les données]({% link cours/web/projets/commentaires/partie-2-requetes-post/2-post.md %})
{: .chemin}

on Envoie les données au serveur, qui les analyses.

## requêtes post

Pour l'instant on a toujours utilisé des requêtes GET pour parler au serveur. Ces requêtes ne nécessitent que l'url. Les requêtes POST quant à elles permettent d'envoyer des données au serveur. C'est le cas pour notre formulaire.

> les différences entre requêteGET et POST sont surtout des conventions. Vous pouvez très bien envoyer des données avec une requête GET mais ça rend le code moins lisible

De point de vue de express, la gestion est un peut différente des requêtes GET puisqu'il faut récupérer le contenu

## gestion avec express

Comme il faut récupérer le corps de la réquête POST, on va faire passer toutes les requêtes par un bout de code (que express appelle *middleware*) qui va ajouter un attribut `body` contenant le corps de la requête.

C'est identique à ce qu'on a fait précédemment dans le projet numérologie :

```js
const express = require('express')
// ...

app.use(express.json())
```

La ligne précédente ajoute  un attribut `body` qui contient le corps de la requête au format json. Pile ce que l'on veut.

Le code suivant ajoute une route nommé `/donne` qui récupère une requête de type POST et affiche son résultat dans la console (du serveur) :

Fichier *"commentaires/server.js"* :

```js
const path = require('path')

const express = require('express')

const app = express()


const hostname = '127.0.0.1';
const port = 3000;

app.use(express.json())

app.use("/static", express.static(path.join(__dirname, '/static')))

app.get('/', (req, res) => {
    res.redirect(301, '/static/index.html')
})


app.post('/donne', (req, res) => {
    console.log(req.body)
})

app.use(function (req, res) {
    console.log("et c'est le 404 : " + req.url);

    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/html');

    res.end("<html><head><title>404</title></head><body><h1>Et c'est le 404.</h1><p> ressource non trouvée</p></body></html>");

})

app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);
```

## envoi de la requête post

Il ne nos reste plus qu'à envoyer nos données depuis le fichier html.

On peut le faire facilement avec `fetch`, que l'on a déjà utilisé pour numérologie. Il faut juste préciser :

* que l'on envoie une requête post
* envoyer les données dans le corps de la requête

> TBD :
> on envoie que si le titre est non vide : ajouter bootstrap verification
> après envoie on supprime le titre et le message pour eviter les soucis de double post
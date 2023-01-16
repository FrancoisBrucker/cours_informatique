---
layout: layout/post.njk 
title:  "Cookies"

category: cours
tags: 
author: Valentin Defrance
---


## Introduction

Les [cookies](https://fr.wikipedia.org/wiki/Cookie_(informatique)#Cr%C3%A9ation_d'un_cookie) sont l'équivalent de fichiers texte de petite taille stocké sur le terminal de l'internaute. Ceux-ci existent depuis les années 1990 et permettent aux développeurs web de conserver des données utilisateur afin de faciliter la navigation et de permettre certaines fonctionnalités. Les cookies étant généralement stockés sous forme de fichiers texte, iols ne sont pas exécutables et ne peuvent donc pas être des logiciels espions ou des virus. Ils peuvent cependant permettre de suivre les utilisateurs ayant visité un site web en particulier.

Un cookie est donc un objet chez le client qui a un nom, une durée de vie et contient des informations.

## Voir les cookies

- Pour voir la liste des cookies dans votre navigateur, rendez vous dans les paramètres avancés, puis dans les paramètres de confidentialité et sécurité où vous pourrez accéder à la liste de tous les cookies enregistrés par votre naviagteur.
- Si vous voulez voir les cookies d'un site en particulier depuis le site, ouvrez les outils de développement et entrez la commande `document.cookie` dans la console.

## Création d'un cookie

Pour avoir accès aux cookies, il faut utiliser le middleware [cookie-parser](https://www.npmjs.com/package/cookie-parser).

Pour installer `cookie-parser`, il faut utiliser la commande `npm install cookie-parser` dans le répertoire du projet.

Une fois cookie parser installé, il faut modifier ou créer le fichier `app.js` afin d'y ajouter les lignes suivantes :

~~~ javascript
var express = require('express')
var cookieParser = require('cookie-parser')
 
var app = express()
app.use(cookieParser())
~~~

Maintenant nous pouvons commencer à utiliser les cookies. Par exemple, entrons ces lignes si dans le fichier `app.js`:

~~~ javascript
var express = require('express');
var cookieParser = require('cookie-parser'); // module for parsing cookies
var app = express();
app.use(cookieParser());

app.get('/setcookie', function(req, res){
    // setting cookies
    res.cookie('username', 'Robbert', { maxAge: 60000, httpOnly: true });
    return res.send('Cookie has been set');
});

app.get('/getcookie', function(req, res) {
    var username = req.cookies['username'];
    if (username) {
        return res.send(username);        
    }

    return res.send('No cookie found');
});

app.listen(3000);
~~~

Maintenant entrons la commande `node app.js` dans notre terminal. Nous aurons créé un serveur local ouvert sur le port 3000, nous pouvons donc nous y connecter depuis notre navigateur via l'adresse `http://localhost:3000`. Maintenant, en accédant à l'adresse `http://localhost:3000/setcookie`, le message `Cookie has been set` s'affiche et nous indique que notre cookie à bien été créé. Ce cookie a comme nom "username", comme information "Robbert" et comme durée de vie 1 minute (maxAge en milisecondes)


En accédant à l'adresse `http://localhost:3000/getcookie`, le message `Robbert` s'affiche et nous montre que notre cookie à bien été lu par notre naviagteur.

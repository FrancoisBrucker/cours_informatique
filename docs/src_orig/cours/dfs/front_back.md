---
layout: layout/post.njk 
title:  "Front back"
category: tutorial
tags: dev git 
author: Laurie Dégeorges
---

# Frontend, Backend et ce qu'il manque entre les deux

De la structure d'un projet et de la séparation entre front et back.

#### Comme partout ailleurs, commençons par créer un projet

~~~ sh
    mkdir project && cd project
    git init
    yarn init -y
~~~
Le dossier *projet* contient alors un *.git* et un *package.json*, que l'on peut commit pour en garder une trace.
Nous sommes maintenant prêts à commencer.

## Frontend ou ce qui se voit
Le front correspond à ce que l'utilisateur peut voir depuis son navigateur lorsqu'il appelle un url, c'est-à-dire les visuels du site, les images et les scripts permettant de gérer l'affichage. 

### Static ![Pikachu attaque static !]({{"images/static-resize.png"}})


Pour bien s'y retrouver tout ce qui concerne le front sera placé dans un dossier *static*. Ce dossier contiendra un package.json où seront répertoriés les modules qui seront utilisés pour l'affichage.

Initialisation de static

~~~    
    mkdir static && cd static
    yarn init -y
~~~


On crée un *index.html* dans static pour la démo

~~~ html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Titre trop stylé</title> 
    </head>
    <body>
        <div class="body">
            <h1> Une page web </h1>
            <div> Et son contenu 
                <form class="pure-form">
                    <label for="mot">Ecrivez ici :</label>
                    <input id="mot" type="text" name="mot"/>
                    <button id="press" class="pure-button" type="submit">Bouton inutile ?</button>
                </form>            
                <p id="get-value">Valeureuse valeur</p>
            </div>
        </div>
    </body>
</html>
~~~

On crée *style.css* pour le styliser un peu

~~~ css
html, body {
    margin: 0;
    background-color: sandybrown;
}

.body {
    font-family: Dyuthi, serif;
    margin-top: 100px;
    margin-left: auto;
    margin-right: auto;
    width: 80%;
}

p {
    text-align: center;
    margin-top: 100px;
    margin-bottom: 0;
    font-size: 50px;
}
~~~

Allons même jusqu'à utiliser Pure css juste pour pouvoir briller en soirée mondaine.
Il suffit de lancer la commande `yarn add purecss` et voilà ! Pure css est ajouté au node_modules de *static* exactement comme prévu.

N'oublions pas d'éditer *index.html* pour importer notre style

~~~ html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Titre trop stylé</title> 

        <link href="./node_modules/purecss/build/pure-min.css" rel="stylesheet">
        <link href="style.css" rel="stylesheet">

    </head>
    <body>
        <div class="body">
            <h1> Une page web </h1>
            <div> Et son contenu 
                <form class="pure-form">
                    <label for="mot">Ecrivez ici :</label>
                    <input id="mot" type="text" name="mot"/>
                    <button id="press" class="pure-button" type="submit">Bouton inutile ?</button>
                </form>            
                <p id="get-value">Valeureuse valeur</p>
            </div>
        </div>
    </body>
</html>
~~~

### Un peu d'action

Créons dans *static/* un fichier *main.js*

*static/main.js*
~~~ js
function change_value() {
    mot = document.querySelector("#mot").value
    if (mot) {
        document.querySelector("#get-value").textContent = mot
    } else {
        document.querySelector("#get-value").textContent = "Valeureuse valeur"
    }

}
change_value()

document.querySelector("#press").addEventListener("click", (event) => {
    change_value()
    event.preventDefault()
})
~~~

Enfin il faut ajouter `<script src="main.js"></script>` à la fin de index.html 

## Back, la face cachée de l'iceberg immergé !
![I'll be back]({{"images/termin.png"}})

C'est ce qui se passe côté serveur, tous les calculs, les fonctions et les traitements de base de données compliqués qui seront envoyés au navigateur.

**Pour la suite sortons de *static/* et replaçons-nous à la racine du projet.**

### Lancer notre site
Nous aurons besoin d'express, ajoutons le donc simplement à node_modules avec `yarn add express` (bien sortir du dossier *static*)

A ce stade le projet s'organise comme suit

(`tree -I node_modules`)

    .
    ├── package.json
    ├── static
    │ ├── index.html
    │ ├── main.js
    │ ├── package.json
    │ ├── style.css
    │ └── yarn.lock
    └── yarn.lock

Avec express dans le package.json de la racine et pure css dans celui de static.


### Des routes
Créons un fichier *app.js* permettant de lancer notre site
~~~ js
var express = require('express');
var app = express();
var port = 8000;

app.get('/', function (req, res) {res.send('Hello World!');});

app.listen(port, function () {
  console.log('Listening to Port ' + port);
});
~~~

Ainsi il se lance avec `node app.js`, et devrait aimablement nous dire **Hello World** en se connectant à localhost:8000/

Mais Hello World n'a jamais été un résultat très passionnant (bien que la politesse soit importante), remplaçons cela par des routes plus intéressantes.


*app.js*
~~~ js
var express = require('express');
var app = express();
var port = 8000;

app.use("/static", express.static(__dirname + '/static'))

app.get('/', (request, response) => {
    response
        .redirect(301, '/static/index.html')
})

app.listen(port, function () {
  console.log('Listening to Port ' + port);
});
~~~

Dès à présent lancer le serveur avec `node app.js` permet d'aller voir notre site !

Il est capable d'afficher un mot écrit par l'utilisateur ! Impressionnant n'est-ce pas ? Non !? Tssk jamais contents ces développeurs...

## Et une API pour la route

Créons une route commençant par `/api` qui permettra à des applications tierces d'utiliser notre site. 

L'usage veut également que les différentes versions des api soient conservées pour pouvoir changer nos appels sans perturber les sites utilisant ceux-ci. On va donc avoir les routes suivantes : 

  - `/api/current/` qui sera la route pour la version actuelle de l'API 
  - `/api/v1/` qui sera un lien vers la version courante. 
  
Ceci nous permettra de maintenir la version `v1` de l'API lorsque la version courante changera en `v1.2` ou `v2`.

On aura aussi pour l'instant qu'une unique méthode : `affichage/<mot>` qui prend une chaîne de caractère en *"paramètre"*.

Construisons ces routes, et pour cela créons des dossiers que l'on importera (importer un dossier revient à importer le fichier *index.js* qui s'y trouve). 

Notre site correspond maintenant à ça : 

~~~
├── app.js
├── package.json
├── routes
│ ├── index.js
│ └── v1
│     └── index.js
├── static
│ ├── index.html
│ ├── style.css
│ ├── main.js
│ ├── package.json
│ └── yarn.lock
└── yarn.lock

~~~

Le dossier *routes* contient un fichier *index.js*. Ce fichier est importé dans *app.js* avec 2 lignes : 

~~~ js
var express = require('express');
var app = express();

app.use("/static", express.static(__dirname + '/static'))

app.get('/', (request, response) => {
    response
        .redirect(301, '/static/index.html')
})

api = require('./routes')
app.use('/api', api)

app.listen(8000, function () {
  console.log('Listening to Port 8000');
});
~~~

Le fichier *routes/index.js* contient le code suivant :

~~~ js
var express = require('express');
var router = express.Router();

module.exports = router

router.use('/current', require('./v1'))
router.use('/v1', require('./v1'))
~~~

Son boulot est de créer (et de rendre) un router qui contient deux routes `/current` et `/v1` qui seront identiques. 

Le fichier *routes/v1/index.js* contient la route proprement dite de notre api. Pour l'instant c'est un fake. On fera le lien avec notre code js plus tard :

~~~ js
var express = require('express');
var router = express.Router();

module.exports = router

router.get('/affichage/:mot', (req, res) => {
    res.json({
        "mot": req.params.mot,
    })
})
~~~

Remarquez que cette route prend un paramètre nommé `:mot` que l'on peut ensuite reprendre dans le code. 

Pour l'instant le code rend un objet [json](https://www.json.org/json-fr.html) contenant 1 champ, le mot (le paramètre de notre route). 

Pour savoir comment appeler cette route depuis notre server, regardons comment elle est appelée : 

  1. on commence par l'appeler depuis *./app.js* : `app.use('/api', api)` où `api = require('./routes')`
  2. cela continue dans *./routes/index.js* avec `router.use('/current', require('./v1'))` et `router.use('/v1', require('./v1'))`
  3. on arrive enfin au *./routes/v1/index.js* qui crée la route : `router.get('/affichage/:mot', ...`

En combinant tout ça on arrive à une route : `http://localhost:3000/api/current/affichage/un truc` qui est la même que `http://localhost:3000/api/v1/affichage/un truc`. On peut bien sur remplacer "un truc" par ce qu'on veut du moment que ce n'est pas vide.


## Pour déplacer notre projet

Pour lancer le projet depuis une autre machine ou l'héberger sur un serveur il suffit de :

- Copier le répertoire à l'endroit voulu

- Lancer `yarn install` à la racine

- Lancer `yarn install` dans static
    

---
layout: page
title:  "Les routes"
category: cours
tags: node express test
authors: "Tina Alaei"
---

Le but d’un serveur web est de répondre à des requêtes (une url). Cette réponse peut prendre des formes très diverses, les plus courantes étant du html ou des données aux format json. Nous allos donc apprendre a mettre en place des routes. Chaque différente url sera une route qui nous renverra à une réponse que l'on lui aura assigné.


## Concept

Dans un nouveau fichier ```routes.js``` nous allons définir les réponses des requêtes possible sur note site web.

Un exemple de ce à quoi se fichier peut ressember se presente ainsi :

_routes.js_
~~~javascript
var server = http.createServer((request, response) =>{
    reponse.statusCode = 200; //La réponse type aura comme code http 200 : OK
    response.setHeader('Content-Type', 'text/html');

    if (request.url === "/" || request.url === "/home") {
        // réponse au navigateur pour les routes "/" et "/home"
    }
    else if (request.url === "/contact") {
        // réponse au navigateur pour la route "/contact"
    }
    else {
    	response.statusCode = 404; //Si la route n'a pas été définie, la reponse aura comme code http 404 : Not found
        // réponse pour les routes non définies
    }
})
~~~

> **_Remarque :_** Les codes http permettent d'identifier le resultat d'une requête et eventuellement de renvoyer une erreur au client si celle-ci n'aboutit pas. Pour avoir le détail des codes vous pouvez consulter [http.cat](http.cat), mais les plus courants sont le 200, qui indique le succés de la requête, le 401 pour non-authorisé (si l'utilisateur est non connecté par exemple), le 403 pour accès refusé, et le 404 pour une page non trouvée.

> **_Remarque :_** Le Header correspond aux en-têtes HTTP. Ils permettent la transmission d'informations supplémentaires avec une requête ou une réponse. Ici le set Header indique le _Content-Type_ dans lequel on renseingne le type de média de la ressource. Vous pourrez avoir plus d'informations concernant les headers en vous rendant [ici](https://developer.mozilla.org/fr/docs/Web/HTTP/Headers).

Pour avoir la liste des méthodes que l'on peut associer à une réponse en Node.js, vous pouvez les voir [ici dans la documentation](https://nodejs.org/api/http.html#http_class_http_serverresponse).

Les réponses au navigateur pour chaque route peuvent prendre des formes diverses, dont voici un exemple :

~~~javascript
var fs = require('fs')

var server = http.createServer((request, response) =>{
	...

    else if (request.url === "/contact") {
        response.writeHead(200,  {'Content-Type': 'text/html'}) //Cette ligne écrit le header de notre page
        var readStream = fs.createReadStream(__dirname + "/contact.html", "utf8") //fs signifie File System : cette ligne va chercher le fichier html qui nous intéresse
        readStream.pipe(response) // cette ligne envoie notre fichier en réponse
    }
    ...
})
~~~


## Express

Nous remarquons que la gestion des routes en Node.js est peu pratique. En effet, un site avec plus de ressources sera
 une énorme imbrication de if/else - ou de switch/case - ce qui n'est pas très propre.

Express est un framework pour Node.js qui va nous faciliter l'écriture de ce fichier ```routes.js```.

### Installation

Express se met en place dans votre projet à l'aide de la commande ```yarn add express``` (ou ```npm install express```).

On l'importe alors dans notre fichier ```routes.js``` avec ```require```:

~~~javascript
var express = require('express')
var app = express()
~~~

### Utilisation

> **_Remarque :_** La documentation pour le routage en Express est accessible [ici](https://expressjs.com/fr/guide/routing.html).

Via, l'import d'express montré dans **_Installation_**, nous avons créé une insatnce dans la classe ```express``` dans ```app```.

Notre code pour ```routes.js``` devient :

_routes.js_
~~~javascript
var express = require('express')
var app = express()

app.use(function timeLog(req, res, next) {
  console.log('Time: ', Date.now());
  next();
});

app.get('/', (request, response) => {
    response.statusCode = 200;
    response.setHeader('Content-Type', 'text/html');
    // réponse au navigateur pour la route "/"
})

app.get('/contact', (request, response) => {
	response.statusCode = 200;
    response.setHeader('Content-Type', 'text/html');
    // réponse au navigateur pour la route "/contact"
})

app.use(function (request,response) {
    response.statusCode = 404;
    // réponse pour les routes non définies
    
})
~~~

Comme vous pouvez le voir, nos appels passent par l'instance de la classe ```express``` dans ```app```. On utilise essentiellement trois méthodes de ```app``` :

- ```app.use()``` : qui reçoit tout type de requêtes, 
- ```app.get()```, ```app.post()``` : qui reçoivent respectivement les requêtes http get et post.


#### Contexte d'utilisation pour ```app.use()```

```app.use()``` va établir une fonction qui va s'executer lorsque la base du path de la requête concorde avec celui spécifié dans la fonction. Par défaut, ce path est ```'/'```. Ainsi, lorsque l'argument path n'est pas spécifié, la fonction peut s'executer pour toutes les requêtes.

> **_Exemple :_** Si on écrit ```app.use('/api', ...)```, le contenu de la fonction pourra être appelé par les requêtes de types ```'/api/images'```, ```'/api/images/profile'```, ...

_Exemple d'application courant dans le ```routes.js```_
~~~javascript
app.use(function timeLog(req, res, next) {
  console.log('Time: ', Date.now());
  next();
});
~~~

Dans cet exemple, à chaque requête envoyée, la console va afficher l'heure de son arrivée dans la fonction _timeLog_.

> **_Remarque :_** ```next()```va nous permettre de sortir du ```app.use()```, pour que la requête puisse être trouvée par les autres fonctions.

Un autre exemple d'utilisation est lors du chargement de fichiers statiques. Nous allons le voir plus tard, mais lorsque l'on va créer une route qui renvoie à un fichier html, nous allors devoir charger le ficher dans la réponse. Pour éviter le chargement de ces fichiers à la main à chaque fois, on ajoute un middleware dont le boulot est de gérer les fichiers statiques : ```express.statique()``` va nous servir à cela.

Ainsi, dans notre code, nous allons ajouter une ligne : 
~~~javascript
app.use("/static", express.static(__dirname + '/static'))
~~~

> **_Remarque :_** Notez le ```"/static"``` qui correspond ici à la base du path dont nous parlions au début de cette partie.

Pour plus d'informations : [https://expressjs.com/en/api.html#app.use](https://expressjs.com/en/api.html#app.use)

#### Contexte d'utilisation pour ```app.get()``` et ```app.post()```





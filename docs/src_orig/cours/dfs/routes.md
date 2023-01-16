---
layout: layout/post.njk 
title:  "Les routes"
category: cours
tags: node express test
authors: "Tina Alaei"
---

Le but d’un serveur web est de répondre à des requêtes (une url). Cette réponse peut prendre des formes très diverses, les plus courantes étant du html ou des données aux format json. Nous allos donc apprendre a mettre en place des routes. Chaque différente url sera une route qui nous renverra à une réponse que l'on lui aura assigné.


## Concept

Dans un nouveau fichier ```app.js``` nous allons définir les réponses des requêtes possible sur note site web.

Un exemple de ce à quoi se fichier peut ressember se presente ainsi :

_app.js_
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

Express est un framework pour Node.js qui va nous faciliter l'écriture de ce fichier ```app.js```.

### Installation

Express se met en place dans votre projet à l'aide de la commande ```yarn add express``` (ou ```npm install express```).

On l'importe alors dans notre fichier ```app.js``` avec ```require```:

~~~javascript
var express = require('express')
var app = express()
~~~

### Utilisation

> **_Remarque :_** La documentation pour le routage en Express est accessible [ici](https://expressjs.com/fr/guide/routing.html).

Via, l'import d'express montré dans **_Installation_**, nous avons créé une insatnce dans la classe ```express``` dans ```app```.

Notre code pour ```app.js``` devient :

_app.js_
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

_Exemple d'application courant dans le ```app.js```_
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

GET et POST sont des méthodes de requête HTTP. On dit qu'on utilise en principe la méthode 
GET pour récupérer des données, et la méthode POST pour envoyer des données au serveur.

La méthode GET passe en Express, sans grandes surprises, par ```app.get()``` et la méthode POST passe par ```app.post()```.

_Exemple d'application_

~~~javascript
app.get('/', (request, response) => {
    response.statusCode = 200;
    response.setHeader('Content-Type', 'text/html');
    response.sendFile('./index.html');
})
~~~

Ici, la requete ```'/'``` renvoie à la page ```index.html```. On peut éventuellement aussi utiliser une redirection, 
avec ```response.redirect(301, "index.html")```.

Pour avoir la liste des méthodes que l'on peut associer à une réponse en Express, vous pouvez les voir [ici dans la 
documentation](https://expressjs.com/en/api.html#res).

**Passer des paramètres dans l'url**

Pour indiquer un passage de paramètre dans l'url, on va écrire la requête telle que ```:nom-du-paramètre```. Par 
exemple une route telle que ```'/article/:idArticle'``` prend en paramètre un id d'article.

_Exemples d'utilisation :_
- Le passage de paramètre à une route API
- Utiliser le template mais pour des routes différentes (par exemple, l'affichage d'articles dans un blog : on ne va pas créer une nouvelle page à chaque fois, on va faire appel au même template, que l'on remplira selon ce qui est dans l'article appelé par la requête)


#### Gestion de plusieurs fichiers de route

Si vous voulez mettre les routes dans un fichier séparé (par ex ```routes.js```) , vous pouvez créer le structurer de 
cette façon:

~~~javascript
module.exports = function(app){
    // placer ici les app.use(), app.get() ...
}
~~~

et depuis votre fichier de routes principal :

~~~javascript
require('./routes')(app);
~~~

## Tests de routes

Pour tester nos routes, on peut utiliser un outil spécialisé comme postman ou une bibliothèque de test comme supertest.

### Postman

Postman est un outil plutôt utilisé dans le cadre des routes des APIs.

Vous pouvez le télécharger ici : [https://www.postman.com/downloads/](https://www.postman.com/downloads/).

En ouvrant un testeur de requêtes (cadre 1), on peut entrer une url qu'on veut tester avec la méthode HTTP correspondante (cadre 2) et éventuellement ajouter les paramètres que l'on veut envoyer avec la route dans _Query Params_ (cadre 3). En cliquant sur _Send_, on verra la réponse de l'url dans la partie _Response_ (cadre 4). Les routes que l'ont teste sont conservées dans l’historique (cadre 5) pour pouvoir être réutilisées facilement ensuite.

_Interface de postman :_
![Interface de postman](images/postman.png)

Cet outil est particulièrement utile en développement, mais pour des tests à refaire régulièrement ce n'est pas recommandé.

> **_Remarque :_** Cela peut se faire avec la partie _Collections_ dans postman. Vous pouvez consulter ce tuto openclassroom pour plus d'information : [Testez votre API grâce à Postman](https://openclassrooms.com/fr/courses/4668056-construisez-des-microservices/5123020-testez-votre-api-grace-a-postman) dans la partie _Comprendre Postman_.

### Supertest

Supertest est une bibliothèque qui va justement nous permettre de faire des tests réguliers.

#### Installation

Express se met en place dans votre projet à l'aide de la commande ```yarn add --dev supertest``` (ou ```npm install supertest --save-dev```).

On y fera appel grâce à la ligne :
~~~javascript
const request = require('supertest');
~~~

#### Utilisation

Les test de routes servent essentiellement à verifier que nos routes aboutissent correctement, par exemple, lorsque nous voulons être sûrs que telle route n'aboutisse pas à un 404, que telle route est bien innaccessible sous certaines conditions, etc ... Notez donc que ces tests ne vont pas avoir le même objectif que les tests unitaires et les user story.

> **_Remarque :_** Pour le bon fonctionnement de supertest, il faut d'abord bien vous assurer que le serveur de votre application se lance bien dans un autre fichier que vos routes.

On crée alors nos tests de routes dans un fichier ```routes.test.js```.

Un exemple de ce à quoi se fichier peut ressembler se presente ainsi :

~~~javascript
const request = require('supertest');
const app = require('../app');

let user;
let server;

beforeAll(async () => {
    user = await request.agent(app);
    server = await app.listen(3000);
});

afterAll(async () => {
    await server.close();
});


test('GET index.html', (done) => {
    //Le test
})

test('GET 404', (done) => {
    //Le test
})
~~~

Vous pouvez trouver la [documentation pour les fonctions de jest](https://jestjs.io/docs/en/api.html) telle que ```beforeAll()```, ```afterAll()```, ```test()```.

Vous pouvez trouver une [documentation pour les fonctions de supertest](https://npmdoc.github.io/node-npmdoc-supertest/build/apidoc.html) grâce à laquelle vous allez pouvoir construire l'intérieur des fonctions de test.

Un exemple avec 'GET index.html' :

~~~javascript
test('GET index.html', (done) => {
    user.get('/')
        .expect(301)
        .expect(function(res) {
            expect(res.headers.location).toBe('/static/index.html')
        })
        .end((err, res) => {
            if (err) {
                return done(err);
            }
            done()
        })
})
~~~

### Liens importants

Cette partie répertorie les liens de documentation utiles cités plus haut.

[Documentation pour les réponses des requêtes HTTP en Node.js](https://nodejs.org/api/http.html#http_class_http_serverresponse)

[Documentation pour le routage en Express](https://expressjs.com/fr/guide/routing.html)

[Documentation pour l'utilisation de app.use() en Express](https://expressjs.com/en/api.html#app.use)

[Documentation pour les réponses des requêtes HTTP en Express](https://expressjs.com/en/api.html#res)

[Documentation pour les fonctions de jest](https://jestjs.io/docs/en/api.html)

[Documentation pour les fonctions de supertest](https://npmdoc.github.io/node-npmdoc-supertest/build/apidoc.html)


---
layout: page
title:  "Projet numérologie : partie 2 / niveau 1 / serveur web minimal"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 2]({% link cours/web/projets/numerologie/partie-2-post-get/index.md %}) / [niveau 1]({% link cours/web/projets/numerologie/partie-2-post-get/niveau-1/index.md %}) / [serveur web minimal]({% link cours/web/projets/numerologie/partie-2-post-get/niveau-1/1-serveur-web-minimal.md %})
{: .chemin}

On utilise node comme un serveur web qui dit bonjour.

## prérequis

Vous devez avoir un projet de la [partie 1]({% link cours/web/projets/numerologie/partie-1-front/index.md %}). Nous nous baserons sur les [fichiers du niveau 1]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/5-structures.md %}).

On suppose que la racine du projet est *"numerologie"*.

## un serveur web minimal

Le but d'un serveur web est d'attendre qu'un client le contacte et lui demande des choses sous la forme d'une url et d'une méthode. Le serveur lui répond avec un status et un message.

### le code

Créez un fichier *"numerologie/index.js"* qui sera le point d'entrée de notre serveur :

```javascript
const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
```

> Ce serveur est celui donné dans [la doc de node](https://nodejs.org/api/synopsis.html#synopsis_example)

Pour exécuter ce fichier, dans un terminal placé dans le dossier où se trouve *"index.js"* (normalement *"numerologie"*), tapez la commande :

```shell
node index.js
```

Le programme s'exécute dans le terminal et il ne rend pas la main. Il ne s'arrête pas et demande d'aller voir à l'url : <http://127.0.0.1:3000>.

SI on tape cette adresse dans un navigateur on voit le texte : `Hello World` s'afficher.

### anatomie du code

Regardons la syntaxe :

* `const` : déclaration de constantes.
* `require` : importation d'une bibliothèque (ici la bibliothèque [http](https://nodejs.org/api/http.html) de node) et affectation de celle-ci à une constante : en javascript **on importe toujours quelque chose**
* les fonctions peuvent se créer à la volée avec : `nomFonction((paramètres) => {})`

Que fait le code :

1. on crée un serveur avec la fonction [http.createServer](https://nodejs.org/api/http.html#http_http_createserver_options_requestlistener). Cette fonction prend **1 paramètre** en argument qui est une fonction. Cette fonction sera appelée à chaque appelle au serveur avec deux paramètres :
   1. `req` (qui contiendra la **requête `http`**) : de type [`http.IncomingMessage`](https://nodejs.org/api/http.html#http_class_http_incomingmessage)
   2. `res` (qui contiendra notre **réponse `http`**) : de type [`http.ServerResponse`](https://nodejs.org/api/http.html#http_class_http_serverresponse)
2. une fois le serveur crée on le place derrière un port de la machine, ici 3000.

> La réponse aux requêtes du serveur est un objet qui existe déjà, ce n'est pas la réponse de notre fonction. Le boulot d'un serveur node est de renseigner les champs de cet objet puis de l'envoyer (avec [`res.end()`](https://nodejs.org/api/http.html#http_response_end_data_encoding_callback) par exemple).
{: .attention}

### protocole http

On ne va pas faire un long cours sur le [protocole http](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol), on va juste décrire succinctement les requêtes (ce que le serveur reçoit du navigateur) et les réponses (ce que le serveur envoie au navigateur).

> Utiliser node nous permet de nous concentrer sur ce qui est important : répondre correctement aux demande du navigateur, sans avoir besoin d'écrire des requêtes http convfrme (ce qui n'est pas très marrant).

#### requête http

On peut afficher l'url de la requête : On récupère les variables *hostname* et *port* et on les affiche dans la console.

Une requête http est en deux parties :

* des entêtes qui font la demande
* le corps du message (qui est souvent vide)
  
On peut par exemple modifier notre serveur dans le fichier *"numerologie/index.js"* :

```javascript
// ...

const server = http.createServer((req, res) => {

    console.log("-------")
    console.log(req.headers);
    console.log("========")
    console.log(req.httpVersion);
    console.log("========")
    console.log(req.method);


    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

// ... 
```

Si l'on recharge le serveur dans le vaviguateur, on obtient quelque chose du genre :

```text
-------
/
========
GET
========
1.1
========
{
  host: '127.0.0.1:3000',
  connection: 'keep-alive',
  'cache-control': 'max-age=0',
  'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
  accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site': 'none',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
}
-------
/favicon.ico
========
GET
========
1.1
========
{
  host: '127.0.0.1:3000',
  connection: 'keep-alive',
  pragma: 'no-cache',
  'cache-control': 'no-cache',
  'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
  'sec-ch-ua-platform': '"macOS"',
  accept: 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'no-cors',
  'sec-fetch-dest': 'image',
  referer: 'http://127.0.0.1:3000/',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
}

```

> A chaque actualisation, le serveur est **sollicité deux fois**, une fois pour l'url `/` et une autre fois pour l'url [`/flavicon.ico`](https://fr.wikipedia.org/wiki/Favicon).

Pour résumer :

* le navigateur parle en http 1.1 (ce qui est ok)
* les [headers](https://developer.mozilla.org/fr/docs/Web/HTTP/Headers) nous informent un peut plus sur lui
* il demande avec la [méthode](https://developer.mozilla.org/fr/docs/Web/HTTP/Methods) **GET** l'url `/` au serveur puis l'url `/flavicon.ico`

**Pour répondre à une requête http de façon satisfaisante, le serveur à toujours besoin de :**

* l'url
* de la méthode http utilisée par le serveur

La version de l'http n'est pas importante pour nous, c'est node qui s'occupe de communiquer directement avec le navigateur.

#### réponse http

Une réponse http **est toujours** en trois parties :

* le [status code](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP) qui résume ce que le serveur a fait avec la requête
* des [headers](https://developer.mozilla.org/en-US/docs/Glossary/Response_header)
* le corps du message (qui peut, mais c'est rare) être vide.

Dans notre cas :

* le status est [200](https://http.cat/200) (ou [200](https://httpstatusdogs.com/200) si vous êtes ce genre de personnes)
* le header informe le navigateur du [type de message](https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/Content-Type) : ici du texte
* le message complet : ici la chaine de caractère `'Hello World\n'`

## status

Les [status HTTP](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP) d'un serveur sont importants car ils informent le client de comment on a compris leur requête.

Dans les [outils de développement]({% link cours/web/tuto_outils_dev.md %}), c'est l'onglet network qui renseigne de ces champs.

En gros :

* 2XX: ok
* 3XX : redirection
* 4XX : requête non trouvée/non autorisée
* 5XX : erreur serveur

> Les informaticiens aiment le lol. Le status 418 fait parti d'une RFC publiée le 1/04/1998.

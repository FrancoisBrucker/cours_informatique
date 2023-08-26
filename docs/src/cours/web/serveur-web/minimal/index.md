---
layout: layout/post.njk

title: "Serveur web minimal"
authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

On utilise `node` comme un serveur web qui dit bonjour.

<!-- fin résumé -->

Le but d'un serveur web est d'attendre qu'un client le contacte et lui demande des choses sous la forme d'une url et d'une méthode. Le serveur lui répond avec un status et un message.

## Préparation

{% faire %}
Créez un dossier `serveur_web`{.fichier} où l'on stockera les fichiers de notre serveur.
{% endfaire %}

Comme on va utiliser node pour gérer notre serveur, on crée le fichier node du projet :

{% faire %}

Dans le dossier `serveur_web`{.fichier}, initialisez le projet en tapant la commande : `npm init` puis en tapant entrée à chaque question pour utiliser les réponses par défaut.
{% endfaire %}

Vous devriez maintenant avoir un fichier nommé `package.json`{.fichier} qui contient la configuration minimale d'un projet utilisant node :

```json#
{
  "name": "code",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```

Nous allons y ajouter une configuration que vous devrez utiliser à chaque fois que vous utiliserez des bibliothèques en node (c'est à dire tout le temps) :

{% faire %}
Ajouter la ligne `"type": "module",`{.language-} dans le fichier de configuration `package.json`{.fichier}, juste en-dessous de la ligne 5

{% endfaire %}

A la fin de cette opération, vous devriez avoir le fichier un fichier nommé `package.json`{.fichier} qui contient la configuration minimale d'un projet utilisant node :

```json#
{
  "name": "code",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```

{% info %}
Nous allons utiliser dans toute la suite de ce cours la gestion javascript des modules (es6 modules) et non celle historique de node (commonJS). Si vous cherchez du code sur internet, vous pourrez tout de suite voir de quel type d'import il s'agit :

* `import http from 'http';`{.language-} : import javascript
* `const http = require('http');`{.language-} : import commonJS

Lorsque vous importez des bibliothèques node, il suffit souvent de remplacer une écriture par l'autre pour que tout fonctionne.

{% endinfo %}

## Le code

Créez un fichier `serveur_web/index.js`{.fichier} qui sera le point d'entrée de notre serveur :

```javascript
import http from 'http';

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

{% info %}
Ce serveur est celui donné dans [la doc de node](https://nodejs.org/api/synopsis.html#synopsis_example)
{% endinfo %}

Pour exécuter ce fichier, dans un terminal placé dans le dossier où se trouve `index.js`{.fichier} (normalement `serveur_web`{.fichier}), tapez la commande :

```
node index.js
```

Le programme s'exécute dans le terminal et il ne rend pas la main. Il ne s'arrête pas et demande d'aller voir à l'url : <http://127.0.0.1:3000>. Si on tape cette adresse dans un navigateur on voit le texte : `Hello World`{.language-} s'afficher.

{% note %}
Nous venons de créer un serveur web sur notre machine locale sur le port 3000.

La machine locale s'appelle :

* `127.0.0.1` avec des nombres
* `localhost` avec des lettres
{% endnote %}

{% info %}
Allez du côté de la partie [port du cours sur les url](../../anatomie-url#port){.interne} pour vous rappeler ce qu'est un port.
{% endinfo %}

Regardons la syntaxe du code :

* `const`{.language-} : déclaration de constantes.
* `import from`{.language-} : importation d'une bibliothèque (ici la bibliothèque [http](https://nodejs.org/api/http.html) de node) et affectation de celle-ci à une variable (nommée aussi `http`{.language-}) : en javascript **on importe toujours quelque chose**

Que fait le code :

1. on crée un serveur avec la fonction [http.createServer](https://nodejs.org/api/http.html#http_http_createserver_options_requestlistener). Cette fonction prend **1 paramètre** en argument qui est une fonction. Cette fonction sera appelée à chaque appelle au serveur avec deux paramètres :
   1. `req` (qui contiendra la **requête `http`**) : de type [`http.IncomingMessage`](https://nodejs.org/api/http.html#http_class_http_incomingmessage)
   2. `res` (qui contiendra notre **réponse `http`**) : de type [`http.ServerResponse`](https://nodejs.org/api/http.html#http_class_http_serverresponse)
2. une fois le serveur crée on le place derrière un port de la machine, ici 3000.

{% attention %}
La réponse aux requêtes du serveur est un objet qui existe déjà, ce n'est pas la réponse de notre fonction. Le boulot d'un serveur node est de renseigner les champs de cet objet puis de l'envoyer (avec [`res.end()`](https://nodejs.org/api/http.html#http_response_end_data_encoding_callback) par exemple).
{% endattention %}

## Protocole http

On ne va pas faire un long cours sur le [protocole http](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol), on va juste décrire succinctement les requêtes (ce que le serveur reçoit du navigateur) et les réponses (ce que le serveur envoie au navigateur).

{% note %}
Utiliser node nous permet de nous concentrer sur ce qui est important : répondre correctement aux demandes du navigateur, sans avoir besoin d'écrire des requêtes http conformes (ce qui n'est pas très marrant).
{% endnote %}

### Requête http

On peut afficher l'url de la requête : On récupère les variables *hostname* et *port* et on les affiche dans la console.

Une requête http est en deux parties :

* des entêtes qui font la demande
* le corps du message (qui est souvent vide)
  
On peut par exemple modifier notre serveur dans le fichier `serveur_web/index.js`{.fichier} :

```javascript
// ...

const server = http.createServer((req, res) => {

    console.log("-------")
    console.log(req.url);
    console.log("========")
    console.log(req.method);
    console.log("========")
    console.log(req.httpVersion);
    console.log("========")
    console.log(req.headers);

    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

// ... 
```

{% info %}
Lorsque l'on modifie le serveur, il faut arrêter l'ancien (avec les touches `ctrl+c`) et le relancer. Même si l'o modifie le code de `serveur_web/index.js`{.fichier} il n'est pas pris automatiquement en compte par le serveur.
{% endinfo %}

Si l'on recharge le serveur dans le navigateur, on obtient quelque chose du genre :

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

{% note %}
A chaque actualisation, le serveur est **sollicité deux fois**, une fois pour l'url `/` et une autre fois pour l'url [`/flavicon.ico`](https://fr.wikipedia.org/wiki/Favicon).
{% endnote %}

Pour résumer :

* le navigateur parle en http 1.1 (ce qui est ok)
* les [headers](https://developer.mozilla.org/fr/docs/Web/HTTP/Headers) nous informent un peut plus sur lui
* il demande avec la [méthode](https://developer.mozilla.org/fr/docs/Web/HTTP/Methods) **GET** l'url `/` au serveur puis l'url `/flavicon.ico`

{% note "**Pour répondre à une requête http de façon satisfaisante, le serveur à toujours besoin de**" %}

* l'url
* de la méthode http utilisée par le serveur

{% endnote %}

La version de l'http n'est pas importante pour nous, c'est node qui s'occupe de communiquer directement avec le navigateur.

### Réponse http

Une réponse http **est toujours** en trois parties :

* le [status code](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP) qui résume ce que le serveur a fait avec la requête
* des [headers](https://developer.mozilla.org/en-US/docs/Glossary/Response_header)
* le corps du message (qui peut, mais c'est rare) être vide.

Dans notre cas :

* le status est [200](https://http.cat/200) (ou [200](https://httpstatusdogs.com/200) si vous êtes ce genre de personnes)
* le header informe le navigateur du [type de message](https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/Content-Type) : ici du texte
* le message complet : ici la chaîne de caractère `'Hello World\n'`

### Status

Les [status HTTP](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP) d'un serveur sont importants car ils informent le client de comment on a compris leur requête.

Dans les [outils de développement]({{"/cours/web/outils-de-développement" | url}}), c'est l'onglet network qui renseigne de ces champs.

En gros :

* 2XX: ok
* 3XX : redirection
* 4XX : requête non trouvée/non autorisée
* 5XX : erreur serveur

{% info %}
Les informaticiens aiment rigoler. Le status 418 fait parti d'une RFC publiée le 1/04/1998.
{% endinfo %}

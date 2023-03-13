---
layout: layout/post.njk

title: "Gestion des routes"
authors:
    - "François Brucker"


eleventyNavigation:
  key: "Gestion des routes"
  parent: "Serveur Web"
---

<!-- début résumé -->

Gestion des routes avec un serveur web.

<!-- fin résumé -->

{% note "**Définition**" %}
Le but d'un serveur web est de répondre quelque chose à partir d'une requête constituée d'une url et d'une méthode (GET ou POST). Ces différentes url auxquelles peut répondre un serveur sont appelées **routes**.

{% endnote %}

Certaines routes vont nécessiter du travail comme faire une requête en base de données, calculer des choses, etc, et d'autres consisteront seulement à rendre (on dit **servir**) un fichier html, css ou encore javascript qui sera exécuté par le navigateur.

Il est crucial de bien organiser les routes d'un serveur pour pouvoir le modifier et l'agrandir facilement.

## Préparation

Reprenons le serveur de la [partie précédente](../minimal) :

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

Et lançons notre serveur avec la commande :

```
node index.js
```

## Racine du site

Modifions le code du serveur pour qu'il lise un fichier html :

```javascript
import http from 'http';
import fs from 'fs';

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');

    let fichier = fs.readFileSync("./index.html", {encoding:'utf8'})
    res.end(fichier);
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
```

On teste le serveur et on voit que ça ne marche qu'à peut prêt.

En effet, on rend toujours la même chose : le fichier `index.html`{.fichier} même si le client demande autre chose. Regardons ce que demande le client en ajoutant une ligne au début de notre serveur :

```javascript
// ...

const server = http.createServer((req, res) => {
    console.log(req.url)

    // ...

// ...
```

Re-testons le serveur et regardons le résultat dans la console lorsque l'on charge une page :

```text
Server running at http://127.0.0.1:3000/
/
/favicon.ico
```

A chaque chargement de page, le navigateur demande son [flavicon](https://www.w3schools.com/html/html_favicon.asp) associé. Notre navigateur ne peut donc pas rendre toujours a même chose !

## Image flavicon

Commençons par créer [un superbe flavicon](./code/favicon.ico) avec le site <https://www.favicon.cc/> puis ajoutons une route à notre serveur :

```javascript

// ...

const server = http.createServer((req, res) => {
    console.log(req.url)
    if (req.url === "/" || req.url === "/index.html") {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html');
    
        let fichier = fs.readFileSync("./index.html", {encoding:'utf8'})
        res.end(fichier);
    }
    else {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'image/x-icon');
    
        let fichier = fs.readFileSync("./favicon.ico")
        res.end(fichier);

    }

});

// ...

```

Notez que pour la route dédiée au flavicon on n'utilise plus l'encodage 'utf8', réservé aux fichiers textes comme le html par exemple.

## 404

Notre serveur est vraiment frustre, il ne permet de rendre que un fichier html soit un favicon. Si on tape n'importe quelle autre route que `/` ou `/index.html` on obtient notre icône... Remédions à ça en créant rendant un [statut 404](https://http.cat/404) si l'url demandée n'est pas une route valide :

```javascript
// ...

const server = http.createServer((req, res) => {
    console.log(req.url)
    if (req.url === "/") {
        console.log("index")
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html');
    
        let fichier = fs.readFileSync("./index.html", {encoding:'utf8'})
        res.end(fichier);
    }
    else if (req.url === "/favicon.ico") {
        console.log("fav")
        res.statusCode = 200;
        res.setHeader('Content-Type', 'image/x-icon');
    
        let fichier = fs.readFileSync("./favicon.ico")
        res.end(fichier);
    }
    else {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end();
    }    
});

// ...
```

{% note %}
Le `res.end()` est indispensable dans la gestion du 404, sinon le navigateur attendra la réponse du serveur jusqu'à la fin des temps (ou un timeout).
{% endnote %}

## Fichiers statiques

Les fichier statiques sont les fichiers qui seront pris directement sur le disque dur du serveur et envoyés au navigateur sont appelées **fichiers statiques**. Comme notre fichier `index.html`{.fichier}.

Plus un serveur a de fichiers statiques, mieux c'est puisque ces fichiers ne changent pas au court du temps. On peut utiliser sur eux des méthodes de [cache](https://fr.wikipedia.org/wiki/Cache_web) (côté client et serveur) ou encore de [load-balancing](https://fr.wikipedia.org/wiki/R%C3%A9partition_de_charge) pour accélérer le résultat (le réseau coûte toujours du temps).

{% note %}
On essayera toujours de déplacer le travail du serveur (unique) aux clients (multiples).

De là, on maximisera les fichiers statiques remplis de javascript qui construiront la page côté client ou qui ne feront des appels serveur pour récupérer ou transmettre des données.
{% endnote %}

### Servir des fichiers statiques

L'usage veut que tous les fichiers statiques soient servies à partir d'une url reconnaissable. Dans notre cas, nous allons faire commencer toutes les url servant un fichier statique par `/static/`

```javascript

// ...

const server = http.createServer((req, res) => {
    console.log(req.url)

    if (req.url === "/") {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html');
    
        let fichier = fs.readFileSync("./index.html", {encoding:'utf8'})
        res.end(fichier);
    }
    else if (req.url.startsWith("/static/")) {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html');
    
        let fichier = fs.readFileSync("." + req.url.substring(7), {encoding:'utf8'})
        res.end(fichier);
    }
    else {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end();
    }
});

// ...

```

Si l'url est du type `/static/[fin de l'url]`, le serveur essaye de lire le fichier nommé `[fin de l'url]`{.fichier} dans le répertoire courant.

Ceci est effectué en :

1. prenant la variable `req.url`{.language-}
2. en supprimant ses 7 premiers caractères ([méthode `substring`{.language-}](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/String/substring)). Dans notre cas, si `req.url`{.language-} vaut `/static/[fin de l'url]`, alors `req.url.substring(7)`{.language-} vaudra `/[fin de l'url]`
3. en concaténant avec `.` puis en chargeant ce fichier. Dans notre cas, on cherche à lire le fichier `./[fin de l'url]`{.fichier}
4. Une fois ce fichier lu avec la méthode [`fs.readFileSync`{.language-}](https://nodejs.org/api/fs.html#fsreadfilesyncpath-options), il est envoyé par le serveur

On commence à voir deux besoins indispensables dans la gestion des routes :

* il faut pouvoir choisir une route parmi plusieurs possibles
* il faut pouvoir séparer l'url en plusieurs parties

{% faire %}
Accédez au fichier `index.html`{.fichier} des deux façons possibles.
{% endfaire %}

### Fichiers statiques en développement et en production

Il ne faut jamais servir de fichier statique en **production** avec node. C'est **mal** car il n'est pas fait pour ça : il prendra plus de temps, n'utilisera pas de load-balancing, etc. L'usage veut qu'on utilise un serveur dédié comme [nginx](https://www.nginx.com/) qui fait du cache, de la répartition de charge et tout ce genre de choses pour nous.

On ne sert de fichier statiques qu'en développement ou en test.

En production, on a coutume d'utiliser 1 serveur général qui va dispatcher les requêtes à tous les serveurs spécifiques. Ceci permet de lisser la charge et de créer autant de serveur que l'on a de services.

Par exemple, supposons que l'on possède une machine de nom `ovh1.ec-m.fr`. On lui accole un serveur web principal (généralement [apache](https://httpd.apache.org/)) sur le port 80 (pour le protocole http) qui va recevoir toutes les requêtes :

* par exemple :
  * si la requête commence par `trombi.ovh1.ec-m.fr` (c'est un sous-domaine de la machine `ovh1.ec-m.fr`) il fa renvoyer la requête au serveur node qui est sur le port 7000 de la machine `ovh1.ec-m.fr`
  * si la requête commence par `bitcoin.ovh1.ec-m.fr` (c'est un sous-domaine de la machine `ovh1.ec-m.fr`) il fa renvoyer la requête au serveur node qui est sur le port 7777 de la machine `ovh1.ec-m.fr`
  * ...
* Si la requête est de la forme `XXX.ovh1.ec-m.fr/static/` il va renvoyer la requête au serveur nginx qui va servir les fichier du dossier `/usr/XXX/static`{.fichier} sur la machine `ovh1.ec-m.fr`

Cette mécanique fait en sorte que les url commençant par `/static` ne sont jamais vues des serveur dédiés dans un environnement de production. On peut donc tranquillement laisser la route `static` qui ser utile en développement et inutilisée en production.

## API

On va suivra la même méthode pour les appels serveur qui ne sont pas des fichiers statiques. L'usage veut que l'url commence par `/api/`. Ceci permet de gérer des versions différentes de serveur. Lisez [la réponse à ce post](https://stackoverflow.com/questions/389169/best-practices-for-api-versioning) pour avoir une bonne idée de comment procéder.

## Jardinons un peu le code

La version ci-après du serveur est une version améliorée du précédent qui :

* raccourcit et factorise les routes
* gère de façon précise les fichiers

```javascript
import http from 'http';
import fs from 'fs';
import path from 'path';

import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);


const server = http.createServer((req, res) => {
    console.log(req.url)

    if (req.url === "/") {
        res.writeHead(301,{Location: "http://" + req.headers['host'] + '/static/index.html'});
        res.end();
        return;
    } else  if (req.url.startsWith("/static/")) {
        fichier = path.join(__dirname,  req.url.substring(7))
    } else {
        fichier = ""
    }
    console.log("fichier : " + fichier)
    
    if (fs.existsSync(fichier)) {
        res.writeHead(200,  {'Content-Type': 'text/html'})
    
        fichier = fs.readFileSync(fichier, {encoding:'utf8'})
        res.end(fichier);
    }
    else {
    res.writeHead(404,  {'Content-Type': 'text/plain'})
    res.end();
    }
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});

```

### Redirection

Nous avons [redirigé](https://http.cat/301) la requête `/` vers son fichier. Ceci nous permet de n'avoir qu'une seule façon de gérer `index.html`.

### headers

On peut utiliser `res.writeHead(200,  {'Content-Type': 'text/html'})` pour écrire en une fois le status et le type de la réponse.

### Localisation des fichiers

La localisation d'un fichier sur le disque dur est une opération :

* non triviale
* dépendante de l'architecture du disque dur sur lequel le programme tourne

C'est très problématique pour les serveur web puisque l'on veut que le code fonctionne sur la machine du (des) développeur(s) et sur la (les) machine(s) de production. Chacune ayant un autre disque dur et une autre architecture.

La seule chose donc on peut être sur c'est que le projet est identique sur toutes ces machines. On utilise alors une notation relative pour trouver le fichier.

Nous avons utiliser la notation `"./index.html"` pour indiquer que le fichier `index.html`{.fichier} se trouve dans le dossier courant. Mais qu'est-ce que le dossier courant ?

Le **dossier courant** est le dossier dans lequel se trouve le terminal qui a exécuté la commande node. De là, notre serveur :

* **fonctionnera** si on le lance depuis le dossier où se trouve les fichier avec la commande : `node index.js`
* **ne fonctionnera pas** si on le lance depuis le dossier parent avec la commande : `node serveur_web/index.js`. Le serveur trouvera bien `serveur_web/index.js`{.fichier} mais n'arrivera pas à trouver `./index.html`{.fichier} dans le code.

Il ne faut donc pas prendre comme référence le dossier courant mais le dossier où est `index.js`{.fichier}

Node nous permet de faire ça en définissant les constantes `__filename`{.language-} et `__dirname`{.language-} en début de programme. Ces deux constantes contiennent respectivement le nom et le dossier du fichier exécuté (ici notre serveur). On utlise ensuite ce dossier comme racien de notre projet.

Enfin, on ne concatène **jamais** des fichiers à la main. On utilise **toujours** une bibliothèque pour cela (sinon c'est *bad karma* : ça va forcément vous sauter à la tête un jour) qui traite tous les cas particulier pour vous. En node, c'est la [bibliothèque path](https://nodejs.org/api/path.html) qui s'occupe de ça.

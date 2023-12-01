---
layout: layout/post.njk

title: "Gestion des routes"
authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Gestion des routes avec un serveur web.

<!-- fin résumé -->

> TBD : faire avec du texte, pas de fichiers,

{% note "**Définition**" %}
Le but d'un serveur web est de répondre quelque chose à partir d'une requête constituée d'une url et d'une méthode (GET ou POST). Ces différentes url auxquelles peut répondre un serveur sont appelées **routes**.

{% endnote %}

Certaines routes vont nécessiter du travail comme faire une requête en base de données, calculer des choses, etc, et d'autres consisteront seulement à rendre (on dit **servir**) un fichier html, css ou encore javascript qui sera exécuté par le navigateur.

Il est crucial de bien organiser les routes d'un serveur pour pouvoir le modifier et l'agrandir facilement.

## Préparation

Reprenons le serveur de la [partie précédente](../minimal){.interne} :

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
```

{% info %}
Si vous utilisez le navigateur chrome, à chaque chargement de page, il demande en plus une requête [flavicon](https://www.w3schools.com/html/html_favicon.asp) 0 la suite de la première requête.
{% endinfo %}

## 404

Notre serveur est vraiment frustre, il ne permet de rendre que d'un fichier html. Si on tape n'importe quelle autre route que `/` on obtient tout dem même notre fichier html... Remédions à ça en créant rendant un [statut 404](https://http.cat/404) si l'url demandée n'est pas une route valide :

```javascript
// ...

const server = http.createServer((req, res) => {
    console.log(req.url)
    if ((req.url === "/") || (req.url === "/index.html")) {
        console.log("index")
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html');
    
        let fichier = fs.readFileSync("./index.html", {encoding:'utf8'})
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

Plus un serveur a de fichiers statiques, mieux c'est puisque ces fichiers ne changent pas au cours du temps. On peut utiliser sur eux des méthodes de [cache](https://fr.wikipedia.org/wiki/Cache_web) (côté client et serveur) ou encore de [load-balancing](https://fr.wikipedia.org/wiki/R%C3%A9partition_de_charge) pour accélérer le résultat (le réseau coûte toujours du temps).

{% note %}
On essayera toujours de déplacer le travail du serveur (unique) aux clients (multiples).

De là, on maximisera les fichiers statiques remplis de javascript qui construiront la page côté client ou qui ne feront des appels serveur pour récupérer ou transmettre des données.
{% endnote %}

### Servir des fichiers statiques

L'usage veut que tous les fichiers statiques soient servies à partir d'une url reconnaissable. Dans notre cas, nous allons faire commencer toutes les url servant un fichier statique par `/static/`

{% faire %}
Déplacez vos fichiers html, css et js dans un dossier que vous nommerez `static/`{.fichier} dans le dossier de votre projet.
{% endfaire %}

```javascript

// ...

const server = http.createServer((req, res) => {
    console.log(req.url)

    if (req.url === "/") {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html');
    
        let fichier = fs.readFileSync("./static/index.html", {encoding:'utf8'})
        res.end(fichier);
    }
    else if (req.url.startsWith("/static/")) {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html');
    
        let fichier = fs.readFileSync("." + req.url, {encoding:'utf8'})
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

Si l'url est du type `/static/[fin de l'url]`, le serveur essaye de lire le fichier nommé `static/[fin de l'url]`{.fichier} dans le répertoire courant, c'est à dire un fichier qui se trouve dans le dossier `static/`{.fichier}.

Ceci est effectué en :

1. prenant la variable `req.url`{.language-}
2. en concaténant avec `.` puis en chargeant ce fichier. Dans notre cas, on cherche à lire le fichier `./static/[fin de l'url]`{.fichier}
3. Une fois ce fichier lu avec la méthode [`fs.readFileSync`{.language-}](https://nodejs.org/api/fs.html#fsreadfilesyncpath-options), il est envoyé par le serveur

On commence à voir deux besoins indispensables dans la gestion des routes :

* il faut pouvoir choisir une route parmi plusieurs possibles
* il faut pouvoir séparer l'url en plusieurs parties

{% faire %}
Accédez au fichier `index.html`{.fichier} des deux façons possibles.
{% endfaire %}

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

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    console.log(req.url)

    if (req.url === "/") {
        console.log("redirection");

        res.writeHead(301, {Location: "http://" + req.headers['host'] + '/static/index.html'});
        res.end();
    } else  if (req.url.startsWith("/static/")) {
        console.log("fichier statique");
        let fichier = path.join(__dirname,  req.url);
        
        res.writeHead(200,  {'Content-Type': 'text/html'});
        fichier = fs.readFileSync(fichier, {encoding:'utf8'});
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

Nous avons utiliser une [redirection](https://http.cat/301) de la requête `/` vers la requête `http://127.0.0.1:3000/static/index.html` (la variable `req.headers['host']`js contient le nom du serveur et son port. Affichez là dans la console pour vous en convaincre).

Ainsi, lorsque le serveur fait une requête `http://127.0.0.1:3000` :

1. le serveur lui répond que la ressource demandée est maintenant en `http://127.0.0.1:3000/static/index.html` en rendant un stats de 301 et la nouvelle localisation de la ressource
2. le client va refaire une requête avec la nouvelle localisation
3. cette nouvelle requête tombe dans le if des fichiers statique, et le fichier index.html pourra être servi.

{% faire %}
Faire l'expérience de la redirection en demandons depuis un navigateur la route `http://127.0.0.1:3000` et voir dans la console du serveur les deux appels : la requête initiale et la redirection.
{% endfaire %}

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

### A vous

{% faire %}
Ajoutez une route nommée `http://127.0.0.1/API/hasard` qui affiche (en texte) un réel aléatoire entre 0 et 1.
{% endfaire %}
{% info %}
Vous pourrez utiliser la méthode [`Math.random`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random) pour obtenir un réel entre 0 et 1 et le transformer en chaîne de caractère avec : `String` : `String(Math.random())`.
{% endinfo %}
{% details "solution" %}

Bloc à ajouter juste avant le bloc du 404 :

```javascript
    // ...

    else if (req.url.startsWith("/API/hasard")) {
        console.log("API");
        
        res.writeHead(200,  {'Content-Type': 'text/plain'});
        res.end(String(Math.random()));
    }

    // ...
```

{% enddetails %}

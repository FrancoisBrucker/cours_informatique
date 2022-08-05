---
layout: page
title:  "Projet numérologie : partie 2 / niveau 1 / web statique"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 2]({% link cours/web/projets/numerologie/partie-2-serveur/index.md %}) / [serveur web statique]({% link cours/web/projets/numerologie/partie-2-serveur/2-serveur-web-statique.md %})
{: .chemin}

On utilise node comme un serveur web de fichiers statiques.

> Il ne faut jamais servir de fichier statique en **production** avec node. C'est **mal** car il n'est pas fait pour ça. L'usage veut qu'on utilise un serveur dédié comme [nginx](https://www.nginx.com/) qui fait du cache, de la répartition de charge et tout ce genre de choses.
{: .attention}

## But

Le but d'un serveur web est de répondre quelque chose à partir d'une requête constituée d'une url et d'une méthode (GET ou POST). Certaines url vont nécessiter du travail comme faire une requête en base de données, calculer des choses, etc, et d'autres consisteront seulement à rendre un fichier html, css ou encore javascript qui sera exécuté par le navigateur.

Ces fichiers qui seront pris sur le disque dur du serveur et envoyé au navigateur sont appelées **fichiers statiques**.

> Plus on a de fichiers statiques, mieux c'est puisque ces fichiers ne changent pas on peut utiliser des méthodes de [cache](https://fr.wikipedia.org/wiki/Cache_web) (côté client et serveur) ou de [load-balancing](https://fr.wikipedia.org/wiki/R%C3%A9partition_de_charge) pour accélérer le résultat (le réseau coute toujours du temps).
>
> De là, si vous avez le choix entre un serveur web ou juste des fichiers statiques, choisissez **toujours** la seconde possibilité.

Nous allons ici utiliser la gestion de fichiers statiques pour monter la gestion des url d'un serveur web.

## gestion des fichiers avec node

On a déja vu un peu ça dans [le niveau 2 de la partie 1]({% link cours/web/projets/numerologie/partie-1-front/niveau-2/2-code_js.md %}#node-fichier). On chargeait entièrement le fichier avant de le traiter.

Commençons par utiliser ça pour charger le fichier *"numerologie/index.html"*

### on rend tout le temps la même chose

Modifions le fichier *"numerologie/index.js"* pour répondre le contenu d'un fichier :

```javascript
const http = require('http');
const fs = require('fs');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');

    fichier = fs.readFileSync("./index.html", {encoding:'utf8'})
    res.end(fichier);
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
```

On teste le serveur et on voit que ça ne marche qu'à peut prêt.

En effet, on rend toujours la même chose : le fichier *"index.html"* même si le client demande autre chose. Regardons ce que demande le client en ajoutant une ligne au début de notre serveur :

```javascript
// ...

const server = http.createServer((req, res) => {
    console.log(req.url)

    // ...

// ...
```

Re-testons le serveur et regardons le résultat dans la console : 

```text
Server running at http://127.0.0.1:3000/
/
/main.css
/numerologie.js
/favicon.ico
```

La lecture du fichier *"numerologie/index/html"* par le client lance de nouvelles requêtes au serveur pour obtenir *"main.css"*, *"numerologie.js"* et ... *"flavicon.ico"*.

### on rend une chose ou 404

Modifions le code de notre serveur  pour qu'il ne rendre *"index.html"* que and il faut :

```javascript
// ...

const server = http.createServer((req, res) => {
    console.log(req.url)

    if (req.url === "/" || req.url === "/index.html") {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html');
    
        fichier = fs.readFileSync("./index.html", {encoding:'utf8'})
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

On voit que notre serveur va répondre aux url valant `/` (c'est l'url par défaut même s'il n'y a rien) et `/index.html`. Il retournera un 404 pour tout le reste.

> [`==`vs `===` en javascript](https://www.guru99.com/difference-equality-strict-operator-javascript.html) : l'un fait de la conversion de type (`10 == "10"`sera vrai) l'autre non (`10 === "10"`sera faux).

Vous pouvez voir dans la console des [outils de éveloppement]({% link cours/web/tuto_outils_dev.md %}) les erreurs produites par les 404.

### on vérifie que le fichier existe avant

```javascript
// ...

const server = http.createServer((req, res) => {
    console.log(req.url)

    if (req.url === "/") {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html');
    
        fichier = fs.readFileSync("./index.html", {encoding:'utf8'})
        res.end(fichier);
    }
    else if (fs.existsSync("." + req.url)) {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html');
    
        fichier = fs.readFileSync("." + req.url, {encoding:'utf8'})
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

> Notez que le `res.end()` est indispensable dans la gestion du 404, sinon le navigateur attendra la réponse du serveur jusqu'à la fin des temps (ou un timeout).

## on jardine

On va juste un peut améliorer notre code pour le rendre :

1. plus joli
2. plus portable

Fichier *"numerologie/index.js"* :

```javascript
const path = require('path')

// ...

const server = http.createServer((req, res) => {
    console.log(req.url)

    if (req.url === "/") {
        fichier = path.join(__dirname, "./index.html")        
    } else {
        fichier = path.join(__dirname,  req.url)
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

// ...
```

Ajoutez la ligne `const path = require('path')` en début de fichier puis remplacez le serveur.

### headers

On peut utiliser `res.writeHead(200,  {'Content-Type': 'text/html'})` pour écrire en une fois le status et le type de la réponse.

### localisation des fichiers

La localisation d'un fichier sur le disque dur est une opération :

* non triviale
* dépendante de l'architecture du disque dur sur lequel le programme tourne

C'est très problématique pour les serveur web puisque l'on veut que le code fonctionne sur la machine du (des) développeur(s) et sur la (les) machine(s) de production. Chacune ayant un autre disque dur et une autre architecture.

La seule chose donc on peut être sur c'est que le projet est identique sur toutes ces machines. On utilise alors une notation relative pour trouver le fichier.

Nous avons utiliser la notation `"./index.html"` pour indiquer que le fichier *"index.html"* se trouve dans le dossier courant. Mais qu'est-ce que le dossier courant ?

Le **dossier courant** est le dossier dans lequel se trouve le terminal qui a exécuté la commande node. De là, notre serveur :

* **fonctionnera** si on le lance depuis le dossier où se trouve les fichier avec la commande : `node index.js`
* **ne fonctionnera pas** si on le lance depuis le dossier parent avec la commande : `node numerologie/index.js`. Le serveur trouvera bien *"numerologie/index.js"* mais n'arrivera pas à trouver *"./index.html"* dans le code.

Il ne faut donc pas prendre comme référence le dossier courant mais le dossier où est *"index.js"*.

Node nous permet de faire ça avec la constante `__dirname` qui contient le dossier où se trouve le fichier exécuté par node (il y a aussi `__filename` pour connaitre son nom)

> Si l'on exécute juste `node` pour se retrouver dans l'interpréteur, si `__dirname` ni `__filename` ne sont défini, ce qui est logique.

Enfin, on ne concatène **jamais** des fichiers à la main. On utilise **toujours** une bibliothèque pour cela (sinon c'est *bad karma* : ça va forcément vous sauter à la tête un jour) qui traite tous les cas particulier pour vous. En node, c'est la [bibliothèque path](https://nodejs.org/api/path.html) qui s'occupe de ça.

### principe de développement

On a aussi utilisé le principe du [DRY](https://fr.wikipedia.org/wiki/Ne_vous_r%C3%A9p%C3%A9tez_pas) en factorisant les lignes identiques.

Il y en a au moins un autre à connaître, c'est le [KISS](https://en.wikipedia.org/wiki/KISS_principle).

Ce sont des programming (ou code) mantra.

Voir par exemple :

* <http://stereobooster.github.io/programming-mantras>
* <https://medium.com/@codesprintpro/how-to-become-a-better-programmer-e9359e89dee2>
* ...

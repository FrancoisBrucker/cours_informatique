---
layout: page
title:  "Projet numérologie : partie 2 / niveau 1 / web avec express"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 2]({% link cours/web/projets/numerologie/partie-2-serveur/index.md %}) / [serveur web avec express]({% link cours/web/projets/numerologie/partie-2-serveur/3-serveur-web-express.md %})
{.chemin}

On utilise le module express pour gérer plus élégamment notre site.

## gestionnaire de package

[express](https://expressjs.com/) est un module pour node qui permet une gestion efficace et apaisée des site web.

Pour installer des packages node, on peut utiliser [npm](https://www.npmjs.com/) (**n**ode **p**ackage **m**anager) qui est livré avec node.

> Un [tutoriel pour utiliser npm](https://www.digitalocean.com/community/tutorials/how-to-use-node-js-modules-with-npm-and-package-json-fr)

### npm init

Pour que `npm` puisse gérer nos module, il faut lui laisser créer un fichier de configuration nommé *"package.json"*. Pour cela, tapez dans un terminal placé à la racine de notre projet :

```shell
npm init
```

Répondez aux questions (ou tapez sur entrée). Lorsque le programme est fini, vous trouverez un fichier *"package.json"* à la racine de votre projet.

Chez moi, il ressemble à ça :

```json
{
  "name": "numerologie",
  "version": "1.0.0",
  "description": "de la numérologie",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "François Brucker",
  "license": "WTFPL"
}

```

Il ne contient pour l'instant que des informations générales quant au projet. Nous allons bientôt y ajouter des modules.

> Le [json](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation) est un format texte pour sauvegarder des données structurée. C'est un format génial qui sert tout autant pour les fichiers de configurations que le transfert de données par le web.

### ajout d'un module

Pour cela, tapez dans un terminal placé à la racine de notre projet :

```shell
npm add --save express
```

> N'oubliez pas `--save`, sinon le module sera installé mais la dépendance ne sera pas ajoutée au fichier *"package.json"* ce qui est tarte.
{.attention}

Cette commande a ajouté une dépendance à notre fichier *"package.json"* :

```json
"dependencies": {
    "express": "^4.17.1"
  }
```

A créer un fichier *"package-lock.json"* qui contient la liste de tous les modules installés et un (gros) dossier *"node_modules"* qui contient les modules installés.

> Il y a plus de 50 modules installés alors que l'on a demandé d'installer que le module `express`, car il a lui même des dépendances et ses dépendances d'autres dépendances, etc.

La différence entre *"package.json"* et *"package-lock.json"* est que le premier décrit les versions possibles (nous, toutes les versions ultérieures à 4.17.1) alors que *"package-lock.json"* décrit la version effectivement installée (la 4.17.1). Cette méchanique permet de mettre à jour nos modules en supprimant le dossier *"node_module"* et le fichier *"package-lock.json"* et en tapant la commande `npm install`.

### sauvegarde et installation du projet

Le dossier *"node_module"* n'est pas un module à sauver, on peut installer toutes les dépendances avec la commande `npm install` :

* grâce au fichier *"package-lock.json"* : la commande `npm --install` sait exactement quels modules installer
* le fichier *"package.json"* donnant les dépendances générales de notre projet.

## routes

Le module [express](https://expressjs.com/) va nous permettre de créer nos routes (les urls que le serveur connait) simplement.

Avant d'utiliser le module, penchons nous un peut sur que l'on veut :

* site statique : on demande à l'utilisateur de taper son prénom
* une fois que l'on appuie sur le bouton, le prénom est envoyé au server qui retourne le chiffre associé.

Pour l'instant nous n'avons qu'un site front. Donc commençons par organiser le tout.

### séparation front et back

L'usage veut que le site front soit séparé des actions du serveur. Cela permet de ne pas se mélanger les fichiers.

1. créez un dossier *"numerologie/static"* et déplacez les fichiers :
   * *"index.html"*
   * *"mains.css"*
   * *"numerologie.js"*
2. supprimez le fichier *"mes_test.js"*, on ne s'en sert plus depis longtemps.

Le projet ressemble maintenant à ça, en excluant le dossier *"node_modules"* :

```text
.
├── index.js
├── package-lock.json
├── package.json
└── static
    ├── index.html
    ├── main.css
    └── numerologie.js
```

> On a utilisé la commande unix [tree](https://linux.die.net/man/1/tree) (`tree -I node_modules`) pour réaliser le dessin ci-dessus.

### notre site en express

Modifions le fichier *"numerologie/index.js"* pour que notre site fonctionne sous express :

```javascript
const path = require('path')

const express = require('express')
const app = express()

const hostname = '127.0.0.1';
const port = 3000;

app.use("/static", express.static(path.join(__dirname, '/static')))

app.get('/', (req, res) => {
    res.redirect(301, '/static/index.html')
})


app.use(function (req, res) {
    console.log("et c'est le 404 : " + req.url);

    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/html');

    res.end("<html><head><title>la quatre cent quatre</title></head><body><h1>Et c'est la 404.</h1><img  src=\"https://www.leblogauto.com/wp-content/uploads/2020/04/Peugeot-404-1.jpg\" /></body></html>");

})

app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);
```

Tout se passe *via* l'objet `app`, qui est le résultat de l'import de express. Chaque requête au serveur passera d'un appel de `app` à l'autre (dans l'ordre du fichier).

> Express appelle ces bouts de codes qui interceptent une requête un [middleware](https://expressjs.com/fr/guide/using-middleware.html)

Pour chaque appel de app (dans notre cas on en a 2 `app.use` et `app.get`) :

1. on vérifie si la requête satisfait l'appel de `app` :
   * `app.use()` : reçoit toutes les requêtes
   * `app.get()` : ne reçoit que les requêtes de méthode `get`
   * `app.post()` : ne reçoit que les requêtes de méthode `post`
2. Si la requête satisfait l'appel de `app`, on vérifie si elle satisfait le 1er paramètre
3. Si la requête satisfait le 1er paramètre on exécute la méthode du second paramètre avec la requête en 1er paramètre.

> Comme dit précédemment, la route `/static` ne doit être utilisée qu'en développement. En production, on doit avoir un serveur dédié aux fichiers statiques pour éviter tout problème de charge.

Dans notre cas l'enchaînement de route est ainsi :

1. 1er `app.use` : si l'url de la requête commence par `/static` on envoie cette requête dans le gestionnaire de fichiers statiques de express.
2. `app.get`  :  si l'url de la requête est `/` on redirige la requête vers `/static/index.html`. Cette requête redirigée sera alors consommée par le `app.use`
3. 2ème `app.use` : s on arrive là, c'est que toutes les routes précédentes ont échouées : on ne peut rien faire de la requêtes on indique au client que c'est un 404. On en a aussi profité pour rendre du contenu (toute une famille).

> Le dernier appel de `app` doit être pour gérer les requêtes qui n'ont pas pu être consommées avant. C'est souvent que l'on ne sait pas quoi en faire donc on l'indique au client part un 404.

Pour plus d'informations sur le routage express, n'hésitez pas à [consulter la documentation](https://expressjs.com/fr/guide/routing.html)

### fonction next()

On peut remettre des requêtes utilisées en fonction avec la méthode `next()`

Ajoutez par exemple ce code en début de fichier en faisant en sorte que ce soit le 1er appel à `app` :

```javascript
// ...

app.use(function (req, res, next) {
    date = new Date(Date.now())
    console.log('Time:', date.toLocaleDateString(), date.toLocaleTimeString(), "; url :", req.url);
    next(); // sans cette ligne on ne pourra pas poursuivre.
})

// ...
```

> Notez Le format de la fonction change, remarquez qu'il y a un troisième paramètre, `next`.
> Lorsque vous voulez utiliser `next` il faut que vous l'ajoutiez en paramètre de la fonction.
{.attention}

Toutes les requêtes satisfont cet appel, c'est un loggeur rudimentaire.

Si vous supprimez la ligne avec `next()` plus rien ne fonctionne. Toutes les requêtes sont consommées.

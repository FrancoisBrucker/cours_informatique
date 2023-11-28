---
layout: layout/post.njk
title: "Serveur web avec express"

authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

On utilise le module express pour gérer plus élégamment notre site.

<!-- fin résumé -->

Le module node [express](https://expressjs.com/) permet une gestion efficace et apaisée des site web.

Pour installer des packages node, on peut utiliser [npm](https://www.npmjs.com/) (**n**ode **p**ackage **m**anager) qui est livré avec node.

{% info "Tutoriel :" %}
Un [tutoriel pour utiliser npm](https://www.digitalocean.com/community/tutorials/how-to-use-node-js-modules-with-npm-and-package-json-fr)
{% endinfo %}

### `npm init`

Comme fait [précédemment](../minimal/){.interne} on prépare le projet en créant un fichier `package.json`{.fichier}.

{% faire %}

1. créez un dossier `serveur_express`{.fichier} où l'on stockera les fichiers de notre serveur.
2. dans cde dossier, initialisez le projet en tapant la commande : `npm init` puis en tapant entrée à chaque question pour utiliser les réponses par défaut.
3. ajouter la ligne `"type": "module",`{.language-} dans le fichier de configuration `package.json`{.fichier}, juste en-dessous de la ligne 5

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

Il ne contient pour l'instant que des informations générales quant au projet. Nous allons bientôt y ajouter des modules.

{% note %}
Le [json](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation) est un format texte pour sauvegarder des données structurée. C'est un format génial qui sert tout autant pour les fichiers de configurations que le transfert de données par le web.
{% endnote %}

### Ajout d'un module

Pour cela, tapez dans un terminal placé à la racine de notre projet :

```shell
npm add --save express
```

{% attention %}
N'oubliez pas `--save`, sinon le module sera installé mais la dépendance ne sera pas ajoutée au fichier *"package.json"* ce qui est tarte.
{% endattention %}

Cette commande a ajouté une dépendance à notre fichier *"package.json"* :

```json
"dependencies": {
    "express": "^4.17.1"
  }
```

A créer un fichier `package-lock.json`{.fichier} qui contient la liste de tous les modules installés et un (gros) dossier `node_modules`{.fichier} qui contient les modules installés.

{% info %}
Il y a plus de 50 modules installés alors que l'on a demandé d'installer que le module `express`, car il a lui même des dépendances et ses dépendances d'autres dépendances, etc.
{% endinfo %}

La différence entre `package.json`{.fichier} et `package-lock.json`{.fichier} est que le premier décrit les versions possibles (nous, toutes les versions ultérieures à 4.17.1) alors que `package-lock.json`{.fichier} décrit la version effectivement installée (la 4.17.1). Cette mécanique permet de mettre à jour nos modules en supprimant le dossier `node_modules`{.fichier} et le fichier `package-lock.json`{.fichier} et en tapant la commande `npm install`.

### Sauvegarde et installation du projet

Le dossier `node_modules`{.fichier} n'est pas un module à sauver, on peut installer toutes les dépendances avec la commande `npm install` :

* grâce au fichier `package-lock.json`{.fichier} : la commande `npm --install` sait exactement quels modules installer
* le fichier `package.json`{.fichier} donnant les dépendances générales de notre projet.

## Routes

Le module [express](https://expressjs.com/) va nous permettre de créer nos routes (les urls que le serveur connaît) simplement.

Avant d'utiliser le module, penchons nous un peut sur que l'on veut :

* site statique : on demande à l'utilisateur de taper son prénom
* une fois que l'on appuie sur le bouton, le prénom est envoyé au server qui retourne le chiffre associé.

Pour l'instant nous n'avons qu'un site front. Donc commençons par organiser le tout.

### Séparation front et back

L'usage veut que le site front soit séparé des actions du serveur. Cela permet de ne pas se mélanger les fichiers. On va donc créer un dossier `serveur_web/static`{.fichier} et déplacer les fichier `index.html`{.fichier} et `favicon.ico`{.fichier}

Le projet ressemble maintenant à ça, en excluant le dossier `node_modules`{.fichier} :

```
.
├── index.js
└── static
    └── index.html
```

{% info %}
On a utilisé la commande unix [tree](https://linux.die.net/man/1/tree) (`tree -I node_modules`) pour réaliser le dessin ci-dessus.
{% endinfo %}

### Notre site en express

Modifions le fichier `index.js`{.fichier} pour que notre site fonctionne sous express :

```javascript
import path from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

import express from 'express';
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

    res.end("<html><head><title>la quatre cent quatre</title></head><body><img  src=\"https://upload.wikimedia.org/wikipedia/commons/b/b4/Peugeot_404_Champs.jpg\" /></body></html>");

})

app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);

```

Tout se passe *via* l'objet `app`{.language-}, qui est le résultat de l'import de express. Chaque requête au serveur passera d'un appel de `app` à l'autre (dans l'ordre du fichier).

{% note %}
Express appelle ces bouts de codes qui interceptent une requête un [middleware](https://expressjs.com/fr/guide/using-middleware.html)
{% endnote %}

Pour chaque appel de app (dans notre cas on en a 2 `app.use`{.language-} et `app.get`{.language-}) :

1. on vérifie si la requête satisfait l'appel de `app`{.language-} :
   * `app.use()`{.language-} : reçoit toutes les requêtes
   * `app.get()`{.language-} : ne reçoit que les requêtes de méthode `get`{.language-}
   * `app.post()`{.language-} : ne reçoit que les requêtes de méthode `post`{.language-}
2. Si la requête satisfait l'appel de `app`{.language-}, on vérifie si elle satisfait le 1er paramètre
3. Si la requête satisfait le 1er paramètre on exécute la méthode du second paramètre avec la requête en 1er paramètre.

{% note %}
Comme dit précédemment, la route `/static` ne doit être utilisée qu'en développement. En production, on doit avoir un serveur dédié aux fichiers statiques pour éviter tout problème de charge.
{% endnote %}

Dans notre cas l'enchaînement de route est ainsi :

1. 1er `app.use`{.language-} : si l'url de la requête commence par `/static` on envoie cette requête dans le gestionnaire de fichiers statiques de express.
2. `app.get`{.language-}  :  si l'url de la requête est `/` on redirige la requête vers `/static/index.html`. Cette requête redirigée sera alors consommée par le `app.use`{.language-}
3. 2ème `app.use`{.language-} : s on arrive là, c'est que toutes les routes précédentes ont échouées : on ne peut rien faire de la requêtes on indique au client que c'est un 404. On en a aussi profité pour rendre du contenu (toute une famille).

{% note %}
Le dernier appel de `app`{.language-} doit être pour gérer les requêtes qui n'ont pas pu être consommées avant. C'est souvent que l'on ne sait pas quoi en faire donc on l'indique au client part un 404.
{% endnote %}

Pour plus d'informations sur le routage express, n'hésitez pas à [consulter la documentation](https://expressjs.com/fr/guide/routing.html)

### Fonction `next()`{.language-}

On peut remettre des requêtes utilisées en fonction avec la méthode `next()`{.language-}

Ajoutez par exemple ce code en début de fichier en faisant en sorte que ce soit le 1er appel à `app`{.language-} :

```javascript
// ...

app.use(function (req, res, next) {
    let date = new Date(Date.now())
    console.log('Time:', date.toLocaleDateString(), date.toLocaleTimeString(), "; url :", req.url);
    next(); // sans cette ligne on ne pourra pas poursuivre.
})

// ...
```

{% attention %}
Notez Le format de la fonction change, remarquez qu'il y a un troisième paramètre, `next`.
Lorsque vous voulez utiliser `next` il faut que vous l'ajoutiez en paramètre de la fonction.
{% endattention %}

Toutes les requêtes satisfont cet appel, c'est un loggeur rudimentaire.

Si vous supprimez la ligne avec `next()`{.language-} plus rien ne fonctionne. Toutes les requêtes sont consommées.

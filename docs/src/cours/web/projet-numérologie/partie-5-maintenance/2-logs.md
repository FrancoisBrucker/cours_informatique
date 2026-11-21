---
layout: layout/post.njk

title: "Projet numérologie : partie 5 / logs"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Nous allons ajouter un gestionnaire de logs dans le projet

<!-- fin résumé -->

> TBD intro + reste niveau de logs + code + tail -f
> log level : <https://wiki.archlinux.org/title/Systemd/Journal> <https://github.com/winstonjs/winston#logging>

Les logs constituent des messages rendant compte des activités du serveur. Ces messages sont stockées dans un fichier ou affiché dans la console.

Pour toute application faisant de nombreuses chose et devant tourner 24h sur 24 comme un serveur, il est crucial de monitorer toues les actions qu'elle effectue. Ceci permet :

1. de voir ce qu'il se passe en temps réel
2. savoir quand et pourquoi un crash est survenu (qui a — va savoir pourquoi — toujours lieu au milieu de la nuit)
3. comprendre et corriger l'erreur

Si l'application est grande et très utilisée, stocker toutes ses actions dans un fichier serait bien trop gourmand en place et surtout inefficace car les erreurs seraient noyées dans un flot d'actions réalisées sans encombre. Il est donc nécessaire d'ajouter un niveau de gravité de chaque action (couramment de 0 (urgence) à 7 (debug). Voir par exemple le [niveau de priorité de systemd](https://wiki.archlinux.org/title/Systemd/Journal#Priority_level) qui respecte la [RFC5424](https://www.rfc-editor.org/rfc/rfc5424)) et de ne stocker que les actions de niveau 4 ou inférieure (par exemple) en régime stable. Si bug il y a on peut le corriger en visualisant toutes les actions.

## Log front

La console le fait déjà :

{% lien %}
<https://dev.to/ackshaey/level-up-your-javascript-browser-logs-with-these-console-log-tips-55o2>
{% endlien %}

## Winston

{% lien %}
Logger [Winston](https://github.com/winstonjs/winston) pour nodejs
{% endlien %}

Nous allons utiliser [Winston](https://github.com/winstonjs/winston) pour faire les logs de notre serveur car il est très versatile.

Les [niveaux de log de Winston](https://github.com/winstonjs/winston) sont par défaut :

```js
const levels = { 
  error: 0,
  warn: 1,
  info: 2,
  http: 3,
  verbose: 4,
  debug: 5,
  silly: 6
};
```

En production on pourra par exemple utiliser le level 0, en développement le 2 et en debug le 5.

### Mise en place

Commençons par ajouter winston : `npm install --save winston`

Et créons un logger. Pour cela, on va créer un fichier `logger.js`{.fichier} et mettre notre configuration winston à l'intérieur. Ce fichier sera ensuite importé dans tous les fichiers nécessitant des logs. Comme l'import est unique, ce sera le **même** logger qui sera utilisé partout (c'est ce qu'on appelle le [caching](https://nodejs.org/docs/latest/api/modules.html#modules_caching)).

Fichier `logger.js`{.fichier} :

```js
import winston from 'winston';

export const logger = winston.createLogger({
  level: 'verbose',
  format: winston.format.combine(
      winston.format.timestamp(),
      winston.format.json()),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'http.log', level: 'http' }),
  ],
});
```

On a trois sorties :

* une dans la console pour (définie dans les options) tous les log de criticité inférieur à `'verbose'`
* dans un fichier `error.log`{.fichier} pour toutes les erreurs et inférieur.
* dans un fichier `http.log`{.fichier} pour tous les http et inférieur.

#### `index.js`{.fichier}

Modifions notre fichier `index.js`{.fichier} pour prendre en compte notre log :

```js
import { fileURLToPath } from 'url';
import path from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);


import express from 'express';
const app = express()

import {router as routes} from "./routes/index.js";

import { logger } from './logger.js';

const hostname = '127.0.0.1';
const port = 3000;

app.use(function (req, res, next) {
    logger.http(req.url)
    next(); // sans cette ligne on ne pourra pas poursuivre.
})

app.use("/static", express.static(path.join(__dirname, '/static')))

app.get('/', (req, res) => {
    res.redirect(301, '/static/index.html')
})

app.use('/', routes)

app.use(function (req, res) {
    logger.info("et c'est le 404 : " + req.url);

    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/html');

    res.end("<html><head><title>le quatre cent quatre</title></head><body><h1>Et c'est le 404.</h1></body></html>");

})

app.listen(port, hostname);
logger.info(`Start server at http://${hostname}:${port}/`)

```

#### Sequelize

On peut maintenant intégrer les logs de winston avec les sorties de sequelize en lui associant notre logger.

Fichier `db.js`{.fichier} :

```js

// ...

import { logger } from './logger.js';

// ...

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite'),
  logging: (msg) => logger.info(msg),
});
```

### Winston daily rotate

[winston daily rotate](https://github.com/winstonjs/winston-daily-rotate-file) est un plugin winston qui permet de faire des log qui ne maintiennent qu'une durée fixe de log (une journée, semaine, etc) permettant ainsi aux logs de ne pas grossir indéfiniment.

{% info %}
Il existe aussi des outils unix pour cela, comme [logrotate](https://doc.ubuntu-fr.org/logrotate) par exemple (voir [tuto](https://medium.com/techiee/log-rotation-with-forever-6d8a1797355b)).

{% endinfo %}

## Fichiers de logs

> TBD : écrire mieux

### fin d'un fichier

`tail -f http.log`

### clean

```json
...

"scripts": {

        ...

        "clean": "rm *.log"
    },

...
```

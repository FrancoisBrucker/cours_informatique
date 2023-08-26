---
layout: layout/post.njk

title: "Projet numérologie : partie 5 / mise à jour des packages"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Mettre à jour les packages.

<!-- fin résumé -->

> TBD : faire une install de quelque chose de pas à jour et mettre à jour

## Gestion des packages

1. `package.json`{.fichier} : pour déterminer des règles
2. `package-lock.json`{.fichier} : pour montrer ce qui est effectivement installé
3. les mise à jour des bibliothèques par les développeurs

## Mise à jour

En reprenant le code de la [partie 4](../../partie-4-jardinage/4-structures){.interne}, on voit que certains packages ont été mis à jour.

`package.json`{.fichier} :

```json
{
    "name": "numérologie",
    "version": "1.0.0",
    "description": "de la numérologie",
    "main": "index.js",
    "type": "module",
    "scripts": {
        "init": "node db.init.js",
        "test": "echo \"Error: no test specified\" && exit 1",
        "start": "node index.js"
    },
    "author": "François Brucker",
    "license": "WTFPL",
    "dependencies": {
        "express": "^4.17.1",
        "sequelize": "^6.25.6",
        "sqlite3": "^5.1.2"
    }
}

```

Voir les [packages mis à jour](https://docs.npmjs.com/cli/v8/commands/npm-outdated) avec :

```
» npm outdated                     
Package    Current  Wanted  Latest  Location                Depended by
sequelize   6.25.6  6.29.3  6.29.3  node_modules/sequelize  numérologie
sqlite3      5.1.2   5.1.6   5.1.6  node_modules/sqlite3    numérologie
```

On voit de plus que la version installée de `sequelize` était plus la minimum demandée. Voir `package-lock.json`{.fichier} pour avoir les version effectivement installées de tous les packages.

[Mise à jour](https://docs.npmjs.com/cli/v8/commands/npm-update) des packages installées (`package-lock.json`{.fichier}) :

```
npm update
```

Cela change les version installées, mais ne met pas à jour le fichier `package.json`{.fichier}. Pour le faire :

```
npm install [nom package]@latest --save
```

{% lien %}
Voir :

<https://stackoverflow.com/questions/16073603/how-to-update-each-dependency-in-package-json-to-the-latest-version/23391365#23391365>

Attention, la question est vielle, donc les premières réponses ne sont plus exactes.

{% endlien %}

On peut aussi changer le `package.json`{.fichier} pour qu'il ait toujours la dernière version d'installée (mais attention aux incompatibilités de versions) :

Dans le fichier `package.json`{.fichier} (voir [doc](https://docs.npmjs.com/cli/v8/configuring-npm/package-json) ):

```json
... 

"dependencies": {
        ...

        "express": "latest",

        ...
    }

...
```

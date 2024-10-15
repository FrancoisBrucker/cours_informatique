---
layout: layout/post.njk

title: "Projet numérologie : partie 4 / modèles"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Rationalisation des différents modèles de données.

<!-- fin résumé -->

Le principe qui nous a fait séparer nos routes nous fait également séparer les modèles.

## Injection de dépendances

La différence par rapport aux routes est que l'on a besoin de la base de donnée (`sequelize`) pour définir le modèle. La solution élégante à ce problème est d'utiliser [l'injection de dépendance](https://fr.wikipedia.org/wiki/Injection_de_d%C3%A9pendances) : **on va donner notre base de donnée à l'import du modèle**.

Ceci peut se faire simplement en javascript en important une fonction et non plus des objets.

Avant de montrer le code des modèles, créons un dossier `numérologie/modèles/`{.fichier} qui va contenir nos modèles.

### Modèle `Signification`{.language-}

Le modèle `Signification`{.language-} est alors crée dans le fichier `numérologie/models/signification.js`{.fichier} :

```js
import { DataTypes } from 'sequelize';

export default (sequelize) => {

    return sequelize.define('Signification', {
        message: {
            type: DataTypes.STRING,
            allowNull: false
        },
        nombre: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
    }, {
        // Other model options go here
    });

}

```

Remarquez que l'objet exporté n'est plus un dictionnaire comme précédemment, mais une fonction. Lors de l'import dans le fichier `db.js`{.fichier} (on le fera juste après) on passera en paramètre l'objet `sequelize`{.fichier} qui contient notre lien à la base de donnée.

Ceci nous permet d'avoir plusieurs fichiers de modèles avec un unique objet `sequelize`{.fichier} : on injecte les dépendances dans l'initialisation des objets.

### Modèle `Prénoms`{.language-}

De la même manière, on crée le modèle `Prénoms`{.language-} dans le fichier `numérologie/models/prénoms.js`{.fichier} :

```js
import { DataTypes } from 'sequelize';

export default (sequelize) => {

    return sequelize.define('Prénoms', {
        prénom: {
            type: DataTypes.STRING,
            allowNull: false
        },
    }, {
        // Other model options go here
    });

}

```

## Base de donnée

Les modèles crées vont être importé puis exécutés dans notre fichier `numérologie/db.js`{.fichier} remanié :

```js
import { Sequelize, DataTypes } from 'sequelize';

import { fileURLToPath } from 'url';
import path from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});

import signification from "./modèles/signification.js"
import prénoms from "./modèles/prénoms.js"

export default {
    sequelize: sequelize,
    model: {
        Signification: signification(sequelize),
        Prénoms: prénoms(sequelize),
    }
}

```

Voyez comment le modèle est tout d'abord chargé (`import signification from "./modèles/signification.js"`{.language-}) puis exécuté à l'export (`Signification: signification(sequelize)`{.language-}) en utilisant la base de donnée en injection de dépendance.

{% note %}
L'injection de dépendance est une solution simple et élégante pour dispatcher un objet unique à plusieurs entités.
{% endnote %}

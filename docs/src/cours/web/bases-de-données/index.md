---
layout: layout/post.njk

title: "Utilisation de bases de données"

eleventyNavigation:
  key: "Utilisation de bases de données"
  parent: "Web"
---

<!-- début résumé -->

Utiliser une base de données avec express et node.

<!-- fin résumé -->

On peut très bien uniquement stocker ses données sous la forme de variables, de liste ou encore de dictionnaires pendant l'exécution du serveur. Mais lorsque le serveur va s'arrêter on perdra toutes ses données... Pour conserver ses données il faut les stocker dans une base (il en existe de différents types selon l'usage) facilement accessible (en utilisant des requêtes facile à créer et à maintenir).

Nous allons montrer ici un cas d'utilisation simple que vous pourrez adapter à vos besoins futur :

* utilisation d'une base de donnée relationnelle [SQLite](https://www.sqlite.org).
* utilisation de sequelize pour la gestion de celle-ci

Nous aurons besoin d'un projet pour tester ce que nous allons voir donc :

{% faire %}

Créez un dossier `bd-tests`{.fichier}, puis initialisez-le :

```
npm init
```

{% endfaire %}

## SQLite

Tout ce que nous allons faire avec la base de donnée SQLite est transposable en utilisant un autre type de base de donnée utilisant un serveur dédié. SQlite sauve ses données soit en mémoire soit sur un fichier, ce qui permet d'utiliser des bases de données sans avoir à configurer un serveur dédié : c'est donc bien quand on apprend ou que l'on fait de petits sites, mais c'est souvent insuffisant pour des sites professionnels.

### Installation de SQlite

Le module node `sqlite3` nous permet d'utiliser SQlite dans nos serveurs node. Installons-le :

{% faire %}

Dans le dossier `bd-tests`{.fichier} et avec un terminal :

```
npm install --save sqlite3
```

{% endfaire %}
{% info %}
Il existe également Le module node [better-sqlite3](https://www.npmjs.com/package/better-sqlite3) est une version amélioré — selon ses auteurs — du module classique [sqlite3](https://www.npmjs.com/package/sqlite3), mais il ne fonctionne pas — à l'heure où je tape ces caractères — avec sequelize que nous utiliserons ensuite.
{% endinfo %}

Il est parfois aussi utile d'avoir une [cli(https://fr.wikipedia.org/wiki/CLI)] pour vérifier ou installer des données. Installons également le package  :

{% faire %}

```
npm install --save-dev cli-sqlite
```

{% endfaire %}
{% info %}
Nous avons utilisé l'option `--save-dev` pour indiquer qeu ce module ne sera utilisé que pour le développement. On en aura pas besoin en production.

Vous pouvez voir la différence de traitement ce ces modules dans le fichier `package.json`{.fichier}
{% endinfo %}

Le module ci-dessus installe le programme `sqlite` exécutable dans un terminal. Classiquement ces programmes sont placés dans le dossier `node_modles/.bin`{.fichier}. `npm`  fourni le programme [`npx`](https://www.npmjs.com/package/npx) pour exécuter ces programmes sans se soucier du chemin. Pour installer SQLite il nous suffit, une fois dans le dossier du projet, de taper :

```
npx sqlite
```

### Usage

On tape directement les commandes SQL dans une fonction js. Avec des promesses.

#### fichier en cli

{% chemin %}
<https://www.sqlite.org/cli.html>
{% endchemin %}

```
npx sqlite
```

> TBD : tuto sqlite

#### fichier sous node

<https://www.linode.com/docs/guides/getting-started-with-nodejs-sqlite/>

> TBD

#### mémoire sous node

<https://www.sqlite.org/inmemorydb.html>

> TBD

#### gérer ses configurations

> TBD parler des fichiers de configuration différents qui rendent la base de données :
> puis fichier si prod
> mémoire si tests

## ORM : sequelize

Nous n'allons pas utiliser sqlite en tapant juste des commandes sql pour plusieurs raisons :

* la vie est trop courte pour faire du SQL : qui est compliqué à utiliser (sa syntaxe et son fonctionnement n'ont pas changé depuis les années 1970...)
* impossible à débuguer ou a modifier
* plein de dialectes différents. Une fois qu'on a une pase très difficile d'en changer à cause des différents dialectes SQL possibles

On utilise un [ORM](https://fr.wikipedia.org/wiki/Mapping_objet-relationnel) (*Object-Relational Mapping*) qiu permet

* permet d'écrire des bases et d'utiliser des requêtes comme on fait des objets
* pattern facade : indépendant de la base. On peut changer la base de donnée sans changer le code (juste la config)
* très facilement débuguable et modifiable car lisible

### Installation

{% faire %}

```
npm install --save sequelize
```

{% endfaire %}

### Lien à la base de données

Lien avec une base de données SQlite en mémoire :

```js#
const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('sqlite::memory:');
```

Ou avec un fichier (le fichier sera crée s'il n'existe pas encore) :

```js#
path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});
```

A la ligne 3, on crée la variable `sequelize`{.language-} qui sera notre intermédiaire à la base de donnée.

### Modèles

L'intérêt des ORM est que l'on va décrire la base de donnée et interagir avec elle via des *modèles*. Chaque modèle est constitué de champs qui vont décrire nos données. Dans un formalisme objet :

* le modèle est la classe et les attributs correspondent aux colonne de la table SQL
* l'objet est une donnée et il correspond à  une ligne de la table SQL

Les types possible de champs sont disponible [dans la documentation](https://sequelize.org/v5/manual/data-types.html).

On va par exemple créer un modèle constitué d'une chaîne de caractère (`STRING` : chaîne de caractère d'au plus 255 caractères) et d'un entier (`INTEGER`) :

```js
const MonModèle = sequelize.define('MonModèle', {
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
```

Une fois le modèle donné, il faut [synchroniser la base de donnée](https://sequelize.org/master/manual/model-basics.html#model-synchronization) avec celui-ci (si par exemple la base était créer avec un vieux modèle, il faut même changer la base pour qu'elle corresponde à notre nouveau modèle). Ceci se fait avec la promesse `sync` :

```js
sequelize.sync()
    .then(() => {
        console.log("synchronisation terminée.")
    })
```

{% attention %}
Il est important d'attendre la fin de la synchronisation avant de lire ou sauver des données
{% endattention %}

Normalement, la synchronisation des bases ne se fait pas en production. On a un script de création des modèles et de synchronisation que l'on n'exécute que lorsque le modèle change.

Comme ici on a une base de donnée en mémoire, elle est crée à chaque lancement du serveur, ce qui nous oblige à synchroniser à chaque démarrage (il faut ajouter les tables à la base fraîchement créée).

### Champs spéciaux

#### Clé primaire

Si l'on ne crée pas de clé primaire avec notre modèle, sequelize va créer un champ spécial nommé `id` qui s'incrémente tout seul et est la clé primaire de notre table.

Par défaut, utilisez toujours ce champ comme clé primaire.

#### Temps

{% chemin %}
<https://sequelize.org/master/manual/model-basics.html#timestamps>
{% endchemin %}

Par défaut, sequelize ajoute deux champs spéciaux `createdAt`{.language-} and `updatedAt`{.language-} pour connaître la date de création et de la dernière mise à jour d'une donnée.

Le type de ces champ et `DataTypes.DATE`{.language-}. A chaque fois que vous devez utiliser des dates ou des heures, il est **indispensable** d'utiliser des types dédiées. Il est criminel d'utiliser une chaîne de caractère pour stocker des dates ou des heures : il y a trop de cas particuliers selon les pays et ou d'exception (année bissextile, etc).

### Lire et sauver des données

{% chemin %}
<https://sequelize.org/master/manual/model-querying-basics.html>
{% endchemin %}

## Exemple

```js
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize('sqlite::memory:');

const MonModèle = sequelize.define('MonModèle', {
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

async function initDB() {
    await sequelize.sync()
    var data = await MonModèle.create({
        message: "mon premier message",
        nombre: 7,
    })
    console.log("message crée : ")
    console.log(data.toJSON())

    data = await MonModèle.create({
        message: "un autre massage",
        nombre: 3,
    })
    console.log("message crée : ")
    console.log(data.toJSON())
    
}

initDB().then(async () => {
    
    console.log("Lecture id = 1 :")
    data = await MonModèle.findByPk(1); 
    console.log(data.toJSON())

    console.log("---------")
    console.log("clé primaire : ", data.id)
    console.log("message : ", data.message)
    console.log("nombre : ", data.nombre)
    console.log("date de création création : ", data.createdAt)
    console.log("dernière modification : ", data.updatedAt)
    console.log("---------")

    console.log("Lecture id qui n'existe pas :")
    data = await MonModèle.findByPk(42);
    console.log(data) // n'existe pas

    console.log("Lecture tous les éléments :")
    data = await MonModèle.findAll(); 
    for (element of data) {
        console.log(element.toJSON())
    }
    
    console.log("Lecture requête :")
    data = await MonModèle.findAll({
        where: {
            nombre: 3
        }
    }); 
    for (element of data) {
        console.log(element.toJSON())
    }
})

console.log("coucou")
```

{% faire %}
Créer un fichier `ma_db_test.js`{.fichier} qui contient le code précédent et exécutez le avec la commande :

```
node ma_db_test.js
```

{% endfaire %}

Le code vu dans la console qui ressemble à du SQL est bien du SQL. Ce sont les commandes faites par sequelize.

On crée une fonction asynchrone `initDB`{.language-} dont le but est de se synchroniser puis de créer des données dans la base. A l'intérieur d'une fonction asynchrone on exécute du code avec `await`{.language-}, comme ça on est sur qu'on ne passera à la ligne suivant qu'une fois la ligne avec le `await`{.language-} exécutée (on est sur que l'on crée des données une fois la base synchronisée)

On utilise ensuite cette fonction de façon asynchrone, avec un `then`{.language-}. On voit que c'est exécuté de façon asynchrone puisque lorsque l'on exécute le code, la chaîne `"coucou"`{.language-} est écrite tout en haut de l'exécution, bien avant les requêtes en base de sequelize.

Les données sont affichées à l'écran sous la forme d'un json. Mais vous avez accès aux différents champs (entre les deux `console.log("---------")`{.language-}) :

## CRUD

Accéder aux données se fait, on l'a vue, en utilisant le formalisme [CRUD](https://fr.wikipedia.org/wiki/CRUD), c'est à dire que l'on veut avoir des url qui nous permettent de :

* **C**reate : créer un message
* **R**ead : lire un message
* **U**pdate : mettre à jour un message
* **D**elete : supprimer un message

Nous allons accéder à la base uniquement en utilisant ces méthodes.

{% note %}
Nous utiliserons l'id qui est ajouté par défaut à chaque message pour spécifier directement  un message.
{% endnote %}

### Create

{% chemin %}
<https://sequelize.org/master/manual/model-instances.html#creating-an-instance>
{% endchemin %}

Créer une donnée en sequelize peu se faire comme ça :

```js
MonModèle.create({
        message: "un autre massage",
        nombre: 3,
    })
    .then((data) => {
        console.log(data.toJSON())
    })
```

Le message est poussé en base. La clé primaire est le champ `id`.  Si c'est le premier élément que vous créez, son `id` sera de 1, et si vous en créez d'autres, l'`id` va augmenter. C'est la clé primaire de notre modèle.

### Read

{% chemin %}
<https://sequelize.org/master/manual/model-querying-finders.html#-code-findbypk--code->
{% endchemin %}

Lire une instance en connaissant sa clé primaire :

```js
MonModèle.findByPk(1)
    .then((data) => {
        console.log(data.toJSON())
    })
```

Si l'on donne une clé primaire inexistante, on récupère l'objet `null`.

### Update

{% chemin %}
<https://sequelize.org/master/manual/model-instances.html#updating-an-instance>
{% endchemin %}

Mettre à jour un objet en connaissant sa clé primaire et les attributs à changer :

```js
MonModèle.findByPk(1)
    .then(async (data) => {
        data.nombre = 9
        await data.save()
    })
```

Remarquez que l'on a créée une fonction de type `async` pour assurer que la donnée sera sauvée avant de terminer la fonction du `then`.

### Delete

{% chemin %}
<https://sequelize.org/master/manual/model-instances.html#deleting-an-instance>
{% endchemin %}

```js
MonModèle.findByPk(1)
    .then(async (data) => {
        await data.destroy()
    })
```

Remarquez que l'on a créée une fonction de type `async` pour assurer que la donnée sera détruite avant de terminer la fonction du `then`.

## Configurations

Dans un serveur utilisant une base de données on a coutume d'avoir plusieurs fichiers pour gérer la base de donnée

1. un fichier de configuration qui sera utilisé pour définir la base à utiliser (en mémoire, un fichier, etc)
2. un fichier d'initialisation que l'on exécute pour créer la base et lorsque les champs de la base (le modèle) est modifié
3. les différentes parties où est utilisé la base.

### Configuration de la base

{% faire %}
Créez le fichier `db.js`{.language-} et copiez_collez-y le code suivant.
{% endfaire %}

```js
const { Sequelize, DataTypes } = require('sequelize');
path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});

const MonModèle = sequelize.define('MonModèle', {
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

module.exports = {
    sequelize: sequelize,
    model: {
        MonModèle: MonModèle,
    }
}
```

Ce fichier contient tout ce qui est nécessaire à l'utilisation de la base de donnée. Il exporte l'orm `sequelize`{.language-} et le `model`{.language-}

En javascript lorsque l'on lit un module (avec `require`{.language-}) ce module n'est lu qu'une seule fois. Toutes les autres fois il ne fera que rendre l'objet `module.exports`{.language-}.

Ceci permet de ne faire l’initialisation de la base qu'une seule fois et d'être assuré de rendre toujours **le même objet**
 `module.exports`.

{% info %}
Dans la vraie vie, on a plusieurs fichier d'initialisation selon l'environnement du serveur :

* en production : avec la vraie base, souvent derrière un serveur de base de donnée
* en développement : pour les petit tests lorsque l'on développe : avec une base en sqlite sous la forme d'un fichier
* en test : pour les tests unitaires de routes. Souvent une base en mémoire.
{% endinfo %}

### Initialisation de la base

{% faire %}
Créez le fichier `init.db.js`{.language-} et copiez_collez-y le code suivant.
{% endfaire %}

```js
const db = require("./db")

async function initDB() {
    await db.sequelize.sync({force: true})
    
    var data = await db.model.MonModèle.create({
        message: "mon premier message",
        nombre: 7,
    })

    data = await db.model.MonModèle.create({
        message: "un autre massage",
        nombre: 3,
    })

}

initDB()
    .then(() => {
        console.log("base initialisée")
    })
```

Ce code synchronise la base si nécessaire. Il utilise la base rendue par le require du fichier `db.js`{.fichier}. Il ne faut le faire que lorsque la base est nouvellement créée. On l'exécute par la commande :

```
node init.db.js 
```

### Utilisation de la base

{% faire %}
Créez le fichier `app.js`{.language-} et copiez_collez-y le code suivant.
{% endfaire %}

```js
const db = require("./db")

async function utilisation() {
    console.log("Lecture id = 1 :")
    data = await db.model.MonModèle.findByPk(1);
    console.log(data.toJSON())

    console.log("---------")
    console.log("clé primaire : ", data.id)
    console.log("message : ", data.message)
    console.log("nombre : ", data.nombre)
    console.log("date de création création : ", data.createdAt)
    console.log("dernière modification : ", data.updatedAt)
    console.log("---------")

    console.log("Lecture id qui n'existe pas :")
    data = await db.model.MonModèle.findByPk(42);
    console.log(data) // n'existe pas

    console.log("Lecture tous les éléments :")
    data = await db.model.MonModèle.findAll();
    for (element of data) {
        console.log(element.toJSON())
    }

    console.log("Lecture requête :")
    data = await db.model.MonModèle.findAll({
        where: {
            nombre: 3
        }
    });
    for (element of data) {
        console.log(element.toJSON())
    }
}

utilisation()
```

On est obligé de charger le modèle via le `require`{.language-}, mais on est pas obligé de faire la synchronisation si le fichier de base existe déjà.

On peut exécuter la modification et la visualisation du code avec :

```shell
node app.js
```

Notez qu'on a utilisé une fonction asynchrone car on veut pourvoir exécuter nos trois requêtes à la suite (d'où les `await).

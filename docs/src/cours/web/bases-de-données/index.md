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

* utilisation d'une base de donnée relationnelle [sqlite](https://www.sqlite.org).
* utilisation de sequelize pour la gestion de celle-ci

## Sqlite

Tout ce que nous allons faire avec la base de donnée sqlite est transposable en utilisant un autre type de base de donnée utilisant un serveur dédié. Sqlite sauve ses données soit en mémoire soit sur un fichier, ce qui permet d'utiliser des bases de données sans avoir à configurer un serveur dédié : c'est donc bien quand on apprend ou que l'on fait de petits sites, mais c'est souvent insuffisant pour des sites professionnels.

### Installation de sqlite

{% faire %}
On commence par créer un dossier `bd-tests`{.fichier} où l'on va placer notre code, puis on l'initialise :

```
npm init
```
{% endfaire %}

Une fois que l'on a répondu à toutes les questions, on peut installer sqlite3 :

{% faire %}

```
npm install --save sqlite3
```

{% endfaire %}
{% info %}
Il existe également Le module node [better-sqlite3](https://www.npmjs.com/package/better-sqlite3) est une version amélioré — selon ses auteurs — du module classique [sqlite3](https://www.npmjs.com/package/sqlite3), mais il ne fonctionne pas — à l'heure où je tape ces caractères — avec sequelize que nous utiliserons ensuite.
{% endinfo %}

Le module node `better-sqlite3` nous permettra d'utiliser sqlite dans nos serveurs node. Mais il est parfois aussi utile d'avoir une [cli(https://fr.wikipedia.org/wiki/CLI)] pour vérifier ou installer des données. Faisons le :

```
npm install --save cli-sqlite
```

Le module ci-dessus installe le programme `sqlite` exécutable dans un terminal. Classiquement ces programmes sont placés dans le dossier `node_modles/.bin`{.fichier}. `npm`  fourni le programme [`npx`](https://www.npmjs.com/package/npx) pour exécuter ces programmes soans se soucier du chemin. Pour installer sqlite il nous suffit, une fois dans le dossier du projet, de taper :

```
npx sqlite
```

### Usage

> TBD : tuto sqlite :
> 1. sur un fichier en cli 
> 2. en mémoire sous node
> 3. en fichier sous node
> 4. parler des fichiers de configuration différents.

## ORM : sequelize

ORM = sauve la vie.

Utilise un dialecte de SQL.

## asynchrone et promise

La plupart des requêtes en base de données sont asynchrones. C'est à dire que l'on va demander quelque chose à la base de données puis continuer notre code. Une fois que la base de donnée aura répondu, on exécutera une fonction. C'est une *promise* (voir [la doc de node](https://nodejs.dev/learn/understanding-javascript-promises)) et on en a déjà vu une [dans la partie 2]({% link cours/web/projets/numerologie/partie-2-serveur/4-javascript-serveur.md %}#intégration-au-html).

Il peut cependant parfois être utile d'écrire du code, *à l'ancienne*, c'est à dire un exécutant ligne çà ligne notre code. Pour cela, on utilise alors le mots clés `await` qui doit être utilisé  dans une fonction déclarée en `async`. Lisez [la documentation](https://nodejs.dev/learn/modern-asynchronous-javascript-with-async-and-await) pour comprendre la syntaxe.

> On va utiliser cette méthode lorsque l'on créera et synchronisera nos bases de données.

## Base de données

Nous allons voir ici comment créer une base de donnée et l'utiliser avec [sequelize](https://sequelize.org/) qui va nous permettre de gérer tout le côté configuration et utilisation de SQL pour nous.

En effet, selon la base, le dialecte SQL sera différent. Si l'on écrit nos requêtes à la main, il faudra toutes les changer lorsque l'on change de base, ce qui n'est pas humainement possible. On va donc écrire nos requête dans le formalisme de sequelize qui va le traduire pour chaque base utilisée.

### sequelize

Dans le dossier *"numerologie/"* tapez :

```shell
npm install --save sequelize
```

Notre base de donnée étant sqlite3, on installe également le driver :

```shell
npm install --save sqlite3
```

Pour initialiser notre base de données il faut dire à `sequelize` quelle base on utilise.
Nous allons ici utiliser une base de donnée en mémoire. Elle sera remise à zéro à chaque fois que l'on relancera le serveur :

```js
const { Sequelize } = require('sequelize');
const sequelize = new Sequelize('sqlite::memory:');
```

> La première ligne trouve sequelize dans le module et la seconde crée le lien avec la base de donnée.

### model

On va interagir avec notre base via des modèles. Chaque modèle est constitué de champs qui vont décrire nos données : c'est une table où chaque donnée est une ligne et où les colonnes ont des types prédéfinis.

Les types possible de champ sont disponible [dans la documentation](https://sequelize.org/v5/manual/data-types.html).

On va par exemple créer un modèle constitué d'une chaine de caractère (`STRING` : chaine de caractère d'au plus 255 caractères) et d'un entier (`INTEGER`) :

```js
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize('sqlite::memory:');

const MonModele = sequelize.define('MonModele', {
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

Une fois le modèle donné, il faut [synchroniser la base de donnée](https://sequelize.org/master/manual/model-basics.html#model-synchronization) avec celui-ci (si par exemple la base était créer avec un vieux modèle, il faut même changer la base pour qu'elle corresponde à notre nouveau modèle). Ceci se fait avec la fonction **asynchrone** `sync` :

```js
sequelize.sync()
    .then(() => {
        console.log("synchronisation terminée.")
    })
```

> Il est important d'attendre la fin de la synchronisation avant de lire ou sauver des données
{.attention}

Normalement, la synchronisation des bases ne se fait pas en production. On a un script de création des modèles et de synchronisation que l'on exécute que lorsque le modèle change.

Comme ici on a une base de donnée en mémoire, elle est crée à chaque lancement du serveur, ce qui nous oblige à synchroniser à chaque démarrage (il faut ajouter les tables à la base fraîchement créée).

### champs spéciaux

#### clé primaire

Si l'on ne crée pas de clé primaire avec notre modèle, sequelize va créer un champ spécial nommé `id` qui s'incrémente tout seul et est la clé primaire de notre table.

Par défaut, utilisez toujours ce champ comme clé primaire.

#### temps

<https://sequelize.org/master/manual/model-basics.html#timestamps>

Par défaut, sequelize ajoute deux champs spéciaux `createdAt` and `updatedAt` pour connaitre la date de création et de la dernière mise à jour d'une donnée.

Le type de ces champ et `DataTypes.DATE`. A chaque fois que vous devez utiliser des dates ou des heures, il est **indispensable** d'utiliser des types dédiées. Il est criminel d'utiliser une chaine de caractère pour stocker des dates ou des heures : il y a trop de cas particuliers selon les pays et ou d'exception(année bissextile, etc).

### lire et sauver des données

<https://sequelize.org/master/manual/model-querying-basics.html>

### exemple

créer un fichier *"ma_db_test.js"* :

```js
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize('sqlite::memory:');

const MonModele = sequelize.define('MonModele', {
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
    var data = await MonModele.create({
        message: "mon premier message",
        nombre: 7,
    })
    console.log("message crée : ")
    console.log(data.toJSON())

    data = await MonModele.create({
        message: "un autre massage",
        nombre: 3,
    })
    console.log("message crée : ")
    console.log(data.toJSON())
    
}

initDB().then(async () => {
    
    console.log("Lecture id = 1 :")
    data = await MonModele.findByPk(1); 
    console.log(data.toJSON())

    console.log("---------")
    console.log("clé primaire : ", data.id)
    console.log("message : ", data.message)
    console.log("nombre : ", data.nombre)
    console.log("date de création création : ", data.createdAt)
    console.log("dernière modification : ", data.updatedAt)
    console.log("---------")

    console.log("Lecture id qui n'existe pas :")
    data = await MonModele.findByPk(42);
    console.log(data) // n'existe pas

    console.log("Lecture tous les éléments :")
    data = await MonModele.findAll(); 
    for (element of data) {
        console.log(element.toJSON())
    }
    
    console.log("Lecture requête :")
    data = await MonModele.findAll({
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

Exécutez le code avec la commande :

```shell
node ma_db_test.js
```

> Le code vu dans la console qui ressemble à du SQL est bien du SQL. Ce sont les commandes faites par sequelize.

On crée une fonction asynchrone `initDB` dont le but est de se synchroniser puis de créer des données dans la base. A l'intérieur d'une fonction asynchrone on exécute du code avec `await`, comme ça on est sur qu'on ne passera à la ligne suivant qu'une fois la ligne avec le `await` exécutée (on est sur que l'on crée des données une fois la base synchronisée)

On utilise ensuite cette fonction de façon asynchrone, avec un `then`. On voit que c'est exécuté de façon asynchrone puisque lorsque l'on exécute le code, la chaine `"coucou"` est écrite tout en haut de l'exécution, bien avant les requêtes en base de sequelize.

Les données sont affichées à l'écran sous la forme d'un json. Mais vous avez accès aux différents champs (entre les deux `console.log("---------")`) :

## crud

Pour l'accès à nos données, on utilise le formalisme [CRUD](https://fr.wikipedia.org/wiki/CRUD), c'est à dire que l'on veut avoir des url qui nous permettent de :

* **C**reate : créer un message
* **R**ead : lire un message
* **U**pdate : mettre à jour un message
* **D**elete : supprimer un message

Nous utiliserons l'id qui est ajouté par défaut à chaque message pour spécifier directement  un message.

On utilisera les version asynchrone (sans `await` des différentes méthodeq)

### create

> <https://sequelize.org/master/manual/model-instances.html#creating-an-instance>

On veut créer une donnée avec sequelize en ayant le pseudo, le titre et le corps du message. On peut faire comme ça :

```js
MonModele.create({
        message: "un autre massage",
        nombre: 3,
    })
    .then((data) => {
        console.log(data.toJSON())
    })
```

Le message est poussé en base. La clé primaire est le champ `id`.  Si c'est le premier élément que vous créez, son `id` sera de 1, et si vous en créez d'autres, l'`id` va augmenter. C'est la clé primaire de notre modèle.

### read

> <https://sequelize.org/master/manual/model-querying-finders.html#-code-findbypk--code->

On va lire une instance en connaissant sa clé primaire.

```js
MonModele.findByPk(1)
    .then((data) => {
        console.log(data.toJSON())
    })
```

Si l'on donne une clé primaire inexistante, on récupère l'objet `null`.

### update

> <https://sequelize.org/master/manual/model-instances.html#updating-an-instance>

On met à jour un objet en connaissant sa clé primaire et les attributs à changer.

```js
MonModele.findByPk(1)
    .then(async (data) => {
        data.nombre = 9
        await data.save()
    })
```

Remarquez que l'on a créée une fonction de type `async` pour assurer que la donnée sera sauvée avant de terminer la fonction du `then`.

### delete

> <https://sequelize.org/master/manual/model-instances.html#deleting-an-instance>

```js
MonModele.findByPk(1)
    .then(async (data) => {
        await data.destroy()
    })
```

Remarquez que l'on a créée une fonction de type `async` pour assurer que la donnée sera détruite avant de terminer la fonction du `then`.

## fichier sqlite

Nous avons pour l'instant juste utilisé une base de donnée en mémoire, qui sera réinitialisée à chaque fois. Lorsque l'on utilise une base de donnée en dur (fichier ou serveur), on dissocie l'initalisation de la base de son utilisation.

Si l'on reprend l'exemple précédent et que l'on utilise une base de donnée sqlite, on pourra connecter la base ainsi :

```js
path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});
```

Qui utilisera (ou la créera si elle n'existe pas) un fichier *"db.sqlite"* comme base de donnée.

Le fichier *"ma_db_test.js"* est ensuite découpé en 2 :

* *"ma_db_init.js"* qui créera la base et placera les première données
* *"ma_db_utilisation.js"* qui utilisera la base initialisée.

### ma_db_init.js

```js
const { Sequelize, DataTypes } = require('sequelize');
path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});

const MonModele = sequelize.define('MonModele', {
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
    await sequelize.sync({force: true})
    
    var data = await MonModele.create({
        message: "mon premier message",
        nombre: 7,
    })

    data = await MonModele.create({
        message: "un autre massage",
        nombre: 3,
    })

}

initDB()
    .then(() => {
        console.log("base initalisée")
    })

```

On utilise `await sequelize.sync({force: true})` comme synchronisation qui, au contrainre de `await sequelize.sync()`, commence par supprimer la base avant de la récréer.

Exécutez le code avec la commande :

```shell
node ma_db_init.js
```

Une fois le code exécuté, vous devriez voir un fichier nommé *"db.sqlite"* dans le dossier de votre projet. Il contient les 2 entrées créees.

### ma_db_utilisation.js

```js
const { Sequelize, DataTypes } = require('sequelize');
path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});

const MonModele = sequelize.define('MonModele', {
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

async function utilisation() {
    console.log("Lecture id = 1 :")
    data = await MonModele.findByPk(1);
    console.log(data.toJSON())

    console.log("---------")
    console.log("clé primaire : ", data.id)
    console.log("message : ", data.message)
    console.log("nombre : ", data.nombre)
    console.log("date de création création : ", data.createdAt)
    console.log("dernière modification : ", data.updatedAt)
    console.log("---------")

    console.log("Lecture id qui n'existe pas :")
    data = await MonModele.findByPk(42);
    console.log(data) // n'existe pas

    console.log("Lecture tous les éléments :")
    data = await MonModele.findAll();
    for (element of data) {
        console.log(element.toJSON())
    }

    console.log("Lecture requête :")
    data = await MonModele.findAll({
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

On est obligé de charger le modèle, mais on est pas obligé de faire la synchronisation si on a au préalable.

On peut exécuter la modification et la visualisation du code avec :

```shell
node ma_db_utilisation.js
```

Notez qu'on a utilisé une fonction asynchrone car on veut pourvoir exécuter nos trois requêtes à la suite (d'où les `await).

### on fignole

Les deux fichiers *"ma_db_init.js"* et *"ma_db_utilisation.js"* nécessitent le modèle. Comme la duplication de code est à proscrire, il faut déporter la définition du modèle dans un fichier à part, *"db.js"* :

```js
const { Sequelize, DataTypes } = require('sequelize');
path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});

const MonModele = sequelize.define('MonModele', {
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
        MonModele: MonModele,
    }
}
```

On crée dans ce fichier tout ce qui est nécessaire à l'utilisation de la base de donnée.

Comme ce fichier ne sera lu et exécuté qu'au premier `require`, les autres fois on ne rendra que l'objet `module.exports`, on peut importer ce fichier à de multiple reprise et n'avoir au final qu'une seule base de donnée.

Ceci supprime la duplication des deux fichiers *"ma_db_init.js"* et *"ma_db_utilisation.js"*

*"ma_db_init.js"* :

```js
const db = require("./db")

async function initDB() {
    await db.sequelize.sync({force: true})
    
    var data = await db.model.MonModele.create({
        message: "mon premier message",
        nombre: 7,
    })

    data = await db.model.MonModele.create({
        message: "un autre massage",
        nombre: 3,
    })

}

initDB()
    .then(() => {
        console.log("base initalisée")
    })
```

*"ma_db_utilisation.js"* :

```js
const db = require("./db")

async function utilisation() {
    console.log("Lecture id = 1 :")
    data = await db.model.MonModele.findByPk(1);
    console.log(data.toJSON())

    console.log("---------")
    console.log("clé primaire : ", data.id)
    console.log("message : ", data.message)
    console.log("nombre : ", data.nombre)
    console.log("date de création création : ", data.createdAt)
    console.log("dernière modification : ", data.updatedAt)
    console.log("---------")

    console.log("Lecture id qui n'existe pas :")
    data = await db.model.MonModele.findByPk(42);
    console.log(data) // n'existe pas

    console.log("Lecture tous les éléments :")
    data = await db.model.MonModele.findAll();
    for (element of data) {
        console.log(element.toJSON())
    }

    console.log("Lecture requête :")
    data = await db.model.MonModele.findAll({
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

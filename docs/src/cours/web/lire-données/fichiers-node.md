---
layout: layout/post.njk

title: Lire des fichiers avec node

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Projet node

Commençons par créer un projet <https://nodejs.org/> :

1. créez un dossier `fichier-node`{.fichier} où vous allez mettre les fichiers de votre projet,
2. dans un terminal et dans ce dossier, initialisez votre projet avec la commande `npm init`

Vous devriez maintenant avoir un fichier nommé `package.json`{.fichier} qui contient la configuration minimale d'un projet utilisant node :

```json#
{
  "name": "fichier-node",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```

Nous allons utiliser des bibliothèques pour notre projet, bibliothèques qu'il va falloir importer. Node utilise par défaut un mode d'import nommé [commonjs](https://nodejs.org/api/modules.html#modules-commonjs-modules), alors que javascript en utilise une autre basée sur la norme [ES6 modules](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Modules).

Nous allons dire à node que nous allons utiliser la gestion javascript des modules en ajoutant la ligne `"type": "module",`{.language-} dans le fichier de configuration `package.json`{.fichier}, juste en-dessous de la ligne 5. A la fin de cette opération, vous devriez avoir le fichier un fichier nommé `package.json`{.fichier} qui contient la configuration minimale d'un projet utilisant node :

```json#
{
  "name": "fichier-node",
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

{% info %}
Nous allons utiliser dans toute la suite de ce cours la gestion javascript des modules (es6 modules) et non celle historique de node (commonJS). Si vous cherchez du code sur internet, vous pourrez tout de suite voir de quel type d'import il s'agit :

- `import fs from 'fs';`{.language-} : import ES6
- `const fs = require('fs');`{.language-} : import commonJS

Lorsque vous importez des bibliothèques node, il suffit souvent de remplacer une écriture par l'autre pour que tout fonctionne.

{% endinfo %}

Notre projet est prêt à être utilisé.

## Code initial

Dans le dossier de votre projet, créez un fichier `fichier-texte.txt`{.fichier} contenant :

```
Je suis le contenu du fichier.

Bonjour cher lecteur !

```

Puis un fichier `code.js`{.fichier} :

```js
import fs from 'fs';

let contenu = fs.readFileSync("./fichier-texte.txt", {encoding:'utf8'})
console.log(contenu)
```

En exécutant le code on obtient, comme attendu, le contenu du fichier dans la console :

```shell
$ node code.js 
Je suis le contenu du fichier.

Bonjour cher lecteur !

```

## Dossier courant

Le code précédent charge le fichier de façon relative, donc depuis le dossier courant, qui est celui du terminal. Il ne fonctionnera donc plus si on exécute le fichier `code.js`{.fichier} depuis un autre dossier. Par exemple si on remonte vers le dossier parent avant de l'exécuter :

```shell#
$ cd ..                    
$ node fichier-node/code.js 
node:fs:453
    return binding.readFileUtf8(path, stringToFlags(options.flag));
                   ^

Error: ENOENT: no such file or directory, open './fichier-texte.txt'
    at Object.readFileSync (node:fs:453:20)
    at file:///Users/fbrucker/fichier-node/code.js:3:18
    at ModuleJob.run (node:internal/modules/esm/module_job:218:25)
    at async ModuleLoader.import (node:internal/modules/esm/loader:329:24)
    at async loadESM (node:internal/process/esm_loader:34:7)
    at async handleMainPromise (node:internal/modules/run_main:113:12) {
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: './fichier-texte.txt'
}

Node.js v21.1.0
```

Le fichier `fichier-texte.txt`{.fichier} n'est plus dans le dossier courant mais est à `./fichier-node/fichier-texte.txt`{.fichier}, node ne trouve pas le fichier,

Une solution pour palier ces problèmes de localisation de fichiers est de se fixer un point de référence, comme la localisation du fichier entrain d'être exécuté. On peut facilement trouver ces valeurs avec node qui définit deux variables :

- `__filename`{.language-} : qui contient la localisation du fichier entrain d'être exécuté
- `__dirname`{.language-} : qui contient la localisation du dossier du fichier entrain d'être exécuté

Comme rien ne peut être simple, ces deux variables dépendant de l'import commonjs et ne sont pas directement disponibles lorsque l'on utilise des modules ES6 (comme nous). Il faut donc recréer ces deux variables, heureusement que c'est simple :

```js
import path from 'path'
import {fileURLToPath} from 'url'

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

console.log(__filename)
console.log(__dirname)

```

{% info %}
Si vous avez une version très récente de node, il existe [une alternative](https://nodejs.org/api/esm.html#no-__filename-or-__dirname).
{% endinfo %}

On peut ensuite toutes nos lectures de fichier au dossier `__dirname`{.language-} en utilisant la fonction [`path.join`{.language-}](https://nodejs.org/api/path.html#pathjoinpaths) qui colle des chemins entre eux.

On obtient alors le code final suivant :

```js#
import fs from 'fs';

import path from 'path'
import {fileURLToPath} from 'url'

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let localisation_fichier = path.join(__dirname,  "./fichier-texte.txt");
let contenu = fs.readFileSync(localisation_fichier, {encoding:'utf8'})
console.log(contenu)
```

Ce code est portable, il peut être exécuté de n'importe où :

```shell
$ node code-final.js 
Je suis le contenu du fichier.

Bonjour cher lecteur !

$ cd ..          
$ node fichier-node/code-final.js 
Je suis le contenu du fichier.

Bonjour cher lecteur !

```

## Lecture Asynchrone

La lecture de fichier précédente (ligne 10) :

```js
let contenu = fs.readFileSync(localisation_fichier, {encoding:'utf8'})
```

Était ***synchrone***, c'est à dire que le retour de la fonction `fs.readFileSync`{.language-} est le contenu du fichier. C'est le comportement attendu de tout programme. On passe à la ligne suivant que si la ligne précédente est terminé.

Ce n'est cependant pas ce qu'il se passe dans la majorité des cas dans le web. En effet la lecture d'un fichier peut prendre temps s'il est :

- gros
- sur le réseau

Et souvent, on peut faire autre chose en attendant son chargement. On procède alors de façon ***asynchrone*** : on lance la lecture du fichier puis le programme continue à la ligne suivante. À la fin de la lecture une méthode définie à l'avance  est exécutée.

Ce mode de programmation est dit évènementiel. Le code réagit à des évènements en exécutant une fonction déterminée à l'avance.

### Code asynchrone

Dans notre cas le code serait le suivant :

```js#
import fs from 'fs/promises';

import path from 'path'
import {fileURLToPath} from 'url'

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let localisation_fichier = path.join(__dirname,  "./fichier-texte.txt");
fs.readFile(localisation_fichier, {encoding:'utf8'}).then(data => (
    console.log(data)
))
```

{% faire %}
Créez un fichier `node-asynchrone.js`{.fichier} dans le dossier racine de votre projet (le dossier `fichier-node`{.fichier}) et copiez/collez-y le code précédent.

Exécutez le fichier avec node pour voir que le fichier `fichier-texte.txt`{.fichier} est bien lu.
{% endfaire %}

Il y a deux différences par rapport au code précédant :

1. on importe une autre bibliothèque : `fs/promises`{.language-} en non plus juste `fs`{.language-}
2. on a jouté une méthode `then`{.language-} au fesses de la lecture.

Le paramètre de la méthode `then`{.language-} est une fonction à un paramètre qui sera exécutée à la fin de la lecture : *lorsque* (*then*) la lecture est terminée.

{% faire %}
Vous pouvez vérifier que la lecture du fichier n'est pas immédiate en ajoutant la ligne `console.log("coucou !")`{.language-} à la fin du fichier et voir que "coucou !" est affiché avant le contenu du fichier.
{% endfaire %}

### Promesses

Le mécanisme à l'œuvre ici est appelé [promesse](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Using_promises).

Le retour de la fonction `fs.readFile`{.language-} est une promesse qui possède une méthode `then`{.language-} dont le paramètre est une fonction à un paramètre qui est exécutée à la fin de la promesse si la fonction s'est terminé sans erreur. Le retour est passé en paramètre du paramètre de `then`{.language-}

Explicitons ceci modifiant notre code :

```js
import fs from 'fs/promises';

import path from 'path'
import {fileURLToPath} from 'url'

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let localisation_fichier = path.join(__dirname,  "./fichier-texte.txt");
let promesse = fs.readFile(localisation_fichier, {encoding:'utf8'})

promesse.then(data => {
    console.log("tout s'est bien passé. Le contenu du fichier lu est :");
    console.log(data)
})
```

Souvent, on lie le tout en un seul grand appel (le retour de then est la promesse) :

```javascript
promesse
  .then(réponse => {
    // exécuté lorsque la longue fonction s'arrête
    // le paramètre de cette fonction étant de retour de la longue fonction
  })
```

Le côté sympathique des promesses c'est qu'elle [peuvent s'enchaîner](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#chaining) si le retour de `then`{.language-} est aussi une promesse :

```javascript
promesse
  .then(response => {
    // then de la promesse

    return une_autre_promesse
  })
  .then(response => {
    // c'est le then de une_autre_promesse

  })
```

Enfin, comme on l'a vu tout au début souvent on combine la fonction et son retour sous la forme d'une promesse en seule grosse instruction sans déclarer explicitement de promesse :

```js
// ... 

fs.readFile(localisation_fichier, {encoding:'utf8'})
  .then(data => {
    console.log("tout s'est bien passé. Le contenu du fichier lu est :");
    console.log(data)
  })

// ... 
```

### await/async

Il peut cependant parfois être utile d'écrire du code, *à l'ancienne*, c'est à dire un exécutant ligne à ligne notre code. Il n'y a en effet dans notre cas pas grand intérêt à utiliser du code asynchrone.

Le javascript permet d'utiliser des promesses de façon synchrone en utilisant l'instruction : `await`{.language-}. Cette instruction attend que la promesse se termine pour aller à la ligne d'après. Dans notre cas, cela donnerait :

```javascript
import fs from 'fs/promises';

import path from 'path'
import {fileURLToPath} from 'url'

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let localisation_fichier = path.join(__dirname,  "./fichier-texte.txt");
let contenu = await fs.readFile(localisation_fichier, {encoding:'utf8'})
```

On ne peut cependant pas utiliser `await`{.language-} partout. On ne peut le faire que dans le corps du programme ou à l'intérieur d'une fonction taguée [`async`{.language-}](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function).

Dans notre cas, si on voulait déporter la lecture de notre fichier dans une fonction séparée il faudrait l'écrire de cette façon :

```js
async function lire(fichier) {
    let contenu = await fs.readFile(fichier, {encoding:'utf8'});
    return contenu
}
```

### Gestion des erreurs

Les promesses contiennent aussi une gestion des erreurs avec la méthode `catch`{.language-} dont le paramètre est une fonction à un paramètre qui est exécutée à la fin de la promesse si la fonction a échoué. Le type d'erreur est passé en paramètre du paramètre de `catch`{.language-}

```js
import fs from 'fs/promises';

import path from 'path'
import {fileURLToPath} from 'url'

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let localisation_fichier = path.join(__dirname,  "./fichier-texte.txt");
fs.readFile(localisation_fichier, {encoding:'utf8'})
  .then(data => {
    console.log("tout s'est bien passé. Le contenu du fichier lu est :");
    console.log(data)
  })
  .catch(erreur => {
    console.log("une erreur :", erreur)
  })

```

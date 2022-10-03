---
layout: page
title:  "bases du javascript"
category: cours
author: "François Brucker"
---


### node

[Node](https://nodejs.org/en/) est un interpréteur javascript puissant basé sur la V8 et qui contient des bibliothèques dédiées très pratiques lorsque l'on code en javascript.


<https://nodejs.dev/learn>


#### installation de node {#bloc-id-installation-node}


#### utilisation de node

Une fois <https://nodejs.org/en/>, tapez `node` dans un [terminal]({% link _tutoriels/systeme/2021-08-24-terminal.md %}). Vous êtes dans un interpréteur javascript. Vous pouvez ensuite taper `console.log("bonjour monde !")`. Vous devriez obtenir quelque chose du genre : 

```js
> console.log("coucou")
coucou
undefined
> 
```

La première réponse (`coucou`) correspond à l'action de `console.log` qui est d'afficher du texte, la seconde réponse (`undefined`) correspond au retour de `console.log`.

> Utiliser l'interpréteur `node` dans un terminal est identique à utiliser l'interpréteur `python` par exemple. On tape des lignes qui sont interprétées lorsque l'on tape entrée.

On peut aussi, tout comme pour python, exéctuer un fichier. Par exemple le fichier *"hello.j"* :

```js
nom = "François"

console.log("bonjour " + nom + " !")
```

Qu'on pourra exécuter avec la commande : `node hello.js` dans un terminal se trouvant dans le dossier contenant le fichier *"hello.js"*.

> Soyez à l'aise avec la notion de [terminal]({% link _tutoriels/systeme/2021-08-24-terminal.md %}) et de [dossiers]({% link _tutoriels/systeme/fichiers-navigation.md %}). Entraînez vous si nécessaire.
{.attention}

Pour la bonne bouche, un petit exemple de javascript utilisant node un peu plus compliqué : 

fichier *"hello_qui.js"* : 
```js
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Quel est ton nom ? ', (answer) => {
  console.log(`Bonjour ${answer} !`);

  rl.close();
});
```

On a utilisé :
* l'import de la bibliothèque [readline](https://nodejs.org/api/readline.html#readline_readline) de node,
* [process.stdin](https://nodejs.org/api/process.html#process_process_stdin) et [process.stdout](https://nodejs.org/api/process.html#process_process_stdout) pour les entrées/sorties standard
* une fonction anonyme du type `() => {}` comme paramètre d'une fonction.
* les [construction de chaines de caractère avec `${}`](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Template_literals)



## gestion des dépendances

> TBD : à faire propre
{.note}

L'import de fichiers en javascript est différents de beaucoup d'autres langages. En gros : 

> c'est le cirque.
{.attention}

### bibliothèques node

node_modules et npm/yarn

### importer dans un script

Il existe plusieurs façon d'importer des modules en javascript :
* la façon ecmascript avec les mots clés `import` et `export`
* la façon commonjs avec les mots clés `require` et `module.export`
* la façon web en lisant bêtement le fichier à importer dans l'interpréteur

On peut plus ou moins passer d'une version à l'autre mais c'est compliqué 

<https://redfin.engineering/node-modules-at-war-why-commonjs-and-es-modules-cant-get-along-9617135eeca1>


<https://adrianmejia.com/getting-started-with-node-js-modules-require-exports-imports-npm-and-beyond/>

<https://javascript.info/import-export>

#### ecmascript modules 

import / export

<https://nodejs.org/api/esm.html#esm_modules_ecmascript_modules>

#### commonjs modules 

require 

<https://nodejs.org/api/modules.html#modules_modules_commonjs_modules>

### dans le web

* plusieurs balises script
* charger un fichier par le script
  * local
  * cdn
  * node_modules

<https://developer.mozilla.org/fr/docs/Web/HTML/Element/script>

> par d'import sauf si module 
> <https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Statements/import>
> <https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Modules>
{.attention}
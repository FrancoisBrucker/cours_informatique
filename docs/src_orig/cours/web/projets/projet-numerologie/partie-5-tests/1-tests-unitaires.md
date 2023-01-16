---
layout: layout/post.njk 
title:  "Projet numérologie : partie 5 / tests unitaires"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 5]({% link cours/web/projets/numerologie/partie-5-tests/index.md %}) / [tests unitaires]({% link cours/web/projets/numerologie/partie-5-tests/1-tests-unitaires.md %})
{.chemin}

## bibliothèque de test

Il existe plusieurs bibliothèques permettant de faire des tests unitaires. Nous allons utiliser [jest](https://jestjs.io/)

Commençons par l'installer :

```shell
npm install --save-dev jest
```

Remarquez qu'on a pas utilisé le classique `--save` mais le nouveau `--save-dev`. Ceci à changer le fichier *"package.json"* :

```json
{
  "name": "numerologie",
  "version": "1.0.0",
  "description": "de la numérologie",
  "main": "index.js",
  "scripts": {
    "init": "node db-init.js",
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node index.js"
  },
  "author": "François Brucker",
  "license": "WTFPL",
  "dependencies": {
    "express": "^4.17.1",
    "sequelize": "^6.7.0",
    "sqlite3": "^5.0.2"
  },
  "devDependencies": {
    "jest": "^27.3.1"
  }
}
```

Une valeur a été ajoutée : `"devDependencies"` pour distinguer les dépendances utiles en production (`"dependencies"`) et celles utiles en développement. En tapant :

* `npm install` : toutes les dépendances (`"dependencies"` et `"devDependencies"`) seront installées
* `npm install --production` : uniquement les dépendances `"dependencies"`  seront installées

Voir [la documentation](https://docs.npmjs.com/cli/v7/commands/npm-install) pour de plus amples informations.

## usage

`jest` va exécuter des tests écrit dans des fichiers. Par défaut ces fichiers sont :

* les fichiers finissant par *".test.js"* (ou *".spec.js"*) du projet ou dans ses sous dossiers
* tous les fichiers du dossier *"__tests__"* s'il existe.

### commande

On peut exécuter jest de deux façon, soit via `npm` et une configuration dans *"package.json"* ou en ligne de commande.

#### npm

On commence par associer `jest` aux tests en renseignant le champ `"test"` de l'attribut `"script"` du fichier *"package.json"* :

```json
...

  "scripts": {
    "init": "node db-init.js",
    "test": "jest",
    "start": "node index.js"
  },

...
```

Puis on exécute `jest` en tapant la commande :

```shell
npm test
```

> `npm test` est un raccourci pour `npm run test`

#### CLI

Le programme `jest` est rangé dans le dossier *"node_modules/.bin"*, on peut donc l'appeler directement par la commande :

```shell
./node_modules/.bin/jest
```

### vscode

Vous pouvez installer le plugin [vscode-jest](https://github.com/jest-community/vscode-jest) pour utiliser jest dans vscode. Nous allons ici tout faire en ligne de commande, mais c'est pratique et ça permet (entre autres) :

* à vscode de comprendre notre code jest
* d'exécuter les tests quand on les crée

> La palette de commande permet d'accéder à toutes les commandes du plugin en tapant *jest*

On installera également le module `@types/jest` pour que vscode fasse la completion automatique lorsque l'on code des tests : `npm install --save-dev @types/jest` (tips pris de [là](https://tekloon.dev/autocomplete-for-jest-in-vscode)).

### tests

les tests seront tous de la forme (repris des [premiers pas](https://jestjs.io/fr/docs/getting-started)) :

```js
test('deux plus deux font quatre', () => {
  expect(2 + 2).toBe(4);
});
```

Chaque test aura :

* un nom. Ici : `'deux plus deux font quatre'`
* le test en lui même qui est une fonction et dont le but est de comparer une valeur théorique à une valeur réelle. Ici on cherche à vérifier que `2 + 2` vaut `4`.

L'essence même d'un test est l'utilisation de [comparateurs](https://jestjs.io/fr/docs/using-matchers)

### blocs de tests

Par défaut, on va grouper les tests similaire dans un même fichier. Si l'on a besoin de sous-groupes à l'intérieur d'un fichier, par exemple en faisant un groupe pour les tests d'une fonction, on peut utiliser un bloc [describe](https://jestjs.io/fr/docs/api#describename-fn).

## tests métiers

On va tester ici les méthodes *métiers* c'esrt à dire tout ce qui n'est pas des routes. Notre projet à un unique fichier métier : *"numerologie/back/numerologie.js"*

On doit tester toutes les méthodes de ce fichier : `nombre`, `somme` et `chiffreAssocie`.

Il n'y a jamais de bonne réponses à la question : quoi tester ? La seule réponse satisfaisante est: juste assez pour que l'on soit intimement persuadé que la fonction marche si les testent passent.

De toute façon, si l'on se rend compte (ou plutôt quand on se rendra compte) qu'il y a un bug, on écrira un test qui mettra en évidence le bug, puis on le corrigera. De cette façon ce bug ne pourra plus jamais réapparaitre, les tests étant conservés.

> Lorsqu'un programme et muni de tests, il ne peut jamais régresser : Kent Beck dit que c'est une progression par [cliquet](https://fr.wikipedia.org/wiki/Cliquet_(m%C3%A9canique))

Chaque test doit tester une seule chose, et on peut s'appuyer sur une fonction que si les tests des fonctions qui la composent sont testées. On doit donc tester `nombre` et `somme` avant de tester `chiffreAssocie`.

### module rewire

Il reste un dernier problème à résoudre avant de commencer les tests proprement dit : `nombre` et `somme` ne sont pas exportées, il est donc a priori impossible de simplement les importer pour les tester. POur faire cela, on va utiliser le module [rewire](https://github.com/jhnns/rewire) comme expliqué dans [ce tuto](https://javascript.plainenglish.io/how-to-test-a-non-export-function-in-javascript-a1d0bc339ac) :

```shell
npm install --save-dev rewire
```

### numerologie.test.js

Plaçons nos tests dans un dossier *"numerologie/__tests__"*, comme le veut jest par défaut

> Un autre coding mantra pour la route : [convention over configuration](https://en.wikipedia.org/wiki/Convention_over_configuration). On essaie dans la mesure du possible de se conformer aux conventions, cela facilite le travail en groupe.

```js
const rewire = require('rewire')

const numerologieRewire = rewire('../back/numerologie')
const numerologie = {
    nombre: numerologieRewire.__get__('nombre'),
    somme: numerologieRewire.__get__('somme'),
    chiffreAssocie: numerologieRewire.__get__('chiffreAssocie'),
}

describe("numerologie.nombre", () => {
    test("chaine vide", () => {
        expect(numerologie.nombre("")).toBe(0)
    })
    test("un caractère simple", () => {
        expect(numerologie.nombre("A")).toBe(65)
    })
    test("deux caractères", () => {
        expect(numerologie.nombre("éç")).toBe(0xE9 + 0xE7)
    })
})

describe("numerologie.somme", () => {
    test("0", () => {
        expect(numerologie.somme(0)).toBe(0)
    })
    test("un chiffre", () => {
        expect(numerologie.somme(4)).toBe(4)
    })
    test("un nombre", () => {
        expect(numerologie.somme("101")).toBe(2)
    })
})


describe("numerologie.chiffreAssocie", () => {
    test("éç", () => {
        expect(numerologie.chiffreAssocie("éç")).toBe(1 + 4)
    })
})
```

### exécution des tests

On peut exécuter ce code de plusieurs manières :

* tous les tests via `npm` : `npm test`
* tous les tests via le programme : `./node_modules/.bin/jest`
* un fichier particulier via `npm` : `npm test -- __tests__/numerologie.test.js` (`npm test --  numerologie.test.js` fonctionne aussi)
* un fichier particulier via le programme : `./node_modules/.bin/jest __tests__/numerologie.test.js` (`./node_modules/.bin/jest numerologie.test.js` fonctionne aussi)

Chez moi, le résultat de ces tests est :

```text

> numerologie@1.0.0 test
> jest

 PASS  __tests__/numerologie.test.js
  numerologie.nombre
    ✓ chaine vide (2 ms)
    ✓ un caractère simple
    ✓ deux caractères (1 ms)
  numerologie.somme
    ✓ 0
    ✓ un chiffre
    ✓ un nombre
  numerologie.chiffreAssocie
    ✓ éç

Test Suites: 1 passed, 1 total
Tests:       7 passed, 7 total
Snapshots:   0 total
Time:        0.489 s, estimated 1 s
Ran all test suites.
```

On voit les noms des 3 suites et des tests dans chacune d'elle.

### structure du fichier

On a commencé par importer toutes les fonction de *"numerologie/back/numerologie.js"*, puis on a fait un bloc par fonction testée. Pour chaque fonction, je commence par tester un cas simple (sans paramètre ou un paramètre trivial), puis les cas d'usages courant.

J'ai l'impression que si ces tests fonctionnent, mes fonctions sont correctes.

### coverage

Pour savoir si nos tests couvrent bien l'ensemble du projet, c'est à dire si les tests passent bien par chaque ligne de code, on utilise des outils de [couverture de code](https://fr.wikipedia.org/wiki/Couverture_de_code).

>**Attention** : Avoir 100% de couverture de code ne signifie pas que votre projet est bien testé... Juste que les tests ont utilisé toutes les lignes de codes :
>
>* ça ne prouve pas que les fonctionnalités de votre code sont correctes
>* certaines fonctions n'ont pas besoin d'être testées (comme les constantes ou les affichages à l'écran par exemple)

Le code coverage est particulièrement utile pour savoir si on a bien testé ce *else* d'un *if/then/else* qui n'arrive que rarement.

Il suffit de rajouter `--coverage`à jest pour qu'il fasse le coverage tout seul : `npm test -- --coverage` (ou `./node_modules/.bin/jest --coverage`).

Si on essaie sur notre code... Ca ne va pas marcher. C'est à cause du module `rewire` qui ne déclenche pas le coverage de jest. Pour palier ça, on va utiliser chiffre, qui est la fonction importée plutôt que de l'utiliser via `rewire` dans *"numerologie/__tests/numerologie.test.js"* :

```js
const rewire = require('rewire')
const { chiffre } = require('../back/numerologie')

const numerologieRewire = rewire('../back/numerologie')
const numerologie = {
    nombre: numerologieRewire.__get__('nombre'),
    somme: numerologieRewire.__get__('somme'),
    chiffreAssocie: chiffre,
}

// ...
```

Lorsque l'on exécutera nos tests avec coverage (`npm test -- --coverage`), on aura comme réponse :

```text

> numerologie@1.0.0 test
> jest "--coverage"

 PASS  __tests__/numerologie.test.js
  numerologie.nombre
    ✓ chaine vide (1 ms)
    ✓ un caractère simple
    ✓ deux caractères
  numerologie.somme
    ✓ 0
    ✓ un chiffre (1 ms)
    ✓ un nombre
  numerologie.chiffreAssocie
    ✓ éç (1 ms)

----------------|---------|----------|---------|---------|-------------------
File            | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s 
----------------|---------|----------|---------|---------|-------------------
All files       |     100 |      100 |     100 |     100 |                   
 numerologie.js |     100 |      100 |     100 |     100 |                   
----------------|---------|----------|---------|---------|-------------------
Test Suites: 1 passed, 1 total
Tests:       7 passed, 7 total
Snapshots:   0 total
Time:        0.574 s, estimated 1 s
Ran all test suites.
```

Les tests de `chiffreAssoce` (et uniquement eux, les autres passant par le module rewire) passent bien par toute les lignes de *"back/numerologie.js"*. 

Modifions le test de chiffreAssocie pour s'en convaincre :

```js
describe("numerologie.chiffreAssocie", () => {
    test("éç", () => {
        expect(numerologie.chiffreAssocie("")).toBe(0)
    })
})
```

Le résultat est maintenant :

```text

> numerologie@1.0.0 test
> jest "--coverage"

 PASS  __tests__/numerologie.test.js
  numerologie.nombre
    ✓ chaine vide (1 ms)
    ✓ un caractère simple
    ✓ deux caractères
  numerologie.somme
    ✓ 0
    ✓ un chiffre (1 ms)
    ✓ un nombre
  numerologie.chiffreAssocie
    ✓ éç (1 ms)

----------------|---------|----------|---------|---------|-------------------
File            | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s 
----------------|---------|----------|---------|---------|-------------------
All files       |      50 |      100 |   66.66 |      50 |                   
 numerologie.js |      50 |      100 |   66.66 |      50 | 4,10-15,22        
----------------|---------|----------|---------|---------|-------------------
Test Suites: 1 passed, 1 total
Tests:       7 passed, 7 total
Snapshots:   0 total
Time:        0.575 s, estimated 1 s
Ran all test suites.
```

On est pas passé par la ligne 4 (l'intérieur de la boucle for de la fonction `nombre`), 10 à 15 (on a pas utilisé la fonction `somme`) et 22 (l'intérieur du while de `chiffreAssocie`).

Remettons nos test comme avant pour bien avoir 100 de coverage...

> Le coverage crée un dossier coverage, que l'on ajoute dans le fichier *".gitignore"*, il n'a pas à être suivi.

## mocker des fonctions

Concept avancé mais très utile lorsque l'on veut tester un comportement spécifique d'une fonction sans avoir à tout paramétrer. On va l'utiliser ici de façon un peut surfaite, mais pensez-y pour les tests de pannes, d'erreurs ou de fonction nécessitant le réseau.

<https://jestjs.io/docs/mock-functions>

## ressources

* <https://www.valentinog.com/blog/jest/>
* <https://practicalprogramming.fr/jest>
* <https://jestjs.io/>

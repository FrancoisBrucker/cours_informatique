---
layout: page
title:  "Tests Unitaires"
category: tutorial
tags: tests unitaires
authors: 
    - "Romain Herbelleau"
    - "Theophile Bonneau"
---

Les tests unitaires permettent d’automatiser la vérification du bon fonctionnement d’une partie du site que l’on est entrain de développer.
Pour cela on utilise la bibliothèque [jest](https://jestjs.io/) 

## Mise en place de Jest

- Tout d’abord on crée un projet node avec [yarn](https://classic.yarnpkg.com/en/), pour créer ce projet on utilise ``yarn init``
- On installe jest ``yarn add --dev jest``.
- On place dans ``.gitignore`` les fichiers et dossiers de jest car cette dépendance ne nous intéresse qu’en local pour développer.
- Dans *package.json* on ajoute

~~~ shell
”scripts”: {
	“test”: “jest”
},
~~~

On pourra ensuite exécuter la commande ``yarn run test`` pour exécuter tous les tests.

Par défaut, *jest* va exécuter tous les fichiers qui finissent par test.js récursivement dans tout le projet et tous les fichiers dans le dossier **__tests__**.

``yarn run test`` (ou ``./node_modules/.bin/jes``) permet de déclencher les tests.

Voila, normalement tout est en place pour programmer des tests unitaires.

On peut tester si cela marche bien en créant par exemple le fichier *main.test.js*:

~~~ shell
test('empty test', () => {
  expect(true).toBe(true);
});
~~~ 
Puis on l'exécute avec ``yarn run test``.


## Import

Un import, créer le lien entre *main.js* et *main.test.js*.
L'intérêt d’un test est de tester une fonction dans notre programme. Généralement, un fichier test ``main.test.js``, teste les fonctions qui existent dans ``main.js``. Pour que cela fonctionne, il faut importer les fonctions de ``main.js`` dans le fichier test. 

Pour cela :
- On exporte avec ``module.exporte``. On peut choisir d’exporter différentes choses : objets, fonction…
- On importe grâce à la commande ``require``

Exemple :

*main.js*
~~~ shell
function addCinq (nombre) {
	return nombre +5
}
module.exports = addCinq
~~~
*main.test.js*
~~~ shell
addCinq = require (“./main”)

test(“addition”, () =>{
	expect(addCinq(7)).toBe(12)
})
~~~

## Plusieurs imports

Bien évidement on voudra tester plusieurs choses lors de nos tests. Pour cela il exciste deux solutions :

- La première est de passer tous les paramètres dans l’*export*.

``module.export = {addCinq, mulCinq}``

et de les récupérer dans le *require*.

``{addCinq, mulCinq} = require  (“./main”)``

- La deuxième, et la plus courante, est de passer un objet contenant les différents éléments que l’on veut transférer.

*main.js*
~~~ shell

module.exports = {
    add: addCinq,
}
~~~

*main.test.js*
~~~ shell

main = require("./main")

test("addition", () => {
    expect(main.add(7)).toBe(12)
})
~~~

## Retour de fonction

Il est aussi possible, et intéressant dans certains cas, de retourner une fonction plutot que des modules. Cela permet de rentrer un paramètre dans la fonction importée.

*main.js*
~~~ shell

module.exports = (parametre) => {
    return {
        addition: (data) => {return data + parametre},
    }
}
~~~
*main.test.js*
~~~ shell

main = require("./main")(5)

test("addition", () => {
    expect(main.addition(7)).toBe(12)
})
~~~

## Tests groupés

Il est possible de grouper les tests par unit si par exemple ces tests sont reliés. Cela permet de paramétrer différents setup pour les différentes units. Pour les setup, on utilise ``beforeAll()``.

*main.test.js*

~~~ shell
main = require(./main)
let chiffre;
let somme;
let multiplication;

describe('testing math utilities', () => {
    beforeAll(() => {
        chiffre = 7;
        somme = 12;
        multiplication = 35;
    })

    test('la somme doit faire 12', () => {
        expect(add(chiffre)).toBe(somme);
    });

    test('la multiplication doit faire 35', () => {
        expect(mulCinq(chiffre)).toBe(multiplication);
    });
});
~~~




---
layout: layout/post.njk

title: "Projet numérologie : partie 5 / tests unitaires : js"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons ajouter des tests unitaires à notre projet. Il existe de [nombreuses bibliothèques](https://www.lambdatest.com/blog/best-javascript-unit-testing-frameworks/) de tests en javascript. Nous allons nous focaliser sur [jest](https://jestjs.io/fr/) efficace et populaire.

## Installation

### Bibliothèque

On installe la bibliothèque pour le développement (on en aura pas besoin en production) :

```
npm install --save-dev jest
```

Si vous regardez le fichier `package.json`{.fichier}, vous voyez que jest est dans une section de dépendance spéciale, où sont listées les bibliothèque non utiles en production :

```json
...
    "devDependencies": {
        "jest": "^29.5.0",
    }
...
```

Une valeur a été ajoutée : `"devDependencies"` pour distinguer les dépendances utiles en production (`"dependencies"`) et celles utiles en développement. En tapant :

* `npm install` : toutes les dépendances (`"dependencies"` et `"devDependencies"`) seront installées
* `npm install --production` : uniquement les dépendances `"dependencies"`  seront installées

Voir [la documentation](https://docs.npmjs.com/cli/v7/commands/npm-install) pour de plus amples informations.

### Exécutable

Puis on va l'utiliser pour lancer nos tests avec la commande `npm run test`. Pour cela, modifions l'entrée test du `package.json`{.fichier}  pour :

```json
...

"scripts": {

    ...

    "test": "jest",

    ...
}

...
```

L'exécutable jest est présent dans le dossier `node_modules/.bin/`{.fichier}. On peut alors l'exécuter :

* soit avec son nom complet `node_modules/.bin/jest`
* soit en utilisant la commande [`npx`](https://www.npmjs.com/package/npx) :  `npx jest`

### vscode

Vous pouvez installer le plugin [vscode-jest](https://github.com/jest-community/vscode-jest) pour utiliser jest dans vscode. Nous allons ici tout faire en ligne de commande, mais c'est pratique et ça permet (entre autres) :

* à vscode de comprendre notre code jest
* d'exécuter les tests quand on les crée

> La palette de commande permet d'accéder à toutes les commandes du plugin en tapant *jest*

On installera également le module `@types/jest` pour que vscode fasse la completion automatique lorsque l'on code des tests : `npm install --save-dev @types/jest` (tips pris de [là](https://tekloon.dev/autocomplete-for-jest-in-vscode)).

Par défaut `jest` va exécuter tous les fichiers :

* de la forme `[nom].test.js`{.fichier} dans le dossier du projet et dans tout ses sous dossiers.
* de la forme `[nom].js`{.fichier} dans le dossier `__tests__`{.fichier} et dans tout ses sous dossiers.

{% info %}
[Chemins par défaut des fichiers de tests](https://jestjs.io/docs/configuration/#testmatch-arraystring) pour jest.

{% endinfo %}

## Utilisation de jest

### Fonctionnement

Essayons ça en créant un fichier `__tests__/essais.js`{.fichier} :

```js
test('test vide', () => {
  expect(true).toBe(true);
});
```

Chaque test aura :

* un nom. Ici : `'test vide'`{.language-}
* le test en lui même qui est une fonction et dont le but est de comparer une valeur théorique à une valeur réelle. Ici on cherche à vérifier que `true` vaut `true`.

### Exécution des tests

Puis exécutons le par les différentes manières possibles :

* `npm test` qui est un raccourci pour `npm run test`
* `npx jest`
* `node_modules/.bon/jest`
* `npx jest __tests__/essais.js`

{% faire %}
Changez ensuite le vrai en faux pour voir le test planter.
{% endfaire %}

## Import ES6

Par défaut, `jest`ne fonctionne qu'avec les import commonJs de node. [Pour utiliser les modules ES6](https://jestjs.io/docs/ecmascript-modules) il faut le préciser à `jest` avec une variable d'environnement :

```
NODE_OPTIONS=--experimental-vm-modules npx jest
```

{% faire %}
Modifiez le script d'exécution des tests `package.json`{.fichier} pour qu'il puisse utiliser les imports ES6.
{% endfaire %}

## Tests

Nous allons tester ici les fonctions de `numérologie.js`{.fichier}

Pour l'instant, le fichier numérologie exporte un objet contenant une référence vers la fonction `chiffreAssocie`{.language-}. Exportons les 2 autres fonctions :

```javascript
export default {
    chiffre: chiffreAssocie,
    nombre: nombre,
    somme: somme,
}
```

```js
import numérologie from "../back/numérologie.js"

describe("Un chiffre associé à un prénom", () => {
    test("65 -> 6 + 5 = 11 -> 1 + 1 = 2", () => {
        expect(numérologie.somme(65)).toBe(6+5)
    })
    test("nombre associé au prénom d'une lettre", () => {
        expect(numérologie.nombre("A")).toBe(65)
    })
    test("nombre associé au prénom de plusieurs lettres", () => {
        expect(numérologie.chiffre("A")).toBe(2)
        expect(numérologie.chiffre("m")).toBe(1)
        expect(numérologie.chiffre("y")).toBe(4)
        expect(numérologie.chiffre("Amy")).toBe(2 + 1 + 4)
    })

})
```

Par défaut, on va grouper les tests similaire dans un même fichier. Si l'on a besoin de sous-groupes à l'intérieur d'un fichier, par exemple en faisant un groupe pour les tests d'une fonction, on peut utiliser un bloc [describe](https://jestjs.io/fr/docs/api#describename-fn).

## Front

On peut tester de la même manière le js front. En revanche, on ne testera pas la manipulation de l'arbre DOM, il faut donc séparer les fichiers js en 2 types : ceux testables et les autres.

Les fichiers js testables sont ensuite importé directement dans les fichiers html avec [un import classique](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import).

Ici nous n'avons que ju javascript qui manipule l'arbre DOM, il est donc inutile de le tester.

## Coverage

Pour savoir si nos tests couvrent bien l'ensemble du projet, c'est à dire si les tests passent bien par chaque ligne de code, on utilise des outils de [couverture de code](https://fr.wikipedia.org/wiki/Couverture_de_code).

{% attention %}
Avoir 100% de couverture de code ne signifie pas que votre projet est bien testé... Juste que les tests ont utilisé toutes les lignes de codes :

* ça ne prouve pas que les fonctionnalités de votre code sont correctes
* certaines fonctions n'ont pas besoin d'être testées (comme les constantes ou les affichages à l'écran par exemple)

{% endattention %}

Le code coverage est particulièrement utile pour savoir si on a bien testé ce *else* d'un *if/then/else* qui n'arrivent que rarement.

Il suffit de rajouter `--coverage`à jest pour qu'il fasse le coverage tout seul : `npm test -- --coverage` (ou `./node_modules/.bin/jest --coverage`).

{% lien %}
<https://www.valentinog.com/blog/jest-coverage/>
{% endlien %}

Modifions le test de chiffreAssocie pour s'en convaincre :

```js
test("nombre associé au prénom de plusieurs lettres", () => {
    expect(numérologie.chiffreAssocie("")).toBe(0)
})
```

Ou ajoutons un fichier et voyons comme tout n'est pas testé :

`__tests__/numérologie.js`{.fichier} :

```js
import numérologie from "../back/numérologie.js"
import db from "../db.js" // inutile. Juste pour voir le coverage

// ...
```

## Mocker des fonctions

Concept avancé mais très utile lorsque l'on veut tester un comportement spécifique d'une fonction sans avoir à tout paramétrer. On va l'utiliser ici de façon un peut surfaite, mais pensez-y pour les tests de pannes, d'erreurs ou de fonction nécessitant le réseau.

{% lien %}
<https://jestjs.io/docs/mock-functions>
{% endlien %}

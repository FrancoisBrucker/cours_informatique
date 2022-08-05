---
layout: page
title:  "serveur Web avec node"
category: tutorial
tags: dev node
author: "François Brucker"
---

## But

Un (trop) long tutorial pour mettre en place un serveur web et la plupart des outils nécessaires pour son développement et son maintient.

On prendra comme exemple un site de numérologie qui associe un numéro à chaque prénom.

On aimerait avoir un site :

  - dont le titre serait numérologie
  - et où on pourrait taper son prénom pour en connaître son numéro
  - si l'on ne tape aucun prénom, le site devrait afficher un '?'
  

## initialisation du projet

On va écrire le code en [node](https://nodejs.org/en/), donc commencez par l'installer (avec apt-get ou brew) si ce n'est pas déjà le cas.

### node

[Node](https://nodejs.org/en/) est un interpréteur [javascript V8](https://fr.wikipedia.org/wiki/V8_(moteur_JavaScript)) performant, très utilisé pour créer des serveur web. On va commencer par découvrir un peu ses fonctionnalités en console. Tapez `node` dans un terminal pour entrer en mode interpréteur où chque ligne tapée est directement interprétée ;

~~~ shell
fbrucker@emma » node
Welcome to Node.js v14.13.0.
Type ".help" for more information.
> console.log("Hello World!")
Hello World!
undefined
> x = 1
1
> console.log(x)
1
undefined
> f = () => { return "je suis une fonction"}
[Function: f]
> f()
'je suis une fonction'
~~~

Chaque ligne est exécutée puis son résultat est donné. C'est pour ça qu'il y a de temps en temps des `undefined`, c'est des retour de fonctions (comme `console.log` qui ne rend **RIEN**, elle ne fait qu'afficher à l'écran)

C'est idéal pour tester des choses, en particulier pour reprendre les exemples de [cette fameuse comparaison entre ruby et js](https://www.destroyallsoftware.com/talks/wat) (même si les plus terribles exemples ont été corrigés...).


### git 

On suit le tuto et on crée notre projet git, que l'on synchronise avec notre github.

  1. `git init`
  2. synchronise avec github
  3. on crée un fichier `main.js` vide et on commit le tout.

## Un peut de js

On va créer un site de numérologie du prénom qui associera un nombre à chaque prénom écrit en utf8. On va s'inspirer de [cet article scientifique](https://numerologist.com/numerology/the-numerology-of-your-first-name-decoded-explained/) mais permettre tout prénom écrit en unicode. Il nous faut donc :

  - pouvoir associer un chiffre à chaque lettre
  - sommer tout ça et, si le nombre est plus grand que 10, re-sommer les chiffres sauf si la somme fait 11, 22, ou 33.
  
On ne va cependant pas commencer à coder directement, on va utiliser une bibliothèque de tests unitaires, [jest](https://jestjs.io/) et créer un projet node avec [yarn](https://classic.yarnpkg.com/en/) (`yarn init` pour initialiser le projet, suivez le tuto dédié si vous avez du mal)

### jest

On installe jest comme dépendance de développement au projet, on en aura en effet pas besoin en production : `yarn add --dev jest`. `git status` devient fou, on ajute donc ce qu'il faut dans le `.gitignore` et on commit le tout.

Remarquez que le fichier `package.json` contient les dépendances de développement.

On va tout de suite ajouter une ligne pour que les tests s'exécutent via une commande `yarn` en ajoutant les lignes suivantes à votre fichier *package.json* :

~~~
"scripts": {
    "test": "jest"
  },
~~~

On pourra ensuite exécuter la commande `yarn run test` pour exécuter tous les tests. Pour l'instant il n'y en a pas. 

> **Nota Bene :** Si l'on ne veut pas passer par une commande de `yarn`, il faut trouver l'exécutable `jest` qui se trouve dans *node_modules/.bin*


Par défaut, *jest* va exécuter tous les fichier qui finissent par *test.js* récursivement dans tout le projet et tous les fichiers dans le dossier **__tests__**.

Essayons ça en créant un fichier *main.test.js* :

~~~ js
test('empty test', () => {
  expect(true).toBe(true);
});
~~~

Puis `yarn run test` (ou `./node_modules/.bin/jest`) pour voir le résultat.

Changez ensuite le vrai en faux pour voir le test planter.

### import

Nos tests doivent importer des fonctions définies autre part. Typiquement le fichier de test *main.test.js* doit importer des fonctions définies dans *main.js*. La gestion des imports est spéciale en js, et suit deux modèles celui de commonJs et l'autre ES6. Nous allons ici suivre celui classique dans node de commonJS. 

Tout est expliqué [dans cet excellent guide](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Modules), mais en deux mots :

  - on n'exporte qu'un nom `module.exports`. Ce nom peut alors être plein de choses mais c'est typiquement une fonction ou un objet.
  - on importe un nom via la commande `require`.
 

#### exemple 

*main.js* :

~~~ js
function numerologie(prenom) {
    return 22
}

module.exports = numerologie
~~~

*main.test.js* :

~~~ js
numerologie = require("./main")

test("numerologie", () => {
    expect(numerologie("moi")).toBe(22)
})

~~~

#### plusieurs imports

Si l'on veut importer plusieurs choses, on a coutume de rendre un objet dont les clés sont les noms et les valeurs le fonctions associées.

*main.js* : 

~~~ js
function numerologie(prenom) {
    return 22
}

module.exports = {
    numerologie: numerologie,
}
~~~

et le *main.test.js* : 

~~~ js
main = require("./main")

test("numerologie", () => {
    expect(main.numerologie("moi")).toBe(22)
})
~~~

#### retour de fonctions

L'intérêt de rendre une fonciton plutôt qu'un module est que l'on peut ainsi paramétrer ce que l'on rend. 

Exemple : 

~~~ js
module.exports = (parametre) => {
    return {
        addition: (data) => {return data + parametre},
    }
}
~~~

et le test : 

~~~ js
main = require("./main")(42)

test("numerologie", () => {
    expect(main.addition(8)).toBe(50)
})

~~~


### le code and main.json

  - trouver le code associé à un caractère est facile en js en utilisant [charCodeAt](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Objets_globaux/String/charCodeAt). Testez dans un node ` ('coucou').charCodeAt(1)` par exemple ou encore `('你好').charCodeAt(0)`
  - pour associer un chiffre à un nombre en sommant ses composantes on peut tricher en utilisant les chaînes de caractères. Cela va être notre premier test.
  
On va mettre tout ça dans les fichiers *numerologie.js* et *numerologie.test.js* 

On ajoute une [suite de test](https://jestjs.io/docs/en/api#describename-fn) qui va correspondre à l'association d'un chiffre à un prénom. Commençons par le test :

#### boilerplate 

*numerologie.js* :

~~~ js

module.exports = {
    somme: (nombre) => {
        return 6+5
    }
}

~~~

*numerologie.test.js* :

~~~ js
numerologie = require("./numerologie")

describe("Un chiffre à un prenom", () => {
    test("somme des nombres", () => {
        expect(numerologie.somme(65)).toBe(6+5)
    })

})

~~~
  
#### on résoud le problème

*numerologie.js* : 

~~~ js
module.exports = {
    somme: (nombre) => {
        somme = 0
        chaine = String(nombre)
        for (var i=0; i < chaine.length ; i++) {
            somme += parseInt(chaine.charAt(i))
        }        
        return somme
    }
}

~~~
 

Ce qui nous permet de transformer tout nombre en somme de ses chiffres tant que sa valeur est >9.

En ajoutant un test : 

*numerologie.test.js* :

~~~ js
numerologie = require("./numerologie")

describe("Un chiffre à un prenom", () => {
    test("somme des nombres", () => {
        expect(numerologie.somme(65)).toBe(6+5)
    })
    test("<=9", () => {
        expect(numerologie.sommeFinale(65)).toBe(2)
    })
})
~~~

et le code : 

*numerologie.js*

~~~ js
function somme(nombre) {
    var somme = 0
    chaine = String(nombre)
    for (var i=0; i < chaine.length ; i++) {
        somme += parseInt(chaine.charAt(i))
    }
    return somme
}

function sommeFinale(nombre) {
    while (nombre > 9) {
        nombre = somme(nombre)
    }
    return nombre
}

module.exports = {
    somme: somme,
    sommeFinale: sommeFinale,
}
~~~


> **Nota Bene :** Attention à la blague lorsque l'on enlève le `var` à la première ligne de la fonction somme. La variable n'est plus locale et elle remplace donc la valeur de la fonction...

#### le nombre associé à un prenom


*numerologie.test.js* :

~~~ js
numerologie = require("./numerologie")

describe("Un chiffre à un prenom", () => {
    test("somme des nombres", () => {
        expect(numerologie.somme(65)).toBe(6+5)
    })
    test("<=9", () => {
        expect(numerologie.sommeFinale(65)).toBe(2)
    })
    test("nombre associé au prénom d'une lettre", () => {
        expect(numerologie.nombre("A")).toBe(2)
    })
    test("nombre associé au prénom de plusieurs lettres", () => {
        expect(numerologie.nombre("A")).toBe(2)
        expect(numerologie.nombre("m")).toBe(1)
        expect(numerologie.nombre("y")).toBe(4)
        expect(numerologie.nombre("Amy")).toBe(2 + 1 + 4)
    })

})

~~~


Le code : 

*numerologie.js*

~~~ js

function somme(nombre) {
    var somme = 0
    chaine = String(nombre)
    for (var i=0; i < chaine.length ; i++) {
        somme += parseInt(chaine.charAt(i))
    }
    return somme
}

function sommeFinale(nombre) {
    while (nombre > 9) {
        nombre = somme(nombre)
    }
    return nombre
}

function nombre(chaine) {
    var somme = 0
    for (var i=0; i< chaine.length; i++) {
        somme += sommeFinale(chaine.charCodeAt(i))
    }
    return sommeFinale(somme)
}

module.exports = {
    somme: somme,
    sommeFinale: sommeFinale,
    nombre: nombre,
}

~~~

> **Nota Bene :** On a pas ici traité le cas particuliers des prénoms valant 11, 22, ou 33;


## Une page web


On va créer une page *index.html* qui nous permettra d'associer un chiffre à chaque prénom

On va d'abord créer le html puis le rendre joli et enfin ajouter le js.

### html


~~~ html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Numérologie</title>
    </head>
    <body>
        <form>
            <label for="prenom">Prénom :</label>
            <input id="prenom" type="text" name="prenom"/>

            <button type="submit">Envoi</button>
        </form>
        <p>7</p>
    </body>
</html>

~~~


### css

On va le rendre joli. D'abord en mettant un peu de css puis en ajoutant la lib [purecss](https://purecss.io/).

#### main.css

~~~ css
html, body {
    margin: 0;
    background-color: azure;
}

.body {
    margin-top: 100px;
    margin-left: auto;
    margin-right: auto;
    width: 600px;
    text-align: center;
}

p {
    font-size: 100px;
}

~~~


en modifiant un peu le html :

~~~ html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Numérologie</title>

        <link href="main.css" rel="stylesheet">

    </head>
    <body>
        <div class="body">
            <form>
                <label for="prenom">Prénom :</label>
                <input id="prenom" type="text" name="prenom"/>

                <button type="submit">Envoi</button>
            </form>
            <p>7</p>
        </div>
    </body>
</html>
~~~

#### on ajoute purecss 

Pour cela on va le rajouter à nos dépendances du projet : `yarn add purecss`

E l'ajouter, avec son style dans le *index.html* :

  - on le rajoute avant le link du *main.css* car on doit avoir le dernier mot pour les propriétés css
  - on prend la version *-min* qui est "minified" pour être chargée plus vite.

On a du coup : 

*main.css* :

~~~ css
html, body {
    margin: 0;
    background-color: azure;
}

.body {
    margin-top: 100px;
    margin-left: auto;
    margin-right: auto;
    width: 600px;
    text-align: center;
}

p {
    margin-top: 0;
    margin-bottom: 0;
    font-family: 'Lobster', cursive;
    font-size: 200px;
}
~~~

*index.html* :

~~~ html 
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Numérologie</title>

        <link href="./node_modules/purecss/build/pure-min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
        <link href="main.css" rel="stylesheet">

    </head>
    <body>
        <div class="body">
            <form class="pure-form">
                <label for="prenom">Prénom :</label>
                <input id="prenom" type="text" name="prenom"/>

                <button type="submit"class="pure-button pure-button-primary">Envoi</button>
            </form>
            <div class="pure-g">
                <div class="pure-u-1-3"></div>
                <div class="pure-u-1-3"><p>7</p></div>
                <div class="pure-u-1-3"></div>
            </div>

        </div>
    </body>
</html>
~~~

### js

Pour l'instant appuyer sur le bouton ne sert à rien. On va donc faire en sorte que lorsque'on appuie sur le bouton le chiffre change.
 

On ne peut pas utiliser require dans le browser... Pour le pas avoir besoin de compiler notre js on fait des choses un peu sales.


~~~ html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Numérologie</title>

        <link href="./node_modules/purecss/build/pure-min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
        <link href="main.css" rel="stylesheet">

    </head>
    <body>
        <div class="body">
            <form class="pure-form">
                <label for="prenom">Prénom :</label>
                <input id="prenom" type="text" name="prenom"/>

                <button id="button-form" type="submit" class="pure-button pure-button-primary">Envoi</button>
            </form>
            <div class="pure-g">
                <div class="pure-u-1-3"></div>
                <div class="pure-u-1-3"><p id="get-value">7</p></div>
                <div class="pure-u-1-3"></div>
            </div>

        </div>

        <script>
         module = {}
        </script>
        <script src="numerologie.js"></script>
        <script src="main.js"></script>
    </body>
</html>
~~~ 

*main.js*

~~~ js
function change_value() {
    prenom = document.querySelector("#prenom").value
    if (prenom) {
        document.querySelector("#get-value").textContent = nombre(prenom)
    } else {
        document.querySelector("#get-value").textContent = "?"
    }

}
change_value()

document.querySelector("#button-form").addEventListener("click", (event) => {
    change_value()
    event.preventDefault()
})
~~~

>**Nota Bene :** on pourrait ajouter une animation pour savoir que le code est exécuté.


## on met en prod !

On envoie le tout sur l'ovh !

  1. une fois sur l'ovh (on fait attention d'être bien parti avec son agent) on clone notre répo dans le dossier `~/www`
  2. on procède à un `yarn install --production` qui va mettre à jour tous nos packages, exepté ceux liés au développement. On a donc uniquement `purecss`. Comparez avec la taille en dev. 


## tests fonctionnels/users stories

Lorsque l'on fabrique un site, on a envie de l'utiliser d'une certaine manière, de pouvoir naviguer et récupérer des informations. On peut regrouper ces utilisations en  petites saynètes d'utilisation 
appelées *user stories*.

On a déjà notre première user story, c'est notre but. Il est atteint puisqu'on peut faire cette user story sur l'ovh.

Comme toujours, on va automatiser ce processus en utilisant un script qui fera les manipulation et vérifiera le résultat pour nous.

### selenium

[selenium](https://www.selenium.dev/) est un outil, écrit en java, qui permet d'automatiser un browser. 

Cet outils est très générique car :
    - de nombreux browsers sont supportés
    - on peut utiliser selenium en codant avec de nombreux langages.

Avant d'utiliser selenium pour notre site, faisons le fonctionner.

#### exemple

Pour que l'on puisse faire fonctionner selenium vous devez avoir un java d'installé (vous devriez le faire avec [sdkman](https://sdkman.io/))


On va avoir besoin de plusieurs bibliothèques : `yarn add --dev selenium-webdriver chromedriver` :

  - `selenium-webdriver` est selenium proprement dit,
  - un driver de navigateur (`geckodriver` pour firefox ou `chromedriver` pour chrome)
  

Pour finir la paramétrisation, voilà le *package.json* avec les deux driver de navigateurs installés :

~~~
{
  "name": "selenium_jest",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT",
  "devDependencies": {
    "geckodriver": "^1.20.0",
    "jest": "^26.5.2",
    "selenium-webdriver": "^4.0.0-alpha.7",
    "chromedriver": "85.0.0"
  }
}
~~~

> **Nota Bene :** On a mis la version 85 de chromedriver car la version 86 n'est pas encore supportée chez moi.


On place notre premier essai dans le fichier : *user-story/look-at-google.user-story.js* (on a pas mis l'extension test sinon il serait exécuté tout le temps avec les tests unitaires et ça prend un peu de temps...)

~~~ js

var fs = require('fs');

const url = 'https://www.google.com'



const {By, Key} = require('selenium-webdriver');

const webdriver = require('selenium-webdriver');
 
 
describe('Google renders', () => {

    // beforeEach(() => {
    //     require('chromedriver');
    //     browser =  new webdriver.Builder().forBrowser('chrome').build()
    // })

    beforeEach(() => {
        require('geckodriver');
        browser =  new webdriver.Builder().forBrowser('firefox').build()
    })


  test('it renders', async () => {
    await browser.get(url)
    const title = await browser.getTitle()
    expect(title).toContain('Google')
  })

  test('save a picture', async () => {
        // files saved in ./reports/screenshots by default
        await browser.get(url)
        const iframe = browser.findElement(By.css('iframe'));
        await browser.switchTo().frame(iframe);
      
        await browser.findElement(By.id("introAgreeButton")).click()

        await browser.switchTo().defaultContent();
        await browser.findElement(By.name("q")).sendKeys("Carole Deumié", Key.ENTER);
      
      
        browser.takeScreenshot().then((data) => {
          fs.writeFileSync('img.png', data, 'base64')
        })
    }, 10000)
    
    afterEach(async () => {
        await browser.quit()
    })
})
~~~

Que l'on lance avec la commande : `yarn run test --testRegex="user-story.js"`

Testez le. Ca fait plein de trucs. Attention, c'est comme si vous faisiez une naviguation privée, auun cookie n'est placé. [La doc](https://www.selenium.dev/documentation/en/getting_started/) est très bien faite et explique beaucoup de choses. 

Les commandes `await` (et `async` que vous ne voyez pas là mais qui existent) permettent de gérer les événemnts asynchrones (le temps que la commande se fasse). C'est lié aux [Promises](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Utiliser_les_promesses). Regardez ce [tuto](https://www.grafikart.fr/tutoriels/promise-async-await-875) si vous voulez tout savoir sur les promesses (le tuto date un peu donc tout ce qu'il dit est maintenant implémenté dans les browser modernes. Vous pouvez le voir sur [ce site](https://caniuse.com/?search=async) par exemple).

Enfin, on a augmenté le temps disponible du second test à 10s.


#### tests en local

On ne va pas faire nos tests en production. On aimerait tout tester en local, comme nos tests unitaires. Pour l'instant on peut utiliser le protocole file des browser. 


*numerologie.user-story.js* :

~~~ js
/**
 * @jest-environment jest-environment-webdriver
 */

var fs = require('fs');

const url = "file://" + __dirname +'/../index.html'



describe('Le site fonctionne', () => {
  test('it renders', async () => {
    await browser.get(url)
    const title = await browser.getTitle()
    expect(title).toContain('Numérologie')
  })
})

~~~

#### pour notre site

Transformons notre user-story en test selenium.

TBD

## node

Nos allons enfin utiliser [node](https://nodejs.org/en/) sous la forme d'un serveur web.

On a souvent besoin d'un petit serveur web, en particulier pour la gestion des données. L'usage courant est de faire son appli front avec une bibliothèque front comme [vuejs](https://vuejs.org/) ou [react](https://fr.reactjs.org/) et de gérer les données via le serveur node (en utilsant une architecture [REST](https://fr.wikipedia.org/wiki/Representational_state_transfer) et/ou [graphql](https://graphql.org/)).


Cette partie sera décorrelée  du site front. On y reviendra lorsque l'on utilisera [express](https://expressjs.com/fr/), un module quasi indispensable pour créer des serveur web en node. On expliquera ici comment fonctionne node et son utilisation avec l'ovh.

### mon premier serveur node

On va le mettre dans le fichier *index.js* qui était là depuis le début dans le fichier *package.json*.

~~~ js

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
~~~

On exécute ce fichier en console : `node index.js`


Et on peut ensuite voir le résultat dans un navigateur à l'url : http://localhost:3000.

Le code précédent crée un serveur *http* qui répond toujours la même chose dès qu'on le contacte. Il affiche en log la requête reçue, qui elle dépend de l'url donnée.


Regardons le code de près :

  - `const` : déclaration de constantes. Changer port par exemple produit une erreur.
  - `require` : importation d'une bibliothèque  et affectation de celle-ci à une constante.
  - les fonctions peuvent se créer à la volée avec : `nomFonction((paramètres) => {})`
  - création d'un objet serveur avec une fonction ayant 2 paramètres, la requête et la réponse (voir [doc](https://nodejs.org/dist/latest-v14.x/docs/api/http.html#http_http_createserver_options_requestlistener)).
  - `listen` : lien entre le serveur et le couple adresse + port.


On peut afficher l'url de la requête : On récupère les variables *hostname* et *port* et on les affiche dans la console.
  
Détails, en utilisant la [documentation](https://nodejs.org/en/docs/) de nodejs :

  - `http` : C'est le module s'occupant des échanges et du codage des données.
  - `http.createServer` : demande un [`requestListener`](https://www.w3schools.com/nodejs/func_http_requestlistener.asp) qui est ajouté à l'événement request.
  - event request : deux paramètres `http.IncomingMessage`  et `http.ServerResponse`. Il est émit à chaque fois qu'un *request* est demandé
  - `http.IncomingMessage` a un attribut url : il sert à générer le *Readable Stream interface* et beaucoup d'autres choses (événements, méthodes, ...).

La [documentation](https://nodejs.org/api/) de nodejs est très bien faite. Trouvez tous les éléments mentionnés ci-dessus.


Tout est orienté autour d'évènements auxquels le serveur doit répondre.



### on regarde ce que ça donne sur l'ovh
 
 Le serveur est local. Pour l'exécuter sur l'ovh il va falloir faire des trucs.
 
#### ports
 
La configuration du serveur est la suivante : 

  - chaque étudiant a un certain nombre de ports alloués pour ses serveurs, un par techno. Les ports sont visibles dans le fichier *readme.txt* à la racine de votre site.
  - le nginx de l'ovh enverra toutes les requêtes arrivant pour l'adresse `node.herbe.ovh1.ec-m.fr` (où *herbe* est votre herbe) à `127.0.0.1:port` (où *pour* est votre port)
  
La conf du [nginx](https://www.nginx.com/) ([un petit tuto](https://www.grafikart.fr/tutoriels/nginx-692)) est : 

  1. chargée lors du lancement du démon et est le fichier */etc/nginx.conf*
  2. ce fichier charge tous les fichiers de */etc/nginx/conf.d/\*.conf*
  3. regardons celui appelé *nodejs.conf* :
    - il regarde la liste des port par herbe
    - et envoie toutes les requêtes sur le démon qui écoute le port de votre herbe
    - il n'envoie cependant pas les adresse qui commencent par `/static` qui eux sont traitées directement en cherchant un fichier dans le dossier *static/* du `root` de cette configuration : `/home/$user/node`.

#### exemple d'organisation

dans le dossier `~/node`

  - un fichier *index.js* qui va contenir notre serveur
  - un dossier static contenant une image `img.png`
  
Par défaut l'adresse `http://node.herbe.ovh1.ec-m.fr` ne rend rien, juste un [502](https://http.cat/502).

Lançons notre serveur ! (mais pas trop loin) : `node index.js` :

  - Maintenant l'adresse fonctionne et nous accueille avec un `Hello World` bien mérité.
  - `http://node.herbe.ovh1.ec-m.fr/static/img.png` fonctionne aussi.


Sauf qu'en se déconnectant, le terminal et tous ses process attachés disparaissent, dont notre serveur.

En revanche, l'adresse  `http://node.herbe.ovh1.ec-m.fr/static/img.png` continue de fonctionner puisqu'elle n'est pas dépendante du serveur node...

#### le démon

On va utiliser la commande [screen](https://linuxize.com/post/how-to-use-linux-screen/) qui nous permet de détacher des process. Elle possède pleins de paramètres mais, pour nous, on va exécuter le screen avec la commande : `/usr/bin/screen -d -m -S node node index.js` :

  - -S : When creating a new session, this option can be used to specify a meaningful name for the session. This name  identifies
            the session for "screen -list" and "screen -r" actions. It substitutes the default [tty.host] suffix.
  - -d -m :  Start  screen  in  "detached"  mode.  This  creates a new session but doesn't attach to it. This is useful for system startup scripts.


Après la commande, l'adresse `http://node.herbe.ovh1.ec-m.fr` répond, et on peut se déconnecter, ça marche toujours.

Le process `screen` est détaché de notre shell et reste donc effectif après déconnection. On le retrouve en regardant tous nos processes : `ps aux | grep herbe`. On retrouve le process *screen*. On va le tuer et voir ce qu'il se passe : `kill numero_du_process` (le premier numéro). Le serveur a disparu et le process aussi.

Relançons le : `/usr/bin/screen -d -m -S node node index.js`. On peut manager ses process screen sans avoir beoin de les tuer sauvagement avec [kill](https://korben.info/commande-kill-linux-tuer-processus.html) :

  - `screen -ls` : trouve les différents screen
  - `screen -X -S [nom de la session à tuer, pour nous node] quit` : tue le screen


#### conf d'un app node

  - front dans `~/node/static/`. Les fichiers html, css de l'app mais aussi ses node_modules. Le mieux est de faire un lien de votre dossier front vers *static*
  - back dans le dossier `~ /node/` avec ses fichiers js, mais aussi ses templates si vous en avez et son dossier node_module


### Globaux et Asynchrones

Node est un interpréteur javascript, mais sa grande force est dans ses modules et son fonctionnement purement asynchrone :

> Lorsque cet évènement se produit ou lorsque j'ai fini de faire quelque chose, j'exécute une fonction.

Par exemple, on utilise la méthode `setInterval` utilisable par défaut en node car définit dans https://nodejs.org/api/globals.html


~~~ js
function affiche_bloup() {
    console.log("bloup")
}

var timer1 = setInterval( affiche_bloup, 1000) // un intervalle

var timer2 = setInterval(function() { // un deuxième avec une function anonyme
    console.log("bim")
}, 2000)
~~~

Tout est asynchrone, lorsque la condition est vérifiée la fonction est exécutée. On peut donc en ajouter plusieurs sans problème.

### les routes

Le but d'un serveur web est de répondre à des requêtes (une url). Cette réponse peut être beaucoup de choses (défini dans son [type mime](https://developer.mozilla.org/fr/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types) qui permet au navigateur de savoir ce que c'est), les plus courantes étant du html ou des données aux format json (le reste étant souvent des fichiers statiques). 

Nodejs gère les routes de façon assez frustre, nous utiliserons ensuite  [expressjs](https://expressjs.com/fr/) pour gérer tout ça de façon plus simple. Mais voici un exemple avec 3 routes (une où la réponse est directe, une qui charge un fichier local et une qui charge un fichier distant) et un 404 : 

~~~ js
var http = require('http')
var fs = require('fs')

var server = http.createServer((request, response) =>{
    response.statusCode = 200;
    response.setHeader('Content-Type', 'text/html');

    if (request.url === "/" || request.url === "/home") {
        response.writeHead(200,  {'Content-Type': 'text/html'})
        var readStream = fs.createReadStream(__dirname + "/index.html", "utf8")
        readStream.pipe(response)
    }
    else if (request.url === "/contact") {
        response.end("<html><head><title>contact</title></head><body><h1>contact</h1></body></html>");
    }
    else if (request.url === "/lecture") {
        response.statusCode = 200;
		response.setHeader('Content-Type', 'text/plain');
	
        http.get("http://www.gutenberg.org/files/4300/4300-0.txt", (response_get) => {
            response_get.setEncoding('utf8');
            response_get.pipe(response)
        })
    } 
    else {
        response.statusCode = 404;
        response.setHeader('Content-Type', 'text/plain');
        response.end();
    }
})

server.listen(3000, 'localhost')
console.log("c'est parti")
~~~

Notez comment un fichier local et distant sont chargés. En particulier comment la réponse du ficher distant est rendue immédiatement. Ceci permet de donner une réponse même si tout n'est pas chargé.

## express 

La gestion de différentes routes est malaisée en node pure, on se perd vite dans tous ces else/if. C'est pourquoi on va utiliser la bibliothèque [expressjs](https://expressjs.com/fr/) à notre projet back : `yarn add express`


### les requêtes en express

Comme toute bibliothèque node pour l'utiliser on utilise `require` :

~~~ js
var express = require('express')
var app = express()
~~~

Notez que l'import est une fonction, ce qui permettrait de passer des paramètres à l'app express si besoin.

Tout va maintenant passer via l'objet `app`. Chaque requête va passer dans les appels successifs jusqu'à être *"consommée"*. 

On utilisera essentiellement quatre méthodes de `app` :

  - `app.set()` : qui s'occupe des paramètres de express,
  - `app.use()` : qui reçoit toutes les requêtes
  - `app.get()`, `app.post()` : qui reçoivent respectivement les requêtes http get et post.

Avant d'expliquer comment tout ça se passe, regardons un exemple en recréant un fichier *index.js* utilisant express dans notre projet : 

~~~ js

var express = require('express')
var app = express()

app.use(function (req, res, next) {
    console.log('Time:', Date.now());
    next(); // sans cette ligne on ne pourra pas poursuivre.
})



app.get('/', (request, response) => {
    response.statusCode = 200;
    response.setHeader('Content-Type', 'text/html');

    response.end("<html><head><title>index</title></head><body><h1>Hello world</h1></body></html>");
})

app.use(function (req, res, next) {
    console.log("ensuite");
    next(); // sans cette ligne on ne pourra pas poursuivre.
})

app.get('/contact', (request, response) => {
    response.statusCode = 200;
    response.setHeader('Content-Type', 'text/html');

    response.end("<html><head><title>contact</title></head><body><h1>contact</h1></body></html>");
})

app.use(function (request,response) {
    console.log("et c'est le 404");
    
    response.statusCode = 404;
    response.setHeader('Content-Type', 'text/html');

    response.end("<html><head><title>quatre cent quatre</title></head><body><h1>404</h1></body></html>");
    
})

app.listen(3000);
console.log("c'est parti")
~~~

Lorsque vous exécutez votre code vous voyez des choses qui s'affichent dans la console :

  - *"Time"* s'affiche à chaque appel
  - *"ensuite"* ne s'affiche que si notre requête est différente de '/'
  - *"et c'est le 404"* s'affiche si l'on demande une url différente de `/` ou `contact`

Ceci s'explique par les différentes manières dont peuvent s'appeler les méthodes de `app` :

  - un unique paramètre qui est une `fonction(request, response)` :
      
  - un unique paramètre qui est une `fonction(request, response, next)`
  - deux paramètres un premier qui est un *"filtre à requête* (`get` dans l'exemple) et le second la fonction à 2 ou 3 paramètres.

Les deux ou trois paramètres de la requetes sont des objets qui permettent de gérer :

  - la [requête](https://expressjs.com/fr/api.html#req) (paramètre `request`) qui permet de tout savoir sur la requête,
  - la [réponse](http://expressjs.com/fr/api.html#res) (paramètre `response`) qui permet de gérer la réponse que va envoyer le serveur
  - lorsque l'on exécute ce paramètre, la requête est envoyé à la prochaine route possible (l'ordre est déterminé par l'ordre dans le quel ces routes sont écrites dans le code). S'il n'y a pas de paramètre `next` ou que la fonction n'est pas appelée, la requête est consommée : elle ne sera pas passé à d'autres routes.
  
>**Nota Bene : ** essayez d'enlever un next() n'une route pour voir l'effet que ça fait. Il faudra bien sur relancer le serveur avant que les modifications prennent effet.


### les fichiers statiques

On serait tenté de charger à la main chaque fichier : 

~~~ js
app.get('/', (request, response) => {
        response.sendFile(__dirname + "/static/index.html")
})
~~~

Mais ce n'est pas une bonne idée pour plusieurs raisons : 

  1. on ne sais pas combien de fichier statique on va avoir besoin, car ce n'est pas que les fichiers html, c'est aussi les images, les css, tous les fichiers js, etc. Bref il y en a beaucoup trop
  2. si l'on laisse node charger les fichiers statiques, on ajoute le délais de traitement des fichiers de node dans chaque traitmeent de la requête
  3. on ne peut pas gérer le cache web.
  
On laisse donc nginx gerer les fichiers statiques pour nous dans la configuration de l'ovh (regardez la doc) : toutes les requetes qui commencent par `/static` sont gérées immédiatement par nginx et ne passent même pas par le serveur node.

Mais en développement, à moins de simuler la production, on ne peut pas faire ça. Du coup, on ajoute un middleware dont le boulot est de gérer les fichiers statiques en simulant ce que ferait le nginx en production. 

On ajoute donc la ligne : 

~~~ js
app.use("/static", express.static(__dirname + '/static'))
~~~

Au début des routes.

## Notre site avec express

Pour l'instant pas de routes, que des fichiers statiques.  Ca va changer bientôt, mais pour l'instant on prépare le tout. 

  - Il va falloir créer un dossier *static* qui 
    - contiendra nos pages statiques
    - possédera un fichier *package.json* (et donc un dossier *node_modules*) pour toutes les bibliothèques front (ici purecss)
  - On épure le fichier *package.json* côté serveur pour qu'il ne possède plus que les bibliothèques nécessaires au back. 
  - mettre tous nos tests unitaires et de user stories dans un dossier *tests* (pas *__tests__* car par défaut tous les fichiers de ce dossier sont exécutés en tant que tests, et nous on veut séparer tests unitaires et tests de users stories).
  

Il faut un peu jardiner le code pour qu'il continue de fonctionner :
  
  - Il faut changer les chemin d'import des tests
  - il faut faire deux package.json (un pour le back et un pour le front) et procéder aux imports. Le plus simple est de supprimer les fichiers node_modules et de les laisser se recréer avec un `yarn install` côté front et côté back
  - il faut un peut changer la configuration de jest pour qu'il ne voit pas le dossier static et son *package.json*
  - On [redirige](https://expressjs.com/fr/api.html#res.redirect) la route `/` vers `static/index.html`.

On a alors une architecture qui ressemble à (commande `tree -I node_modules `) :

~~~
.
├── index.js
├── package.json
├── static
│   ├── index.html
│   ├── main.css
│   ├── main.js
│   ├── numerologie.js
│   ├── package.json
│   └── yarn.lock
├── tests
│   ├── numerologie.test.js
│   └── user-stories
│       ├── look-at-google.user-story.js
│       └── numerologie.user-story.js
└── yarn.lock

~~~

Avec le fichier *package.json* du back qui ressemble à :

~~~ 
{
  "name": "web_serveur",
  "version": "1.0.0",
  "main": "index.js",
  "repository": "git@github.com:FrancoisBrucker/web_serveur_cours.git",
  "author": "François Brucker <francois.brucker@centrale-marseille.fr>",
  "license": "MIT",
  "scripts": {
    "test": "jest",
    "user-story": "jest --testRegex=\"user-story.js\""
  },
  "devDependencies": {
    "selenium-webdriver": "^4.0.0-alpha.7",
    "geckodriver": "^1.20.0",
    "chromedriver": "85.0.1",
    "jest": "^26.5.0"
  },
  "dependencies": {
    "express": "^4.17.1"
  },
  "jest": {
    "modulePathIgnorePatterns": [
      "<rootDir>/static"
    ]
  }
}
~~~

> Notez la modification des paramètres de jest.

Et celui du du *static/package.json* qui ne contient plus que la dépendance purecss :

~~~ 
{
  "name": "web_serveur",
  "version": "1.0.0",
  "main": "index.html",
  "repository": "git@github.com:FrancoisBrucker/web_serveur_cours.git",
  "author": "François Brucker <francois.brucker@centrale-marseille.fr>",
  "license": "MIT",
  "dependencies": {
    "purecss": "^2.0.3"
  }
}

~~~

Enfin, le ficher *index.js* qui ne continent que gestion des fichiers statiques, une route (une redirection) et la gestion des 404 : 

~~~ js
var express = require('express')
var app = express()

app.use(function (req, res, next) {
    console.log('Time:', Date.now());
    next(); // sans cette ligne on ne pourra pas poursuivre.
})

app.use("/static", express.static(__dirname + '/static'))

app.get('/', (request, response) => {
    response
        .redirect(301, '/static/index.html')
})


app.use(function (request,response) {
    console.log("et c'est le 404 : " + request.url);

    response.statusCode = 404;
    response.setHeader('Content-Type', 'text/html');

    response.end("<html><head><title>la quatre cent quatre</title></head><body><h1>Et c'est la 404.</h1><img  src=\"https://www.leblogauto.com/wp-content/uploads/2020/04/Peugeot-404-1.jpg\" /></body></html>");

})

app.listen(3000);
console.log("c'est parti")

~~~

> **Nota Bene : ** On a mis du contenu dans la 404 (toute une famille).


## tests de routes

Pour être sur que notre serveur fonctionne, on va tester les routes qu'il produit. Ceci peut se faire avec un outil spécialisé comme [postman](https://www.postman.com/) ou une bibliothèque de test comme [supertest](https://github.com/visionmedia/supertest).

### postman

Très utile lorsque l'on veut tester nos routes en post (ce qui est dur/impossible à faire avec un navigateur), [postman](https://www.postman.com/) permet aussi de tester nos routes toute simple en get.

Attention, postman va vouloir vous enregistrer, mais ce n'est pas nécessaire. Il faut  juste bien lire toutes les petites lignes avant de cliquer. 

On commence par [télécharger le client](https://www.postman.com/downloads/). Lorsque vous le lancez il va vous ouvrir une fenêtre de login. Lisez la petite ligne tout en bas de la fenêtre pour*skip sign in*

Cliquez sur le *+* de la fenêtre pour ouvrir un testeur de requête. On choisit get et vous pouvez ensuite tester une route de votre serveur. Ces routes sont conservées dans l'historique pour pouvoir être réutilisées facilement ensuite. 

Si cette méthode est idéale en développementpour configurer une route récalcitrante, elle n'est pas recommandée pour faires des tests réguliers. Pour ça on va les automatiser avec la bibliothèque supertest.

### supertest

[supertest](https://github.com/visionmedia/supertest) est une bibliothèque permettant de tester facilement les routes. On commence par l'installer : `yarn add --dev supertest`


[un tuto](https://dev.to/nedsoft/testing-nodejs-express-api-with-jest-and-supertest-1km6)

On teste toutes les routes du serveur pour être sur de ne pas avoir de 404. Ce n'est pas la peine de tester l'algorithmie des routes s'il y en a, puisque ceci est fait avec des tests unitaires.


Pas une user story ni un test unitaire, on vérifie que nos routes sont ok.

Pour que supertest fonctionne, il faut pouvoir lancer le serveur à la volée ce qui est impossible actuellement puisque *index.js* crée les routes et lance le serveur tout seul. On sépare donc tout ça en deux fichiers. 

*app.js* qui crée les routes :

~~~ js
var express = require('express')
var app = express()

app.use(function (req, res, next) {
    console.log('Time:', Date.now());
    next(); // sans cette ligne on ne pourra pas poursuivre.
})

app.use("/static", express.static(__dirname + '/static'))

app.get('/', (request, response) => {
    response
        .redirect(301, '/static/index.html')
})


app.use(function (request,response) {
    console.log("et c'est le 404 : " + request.url);

    response.statusCode = 404;
    response.setHeader('Content-Type', 'text/html');

    response.end("<html><head><title>la quatre cent quatre</title></head><body><h1>Et c'est la 404.</h1><img  src=\"https://www.leblogauto.com/wp-content/uploads/2020/04/Peugeot-404-1.jpg\" /></body></html>");

})

module.exports = app

~~~

Et *index.js* qui ne fait que lancer le serveur :
~~~js
const app = require('./app');

config = {
    baseUrl: "localhost",
    port: 3000
}


app.listen(config.port, () => {
    console.log('server is running at: ' + 'http://' + config.baseUrl + ':' + config.port);
});

~~~

 Du coup nos tests de routes peuvent s'écrire par exemple (fichier *test/routes.test.js*) :
 
~~~ js

const request = require('supertest');

const app = require('../app');

let user;
let server;

beforeAll(async () => {
    user = await request.agent(app);
    server = await app.listen(3000);
});

afterAll(async () => {
    await server.close();
});


test('GET index.html', (done) => {
    user
        .get('/')
        .expect(301)
        .expect(function(res) {
            expect(res.headers.location).toBe('/static/index.html')
        })
        .end((err, res) => {
            if (err) {
                return done(err);
            }
            done()
        })
})

test('GET 404', (done) => {
    user
        .get('/not here')
        .expect(404)
        .end((err) => {
            done(err)
        })
})
 
~~~


On teste qu'il y a une redirection vers `/static/index/html` et que les 404 sont mis en œuvre.

## loggeur

Lorsqu'il y a une erreur sur un serveur distant, il est très rare qu'elle se produise alors que le développeur la regarde. Il faut donc pouvoir a posteriori retrouver ce qu'il s'est passé.

On va en utiliser deux : [morgan](https://github.com/expressjs/morgan) et [winston](https://github.com/winstonjs/winston).

### morgan

Le loggeur  [morgan](https://github.com/expressjs/morgan) permet d'intercepter toutes les requêtes http. Il permet de savoir exactement ce qu'il se passe sur notre serveur.

On l'ajoute en commençant par l'installer : `yarn add morgan`

  - on l'importe : `var morgan = require('morgan')`
  - puis on ajoute la ligne `app.use(morgan('dev'))` au début des routes pour l'utiliser.

Selon ce que l'on veut logger, il y a plein de possibilités, essayez par exemple `'combined'` ou `'tiny'` à la place de `'dev'` par exemple.


### winston

[winston](https://github.com/winstonjs/winston) permet lui de loggeur tout ce que l'on veut. L'idée est de **pouvoir** tout loger pour retrouver un bug, mais de ne pas tout stocker pour éviter d'avoir des fichiers de logs énorme et pour le coup non utile.

L’usage veut que l’on donne donc des niveaux de log et que ne sont stockés que les log de niveau inférieur à un seuil donné. Pour winston les logging levels sont :

~~~ js
const levels = { 
  error: 0,
  warn: 1,
  info: 2,
  http: 3,
  verbose: 4,
  debug: 5,
  silly: 6
};
~~~ 

En production on pourra par exemple utiliser le level 0, en développement le 2 et en debug le 4.

Commençons par ajouter winston : `yarn add winston` 

Et créons un loggeur. Pour cela, on va créer un fichier *logger.js* et mettre notre configuration winston à l'intérieur. Ce fichier sera ensuite importé dans tous les fichiers nécessitant des logs. Comme l'import est fait avec un [require] ), ce sera le *même* loggeur qui sera utilisé partout (c'est ce qu'on appelle le [caching](https://nodejs.org/docs/latest/api/modules.html#modules_caching)).

Fichier *logger.js* :

~~~ js
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
      winston.format.timestamp(),
      winston.format.json()),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.Console(),
  ],
});

module.exports = logger
~~~

On a deux sorties, une dans la console pour (défini dans les options) tous les log de criticité inférieur à `'info'`  et dans un fichier pour toute les erreurs. 

Puis on l'importe dans *app.js* pour :

  - inclure les messages de morgan dans winston au level `http`

~~~ js
var express = require('express')
var app = express()

var morgan = require('morgan')

const logger = require('./logger')

app.use(morgan('dev', {stream: {write:(log) => {logger.http(log)}}}))

app.use("/static", express.static(__dirname + '/static'))

app.get('/', (request, response) => {
    response
        .redirect(301, '/static/index.html')
})


app.use(function (request,response) {

    response.statusCode = 404;
    response.setHeader('Content-Type', 'text/html');

    response.end("<html><head><title>la quatre cent quatre</title></head><body><h1>Et c'est la 404.</h1><img  src=\"https://www.leblogauto.com/wp-content/uploads/2020/04/Peugeot-404-1.jpg\" /></body></html>");

})

module.exports = app
~~~

Et enfin dans *index.js* pour un petit message au démarrage du serveur : 

~~~ js
const logger = require('./logger')
const app = require('./app');

config = {
    baseUrl: "localhost",
    port: 3000
}


app.listen(config.port, () => {
    logger.info('server is running at: ' + 'http://' + config.baseUrl + ':' + config.port);
});
~~~

Essayer de changer le level par défaut pour voir les messages de niveau http dans la console.


### winston daily rotate

[winston daily rotate](https://github.com/winstonjs/winston-daily-rotate-file) est un plugin winston qui permet de faire des log qui ne maintiennent qu'une durée fixe de log (une journée, semaine, etc) permettant ainsi aux logs de ne pas grossir indéfiniment.

Il existe aussi des outils unix pour cela, comme [logrotate](https://doc.ubuntu-fr.org/logrotate) par exemple (voir [tuto](https://medium.com/techiee/log-rotation-with-forever-6d8a1797355b)).


TBD

## transfert de données en post et fetch

Pour l'instant, le code js de calcul du nombre est inclus dans le front. On va le mettre dans une route. On va mettre ces nouvelles routes dans un fichier séparé.


### API et nouvelle route

On va créer une route commençant par `/api` qui contiendra notre appel à la fonction numérologie. 

L'usage veut également que l'on conserve les différentes versions des api pour pouvoir changer nos appels sans perturber les sites utilisant ceux-ci. On va donc avoir les routes suivantes : 

  - `/api/current/` qui sera la route pour la version actuelle de l'api 
  - `/api/v1/` qui sera un lien vers la version courante. 
  
Ceci nous permettra de maintenir la version `v1` de l'api lorsque la version courante changera en `v1.2` ou `v2`.
  
On aura aussi pour l'instant qu'une unique méthode : `numerologie/<prenom>` qui prend une chaîne de caractère en *"paramètre"*.
  
Construisons ces routes. Pour cela on crée des dossiers que l'on importera (importer un dossier revient à importer le fichier *index.js* qui s'y trouve). 

Notre site correspond maintenant à ça : 

~~~
├── app.js
├── error.log
├── index.js
├── logger.js
├── package.json
├── routes
│   ├── index.js
│   └── v1
│       └── index.js
├── static
│   ├── index.html
│   ├── main.css
│   ├── main.js
│   ├── numerologie.js
│   ├── package.json
│   └── yarn.lock
├── tests
│   ├── numerologie.test.js
│   ├── routes.test.js
│   └── user-stories
│       ├── look-at-google.user-story.js
│       └── numerologie.user-story.js
└── yarn.lock

~~~

On a ajouté un dossier *routes* contenant un fichier *index.js*. Ce fichier est importé dans *app.js*, juste avant la gestion des 404 avec 2 lignes : 

~~~js
var express = require('express')
var app = express()

var morgan = require('morgan')

const logger = require('./logger')

app.use(morgan('dev', {stream: {write:(log) => {logger.http(log)}}}))

app.use("/static", express.static(__dirname + '/static'))

app.get('/', (request, response) => {
    response
        .redirect(301, '/static/index.html')
})

api = require('./routes')
app.use('/api', api)


app.use(function (request,response) {

    response.statusCode = 404;
    response.setHeader('Content-Type', 'text/html');

    response.end("<html><head><title>la quatre cent quatre</title></head><body><h1>Et c'est la 404.</h1><img  src=\"https://www.leblogauto.com/wp-content/uploads/2020/04/Peugeot-404-1.jpg\" /></body></html>");

})

module.exports = app
~~~

Le fichier *index.js* contient le code suivant :

~~~js
var express = require('express');
var router = express.Router();

module.exports = router

router.use('/current', require('./v1'))
router.use('/v1', require('./v1'))

~~~

Son boulot est de créer (et de rendre) un router qui contient deux routes `/current` et `/v1` qui seront identiques. 

Le fichier *index.js* contient la route proprement dite de notre api. Pour l'instant c'est un fake. On fera le lien avec notre code js plus tard :

~~~ js
var express = require('express');
var router = express.Router();

module.exports = router

router.get('/numerologie/:prenom', (req, res) => {
    res.json({
        "prenom": req.params.prenom,
        "numero": 4,
    })
})

~~~

Remarquez que cette route prend un paramètre nommé `:prenom` que l'on peut ensuite reprendre and le code. 

Pour l'instant le code rend un objet [json](https://www.json.org/json-fr.html) contenant 2 champ, le prénom (le paramètre de notre route) et le code (pour l'instnant toujours 4) 

Pour savoir comment appeler cette route depuis notre server, regardons comment elle est appelée : 

  1. on commence par l'appeler depuis *./app.js* : `app.use('/api', api)` où `api = require('./routes')`
  2. cela continue dans *./routes/index.js* avec `router.use('/current', require('./v1'))` et `router.use('/v1', require('./v1'))`
  3. on arrive enfin au *./routes/v1/index.js* qui crée la route : `router.get('/numerologie/:prenom', ...`

En combinant tout ça on arrive à une route : `http://localhost:3000/api/current/numerologie/un truc` qui est la même que `http://localhost:3000/api/v1/numerologie/un truc`. Onpeut bien sur remplacer "un truc" par ce qu'on veut du moment que ce n'est pas vide.


### tests

On peut tester notre route directement dans un navigateur (puisque c'est une requête get), mais aussi avec postman. 

Remarquez que :

  - le corps de la réponse est notre objet json
  - le type (dans les header) est bien placé à json. C'est express qui a fait ça.
  

Ajoutons un test avec supertest en créant le fichier *./tests/routes.api.test.js* : 

~~~ js

const request = require('supertest');

const app = require('../app');

let user;
let server;

beforeAll(async () => {
    user = await request.agent(app);
    server = await app.listen(3000);
});

afterAll(async () => {
    await server.close();
});


test('GET /api/current/numerologie/François', (done) => {
    user
        .get('/api/current/numerologie/François')
        .expect(200)
        .expect(function(res) {
            expect(res.body).toMatchObject(
                {
                    "prenom": "François",
                    "numero": 8,
                }
            )
        })
        .end((err, res) => {
            if (err) {
                return done(err);
            }
            done()
        })
})


~~~

Pour l'instant notre test rate (puisque l'on ne rend que 4. Changez le 8 en 4 dans le test pour voir le test réussir), mais on va le faire marcher dans la suite.


### mise à jour du site 

#### côté back 

Commençons par faire marcher les tests. Pour cela, il faut rapatrier le fichier *static/numerologie.js* dans la racine du site et l'utiliser dans */routes/v1/numerologie.js* :

~~~js
var express = require('express');
var router = express.Router();

module.exports = router

const numerologie = require('../../numerologie')


router.get('/numerologie/:prenom', (req, res) => {
    res.json({
        "prenom": req.params.prenom,
        "numero": numerologie.nombre(req.params.prenom),
    })
})
~~~

Les tests doivent maintenant passer (si vous avez bien changé le path pour le require du test de numérologie). On ne fait pas de tests supplémentaire dans supertest, les tests unitaires de *numerologie.js* nous assurant que la fonction `numerologie.nombre` fonctionne.
#### côté front


Enfin, il faut modifier le fichier *static/main.js* pour qu'il cherche la réponse dans le serveur plutôt que par une fonction js. On utilise pour ça la fonction [fetch](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API/Using_Fetch), très pratique, qui permet de récupérer des choses sur internet avec des promesses :


~~~ js
function change_value() {
    prenom = document.querySelector("#prenom").value
    if (prenom) {
        fetch('/api/current/numerologie/' + prenom)
            .then(response => response.json())
            .then(data => {
                document.querySelector("#get-value").textContent = data.numero
                console.log(data)
            })
    } else {
        document.querySelector("#get-value").textContent = "?"
    }

}
change_value()

document.querySelector("#button-form").addEventListener("click", (event) => {
    change_value()
    event.preventDefault()
})

~~~


Regardez la console pour voir ce que reçoit le fetch : les données brutes sont d'abort converties en json avant d'être utilisées (c'est le double `then`) 

On oublie pas de modifier *static/index.html* pour supprimer les imports non nécessaires

~~~html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Numérologie</title>

        <link href="./node_modules/purecss/build/pure-min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
        <link href="main.css" rel="stylesheet">

    </head>
    <body>
        <div class="body">
            <form class="pure-form">
                <label for="prenom">Prénom :</label>
                <input id="prenom" type="text" name="prenom"/>

                <button id="button-form" type="submit" class="pure-button pure-button-primary">Envoi</button>
            </form>
            <div class="pure-g">
                <div class="pure-u-1-3"></div>
                <div class="pure-u-1-3"><p id="get-value">7</p></div>
                <div class="pure-u-1-3"></div>
            </div>

        </div>

        <script src="main.js"></script>
    </body>
</html>
~~~


## à faire ?
   - graphql ?

 - templating express ?
 - gestion des environnements de prod, test, etc
 - bases de données et requêtes post
 - compilation du front
 - gestion des routes dans des fichiers séparés
 
 

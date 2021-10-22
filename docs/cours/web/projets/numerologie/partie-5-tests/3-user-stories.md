---
layout: page
title:  "Projet numérologie : partie 5 / user stories"
category: cours
authors: 
    - "François Brucker"
    - "Yi Mei Jiang"
    - "Léo Laurent" 
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 5]({% link cours/web/projets/numerologie/partie-5-tests/index.md %}) / [user stories]({% link cours/web/projets/numerologie/partie-5-tests/3-user-stories.md %})
{: .chemin}

Les user stories sont de utilisations possibles du site. Elles dépendent souvent de [persona](https://fr.wikipedia.org/wiki/Persona_(marketing)), sorte d'utilisateurs idéaux, qui ont des besoins précis et identifiés.

Pour réaliser — et automatiser — ces tests, nous utiliserons la bibliothèque selenium qui permet de prendre le contrôle d'un navigateur.

## User Stories et Tests Fonctionnels

Le concept de User Story rejoint celui d'expérience utilisateur.  En effet il s’agit de comment on imagine que l’utilisateur va utiliser le produit, quel est le chemin qu’il va parcourir, surtout quel est le chemin qu’on veut qu’il parcoure. Définir une user story permet également de définir comment sera utilisé le site qu’on va écrire. 

Ici, on souhaite tester le comportement du site en fonction du parcours d'un utilisateur.
On doit donc réaliser des tests fonctionnels: On veut observer le résultat d'une séquence d'opérations complexes.

Pour cela, on va utiliser [Selenium](https://www.selenium.dev), un outil qui permet d’automatiser un navigateur web. On peut l’utiliser pour simuler un utilisateur, et donc vérifier que le site fonctionne comme il devrait d’un point de vue utilisateur.
C’est un outil très générique puisqu’il supporte de nombreux navigateurs, il est utilisable avec de nombreux langages également.

## Installation de Selenium

Selenium est écrit en Java, avant de l’utiliser assurez-vous d’avoir Java installé sur votre machine. Vous pouvez le faire en passant par l’installer [sdkman](https://sdkman.io).

Pour utiliser Selenium on va avoir besoin de plusieurs bibliothèques :

* ``selenium-webdriver``, la bibliothèque de Selenium proprement dit
* un navigateur web :
  * ``geckodriver`` pour firefox
  * ``chromedriver`` pour chrome

On peut les installer avec la commande : ``npm instal --save-dev selenium-webdriver chromedriver geckodriver``

## documentation

La [documentation officielle](https://www.selenium.dev/documentation/) est très précieuse. Il y a en effet plein de possiblités.

## exemples

### premier exemple

#### à la main {#un-eme-exemple-main}

On veut aller aller sur la page de google et vérifier que son titre contient *Google*

Tester ça avec une navigation privée sur chrome et firefox

> Remarquez qu'il y a une fenêtre sur laquelle cliquer pour accéder à la barre de recherche.

#### automatisé {#un-eme-exemple-selenium}

Créez un nouveau dossier *"numerologie/user-stories"*, puis un fichier : *"numerologie/user-stories/look-at-goole.user-story.js"* :

```js
var fs = require('fs');
const url = 'https://www.google.com'

const webdriver = require('selenium-webdriver');


beforeEach(() => {
    require('geckodriver');
    browser =  new webdriver.Builder().forBrowser('firefox').build()
})


test('it renders', async () => {
  await browser.get(url)
  const title = await browser.getTitle()
  expect(title).toContain('Google')
})

afterEach(async () => {
  await browser.quit()
})
```

On exécute le fichier avec jest :

```shell
npm test -- --testRegex="user-story.js"
```

La commande précédente exécute jest en cherchant tous les fichiers qui finissent par `user-story.js`.

> On a pas mis nos tests fonctionnels dans les recherche par défaut de jest car ils prennent trop de temps.

Si vous voulez utiliser google à la place de firefox, remplacez la fonction `beforeEach` par :

```js
beforeEach(() => {
  require('chromedriver');
  browser = new webdriver.Builder().forBrowser('chrome').build()
})
```

### deuxième exemple

#### à la main {#deux-eme-exemple-main}

On veut aller aller sur la page de google et :

1. cliquer sur le bouton *j'accepte*
2. rechercher *Carole Deumié*
3. prendre un screenshot

Tester ça avec une navigation privée sur chrome et firefox

#### automatisé {#deux-eme-exemple-selenium}

```js
var fs = require('fs');
const url = 'https://www.google.com'

const {By, Key} = require('selenium-webdriver');
const webdriver = require('selenium-webdriver');

beforeEach(() => {
    require('chromedriver');
    browser = new webdriver.Builder().forBrowser('chrome').build()
})

test('save a picture', async () => {
    // files saved in ./reports/screenshots by default
    await browser.get(url)
    await browser.findElement(By.id("L2AGLb")).click()
    await browser.switchTo().defaultContent();
    await browser.findElement(By.name("q")).sendKeys("Carole Deumié", Key.ENTER);
    
    browser.takeScreenshot().then((data) => {
        fs.writeFileSync('img.png', data, 'base64')
    })
}, 10000)

afterEach(async () => {
    await browser.quit()
})
```

> Incroyable, non ?

## comment ça marche

Pour réaliser des tests en ligne depuis un navigateur web, on utilise le WebDriver.
Celui-ci communique avec un driver dépendant du navigateur web qu'on souhaite utiliser.
Voici à quoi ressemble le code dans ce cas:

```js
var fs = require('fs');

const url = "url";

// On charge le webdriver
const webdriver = require('selenium-webdriver');

describe('Le site fonctionne', () => {
    beforeEach(() => { // Avant chaque test...
        require('geckodriver'); // On charge le driver
        browser =  new webdriver.Builder().forBrowser('firefox').build() // On ouvre le navigateur web
    })

  test('premier test', async () => {
      // Contenu du test
  });

  test('second test', async () => {
      // Contenu du test
  });

    afterEach(async () => { // Après chaque test...
        await browser.quit() // On ferme le navigateur
    })
});
```

Ici on a utilisé firefox et son driver associé geckodriver.
On peut de la même manière utiliser d'autres navigateurs comme Chromium, Edge, Opera...
Il suffit dans le code de changer les noms du driver et du navigateur.
Pour installer et utiliser d'autres drivers [consultez cette page](https://www.selenium.dev/documentation/fr/webdriver/driver_requirements/).

### Trouver un Élément Web

Pour naviguer sur le site, on recherche en général des éléments précis sur cette page avec lesquels interagir.
Pour trouver un élément sur une page web, on utilise `findElement`.

Cette fonction renvoie un objet WebElement qui représente un noeud de l'arbre DOM,
en prenant en argument un contexte de recherche.
Par exemple, la ligne suivante permet de trouver l'élément dont l'`id` est "introduction",
et de stocker cet objet dans la variable intro :

```js
const intro = driver.findElement(By.id("introduction")); 
```

*Pensez à charger le module `By` au début du fichier en rajoutant la ligne suivante :*

```js
const {By} = require('selenium-webdriver');
```

Ensuite, si on veut trouver un élément contenu dans l'objet intro (par exemple l'image d'`id` `"img-intro"`), on écrit :

```js
const imgIntro = intro.findElement(By.id("img-intro")); 
```

`findElements` renvoie une liste des éléments respectant les critères de recherche :

```js
const listLinks = intro.findElements(By.name("a")); 
```

On peut rechercher un Élément en fonction de divers sélecteurs grâce à `By`. En voici quelques-uns :

```js
// dont le nom est "a" (un lien):
const element = driver.findElement(By.name("a"));
// dont l'id est "truc":
const element = driver.findElement(By.id("truc"));
// possédant a minima les attributs css "#machin" et "bidule":
const element = driver.findElement(By.css("#machin bidule"));
```

De manière générale, il est conseillé de rechercher des éléments par leur `id` unique s'il existe,
ou par leurs sélecteurs CSS.
Cela évite de parcourir l'arbre DOM avec plusieurs recherches, ce qui prend plus de temps.

On peut aussi rechercher un élément en fonction de sa position par rapport à un autre élément :

```js
// Trouve un bouton en dessous de intro
const intro = driver.findElement(By.id("introduction"));
const button = await driver.findElement(withTagName("button")
                                        .below("intro"));
```

On utilise `withTagName` qui remplace `By.name`.
On peut rechercher :

* au dessus avec `.above`
* en dessous avec `.below`
* à gauche avec `.toLeftOf`
* à droite avec `.toRightOf`
* à moins de 50px avec `.near`

On peut utiliser plusieurs de ces sélecteurs en même temps :

```js
const button = await driver.findElement(withTagName("button")
                                        .above(By.id("introduction"))
                                        .toRightOf(By.cssSelector("#menu")));
```

### Réaliser des actions sur la page

Une fois qu'un élément est trouvé, on peut automatiser les actions de l'utilisateur sur le site.
Les exemples les plus fréquents sont :

```js
// Cliquer sur un bouton
await driver.findElement(By.name("button")).click();
// Remplir un champ et valider (penser à charger Key au début du fichier)
await driver.findElement(By.name('name')).sendKeys("Manu", Key.ENTER);
```

Des actions plus précises peuvent être faites
[à la souris](https://www.selenium.dev/documentation/fr/support_packages/mouse_and_keyboard_actions_in_detail/) 
comme [au clavier](https://www.selenium.dev/documentation/fr/webdriver/keyboard/).

### Quelques commandes utiles

Pour prendre une capture d'écran et l'enregistrer, on utilise :

```js
browser.takeScreenshot().then((data) => {
      fs.writeFileSync('img.png', data, 'base64')
    })
```

Certaines pages comme Google font apparaitre un popup dans une [iframe](https://developer.mozilla.org/fr/docs/Web/HTML/Element/iframe).
Dans ce cas, on doit utiliser `switchTo` pour accéder à son contenu :

```js
const iframe = browser.findElement(By.css('iframe')); // On trouve d'abord l'iframe

await browser.switchTo().frame(iframe); // On rentre dans l'iframe
// On fait ici nos actions / recherches dans l'iframe
await browser.switchTo().defaultContent(); // On sort de l'iframe
```

## user story

Pour notre site. On va exécuter du code en mode test (donc avec une base de donnée en mémoire). Après avoir ajouté les signification des chiffre, on veut tester la user story suivante :

1. je me connecte au site
2. je tape mon nom "François" puis s'appuie sur entré.
3. je remarque que mon nom est associé au chiffre 8 et que des projets, j'en ai toujours en pagaille.
4. Je vais ensuite sur la page des prénoms et je vérifie que j'ai bien mon nom qui est affiché.

Il va falloir lancer notre site dans un mode spécial, pour que nos tests puissent accéder à la base de donnée. On crée donc un nouvel environnement, et on modifie *"numerologie/db.js"* pour qu'il le prenne compte :

```js
//...

if (env == 'test') {
  sequelize = new Sequelize('sqlite::memory:');
} else if (env == "test-user-stories")
  sequelize = new Sequelize({
    dialect: 'sqlite',
    storage: path.join(__dirname, 'db-test-user-stories.sqlite')
  });

else {
  sequelize = new Sequelize({
    dialect: 'sqlite',
    storage: path.join(__dirname, 'db.sqlite')
  });
}

//...
```

Une fois cet environnement réalisé, on initialise la base :

sous mac ou unix :

```shell
NODE_ENV='test-user-stories' node db-init.js
```

sous powershell  :

```shell
$env:NODE_ENV='test-user-stories' ; node db-init.js
```

Puis on peut ensuite exécuter notre serveur :

sous mac/unix :

```shell
NODE_ENV='test-user-stories' npm start
```

sous powershell  :

```shell
$env:NODE_ENV='test-user-stories' ; npm start
```

> on peut aussi lier les deux instruction par un `;` : sous mac/unix : `NODE_ENV='test-user-stories' node db-init.js ; NODE_ENV='test-user-stories' npm start` et sous windows : `$env:NODE_ENV='test-user-stories' ; node db-init.js ; npm start`

Enfin, dans un nouveau terminal, on lance notre nouveau test qu'on a placé dans le fichier *"numerologie/user-stories/ajout-prenom.user-story.js"* :

```js

const { By, Key } = require('selenium-webdriver');
const webdriver = require('selenium-webdriver');

process.env.NODE_ENV = 'test-user-stories'
const db = require('../db')

beforeAll(async () => {
  await db.sequelize.sync()
})

beforeEach(() => {
  require('chromedriver');
  browser = new webdriver.Builder().forBrowser('chrome').build()
})


test('mon prénom', async () => {
  await browser.get("http://127.0.0.1:3000/")

  
  await browser.findElement(By.id("form-input")).sendKeys("François", Key.ENTER)
  
  text = await browser.wait(browser.findElement(By.id("message")).getText(), 5000)

  expect(text).toContain("Des projets, vous en avez toujours en pagaille")

  await browser.get("http://127.0.0.1:3000/static/prenoms.html")
  expect(await browser.findElement(By.css("li")).getText()).toContain("François")
}, 10000)

afterEach(async () => {
  await browser.quit()
})
```

Il est souvent nécessaire d'ajouter des temps d'attente pour laisser le browser réagir. On a mis ici un [temps d'attente explicite](https://www.selenium.dev/fr/documentation/webdriver/waits/#explicit-wait) pour laisser au browser le temps de réagir à la fin de la requête : on attend que la méthode `getText()` rende une valeur non nulle, et on attend au pire 10s.

> Si on veut attendre de façon certaine, 2s par exemple, on peut utiliser une fonction qui rend toujours faux : `await browser.wait(() => false, 2000)`

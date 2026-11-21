---
layout: layout/post.njk

title: "Projet numérologie : partie 5 / tests utilisateurs"
authors: 
    - "François Brucker"
    - "Yi Mei Jiang"
    - "Léo Laurent" 

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

User stories.

<!-- fin résumé -->

Lorsque l'on fabrique un site, on a envie de l'utiliser d'une certaine manière, de pouvoir naviguer et récupérer des informations. On peut regrouper ces utilisations en  petites saynètes d'utilisation
appelées *user stories* ou *test fonctionnels*. Elles dépendent souvent de [persona](https://fr.wikipedia.org/wiki/Persona_(marketing)), sorte d'utilisateurs idéaux, qui ont des besoins précis et identifiés.

Le but est de tester que les intentions d'un utilisateurs peuvent être satisfaites. C'est un enchaînement de tests fonctionnels qui racontent une histoire d'**un** utilisateur voulant réaliser **une** tache sur notre application/site.

Comme toujours, on va automatiser ce processus en utilisant un script qui fera les manipulation et vérifiera le résultat pour nous.

## User Stories et Tests Fonctionnels

Le concept de User Story rejoint celui d'expérience utilisateur.  En effet il s’agit de comment on imagine que l’utilisateur va utiliser le produit, quel est le chemin qu’il va parcourir, surtout quel est le chemin qu’on veut qu’il parcoure. Définir une user story permet également de définir comment sera utilisé le site qu’on va écrire.

Ici, on souhaite tester le comportement du site en fonction du parcours d'un utilisateur.
On doit donc réaliser des tests fonctionnels: On veut observer le résultat d'une séquence d'opérations complexes.

Pour cela, on va utiliser [Selenium](https://www.selenium.dev), un outil qui permet d’automatiser un navigateur web. On peut l’utiliser pour simuler un utilisateur, et donc vérifier que le site fonctionne comme il devrait d’un point de vue utilisateur.
C’est un outil très générique puisqu’il supporte de nombreux navigateurs, il est utilisable avec de nombreux langages également.

## Selenium

[Selenium](https://www.selenium.dev/) est une bibliothèque permettant de contrôler les actions d'un navigateur.

{% lien %}
La [documentation officielle](https://www.selenium.dev/documentation/) est très précieuse. Il y a en effet plein de possibilités.
{% endlien %}

### Installation

Pour utiliser selenum il nous [faudra installer](https://www.selenium.dev/documentation/webdriver/getting_started/) :

* `selenium-webdriver`, la bibliothèque de Selenium proprement dit
* un navigateur web :
  * `geckodriver` pour firefox
  * `chromedriver` pour chrome

```
npm instal --save-dev selenium-webdriver chromedriver geckodriver
```

Il faut que vous ayez :

* les navigateurs Firefox et Chrome d'installés
* java pour selenium

> TBD : sûr que java est nécessaire ?

## Exemples

Nous allons placer nos exemple dans un dossier nommé `__usr-stories__`{.fichier}

### Ouvrir une fenêtre google

On veut aller aller sur la page de google et vérifier que son titre contient `"Google"`{.language-}

{% faire %}

1. ouvrez une nouvelle fenêtre
2. tapez <https://www.google.fr>
3. vérifiez que le titre de la fenêtre contient `"Google"`{.language-}

{% endfaire %}

Testez la user story *"à la main"* :

1. dans une fenêtre normale
2. dans une fenêtre de navigation privée

Remarquez qu'il y a une fenêtre sur laquelle cliquer pour accéder à la barre de recherche lorsque l'on utilise une fenêtre de navigation privée. Il faut en tenir compte lors de nos tests automatisés c'est ce que l'on va avoir.

Test automatisé dans le fichier : `__user-stories__/look-at-goole.js`{.fichier} :

```js#
const url = 'https://www.google.com'

import webdriver from 'selenium-webdriver';

import 'geckodriver';
let browser;

beforeEach(() => {
    browser =  new webdriver.Builder().forBrowser('firefox').build()
})


test('it renders', async () => {
  await browser.get(url)
  const title = await browser.getTitle()
  expect(title).toContain('Google')
})

afterEach(async () => {
  await browser.quit()
}, 10000)
```

{% info %}
NOtez le 10000 à la fin du test qui donne 10secondes au test pour s'exécuter. Par défaut, jest donne 5 secondes, ce qui est souvent insuffisant pour des tests selenium.
{% endinfo %}

On exécute le fichier avec jest :

```
npm test -- --testRegex='__user-stories__/look-at-google.js'
```

{% info %}
Notez que le `--` permet d'ajouter des arguments à la commande.
{% endinfo %}

{% attention %}
Pour exécuter tous les fichier d'un dossier, il faut des paramètres différents :

```
npm test -- --testMatch='**/__user-stories__/**/*.js'
```

{% endattention %}

On a pas mis nos tests fonctionnels dans les recherches par défaut de jest car ils prennent trop de temps.

Si vous voulez utiliser Chrome à la place de Firefox, remplacez les lignes :

* 5 par `import 'chromedriver';` {.language-}
* 9 par `browser = new webdriver.Builder().forBrowser('chrome').build()`{.language-}

### Faire une recherche google

On veut réellement utiliser google dans notre user story :

{% faire %}

1. ouvrez une nouvelle fenêtre
2. tapez <https://www.google.fr>
3. cliquer sur le bouton *j'accepte*
4. rechercher *Carole Deumié*
5. prendre un screenshot

{% endfaire %}

Testez la user story *"à la main"*  dans une fenêtre de navigation privée

Fichier : `__user-stories__/recherche-goole.js`{.fichier} :

```js
import fs from 'fs';

const url = 'https://www.google.com'

import webdriver from 'selenium-webdriver';
import { By, Key } from 'selenium-webdriver';

// import 'geckodriver';
import 'chromedriver';

let browser;

beforeEach(() => {
  // browser = new webdriver.Builder().forBrowser('firefox').build()
  browser = new webdriver.Builder().forBrowser('chrome').build()
})


test('sauve un screenshot', async () => {

  await browser.get(url)
  await browser.findElement(By.id("L2AGLb")).click()
  await browser.switchTo().defaultContent();
  await browser.findElement(By.name("q")).sendKeys("Carole Deumié", Key.ENTER);

  // await browser.manage().setTimeouts( { implicit: 5000 } );

  browser.takeScreenshot().then((data) => {
    fs.writeFileSync('img.png', data, 'base64')
  })
}, 20000)

afterEach(async () => {
  await browser.quit()
})

```

> [Étonnant, non ?](https://www.youtube.com/watch?v=NzxejXTumLQ)

## Fonctionnement de selenium

Pour réaliser des tests en ligne depuis un navigateur web, on utilise le WebDriver.
Celui-ci communique avec un driver dépendant du navigateur web qu'on souhaite utiliser.
Voici à quoi ressemble le code dans ce cas:

```js
var fs = require('fs');

const url = "url";

// On charge le webdriver
import webdriver from 'selenium-webdriver';

// On charge le driver
import 'chromedriver'; 

describe('Le site fonctionne', () => {
    beforeEach(() => { // Avant chaque test...
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

Ici on a utilisé Chrome et son driver associé `'chromedriver'`{.language-}. On peut de la même manière utiliser d'autres navigateurs comme Firefox, Edge, Opera...
Il suffit dans le code de changer les noms du driver et du navigateur.

{% lien %}
Pour installer et utiliser d'autres drivers [consultez cette page](https://www.selenium.dev/documentation/fr/webdriver/driver_requirements/).
{% endlien %}

### Trouver un Élément Web

Pour naviguer sur le site, on recherche en général des éléments précis sur cette page avec lesquels interagir.
Pour trouver un élément sur une page web, on utilise `findElement`{.language-}.

Cette fonction renvoie un objet WebElement qui représente un noeud de l'arbre DOM,
en prenant en argument un contexte de recherche.
Par exemple, la ligne suivante permet de trouver l'élément dont l'`id` est "introduction",
et de stocker cet objet dans la variable intro :

```js
const intro = driver.findElement(By.id("introduction")); 
```

Pensez à charger le module `By` au début du fichier en rajoutant la ligne suivante :

```js
import {By} from 'selenium-webdriver';
```

Ensuite, si on veut trouver un élément contenu dans l'objet intro (par exemple l'image d'`id` `"img-intro"`), on écrit :

```js
const imgIntro = intro.findElement(By.id("img-intro")); 
```

`findElements`{.language-} renvoie une liste des éléments respectant les critères de recherche :

```js
const listLinks = intro.findElements(By.name("a")); 
```

On peut rechercher un Élément en fonction de divers sélecteurs grâce à `By`{.language-}. En voici quelques-uns :

```js
// dont le nom est "a" (un lien):
const element = driver.findElement(By.name("a"));
// dont l'id est "truc":
const element = driver.findElement(By.id("truc"));
// possédant a minima les attributs css "#machin" et "bidule":
const element = driver.findElement(By.css("#machin bidule"));
```

De manière générale, il est conseillé de rechercher des éléments par leur `id`{.language-} unique s'il existe,
ou par leurs sélecteurs CSS.
Cela évite de parcourir l'arbre DOM avec plusieurs recherches, ce qui prend plus de temps.

On peut aussi rechercher un élément en fonction de sa position par rapport à un autre élément :

```js
// Trouve un bouton en dessous de intro
const intro = driver.findElement(By.id("introduction"));
const button = await driver.findElement(withTagName("button")
                                        .below("intro"));
```

On utilise `withTagName`{.language-} qui remplace `By.name`{.language-}.
On peut rechercher :

* au dessus avec `.above`{.language-}
* en dessous avec `.below`{.language-}
* à gauche avec `.toLeftOf`{.language-}
* à droite avec `.toRightOf`{.language-}
* à moins de 50px avec `.near`{.language-}

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

{% lien %}
Des actions plus précises peuvent être faites
[à la souris](https://www.selenium.dev/documentation/fr/support_packages/mouse_and_keyboard_actions_in_detail/)
comme [au clavier](https://www.selenium.dev/documentation/fr/webdriver/keyboard/).
{% endlien %}

### Quelques commandes utiles

Pour prendre une capture d'écran et l'enregistrer, on utilise :

```js
browser.takeScreenshot().then((data) => {
      fs.writeFileSync('img.png', data, 'base64')
    })
```

Certaines pages comme Google font apparaître un popup dans une [iframe](https://developer.mozilla.org/fr/docs/Web/HTML/Element/iframe).
Dans ce cas, on doit utiliser `switchTo`{.language-} pour accéder à son contenu :

```js
const iframe = browser.findElement(By.css('iframe')); // On trouve d'abord l'iframe

await browser.switchTo().frame(iframe); // On rentre dans l'iframe
// On fait ici nos actions / recherches dans l'iframe
await browser.switchTo().defaultContent(); // On sort de l'iframe
```

### Faire une pause

Utile pour debugger le code en ajoutant une pause :

```js
await new Promise(r => setTimeout(r, 2000));
```

## User story

On veut tester la user story suivante :

{% faire %}

1. je me connecte au site
2. je tape le nom "Carole" puis j'appuie sur entré.
3. je remarque que ce nom est associé au chiffre 4 et que la spontanéité, ce n'est pas son truc.
4. Je vais ensuite sur la page des prénoms et je vérifie que j'ai bien "Carole" qui est affiché.

{% endfaire %}

On veut exécuter le test en mode test pour ne pas polluer la base de donnés. Il faut donc :

1. exécuter le serveur en mode test : `NODE_ENV=test npm start` (ou `$env:NODE_ENV=test; npm start` sous powershell)
2. ajouter à la base de test le message associé au chiffre 4 (celui des "Carole")

On commence donc par ajouter les lignes suivante dans le fichier `db.js`{.fichier} pour ajouter un message à la base :

```js
// ...

if (env === "test") {
  await sequelize.sync({force: true})
  await signification(sequelize).sync({force: true})
  await prénoms(sequelize).sync({force: true})

  await signification(sequelize).create({
    message: "La spontanéité, ce n'est pas votre truc. Dans votre vie, tout doit être rangé, organisé, planifié, sinon c'est la panique ! Au travail, les responsabilités vous font peur : vous préférez vous mettre au service d'un supérieur plutôt que de prendre les commandes. Votre prudence naturelle vous pousse à ne pas vous aventurer en terrain inconnu...",
    nombre: 4,
  })
}

// ...
```

Puis la user storyFichier `__user-stories__/ajout-prénom.js`{.fichier} :

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

{% info %}
On devrait en toute logique exécuter notre site en mode test pour ne pas polluer la base de données.

On ne peut cependant pas le faire directement ici, car la base serait vide, sans messages associé aux chiffres. Il faudrait ajouter le message associé au chiffre 4 à la base avant de commencer proprement le test.
{% endinfo %}

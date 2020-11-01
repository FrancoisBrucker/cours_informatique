---
layout: page
title:  "Selenium"
category: cours
tags: combat web
authors: 
  - "Jiang Yi Mei"
  - "Laurent Léo"
---

## User Stories et Tests Fonctionnels

Le concept de User Story rejoint celui d'expérience utilisateur.  En effet il s’agit de comment on imagine que l’utilisateur va utiliser le produit, quel est le chemin qu’il va parcourir, surtout quel est le chemin qu’on veut qu’il parcoure. Définir une user story permet également de définir comment sera utilisé le site qu’on va écrire. 

Pour tester notre code, on a déjà vu les [tests unitaires] qui permettent de vérifier que des petites portions du code fonctionnent correctement. 
Ici, on souhaite tester le comportement du site en fonction du parcours d'un utilisateur. 
On doit donc réaliser des tests fonctionnels: On veut observer le résultat d'une séquence d'opérations complexes.

Pour cela, on va utiliser [Selenium](https://www.selenium.dev), un outil qui permet d’automatiser un navigateur web. On peut l’utiliser pour simuler un utilisateur, et donc vérifier que le site fonctionne comme il devrait d’un point de vue utilisateur. 
C’est un outil très générique puisqu’il supporte de nombreux navigateurs, il est utilisable avec de nombreux langages également. 

## Installation de Selenium

Selenium est écrit en Java, avant de l’utiliser assurez-vous d’avoir Java installé sur votre machine. Vous pouvez le faire en passant par l’installer [sdkman](https://sdkman.io).

Pour bien prendre en main selenium, faisons quelques tests\
[Doc de Selenium](https://www.selenium.dev/documentation/en/).


## Petite recherche sur Google

Pour commencer, voici un petit exemple de fichier de test selenium. 
Créez un fichier *look-at-google.user-story.js* et mettez-y le code ci-dessous :  
~~~js
var fs = require('fs');
const url = 'https://www.google.com'

const {By, Key} = require('selenium-webdriver');
const webdriver = require('selenium-webdriver');

describe('Google renders', () => {
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

Ce code va sur Google et teste les User Stories suivantes:
- Le site s'affiche
- L'utilisateur peut faire une recherche de mots clés sur le site 

En plus de cela, le second test prend une photo à la fin des actions et l'enregistre dans *img.png*.
Vous allez apprendre ici à créer un fichier du même genre, mais pour votre propre site.

## Structure de base du fichier de test

Voyons comment créer votre premier fichier de test selenium.
La base du fichier doit ressembler à ça :

~~~js
var fs = require('fs');

const url = "url";

describe('Le site fonctionne', () => {

  test('premier test', async () => {
      // Contenu du test
  });

  test('second test', async () => {
      // Contenu du test
  });
});
~~~

Dans la variable url, on met le lien vers la page de départ de notre test.
On peut réaliser des tests en local. Par exemple pour partir du fichier *index.html*, on utilise :

~~~js
const url = "file://" + __dirname +'/../index.html'
~~~

Pour réaliser des tests en ligne depuis un navigateur web, on utilise le WebDriver.
Celui-ci communique avec un driver dépendant du navigateur web qu'on souhaite utiliser.
Voici à quoi ressemble le code dans ce cas:

~~~js
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
~~~

Ici on a utilisé firefox et son driver associé geckodriver.
On peut de la même manière utiliser d'autres navigateurs comme Chromium, Edge, Opera...
Il suffit dans le code de changer les noms du driver et du navigateur.
Pour installer et utiliser d'autres drivers [consultez cette page](https://www.selenium.dev/documentation/fr/webdriver/driver_requirements/).

## Trouver un Élément Web

Pour naviguer sur le site, on recherche en général des éléments précis sur cette page avec lesquels interagir.
Pour trouver un élément sur une page web, on utilise `findElement`.

Cette fonction renvoie un objet WebElement qui représente un noeud de l'arbre DOM,
en prenant en argument un contexte de recherche.
Par exemple, la ligne suivante permet de trouver l'élément dont l'id est "introduction", 
et de stocker cet objet dans la variable intro :
~~~js
const intro = driver.findElement(By.id("introduction")); 
~~~
*Pensez à charger le module `By` au début du fichier en rajoutant la ligne suivante :*
~~~js
const {By} = require('selenium-webdriver');
~~~

Ensuite, si on veut trouver un élément contenu dans l'objet intro (par exemple l'image d'id "img-intro"), on écrit :
~~~js
const imgIntro = intro.findElement(By.id("img-intro")); 
~~~

`findElements` renvoie une liste des éléments respectant les critères de recherche :
~~~js
const listLinks = intro.findElements(By.name("a")); 
~~~

On peut rechercher un Élément en fonction de divers sélecteurs grâce à `By`. En voici quelques-uns:
~~~js
// dont le nom est "a" (un lien):
const element = driver.findElement(By.name("a"));
// dont l'id est "truc":
const element = driver.findElement(By.id("truc"));
// possédant a minima les attributs css "#machin" et "bidule":
const element = driver.findElement(By.css("#machin bidule"));
~~~

De manière générale, il est conseillé de rechercher des éléments par leur id unique s'il existe,
ou par leurs sélecteurs CSS.
Cela évite de parcourir l'arbre DOM avec plusieurs recherches, ce qui prend plus de temps.

On peut aussi rechercher un élément en fonction de sa position par rapport à un autre élément:
~~~js
// Trouve un bouton en dessous de intro
const intro = driver.findElement(By.id("introduction"));
const button = await driver.findElement(withTagName("button")
                                        .below("intro"));
~~~
On utilise `withTagName` qui remplace `By.name`.
On peut rechercher:
- au dessus avec `.above`
- en dessous avec `.below`
- à gauche avec `.toLeftOf`
- à droite avec `.toRightOf`
- à moins de 50px avec `.near`

On peut utiliser plusieurs de ces sélecteurs en même temps :

~~~js
const button = await driver.findElement(withTagName("button")
                                        .above(By.id("introduction"))
                                        .toRightOf(By.cssSelector("#menu")));
~~~

## Réaliser des actions sur la page

Une fois qu'un élément est trouvé, on peut automatiser les actions de l'utilisateur sur le site.
Les exemples les plus fréquents sont : 
~~~js
// Cliquer sur un bouton
await driver.findElement(By.name("button")).click();
// Remplir un champ et valider (penser à charger Key au début du fichier)
await driver.findElement(By.name('name')).sendKeys("Manu", Key.ENTER);
~~~

Des actions plus précises peuvent être faites 
[à la souris](https://www.selenium.dev/documentation/fr/support_packages/mouse_and_keyboard_actions_in_detail/) 
comme [au clavier](https://www.selenium.dev/documentation/fr/webdriver/keyboard/).

## Quelques commandes utiles

Pour prendre une capture d'écran et l'enregistrer, on utilise :
~~~js
browser.takeScreenshot().then((data) => {
      fs.writeFileSync('img.png', data, 'base64')
    })
~~~

Certaines pages comme Google font apparaitre un popup dans une [iframe](https://developer.mozilla.org/fr/docs/Web/HTML/Element/iframe). 
Dans ce cas, on doit utiliser `switchTo` pour accéder à son contenu : 

~~~js
const iframe = browser.findElement(By.css('iframe')); // On trouve d'abord l'iframe

await browser.switchTo().frame(iframe); // On rentre dans l'iframe
// On fait ici nos actions / recherches dans l'iframe
await browser.switchTo().defaultContent(); // On sort de l'iframe
~~~


## Attendre la réponse du navigateur



## CheatSheet


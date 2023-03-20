---
layout: layout/post.njk 
title:  "serveur Web avec node"
category: tutorial
tags: dev node
author: "François Brucker"
---



## tests fonctionnels/users stories


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


*numérologie.user-story.js* :

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

---
layout: layout/post.njk

title: "Projet numérologie / partie 4 tests"

eleventyNavigation:
  key: "Projet numérologie / partie 4 tests"
  parent: "Projet numérologie"

prerequis:
    - "../partie-4-jardinage/"
---

<!-- début résumé -->

Numérologie partie 5. On reprend tout le projet en codant proprement pour pouvoir faire évoluer notre site.

<!-- fin résumé -->

Utilisation de tests unitaires, fonctionnels et des logs.

Nous allons utiliser le code obtenu en fin de partie 4 et rendre le tout compatible avec un développement continu du projet. En particulier, nous ferons en sorte que :

1. le projet ait des logs
2. vérifier les routes avec postman
3. faire des tests utilisateur avec selenium
4. snapshot front
5. tests unitaires
   1. fonctions
   2. routes
   3. bases de données : environnement de test pour la base de donnée de test

> TBD jest snapshot ?
>
> * <https://www.lambdatest.com/blog/best-javascript-unit-testing-frameworks/>
> * <https://www.youtube.com/watch?v=jiEOXOjLfq4>
> * <https://www.selenium.dev/>
> * <https://www.browserstack.com/guide/front-end-testing>
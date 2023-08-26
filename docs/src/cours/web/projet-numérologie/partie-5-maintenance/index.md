---
layout: layout/post.njk

title: "Projet numérologie / partie 5 maintenance"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Numérologie partie 5. On reprend tout le projet en codant proprement pour pouvoir faire évoluer notre site.

<!-- fin résumé -->

Utilisation de tests unitaires, fonctionnels et des logs.

Nous allons utiliser le code obtenu en fin de partie 4 et rendre le tout compatible avec un développement continu du projet. En particulier, nous allons :

1. [mettre à jour les bibliothèques](./1-mise-jour-des-bibliothèques){.interne}
2. [doter le projet de logs](./2-logs){.interne}
3. [vérifier les routes avec postman](./3-postman){.interne}
4. [faire des tests unitaires](./4-tests-unitaires){.interne}
5. [tests front](./5-tests-front){.interne}
6. [faire des tests utilisateur](./6-tests-utilisateurs){.interne}

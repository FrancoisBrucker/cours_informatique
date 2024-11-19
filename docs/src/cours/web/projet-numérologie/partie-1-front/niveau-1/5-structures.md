---
layout: layout/post.njk
title: "Projet numérologie / partie 1 : front / niveau 1 / structures"

authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Code complet après la partie 1.

## Structure du projet

Le nom du dossier du projet est `numérologie`{.fichier}. Sa structure finale est :

```
.
├── index.html
├── main.css
├── mes_tests.js
└── numérologie.js
```

## Projet final

Les fichiers sont disponibles à [cette adresse](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/web/projet-numérologie/partie-1-front/niveau-1/numérologie).

---
layout: layout/post.njk

title: "Projet numérologie : partie 4 / structures"

eleventyNavigation:
  key: "Projet numérologie : partie 4 / structures"
  parent: "Projet numérologie / partie 4 jardinage"
---

<!-- début résumé -->

Structure du projet à l'issue de la partie 4.

<!-- fin résumé -->

## Structure du projet

Le nom du dossier du projet est `numérologie`{.fichier}. Sa structure finale est :

```text
.
├── back
│   └── numérologie.js
├── db.init.js
├── db.js
├── index.js
├── modèles
│   ├── prénoms.js
│   └── signification.js
├── package.json
├── readme.md
├── routes
│   ├── api
│   │   └── index.js
│   └── signification.js
└── static
    ├── index.html
    ├── main.css
    └── prénoms.html    
```

{% note %}
Ni le dossier `node_modules`{.fichier} ni les fichiers `package-lock.json`{.fichier} et `bd.sqlite`{.fichiers} n'ont été représentés.
{% endnote %}

## Projet final

Les fichiers sont disponibles à [cette adresse](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/web/projet-numérologie/partie-4-jardinage/numérologie).

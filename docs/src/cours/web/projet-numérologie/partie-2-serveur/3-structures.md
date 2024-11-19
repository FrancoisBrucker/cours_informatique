---
layout: layout/post.njk

title: "Projet numérologie : partie 2 / structures"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Structure du projet à l'issue de la partie 2.

<!-- fin résumé -->

## Structure du projet

Le nom du dossier du projet est `numérologie`{.fichier}. Sa structure finale est :

```
.
├── back
│   └── numérologie.js
├── index.js
├── package.json
└── static
    ├── index.html
    └── main.css
```

{% note %}
Ni le dossier `node_modules` ni le fichier `package-lock.json`{.fichier} n'ont été représentés.
{% endnote %}

## Projet final

Les fichiers sont disponibles à [cette adresse](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/web/projet-numérologie/partie-2-serveur/num%C3%A9rologie).

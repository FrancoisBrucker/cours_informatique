# Les cours d'informatique de l'ecm

On devrait voir ici  différents cours de 1A, 2Ai MIE et 3A en informatique.

<https://francoisbrucker.github.io/cours_informatique/index.html>

## structure du dépot

* dossier `docs` contient les sources du site
* dossier `resources` contient les ressources brutes comme les images non redimensionnées, les fichiers de tests, etc.

## Usage

Le site est généré en utilisant [eleventy](https://www.11ty.dev/) qui est un générateur de site statique.

### Logiciels à installer

Pour installer et compiler le site, il suffit d'installer [node](https://nodejs.org/en/) (sous mac, utilisez <https://brew.sh> pour l'installation).

Une fois node installé et le site cloné, placez vous dans le dosser du projet puis tapez les commandes :

```shell
cd docs
npm install
```

Ceci vous installera les divers bibliothèques nécessaires.

### Compiler le site

Assurez vous d'être dans le dossier `docs`.

1. `npm run clean` : supprime les fichiers compilés
2. `npm run build` : crée le site dans le dossier ./docs/dist

### Voir le site en local

Pour voir vos modifications, une fois dans le dossier `docs` tapez la commande : `npm run serve`

Ceci compilera votre site et créera un serveur en local à l'adresse : <http://localhost:8080>

## Fonctionnement général

Les divers fichiers sont des fichiers markdown.

### Markdown

Nous utiliserons le langage [markdown](https://fr.wikipedia.org/wiki/Markdown) comme langage d'écriture de nos page (ou plutôt une variante de celui-ci appelé [CommonMark](https://spec.commonmark.org/) mais les différences sont minimes) qui a l'intérêt d'être compréhensible dans son format texte et facilement *compilable* en html, pdf, ou autre. Le markdown (ou ses multiples variante) est un format d'écriture très utilisé en développement.

### pages

Les pages sont au format markdown, mais pour être dûment compilées il leur faut une entête :

#### entête minimale

Doit contenir :

* le layout de la page
* le titre
* les éléments de navigation :
  * `key` : doit être égale au titre
  * `parent` : le dossier parent dans la navigation

```text
---
layout: layout/post.njk

title: Algorithme, code et théorie

eleventyNavigation:
  key: "Algorithme, code et théorie"
  parent: Cours
---
```

#### entête complète

Peut contenir en plus :

* un ou plusieurs auteurs
* des mots clés

```text
---
layout: layout/post.njk

title: Algorithme, code et théorie
authors:
    - François Brucker

tags: ['cours', 'algorithmie', 'code', 'théorie']

eleventyNavigation:
  key: "Algorithme, code et théorie"
  parent: Cours
---
```

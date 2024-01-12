---
layout: layout/post.njk

title: Coder et développer
tags: ['cours', 'code', 'python']
authors:
    - François Brucker


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Ce cours est dédié au code informatique. On utilisera le language python comme support car c'est un langage très utilisé et qui permet de mettre en lumière tous les aspects du développement d'un code informatique. La très grande majorité des concepts que l'on verra seront cependant transposables dans d'autres langages (comme le javascript ou encore ruby par exemple),

On supposera que vous avez des connaissances scientifiques de base (ie. mathématiques de Lycée) et que vous disposer d'un ordinateur dont vous êtes administrateur.

Aucune compétences en informatique préalable n'est nécessaire.

<!-- fin résumé -->

## Bases

### Langage python

Bases de la programmation sous la forme d'un tutoriel au langage python.

{% aller %}
[Bases de python](bases-python){.interne}
{% endaller %}

### Tutoriels

#### Matplotlib

{% aller %}
[Tutoriel Matplotlib](/tutoriels/matplotlib){.interne}
{% endaller %}

{% info %}
Pour aller plus loin, vous pouvez suivre le [cours d'analyse des données](/cours/analyse-données#pandas) sur l'utilisation de la bibliothèque d'analyse des données [pandas](https://pandas.pydata.org/).
{% endinfo %}

#### python

Une fois les bases acquises, terminez cette partie en faisant le tutoriel de python qui reprend tout ce que nous avons vu de façon plus détaillée :

{% lien %}
<https://docs.python.org/fr/3/tutorial/index.html>
{% endlien %}

## <span id="s-équiper"></span> S'équiper pour le développement

### Un ordinateur pour le développement

- connaissances minimales du fonctionnement d'un ordinateur (application, process, mémoire)
- dossiers/fichiers
- terminal pour exécuter des commandes/applications

{% aller %}
[Un ordinateur pour le développement](ordinateur-développement){.interne}
{% endaller %}

### Installation d'un interpréteur

Lorsque l'on veut utiliser l'interpréteur python exécuter un programme informatique que l'on aura développé, il faut s'assurer que chaque exécution du programme soit identique.
Pour éviter les effets de bords (anciennes variables déclarées, modules importées, etc) Il est  indispensable de pouvoir :

1. créer un nouvel interpréteur python pour ***chaque*** exécution du programme.
2. écrire notre programme en-dehors de tout interpréteur

{% aller %}
[Installer python](installer-python){.interne}
{% endaller %}

{% aller %}
[Installer et utiliser l'éditeur vscode](éditeur-vscode){.interne}
{% endaller %}

## Développement

{% aller %}
[Écrire et exécuter du code](développement){.interne}
{% endaller %}

{% aller %}
[Déboguer son code](debugger){.interne}
{% endaller %}

> TBD exercices mpci.

## Stockage des données

> TBD tout est nombre. type historique du C.
> TBD python permet d'abstraire ça avec la notion de variable et d'objet.

### En mémoire

{% aller %}
[Mémoire et espace de noms](mémoire-espace-noms){.interne}
{% endaller %}

Exemple des textes :

{% aller %}
[Chaînes de caractères](chaîne-de-caractères){.interne}
{% endaller %}

## Sur des fichiers

### Manipuler des fichiers en python

{% aller %}
[Fichiers](fichiers){.interne}
{% endaller %}

### Stocker ses données

{% aller %}
[fichiers pour stocker des données](projet-données-texte){.interne}
{% endaller %}

## Programmation objet

> TBD cours

## Programmation évènementielle

> TBD cours

## Un interpréteur par projet

> TBD cours virtualenv, poetry, etc.


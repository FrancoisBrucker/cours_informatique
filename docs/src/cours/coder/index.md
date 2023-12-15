---
layout: layout/post.njk

title: Coder et développer (en python)
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

Ce cours est dédié au code informatique. On utilisera le language python comme support car c'est un langage très utilisé et qui permet de mettre en lumière tous les aspects du développement d'un code informatique.

On supposera que vous avez des connaissances scientifiques de base (ie. mathématiques de Lycée) et que vous disposer d'un ordinateur dont vous êtes administrateur.

Aucune compétences en informatique préalable n'est nécessaire.

<!-- fin résumé -->

## Bases

> Bases de la programmation et application à python.

{% aller %}
[Bases de python](bases-python){.interne}
{% endaller %}

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
[Installer l'éditeur vscode](/Tutoriels/éditeur-vscode){.interne}
{% endaller %}

## Développement

### Tutoriel python

Vous pourrez terser votre installation en faisant le tutoriel python du site : <https://docs.python.org/fr/3/tutorial/index.html>

C'est un incontournable  pour qui veut faire du python.

### Coder en python

> TBD structures avances. Cours coder

## Programmation objet

> TBD cours

## Programmation évènementielle

> TBD cours
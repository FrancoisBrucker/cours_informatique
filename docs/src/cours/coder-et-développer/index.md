---
layout: layout/post.njk

title: Coder et développer
tags: ['cours', 'code', 'python']
authors:
    - François Brucker

resume: "Ce cours est dédié au code informatique. Comment l'écrire, le tester et l'exécuter."

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Ce cours est dédié au code informatique. On utilisera le language python comme support car c'est un langage très utilisé et qui permet de mettre en lumière tous les aspects du développement d'un code informatique. La très grande majorité des concepts que l'on verra seront cependant transposables dans d'autres langages (comme le javascript ou encore ruby par exemple),

On supposera que vous avez des connaissances scientifiques de base (ie. mathématiques de Lycée) et que vous disposer d'un ordinateur dont vous êtes administrateur.

Aucune compétences en informatique préalable n'est nécessaire.

<!-- fin résumé -->

## <span id="bases"></span>Bases

### Langage python

Bases de la programmation sous la forme d'un tutoriel au langage python.

{% aller %}
[Bases de python](bases-python){.interne}
{% endaller %}

> TBD : QCM sur les notions vues (variable, conteneurs, espace de noms)

### Tutoriels

#### Matplotlib

{% aller %}
[Tutoriel Matplotlib](/tutoriels/matplotlib){.interne}
{% endaller %}

{% info %}
Pour aller plus loin, vous pouvez suivre le [cours d'analyse des données](/cours/analyse-données#pandas) sur l'utilisation de la bibliothèque d'analyse des données [pandas](https://pandas.pydata.org/).
{% endinfo %}

#### Python

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
[Prendre en main l'éditeur vscode](éditeur-vscode/prise-en-main/){.interne}
{% endaller %}

## <span id="développer"></span>Développer

> TBD refaire on fait des fichiers et on importe des choses sans l'avoir défini avant.

{% aller %}
[Écrire et exécuter du code](développement){.interne}
{% endaller %}

Python gère les noms de variables via un concept appelé espace de noms. Il est crucial de comprendre comment cela fonctionne pour ne pas laisser par au doute quand à savoir quelle variable est utilisée quand :

> TBD exercices : plein de fonctions différentes à créer (voir partie algorithmie ?). Utilisation de listes, suppression de doublon, recursion (flocon de koch ?) etc
>
> TBD faire de petits programmes

{% aller %}
> TBD : mettre espace de nom dans bases de python.

[Espace de noms](espace-noms){.interne}

> TBD exercices : variables locales vs globales/fonctions/ajout d'éléments dans une liste

{% endaller %}

Le débogueur, qui permet d'exécuter ligne à ligne du code python est non seulement un excellent outil pour corriger son code, mais également un très bon outil d'apprentissage puisqu'il vous permettra d'assimiler plus rapidement ces notions de variables, d'objets et d'espaces de noms :

{% aller %}
[Déboguer son code](debugger){.interne}
{% endaller %}

> TBD exercices/projet

## Gestion des dépendances

On a utilisé [pip](https://fr.wikipedia.org/wiki/Pip_(gestionnaire_de_paquets)) pour installer des modules python comme [pytest](https://docs.pytest.org/) (voir [partie modules](installer-python/#modules){.interne}). Nous allons voir dans cette partie comment créer ses propres modules et la gestion des modules par projets.

### Un interpréteur par projet

{% aller %}
[Environnements virtuels](environnements-virtuels){.interne}
{% endaller %}

### Créer ses propres modules

> TBD déjà vu ?
> parler de module dossier avec `__init__.py` (vide. Le remplir est niveau 2)
> référence dans le module

{% aller %}
[Modules python](modules-python){.interne}
{% endaller %}

## Stockage des données

### En mémoire

{% aller %}
[Données en mémoire](données-mémoire){.interne}
{% endaller %}

### Chaîne de caractères

{% aller %}
[Encodage Unicode](encodage-unicode){.interne}
{% endaller %}

> TBD méthodes de chaines de caractères :
>
> - split
> - caractères spéciaux : tabulation, fin de ligne
> - strip
> - supprimer les accents. transformation et ascii. voir partie data
>

### Sur des fichiers

{% aller %}
[Fichiers](fichiers){.interne}
{% endaller %}

## Archétype de programmation

### Programmation objet

La programmation objet est un principe de programmation utilisé par la quasi-totalité des langages de programmation. Nes nuances existent bien sur, la programmation objet en rust n'est pas la même qu'en java par exemple, mais quelques principes fondateurs sont utilisés partout.

Nous allons dans cette partie du cours nous atteler à montrer ces principes et leur utilité dans le cadre du langage python.

{% aller %}
[Programmation objet](programmation-objet){.interne}
{% endaller %}

### Programmation évènementielle

La programmation évènementielle est un principe de développement très utilisé dans le développement de [GUI](https://fr.wikipedia.org/wiki/Interface_graphique). Le principe est de coder des *réactions* qui seront exécutées lorsqu'un utilisateur effectuera une action spécifique (générant un *évènement*) comme cliquer sur quelque chose, appuyer sur une touche, etc.

{% aller %}
[Programmation évènementielle](programmation-évènementielle){.interne}
{% endaller %}

## Maintenir et développer du code sûr

### Programmation par les tests

On a pris l'habitude d'écrire des tests pour se rassurer quant à l'exactitude de nos fonctions. Mais pourquoi pas ne pas écrire les tests avant ? C'est le parti pris osé (mais très efficace) de la [programmation par les tests (*Test Driven Development*, ou *TDD*)](https://fr.wikipedia.org/wiki/Test_driven_development) que l'on vous propose d'essayer dans le projet ci-après.

{% aller %}
[Projet de programmation par les tests](projet-TDD){.interne}
{% endaller %}

### Couverture de code

La couverture de code est un outils essentiel lorsque l'on programme par les tests et plus généralement lorsque l'on code tout court. Cet outil permet de vérifier les lignes de codes qui sont testées (*ie.* couvertes).

{% aller %}
[Couverture de code](couverture-de-code){.interne}
{% endaller %}

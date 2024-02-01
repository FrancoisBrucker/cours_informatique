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

## <span id="bases"></span>Bases

### Langage python

Bases de la programmation sous la forme d'un tutoriel au langage python.

{% aller %}
[Bases de python](bases-python){.interne}
{% endaller %}

Python gère les noms de variables via un concept appelé espace de noms. Il est crucial de comprendre comment cela fonctionne pour ne pas laisser par au doute quand à savoir quelle variable est utilisée quand :

{% aller %}
[Mémoire et espace de noms](mémoire-espace-noms){.interne}
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
[Prendre en main l'éditeur vscode](éditeur-vscode/prise-en-main/){.interne}
{% endaller %}

## <span id="développer"></span>Développer

{% aller %}
[Écrire et exécuter du code](développement){.interne}
{% endaller %}

{% aller %}
[Déboguer son code](debugger){.interne}
{% endaller %}

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

## Programmation par les tests

On a pris l'habitude d'écrire des tests pour se rassurer quant à l'exactitude de nos fonctions. Mais pourquoi pas ne pas écrire les tests avant ? C'est le parti pris osé (mais très efficace) de la [programmation par les tests (*Test Driven Development*, ou *TDD*)](https://fr.wikipedia.org/wiki/Test_driven_development) que l'on vous propose d'essayer dans le projet ci-après

### Projet TDD

La programmation part les tests n'est pas quelque chose d'instinctif. Elle nécessite :

1. un apprentissage (au départ on se sent nul et comme on aime pas ça on blame la méthode)
2. d'être appréhendée de façon non dogmatique (on ne test pas tout avant, on utilise juste la fonctionnalité que l'on va coder pour nous permettre de mieux la définir)

Bref, prenez la comme une voie à suivre. Une fois habitué vous ne pourrez plus vous en passer.

{% aller %}
[Projet de programmation par les tests](projet-TDD){.interne}
{% endaller %}

### Couverture de code

> TBD code coverage pour que tout soit ok.

## Stockage des données

> TBD tout est nombre. type historique du C.
> TBD python permet d'abstraire ça avec la notion de variable et d'objet.

### Structures de données

Exemple des textes :

{% aller %}
[Chaînes de caractères](chaîne-de-caractères){.interne}
{% endaller %}

### Sur des fichiers

#### Manipuler des fichiers en python

{% aller %}
[Fichiers](fichiers){.interne}
{% endaller %}

#### Stocker ses données

{% aller %}
[fichiers pour stocker des données](projet-données-texte){.interne}
{% endaller %}

## Un interpréteur par projet

> TBD cours virtualenv, poetry, etc.


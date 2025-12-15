---
layout: layout/post.njk
templateEngineOverride: njk, md

title: "J'aimerais être moins nul en python"
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 0

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Le premier d'une série de 3 enseignements orienté développement et axé autour de 3 thèmes :

- le développement : comment écrire du code propre et fonctionnel ([clean code that works](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530))
- le système : là où sera exécuté le code
- la gestion du code source ([SCM](https://developer.mozilla.org/fr/docs/Glossary/SCM))

{% info %}
[La trilogie](/enseignements/ecm/#mdd)

{% endinfo %}

Une semaine pour comprendre le fonctionnement de python et l'utiliser pour développer ses propres programmes comme le ferait un informaticien.

Basé sur 3 journée de 6h et (environ) 6h de travail personnel pour un total de 24h d'enseignement.

## Jour 1

### Matin

<!-- > TBD 

les faire installer le tout sur leur ordi au milieu de la matinée. 
faire les exercices du cours avec eux. Découper le cours en atelier où on commence chaque exercice et on leur demande de finir ensuite. Il faut que le début de chaque exercice soit fait en exercice+corrigé et ensuite à eux.

-->

{% aller "**Cours**" %}
[Bases du développement](/cours/coder-et-développer/bases-programmation/){.interne}
{% endaller %}

### Après-midi

{% aller "**Exercices d'entraînement**" %}

[Petits programmes](/cours/coder-et-développer/projet-codes/){.interne}

{% endaller %}
{% aller "**On vérifie son niveau**" %}

[100 mono-lignes](/cours/coder-et-développer/mono-lignes/){.interne}
{% endaller %}

## Jour 2

### Matin

{% aller "**Cours**" %}

1. [Bases de système d'exploitation](/cours/système-et-réseau/bases-système/){.interne}
2. [Modules externes python](/cours/coder-et-développer/modules-externes-python/){.interne}
3. Gestion des données :
   1. [chaînes de caractères](/cours/coder-et-développer/encodage-unicode/){.interne}
   2. [notion de fichier](/cours/coder-et-développer/fichiers/structure/){.interne} et [fichier texte](/cours/coder-et-développer/fichiers/fichiers-texte/){.interne}

{% endaller %}

### Après-midi

{% aller "**Exercices d'entraînement**" %}

1. [Tutoriel matplotlib](/cours/coder-et-développer/tutoriel-matplotlib/){.interne}
2. [Projet fichier texte](/cours/coder-et-développer/fichiers/projet-texte/){.interne}

{% endaller %}
{% aller "**On va plus loin**" %}

[Données texte](/cours/coder-et-développer/fichiers/projet-données/){.interne}
{% endaller %}

## Jour 3

### Matin

{% aller "**Cours**" %}

1. [mettre ses sources à disposition](/cours/gestion-des-sources/#dépot){.interne}
2. [déboguer son code](/cours/coder-et-développer/débogueur/){.interne}
3. [tester son code](/cours/coder-et-développer/tests-unitaires/){.interne}
4. [écrire du code lisible et maintenable](/cours/coder-et-développer/écrire-code/coder/){.interne}

{% endaller %}
{% aller "**TD**" %}

1. [écrire du code lisible et maintenable](/cours/coder-et-développer/écrire-code/tutoriel-hello-dev/){.interne}
2. [Projet pourcentages](/cours/coder-et-développer/projet-pourcentages){.interne}
3. [faites le TD déboguer son code](/cours/coder-et-développer/débogueur/){.interne}

{% endaller %}

### Après-midi

{% aller "**Exercices d'entraînement**" %}

[On s'entraîne en ajoutant des tests](/cours/coder-et-développer/projet-codes-tests/){.interne}

{% endaller %}

{% aller "**On vérifie son niveau**" %}
[Exercices](/cours/coder-et-développer/exercices-tests/){.interne}

{% endaller %}

## Projet à rendre

Choisissez un exercice du <https://adventofcode.com/> actuel et résolvez le. On vous demande de rendre :

- un fichier `main.py`{.fichier} pour votre programme principal
- un fichier `fonction.py`{.fichier} pour vos fonctions
- un fichier `test_fonction.py`{.fichier} pour vos tests
- un fichier `readme.md`{.fichier} pour les informations générales sur votre projet

Ainsi que la preuve que votre exercice est réussi.

Vous devrez rendre votre travail [sur moodle](https://moodle.centrale-med.fr/course/view.php?id=1231) avant le 24 décembre 23h59.

{% info %}
Si vous rendez le code sous la forme d'un lien vers un projet github, vous aurez toute ma considération.
{% endinfo %}

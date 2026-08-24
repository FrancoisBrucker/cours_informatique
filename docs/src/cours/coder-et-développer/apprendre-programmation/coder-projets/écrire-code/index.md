---
layout: layout/post.njk

title: Écrire du code


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



### Séparer fonctions et exécutions

> TBD créer ses modules.

### Corriger son code

Le débogueur, qui permet d'exécuter ligne à ligne du code python est non seulement un excellent outil pour corriger son code, mais également un très bon outil d'apprentissage puisqu'il vous permettra d'assimiler plus rapidement ces notions de variables, d'objets et d'espaces de noms :

{% aller %}
[Déboguer son code](débogueur){.interne}
{% endaller %}

### Écrire du code maintenable

Il faut essayer de limiter au maximum la création de bug et, surtout, éviter qu'ils réapparaissent à la suite d'une modification de code.

Mais plutôt que de corriger il vaut mieux éviter que les bugs arrivent

{% aller %}
[Tester son code](tests-unitaires){.interne}
{% endaller %}

{% aller %}
[On s’entraîne : écrire des tests](projet-codes-tests){.interne}
{% endaller %}

### Écrire du code lisible

{% aller %}
[Coder](coder){.interne}
{% endaller %}

Installation et utilisation des outils de développement :

{% aller %}
[Projet Mise en œuvre d'un projet informatique](tutoriel-hello-dev){.interne}
{% endaller %}

### On s'entraîne à écrire du code propre qui fonctionne

#### Un projet complet

{% aller %}
[Projet pourcentage](projet-pourcentages){.interne}
{% endaller %}

#### On vérifie qu'on sait faire

{% aller %}
[exercices](exercices-tests){.interne}
{% endaller %}
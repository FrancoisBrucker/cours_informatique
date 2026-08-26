---
layout: layout/post.njk

title: Écrire du code


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Modifier du code est ce vous ferez le plus souvent : on passe son temps à modifier du code plutôt que d'implémenter des algorithmes (c'est ce que l'on appelle [le refactoring](https://fr.wikipedia.org/wiki/R%C3%A9usinage_de_code)).

Il en découle que :

{% attention2 "**À retenir**" %} 
Vous allez passer plus de temps à **lire** du code qu'à en **écrire**

{% endattention2 %}

Comme il faut que : *ce qui se fait souvent doit se faire rapidement*, on utilisera une série de règles et de méthodes pour lire aisément son code, se faire comprendre aisément de ses partenaires et - surtout - s'assurer de son bon fonctionnement.


## Bonnes pratiques

{% aller %}
[Bonnes pratiques](bonnes-pratiques){.interne}
{% endaller %}


## Écrire du code

Des bonnes pratiques découlent une série de méthodes et pratiques utilisé pour écrire _du code propre qui fonctionne_.

{% attention2 "**À retenir**" %}
Selon Kent Beck (grand développeur), le but de la programmation est d'écrire du : _**Clean code that works**_
{% endattention2 %}


### Séparer fonctions et exécution

Un projet va être composé d'un fichier qui exécute le code et de multiples modules importés par lui. Nous allons voir comment créer un projet avec plusieurs modules en python :

{% aller %}
[Création de modules](création-modules){.interne}
{% endaller %}

{% aller %}
[On s’entraîne : séparer fonctions et exécution](projet-création-modules){.interne}
{% endaller %}

### Écrire du code maintenable

Il faut essayer de limiter au maximum la création de bug et, surtout, éviter qu'ils réapparaissent à la suite d'une modification de code. Mais plutôt que de corriger il vaut mieux éviter que les bugs arrivent en testant chaque fonctionnalité :

{% aller %}
[Tester son code](tests-unitaires){.interne}
{% endaller %}

{% aller %}
[On s’entraîne : écrire des tests](projet-codes-tests){.interne}
{% endaller %}


### Projet Informatique

On a toutes les méthodes pour écrire du code, on va pouvoir combiner tout ça pour créer un projet informatique :

{% aller %}
[Mise en œuvre d'un projet informatique](projet-informatique){.interne}
{% endaller %}
Un dernier projet guidé avant le grand bain pour être sur que tout soit acquis :
{% aller %}
[On s'entraîne : Projet pourcentage](projet-pourcentages){.interne}
{% endaller %}

## Corriger son code

Le débogueur, qui permet d'exécuter ligne à ligne du code python est non seulement un excellent outil pour corriger son code, mais également un très bon outil d'apprentissage puisqu'il vous permettra d'assimiler plus rapidement ces notions de variables, d'objets et d'espaces de noms :

{% aller %}
[Déboguer son code](débogueur){.interne}
{% endaller %}

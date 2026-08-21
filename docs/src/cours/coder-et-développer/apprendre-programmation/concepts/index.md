---
layout: layout/post.njk

title: Concepts

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


La programmation repose sur quelques concepts (variables, fonctions, ...) partagés par tous les langages. Nous allons nous concentrer sur **_les langages à objets_**, dont python fait parti, ou l'on manipule des "_objets_" référencés par des _"variables"_. Ces langages forment une grande majorité des langages utilisés (python, javascript, java, ...) et leurs concepts sont majoritairement utilisés dans des langages à **_structure_** comme le go ou encore le rust.

En tout état de cause, ce sont des langages idéals pour commencer à programmer.

## Fondements

{% aller %}
[Fondements de la programmation (avec python)](fondements-programmation){.interne}
{% endaller %}

## Conteneurs et mutabilité

Les conteneurs sont des objets contenant des variables. Python a popularisé ces structures qui sont maintenant universellement utilisées.

{% aller %}
[Conteneurs](conteneurs){.interne}
{% endaller %}

Les conteneurs sont liés à une notion fondamentale en python et dans tous les langages objets qu'est la mutabilité.

{% attention %}
La notion de mutabilité d'un objet est cruciale à comprendre. Elle permet du code clair et optimisé (aucun objet n'est copié) mais est la cause de nombre d'erreurs a priori incompréhensibles si on ne l’appréhende pas bien.
{% endattention %}
{% aller %}
[Objets mutables et non mutables](mutable-immutable){.interne}
{% endaller %}

## Chaines de caractères

Les chaines de caractères ne sont pas _sticto sensu_ des conteneurs puisqu'elles sont composés de caractères et par de variables, mais elles  partagent de nombreuses propriétés avec les listes comme on va le voir. Elles sont très utilisés lorsqu'un programme doit communiquer avec son utilisateur et python permet de faire beaucoup de choses avec elles :

{% aller %}
[Chaînes de caractères](chaines-caractères){.interne}
{% endaller %}


## Modules et espace de nommage

Les [modules](https://docs.python.org/fr/3/tutorial/modules.html) pythons sont des regroupement de fonctions utiles. 

{% aller %}
[Modules et espace de nommages python](utilisation-modules){.interne}
{% endaller %}

Il existe quelques modules externes à python très utilisés. Ils ne sont pas présent par défaut lorsque l'on installe un nouvel interpréteur mais de nombreuses solutions les intègrent par défaut. C'est le cas de spyder, vous pouvez donc faire les deux tutoriaux suivant sans avoir à installer quoi que ce soit.

### module `matplotlib`{.language-}

Le module matplotlib est devenu un standard de fait (pour le meilleur et surtout le pire) pour représenter des graphiques.

{% aller %}
[Tutoriel Matplotlib](tutoriel-matplotlib){.interne}
{% endaller %}

Si vous avez le choix, je conseille plutôt d'utiliser [le module seaborn](https://seaborn.pydata.org/) pour dessiner vos graphique. Mais comme ce module est basé sur matplotlib, une connaissance minimale de matplotlib, comme le donne le tutoriel précédent est tout de même nécessaire.

### module `numpy`{.language-}

Le module numpy est très utilisé pour les calculs scientifique, en particulier matriciels.

{% aller %}
[Tutoriel Numpy](tutoriel-numpy){.interne}
{% endaller %}


## Tutoriel python

Terminez cette partie en faisant le tutoriel de python qui reprend tout ce que nous avons vu, parfois de façon plus détaillée :

{% lien %}
<https://docs.python.org/fr/3/tutorial/index.html>
{% endlien %}

## <span id='exercices-fin'></span>On vérifie qu'on a compris

{% aller %}
[Petits projets de code](projet-codes){.interne}
{% endaller %}
{% aller %}
[mono-lignes en python](./mono-lignes){.interne}
{% endaller %}



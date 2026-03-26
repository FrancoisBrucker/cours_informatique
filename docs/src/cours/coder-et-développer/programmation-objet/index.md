---
layout: layout/post.njk
title: Programmation Objet

authors:
  - François Brucker
  - Célia Châtel
  - Valentin Emiya

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


<!-- TBD 

à refaire en 

1. mettre l'argumentaire avec les objets partout dans un fichier à part.
2. 
3. mettant améliorer ses objets (property, méthodes de classes) à la toute fin. Juste parler à la fin du cours 

- de str et repr comme méthodes spéciales.
- des comparaisons de cartes

Faire 1h de cours et 3h de code :
- 1h cours avec compteur
- 1h TD avec dés
- 2h TP avec carte.

-->



La programmation objet est un sujet très commenté. Il existe de nombreux cours en parlant et ce depuis de très longues années. Vous côtoierez donc sur internet des choses très anciennes (aux concepts désuets ou en disgrâce comme l'héritage) aux choses très récentes (aux concepts non encore clairement établis et dont on ne sait s'ils survivront à l'épreuve du temps). Le but ici est de présenter les bases opérationnelles et les raisons fondamentales de ce type de programmation et de pourquoi il est utilisé dans la quasi-totalité des langages actuels.

Ce cours devrait vous permettre de vous lancer dans la programmation objet dans tout langage, mais nous illustrerons tous les principes vues en python. Il restera bien sur des choses à découvrir, des concepts avancés ou encore les subtilités d'utilisation des objets dans divers langages, mais après ce cours vous devriez être bien préparé.

Le but de la programmation objet est d'écrire du code :

- facile à lire
- maintenable
- facile à étendre en ajoutant des fonctionnalités

Si un concept objet va à l'encontre de ce principe dans votre programme **NE L'UTILISEZ PAS**. C'est souvent vrai pour l'héritage qui n'a d'utilité que dans des cas très précis...

## <span id="classes-objets"></span>Classes et objets

### Tout est objet en python

{% aller %}
[Utiliser des objets en python](introduction){.interne}
{% endaller %}

### Concevoir des classes et des objets

{% aller %}
[Classes et objets](classes-et-objets){.interne}
{% endaller %}
{% aller %}
[Coder ses objets](coder-ses-objets){.interne}
{% endaller %}

On s'entraîne à la création d'objets :

{% aller %}
[Projet dés](projet-objets-dés){.interne}
{% endaller %}
{% aller %}
[Projet cartes](projet-objets-cartes){.interne}
{% endaller %}

### Améliorer ses objets

{% aller %}
[Améliorer ses objets](améliorer-ses-objets){.interne}
{% endaller %}

On s'entraîne en perfectionnant nos dés et cartes :

{% aller %}
[Améliorons nos dés](projet-objets-dés-amélioration){.interne}
{% endaller %}
{% aller %}
[Améliorons nos cartes](projet-objets-cartes-amélioration){.interne}
{% endaller %}

## Combiner ses objets entre eux

{% aller %}
[Composition et agrégation](composition-agrégation){.interne}
{% endaller %}

Reprenons nos objets et combinons les avec d'autres :

{% aller %}
[Projet de compositions de dés](projet-composition-dés){.interne}
{% endaller %}
{% aller %}
[Projet d'agrégation de cartes](projet-agrégation-cartes){.interne}
{% endaller %}

## Héritage

{% aller %}
[Héritage](héritage){.interne}
{% endaller %}

{% aller %}
[Projet héritage](projet-héritage){.interne}
{% endaller %}

## On s'entraîne

{% aller %}
[La bataille navale](projet-bataille-navale){.interne}
{% endaller %}

## Pour aller plus loin

{% aller %}
[Autres améliorations](./odds-and-ends){.interne}
{% endaller %}

<!-- TBD

## Pour aller plus loin : les design pattern

{% aller %}
[Design Patterns](design-patterns){.interne}
{% endaller %} 

-->

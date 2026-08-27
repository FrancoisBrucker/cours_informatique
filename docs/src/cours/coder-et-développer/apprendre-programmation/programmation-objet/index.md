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

La programmation objet est un sujet très commenté. Il existe de nombreux cours en parlant et ce depuis de très longues années. Vous côtoierez donc sur internet des choses très anciennes (aux concepts désuets ou en disgrâce comme l'héritage) aux choses très récentes (aux concepts non encore clairement établis et dont on ne sait s'ils survivront à l'épreuve du temps). Le but ici est de présenter les bases opérationnelles et les raisons fondamentales de ce type de programmation et de pourquoi il est utilisé dans la quasi-totalité des langages actuels.

Ce cours devrait vous permettre de vous lancer dans la programmation objet dans tout langage, mais nous illustrerons tous les principes vues en python. Il restera bien sur des choses à découvrir, des concepts avancés ou encore les subtilités d'utilisation des objets dans divers langages, mais après ce cours vous devriez être bien préparé.


{% attention2 "**À retenir**" %}
Le but de la programmation objet est d'écrire du code :

- facile à lire
- maintenable
- facile à étendre en ajoutant des fonctionnalités


Si un concept objet va à l'encontre de ce principe dans votre programme **NE L'UTILISEZ PAS**. 
{% endattention2 %}

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
[Projet dés](projet-objets-dés){.interne}
{% endaller %}

On s'entraîne à la création d'objets :

{% aller %}
[Projet cartes](projet-objets-cartes){.interne}
{% endaller %}

### Améliorer ses objets

{% aller %}
[Améliorer ses objets](améliorer-ses-objets){.interne}
{% endaller %}
{% aller %}
[Améliorons nos dés](projet-objets-dés-amélioration){.interne}
{% endaller %}

On s'entraîne en perfectionnant nos cartes :

{% aller %}
[Améliorons nos cartes](projet-objets-cartes-amélioration){.interne}
{% endaller %}

## Combiner ses objets entre eux

{% aller %}
[Composition et agrégation](composition-agrégation){.interne}
{% endaller %}
{% aller %}
[Projet de compositions de dés](projet-composition-dés){.interne}
{% endaller %}

Reprenons nos objets et combinons les avec d'autres :

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

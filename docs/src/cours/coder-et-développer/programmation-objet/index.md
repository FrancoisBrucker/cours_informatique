---
layout: layout/post.njk
title: Programmation Objet

authors:
  - François Brucker
  - Célia Châtel

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La programmation objet est un sujet très commenté. Il existe de nombreux cours en parlant et ce depuis de très longues années. Vous côtoierez donc sur internet des choses très anciennes (aux concepts désuets ou en disgrâce comme l'héritage) aux choses très récentes (aux concepts non encore clairement établis et dont on ne sait s'ils survivront à l'épreuve du temps). Le but ici est de présenter les bases opérationnelles et les raisons fondamentales de ce type de programmation et de pourquoi il est utilisé dans la quasi-totalité des langages actuels.

Ce cours devrait vous permettre de vous lancer dans la programmation objet dans tout langage, mais nous illustrerons tous les principes vues en python. Il restera bien sur des choses à découvrir, des concepts avancés ou encore les subtilités d'utilisation des objets dans divers langages, mais après ce cours vous devriez être bien préparé.

Le but de la programmation objet est d'écrire du code :

- facile à lire
- maintenable
- facile à étendre en ajoutant des fonctionnalités

Si un concept objet va à l'encontre de ce principe dans votre programme **NE L'UTILISEZ PAS**. C'est souvent vrai pour l'héritage qui n'a d'utilité que dans des cas très précis...

## <span id="classes-objets"></span>Classes et objets

La base de la programmation objet, c'est les classes et comment elles permettent de construire (on dira instancier) des objets.

{% aller %}
[Classes et objets](classes-et-objets){.interne}
{% endaller %}
{% aller %}
[Coder ses objets](coder-ses-objets){.interne}
{% endaller %}
{% aller %}
[Améliorer ses objets](améliorer-ses-objets){.interne}
{% endaller %}

On s'entraîne à la création d'objets :

{% aller %}
[Projet dés](projet-objets-dés){.interne}
{% endaller %}
{% aller %}
[Projet cartes](projet-objets-cartes){.interne}
{% endaller %}

Améliorer ses objets en gérant précisément l'accès aux attributs :

{% aller %}
[Projet dés accesseur](projet-objets-dés-accesseur){.interne}
{% endaller %}

{% aller %}
[Projet carte value object](projet-objets-cartes-value-object){.interne}
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

## Projet final

{% aller %}
[La bataille navale](projet-bataille-navale){.interne}
{% endaller %}

---
layout: layout/post.njk

title: Méthodes de développement
tags: ["code", "go"]


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD 
>
> le go
>
> - prérequis : git
> - outils de la partie A : 
>   - dépendances
>   - débogueur
> ajouter code coverage
> 
Dernière partie en python avant d'apprendre un nouveau langage. On montre comment développer du code au quotidien.

## TDD

La méthode de développement des années 2000 qui était tellement en avance sur son temps qu'on a encore l'impression qu'elle est neuve :

{% aller %}
[Test Driven Development](./TDD/){.interne}
{% endaller %}

## Design pattern

Algorithmie objet ou comment résoudre efficacement des problèmes de conception courant :

{% aller %}
[Design pattern](./design-patterns/){.interne}
{% endaller %}

## Couverture de code

La couverture de code est un outils essentiel lorsque l'on programme par les tests et plus généralement lorsque l'on code tout court. Cet outil permet de vérifier les lignes de codes qui sont testées (_ie._ couvertes).

{% aller %}
[Couverture de code](couverture-de-code){.interne}
{% endaller %}

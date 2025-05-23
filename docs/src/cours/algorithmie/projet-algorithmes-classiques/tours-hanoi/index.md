---
layout: layout/post.njk

title: Tours de Hanoi

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Corrigé](./corrigé){.interne}
{% endlien %}

[Les _tours de Hanoï_](https://fr.wikipedia.org/wiki/Tours_de_Hano%C3%AF) sont un célèbre casse tête inventé par Édouard Lucas.

Il consiste à déplacer $n$ disques de diamètres différents d'une tour de _"départ"_ à une tour d' _"arrivée"_ en passant par une tour _"intermédiaire"_, tout en respectant les règles suivantes :

- on ne peut déplacer qu'un disque à la fois
- on ne peut placer un disque sur un disque plus petit que lui.

On suppose que cette dernière règle est également respectée dans la configuration de départ.

{% lien %}
[Une interface pour jouer aux tours de Hanoï](http://championmath.free.fr/tourhanoi.htm).

Déplacez les cylindres par glisser/déposer.
{% endlien %}

Essayons de résoudre ce problème de façon optimale.

{% faire %}
Donnez un algorithme récursif permettant de résoudre le problème.
{% endfaire %}
{% faire %}
Quelle est sa complexité ?
{% endfaire %}
{% faire %}
Peut-on faire mieux ?
{% endfaire %}

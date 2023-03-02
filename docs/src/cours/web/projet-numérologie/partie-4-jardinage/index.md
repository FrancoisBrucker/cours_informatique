---
layout: layout/post.njk

title: "Projet numérologie / partie 4 jardinage"

eleventyNavigation:
  key: "Projet numérologie / partie 4 jardinage"
  parent: "Projet numérologie"
---

<!-- début résumé -->

Numérologie partie 4. On jardine le code pour le rendre plus propre et ainsi plus apte a être débuggé et amélioré.

<!-- fin résumé -->

{% prerequis "**Prérequis**" %}

* [Projet numérologie / partie 3 données](../partie-3-données)

{% endprerequis %}

Dans tout projet, il y a 3 phases qu'il faut respecter, et dans cet ordre :

1. make it work
2. make it right
3. make it fast

On doit cette phrase au célèbre Kent Beck, inventeur du TDD. Ce coding mantra (comme [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), [KISS](https://en.wikipedia.org/wiki/KISS_principle) ou encore [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)) marche à tout niveau de votre projet, vous pouvez tout aussi bien l'appliquer à une fonction/algorithme que vous venez de développer qu'à votre projet en entier.

{% note %}

Notre projet fonctionne, rendons le propre.

{% endnote %}

## Projet

1. [Séparation des routes](./1-routes)
2. [Séparation des modèles](./2-modeles)
3. [Scripts](./3-scripts)
4. [projet final](./4-structures)

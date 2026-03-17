---
layout: layout/post.njk
title: "Projet : Amélioration des objets dés"

eleventyNavigation:
  prerequis:
    - "../projet-objets-dés/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


<!-- TBD 

prendre les str et repr de composition/agrégation et les mettre là dedans

-->


## Valeur par défaut

{% faire %}
Faites en sorte que l'on puisse créer des dés avec une position initiale, On doit pouvoir :

- créer un dé sans paramètre, `Dé()`{.language-}, et sa position doit être sur la position 1
- créer un dé avec un paramètre qi sera sa position par défaut `Dé(4)`{.language-} par exemple.

Modifiez tous les tests et les programmes principaux.
{% endfaire %}

## Méthodes de classes

On ne crée pour l'instant que des dés à 6 faces.

{% faire %}
Utilisez des méthodes de classes pour créer des dés à 4 et 20 faces. On devra pouvoir écrire :

- `Dé.d4()`{.language-} pour créer un dé à 4 faces sur la position 1
- `Dé.d20()`{.language-} pour créer un dé à 20 faces sur la position 1

Modifiez tous les tests et les programmes principaux.
{% endfaire %}
{% info %}
Il faut maintenant faire attention aux bornes d'un lancé.
{% endinfo %}

## Finalement

{% faire %}
Vérifier que tout fonctionne :

- les tests
- la user story
- le programme principal

{% endfaire %}

---
layout: layout/post.njk

title:  "Gestion des dépendances"

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

Les dépendances d'un projet sont de deux ordres :

- la version du langage : chaque nouvelle version peut amener son lot de modifications par rapport à des versions antérieures
- les modules externes : un projet peut utiliser des dizaines de bibliothèques différentes qu'il faut installer pour être utilisé

Nous allons ici nous concentrer sur la façon de faire de python, chaque langage va avoir ses propres façon de faire pour gérer ces deux problèmes.

## Interpréteur

Lorsque l'on veut utiliser l'interpréteur python exécuter un programme informatique que l'on aura développé, il faut s'assurer que chaque exécution du programme soit identique. Pour éviter les effets de bords (anciennes variables déclarées, modules importées, etc) Il est indispensable de pouvoir :

1. créer un nouvel interpréteur python pour **_chaque_** exécution du programme.
2. écrire notre programme en-dehors de tout interpréteur

{% aller %}
[Version de l'interpréteur python](version-python){.interne}
{% endaller %}

## Créer son environnement python

Chaque projet va dépendre de modules externes que vous avez installés avec `pip`. Mais lorsque vous voulez partager votre travail avec d'autres personnes, il leur faudra aussi installer les différents modules pour utiliser votre projet. De plus, certains de ces modules pourraient être incompatible avec leur version de python ou des modules qu'ils utilisent par ailleurs.

Python règle ces deux problèmes d'un seul coup en utilisant des environnements virtuels :

{% aller %}
[Environnements virtuels](environnements-virtuels){.interne}
{% endaller %}

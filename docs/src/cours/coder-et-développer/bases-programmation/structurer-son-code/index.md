---
layout: layout/post.njk

title: Structurer son code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Lorsque l'on veut plus que juste utiliser des méthodes et fonctions déjà existante, il faut structurer son code en parties utilisables indépendamment, que ce soit sous la forme de code (bloc, fonctions, modules) ou de données (conteneurs).

Nous n'utiliserons plus directement l'interpréteur pour nos futurs code. En effet, créer des bloc directement avec l'interpréteur est un calvaire car il est fait pour exécuter une ligne après l'autre alors qu'un bloc nécessite plusieurs lignes.

{% info %}
Utilisez un notebook ou spyder pour exécuter les divers exemples et exercices.
{% endinfo %}

## Blocs, condition et répétitions

Pour l'instant nous avons envoyé chaque ligne de python que nous avons écrite directement à l'interpréteur pour être exécuté. Les *blocs* de python permettent de grouper un ensemble de lignes de code pour être exécutés sous certaines conditions.

{% aller %}
[Blocs](blocs){.interne}
{% endaller %}

### Bloc

### Conditions

### Répétitions

### Créer ses propres fonctions

Si un bloc de code est exécuté plusieurs fois à l'identique, on aimerait aussi pouvoir nommer ce groupe pour **pouvoir le réutiliser juste en appelant son nom**. C'est possible avec les fonctions.

{% aller %}
[Création de fonctions](creation-fonctions){.interne}
{% endaller %}

> TBD exercice avec fonctions, méthodes et listes

### Créer ses propres modules

> TBD sous la forme d'un fichier (package = dossier)

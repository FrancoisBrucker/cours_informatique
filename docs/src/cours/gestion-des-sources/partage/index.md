---
layout: layout/post.njk

title: Partager du code source

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Pour que son accès soit facile, il faut que la structure de stockage soit sur le même ordinateur que celui ayant le répertoire de travail.

Si cette solution est idéal lorsque l'on est un unique développeur, elle devient plus complexe à mettre en œuvre si on est plusieurs à travailler sur le projet. Il faut :

1. en avoir une copie de la structure de stockage chez chaque participant,
2. permettre à plusieurs personnes de travailler sur le même fichier,
3. permettre le travail asynchrone entre les personnes : une personne va avancer à un endroit pendant qu'une autre travaille sur autre chose
4. pouvoir reprendre un projet existant avec une nouvelle équipe

Ceci implique que chaque copie soit synchronisée par un dépôt référent, un **_projet référent_** faisant autorité pour tous les participants.

Une bonne implémentation consiste **à ne pas sacraliser la mise en commun**. Il faut le faire le souvent pour que tout le monde ait une version claire de l'ensemble **actuel** du projet.

{% attention2 "**À retenir**" %}

Lorsque vous utilisez un projet en commun il faut avoir un dépôt commun mais ne faut pas en sacraliser la mise en commun avec des règles de soumission stricte ou un superviseur.

{% endattention2 %}

## Besoins pour l'utilisation d'un dépôt distant

{% aller %}
[Besoins](./besoins-origin){.interne}
{% endaller %}

### Projet : local et origine

{% aller %}
[Projet avec github desktop](./github-desktop){.interne}
{% endaller %}

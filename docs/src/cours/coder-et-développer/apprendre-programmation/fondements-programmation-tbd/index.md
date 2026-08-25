---
layout: layout/post.njk

title: Fondements de la programmation (avec python)
authors:
  - François Brucker
  - Pierre Brucker

eleventyNavigation:
    prerequis:
        - "/cours/système/ordinateur-programmes-OS/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---







## Partie III : Structures de données




<!-- TBD 

Faire des exercices : listes et dictionnaires.

-->


## Partie IV : Structures du programme

### Espace de nommage

La base de cette séparation en unités fonctionnelles séparée est l'espace de nommage. Nous l'avons déjà entre-aperçu lorsque l'on a parlé de modules et de fonctions, nous allons ici rentrer dans les détails et expliciter comment python trouve un objet associé à un nom.

{% aller %}
[Espace de nommage](espace-nommage){.interne}
{% endaller %}

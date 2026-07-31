---
layout: layout/post.njk

title: Système

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On suppose ici que vous savez minimalement interagir avec votre système d'exploitation en exécutant des applications via un menu ou l'explorateur de fichiers.

<!-- TBD :
- alt f4, finder ou truc ubuntu pour connaître applis
-  

-->

## Partie I : Ordinateur et Applications

{% aller %}
[Bases](bases){.interne}
{% endaller %}



## Partie II : interagir avec le système

- dossier / fichier
- terminal
- application utiles
- installation nouveau système optionnel.

### Le terminal

Le terminal permet d'exécuter rapidement des commandes.

{% aller %}
[Terminal](terminal){.interne}
{% endaller %}

### Installation d'un nouveau système

{% aller %}
[Nouvelle installation d'un système](système-installation){.interne}
{% endaller %}


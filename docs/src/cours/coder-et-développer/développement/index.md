---
layout: layout/post.njk

title: Développer du code


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Principes à garder en mémoire pour tout développement de code :

{% aller %}
[Coder](coder){.interne}
{% endaller %}

Installation et utilisation des outils de développement :

{% aller %}
[Projet `hello-dev`{.fichier}](tutoriel-hello-dev){.interne}
{% endaller %}

Mise en pratique :

{% aller %}
[Projet `pourcentages`{.fichier}](projet-pourcentages){.interne}
{% endaller %}

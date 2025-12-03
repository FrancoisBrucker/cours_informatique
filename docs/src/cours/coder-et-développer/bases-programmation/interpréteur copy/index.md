---
layout: layout/post.njk

title: Installer et utiliser un interpréteur

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD supprime petit à petit. Ce qui reste est à dispatcher.

Les logiciels et outils nécessaires pour écrire et exécuter du code python.

## Éditeur de code

Une fois l'interpréteur installé, on va l'utiliser _via_ [un IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement). Il existe plusieurs choix possible, mais le plus utilisé actuellement est vscode :

{% aller %}
[Éditeur vscode](éditeur-vscode){.interne}
{% endaller %}

Vscode utilise le terminal pour exécuter ses programmes python. C'est une pratique courante dans le monde unix mais iun peu plus exotique sous windows. Prenez le temps de lire le tutoriel suivant pour l'utiliser efficacement.

{% aller %}
[Utiliser le terminal de vscode](terminal-vscode){.interne}
{% endaller %}

## Modules python

Un interpréteur tout neuf vient presque nu. Il ne possède aucun des modules mis à disposition d'environnement tels que anaconda ou Spyder. Mais ce n'est pas grave, nous allons les installer nous même !

{% aller %}
[Installer des modules](modules-python){.interne}
{% endaller %}

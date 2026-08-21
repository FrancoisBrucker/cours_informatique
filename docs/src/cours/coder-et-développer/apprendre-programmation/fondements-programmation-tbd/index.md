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


> TBD ajout des parties non utiles


### <span id="installation-développement"></span>Installer et utiliser un interpréteur python

> installer un interpréteur
> vscode ou pycharm dans un second temps


Jusqu'à présent on a utilisé des interpréteurs externes pour exécuter notre code. Si l'on cherche à créer ses propres programmes, il est préférable d'avoir un interpréteur sur propre ordinateur. Ceci sera plus rapide et permettra à terme d'être paramétrable à l'envie.

{% aller %}
[Installer un interpréteur python](interpréteur-installation){.interne}
{% endaller %}

Une fois l'interpréteur installé, plutôt que de l'utiliser directement, on utilise un éditeur de texte spécialisé dans l'écriture de code : [un IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement). Il existe plusieurs choix possible, mais le plus utilisé actuellement est vscode.

{% aller %}
[Éditeur vscode](éditeur-vscode){.interne}
{% endaller %}

La principale différence entre un éditeur de texte et un notebook est que l'interpréteur est re-exécuté à chaque exécution : il ne garde rien en mémoire de la précédente exécution du code. Ceci permet de faire du code rép´table où toutes les informations sont uniquement contenues dans le fichier que l'on exécute.



## Partie III : Structures de données




<!-- TBD 

Faire des exercices : listes et dictionnaires.

-->


## Partie IV : Structures du programme

Structurer son programmes en fichiers.

### Modules

{% aller %}
[Création de modules](creation-modules){.interne}
{% endaller %}

### Espace de nommage

La base de cette séparation en unités fonctionnelles séparée est l'espace de nommage. Nous l'avons déjà entre-aperçu lorsque l'on a parlé de modules et de fonctions, nous allons ici rentrer dans les détails et expliciter comment python trouve un objet associé à un nom.

{% aller %}
[Espace de nommage](espace-nommage){.interne}
{% endaller %}

{% aller %}
[Espace de nommage et fonctions](fct-espace-nommage){.interne}
{% endaller %}

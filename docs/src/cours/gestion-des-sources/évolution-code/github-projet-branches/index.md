---
layout: layout/post.njk
title: "Projet github : utilisation de branches"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Je suis content de mon projet, mais soit :

- j'aimerai tester des modifications sans être sûr de les conserver
- j'aimerai corriger un bug mais sa correction risque de prendre un peu de temps

De plus, je ne voudrai pas juste travailler dans mon coin et tout commiter une fois que ce sera fini car :

- le travail risque de prendre du temps et plusieurs commits
- si je travaille dans mon coin, lorsque j'aurai fini, les autres membres du projets auront certainement modifié le code.

La solution à ce problème consiste à ajouter **une branche** au projet.

## Création d'une nouvelle branche

1. ![branches](github-branches-1.png)
2. On clique :
   - pour ajouter une nouvelle branche : ![ajout d'une branche](github-branches-2.1.png)
   - on indique son nom et la branche à copier : ![paramètres de la branche](github-branches-2.2.png)
3. On peut maintenant changer de branche :
   - on retourne à la page de gestion de projet et on voit qu'on a 2 branches : ![plusieurs branches](github-branches-3.1.png)
   - passage sur une autre branche : ![passage à la nouvelle branche](github-branches-3.2.png)

## Travail sur la nouvelle branche

1. ajout d'un fichier : ![ajout fichier](github-feature-1.png)
2. modification d'un fichier : ![modification](github-feature-2.png)

On obtient alors les commits sur la branches feature :

![commits sur la branche feature](github-feature-3.png)

Les 3 premiers commits sont communs à la branche main (allez dans _"insights/network"_ pour voir le graphe de dépendances) :

![graphe de dépendances](github-feature-4.png)

Pour bien voir que les branches sont indépendantes, ajoutons un commit sur la branche main, en modifiant le fichier `programme.txt`{.fichier} :

![ajout commit dans la branche main](github-feature-5.png)

Le graphe de dépendance à maintenant deux histoires qui divergent :

![graphe de dépendances suite](github-feature-6.png)


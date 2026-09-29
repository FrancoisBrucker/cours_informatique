---
layout: layout/post.njk
title: "Projet github : commits"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Nous allons maintenant modifier le fichier `readme.md`{.fichier} qui est aussi un fichier texte écrit [au format Markdown](https://docs.github.com/fr/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). Pour que ce fichier soit agréable à la lecture, github le compile en html, mais — en vrai — c'est juste du texte.

## Modification du fichier readme

1. ![cliquer pour accéder au fichier `readme.md`](github-modification-readme-1.png)
2. ![cliquer pour éditer le fichier `readme.md`](github-modification-readme-2.png)
3. ![édition du fichier `readme.md`](github-modification-readme-3.png)
4. ![modification du fichier `readme.md`](github-modification-readme-4.1.png)

On peut maintenant le commit :

![commit du fichier `readme.md`](github-modification-readme-4.2.png)


1. Notre fichier modifié est maintenant ![fichier](github-modification-readme-5.1.png)
2. Son historique montre qu'il a été modifié par 2 commit ![fichier](github-modification-readme-5.2.png)
3. Le dernier commit a modifié son contenu ![fichier](github-modification-readme-5.3.png)

L'index qui permet de voir les différences entre ce qu'on a sauvegarder et ce qu'on va ajouter. L'index est transparent pour l'instant mais plus on progressera plus il sera visible.


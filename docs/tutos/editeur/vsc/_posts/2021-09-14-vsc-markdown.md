---
layout: page
title:  "vsc et markdown"
categories: 
    - installation 
    - configuration
    - markdown
---

Comment écrire du markdown avec [visual studio code](https://code.visualstudio.com/) (vsc).

<!--more-->

> TBD : ajouter le latex.
{: .note}

## extensions génériques

La documentation comporte une [partie consacrée au markdown](https://code.visualstudio.com/docs/languages/markdown). Nous allons utiliser deux extensions :

* [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) qui permet de fluidifier l'écriture de markdown et permet un export de celui-ci en html.
* [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) qui souligne en orange les fautes de style (un espace après un `.` par exemple) et les erreurs de markdown (sauf dans la hiérarchie des paragraphes par exemple).

> Le seconde extension est un [linter](https://mindsers.blog/fr/post/linting-good-practices/), qui incite à utiliser les bonnes pratiques d'écriture. Il en existe pour quasi tous les langages.

### export et preview

Pour exporter le markdown dans quelque chose de plus joli. On peut utiliser la [palette de commande]({% post_url tutos/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main %}#palette-de-commande) pour exétuter les commandes :

* *markdown All in One: Print current document to HTML* : qui va rednre un fichier html
* *markdown: Open preview* pour faire une preview.

## extensions specifiques

* [Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/) Permet d'avoir des feuilles de styles jolies lorsque l'on converti du markdown.

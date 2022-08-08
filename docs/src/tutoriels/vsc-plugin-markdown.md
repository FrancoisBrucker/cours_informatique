---
layout: layout/post.njk 
title: Vsc plugin Markdown

tags: ['vsc', 'tutoriel', 'markdown']
---

{% pres-requis %}
* vsc
{% endpres-requis %}

> TBD : fix prés-requis

<!-- début résumé -->

Écrire et *compiler* du markdown avec vsc.

<!-- fin résumé -->


L'éditeur de texte [vscode](https://code.visualstudio.com/) permet d'écrire et d'exporter facilement du markdown. Sa documentation comporte une [partie consacrée au markdown](https://code.visualstudio.com/docs/languages/markdown). 


## installation des plugins 

Nous allons utiliser deux extensions :

* [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) qui permet de fluidifier l'écriture de markdown et permet un export de celui-ci en html.
* [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint), un [linter](https://mindsers.blog/fr/post/linting-good-practices/) qui souligne en jaune les fautes de style de markdown (saut dans la hiérarchie des sections par exemple) pour que vous puissiez les corriger et écrire parfaitement du markdown

> Installez les deux plugins ci-dessus dans votre vscode.
{.a-faire}

## export en html

Si le markdown est pratique pour être écrit et lu rapidement, pour de long documents ou le partage de ceux-ci, il est important de les exporter dans un format comme le html.

Avec le plugin *Markdown All in One* de vscode, il suffit de taper la commande :

```text
markdown All in One: Print current document to HTML
```

dans la [palette de commande](../vsc-installation-et-prise-en-main#palette-de-commande) (que l'on peut copier/coller). Ceci va créer un fichier html contenant votre code markdown *compilé*.

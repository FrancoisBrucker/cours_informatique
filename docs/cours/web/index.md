---
layout: page
title:  "Web"
category: cours
author: "François Brucker"
---

## But

Ce cours, tente de donner des notions de développement web. 

> TBD : en chantier
{: .note}


## Prérequis

Quelques outils sont nécessaires pour pouvoir faire du développement web. Installez les sur votre ordinateur. Vous pouvez bien sur utiliser d'autres outils que ceux utiliés dans ce cours, mais si vous n'êtes pas à l'aise avec ce qu'on va voir préférez ceux préconisés.

Pour démarrer : 

* un navigateur web possédant des outils de développement. J'utilise [chrome](https://www.google.fr/chrome/)
* un éditeur de texte à tout faire ([vim](https://www.vim.org/) sous linux, [textmate](https://macromates.com/) sous osx ou [notepad++](https://notepad-plus-plus.org/) sous windows par exemple)

Plus tard : 
* avoir accès au [terminal]({% post_url tutos/systeme/2021-08-24-terminal %})
* posséder [un vrai éditeur de texte]({% post_url tutos/editeur/vsc/2021-09-03-vsc-installation-et-configuration %})

## Introduction

Lorsque l'on ouvre une fenêtre du navigateur chrome, dans le haut de la fenêtre il y a un champ où l'on peut marquer du texte. Il y est, avant que l'on écrive,  marqué : *"Effectuez une recherche sur google ou saisissez une URL"*.

On pet ainsi taper du texte qui sera, si ce n'est pas une url, interprétée comme une recherche google. Tapons : `URL` puis appuyons sur la touche entrée. 

Bon. Ce n'est vraisemblablement pas une URL qu'on a tapé puisque l'on obtient le résultat d'une recherche google. Allons sur le 1er lien proposé, qui est chez moi celui-là : <https://fr.wikipedia.org/wiki/Uniform_Resource_Locator>, et qui est une URL nous dirigeant vers la définition d'une URL.

### url 

Vous pouvez suivre cette petite [intruction aux URLs]({% link cours/web/tuto_url.md %}).

### html/css/js

Tout le web tourne autour du trio html (pour la structure des page), css (pour la mise en forme de la page) et le javascript (pour le dynamisme de la page). Avant de les étudier en détail, vous pouvez faire ce petit [tuto introductif]({% link cours/web/tuto_html_css_js.md %}) pour voir un peut de quoi il en retourne.


### outils de développement

L'informatique en général et le web en particulier sont des sciences incarnées. C'est à dire que le code produit un résultat et ce n'est que lorsque ce que l'on pense faire (le code) est conforme à la réalité (ce qu'il produit réellement) que l'on est content. 

Il faudra donc sans cesse exécuter votre code (ici voir le résulta dans un navigateur) pour être sur que tout se passe comme prévu.

> Si vous n'avez pas exécuté votre code depuis 10min, vous pouvez être sur qu'il ne fonctionne plus.
{: .attention}

POur vous aider a comprendre comment votre code est exécuté, les navigateurs mettent à votre disposition des outils de développements. **Utilisez les** ! ils vous feront gagner un temps précieux. 

Vous pouvez [suivre ce tuto]({% link cours/web/tuto_outils_dev.md %}) pour voir comment ils fonctionnent.


## plan du cours

> TBD
{: .note}

### serveur et navigateur web niveau 1



1. url comme protocole/serveur/ressource
2. fichier dan une url (avec exemple bonjour monde)
3. interprétation par le navigateur( test avec un docx ?)
4. expérimentation avec les outils de développement

> pas forcément du html/css, on peut transmettre ce qu'on veut par les tuyaux d'internet

* navigateur [url](https://fr.wikipedia.org/wiki/Uniform_Resource_Locator) (ou [uri](https://fr.wikipedia.org/wiki/Uniform_Resource_Identifier) ) et serveur
* interpréter l'url en html/css/js
* réseau ? adresse d'u serveur ? ports d'un ordinateur ? (dans serveur)
* normes et rfc (pour aller plus loin ?)
* récupérer un fichier sur ordi avec son terminal (pour aller plus loin ?)

### technos mise en œuvre

### Front

[Front]({% link cours/web/front/index.md %})


### javascript

[cours]({% link cours/web/js/index.md %})

### Back

[Back]({% link cours/web/back/index.md %})


### serveur et navigateur web niveau 2
---
layout: page
title:  ""
category: cours
tags: combat web
author: Baptiste Mahé
---
![Jekyll logo](../../assets/jekyll_logo.png)

## Qu'est-ce que c'est ?

[Jekyll](https://jekyllrb.com/) est un `générateur` de site statique à partir de languages qui ne sont pas lu par le navigateur (type Marckdown et Yaln). Jekyll est écrit en [Ruby](https://www.ruby-lang.org/fr/) et requiert le programme `gem` pour l'installation.

## Installation

Installer Ruby :
~~~ sh
sudo apt install ruby-full
~~~

En plus de Ruby il va nous falloir les programmes de compilation en C et C++, si vous ne les avez pas encore :
~~~ sh
sudo apt install make gcc g++
~~~

Gem est le progamme d'installation de logiciels Ruby nous allons l'utiliser pour installer Jekyll :
~~~ sh
sudo gem install bundler jekyll
~~~

Pour tester l'installation :
~~~ sh
jekyll -v
~~~
vous devriez obtenir quelque chose comme : `jekyll 4.X.X`

## Quelques fonctionalités

**Créer** un projet Jekyll :
~~~ sh
sudo jekyll new my-jekyll-site
~~~
 
Démarrer un **server local** pour développer le projet Jeckyll
~~~ sh
cd my-jekyll-site
bundle exec jekyll serve
~~~
(executer cette commande dans le dossier cours_informatique/docs/ pour servir le site de M. Brucker)

Ensuite naviguer à l'adresse `http://127.0.0.1:4000` avec votre navigateur et votre site Jekyll devrait y être affiché. (rajouter `/cours_informatiques/` pour le site de M. Brucker)

Une fois l'application fini il faut la **compiler** en html pour qu'elle soit comprise par le navigateur en production :
~~~ sh
bundle exec jekyll build
~~~
Cette commande créer un dossier `_site` où le site compilé sera stocké.

## Le langage Markdown

Dans notre site Jekyll il va falloir "coder" en Markdown. Comme le HTML le Markdown et un langage de **balisage** qui se veut être facile à lire par les humains (mais du coup moins facile pour les navigateurs...).

C'est le langages de base des fichiers README sur GitHub. Les fichiers `.md` et `.marckdown` sont les fichiers interprétés en Markdown.

Jekyll utilise un sous-type de Markdown, le **kramdown** de Github.

Une bonne overview de Markdown [ici](https://guides.github.com/features/mastering-markdown/)

## La configuration

La configuration du projet est contenu dans le fichier YAML `_config.yml` généré automatiquement par la création du projet jekyll. YAML ou Yet Another Markup Language, est un format de représentation des données comme XML.

*TODO: finir explications configs*

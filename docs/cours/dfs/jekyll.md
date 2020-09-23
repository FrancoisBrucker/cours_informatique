---
layout: page
title:  "Jekyll"
category: cours
tags: combat web
---

## Qu'est-ce que c'est ?

[Jekyll](https://jekyllrb.com/) est un `générateur` de site statique à partir de languages qui ne sont pas dédiés au web (type Marckdown et Yaln)? Jekyll est écrit en [Ruby](https://www.ruby-lang.org/fr/) et requiert le programme `gem` pour l'installation.

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
Cette commande créer un dossier `.jekyll-cache` où le site compilé sera stocké.

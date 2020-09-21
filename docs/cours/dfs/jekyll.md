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
---
layout: page
title: "Sass"
category: cours
tags: packaging sass web front
author: Adèle Bourgeix & Maxime Vivier 
---
# Sass, c'est quoi ?

Au fil du temps, les développeurs se sont rendus compte de la difficulté d'écrire des feuilles de style (.css) efficientes et optimisées: ces fichiers deviennent de plus en plus longs, complexes et difficiles de maintenir. Il est donc devenu évident qu'une solution était nécessaire. 

Sass est un préprocesseur CSS, une couche entre les feuilles de style que l'on écrit et les fichiers .css qui sont envoyés  au navigateur. Sass (abréviation de Syntactically Awesome Stylesheets) comble les lacunes de CSS en développant un langage permettant d'écrire du code DRY qui sera plus rapide, plus efficace et plus facile à maintenir.


> **Nota Bene** : c'est quoi le code DRY ? 
>
> DRY pour Don't Repeat Yourself c'est une "bonne pratique" de développement qui consiste à éviter la duplication des lignes de code pour permettre une optimisation de celui-ci. 


# Comment ça marche?

+ Sass permet la création de variables globales.
 
~~~ 
$font-stack:    Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}
~~~

Ici, la création des variables $font-stack et $primary-color permettent la réutilisation de la même police et de la même couleur à plusieurs endroits de la feuille de style. Si besoin est, il n'est pas nécessaire de devoir changer la couleur ou la police à chaque occurrence. 

+ Sass permet aussi l'encapsulation, impossible en .css. En effet, on peut se rendre compte rapidement de l'existence de cette encapsulation dans un fichier .html, il serait donc plus logique de réutiliser cette structure dans un fichier de style. 

fichier .scss de sass

~~~
nav {
  ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  li { display: inline-block; }

  a {
    display: block;
    padding: 6px 12px;
    text-decoration: none;
  }
}
~~~

fichier .css

~~~
nav ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
nav li {
  display: inline-block;
}
nav a {
  display: block;
  padding: 6px 12px;
  text-decoration: none;
}
~~~


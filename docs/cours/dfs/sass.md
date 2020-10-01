---
layout: page
title: "Sass"
category: cours
tags: packaging sass web front
authors:
	- "Adèle Bourgeix"
	- "Maxime Vivier"
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

fichier **styles.scss** de sass: 

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

fichier **styles.css** généré après compilation: 

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

+ Sass permet aussi de découper les feuilles de style en plusieurs fichiers et permer de charger différents fichiers Sass comme des modules. On peut donc accéder à la fois aux variables et fonctions d'autres feuilles de style. 

fichier **base.scss** de Sass qui pose des règles de base pour l'ensemble du corps de texte:

~~~
$font-stack:    Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}
~~~

fichier **styles.scss** de sass qui réutilise le style imposé par le fichier base.scss:

~~~
@use 'base';

.inverse {
  background-color: base.$primary-color;
  color: white;
}
~~~

génèrent le fichier **styles.css** suivant: 

~~~
body {
  font: 100% Helvetica, sans-serif;
  color: #333;
}

.inverse {
  background-color: #333;
  color: white;
}
~~~

> **Nota Bene**: En programmation orientée objet, l'héritage est le principe selon lequel les classes filles héritent des propriété des classes mères. 

+ Sass permet aussi de réutiliser le concept d'héritage : des propriétés peuvent se partager d'un selecteur à l'autre. 

Par exemple le fichier **styles.scss** suivant : 

~~~
%message-shared {
  border: 1px solid #ccc;
  padding: 10px;
  color: #333;
}

%equal-heights {
  display: flex;
  flex-wrap: wrap;
}

.message {
  @extend %message-shared;
}

.success {
  @extend %message-shared;
  border-color: green;
}

.error {
  @extend %message-shared;
  border-color: red;
}

.warning {
  @extend %message-shared;
  border-color: yellow;
}

~~~

génère le fichier **styles.css** suivant après compilation: 

~~~
.message, .success, .error, .warning {
  border: 1px solid #ccc;
  padding: 10px;
  color: #333;
}

.success {
  border-color: green;
}

.error {
  border-color: red;
}

.warning {
  border-color: yellow;
}
~~~

> **Nota Bene:** On peut remarquer que la classe equal-heights ne sera générée car elle n'est jamais "étendue". 

> **Nota Bene**: Les classes success, error et warning héritent donc toutes les trois des propriétés de la classe message, qui a son tour hérite de la classe message-shared.


+ Finalement, Sass permet l'introduction d'opérateurs mathématiques comme + - /.

Par exemple, ce fichier **styles.scss**: 

~~~
.container {
  width: 100%;
}

article[role="main"] {
  float: left;
  width: 600px / 960px * 100%;
}

aside[role="complementary"] {
  float: right;
  width: 300px / 960px * 100%;
}
~~~

permet de génerer le fichier **styles.css** suivant : 

~~~
.container {
  width: 100%;
}

article[role="main"] {
  float: left;
  width: 62.5%;
}

aside[role="complementary"] {
  float: right;
  width: 31.25%;
}
~~~

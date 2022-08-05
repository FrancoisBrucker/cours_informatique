---
layout: page
title: "Sass"
category: cours
tags: packaging sass web front
authors:
  - "Adèle Bourgeix - 2020/2021"
  - "Maxime Vivier - 2020/2021"
  - "William Templeton - 2021/2022"
  - "Victoire Flesselles - 2021/2022"
---
# Sass, qu'est-ce que c'est ?

Au fil du temps, les développeurs se sont rendus compte de la difficulté d'écrire des feuilles de style (.css) efficientes et optimisées: ces fichiers deviennent de plus en plus longs, complexes et difficiles de maintenir. Il est donc devenu évident qu'une solution était nécessaire. 

Sass (Syntactically awesome stylsheets) est un préprocesseur CSS, une couche entre les feuilles de style que l'on écrit et les fichiers .css qui sont envoyés  au navigateur. Sass comble les lacunes de CSS en développant un langage permettant d'écrire du code DRY qui sera plus rapide, plus efficace et plus facile à maintenir.


> **Nota Bene** : c'est quoi le code DRY ? 
>
> DRY pour Don't Repeat Yourself c'est une "bonne pratique" de développement qui consiste à éviter la duplication des lignes de code pour permettre une optimisation de celui-ci. 


Sass permet de convertir le code SCSS en code CSS. Il possède de nombreuses fonctionnalités qui n'existent pas dans CSS. Nous allons en étudier quelques-unes dans ce cours.

# Installer Sass

[Installer Sass](https://sass-lang.com/install)

# Fonctionnalités

## Variables

+ Sass permet la création de variables globales. Les variables commencent avec le symbole dollar **$** et leur affection avec les deux-points **:**.
 
~~~ 
$font-stack:    Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}
~~~

Ici, la création des variables $font-stack et $primary-color permettent la réutilisation de la même police et de la même couleur à plusieurs endroits de la feuille de style. Si besoin est, il n'est pas nécessaire de devoir changer la couleur ou la police à chaque occurrence. Cela est très pratique, notamment pour maintenir la cohérence d'une charte graphique. 

## Encapsulation

+ Sass permet aussi l'encapsulation, impossible en .css. Dans un fichier .html, le code est écrit de façon encapsulé. Or, dans un fichier .css, la structure du code n'est pas la même. Il serait donc plus logique de réutiliser cette structure encapsulée du .html dans le fichier de style associé. On garde ainsi la même structure de construction ce qui permet de gagner en lisibilité, c'est un vrai gain de temps pour la maintenance du site. 

fichier **index.html**
~~~

<html>
  <body>
    <main>
      <h1 class="title">Calculatrice</h1>
			<div class="calculator">Nous créérons ici le cadre de la calculatrice.</div>
    </main>
   </body>
</html>

~~~

fichier **styles.scss** de sass: 

~~~
body {
    text-align: center;
    padding: 0;
    margin: 0;
    min-height: 100vh;
    font-family: "Montserrat", sans-serif;
    background-color: #b8c6db;
    background-image: linear-gradient(315deg, #b8c6db 0%, #f5f7fa 74%);
}
    main {
    width: min-content;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
      .title {
        margin: 50px 0 10px;
        font-size: 3.5em;
        text-transform: uppercase;
        font-weight: lighter;
      }
      .calculator{
        width: $main-width;
        padding: 20px;
        background: #efefef;
        border-radius: .5rem;
        box-shadow: 10px 10px 40px rgba(0, 0, 0, 0.2);
        display: grid;
        grid-template-areas:
                        "result result"
                        "number-inputs operators"
                        "bottom-rank bottom-rank";
        grid-template-columns: 3fr 1fr;
      }
    }
}          
~~~

fichier **styles.css** généré après compilation: 

~~~
body {
  text-align: center;
  padding: 0;
  margin: 0;
  min-height: 100vh;
  font-family: "Montserrat", sans-serif;
  background-color: #b8c6db;
  background-image: linear-gradient(315deg, #b8c6db 0%, #f5f7fa 74%);
}

main {
  width: -webkit-min-content;
  width: -moz-min-content;
  width: min-content;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}
main .title {
  margin: 50px 0 10px;
  font-size: 3.5em;
  text-transform: uppercase;
  font-weight: lighter;
}
main .calculator {
  width: 450px;
  padding: 20px;
  background: #efefef;
  border-radius: 0.5rem;
  box-shadow: 10px 10px 40px rgba(0, 0, 0, 0.2);
  display: grid;
  grid-template-areas: "result result" "number-inputs operators" "bottom-rank bottom-rank";
  grid-template-columns: 3fr 1fr;
}
~~~
## Modules

 Sass permet aussi de découper les feuilles de style en plusieurs fichiers et permet de charger différents fichiers Sass comme des modules. On peut donc accéder à la fois aux variables, mixins et fonctions d'autres feuilles de style. 


Fichier **base.scss** de Sass qui pose des règles de base pour l'ensemble du corps de texte:

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

L'appel à un fichier Sass se fait sous la forme *@use 'nom du fichier*. Il n'y a pas besoin d'inclure l'extension de fichier, Sass a compris tout seul qu'il devait ici utiliser le module *base* qui se trouve dans le fichier *styles.scss*.


## Mélanges

Le *mixin* permet de créer des groupes de déclarations CSS réutilisables dans tout le site.

L'exemple ci-dessous permet de définir le thème qui pourra être utilisé dès qu'il y a besoin.

Fichier en **theme.scss**
~~~
@mixin theme($theme: DarkGray) {
  background: $theme;
  box-shadow: 0 0 1px rgba($theme, .25);
  color: #fff;
}

.info {
  @include theme;
}
.alert {
  @include theme($theme: DarkRed);
}
.success {
  @include theme($theme: DarkGreen);
}
~~~

génère le fichier **theme.css**

~~~
.info {
  background: DarkGray;
  box-shadow: 0 0 1px rgba(169, 169, 169, 0.25);
  color: #fff;
}

.alert {
  background: DarkRed;
  box-shadow: 0 0 1px rgba(139, 0, 0, 0.25);
  color: #fff;
}

.success {
  background: DarkGreen;
  box-shadow: 0 0 1px rgba(0, 100, 0, 0.25);
  color: #fff;
}
~~~

On créé le mixin avec le symbole **@**, on peut éventuellement ajouter des variables dans les parenthèses **($nomvariable: valeurpardéfaut)**. On appelle ensuite le mixin **@include nommixin** et éventuellement on modifie les variables.

## Héritage

> **Nota Bene**: En programmation orientée objet, l'héritage est le principe selon lequel les classes filles héritent des propriété des classes mères. 

Sass permet aussi de réutiliser le concept d'héritage : des propriétés peuvent se partager d'un sélecteur à l'autre. 

L'exemple ci-dessous permet d'afficher des messages de succès, d'erreur, ou d'avertissement dont la seule propriété qui change est la couleur.

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

## Opérateurs

Sass permet l'introduction d'opérateurs mathématiques comme **+ - * /**.

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

permet de générer le fichier **styles.css** suivant : 

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

Ici, l'intérêt des opérateurs est de convertir des pixels en pourcentages.

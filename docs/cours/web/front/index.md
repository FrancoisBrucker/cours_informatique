---
layout: page
title:  "Web Front"
category: cours
tags: informatique graphes
author: "François Brucker"
---

## Introduction

Web front

> TBD : en chantier
{: .note}

## refs possible 

* <https://www.internetingishard.com/>
* <https://sequelize.org/master/>
* <https://fr.learnlayout.com/>
* <https://www.sqlitetutorial.net/sqlite-nodejs/>
* <https://www.tutorialspoint.com/javascript/index.htm>
* <https://javascript.info/>
* <https://nodejs.org/en/>
* <https://www.theodinproject.com/courses/html-and-css>
* <https://shopify.github.io/liquid/basics/types/>
* <https://getshogun.com/learn/shopify-liquid-tutorial>
* <https://github.com/janl/mustache.js/>
* <https://observablehq.com/@d3/learn-d3-by-example?collection=@d3/learn-d3>
* <https://observablehq.com/@d3/learn-d3-by-example?collection=@d3/learn-d3>


### js 

> TBD : à modifier. C'est l'exemple initial du tuto js qui était trop compliqué pour une initiation.
{: .note}

## js

> TBD : mettre l'usage d'un array ici. Puis parler de jquery comme exemple d'import. t broder sur local/cdn/node_modules.
{: .note}

### compliquons les choses

Imaginons maintenant que nous n'avons plus un seul div, mais deux.

~~~~html
<!doctype html>
<html lang="fr">
  <head>
      <title>Ma Page</title>
  </head>
  <body>
    <style>
        html, body {
            margin: 0;
            padding:0;
        }
        .milieu {
            margin: 10px auto;
            height: 50px;
            width: 20px;
        }
        .color {
            background-color: red;
        }
    </style>

    <div id="mon_div" class="milieu color"></div>

    <div id="div2" class="milieu color"></div>
  </body>
</html>
~~~~

Cette fois on souhaite pouvoir changer la couleur de nos **DEUX** div, alors pourquoi pas attraper les éléments par `class` plutôt que par `id` ?

~~~~~html
<script>
    bleu = false;
    document.getElementsByClassName("color").onclick = function() {
        if(bleu){
            bleu=false;
            document.getElementsByClassName("color").style.backgroundColor = "red"
        }
        else{
            bleu=true;
            document.getElementsByClassName("color").style.backgroundColor = "blue"
        }
    }
</script>
~~~~~

Malheureusement ce code ne code ne fonctionne pas. En effet la fonction `getElementsByClassName` renvoie un array et le reste du code n'est pas applicable tel quel à un array.
Si l'on souhaite faire exactement la même chose mais cette fois sur tous les éléments de la classe ``.color`` il faut passer par une boucle sur les éléments de l'array.

~~~~~html
<script>
    var array = document.getElementsByClassName("color");
    blue = false;
    function change (){
        if(blue){
            bleu=false;
            this.style.backgroundColor= "red"
        }
        else{
            blue=true;
            this.style.backgroundColor= "blue"
        }
        }

    for (let element of array ){
        element.onclick = change
    }
</script>
~~~~~

Cela devient vite compliqué, on préfère alors utiliser des bibliothèques, comme [jQuery](https://jquery.com).

Cela nous permet de simplifier un peu la syntaxe, mais aussi de nous faciliter la vie. 
On va reprendre l'exemple pour illustrer l'utilité d'une bibliothèque telle que jQuery.

### bibliothèque jquery

Ce qui est assez long à écrire, o peut alors utilsier des bibliothèques, comme la bibliothèque jQuery par exemple, qui prend en charge ce genre de problème.

Pour pouvoir l'utiliser il faut d'abord l'importer, ici on va passer pas un [cdn](https://en.wikipedia.org/wiki/Content_delivery_network)

~~~~html
<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>

<script>
    blue=false;
    $(".color").click(function (){
        if(red){
            blue=false;
            $(this).css("backgroundColor","red");
        }
        else{
            blue=true;
            $(this).css("backgroundColor","blue");
        }

    })
</script>
~~~~

Ici on retrouve le code écrit en jQuery, il a exactement la même fonctionnalité que l'exemple précédent. On remarque bien que l'on n'a pas besoin de passer par la boucle `for`, elle est caché dans l'appel de la méthode `click`. La fonction en paramètre de click est utilisée pour toute balise satisfaisant le critère, ici qu'elle soit de classe `color`.

Pour en savoir plus sur l'utilisation de jQuery, il existe de nombreux tutos sur l'internet mondial : 
* <https://www.digitalocean.com/community/tutorials/an-introduction-to-jquery>
* <https://www.youtube.com/playlist?list=PL4cUxeGkcC9hNUJ0j6ccnOAcJIPoTRpO4>




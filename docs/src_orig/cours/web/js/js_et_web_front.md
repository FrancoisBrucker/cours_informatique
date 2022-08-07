---
layout: page
title:  "javascript pour le web front"
category: cours
author: "François Brucker"
---


L'utilisation de javascript dans le web a 3 but : 

* manipulation de l'arbre DOM : modifications des blocs HTML et des propriétés CSS
* programmation évènementielle : on réagit à des actions de l’utilisateur
* transfert d’information entre le client et le serveur ([ajax](https://www.webexmachina.fr/article/2018/08/utilisation-ajax-developpement-web.html)). C'est déjà une technique avancée, non pas parce que c'est compliqué une fois que ça marche mais parce qu'il y a plein de raisons pour que ça rate.

Vous avez déjà vu un peu comment utiliser le javascrpt dans le web grâce [au tutorial html/css/js]({% link cours/web/tuto_html_css_js.md %}) et aux [bases du javascript]({% link cours/web/js/bases.md %}).

Nous allons ici plus particulièrement parler de ce qui est spécifique au web :

* chargement de bibliothèque js dans le web (direct, cdn, node_modules front)
* échanges de données ajax / json 
*  utilisation des évènements 
*  modification de l'arbre dom
*  gestion des callbacks (promise)

> TBD
{.note}

## chargement de libs

exemple de jquery.

1. direct via un script. ON peut en parler ensuite
2. cdn
3. node_modules

## données

1. fichier distant chargement :
   1. texte
   2. json (avec conversion d'un objet js)
2. download

doit avoir un serveur pour que ça marche. Exemple en python tout couillon.

## évènement

reprendre cours ? Attention a prevent default

## arbre dom

dans le tuto. Jouer avec hidden ? OU charger ds données avec placeholder puis chargement

## gestion des callbacks

promise ?

## old

> TBD : vieux truc à ranger dans les nouvelles sections
{.note}

### manipulation de l'arbre dom 

```html
<html>
    <head>
      <title>Magie javascript</title>


    </head>
    <body>
      <style>
        html, body {
          margin: 0;
          padding:0;

          background: skyblue;
          color: #FFFFFF;
          font-size: 2em;
          text-align: center;
        }
        .milieu {
          margin: 10px auto;
          height: 50px;
          width: 20px;
        }
        .color {
          background-color: olive;
        }
      </style>

      <h1> Enfin du web !</h1>
      <p> et on aime ça</p>
      <div id="mon_div" class="milieu color"></div>

      <script>
        document.getElementById("mon_div").onclick = function() {
          document.getElementById("mon_div").style.backgroundColor = "blue"
        }

      </script>
    </body>
  </html>
``` 

> **Testez ce code.**  Que fait-il ? Et pourquoi ?


On a mis le code en fin de fichier parce qu'il est exécuté dès qu'il est vu. Si on l'avait exécuté au début les blocs n'existaient pas encore et le [`document.getElementById`](https://developer.mozilla.org/fr/docs/Web/API/Document/getElementById) n'aurait rien trouvé.


### gestion des évènements

Remplacez la partie script de l'exemple précédent par le code suivant : 

```html
 <script>
    blue = false;
    document.getElementById("mon_div").onclick = function() {
      if (blue) {
        blue = false;
        document.getElementById("mon_div").style.backgroundColor = "olive"
      }
      else {
        blue = true;
        document.getElementById("mon_div").style.backgroundColor = "blue"
      }

    }
  </script>
``` 

> **Testez ce code.**  Que fait-il ?

On a associé une fonction à un évènement, ici le fait de cliquer sur un élément donné (le `div` d'`id` `#mon_div`). On voit bien ici l'utilité d'une fonction anonyme, et en creux l'utilisation d'une variable globale (on modifie `blue` dans une fonction. Ce n'est pas possible en python par exemple)

## bibliothèques

La gestion de l'arbre DOM à la main en javascript est assez lourde. On préfèrera toujours utiliser une bibliothèque. C'est <https://jquery.com/> qui est la plus utilisée pour ce genre de chose. Elle est quasi-systématiquement incluse par les bibliothèques javascript.


### Chargement de jquery

> **exemple** : fichier [`hello_jquery.html`](./javascript_files/hello_jquery.html). Ouvrez le dans un navigateur et un éditeur


Pour l'instant on a juste chargé `jquery` via son `cdn`. On a utilisé une version [minifiée](https://fr.wikipedia.org/wiki/Minification) pour gagner du temps de chargement.

On va utiliser la console pour se familiariser avec la sélection d'élément via jquery. Elle se fait toujours par un sélecteur css entouré d'un dollar suivi d'une méthode à exécuter. Par exemple : `console.log($("p").html())`

> **A faire dans la console** : 

>* le faire dans la console : `$("p").html();`
>* changez le html du paragraphe : `$("p").html("coucou les gars ");`



> **En utilisant l'aide de jquery (`https://api.jquery.com/`)** :
>
>* Changez la couleur (méthode `css`) du titre  (réponse `$("h1").css("color", "olive")`)
>* quelle est la largeur du `h1` ? (réponse : `$("h1").width()`)
>* la changer en 50% de la hauteur totale. (réponse : `$("h1").width("50%")`)



> **Réponses** : 
>
>* `$("h1").css("color", "olive")`
>* `$("h1").width()`
>* `$("h1").width("50%")`


### gestion des évènements

On utilise souvent le javascript et jquery pour réagir aux évènements :

> **exemple** : le fichier [`evenements_jquery.html`](./javascript_files/evenements_jquery.html) contient le code ci-dessous :

faire l'exemple petit à petit : 

1. un p et mouseenter, mouseleave
2. hover
3. mettre le code en haut
4. plusieurs éléments avec une liste
5. charger une liste avec js


```
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Chargement de la bibliothèque jquery</title>


        <style>
            html, body {
                margin:0;
                padding:0;

                background: skyblue;
                color: #FFFFFF;
                font-size: 2em;
                text-align: center;
            }
        </style>

        <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
		<script src="./mes_donnees.js"></script>
		<script>
			$(function() {
				
				liste = $("<ul>")
				
				for (i=0; i < valeurs.length; i += 1) {
					ligne = $("<li>")
					ligne.text(valeurs[i])
					liste.append(ligne)					
				}
				
				// valeurs.forEach(function(v) {
				// 	console.log(v)
				// })
				
				$("body").append(liste)
				
				$("li").mouseenter(function() { 
					$(this).css("color", "red")						
				})				
				$("li").mouseleave(function() {
					$(this).css("color","white")						
				})				

			})
		</script>		

    </head>
    <body>
        <h1>Enfin du web !</h1>
        <p>Et on aime ça.</p>
	
    </body>
</html>

```


```html
<!doctype html>
    <html>
        <head>
            <meta charset="utf-8" />
            <title>Magie jquery</title>

            <style>
                html, body {
                    margin:0;
                    padding:0;

                    background: skyblue;
                    color: #FFFFFF;
                    font-size: 2em;
                    text-align: center;
                }
            </style>

            <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
            <script>
                $(function() {
                    $("p").hover(
                        function() {
                            $(this).css("text-decoration", "underline")
                        },
                        function() {
                            $(this).css("text-decoration", "none")
                        }
                    )
                })
            </script>

        </head>
        <body>
            <h1>Enfin du web !</h1>
            <p>Et on aime ça.</p>
        </body>
    </html>
```

> **testez** ce code. Que fait-il ? 


Ce code fonctionne alors qu'il est au début du html ? Oui parce que le code est un paramètre (la fonction) passée en argument de jquery [`$(paramètre)`](https://learn.jquery.com/using-jquery-core/document-ready/). Ce paramètre n'est exécuté que lorsque la page est chargée (le texte, les image et tout le reste). C'est toujours comme ça que l'on utilisera jquery.


Utilisation du nom `$(this)` qui, comme en java signifie : l'objet courant. Ici le paragraphe qui est à l'origine de l'exécution de la fonction.

>**A vous** : faites en sorte que lorsque l'on clique sur le titre il s'ajoute "coucou !". 


> **Solution** :

>1. utiliser la méthode `click` pour afficher `coucou` dans la console lorsque l'on clique suer le titre `$("h1").click(function() {console.log("coucou")})`
>2. utiliser la méthode `click` pour afficher le contenu de h1 dans la console lorsque l'on clique suer le titre (utilisez `this`) `$("h1").click(function() {console.log($(this).html())})`
>3. remarquez que les 2 évènement continuent de fonctionner, le second n'a pas effacé le premier. Rechargez la page.
>4. finir le boulot : `$("h1").click(function() {console.log($(this).html($(this).html() + "coucou !"))})`


## js

> TBD : mettre l'usage d'un array ici. Puis parler de jquery comme exemple d'import. t broder sur local/cdn/node_modules.
{.note}

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

> TBD : faire un array de boolean
{.danger}
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




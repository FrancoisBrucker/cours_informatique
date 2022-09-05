---
layout: page
title:  "html css js"
category: tutorial
tags: web
authors : 
  - "Yi Mei JIANG"
  - "Théophile BONNEAU"
  - François Brucker (corrections)
---

Un petit tutoriel pour faire sa première page liant html/css et js. Il suffit de copier/coller le code dans votre éditeur de texte favori, puis ouvrir le fichier dans un navigateur.

## html

### Les div 

Les `<div></div>` sont des blocs anonymes. Elles seront caractérisées uniquement par les `class` et les `id`. (ils seront expliqués dans la partie css)

Plusieurs éléments peuvent partager une même classe, mais un id est unique pour un élément.

> On utilise principalement les `<div></div>` pour structurer la page. 

## css

### fichier css

Une autre technique, plus propre, consiste à travailler directement dans un fichier css, lui-même relié au fichier html.

Tout d'abord, il faut créer un ficher `.css`. Vous pouvez par exemple le nommer `style.css`.
Une fois que c'est fait, il faut que vous reliez votre fichier html avec votre fichier css.
Pour cela, mettez vos deux fichiers dans un même dossier. Puis il faut rajouter dans la partie `head` de votre fichier html :

~~~~html
  <link rel="stylesheet" href="style.css" />
~~~~

Voila, maintenant votre fichier html est relié au fichier css. Vous pouvez commencer à mettre en page!

Par exemple, copier ce code dans votre ficher css :

~~~~css
p {
    color: red;
}
~~~~

### classes et id


Pour résoudre ce problème, il existe des solutions :

* *les classes* : qui peuvent être utilisées en même temps par plusieurs balises
* `les id* : qui doivent être uniques pour chaque élément.

### les classes 

Il s'agit d'un attribut que l'on peut mettre sur n'importe quelle balise 

~~~~html
<h1 class=""> </h1>
<p class=""> </p>
<img class="" />
~~~~

Comme valeur pour la classe, nous pouvons utiliser n'importe quel nom par exemple :

~~~~html
<h1 class="test"> ce titre est de la classe test</h1>
~~~~
on peut ensuite réutiliser ce nom pour changer l'affichage des balises de cette classe. Il suffit de le définir dans notre fichier CSS.

~~~~css
.test {
  font-size: 16px;
}
~~~~

Ainsi, toutes les balises de classe test auront un texte de taille 16 pixels.

> Une classe est un mot sans espace. Si vous écrivez par exemple `<h1 class="mon test"></h1>` cela signifie que votre `<h1></h1>` sera des deux classe `mon`et `test`. Cela est super pratique pour combiner les styles.

### les id

Ils s'utilisent de la même façon que les classes, à la différence qu'ils ne peuvent être utilisés que par une balise à la fois.

~~~~css
#logo {
  background-color : blue;
}
~~~~


La balise d'id logo aura donc un fond bleu.

> `id` signifie cet élément là précisément. N'utilisez pas le même `id` pour deux balises différentes (même si css ne vous en empêchera pas), c'est **bad karma** et ça vous retombera dessus tôt ou tard. Une bonne règle est de n'utilisez les `id` **que** pour désigner un objet précis à javascript, l'utilisez jamais pour désigner uniquement des propriétés css, utilisez les classes pour cela.



## js

> TBD : simplifier les exemple du js ?
{.note}

### modification de l'arbre dom

Lors de la génération d'une page html, on crée ce qu'on appelle un [arbre DOM (Document Object Model)](https://fr.wikipedia.org/wiki/Document_Object_Model) de la page.


Cet arbre contient tous les éléments html présents sur la page (plus de précisions [ici](https://www.w3schools.com/js/js_htmldom.asp)).
L'ajout d'un script javascript sur une page html permet de modifier cet arbre DOM, sans avoir besoin de recharger la page.
Ces modifications ce font via des événements : [https://www.w3schools.com/jsref/dom_obj_event.asp](https://www.w3schools.com/jsref/dom_obj_event.asp)

Prenons un exemple pour illustrer nos propos. Commençons par écrire dans un fichier *"rectangle.html"* le code suivant, que vous ouvrirez dans un chrome :

~~~html
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
      #mon_div {
        height: 50px;
        width: 20px;
      }

      .milieu {
        margin: 10px auto;
      }
      .color {
        background-color: red;
      }
    </style>

    <div id="mon_div" class="milieu color"></div>
  </body>
</html>
~~~

On y voit un rectangle rouge. Vous devriez comprendre ce qu'il se passe : 
* on a crée un `<div></div>` vide d'identifiant `mon_div`
* sans css, il serait de hauteur nulle (un `<div></div>` aura la hauteur de son contenu et la largeur de l'écran par défaut), mais on a ajouté du style pour :
  * qu'il soit rouge (la classe `color`)
  * qu'il ait une largeur et une hauteur (l'id `#mon_div`)
  * qu'il soit au centre (la classe `milieu`) avec la propriété [margin](https://www.w3schools.com/css/css_margin.asp) à 2 paramètres (le 1er paramètre c'est haut et bas (ici `10px` (px pour pixel)) et le second gauche et droite. `auto` voulant dire au milieu).

>Testez le code sans la balise style pour voir la différence 
{. note}


> `margin auto` ne marche que si la balise a une largeur. Si elle fait la taille de la fenêtre ce qui est le cas par défaut pour la balise `<div></div>` (en vrai, toutes les balises de type [display block](https://developer.mozilla.org/fr/docs/Glossary/Block/CSS)) `margin auto` ne fera rien puisqu'il n'y a rien à centrer.
{.attention}

Ajoutons du javascript qui va modifier l'arbre DOM. On va rendre notre rectangle bleu : 

~~~html
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
      #mon_div {
        height: 50px;
        width: 20px;
      }

      .milieu {
        margin: 10px auto;
      }
      .color {
        background-color: red;
      }
    </style>

    <div id="mon_div" class="milieu color"></div>

    <script>
      document.getElementById("mon_div").style.backgroundColor = "blue";
    </script>
  </body>
</html>
~~~

Magique, non ? Vous verrez, avec un peu d'entraînement, ça viendra tout seul. Il faut juste comprendre la notation pointée pour que cela devienne évident : on applique la propriété à droite du `.` à ce qu'il y a à gauche du point. Et ça se lit de droite à gauche : 

1. on affecte `"blue"` à la propriété `backgroundColor` de `document.getElementById("mon_div").style`
2. `document.getElementById("mon_div").style` est la propriété `style` de `document.getElementById("mon_div")`
3. `document.getElementById("mon_div")` est le résultat de la fonction `getElementById("mon_div")` appliquée à `document`.

On peut maintenant lire le tout dans l'ordre pour comprendre : On récupère l'élément d'identifiant `mon_div` du `document` et on change la propriété `backgroundColor` (propriété [background-color](https://developer.mozilla.org/fr/docs/Web/CSS/background-color) du css) de son style à `"blue"`.

> Le javascript, comme le html et le css d'ailleurs sont exécutés lorsqu'ils sont lu. Si vous mettez le script en début de la balise `<body></body>` ça ne marchera pas puisque le `<div></div>` d'id `#mon_div`n'exite pas encore.
> Teste le.
{.attention}

### évènements

Le javascript précédent, même s'il est bien d'un point de vue pédagogique, n'a pas vraiment de sens d'un point de vue pratique. Autant mettre  la propriété à `"blue"` tout de suite et *basta*. Le javascript prend tout son sens lorsqu'il se passe quelque chose dans la page. 

On va souvent utiliser le javascript de cette façon, en réaction à un évènement qui s'est produit sur la page : On appelle ça [la programmation évènementielle](https://developer.mozilla.org/fr/docs/Learn/JavaScript/Building_blocks/Events). 


Essayez le code suivant, en cliquant sur le rectangle rouge : 

~~~html
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
      #mon_div {
        height: 50px;
        width: 20px;
      }

      .milieu {
        margin: 10px auto;
      }
      .color {
        background-color: red;
      }
    </style>

    <div id="mon_div" class="milieu color"></div>

    <script>
      function changeCouleur() {
        document.getElementById("mon_div").style.backgroundColor = "blue";
      }
      document.getElementById("mon_div").onclick = changeCouleur;
    </script>
  </body>
</html>
~~~

On a fait exactement pareil que tout à l'heure, sauf que :
* on a affecté un comportement à un évènement ([onclick](https://developer.mozilla.org/fr/docs/Web/API/GlobalEventHandlers/onclick)) plutôt qu'à une propriété css
* on a affecté une fonction plutôt qu'une chaine de caractère


> une fonction est différent de son résultat. Dans l'exemple, `changeCouleur` est la fonction, `changeCouleur()` est le résultat de son exécution. On affecte une fonction à un évènement, pas son exécution.
{. attention}

Comme on va passer son temps à créer des fonction qui ne vont être utilisées que lors d'un évènement, javascript permet d'écrire ce que l'on nomme des [fonction anonyme](http://www.coursweb.ch/javascript/anonymous-functions.html) (elles n'ont pas de nom). Remplacez la balise script par ce qui suit pour voir comment définir et utiliser une fonction anonyme :

```html
<script>
  document.getElementById("mon_div").onclick = function() {
    document.getElementById("mon_div").style.backgroundColor = "blue"
  }      
</script>
```

Vous voyez, c'est simple, on défini directement une fonction avec le mot clé `function` ses paramètres (ici il n'y en a pas donc on écrit juste `()`) et le corps e la fonction entre `{}`.


### garder en mémoire des changements

Si l'on veut pouvoir recliquer sur le rectangle pour faire repasser sa couleur à rouge, il faut se rappeler de sa couleur actuelle. Par exemple : 


```html
<script>
  est_bleu = false;
  document.getElementById("mon_div").onclick = function() {
    if(est_bleu){
        est_bleu = false;
        document.getElementById("mon_div").style.backgroundColor = "red"
    }
    else{
        est_bleu = true;
        document.getElementById("mon_div").style.backgroundColor = "blue"
    }
  }
</script>
```

> En javascript, une variable est globale par défaut. C'est à dire qu'on peu en parler et la modifier partout. 
> Dans le code ci-dessus par exemple, on modifie la variable dans une fonction alors que celle-ci n'est pas défini dans la fonction. 
> Cela ne fonctionne **qu'en javascript**.
{.attention}





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

Le html est un langage à balises, par exemple `<head></head>` `<body></body>`. Il y a des balises ouvrantes et fermantes, marquées par un `/`.\


>[Liste des balises html](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1608357-memento-des-balises-html)

Dans le tutoriel suivant le navigateur interprétera directement le fichier sans passer par un serveur.
Il trouve le fichier à afficher via une [uri](https://fr.wikipedia.org/wiki/Uniform_Resource_Identifier) : `file://chemin/absolu/vers/fichier.html`. \
On ne traitera pas tous les détails depuis la base de la base. \
Il existe pleins de tutos pour apprendre les bases sur l'internet mondial :

* <https://www.internetingishard.com/>
* <https://www.theodinproject.com/courses/html-and-css>
* <https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web>
* le <http://www.thenetninja.co.uk/> a plein de tutos sur le web.
* <http://www.w3schools.com/> est le site de référence sur tout ce qui concerne html/css.


> Avant de choisir un tuto, Vérifier bien cependant qu'ils traitent de la dernière version, ici html5 et css3.

Pour commencer nous allons créer un nouveau projet vide dans l'[IDE](https://fr.wikipedia.org/wiki/Environnement_de_développement) Webstorm, téléchargeable [ici](https://www.jetbrains.com/fr-fr/webstorm/).

> New Projet > Empty Project
{: .note}

Nous allons créer un premier fichier : `index.html`. 
> new > file 
{: .note}

~~~html 
<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Maison page</title>
</head>
<body>
<h1>Bonjour Monde</h1>
<p>Bienvenue sur ma page web.</p>
</body>
</html>
~~~
Ici on définit bien le type de document mais aussi l'encodage (fortement conseillé pour pouvoir écrire correctement).

Webstorm n’est pas content, il souligne la ligne 2. En passant le curseur à droite de l’éditeur, en regard de la ligne 2 sur le trait orange, il est dit : Missing required “lang” attribute. En cliquant dessus une ampoule orange apparait sur le mot html. Si on clique si cette ampoule elle propose un correctif : insert required tag. Faisons-le et choisissons fr comme langue.

On obtient donc le code suivant :
~~~~html
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8"/>
    <title>Maison page</title>
</head>
<body>
<h1>Bonjour Monde</h1>
<p>Bienvenue sur ma page web.</p>
</body>
</html>
~~~~

### Quelques balises courantes 

* `<head></head>` : en-tête de la page 
* `<body></body>` : corps de la page 
* `<hX></hX>` : titre de niveau avec X valant 1, 2, 3, ... (par exemple `<h1></h1>` est un titre de niveau 1 qui sera écrit plus gros qu'un titre de niveau 3 `<h3></h3>`)
* `<p></p>` : paragraphe
* `<a href="url_du_lien">le texte du lien</a>` : permet d'insérer des liens hypertexte lorsque l'on clique sur "le texte du lien"
* `<em></em>` : permet de mettre en valeur un élément du texte
* `<strong></strong>` : permet d'accentuer un élément du texte 


Il existe des dizaines de balises différentes qui permettent d'insérer des liens, des images, créer des listes... Vous pouvez facilement trouver des listes de ces balises sur internet, en voici quelques exemples :

* <https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1608357-memento-des-balises-html>
* <https://www.w3schools.com/tags/>
* <https://eastmanreference.com/complete-list-of-html-tags>


### Les div 

Les `<div></div>` sont des blocs anonymes. Elles seront caractérisées uniquement par les `class` et les `id`. (ils seront expliqués dans la partie css)

Plusieurs éléments peuvent partager une même classe, mais un id est unique pour un élément.

> On utilise principalement les `<div></div>` pour structurer la page. 

## css


le css est un langage qui permet de gérer la mise en forme de votre site. c'est à dire qu'avec le css vous allez pouvoir mettre de la couleur, changer les styles d'écriture, la mise en page...

### Comment utiliser css ?

Une 1ère technique consiste à écrire directement dans le fichier html, dans la  balise de `<head></head>` grâce à la balise `<style></style>`.

~~~html 
<!doctype html>
<html>
  <head>
      <meta charset="utf-8"/>
      <title>Maison page</title>
      <style>
        p {
              color: red;
        }
      </style>
  </head>
  <body>
      <h1>Bonjour Monde</h1>
      <p>Bienvenue sur ma page web.</p>
  </body>
</html>
~~~

> Sauvez le fichier et recherchez votre page dans le navigateur : Vous pouvez voir que le texte dans le paragraphe est devenu rouge.

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

Ce code est composé de 3 éléments :

* la *balise* (`p`) : il suffit de noter le nom des balises que l'on veut modifier. On aurait pu utiliser `h1`,`em`ou n'importe quelle autre balise.
* une *propriété css* (`color`): cela permet de définir ce que l'on veut modifier. cela peut être la couleur, la taille (`font-size`) ou autre.
* une *valeur* (`red`) : ici c'est le nom de la couleur. Pour chaque propriété, une valeur doit être donnée.

> Il existe de nombreuses propriétés, vous pouvez retrouver les principales [ici](https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Properties_Reference) ou [là](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1608902-memento-des-proprietes-css).

Il y a tout de même un problème. Comment faire si l'on veut avoir des formats différents pour plusieurs paragraphes ? en effet, tous les paragraphes ont la même balise :`p`

Pour resoudre ce problème, il existe des solutions:
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
.test {}
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

### les autres sélecteurs

Il existe de nombreuses autres façons pour sélectionner un élément précis du fichier html. voir [ici](https://ensweb.users.info.unicaen.fr/pres/sel/intro.php)

Pour la suite, vous pouvez apprendre à structurer vos pages [ici](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1605881-structurez-votre-page) et continuer ce tuto!


## js

> TBD : simplifier les exemple du js ?
{: .note}

### modification de l'arbre dom

Lors de la génération d'une page html, on crée ce qu'on appelle un [arbre DOM (Document Object Model)](https://fr.wikipedia.org/wiki/Document_Object_Model) de la page.


Cet arbre contient tous les éléments html présents sur la page (plus de précisions [ici](https://www.w3schools.com/js/js_htmldom.asp)).
L'ajout d'un script javascript sur une page html permet de modifier cet arbre DOM, sans avoir besoin de recharger la page.
Ces modifications ce font via des événements : [https://www.w3schools.com/jsref/dom_obj_event.asp](https://www.w3schools.com/jsref/dom_obj_event.asp)

Prenons un exemple pour illustrer nos propos. Dans premier temps on écrira le script js dans le fichier html. Cependant pour avoir un code plus propre il est recommandé de séparer le code et de créer un fichier en ``.js``en parallèle.

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

    <script>
      document.getElementById("mon_div").onclick = function() {
        document.getElementById("mon_div").style.backgroundColor = "blue"
      }
    </script>
  </body>
</html>
~~~

Ici, on a crée un div dans la page html, originellement de couleur rouge. Le script js va permettre de changer la couleur de ce div en bleu lorsque l'on clique dessus avec la souris.\
Il faut bien noter que l'on écrit le script dans le code à l'endroit où il va être exécuté. 

On peut faire plus compliqué, si l'on souhaite que le div retrouve sa couleur d'origine si on re-clique dessus par exemple :


~~~~html
<script>
  blue = false;
  document.getElementById("mon_div").onclick = function() {
    if (blue) {
      blue = false;
      document.getElementById("mon_div").style.backgroundColor = "red"
    }
    else {
      blue = true;
      document.getElementById("mon_div").style.backgroundColor = "blue"
    }
  }
</script>
~~~~



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






---
layout: page
title:  "HTML CSS JS"
category: tutorial
tags: web
authors : 
  - "Yi Mei JIANG"
  - "Théophile BONNEAU"
---


# Tutoriel HTML CSS JS

Le web front est partie d'un tout contenant le front, le back et l'ops.
Le front (client) est celui qui va afficher le contenu HTML, CSS et js (JavaScript).
Le back (serveur) peut lui dans un sens assez large servir du contenu (html, css, js), ou des fichiers (binaires ou textes).  

## HTML
Le HTML est un langage à balises, par exemple `<head></head>` `<body></body>`. Il y a des balises ouvrantes et fermantes, marquées par un `/`.\
[Liste des balises HTML](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1608357-memento-des-balises-html)

Dans le tutoriel suivant le navigateur interprétera directement le fichier sans passer par un serveur.
Il trouve le fichier à afficher via une [uri](https://fr.wikipedia.org/wiki/Uniform_Resource_Identifier) : `file://chemin/absolu/vers/fichier.html`. \
On ne traitera pas tous les détails depuis la base de la base. \
Il existe pleins de tutos pour apprendre les bases sur l'internet mondial :
- [https://internetingishard.com/html-and-css/](https://internetingishard.com/html-and-css/)
- [https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web)
- [http://www.thenetninja.co.uk/](http://www.thenetninja.co.uk/)
- [http://www.w3schools.com/](http://www.w3schools.com/)
\
Vérifier bien cependant que les tutos traitent de la dernière version, ici HTML5 et CSS3

Pour commencer nous allons créer un nouveau projet vide dans l'[IDE](https://fr.wikipedia.org/wiki/Environnement_de_développement) Webstorm, téléchargeable [ici](https://www.jetbrains.com/fr-fr/webstorm/).
>New Projet > Empty Project

Nous allons créer un premier fichier : `index.html`. 
> new > file 

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
#### Quelques balises courantes 
``<head>`` : en-tête de la page \
``<body>`` : corps de la page \
``<hx>`` : titre de niveau x (x=1,2,3...)\
``<p>`` : paragraphe \
``<a href="lien">`` : permet d'insérer des liens hypertexte \
``<em>`` : permet de mettre en valeur un élément du texte \
``<strong>`` : permet d'accentuer un élément du texte \
Il existe des dizaines de balises différentes qui permettent d'insérer des liens, des images, créer des listes ...\
Vous pouvez facilement trouver des listes de ces balises sur internet, en voici quelques exemples:
- [https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1608357-memento-des-balises-html](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1608357-memento-des-balises-html)
- [https://www.w3schools.com/tags/](https://www.w3schools.com/tags/)
- [https://eastmanreference.com/complete-list-of-html-tags](https://eastmanreference.com/complete-list-of-html-tags)

#### Les div 
Les div sont des blocs anonymes. Elles seront caractérisées uniquement par les `class` et les `id`. (ils seront expliqués dans la partie CSS)
Plusieurs éléments peuvent partager une même classe, mais un id est unique pour un élément.
On les utilise principalement pour structurer la page. 

## CSS
CSS est un langage qui permet de gérer la mise en forme de votre site. c'est à dire qu'avec le CSS vous allez pouvoir mettre de la couleur,changer les styles d'écriture, la mise en page...

Comment utiliser CSS?

Une 1ère technique consiste à écrire directement dans le fichier HTML, au niveau de `head` grâce à la balise `<style>`.

~~~html 
<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Maison page</title>
    <style>
        p
        {
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

Vous pouvez voir que le texte dans le paragraphe est devenu rouge.

Une autre technique, plus propre, consite à travailler directement dans un fichier CSS, lui-même relié au fichier HTML.

Tout d'abord, il faut créer un ficher `.css`. Vous pouvez par exemple le nommer style.css.
Une fois que c'est fait, il faut que vous reliez votre fichier html avec votre fichier css.
Pour cela, mettez vos deux fichiers dans un même dossier. Puis il faut rajouter dans la partie `head` de votre fichier html :
~~~~html
    <link rel="stylesheet" href="style.css" />
~~~~
Voila, maintenant votre fichier html est relié au fichier css. Vous pouvez commencer à mettre en page!

Par exemple, copier ce code dans votre ficher css :
~~~~CSS
p
{
    color: red;
}
~~~~

Ce code est composé de 3 éléments :
- la `balise` (p) : il suffit de noter le nom des balises que l'on veut modifier. On aurait pu utiliser `h1`,`em`ou n'importe quelle autre balise.

- une `propriété CSS` (color): cela permet de définir ce que l'on veut modifier. cela peut être la couleur, la taille (font-size) ou autre.

- une `valeur`(red) : ici c'est le nom de la couleur. Pour chaque propriété, une valeur doit être donnée.

Il existe de nombreuses propriétés, vous pouvez retrouver les principales [ici](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1608902-memento-des-proprietes-css)

Il y a tout de même un problème. Comment faire si l'on veut avoir des formats différents pour plusieurs paragraphes ? en effet, tous les paragraphes ont la même balise :`p`

Pour resoudre ce problème, il existe des solutions:
- `les classes` : qui peuvent être utilisées en même temps par plusieurs balises
- `les id`: qui doivent être uniques pour chaque élément.

#### les classes 

Il s'agit d'un atribut que l'on peut mettre sur n'importe quelle balise 

~~~~HTML
<h1 class=""> </h1>
<p class=""> </p>
<img class="" />
~~~~

Comme valeur pour la classe, nous pouvons utiliser n'importe quel nom par exemple :

~~~~HTML
<h1 class="test"> ce titre est de la classe test</h1>
~~~~
on peut ensuite réutiliser ce nom pour changer l'affichage des balises de cette classe. Il suffit de le définir dans notre fichier CSS.

~~~~CSS
.test
{
    font-size: 16px;
}
~~~~

Ainsi, toutes les balises de classe test auront un texte de taille 16 pixels.

#### les id

Ils s'utilisent de la même facon que les classes, à la différence qu'ils ne peuvent être utilisés que par une balise à la fois.

~~~~CSS
#logo
{
    background-color : blue;
}
~~~~
La balise d'id logo aura donc un fond bleu.

#### les autres selecteurs

Il existe de nombreuses autres façons pour selectioner un element précis du fichier html. voir [ici](https://ensweb.users.info.unicaen.fr/pres/sel/intro.php)

Pour la suite, vous pouvez apprendre à structurer vos pages [ici](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1605881-structurez-votre-page) et continuer ce tuto!


## js
Lors de la génération d'une page html, on crée ce qu'on appelle un ardre DOM (Document Object Model) de la page.\
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

On peut faire plus compliqué, si l'on souhaite que le div retrouve sa couleur d'origine si on re-clique dessus par exemple:
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
Cela devient vite compliqué, on préfére alors utiliser des bibliothèques, comme [jQuery](https://jquery.com).
Cela nous permet de simplifier un peu la syntaxe, mais aussi de nous faciliter la vie. 
On va reprendre l'exemple pour illustrer l'utilité d'une bibliothèque telle que jQuery.

####jQuery
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
Cette fois on souhaite pouvoir changer la couleur de nos DEUX div, alors pourquoi pas attraper les éléments par ``class`` plutôt que par `id` ?
~~~~~html
<script>
    bleu=false;
    document.getElementsByClassName("color").onclick=function (){
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
Malheureusement ce code ne code ne fonctionne pas. En effet la fonction ``getElementsByClassName`` renvoie un array et le reste du code n'est pas applicable tel quel à un array.
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
Ce qui est assez long à écrire, alors que la bibliothèque jQuery prend en charge ce genre de problème.
Pour pouvoir l'utiliser il faut d'abord l'importer, ici on va passer pas un [CND](https://en.wikipedia.org/wiki/Content_delivery_network)

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
Ici on retrouve le code écrit en jQuery, il a exactement la même fonctionnalité. On remarque bien que l'on n'a pas besoin de passer par la boucle ``for``. 

Pour en savoir plus sur l'utilisation de jQuery, il existe de nombreux tutos sur l'internet mondial : 
- [https://www.w3schools.com/jquery/jquery_get_started.asp](https://www.w3schools.com/jquery/jquery_get_started.asp)
- [https://www.digitalocean.com/community/tutorials/an-introduction-to-jquery](https://www.digitalocean.com/community/tutorials/an-introduction-to-jquery)
- [https://www.youtube.com/playlist?list=PL4cUxeGkcC9hNUJ0j6ccnOAcJIPoTRpO4](https://www.youtube.com/playlist?list=PL4cUxeGkcC9hNUJ0j6ccnOAcJIPoTRpO4)






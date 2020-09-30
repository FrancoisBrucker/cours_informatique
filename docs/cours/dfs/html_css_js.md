---
layout: page
title:  "HTML CSS JS"
category: tutorial
tags: web
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
CSS est un langage qui permet de gérer la mise en forme de votre site.

comment utilisé CSS?

Tout d'abord, il faut créer un ficher `.css`. Vous pouvez par exemple le nommer style.css.
Une fois que c'est fait, il faut que vous relier votre fichier html avec votre fichier css.
Pour cela, mettez vos deux fichier dans un même dossier. Puis il faut rajouter dans la partie `head` de votre fichier html :
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

Ce code est coposé de 3 élements :
- la `balise` (p) : il suffit de noter le nom des balises que l'on veut modifier. On aurait pu utiliser `h1`,`em`ou n'importe quelle autre balise.

- une `propriété CSS` (color): cela permet de définir ce que l'on veut modifier. cela peut être la couleur, la taille (font-size) ou autre.

-une `valeur`(red) : ici c'es le nom de la couleur. Pour chaque propriété, une valeur doit être donnée.

Il existe de nombreuse propriétés, vous pouvez en retrouver [ici](https://websitesetup.org/css3-cheat-sheet/)

Il y a tout de même un problème. Comment faire si l'on veut avoir des formats différents pour plusieurs paragraphe ? en effet, tout les paragraphe ont la même balise :`p`

Pour resoudre ce problème, il existe deux solutions:
- `les classes` : qui peuvent etre utilisés en même temps par plusieurs balises
- `les id`: qui doivent être unique pour chaque élément.

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
    color: red;
}
~~~~

Ainsi, toutes les balises de classe test auront un texte rouge.

#### les id

Ils s'utilisent de la même facon que les classe, à la différence qu'il ne peuvent être utilisé que par une balise à la fois.
~~~~CSS
#logo
{
    /* Indiquez les propriétés CSS ici */
}
~~~~

#### les autres selecteurs

Il existe de nombreuses autres façons pour selectioner un element précis du fichier html. voir [ici](https://ensweb.users.info.unicaen.fr/pres/sel/intro.php)

Pour la suite, vous pouvez apprendre à structurer vos pages [ici](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1605881-structurez-votre-page) et continuer ce tuto!

## js

https://www.w3schools.com/js/js_htmldom.asp




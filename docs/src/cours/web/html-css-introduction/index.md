---
layout: layout/post.njk
title: Introduction à html et css

authors:
  - "François Brucker"
  - "Yi Mei Jiang"
  - "Théophile Bonneau"

eleventyNavigation:
  key: "Html/css 101"
  parent: "Web"
---

<!-- début résumé -->

Principales balises de html et premières modification avec css.

<!-- fin résumé -->

On ne traitera pas tous les détails. Il existe pleins de tutos pour apprendre les bases sur l'internet mondial :

{% chemin "**Tutoriels généraux sur html/css** :" %}

* <https://www.internetingishard.com/>
* <https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web>
* <https://www.theodinproject.com/paths/full-stack-javascript/courses/intermediate-html-and-css>
* <https://fr.learnlayout.com/> petits tutos sur le layout css. Sympa à voir mais on utilise le plus souvent des framework web or gérer le layout.
* le <http://www.thenetninja.co.uk/> a plein de tutos sur le web.
* <http://www.w3schools.com/> est le site de référence sur tout ce qui concerne html/css.

{% endchemin %}
{% attention %}
Avant de choisir un tuto, Vérifier bien cependant qu'ils traitent de la dernière version, ici html5 et css3.
{% endattention %}

## Fichier html

Le html est un langage à balises, par exemple les balises `<head></head>`{.language-} ou encore `<body></body>`{.language-}. Il y a des balises ouvrantes (`<head>`{.language-}) et fermantes (`</head>`{.language-}), marquées par un `/`{.language-}. Tout ce qui est entre ces deux balises est son **contenu**.

{% chemin  %}
[Une liste de balises html](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1608357-memento-des-balises-html)
{% endchemin %}

### Premier fichier html

{% faire %}
Prenez votre éditeur de texte favori et créez un nouveau fichier que vous nommerez `index.html`{.fichier}, et collez- le contenu suivant :

```html
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
```

Vous pouvez maintenant l'ouvrir en tant que fichier texte avec chrome : "fichier > ouvrir un fichier ...".
{% endfaire %}

{% note %}
Si vous modifiez un fichier, chrome ne le mettra par à jour immédiatement. Il faut l'actualiser. Vous pouvez le faire dans : "menu Afficher > Actualiser cette page"
{% endnote %}

Vous voyez votre fichier html être interprété par chrome :

{% info %}
félicitations !
Vous venez d'écrire votre 1er fichier html.
{% endinfo %}

### Validation du html

Avant de continuer, vérifions qu'on a bien écrit du html correct. Il est en effet très (trop) facile d'écrire quelque chose qui *ressemble* à du html sans en être.

Le navigateur qui lit de l'à-peu-prêt-html ne peut pas l'interpréter directement, il est obligé de faire des suppositions sur ce que vous avez voulu dire. Il a souvent raison mais cela comporte plusieurs effets de bords problématique :

{% note "**Problème de l'à-peu-prêt-html** :" %}

* les petites erreurs vont s'accumuler et, au moment où vous ne vous y attendrez pas, plus rien ne fonctionnera. Il sera alors très difficile de trouver l'erreur puisqu'il va y en avoir tout un tas les unes à la suite des autres
* chaque navigateur fera des suppositions des suppositions différentes et le rendu sera différent
* c'est bad karma

{% endnote %}

Pour éviter cela, il faut **toujours** faire en sorte que votre html soit correct. La façon ultime de le faire est d'utiliser le [validateur du W3C](https://validator.w3.org/#validate_by_upload+with_options).

{% faire %}

Allez sur le site du [validateur du W3C](https://validator.w3.org/#validate_by_upload+with_options) et choisissez *"Validate by direct input"* et copiez/collez le code html. Puis cliquez sur "check".
{% endfaire %}

Il y a un soucis, il vous demande d'ajouter la langue dans laquelle est écrit votre texte. Faisons le :

```html
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
```

{% faire %}
Re-tentez une validation.
{% endfaire %}
Tout devrait être ok.

{% info %}
Re-Félicitation, vous venez d'écrire votre 1er fichier html correct !{% endinfo %}

Souvent, il existe des plugins pour les éditeurs de texte qui valident automatiquement le html. C'est le cas par défaut avec [vscode](https://code.visualstudio.com/docs/languages/html) par exemple.

## Balises html

Le html est un [langage à balises](https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/HTML_basics) qui s'imbriquent les unes dans les autres en autant de boites. Chaque balise à un sens qu'elle applique à son contenu, c'est à dire ce qui est placé entre ses balises ouvrante et fermante (la même balise avec un `/` devant). Elles permettent de structurer sa page.

### Structure d'une balise

structure de balise :

* ouvert/ fermant
* attribut de balise ="..."
* balise auto-fermante

### balises indispensables

> TBD faire correct.
`<html></html>`

* `<head></head>` : en-tête de la page
  * title
* `<body></body>` : corps de la page

### balises

* `<hX></hX>` : titre de niveau avec X valant 1, 2, 3, ... (par exemple `<h1></h1>` est un titre de niveau 1 qui sera écrit plus gros qu'un titre de niveau 3 `<h3></h3>`)
* `<p></p>` : paragraphe
* `<a href="url_du_lien">le texte du lien</a>` : permet d'insérer des liens hypertexte lorsque l'on clique sur "le texte du lien"
* `<em></em>` : permet de mettre en valeur un élément du texte
* `<strong></strong>` : permet d'accentuer un élément du texte

Il existe des dizaines de balises différentes qui permettent d'insérer des liens, des images, créer des listes... Vous pouvez facilement trouver des listes de ces balises sur internet, en voici quelques exemples :

* <https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1608357-memento-des-balises-html>
* <https://www.w3schools.com/tags/>
* <https://eastmanreference.com/complete-list-of-html-tags>



<https://www.quirksmode.org/compatibility.html>

## balise à placer

quelques balises utiles :

* head/body
* p
* ul li
* ol li
* strong
* em
* table
* a
* img (toujours en relatif)
* h1 à h6

faire du faux texte pur remplir les paragraphes

## css

Si le html permet de structurer votre page, c'est le css qui contrôle son style.

{% info %}
Si vous inspectez les éléments de notre fichier html précédent, vous voyiez qu'il y a du css, même si on ne l'a pas défini. Chaque navigateur va avoir un style (des propriétés css) par défaut pour chaque balise.
{% endinfo %}

Le css est un langage qui permet de gérer la mise en forme de votre site. c'est à dire qu'avec le css vous allez pouvoir mettre de la couleur, changer les styles d'écriture, la mise en page...

### Première utilisation de css

{% faire %}
Modifiez le fichier `index.html`{.fichier} :

```html
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
```

Sauvez le fichier et rechargez votre page dans le navigateur
{% endfaire %}

Vous pouvez voir que le texte dans le paragraphe est devenu rouge.

### Structure css

sélecteur {
  liste de propriétés
}

propriétés : valeurs;

* la *balise* (`p`) : il suffit de noter le nom des balises que l'on veut modifier. On aurait pu utiliser `h1`,`em`ou n'importe quelle autre balise.
* une *propriété css* (`color`): cela permet de définir ce que l'on veut modifier. cela peut être la couleur, la taille (`font-size`) ou autre.
* une *valeur* (`red`) : ici c'est le nom de la couleur. Pour chaque propriété, une valeur doit être donnée.

### Où placer le style ?

Une 1ère technique consiste à écrire directement dans le fichier html, grâce à la balise `<style></style>`.

{% info %}
On place souvent la balise de style `<head></head>` usage.
{% endinfo %}

On peut :

* avoir plusieurs balises styles
* les mettre ou on veut
* mettre le style en attributs ` <p style="margin: 15px; line-height: 1.5; text-align: center;"></p>`

> Il existe de nombreuses propriétés, vous pouvez retrouver les principales [ici](https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Properties_Reference) ou [là](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1608902-memento-des-proprietes-css).

Il y a tout de même un problème. Comment faire si l'on veut avoir des formats différents pour plusieurs paragraphes ? en effet, tous les paragraphes ont la même balise :`p`

### Autres sélecteurs css

Il existe de nombreuses autres façons pour sélectionner un élément précis du fichier html. voir [ici](https://ensweb.users.info.unicaen.fr/pres/sel/intro.php)

Pour la suite, vous pouvez apprendre à structurer vos pages [ici](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1605881-structurez-votre-page) et continuer ce tuto!

* color
* size

## Modèle de boites

display:

* box model : padding, margin, border
* display : inline, box, inline-box (pour les images)

* les boites se mettent :
  * les une en-dessous des autre pour les box
  * les unes à côté des autres pour les inline
* un box prend tout la largeur par défaut
* un inline n'a pas de width.
* Si on veut un inline avec une width : inline-box

> exemple pour centrer une image. 1. display 2. margin.
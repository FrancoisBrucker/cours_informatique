---
layout: layout/post.njk
title: Introduction à css

authors:
  - "François Brucker"
  - "Yi Mei Jiang"
  - "Théophile Bonneau"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Utilisation de css pour modifier le style de sa page.

<!-- fin résumé -->

Si le html permet de structurer votre page, c'est le css qui contrôle son style.

{% info %}
Si vous inspectez les éléments de notre fichier html précédent, vous voyiez qu'il y a du css, même si on ne l'a pas défini. Chaque navigateur va avoir un style (des propriétés css) par défaut pour chaque balise.
{% endinfo %}

Le css est un langage qui permet de gérer la mise en forme de votre site. c'est à dire qu'avec le css vous allez pouvoir mettre de la couleur, changer les styles d'écriture, la mise en page...

## Qu'est ce que le css

{% faire %}
Créez un fichier `exemple.html`{.fichier} contenant le code suivant :

```html
<!doctype html>
<html>
  <head>
      <meta charset="utf-8"/>
      <title>Maison page</title>
      <style>
        p {
              color: red;
              background-color: olive;
        }
      </style>
  </head>
  <body>
      <h1>Bonjour Monde</h1>
      <p>Bienvenue sur ma page web.</p>
      <p>Comment allez vous ?</p>
  </body>
</html>
```

Sauvez le fichier et rechargez votre page dans le navigateur.

Vous pouvez voir que le texte dans le paragraphe est devenu rouge.
{% endfaire %}

Le css est une succession de spécification de propriétés css pour un (ou plusieurs éléments) décrits par un sélecteur :

```
sélecteur {
  propriété: valeur;
  ...
  propriété: valeur;  
}
```

Un [sélecteur](https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Selectors) peut être beaucoup de choses, le plus simple étant le nom d'une balise. Dans l'exemple précédent :

* le sélecteur est l'élément (`<p></p>`{.language-}) : il suffit de noter le nom des balises que l'on veut modifier. On aurait pu utiliser `h1`,`em`ou n'importe quelle autre balise.
* on modifie deux propriétés pour ce sélecteur :
  * la propriété [color](https://www.w3schools.com/cssref/pr_text_color.asp) qui correspond à la couleur du texte
  * la propriété [background-color](https://www.w3schools.com/cssref/pr_background-color.asp) qui change la couleur du fond de l'élément.

## propriétés css

Il existe de nombreuses propriétés, vous pouvez retrouver les principales :

* [ici](https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Properties_Reference)
* ou encore [là](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1608902-memento-des-proprietes-css).

### propriété simple

> TBD : donner des exemples.

Comme width, height, etc.

### propriétés combinée

> TBD : donner des exemples. background, border, font, ...

* [fond d'un élément](https://www.codeur.com/tuto/css/proprietes-css-background/)
* [changez de police de caractères](https://developers.google.com/fonts/docs/getting_started)

## Où placer le style ?

{% lien "**Documentation**" %}

<https://www.w3schools.com/css/css_howto.asp>

{% endlien %}

Il y a trois grandes façons d'inclure du css dans une structure html

### Balise style

Une 1ère technique consiste à écrire directement dans le fichier html, grâce à la balise `<style></style>`.

Par convention, on place souvent la balise de style dans le `<head></head>` de la page.

On peut :

* avoir plusieurs balises styles
* les mettre ou on veut ça ne change rien. Donc autant respecter la convention et toutes les mettre au même endroit : dans head

{% attention %}
Si plusieurs modifient la même propriété, c'est la dernière qui est lue qui est prise en compte. Lorsque l'on a des bibliothèques, ont commencent par elles et on fini pas nos propres propriété css qui peuvent modifier celles établies précédemment.
{% endattention %}

{% note %}
Inclure du style avec la balise style est recommandée lorsque l'on ajoute peu de style.
{% endnote %}

### Fichier séparé

On utilise la balise auto-fermante link :

```
<link rel="stylesheet" href="[nom de fichier]">
```

Lorsque vous incluez vos propres fichiers, utilisez **toujours** un chemin relatif. On a de plus coutume de placer le css dans un dossier spécifique de notre site

### Attribut de la balise

Enfin, on peut utiliser l'attribut style présent dans n'importe quelle balise html.

Par exemple :

```html
<p style="margin: 15px; line-height: 1.5; text-align: center;">
Romani ite domum !
</p>
```

On Utilise souvent cette façon de faire en javascript ou on modifie les propriétés css d'un élément avec du code. C'est aussi pratique lorsque l'on veut changer un petit truc dans une balise particulière.

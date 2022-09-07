---
layout: layout/post.njk
title: Introduction à css

authors:
  - "François Brucker"
  - "Yi Mei Jiang"
  - "Théophile Bonneau"

eleventyNavigation:
  key: "Html/css 101"
  parent: "Web"
---

<!-- début résumé -->

Utilisation de css pour modifier le style de sa page

<!-- fin résumé -->

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


---
layout: layout/post.njk

title: Balises anonymes
authors:
    - "François Brucker"


eleventyNavigation:
  key: "Balises anonymes"
  parent: "Web"
---

<!-- début résumé -->

Les balises anonymes dans le design web.

<!-- fin résumé -->

Souvent, des balises ne sont pas déterminées par un sens précis mais par une volonté de :

* découper la structure en blocs homogènes
* regrouper un bloc qui aura un style déterminé

Pour cela, on utilise des balises anonymes qui n'ont :

* aucun sens a priori
* aucun style par défaut

## types de balises

Il existe deux balises anonymes :

* balise `<div></div>`{.language-} par défaut de display bloc, utilisé pour découper l'espace en bloc
* balise `<span></span>`{.language-} par défaut de display inline, utilisé pour des morceaux de texte qui doivent être placé les uns à côté des autres.

## sélecteurs css { #sélecteur-css }

Ces deux balises sont souvent utilisés avec des sélecteurs css de type
[attribut `class`{.language-}](https://developer.mozilla.org/fr/docs/Web/HTML/Global_attributes/class) auquel on associe un style via le
[sélecteur class](https://developer.mozilla.org/fr/docs/Web/CSS/Class_selectors).

Très utile lorsque le même style sera appliqué à plusieurs balises.

{% info %}
L'attribut class n'est pas réservé aux balises anonymes, on peut l'utiliser avec toutes les balises.
{% endinfo %}

Un autre moyen d'adresser les éléments est d'utiliser l'[attribut `id`{.language-}](https://developer.mozilla.org/fr/docs/Web/HTML/Global_attributes/id) qui doit caractériser de façon **unique** une balise.

C'est utile pour la sélection d'éléments avec javascript ou la design de pages.

On peut ensuite utiliser le [sélecteur css id](https://developer.mozilla.org/fr/docs/Web/CSS/ID_selectors) pour le caractériser.

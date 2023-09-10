---
layout: layout/post.njk
title: Unités et couleurs

authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Quelles unités utiliser lorsque l'on fait du html et gestion de la couleur

<!-- fin résumé -->

## Unités

{% lien %}
<https://www.w3schools.com/cssref/css_units.asp>
{% endlien %}

* Toujours utiliser des unités relatives em et rem dans vos design.
* Toujours donner les unités des images en px sans redimensionnement

### `em`{.language-} et `rem`{.language-}

{% lien %}
<https://medium.com/codeshake/unit%C3%A9s-de-mesures-em-vs-rem-eac03dbcb9c7>
{% endlien %}

En utilisant l'exemple de [modèle de boites](../modèle-boites#exemple){.interne}

```html
<style>
  p {
    font-size: 2em;
  }
  strong {
    font-size: 2em;
  }
</style>
```

vs :

```html
<style>
  p {
    font-size: 2em;
  }
  strong {
    font-size: 2rem;
  }
</style>
```

### Images

Les images doivent toujours contenir les attributs `width`{.language-} et `height`{.language-}, cela permet au navigateur de continuer la mise en place de la page tout en chargeant l'image. Si vous ne renseignez pas la taille, il faudra d'abord charger toute l'image avant de mettre en page le reste de la page, ce qui peut prendre du temps.

Ne changez pas la taille de l'image car on perd soit en qualité soit en temps de chargement

Si vous devez le faire, respectez les proportions de l'image.

## Couleurs

{% lien %}
<https://developer.mozilla.org/fr/docs/Web/CSS/color>
{% endlien %}

* nommées
* rgb
* rgba (?)
* formats
* [color wheel](https://color.adobe.com/fr)

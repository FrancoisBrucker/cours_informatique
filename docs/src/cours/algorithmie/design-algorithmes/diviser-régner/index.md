---
layout: layout/post.njk

title: Diviser pour régner

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Principe

{% aller %}
[Principe](./principe){.interne}
{% endaller %}

## Élément majoritaire

> TBD
> naif
> comme fusion
> vérification à la fin : <https://perso.ens-lyon.fr/frederic.vivien/Enseignement/Algo-2001-2002/Corrige-TD04.pdf>


## Exemple du calcul de la médiane

Un calcul optimal en temps linéaire. Fait parti selon moi des résultats les plus surprenant (et beau) en algorithmie.

{% aller %}
[Calcul de la médiane](./médiane){.interne}
{% endaller %}

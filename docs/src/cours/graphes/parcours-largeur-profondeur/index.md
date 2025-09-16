---
layout: layout/post.njk

title: Parcours

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Deux parcours classiques d'un graphe : largeur et profondeur.

Permettent de :

- parcourir tous les sommets arêtes en temps linéaire (n+m)
- fonctionnent pour les graphes orientés ou non

> TBD exemple avec le graphe de l'arbre couvrant.
> TBD exemple avec le graphe des chemins de poids min positifs.

> TBD un algo fondamental que l'on va retrouver à pleins d'endroits (certains attendus et d'autres de façon pus surprenante)

## Largeur

> TBD largeur et file

{% lien %}

[Parcours en largeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur)

{% endlien %}

> TBD application quand il faut parcourir de proche en proche

## Profondeur

> TBD profondeur et pile

{% lien %}

[Parcours en profondeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur)

{% endlien %}

> TBD propriétés : <https://people.irisa.fr/Francois.Schwarzentruber/algo1/05parcoursprofondeur.pdf>

> TBD application quand il faut aller le plus loin possible
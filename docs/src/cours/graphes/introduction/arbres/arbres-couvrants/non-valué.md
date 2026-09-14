---
layout: layout/post.njk

title: Arbres et arborescences couvrants

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Algorithmes de recherche d'un arbre couvrant ou d'une arborescence

## Parcours

> Sert partout. On les reverra plus tard, ici juste définition et utilisation comme arbre couvrant /arborescence.

### Largeur

{% lien %}

[Parcours en largeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur)

{% endlien %}

### Profondeur

{% lien %}

[Parcours en profondeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur)

{% endlien %}

### Kruskal

> TBD sans valuation. Comme composantes connexes (sans ordre)
>
{% lien %}
<https://fr.wikipedia.org/wiki/Algorithme_de_Kruskal>
{% endlien %}

> TBD Kruskal. On le fait :
> 
> 1. en ajoutant des arêtes en restant sans cycle : algo glouton. On prouve la minimalité par échange.
> 2. on optimise en montrant que c'est de la connexité. si 2 composantes connexes arbre on peut les lier et on reste arbre
> 3. on implémente çe avec des couleurs (attention à la mise à jour)
> 4. calcul de complexité $\mathcal{O}(n^2\log(n))$ s'il faut trier, et $\mathcal{O}(n^2)$ sinon. Le calcul est tricky : que n mise à jour des couleurs.

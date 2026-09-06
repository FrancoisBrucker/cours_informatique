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

## Applications


### Chemins et circuits

> TBD ajout des parcours :
>
> - BFS
>   - Plus courts chemins (démonstration par rec)
> - BFS
>   - chemin et cycles/circuit avec BFS (nœud dans la pile)


### Composantes connexes

> connexité en BFS et DFS.

### <span id="algorithme-fortement-connexe"></span> Algorithme de recherche de composante fortement connexe

> TBD avec un DFS

> TBD  connexes

- Kosaraju en 2 passes : <https://www.youtube.com/watch?v=RpgcYiky7uw>
- Tarjan en une passe : <https://www.youtube.com/watch?v=wUgWX0nc4NY>

> TBD <https://www.youtube.com/watch?v=m2mdGfxs_5E>
>

### Trouver une composante 2-connexe

> TBD aussi avec un DFS

---
layout: layout/post.njk

title: Arbres et arborescences couvrants

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


La recherche d'un arbre couvrant ou d'une arborescence d'un graphe non valué peut se faire en utilisant de algorithmes très généraux de parcours de graphes : les parcours en largeur et en profondeur.

{% attention2 "**À retenir**" %}
Ces parcours servent **beaucoup**. On va les retrouver à plein d'endroit donc connaissez les : ils sont bien plus important qu'on ne le pense au départ.
{% endattention2 %}

Nous allons expliciter les deux parcours en supposant que les graphes ne sont pas forcément connexes, ils rendront ainsi plutôt une forêt couvrant qu'un arbre couvrant. Enfin, ces deux algorithmes fonctionnent sans soucis pour des graphes orientés ou non voir des multi-graphes.

## Parcours en largeur

{% lien %}

[Parcours en largeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur)

{% endlien %}


```pseudocode
algorithme largeur(G: Graphe, x: Sommet): Graphe
    var F: File<Sommet> ← File<Sommet>{x}
    var s: Sommet
    var E: [Arête] ← []

    marque(s)
    tant que F est non vide:
        s ← F.défile()
        Pour chaque v: Sommet de G[s]:
            si v est non marqué :
                ajoute xv à E
                marque(v)
                F.enfile(v)

    rendre (V(G), E)
```

Le code précédent va rendre :

- un arbre couvrant de $G$ de la partie connexe de $G$ contenant $x$
- une arborescence de racine $x$ contenant tous les sommets atteignables par $x$ dans $G$

Pour couvrir tout le graphe on recommence l'algorithme sur un sommet qui est dans le graphe mais pas dans l'arbre rendu par l'algorithme.

### Preuve

> TBD arborescence

### Complexité

> TBD linéaire $\mathcal{O}(\vert E\vert + \vert V\vert)$  si on peut marquer et prendre les voisins d'un sommet en $\mathcal{O}(1)$.

> TBD on l'écrit avec des entiers et tout ça.
>
## Parcours en profondeur

{% lien %}

[Parcours en profondeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur)

{% endlien %}

Ce parcours s'écrit facilement de façon récursive :

```pseudocode
algorithme largeur(G: Graphe, x: Sommet): Graphe
    var F: File<Sommet> ← File<Sommet>{x}
    var s: Sommet
    var E: [Arête] ← []

    marque(s)
    tant que F est non vide:
        s ← F.défile()
        Pour chaque v: Sommet de G[s]:
            si v est non marqué :
                ajoute xv à E
                marque(v)
                F.enfile(v)

    rendre (V(G), E)
```

### Preuve

> TBD arborescence

### Complexité

> TBD linéaire $\mathcal{O}(\vert E\vert + \vert V\vert)$  si on peut marquer et prendre les voisins d'un sommet en $\mathcal{O}(1)$.

> TBD on l'écrit avec des entiers et tout ça.
>

## Parcours et arbre enracinés

> TBD monter que largeur et profondeur peuvent encoder un arbre enraciné en temps linéaire.
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

> Permettent de :
>
> - parcourir tous les sommets arêtes en temps linéaire
> - trouver des cycles pour des chemins
> - fonctionnent pour les graphes orientés ou non

## Largeur

> TBD largeur et file

{% lien %}

[Parcours en largeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur)

{% endlien %}

> TBD application quand il faut parcourir de proche en proche

### BFS et chemin/cycle/circuits

> TBD chemin et cycles/circuit avec BFS (noeud parent)

### BFS et Plus courts chemins

> TBD démonstration par rec

## Profondeur

> TBD profondeur et pile

{% lien %}

[Parcours en profondeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur)

{% endlien %}

> TBD propriétés : <https://people.irisa.fr/Francois.Schwarzentruber/algo1/05parcoursprofondeur.pdf>

> TBD application quand il faut aller le plus loin possible

### DFS et chemin/cycle/circuits

> TBD chemin et cycles/circuit avec BFS (noeud dans la pile)

### DFS et Problème d’ordonnancements

> TBD tri topologique dans un DAG avec un DFS + à la visite ajoute en fin de liste. Ensuite on regarde la liste à l'envers

Un [problème d'ordonnancement](https://fr.wikipedia.org/wiki/Th%C3%A9orie_de_l%27ordonnancement) peut se modéliser par un DAG nommé graphe de dépendances où si $xy$ est une arête alors il faut faire $x$ avant de pouvoir faire $y$.

{% exercice %}
Pourquoi ne doit-il pas y avoir de cycles dans un graphe de dépendance ?
{% endexercice %}
{% details "solution" %}
Il est clair que s'il y a un cycle on ne peut réaliser le projet.
{% enddetails %}

Vous résolvez des problèmes d'ordonnancement tous les jours comme par exemple comment s'habiller le matin (voir graphe ci-après)

![habillage](chemin_habillage.png)

{% exercice %}
Montrer que le tri topologique est une solution au problème d'ordonnancement. Appliquez le au problème de s'habiller le matin.
{% endexercice %}
{% details "solution" %}
De plus un tri topologique fait que lorsque l'on s'attelle à la tache $v_i$ on a déjà fait tous ses prédécesseurs (ses prés-requis).
{% enddetails %}

C'est encore un exemple où les contraintes sont locales et ou l'on cherche une solution globale.

### DFS et calcul de composantes

#### Composantes 2-connexes

> TBD

#### Composantes fortement connexes

> TBD  connexes

- Kosaraju en 2 passes : <https://www.youtube.com/watch?v=RpgcYiky7uw>
- Tarjan en une passe : <https://www.youtube.com/watch?v=wUgWX0nc4NY>

> TBD <https://www.youtube.com/watch?v=m2mdGfxs_5E>

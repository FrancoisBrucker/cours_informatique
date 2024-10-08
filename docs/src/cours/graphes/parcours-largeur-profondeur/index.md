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

[Parcours en largeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur)

> TBD application quand il faut parcourir de proche en proche

### BFS et chemin/cycle/circuits

> TBD chemin et cycles/circuit avec BFS (noeud parent)

### BFS et Plus courts chemins

> TBD démonstration par rec

## Profondeur

> TBD profondeur et pile

[Parcours en profondeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur)

> TBD propriétés : <https://people.irisa.fr/Francois.Schwarzentruber/algo1/05parcoursprofondeur.pdf>

### DFS et chemin/cycle/circuits

> TBD chemin et cycles/circuit avec BFS (noeud dans la pile)

### DFS et Problème d’ordonnancements

Un graphe orienté qui ne contient pas de circuit est souvent appelé _DAG_ (direct acyclic graph).

On appelle **_tri topologique_** d'un graphe orienté $G = (V, E)$ un ordre total $<$ sur les sommets du graphe tel que $xy \in E$ implique $x < y$ dans l'ordre.

{% exercice %}
Montrer que :

1. un graphe orienté ne peut admettre de tri topologique que s'il n'a pas de cycle
2. pour un DAG, il existe toujours un sommet qui n'a pas de voisins entrant (_resp._ sortant)
3. en déduire qu'un DAG admet un tri topologique
4. conclure sur le fait qu'un graphe est un DAG si et seulement s'il admet un tri topologique
{% endexercice %}
{% details "solution" %}
   1 :

Soit $c_0\dots c_k$ un cycle ($c_k = c_0$), quelque soit l'ordre total entre les sommets du graphe, il existe $i$ tel que $c_{i+1} < c_i$ ce qui est impossible si un tel ordre était topologique.

2 :

Supposons que tout sommet d'un DAG admette un voisin entrant et un voisin sortant, et prenons une arête $x_0x_1$ de ce graphe. Il existe donc une arête $x_1x_2$. Si $x_2 = x_0$ il existe un cycle dans le graphe, sinon il existe un chemin $x_0x_1x_2$. Il existe donc une arête $x_2x_3$. Si $x_3 \in \{x_0, x_1 \}$ il existe un cycle et sinon on a un chemin $x_0x_1x_2x_3$. On peut ainsi recommencer jusqu'à tomber sur un cycle par finitude du graphe. Ce n'est pas un DAG.

Le raisonnement est identique pour les voisins entrant.

3 :

en supprimant itérativement les sommets sans voisins rentrant d'un DAG (le graphe obtenu en supprimant un sommet d'un DAG est toujours un DAG puisque supprimer un sommet ne rajoute pas de cycle), on obtient un tri topologique.

4 :

On a montré que :

- cycle implique non tri topologique
- DAG (non cycle) implique tri topologique

On a donc bien l'équivalence : tri topologique est équivalent à DAG.

{% enddetails %}

> TBD tri topologique avec un DFS

On utilisera souvent ce tri pour résoudre des problèmes d'ordonnancement (on le verra tout à l'heure dans un cas d'importance certaine).

{% exercice %}
Utiliser le tri pour trouver un chemin élémentaire de longueur maximum dans un DAG.
{% endexercice %}
{% details "solution" %}
algorithme sur tri topologique :

```text
Entrée :
    - un graphe orienté G = (V, E)
    - un tri topologique V0 < ... < Vn des éléments de V
Initialisation :
    longueur(x) = 0 pour tout sommet x
    predecesseur(x) = x pour tout sommet x
    V' = {}, E' = {}
Algorithme :
    pour v allant de V0 à Vn:
        pour chaque voisin sortant w de v:
            si longueur(w) < longueur(v) + 1:
                longueur(w) = longueur(v) + 1
                predecesseur(w) = v
    soit a l'élément de V ayant la plus grande longueur
    chemin = [a]
    x = a
    tant que x est différent de predecesseur(x):
        x = predecesseur(x)
        ajoute x au début de chemin
Retour :
    chemin
```

La complexité est de $\mathcal{O}(\vert E \vert + \vert V \vert)$, ce qui est optimal.

Pour prouver l'algorithme, on montre par récurrence sur $\vert V \vert$ que `longueur(x)` est la longueur d'un plus long chemin finissant en `x`.

Si $\vert V \vert = 1$, c'est Ok. On suppose la propriété vraie à $\vert V \vert = n$. Pour $\vert V \vert = n +1$ on remarque que `longueur(Vi)` est la même pour le graphe $G$ et pour le graphe $G$ auquel on a enlevé $v_{n+1}$ pour tout $i \neq n+1$. Comme tous les prédécesseurs de $v_{n+1}$ seront vus pour l'algorithme et que `longueur(Vi)` ne change pas après l'étape $i$ on en conclut que la récurrence est vraie à $\vert V \vert = n +1$.
{% enddetails %}

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

### DFS et calcul des composantes fortement connexes

- Kosaraju en 2 passes : <https://www.youtube.com/watch?v=RpgcYiky7uw>
- Tarjan en une passe : <https://www.youtube.com/watch?v=wUgWX0nc4NY>

> TBD <https://www.youtube.com/watch?v=m2mdGfxs_5E>

---
layout: layout/post.njk
title: Exercices gloutons

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> <https://www.techiedelight.com/minimum-number-of-platforms-needed-avoid-delay-arrival-train/>
> <https://www.techiedelight.com/shortest-superstring-problem/>
## réservation SNCF

On suppose que $n$ personnes veulent voyager en train un
jour donné. La personne $i$ veut prendre le train train[i].

Il y a $k$ trains qui partent dans la journée, le train $j$ partant avant le train $j+1$, chaque train ne pouvant contenir plus de $K$ passagers.

### solution possible ?

Proposez un algorithme qui vérifie que pour un nombre de train donné et une liste de trains choisi, il est possible de faire voyager tout le monde.

### solution approchée

On suppose maintenant que la personne $i$, si elle ne peut
pas prendre le train train[i] parce qu’il est complet, accepte
de prendre un des trains suivants (s’il y en a un).

Proposez un algorithme minimisant l'attente globale pour faire voyager tous les voyageurs.

## Recouvrement

<https://algo.gricad-pages.univ-grenoble-alpes.fr/L3I-S5-algo/TD1-10-corrige.pdf>
> recouvrement de points par des intervalles exo 3

## Une quête d'essence

Une route comporte $n$ stations services numérotées dans l’ordre du parcours, de $0$ à $n-1$. La distance du départ de la station $i$ est rangée dans la liste `d`{.language-} (la station $i$ est à `d[i]`{.language-} kilomètres du départ). Le but est d'atteindre la dernière station de la route.


### Admissibilité

Donnez une condition nécessaire et suffisante pour que l'automobiliste puisse parcourir toute la route jusqu'à la dernière station service.

### Algorithmes

Écrivez deux algorithmes :

- le premier qui vérifie, à partir d'une liste `d`{.language-} de stations et d'un nombre maximum de kilomètres `r`{.language-} possibles que le problème admet une solution.
- le second qui vérifie, à partir d'une liste `s`{.language-} d'indices de stations (que l'on supposera croissante) où faire le plein, d'une liste `d`{.language-} de stations et d'un nombre maximum de kilomètres `r`{.language-} si `s`{.language-} est une solution (ou pas) du problème

Exemple :

- Pour une liste `d`{.language-} de stations valant : `d = [2, 5, 6, 10, 12, 13]`{.language-}, le premier algorithme devra répondre Oui pour un `r`{.language-} valant $4$ et None pour `r = 3`{.language-}.
- Pour une liste `d`{.language-} de stations valant : `d = [2, 5, 6, 10, 12, 13]`{.language-}, un réservoir de `r = 4` et une liste `s = [0, 2, 3, 4]`{.language-} il devra répondre `True`{.language-} et pour une liste `d`{.language-} et un réservoir identique, il devra répondre `False`{.language-} pour `s = [0, 1, 3, 4]`{.language-}.

## Reservoir vide

On suppose que chaque litre d'essence permet de parcourir 1km et chaque station $i$ vend 1l d'essence à un prix $p_i$. On essaye de minimiser le coût d'achat d'essence.

### Nombre de stations minimum

1. Montrer qu'il existe une solution de coût minimal qui minimise aussi le nombre d'arrêt.
2. Montrer à partir d'un exemple qu'il peut exister des solutions à coût minimal ayant plus d'arrêt que le nombre minimal.

### Algorithme

Écrivez un algorithme qui, à partir d'une liste `d`{.language-} de stations et d'un nombre maximum de kilomètres `r`{.language-} possible rend une liste `s`{.language-} de couples `(station, litre)`{.language-} qui contient un nombre minimal de stations où acheter de l'essence ainsi que le nombre de litres à y acheter pour minimiser le coût du trajet.

## Partage d'information

<http://www-desir.lip6.fr/~spanjaard/pmwiki/uploads/TDAlgorithmesGloutons.pdf>

exo 2

## Temps d'attente
exo 5 imag


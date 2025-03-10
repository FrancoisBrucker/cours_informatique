---
layout: layout/post.njk

title: Tris spéciaux

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Corrigé](./corrigé){.interne}
{% endlien %}

Les tris spéciaux ont des complexités inférieures à $\mathcal{O}(n\log(n))$, ce qui n'est bien sur possible que si l'on se place dans des cas particuliers d'entrées.

## Tri par paquets (bucket sort)

> TBD description de l'algorithme. [wikipedia](https://fr.wikipedia.org/wiki/Tri_par_paquets)

On suppose que l'on a affaire à des entiers uniquement.

1. pseudo-code
2. complexité min et max
3. cas d'usage ?

## Tri par base

Ce tri s'applique uniquement aux entiers positifs. Notre entrée est une liste $T$  de listes de mêmes tailles composées de 0 et de 1 représentant des entiers écrit en base 2 (comme pour le [compteur binaire](../compteur-binaire)). Par exemple : T = [[1, 0, 0, 1], [1, 1, 1, 0], [0, 0, 0, 1]] qui correspond aux nombres [9, 14, 1].

Le principe de ce tri est très simple :

- On considère d'abord le bit de poids le plus faible (_ie._ le plus à droite). On crée alors deux listes L0 et L1 initialement vides et on va itérativement considérer chaque élément de la liste à trier :
  - les entiers dont le bit de poids le plus faible est 0 sont ajoutés à la fin de L0
  - les entiers dont le bit de poids le plus faible est 1 sont ajoutés à la fin de L1
- On concatène les deux sous-listes T = L0 + L1
- On recommence sur le bit à gauche de celui qu'on vient de traiter.
- ...

Les parcours des liste T se font, toujours, de la gauche vers la droite.

Pour notre exemple :

1. après premiere boucle : [[1,1,1,0], [1, 0, 0, 1], [0, 0, 0, 1]]
2. après deuxième boucle : [[1, 0, 0, 1], [0, 0, 0, 1], [1,1,1,0]]
3. après troisième boucle :[[1, 0, 0, 1], [0, 0, 0, 1], [1,1,1,0]]
4. après quatrième boucle : [[0, 0, 0, 1], [1, 0, 0, 1], , [1,1,1,0]]

Questions :

- Donnez le pseudo-code, la preuve et la complexité de cet algorithme.
- Rappelez la complexité minimale du tri (dans le cas le pire). Commentaires.

### Tri par monotonies

Étant donné un tableau $T$, **_une monotonie_** est une suite croissante maximale d'éléments consécutifs de $T$. Par exemple :
si $T = [2,6, 1,3, 3, 5,2,6, 4,0, 1,8,9,1,3, 2,0,1,0]$, alors $[2,6]$, $[1,3,3,5]$, $[2,6]$, $[4]$, $[0, 1,8,9]$, $[1,3]$, $[2]$, $[0,1]$ et $[0]$ sont les monotonies de $T$.

Donnez un algorithme qui, étant donné un tableau $T$ construit une liste (de listes) $L$, chaque élément de $L$ étant une monotonie de $T$ (et vice versa). À partir de notre exemple, on obtient :
$L = [[2,6], [1,3,3,5],[2,6], [4], [0, 1,8,9], [1,3], [2] ,[0,1], [0]]$.

Donnez un algorithme qui fusionne deux monotonies ; par exemple, à partir de $[2,6]$ et $[1,3,3,5]$, on obtient $[1,2,3,3,5,6]$ (ceci est aussi une question de cours).

Donnez un algorithme qui, étant donnée une liste $L$ de monotonies, les fusionne deux-à-deux (en en laissant éventuellement une ``toute seule" à la fin) et met le résultat dans une liste (de listes) $L'$. Par exemple, à partir de
$L = [[2,6], [1,3,3,5],[2,6], [4], [0, 1,8,9], [1,3], [2] ,[0,1], [0]]$, on obtient $L' = [[1,2,3,3,5,6], [2,4,6],[0,1,1,3,8,9], [0,1,2], [0]]$.

En déduire un algorithme de tri. Donnez sa complexité dans le cas le meilleur et dans le cas
le pire.

Cet algorithme est en fait une variante d'un algorithme vu en cours. Lequel ?

---
layout: page
title:  "Théorie des graphes : arbres"
category: cours
tags: informatique graphes
author: "François Brucker"
---

> [graphes]({% link cours/graphes/index.md %}) / [arbres corrigé]({% link cours/graphes/arbres-corrige.md %})
{: .chemin}

Ce ne sera pas un corrigé exhaustif. On donnera les principale piste pour résoudre les exercices.

## définitions et premières propriétés

### graphe simple

> Redonnez la définition d'un graphe simple. Combien d'arêtes au maximum peut contenir un graphe simple ?
{: .a-faire}

[Dans le cours]({% link cours/graphes/index.md %}#restrictions) : un graphe simple est un graphe sans boucle et non orienté

### arbre ou pas arbre ?

> Déduire de la définition lequel des 2 graphes ci-dessous est un arbre.
{: .a-faire}

C'est bien sur le graphe B qui est connexe et ne contient pas de cycle. Le graphe A est connexe mais il contient des cycles.

### algorithme de reconnaissance

#### graphe connexe

>1. Donnez un algorithme permettant de savoir si un graphe $G = (V, E)$ donné est connexe.
>2. Quelle structure de graphe utiliseriez vous pour que cet algorithme ait la plus petite complexité possible ?
{: .a-faire}

On utilise le [parcours en largeur des graphes](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur). COmme il faut examiner stous les voisins d'un sommet, on a coutume d'utiliser les liste d'adjacence pour le nombre d'opération de l'algorithme soit proportionnel aux nombres d'arêtes du graphes ($\mathcal{O}(\vert E \vert)$) : il est donc optimal.

#### graphe sans cycle ?

>* Tout graphe sans cycle contient au maximum $\vert V \vert - 1$ arêtes.
>* Tout graphe connexe contient au minimum $\vert V \vert - 1$ arêtes.
{: .a-faire}

Pour la 1ère preuve, on utilise la contre-apposée puis le résultat du cours sur l'[existence de cycles dans un graphe]({% link cours/graphes/parcours-euleriens.md %}#prop-cycles-graph).

Pour la seconde preuve, on le montre par récurrence. La propriété est clairement vraie pour un graphe à 1 ou 2 sommets. On le suppose alors vraie jusqu'à $n$ sommets et on considère un graphe connexe à $n+1$ sommets.

POur ce graphe on choisi un sommet, $x$, que l'on supprime du graphe. Ce dernier n'est alors plus connexe et possède $p$ composantes connexes qui respectent l'hypothèse de récurrence : $\vert E_i \vert \geq \vet V_i \vert -1 pour chacune d'elles. En sommant le tout on a alors :

$$\sum \vert E_i \vert \geq \sum (\vert V_i \vert -1) $$

On conclut en remarquant que $\sum \vert E_i \vert = \vert E\vert -p$ et $\sum \vert V_i \vert = V - 1$.

#### conditions

>Un graphe $G=(V, E)$ est un arbre si et seulement si :
>
>* il est connexe
>* $\vert E \vert = \vert V \vert - 1$
{: .a-faire}

clair avec ce qui précède.

>un graphe $G=(V, E)$ est un arbre si et seulement si :
>
>* il est sans cycle
>* $\vert E \vert = \vert V \vert - 1$
{: .a-faire}

Tout pareil, clair avec ce qui précède.

> prouver que :
>
>* Si on ajoute une arête à un arbre (n'importe laquelle) on ajoute un cycle
>* Si on supprime une arête à un arbre (n'importe laquelle) on le déconnecte
{: .a-faire}

Encore une fois, c'est clair (ils sont vraiment trop faciles ces exercices).

> Donnez l'algorithme final pour savoir si un graphe est un arbre.
{: .a-faire}

On utilise le parcours en largeur pour obtenir la composante connexe à partir d'un élément. Si elle contient tous les éléments, le graphe est connexe et si ce graphe à $\vert V \vert -1$ c'est un graphe.

## arbre enracinées

### chemin et arbres

>Montrez que quelques soient deux sommets $x$ et $y$, il n'existe qu'un seul chemin entre $x$ et $y$.
{: .a-faire}

S'il existait 2 chemins distincts pour aller de $x$ à $y$ on se placerait au premier élément distincts et au premier élément en commun après celui-ci et on aurait un cycle.

### ordonnancement des sommets {#ordo-sommets}

> Donnez un exemple de chacun des termes pour le graphe ci-avant.
{: .a-faire}

* $a$ est un **ancêtre** de $n$
* $g$ est un **descendant** de $d$
* $k$ est une **feuille**
* $c$ est un **nœud intérieur**
* $b$ est un **successeur** de $a$
* $h$ est un **prédécesseur** de $m$
* la **hauteur** de $2$ est 2
* la **hauteur** de l'arbre est 4

## arbre binaire planté

### propriété fondamentale des arbres binaires

>Montrer que pour un arbre binaire, si noeud intérieur a exactement 2 successeurs, alors en notant $f$ le nombre de feuilles de l'arbre, on a :
>
>* la hauteur de l'arbre est égale à $\log_2(f)$
>* $f$ est égal au nombre de nœuds intérieurs plus 1.
{: .a-faire}

Si chaque noeud intérieur a 2 successeurs $ \sum \delta(x) = 2 + f + (n-f - 1) \cdot 3$. Comme $\vert E \vert = \vert V \vert -1 = n -1$, assemble ces deux équations pour obtenir $n + 1 = 2f$.

### exemple du tas

#### le problème

#### une solution possible (naïve)

> Quel est le coût algorithmique d'utiliser une telle solution ?
{: .a-faire}

On n'a besoin que de regarder chaque patient lorsqu'il faut en prendre en charge un nouveau. On a pas besoin de faire des choses lorsque les patients changent d'état de gravité ou partent et arrivent. Mais à chaque fois c'est $\mathcal{O}(n)$ opérations.

#### un tas

Voir [wikipedia](https://fr.wikipedia.org/wiki/Tas_(informatique)) pour (presque) toutes les informations nécessaire sur cette belle structure.


> Des trois arbres ci-dessus lequel (il n'y en a qu'un) est binaire, complet et plein ?
{: .a-faire}

* (a) est binaire mais pas complet
* (b) est binaire complet mais pas plein
* (c) est binaire, complet et plein.

> * Créez un tas avec les nombres : 42, 12, 1, 3, 6, 5.
> * Y a-t-il plusieurs possibilités ?
> * que peut-on dire du nœud ayant le plus grand nombre ?

```text
    42
 12    3
6  5  1
```

Ou encore :

```text
    42
 12    6
6  1  5
```

Le plus grand noeud est **toujours** la racine du tas.

#### manipulation d'un tas

> Donner les algorithmes pour effectuer les opérations suivantes :
>
>1. ajout d'un élément
>2. modification d'une valeur
>3. suppression de la racine
{: .a-faire}

1. on l'ajoute à la fin et on le remonte (récursivement) si nécessaire
2. on change la valeur puis on échange avec un de ses successeurs ou son prédécesseur récursivement
3. on prend la dernière feuille, on la supprime et on modifie la racine avec la valeur de la feuille enlevée.

> En conclure que l'utilisation du tas est bien meilleure que la solution naïve.
{: .a-faire}

Toutes les opération nécessitent un nombre proportionnel à la hauteur du tas opérations. Et il y a $2^h$ éléments dans celui-ci. Nous opération sont donc toutes en $\mathcal{O}(\log_2(n))$ opérations.

#### pour la bonne bouche

> * En déduire une façon de trier un tableau de nombre.
> * trouver un de représenter un tas par une liste (on pourra parcourir le tas de haut en bas et de droite à gauche).
{: .a-faire}

On commence par un tas vide et on le remplit petit à petit (cela prend $n$ fois $\mathcal{O}(\log_2(n))$ opérations). Puis on supprime itérativement la racine $n$ fois. Ce qui prend encore $n$ fois $\mathcal{O}(\log_2(n))$ opérations.

On a donc un tri en $\mathcal{O}(n\log_2(n))$ opérations.

Pour la représentation en tableau, voir Voir [wikipedia](https://fr.wikipedia.org/wiki/Tas_(informatique)) (on les place dans l'ordre de haut en bas et de droite à gauche).

## parcours

> TBD
{: .note}

### trois parcours classiques

> Pour chaque parcours ci-après, donnez le résultat pour l'arbre de la partie [ordonnancement des sommets](#ordo-sommets) en supposant que `Examen de la Racine`signifie : affiche le numéro de la racine à l'écran.
>
> Une fois ceci fait, trouvez un ordre qui lira les sommets dans l'ordre alphabétique.
{: .a-faire}

## arbre dans des graphes connexe

> TBD
{: .note}

> Montrer que pour tout graphe connexe $G = (V, E)$, il existe au moins un arbre $T=(V, E')$ tel que $E' \subseteq E$.
{: .a-faire}

### graphe valué

#### une mise en situation

> Pourquoi ?
{: .a-faire}

#### un exemple

> * Quel est l'arête qui sera forcément dans tous les arbres couvrant de poids minimum ?
> * Quel est l'arête qui ne sera forcément jamais dans un arbre couvrant de poids minimum ?
> * y a-t-il plusieurs arbres couvrant de poids minimum pour ce graphe ?
{: .a-faire}

#### propriété

> * montrez que s'il existe deux arbres couvrant de poids minimum ne différent que d'une arête, alors elles on même valuation
> * montrez que si toutes les valuations sont différentes, il n'existe qu'un seul arbre couvrant de poids minimal.
> * montrez que la réciproque n'est pas vraie
{: .a-faire}

#### un algorithme

Voir [wikipedia](https://fr.wikipedia.org/wiki/Algorithme_de_Prim).

> Prouver que si G est connexe, alors T est connexe et est un arbre
{: .a-faire}

Une fois ceci fait :

> Prouver que $T$ est **un arbre couvrant de poids minimal** pour $G$
{: .a-faire}

Maintenant qu'on est sur que ça marche :

> Réalisez l'algorithme en entier sur le graphe précédent.
{: .a-faire}

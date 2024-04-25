---
layout: layout/post.njk
title: Algorithmes gloutons

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

L'objectif est de montrer l'intérêt des algorithmes gloutons, la façon de les construire et de prouver qu'ils fonctionnent. On s'attachera dans ce cours à prouver qu'ils rendent une solution optimale à un problème donné.

On va voir la construction et la preuve d'algorithmes gloutons pour résoudre des problèmes d'optimisation. On utilisera trois exemples, de plus en plus complexes :

1. [le rendu de pièce](./#exemple-le-rendu-de-pièces){.interne}
2. [l'allocation de ressources](./#exemple-allocation-de-salles-de-cinéma){.interne}
3. [ordonnancement](./#exemple-ordonnancement){.interne}

## Algorithmes gloutons

{% note %}
Un [algorithme glouton](https://fr.wikipedia.org/wiki/Algorithme_glouton) choisit à chaque étape la meilleure possibilité localement et ne se remet jamais en question.
{% endnote %}

Le schéma général d'un algorithme glouton est alors le suivant :

<div id="schéma-algo"></div>

```text
Ordonner E en (x_0, x_1, ..., x_n)
S = {}

pour chaque i de 1 à n:
    si S union {x_i} est une solution possible :
        ajouter x_i à S
```

On voit en creux que ce type d'algorithmes :

1. va être utilisé dans des problèmes d'optimisation où l'on cherche la _meilleure solution_ parmi un ensemble de possibilités.
2. l'ordre des étapes est primordial

Ils sont très utilisés car :

- ils donnent toujours un résultat
- ils sont souvent de complexités faibles

Attention cependant :

- ils ne donne pas forcément le meilleur résultat : c'est souvent des [heuristiques](https://fr.wikipedia.org/wiki/Heuristique)
- il n'y pas forcément de solution unique

En conclusion :

{% note %}
Ce type d'algorithmes est très utilisé pour résoudre des problèmes où l'on veut une réponse rapidement, mais pas forcément une réponse optimale. D'un point de vue théorique, ces algorithmes sont extrêmement importants. Il sont, par exemple, en bijection avec la [structure de matroïde](https://fr.wikipedia.org/wiki/Matro%C3%AFde).
{% endnote %}

Pour beaucoup de problèmes d'optimisation réels, un algorithme glouton est optimal pour une version simplifiée du problème. Comme l'algorithme va vite, on peut recommencer plusieurs fois pour trouver une meilleure solution.

### Comment designer un algorithme glouton

1. écrire le problème comme un problème d'optimisation
2. découper le problème en une succession d'étapes où il est facile de choisir la meilleure solution
3. choisir un ordre de parcours des différentes étapes

Un cas particulier important est lorsque le problème d'optimisation revient à trouver un sous-ensemble _optimal_ d'un ensemble connu. Dans ce cas là, l'item 2 revient à examiner itérativement les éléments de l'ensemble et à les ajouter un à un si possible à l'ensemble solution.

### Optimalité et glouton

Les problèmes d'optimalité demandent de trouver, parmi un ensemble de solutions possible, une solution minimisant (ou maximisant) un critère. Par exemple :

- pour un ensemble de coûts de constructions possibles d'une voiture, trouver celle qui minimise le coûts tout en maximisant la qualité totale des pièces
- parmi tous les parcours passant par un ensemble de villes donné, choisir celui qui minimise le nombre de kilomètres parcourus
- maximiser le nombre de films projetés dans un multiplexe de cinéma
- ...

La difficulté de ces problèmes vient du fait que l'on ne peut a priori pas trouver la meilleure solution sans les examiner toutes. Et s'il y a beaucoup de solutions ça peut prendre vraiment beaucoup de temps.

Certains problèmes cependant permettent d'être résolus en construisant petit à petit une solution, sans jamais remettre en cause ses choix. On peut alors souvent trouver très rapidement la meilleure solution possible. On peut également utiliser cette solution construite petit à petit pour trouver une solution approchée à un problème plus général. Cette classe d'algorithmes qui construit itérativement d'une solution est appelée _algorithmes gloutons_.

### Condition nécessaire et suffisante d'optimalité

On peut parfois prouver directement qu'un algorithme glouton est optimal et c'est parfois la solution la plus simple. Mais si l'approche directe n'est pas évidente il existe toujours une preuve par récurrence où on essaie de montrer que chaque étape du glouton peut mener à une solution optimale : 

En reprenant le [schéma générique de l'algorithme glouton](,/#schéma-algo) on prouve qu'il existe une solution optimale qui a fait à chaque étape du glouton les mêmes choix que lui :

- si `S union {x_i}`{.language-} était une solution possible alors `x_i`{.language-} est aussi dans la solution optimale considérée
- si `S union {x_i}`{.language-} n'était pas une solution possible alors `x_i`{.language-} n'est pas dans la solution optimale considérée

Ce qui prouvera l'optimalité de notre algorithme glouton.

### Preuve par l'absurde

On prouve couramment l'optimalité du glouton par l'absurde : 

{% note "schéma de preuve d'optimalité par l'absurde" %}
1. on suppose que la solution donnée par l'algorithme glouton n'est pas optimale
2. pour toute solution optimale il existe donc une étape $i$ où le glouton a :
    - soit choisi `x_i`{.language-} alors qu'il n'est pas dans la solution optimale considérée
    - soit refusé `x_i`{.language-} alors qu'il est dans la solution optimale considérée.
3. On choisi alors la solution optimale qui coïncide **le plus longtemps possible** avec l'algorithme glouton et on considère l'étape $i$ où leur choix a divergé :
    - jusqu'à l'étape $i-1$ les choix ont été identiques entre cette solution optimale et le glouton
    - pour toute autre solution optimale, la première divergence s'est passé à l'étape $i$ ou avant
4. On prouve que l'on peut construire une autre solution optimale qui coïncide avec le glouton jusqu'à l'étape $i$ ce qui invalide l'hypothèse de non optimalité du glouton.

{% endnote %}

## <span id="exemple-le-rendu-de-pièces"></span>Exemple 1 : le rendu de pièces

Proposons un algorithme glouton permettant de rendre la monnaie $R$ d'un achat en un nombre minimum de pièces valant $v=5$, $v=2$ et $v=1$ pokédollar.

### Design de l'algorithme

1. **écrire le problème comme un problème d'optimisation** : Il faut rendre un nombre minimum de pièces
2. **découper le problème en une succession d'étapes** : si l'on doit rendre en pièces d'une valeur de $v$, il faut rendre le maximum de pièces possibles, qui correspond à la division entière de $R$ par $v$. On va donc considérer à chaque étape qu'une seule valeur $v$ de pièce, puisqu'il est facile de trouver l'optimum dans ce cas là. Notre algorithme va donc itérativement rendre le nombre maximum de pièces pour une valeur de pièce donnée
3. **choisir un ordre de parcours** : comme il faut rendre le minimum de pièces données, on va examiner les pièces par valeur décroissantes

### Algorithme : rendu de pièce

- **Problème** : "comment rendre R sous en un nombre minimum de pièces"
- **algorithme glouton** :
  1. choisir la plus grande valeur $v$ de pièce plus petite que $R$
  2. donner $p$ pièces où $p$ est la division entière de $R$ par $v$ (`p = R // v`{.language-})
  3. $R = R - p \cdot v$
  4. revenir en 1. si $R > 0$
- **complexité** : tri des valeur de pièce + une opération par pièce (division puis soustraction). Comme il suffit de trier une fois pour toute, la complexité peut être de l'ordre du nombre de pièces

{% exercice %}
Codez l'algorithme en python.
{% endexercice %}
{% details "**Solution**" %}

```python
def rendu(R, pieces=(1, 2, 5)):
    pieces = list(pieces)
    pieces.sort()
    pieces.reverse()

    rendu = []
    for v in pieces:
        p = R // v
        R -= p * v

        rendu.append((v, p))

    return rendu
```

{% enddetails %}

### Preuve d'optimalité pour un système de pièce valant 1, 2 et 5

On a pas besoin ici de preuve par récurrence. On va analyser les propriétés d'une solution optimale et montrer que la solution de l'algorithme glouton les satisfait.

Considérons une solution optimale. Elle ne **peut pas** contenir :

- **plus de 2 pièces de 2**, sinon on pourrait rendre moins de pièces en échangeant 3 pièces de 2 par 1 pièce de 5 et une pièce de 1 ce qui diminuerait strictement le nombre de pièces rendues.
- **plus de 1 pièce de 1**, sinon on échangerait 2 pièces de 1 par une pièce de 2, ce qui diminuerait strictement le nombre de pièces rendues.

Enfin, cette solution optimale ne **peut pas avoir exactement 2 pièces de 2 et une pièce de 1**, sinon on les échangeraient pour une pièce de 5...

On en déduit donc que la somme d'argent rendu en pièce de 2 et de 1 pour une solution optimale ne peut dépasser 4, ce qui est exactement la division entière de $R$ par 5 et est le premier choix de l'algorithme glouton.

Après le premier choix (les pièces de 5), il ne reste à rendre qu'une somme inférieure ou égale à 4. Il n'y a plus qu'à montrer que pour les 5 cas possibles (lorsqu'il y a 0, 1, 2, 3 ou 4 à rendre) le glouton est optimal, ce qui est évident.

### Système de pièces quelconque ?

On peut démontrer que le système de pièce européen fonctionne avec les pièces et billets de : 1, 2, 5, 10, 20, 50, 100 et 200. Mais attention, cela ne marche pas pour tous les systèmes de pièces :

- exemple 1, 3, 4. Pour rendre 6 il donne 4 + 1 + 1 alors que c'est 3 + 3 le mieux.
- 1, 6, 11, 19 ne fonctionne pas non plus pour 22 par exemple, alors que le système de pièce forme une suite super-croissante ($v_i > v_1 + \dots + v_{i-1}$ pour tout $i >1$). De quoi tordre le coup à une légende urbaine persistante qui stipule en effet que les suites super-croissante permettent un rendu de pièces optimal avec l'algorithme glouton.

Remarques :

- ce n'est pas la seule solution possible pour avoir un système optimal puisque les américains ont des pièces de 25c (les quarter)
- cela peut poser des soucis : les machines à café vous indiquent qu'elles ne peuvent plus vous rendre la monnaie car il n'y a plus de pièces d'une valeur particulière, alors qu'en réalité elle disposent de la somme à rendre en utilisant une autre combinaison.

## <span id="exemple-allocation-de-salles-de-cinéma"></span>Exemple 2 : allocation de salles de cinéma

Un gérant de cinéma a en sa possession $m$ films caractérisés chacun par des couples ($d_i$, $f_i$) où $d_i$ est l'heure de début du film et $f_i$ l'heure de fin. Il se pose 2 problèmes :

- Quel est le nombre maximum de films que je peux voir en une journée ?
- Quel est le nombre minimum de salles à avoir pour visionner tous les films en stock.

Chaque film est décrit par un couple $(d, f)$ où $d$ est la date de début du film et $f$ la date de fin.

### Voir un maximum de films

1. **le problème d'optimisation** : on cherche à rendre une liste maximale de films à voir en une journée.
2. **découpage en étapes** : Comme il faut trouver un sous-ensemble maximal de films, chaque étape consistera en l'examen d'un film et voir si on peut le rajouter à l'ensemble déjà constitué.
3. **ordre d'examen des films** : date de fin croissante.

Pour l'ordre d'examen, il n'y a pas vraiment d'autre choix. En effet, si l'on classe les séances de cinéma par :

- durée croissante : l'ensemble de films $[(1, 3), (3, 5), (5, 7), (2.5, 3.5), (4.5, 5.5)]$ produit un contre exemple,
- date de début croissante : l'ensemble de films $[(1, 10), (2, 3), (3, 4)]$ produit un contre exemple,

#### Algorithme : maximum de films

- **entrée** : liste de films, chaque liste étant une liste `[depart, fin, nom]`{.language-}
- **sortie** : liste ordonnée de films possible

```python
def nombre_films_maximal(films):

    films.sort(key=lambda x: x[1])

    films_a_voir = [films[0]]
    for film in films:
        fin_dernier_film = films_a_voir[-1][1]
        début_nouveau_film = film[0]
        if fin_dernier_film <= début_nouveau_film:
            films_a_voir.append(film)

    return films_a_voir
```

La sortie de l'algorithme glouton correspond à un ordre de visionnage de films maximisant le nombre de films vus.

{% info %}
On a utilisé quelques astuces de programmation python :

- `l[-1]`{.language-} rend le dernier élément d'une liste.
  boucle `for`{.language-}.
- on a un peu fait de magie noire sur les tris en utilisant le paramètre [key](https://docs.python.org/fr/3/howto/sorting.html#key-functions) qui permet de passer une fonction en paramètre. Cette fonction est appelé pour chaque élément. C'est pratique pour ne trier que selon 1 élément d'une liste (ici le 2ème élément).
- on utilise aussi l'écriture lambda qui permet de créer des fonction d'une ligne anonyme. Notre fonction lambda est équivalente à la fonction `fonction_lambda_anonyme`{.language-} suivante :

```python
def fonction_lambda_anonyme(x):
    return x[1]
```

{% endinfo %}

#### Preuve de l'algorithme : maximum de films

On prouve notre algorithme en utilisant la technique de preuve par l'absurde : on suppose que l'algorithme glouton ne donne pas une solution optimale et on considère la solution optimale à $m^\star$ films dont l'ordre de visionnage des films coïncide le plus longtemps possible avec la solution donnée par celui-ci.

Soit $i$ l'indice de l'étape de la première différence. Bornons cet indice :

- on ne peut pas avoir $i > m$ car par construction de l'algorithme glouton, tout film qui n'est pas choisit par lui entre en conflit avec au moins un film choisi.
- on peut en revanche avoir $i=1$ si les deux listes ne commencent pas par le même film

On a donc $1 \leq i \leq m$ et deux cas sont possibles :

1. soit le film $f_i$ a été refusé par l'algorithme glouton alors qu'il est dans la solution optimale
2. soit le film $f_i$ a été accepté par l'algorithme glouton alors qu'il n'est pas dans la solution optimale

Le premier cas est impossible car s'il a été refusé par l'algorithme glouton, c'est qu'il empiète avec un film déjà accepté et comme les solutions optimale et gloutonne coïncident jusqu'à $i$ ces films sont aussi dans la solution optimale.

Dans le deuxième cas, si $(f^\prime_{j})_{1 \leq j \leq m'}$ est sa liste optimale de films à voir on a :

- $f'_j = f_j$ pour $j< i$
- $f'_i \neq f_i$

Par construction de l'algorithme glouton, la date de fin de $f'_i$ est plus grande que la date de fin de $f_i$. On peut alors échanger $f_i$ et $f'_i$ pour créer une nouvelle solution optimale $(f'')$ telle que :

- $f''_j = f_j$ pour $j\leq  i$
- $f''_j = f'_j$ pour $j >  i$

Ceci est impossible par hypothèse (on prend la solution optimale coïncidant le plus longtemps possible avec la solution de l'algorithme glouton) : notre hypothèse était fausse, l'algorithme glouton est optimal.

### Nombre minimum de salles pour placer tous les films en stock

On essaie ici de trouver le nombre minimum de salles à construire pour pouvoir projeter tous les films

#### Algorithme : nombre de salle minimum

On va ici classer les films par date de début croissante. On commence par 0 salles de cinéma.

En analysant dans cet ordre les films, on cherche s'il existe une salle à laquelle on peut rajouter le film (la date de fin du dernier film de la salle est plus tôt que le début du nouveau film). Si oui on rajoute le film à cette salle, si non on crée une nouvelle salle et l'on ajoute notre film à cette nouvelle salle.

{% exercice %}
Codez l'algorithme en python.
{% endexercice %}
{% details "**Solution**" %}

```python
def nombre_salles(films):
    films.sort(key=lambda x: x[0])

    salles = [[films[0]]]
    for film in films[1:]:
        nouvelle_salle = True
        for salle in salles:
            dernier_film = salle[-1]
            if film[0] >= dernier_film[1]:
                salle.append(film)
                nouvelle_salle = False
                break
        if nouvelle_salle:
            salles.append([film])
```

{% enddetails %}

#### Preuve de l'algorithme : minimum de salles

La preuve est ici aisée car si on rajoute une salle pour loger un nouveau film $f$, ça veut dire que pour toutes les $k$ salles actuelles il y a un film qui n'est pas fini pendant le début du nouveau film : il existe au moins $k$ films dont le début est avant $f$ et la fin après $f$ : il faut donc au moins $k+1$ salles pour jouer tous ces films en parallèle.

## <span id="exemple-ordonnancement"></span>Exemple 3 : ordonnancement

Les problèmes d'ordonnancement sont multiples. Certains sont durs d'autres faciles. Mais un algorithme glouton permet de trouver souvent une solution acceptable pour beaucoup d'entres eux et même parfois optimale pour certains problèmes.

Le problème suivant est résoluble par un algorithme glouton : On considère $m$ produits de durée 1 à fabriquer. Si le produit $i$ est réalisée avant la date $d_i$ on peut le vendre pour un prix $p_i$, sinon il est invendable (exemple : de faux billets de match de foot ou de concerts par exemple). Proposez un algorithme permettant de maximiser les profits en considérant que l'on a qu'un seul ouvrier.

Il faut donc trouver un sous-ensemble de produits à créer parmi la liste de toutes les possibilités (exemple : la liste de toutes les dates de match de foot ou de concerts) **et** l'ordre dans lequel les produire. Il faut a priori optimiser deux paramètres alors que les algorithmes gloutons classiques ne sont fait que pour en optimiser un seul.

Commençons par montrer que cet ordre est facile à trouver.

### Ordre de production

Un ensemble de produits est dit _compatible_ s'il existe un ordonnancement de leur production permettant de tous les vendre (chaque produit est fabriqué avant sa date de péremption).

On a la proposition suivante :

{% note %}
Un ensemble de produits est compatible si et seulement si la production par date $d_i$ croissante permet de tous les vendre.
{% endnote %}

Preuve :

- si la production par date croissante permet de tout vendre il est compatible
- s'il existe un autre ordonnancement avec la tâche $j$ placé avant la tâche $i$ alors que $d_j > d_i$, on peut échanger la tâche $i$ et la tâche $j$ et l'ordonnancement reste compatible

Grace à cette propriété, on est ramené à un problème glouton classique : on a plus qu'un seul paramètre à optimiser : le profit.

### Algorithme : ensemble compatible maximum

Montrons que l'algorithme glouton suivant est optimal :

1. on trie les produits par prix décroissant
2. $S = \\{\\}$
3. pour chaque produit $x$ examiné par ordre de prix décroissant : on ajoute $x$ à $S$ s'il reste compatible
4. rendre $S$ (qui est un ensemble de profit maximal)

{% exercice %}
Codez l'algorithme en python.
{% endexercice %}
{% details "**Solution**" %}

```python
def produits_est_compatible(liste_produit):
    liste_produit.sort(key=lambda x: x[0])

    for date, produit in enumerate(liste_produit):
        if date + 1 > produit[0]:
            return False
    return True

def produits_maximum_profit(liste_produit):
    liste_produit.sort(key=lambda x : x[1])
    liste_produit.reverse()

    ensemble_max = []
    for produit in liste_produit:
        if produits_est_compatible(ensemble_max + [produit]):
            ensemble_max.append(produit)

    return ensemble_max
```

{% enddetails %}

### Preuve : ensemble compatible maximum

#### <span id="init-optimisation"></span>Initialisation

Si une solution ne contient pas l'élément de prix maximum on l'échange avec le 1er élément produit et la solution reste compatible tout en ayant un profit plus grand

#### <span id="récurrence-optimisation"></span> Récurrence

Si une solution optimale et la solution gloutonne coïncident au bout de $i$ étapes (les éléments pris le sont pour les deux solutions et les éléments écartés le sont aussi pour les deux solutions), à l'étape $i+1$ on a deux cas :

- on écarte ce produit car la solution n'est plus compatible pour la solution gloutonne. Comme La solution optimale contenait jusqu'à présent tous les éléments de la solution gloutonne, le produit de l'étape $i+1$ n'est pas on plus compatible avec la solution optimale.
- on ajoute le produit à la solution gloutonne. Si la solution optimale ne contient pas ce produit on peut échanger n'importe quel autre élément que les $i-1$ premiers éléments de la solution avec celui-ci pour augmenter le profit.

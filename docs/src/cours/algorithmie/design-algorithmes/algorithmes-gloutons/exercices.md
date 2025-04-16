---
layout: layout/post.njk
title: Exercices gloutons

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Exercices de créations d'algorithmes gloutons pour résoudre divers problèmes d'optimisation. On a séparé les exercices en deux grandes parties : la première où la stratégie gloutonne est optimale (et où il faut le démontrer), la seconde où elle ne l'est pas mais dont on peut garantir les performances.

Attention, souvent les algorithmes gloutons n'ont pas de garanties du tout. Beaucoup d'algorithmes gloutons sont juste des heuristiques qui peuvent être aussi mauvaises que possible, les utiliser dépend alors de la nature des données. Nous n'en parlons cependant pas ici car, en général, les étudiants ont rarement besoin de profs pour écrire des algorithmes non optimaux et sans garanties...

## Gloutons optimal

Comme toujours lorsque l'on crée un algorithme glouton, la principale difficulté est de trouver l'ordre dans lequel considérer les objets. Une fois cet ordre trouvé les preuves sont toujours les mêmes (mais il faut tout de même les faire).

## <span id="exemple-allocation-de-salles-de-cinéma"></span>Exemple 2 : allocation de salles de cinéma

> TBD à mettre sous la forme d'un exercice

Un gérant de cinéma a en sa possession $m$ films caractérisés chacun par des couples ($d_i$, $f_i$) où $d_i$ est l'heure de début du film et $f_i$ l'heure de fin. Ces couples sont fixés et il ne peut pas les modifier. Il se pose 2 problèmes :

- Quel est le nombre maximum de films qu'une personne peux voir en une journée ?
- Quel est le nombre minimum de salles à construire pour qu'une personne puisse voir un film quelconque qu'elle aura choisi.

### Voir un maximum de films

1. **le problème d'optimisation** : on cherche à rendre une liste maximale de films à voir en une journée.
2. **découpage en étapes** : Comme il faut trouver un sous-ensemble maximal de films, chaque étape consistera en l'examen d'un film et voir si on peut le rajouter à l'ensemble déjà constitué.
3. **ordre d'examen des films** : date de fin croissante.

Pour l'ordre d'examen, il n'y a pas vraiment d'autre choix que la date de fin croissante. En effet, si l'on classe les séances de cinéma par :

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


### Réservation SNCF

On suppose que $n$ personnes veulent voyager en train un jour donné. La personne $i$ veut prendre le train $t_i$.

Les données du problème sont :

- $K$ trains partent dans la journée,
- le train $j$ part avant le train $j+1$,
- chaque train ne peut contenir plus de $P$ passagers.

{% exercice "**Solution possible ?**" %}
Proposez un algorithme qui vérifie que pour un nombre de trains donné et une liste de trains choisis, il est possible de faire voyager tout le monde.
{% endexercice %}
{% details "corrigé" %}

Une solution en $\mathcal{O}(n+K)$ :

```python
d = [0] * K

for i in range(n):
    d[t[i]] += 1

for t in range(K):
    if d[t] > P:
        print("le train", t, "contient", d[t] - P, "passagers de trop.")
```

{% enddetails %}

On suppose maintenant que la personne $i$, si elle ne peut pas prendre le train $t_i$ parce qu’il est complet, accepte de prendre un des trains suivants (s’il y en a un).

{% exercice "**Solution approchée**" %}
Proposez un algorithme minimisant l'attente globale pour faire voyager tous les voyageurs.

{% endexercice %}
{% details "corrigé" %}

```python
for i in range(n):
    while d[t[i]] > P:
        d[t[i]] -= 1  # on supprime le passager i de son train initial
        t[i] += 1  # le passager i prend le train suivant
        d[t[i]] += 1  # on augmente son nouveau train de 1 passager
```

A chaque itération de la boucle for, le passager $i$ est placé dans le premier train possible qui part après son train initialement voulu si celui-ci est plein.

Notez que cet algorithme permet de faire partir tous les voyageurs dans leur train initial s'il était non plein au départ.

Cette solution est optimale pour la fonction $\sum_{i\geq 1}(t'[i] - t[i])$ où $t'[i]$ est le train effectivement pris par le passager $i$.

{% enddetails %}

### Une quête d'essence

Une route comporte $n$ stations services numérotées dans l’ordre du parcours, de $0$ à $n-1$. La distance du départ à la station $i$ est de $d_i$ kilomètres et on considère que $d[0] = 0$.

Le but est d'atteindre la dernière station de la route avec un réservoir de $L$ litres d'essence, en considérant qu'un litre d'essence permet de faire 1 kilomètre.

{% exercice  "**Admissibilité**" %}
Donnez une condition nécessaire et suffisante pour que l'automobiliste puisse parcourir toute la route jusqu'à la dernière station service.

{% endexercice  %}
{% details "corrigé" %}

Il faut et il suffit que les stations services soient éloignées de moins de $L$ kilomètres.

{% enddetails %}

On essaie de minimiser les arrêts pour rallier la dernière station du parcours. On suppose de plus que l'on part réservoir vide.

{% exercice  "**Minimum d'arrêts**" %}

Écrivez un algorithme glouton qui donne le nombre minimum de stations auxquelles il faut mettre de l'essence dans le réservoir pour arriver à destination, en supposant que le réservoir est initialement vide.

{% endexercice  %}
{% details "corrigé" %}

Il faut aller le plus loin possible à chaque fois : la prochaine station est la station la plus éloignée dont la distance est inférieure à $L$.

```python
S = [0]
for i in range(2, n):
    s = S[-1]
    if d[i] - d[s] > L;
        s.append(i - 1)
```

Soit $s_i$ la première station d'une solution optimale qui ne correspond pas avec la station $g_i$ choisie par le glouton. On a :

- $i>0$ puisque la première station est la station de départ
- $s_{i-1} = g_{i-1}$

On en conclut que $s_i < g_i$ et que l'on peut choisir $g_i$ comme $i$ ème choix pour la solution optimale et que, comme justement la solution est optimale, $s_{i+1} > g_i$ sinon on aurait pu s'en passer.

Le raisonnement précédent montre que l'on peut construire une solution optimale qui coïncide avec le glouton : le glouton est optimal.

{% enddetails %}

On suppose que le prix de l'essence à la station $i$ vaut $p_i$.

{% exercice  "**Prix fluctuant**" %}
Donnez un algorithme glouton optimal permettant de réaliser le parcours au prix minimum.
{% endexercice  %}
{% details "corrigé" %}

On considère les stations par prix croissants et on leur associe à chacune un recouvrement de taille $L$.

Dans l'exemple ci-dessous on considère que l'ordre de prix croissant est le nombre, que chaque case fait 1km et que $L=10$ :

```text
1111111111
               2222222222
      3333333333
         4444444444
1     3  4     2        5   : ordre des prix
1     2  3     4        5   : ordre dans le parcours
```

Pour chaque kilomètre on prend ensuite la station dont le prix est le plus faible :

```text
1111111111
               2222222222
          33333

1     3  4     2        5
1     2  3     4        5
```

On voit dans l'exemple que la station 4 est inutile et qu'il faut tout de même mettre de l'essence en passant à la station 3.

L'algorithme est alors le suivant :

```python
K = [None] * d[n - 1]
ordre_stations = list(range(n))
ordre_stations.sort(key=lambda i: p[i])

for i in ordre_station:
    for k in range(d[i], d[i] + L):
        if K[k] is None:
            K[k] = i


```

Le nombre de litres qu'il faut ajouter lorsque l'on s'arrête à la station $i$ est le nombre de $i$ conservé dans la liste :

```python
station_essence_achat = [K.count(i) for i in range(n)]
```

La preuve de l'optimalité vient du fait que l'essence mise à la station $i$ permet de faire la distance allant de $d_i$ à $d_i + L$. On a gardé que les kilomètres ne pouvant pas être couvert par une station ayant un prix inférieur.

{% enddetails %}

## Problèmes d'ordonnancements

Les problèmes d'ordonnancement sont très importants car nombre de problèmes courants peuvent s'écrire sous cette forme. Nous allons voir dans cette partie quelques exemples où l'approche gloutonne est optimale.

### Ordonnancement avec pénalité

[Comme dans le cours](../principe/#exemple-ordonnancement){.interne} mais chaque tâche a un coût si on ne la réalise pas à temps.

{% exercice %}
Le but est de minimiser la somme des pénalités.
{% endexercice %}
{% details "corrigé" %}
Tout pareil.

Il suffit de dire que la pénalité est un gain qu'on cherche à maximiser : on réalisera en priorité les tâches avec la plus grande pénalité et donc on minimisera les pénalités des tâches non effectuées.
{% enddetails %}

### Ordonnancement avec départ différé

On suppose que l'on a $n$ tâches à réaliser par **un unique** ouvrier et chaque tâche $1\leq i \leq n$ met $p_i$ unités de temps à être effectuée. Une fois que l'ouvrier commence une tâche, il la termine : s'il effectue la tâche $i$, il ne fait rien d'autre pendant $p_i$ unités de temps.

On veut minimiser la somme des débuts de réalisations des tâches.

{% exercice  "**Formalisation du problème**" %}
En supposant que l'on a effectué les tâches dans l'ordre $\sigma_1, \dots, \sigma_n$ :

1. donnez le temps minimum de départ et de fin des tâches $\sigma_1$, $\sigma_2$ et $\sigma_3$
2. en déduire que la valeur de la somme totale des temps de départ des tâches vaut $\sum_i(n-i)p_{\sigma_i}$
   {% endexercice %}
   {% details "corrigé" %}

- la tâche $\sigma_1$ a commencé en 0 et a fini en $p_{\sigma_1}$
- la tâche $\sigma_2$ a commencé en $p_{\sigma_1}$ et a fini en $p_{\sigma_1} + p_{\sigma_2}$
- la tâche $\sigma_3$ a commencé en $p_{\sigma_1} + p_{\sigma_2}$ et a fini en $p_{\sigma_1} + p_{\sigma_2} + p_{\sigma_3}$

On a donc la formule suivante pour donner la somme de toutes les débuts de tâches :

<div>
$$
   T = \sum_{1\leq i \leq n}( \sum_{1\leq j < i}p_{\sigma_j}) = \sum_i(n-i)p_{\sigma_i}
$$
</div>

{% enddetails %}

{% exercice  "**Exemple**" %}
Quel est l'ordre d'exécution des tâches minimisant la somme des débuts de tâches pour trois tâches de temps de réalisation $p_1 = 1$, $p_2 = 3$ et $p_3 =5$.
{% endexercice %}
{% details "corrigé" %}

Pour les 3 tâches, il y a 6 ordonnancements possibles qui donnent respectivement :

- 1 puis 3 puis 5 : $T = 2 \cdot 1 + 1 \cdot 3 = 5$
- 1 puis 5 puis 3 : $T = 2 \cdot 1 + 1 \cdot 5 = 7$
- 3 puis 1 puis 5 : $T = 2 \cdot 3 + 1 \cdot 1 = 7$
- 3 puis 5 puis 1 : $T = 2 \cdot 3 + 1 \cdot 5 = 11$
- 5 puis 1 puis 3 : $T = 2 \cdot 5 + 1 \cdot 1 = 11$
- 5 puis 3 puis 1 : $T = 2 \cdot 5 + 1 \cdot 3 = 13$

{% enddetails %}

L'exemple précédent a dû vous donner une idée de l'ordre associé au glouton :

{% exercice  "**Ordre d'exécution des tâches**" %}
Donnez (et prouvez) un algorithme glouton permettant de trouver l'ordre optimal d'exécution des tâches pour minimiser la valeur moyenne des débuts de réalisations.
{% endexercice %}
{% details "corrigé" %}

Minimiser la valeur moyenne des débuts de réalisation minimise $T/n$. Il suffit donc de minimiser $T$.

L'ordre selon lequel il faut ordonner les tâches est par durée décroissante. S'il existait en effet $i < j$ tel que $p_{\sigma_i} > p_{\sigma_j}$ changer les deux tâches diminuerait strictement $T$ puisque $n-i > n-j$. Cet ordre donne directement l'algorithme glouton :

```text
On trie les tâches par durée croissante
Pour chaque tâche dans cet ordre:
    réaliser cette tache
```

{% enddetails %}

On suppose maintenant que toutes les tâches ne sont pas immédiatement disponibles. Chaque tâche $i$ a maintenant une date $d_i$ à partir de laquelle elle peut être réalisée.

{% exercice  "**Départs différés**" %}
Donnez (et prouvez) un algorithme glouton permettant de trouver l'ordre optimal minimisant la valeur moyenne des débuts de réalisations.
{% endexercice %}
{% details "corrigé" %}

Le même raisonnement que précédemment montre que l'on peut ordonner les tâches par $d_i + p_i$ croissants.

{% enddetails %}

On suppose maintenant que l'ouvrier peut mettre en pause la réalisation d'une tâche puis la reprendre ultérieurement. Par exemple il peut commencer la tâche $i$ de temps de réalisation $p_i = 5$, la réaliser pendant 2 unités de temps, puis la mettre en pause pour réaliser la tâche $j$ puis, une fois la tâche $j$ terminée, reprendre la tâche $i$ et la finir en y passant les 3 unités de temps restantes.

{% exercice  "**Tâches fragmentables**" %}
Donnez (et prouvez) la méthode permettant de minimiser la moyenne des débuts de chaque tâche.

{% endexercice %}
{% details "corrigé" %}

On peut à chaque unité réaliser une unité de temps de la tâche qui se finit au plus tôt parmi les tâches que l'on peut réaliser. Ceci garantit que les tâches sont bien réalisées de la plus rapide à la plus lente.

{% enddetails %}

### Ordonnancement avec retard

On suppose que pour mener à bien un projet, on doit réaliser $n$ tâches où chaque tâche $t_i$ a :

- une durée de réalisation : $d_i$
- un temps de fin conseillé : $f_i$

Si on note $s_i$ le début de la réalisation de la tâche $t_i$ on définit son retard par :

<div>
$$
    r_i = \max(0, s_i + d_i - f_i)
$$
</div>

Si $r_i > 0$ la tâche $t_i$ est en retard. Le but du problème est de trouver un algorithme glouton qui affecte à chaque tâche son début et qui minimise le retard maximum : $$R = \max_{1\leq i \leq n} r_i$$

Comme on n'a qu'un seul ouvrier pour réaliser les tâches, on ne peut créer qu'une tâche à la fois.

{% exercice  "**Premières propriétés**" %}

1. Montrez que le retard d'une solution ne peut pas augmenter si l'on supprime les temps d'inactivité de celle-ci : l'ouvrier enchaîne les tâches sans s'arrêter jusqu'à ce que toutes les tâches aient été réalisées.
2. En déduire que la solution de notre problème est un ordonnancement des tâches selon un ordre particulier : c'est un algorithme glouton sans étape de choix (toutes les tâches sont dans la solution).

{% endexercice  %}
{% details "corrigé" %}
Si l'on réduit l'inactivité de l'ouvrier, les tâches vont commencer plus tôt, donc $s_i$ va diminuer et donc $r_i$ aussi : $R$ ne peut que diminuer.

La remarque précédente nous indique que l'ouvrier doit commencer une nouvelle tâche immédiatement après avoir fini la précédente.
{% enddetails %}

On suppose que les tâches $(t_i)_{1\leq i \leq n}$ sont rangées dans un certain ordre. Écrivez l'algorithme qui calcule le retard maximum pour cet ordre. Quelle est sa complexité ?

{% exercice  "**Mauvais ordres**" %}
Montrez que les ordres suivants ne sont pas optimaux :

- Les tâches triées par durée décroissante.
- Les tâches triées par durée croissante.

{% endexercice  %}
{% details "corrigé" %}

Durée croissante :

- $d_1 = 1$, $f_1 = 11$
- $d_2 = 10$, $f_2 = 10$

Durée décroissante :

- $d_1 = 10$, $f_1 = 11$
- $d_2 = 1$, $f_2 = 1$

{% enddetails %}

{% exercice  "**Ordre optimal**" %}

Montrez que si une solution possède deux tâches successives $t_{i}$ et $t_{i+1}$ telles que $f_{i} > f_{i+1}$, les échanger n'augmente pas le retard.

En déduire l'ordre optimal.
{% endexercice  %}
{% details "corrigé" %}

On a $r_{i+1} = s_{i+1} + d_{i+1} - f_{i+1} = s_{i} + d_{i} + d_{i+1} - f_{i+1}$, donc :

- $r_{i+1} \geq s_{i} + d_{i+1} - f_{i+1}$
- $r_{i+1} \geq s_{i} + d_{i+1} + d_{i} - f_{i}$, si $f_{i}> f_{i+1}$

L'échange des deux tâches n'augmente pas le retard maximal.

Si l'on range les éléments par taille de fin demandée croissante, on est alors minimal car $f_{i}< f_{i+1}$ pour tout $i$ est équivalent à $f_{i}< f_{j}$ pour tout $i<j$.

{% enddetails %}

## <span id="exemple-ordonnancement"></span>Exemple 3 : ordonnancement

Les problèmes d'ordonnancement sont multiples. Certains sont durs, d'autres faciles. Mais un algorithme glouton permet de trouver souvent une solution acceptable pour beaucoup d'entres eux et même parfois optimale pour certains problèmes.

Le problème suivant est résoluble par un algorithme glouton : on considère $m$ produits de durée 1 à fabriquer. Si le produit $i$ est réalisée avant la date $d_i$ on peut le vendre pour un prix $p_i$, sinon il est invendable (exemple : de faux billets de match de foot ou de concerts par exemple). Proposez un algorithme permettant de maximiser les profits en considérant que l'on n'a qu'un seul ouvrier.

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
2. $S = []$
3. pour chaque produit $x$ examiné par ordre de prix décroissant : on ajoute $x$ à $S$ s'il reste compatible
4. rendre $S$ (qui est une liste de profit maximal)

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

## Glouton pas optimal mais pas mal

### Équilibrage de charge

On appelle **_équilibrage de charge_** (_load balancing_) le problème suivant :

- On possède $m$ machines et $n$ tâches à effectuer.
- Chaque tâche $j$ nécessite $t_j$ unités de temps pour être effectuée par une machine.
- Pour chaque machine $i$, on associe l'ensemble $M_i$ des tâches effectuées par celles-ci, et on note $T_i$ le temps passé à effectuer ces tâches : $T_i = \sum_{j \in M_i} t_j$.

On cherche à trouver les ensembles $M_i$ permettant de minimiser la quantité : $\max_{1\leq i \leq m} T_i$. On note $T^\star$ ce minimum.

La encore, ce problème est :

- [crucial en pratique](https://fr.wikipedia.org/wiki/R%C3%A9partition_de_charge)
- NP-difficile

{% exercice  "**Quelques propriétés**" %}

1. Montrez que l'on a $T^\star \geq \max_{1 \leq j\leq n} t_j$.
2. Montrez que l'on a $T^\star \geq \frac{1}{m}\sum_{1 \leq j\leq n} t_j$ (**attention**, c'est bien $\frac{1}{m}$ et non $\frac{1}{n}$).

{% endexercice  %}
{% details "corrigé" %}
La première inégalité vient du fait que toute tâche doit être effectuée par une machine : la machine $i$ qui réalisera la tâche de plus longue durée aura un $T_i$ plus grand que cette durée.

La seconde inégalité est identique à celle du bin packing (exercice précédent). On peut le démontrer en remarquant que pour une assignation donnée on a l'inégalité : $\frac{1}{m}\sum_i T_i \leq \max_i T_i$ et que $\sum_i T_i = \sum_j t_j$. L'inégalité étant vraie pour toute assignation donc également pour l'assignation optimale.
{% enddetails %}

L'algorithme glouton que l'on utilisera pour résoudre le problème consistera à ajouter itérativement une tâche à la machine $i$ réalisant $T_i = \min_{1\leq j \leq m} T_j$.

{% exercice  "**Un algorithme glouton**" %}

- Dans quel ordre proposez-vous de ranger les tâches ? Justifiez votre réponse.
- Montrez que s'il y a $m$ tâches ou moins à classer, l'algorithme glouton trouve la solution optimale.
  {% endexercice %}
  {% details "corrigé" %}
  Il vaut mieux répartir les tâches longues sur plusieurs machines, par exemples pour trois machines la répartition $[(4,), (4,), (1, 1, 1)]$ est préférable à la répartition $[(1, 4), (1, 4), (1,)]$ de 5 tâches de durée 4, 4, 1, 1 et 1.

On rangera donc les tâches par **durées décroissantes**.

Il est clair que s'il y a moins de $m$ tâches à ranger chaque machine aura au plus 1 tâche : la répartition sera optimale.
{% enddetails %}

On considère une réalisation de l'algorithme. Soit $i^\star$ la machine réalisant $T_{i^\star} = \max_{1\leq i \leq m} T_i$ à la fin de l'algorithme, et $j$ l'indice de la dernière tâche qui lui a été assignée au cours de l'exécution de l'algorithme.

{% exercice  "**Propriétés**" %}

1. Montrez qu'à la fin de l'algorithme, on a $T_{i^\star} -t_j \leq T_k$ pour tout $k$.
2. En déduire que $T_{i ^\star} - t_j \leq \frac{1}{m}\sum_{1\leq k\leq m}T_k$.
3. Déduire de la déduction que $T_{i ^\star} - t_j \leq T^\star$.
4. Puis que $T_{i ^\star} \leq 2 \cdot T^\star$.

{% endexercice %}
{% details "corrigé" %}

1. avant l'affectation de la tâche $j$ à la machine, son temps total était le plus faible. S'il y a eu des tâches d'affectées après la tâche $j$ elles l'ont été à d'autres machines qui ont augmenté leur temps total d'exécution, la propriété est donc toujours vrai à la fin de l'algorithme.
2. En sommant l'inégalité précédente pour toutes les machines on obtient : $m\cdot(T_{i^\star} -t_j)\leq \sum_{1\leq k\leq m}T_k$
3. vient directement du fait que $\frac{1}{m}\sum_{1\leq k\leq m}T_k = \frac{1}{m}\sum_{1 \leq j\leq n} t_j \leq T^\star$
4. clair puisque $t_j \leq \max t_k \leq T^\star$
   {% enddetails %}

Les propriétés précédentes nous permettent de déduire que l'algorithme glouton est à performance garantie :

{% exercice  "**Performances**" %}

- Montrez que la solution proposée par l'algorithme glouton est au pire 2 fois moins bonne que la solution optimale.
- Montrer que cette performance est atteinte quelque soit l'ordre des tâches utilisé.
  {% endexercice %}
  {% details "corrigé" %}
  La première partie est évidente et comme les inégalités ne dépendent pas de l'ordre choisit la seconde également.
  {% enddetails %}

## Heuristique : plan de tables

Une de vos cousines se marie et vous a demandé de faire le plan de table du repas de noces. Pour maximiser la convivialité du repas elle vous demande :

- de ne mettre à chaque table que des personnes qui s'entendent;
- d'avoir un petit nombre de tables.

{% attention %}
On ne demande pas que le nombre de tables soit minimum.
{% endattention %}

On voit tout de suite l'importance crucial de problème... NP-difficile. Pour dernier exemple où l'algorithme glouton est une heuristique. Il n'est pas optimal et n'est pas à performance garantie. Mais en pratique ça va, il est utilisé intensivement pour créer des groupes projets, des équipages d'avions, dessiner des cartes de géographie, etc.

#### Modélisation

Un plan de table $P$ est une structure de données contenant :

- une liste $\verb|NOMS|$ contenant le nom de tous les invités;
- une liste $\verb|IC|$ d'incompatibilités où $\verb|IC[i]|$ contient un ensemble d'indices tel que si $\verb|j|$ est dans $\verb|IC[i]|$ alors $\verb|NOMS[i]|$ ne peut être à la même table que $\verb|NOMS[j]|$.

On suppose de plus que la relation d'incompatibilité est symétrique (si $\verb|j|$ est dans $\verb|IC[i]|$ alors $\verb|i|$ est dans $\verb|IC[j]|$). Par exemple si les invités sont : _"tata Guillemette"_, _"cousin Valentin"_, _"tonton Julien"_, _"papy François"_ et _"soeur Manon"_ et que les relations sont :

- _"tata Guillemette"_ aime bien tout le monde
- _"papy François"_ n'aime personne à part _"tata Guillemette"_
- _"cousin Valentin"_ ne supporte pas _"soeur Manon"_

On a la structure de données suivante (où $\verb|{...}|$ représente des ensembles) :

- $\verb|NOMS = ["tonton Julien", "papy François", "tata Guillemette", "cousin Valentin", "soeur Manon"]|$
- $\verb|IC = [{1}, {0, 3, 4}, {}, {1, 4}, {3, 1} ]|$

Résoudre le problème revient à trouver un plan de table (chaque invité est associé à une table unique) valide (deux invités à une même table ne doivent pas avoir d'incompatibilité), c'est-à-dire créer une liste $\verb|tables|$ telle que :

- chaque élément de $\verb|tables|$ est un ensemble d'indices tel que si $i \in \mbox{tables}[k]$ alors l'invité $\verb|NOMS[i]|$ est placé à la table numéro $k$
- pour tout indice $i\geq 0$ strictement plus petit que le nombre d'invités, il existe un unique $k$ tel que $i \in \mbox{tables}[k]$
- si $i, j \in \mbox{tables}[k]$ alors $j \notin \mbox{IC}[i]$

{% exercice %}

1. Montrez que quelles que soient les incompatibilités et le nombre d'invités, il existe un plan de table valide.
2. Justifiez que pour l'exemple, le nombre minium de tables est 3.
3. Combien de solutions à 3 tables différentes existe-t-il ?
4. Montrez que si l'on supprime l'incompatibilité entre _"papy François"_ et _"soeur Manon"_ dans l'exemple alors il existe une solution à 2 tables.
   {% endexercice %}
   {% details "corrigé" %}
5. Il suffit de mettre une personne par table pour satisfaire toutes les incompatibilités
6. _"papy François"_ (1) doit être sur une table différente de _"cousin Valentin"_ (3) et _"soeur Manon"_ (4) qui eux-mêmes doivent être sur deux tables distinctes : il faut au minimum 3 tables. Comme l'affectation $[\\{1, 2 \\}, \\{3, 0\\}, \\{4\\}]$ fonctionne, 3 est bien le nombre minimum de tables pour réaliser l'affectation.
7. Comme _"tonton Julien"_ ne peut être avec _"papy François"_ il a 2 tables possibles et comme _"tata Guillemette"_ peut aller partout elle a 3 choix. Le nombre total de choix est donc $2 \cdot 3 = 6$
8. $[\\{1, 2, 4 \\}, \\{3, 0\\}]$ est possible.

{% enddetails %}

On se propose d'écrire un algorithme glouton permettant de résoudre le problème :

1. créer une liste $\verb|ordre|$ contenant les indices de tous les convives;
2. créer une liste vide $\verb|tables|$
3. pour chaque élément $\verb|i|$ de $\verb|ordre|$, ajouter $\verb|i|$ à la première table de $\verb|tables|$ possible (la première table ne contenant aucune de ses incompatibilités) si elle existe ou en créer une nouvelle sinon.

{% exercice %}

1. Pourquoi l'algorithme précédent est-il glouton ?
2. Démontrez qu'il donne bien une réponse au problème quel que soit $\verb|ordre|$. Quel ordre utiliseriez-vous par défaut pour résoudre le problème ? Et pourquoi ?
3. Cet algorithme est efficace mais on va voir qu'il dépend fortement de la liste $\verb|ordre|$. Montrez que l'algorithme peut rendre un nombre de tables strictement plus grand que 2 alors qu'il existe une solution à deux tables.
   {% endexercice %}
   {% details "corrigé" %}
4. C'est un algorithme glouton puisqu'il affecte itérativement chaque convive à une table qui ne changera plus.
5. On affecte une personne à une table que lorsque c'est possible, on obtient donc bien finalement une solution au problème. On peut choisir les convives par nombre d'incompatibilité décroissante car à chaque choix on placera le convive à une table qui dépend du nombre d'incompatibilité déjà placées il faut donc placer les personnes à faible nombre d'incompatibilité à la fin.
6. On suppose que l'on utilise l'ordre $a$, $b$, $c$ puis $d$ avec les incompatibilités : - $a$ et $b$ - $b$ et $d$ - $c$ et $d$
   {% enddetails %}

En utilisant la structure de l'algorithme glouton :
{% exercice %}

- démontrez que le nombre minimum de tables ne peut excéder le nombre maximum d'incompatibilités pour une personne plus 1;
- donnez un cas où cette borne est atteinte;
- donnez un cas où on peut faire strictement mieux que cette borne.
  {% endexercice %}
  {% details "corrigé" %}

- A chaque étape le convive sera placé à la première table possible. Le cas le pire arrivant si toutes ses incompatibilités ont déjà été placées à des tables différentes.
- La borne est atteinte si tout le monde déteste tout le monde.
- Si tout le monde aime tout le monde il suffit d'une table

{% enddetails %}

Pour ne pas conclure, même si cet algorithme n'est ni optimal ni à performance garantie, il est très difficile de trouver (même s'il existe) u ordre où il ne va pas trouver de bonne solution.
 (Il est [NP-complet de trouver le plus mauvais ordonnancement de cet algorithme](https://fr.wikipedia.org/wiki/Coloration_gloutonne#Ordre_mauvais)).

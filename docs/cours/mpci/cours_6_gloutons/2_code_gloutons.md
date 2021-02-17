---
layout: page
title:  "Algorithmes gloutons : code"
category: cours
tags: informatique cours 
authors: "François Brucker"
---


## But

Implémenter divers algorithmes gloutons et voir qu'ils fonctionnent. N'oubliez pas qu'un programme python c'est **TOUJOURS** :

* du code,
* des tests
* un programme principal

## Rendu de pièces

### exemple

Donnez le résultat de l'algorithme glouton du cours lorsque l'on doit :

* rendre `R = 28` avec le système de pièces valant `[10, 5, 2, 1]`
* rendre `R = 6` avec le système de pièces `[1, 3, 4]`

### algorithme

Créez un algorithme python qui effectue le rendu de pièces. Il devra, entre autres test faire passer les tests suivants :

``` python
def test_rendu_piece_trie():
  assert rendu_pieces(8, [5, 2, 1]) == [1, 1, 1]

def test_rendu_piece_non_trie():
  assert rendu_pieces(8, [1, 5, 2]) == [1, 1, 1]
```

### le main : rendre des pièces

Créer un programme principal qui demande à l'utilisateur la valeur sur la quelle rendre la monnaie et rend (dans un français impeccable), le nombre de billets et de pièces rendre (il ne donne que les valeurs strictement positives à rendre). Vous utiliserez le système de pièce européen : avec des billets de 200, 100, 50, 20 et 10, et des pièces de .1, .2, .5.

## films

### nombre de films à voir

Reprenez le code du cours et trouvez des tests permettant de montrer que l'algorithme fonctionne.

### génération de films

On va créer un générateur de séances de cinéma.

#### les intervalles

Créez une fonction qui génère tous les intervalles non singletons formés des $n$ premiers entiers. Les intervalles doivent être donné dans l'ordre tel que : $[x, y] < [z, t]$ si ($x < y$) ou si ($x=y$ et $y < t$)

```python
def test_intervalle_1():
  assert intervalles(1) = []

def test_intervalle_3():
  assert intervalles(2) = [[1, 2], [1, 3], [2, 3]]
```

#### des intervalles

Utilisez [`numpy.random.choice`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html) pour créer une fonction `des_intervalles` qui rend $k$ intervalles différents de $[1, n]$.

Ces intervalles seront les films que l'on voudra voir.

### le main : voir des films

Créez un programme principal qui demande un nombre de films $k$ et :

* rend une liste de $k$ intervalles de films dans $[1, 24]$
* donne une liste maximale de films à voir parmi la liste de $k$ films.

### nombre de salles de cinéma

Faites la même chose que précédemment mais pour le problème du nombre minimum de salles à créer pour voir tous les films

## ordonnancement

### génération de produits

Créez un algorithme permettant de créer $k$ produits différents ayant chacun :

* une date de péremption entre 1 et $d$,
* un prix entre 1 et $p$.

Votre algorithme `créer_prix` devra avoir comme paramètre :

* un nombre $k$ : le nombre de produits à rendre
* une date de péremption $d$ (tous les produits auront une date de péremption entre 1 et $d$)
* une prix $p$ (tous les produits auront un prix entre 1 et $p$)

Et devra rendre une liste de $k$ couples $(d_i, p_i)$ avec $1 \leq d_i \leq d$ et $1 \leq p_i \leq p$.

### ensemble compatible

créer une fonction `est_compatible(liste_produits)` qui répond `True` si la liste de produits passée en paramètre et compatible, et `False` sinon.

Un ensemble est compatible si on peut le construire strictement avant sa date de péremption. Si l'on a qu'un seul ouvrier pour construire nos objets, comme on commence à $t=0$ et que chaque objet met 1 unité de temps à être construite : on peut donc $t$ objets avant le temps $t$. 

#### liste_produit croissant

On commence par supposer que notre liste de produit est rangée par date de péremption croissante.

Créer une première une première version de `est_compatible(liste_produits)` avec cette supposition. Elle devra par exemple passer les tests suivant :

```python
def test_est_compatible_oui():
  assert est_compatible([[1, 10]])
def test_est_compatible_non():
  assert est_compatible([[1, 10], [1, 2]])

def test_est_compatible_plusieurs_valeurs_oui():
  assert est_compatible([[1, 10], [2, 12], [4, 2], [5, 2], [5, 2]])
def test_est_compatible_plusieurs_valeurs_non():
  assert est_compatible([[1, 10], [2, 12], [3, 3], [4, 2], [5, 2], [5, 2]])

```

Remarquez qu'une `liste_produit` rangée par date de péremption croissante n'est compatible que si l'on peut créer le produit `liste_produit[i]` au temps $i$. Déduisez-en une implémentation facile de `est_compatible(liste_produits)` en considérant que `liste_produit` est trié par date de péremption croissante.

#### produit rangés aléatoirement

Ajoutez des tests où la liste des produits n'est pas rangés aléatoirement. Par exemple le test suivant qui doit rater :

``` python
def test_est_compatible_non_ordonnée_oui():
  assert est_compatible([[5, 10], [1, 12]])
```

Modifiez votre fonction pour que le test fonctionne.

### algorithme : ordonnancement

Codez l'algorithme de compatibilité maximum. Trouvez des tests pertinent permettant de vérifier qu'il fonctionne

### le main : ordonnancement

Générez aléatoirement des produits et trouvez les ensemble compatibles maximaux.

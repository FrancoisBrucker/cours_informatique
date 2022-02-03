---
layout: page
title:  "DS"
category: cours
tags: informatique cours 
authors: "François Brucker"
---

## Introduction

L'examen était les 7 premières questions (environ 1/3) d'un [examen de concours 2019](./informatique_B_2019.pdf)

La moyenne générale était de 12,15, avec un écart type de 3, 72.

La note moyenne (en pourcentage) pour chaque question était :

|question | 1    | 2   | 3   | 4   | 5   | 6| 7   |
----------|------|-----|-----|-----|-----|--|-----|
|%        |79,81 |70,38|61,54|62,69|47,69|50|22,31|

J'ai mis un corrigé de tout l'examen pour que vous puissiez vous entraîner. Ce sujet est parfait car il n'est pas trop compliqué au début (mais du coup il faut aller vite) et permet de s'entraîner avec les listes. Toutes les subtilités des listes et de leurs indices y sont en effet présentes. Et en plus, et c'est certainement le plus important, il est marrant et agréable à faire (enfin si on aime un peu l'algorithmie bien sûr (mais comment pourrait-on ne pas ?)).

## Question 1

```python
def creerGrille(largeur, hauteur):
    grille = []
    for l in range(largeur):
        colonne = []
        for h in range(hauteur):
            colonne.append(VIDE)

        grille.append(colonne)

    return grille
```

On crée élément par élément un liste de liste. La première liste contient les colonnes, chaque colonne étant également une liste. Il y a deux `append` différents, le premier qui remplit les colonnes le second qui ajoute les colonne à la grille. La complexité est en $\mathcal{O}(largeur * longueur)$.

**Erreurs fréquentes :**

* la grille est une liste de colonne, chaque colonne étant une liste d'éléments valant tous `VIDE` : il faut donc commencer par une boucle for sur le nombre de colonnes, c'est à dire la `largeur`
* `VIDE`est une **donnée** du problème. Le sujer précise que c'est une constante que l'on peut utiliser. Ce n'est ni `"VIDE"` ni `[]` ni même rien du tout, c'est la constante nommée `VIDE`.
* ne mettez pas plusieurs fois la même liste dans grille. un truc du genre : `l= [1, 2]` et `grille = [l, l]` ne fonctionnera pas car c'est la **même** liste qui sera là, pas deux colonnes différentes (pour vous en rendre compte écrivant `grille[0][1] = '?'` puis affichez la grille. Les deux colonnes sont modifiées car c'st la **même** colonne)
* attention à la ligne `colonne = []` est est **dans** la boucle et pas au dessus. Il faut qu'elle soit recréée à chaque fois.

## Question 2

```python

def afficherGrille(grille):

    nouvelleLigne()
    for h in range(hauteur - 1, -1, -1):
        for l in range(largeur):
            if grille[l][h] == VIDE:
                afficheBlanc()
            else:
                afficheCouleur(grille[l][h])
        nouvelleLigne()
    
```

Attention à la lecture d'un élément. On procède en 2 temps :

1. On commence par lire de droite à gauche, en enlevant à chaque fois une opération (ici les `[]`) :
   * en notant `o1=grille[l]`, notre expression cherche  l'élément de `o1` qui se trouve à la position `h`.
   * On cherche ensuite `o1`. C'est l'élément est l'élément à la position `l` de grille.
2. puis on résout de gauche à droite :
   * l'élément à la position `l` de grille est la colonne d'indice `l`.
   * `o1` étant la colonne d'indice `l` de grille, chercher son élément de position `h` est donc l'élément de hauteur `h`

Notez bien que comme ces opérations sont des positionnement dans des listes, elles sont de complexité $\mathcal{O}(1)$

**Erreurs fréquentes :**

* ne modifiez pas la grille ! `grille.reverse()` par exemple retourne la grille et donc votre grille n'a plus les caractéristiques demandée dans l'exercice. A la limite il faudra refaire un `grille.reverse()` avant de sortir de la fonction pour tout remettre en place. Mais comme on risque de l'oublier on essaie de programmer sans ça
* attention à la place de `nouvelle_ligne`
* hauteur doit décroître et largeur croître
* l'ordre des boucle imbriqué est important

## Question 3

```python

def grilleLibre(grille, k):

1:    for l in range(largeur):
2:        ok = True
3:        for h in range(hauteur - 1, hauteur - 1 - k, -1):
4:            if grille[l][h] != VIDE:
5:                ok = False
6:        if ok:
7:            return True
8:    return False

```

Les lignes 1 et 3 sont des boucles. Pour les autres lignes, on a une complexité de :

* la ligne 2 : c'est une affectation, donc en $\mathcal{O}(1)$ opérations
* la ligne 4 :
  * un positionnement dans une liste de liste, donc en $\mathcal{O}(1)$ opérations ($\mathcal{O}(1)$ opérations pour chaque positionnement)
  * un test en $\mathcal{O}(1)$ opérations
* la ligne 5 : c'est une affectation en $\mathcal{O}(1)$ opérations
* la ligne 6 : c'est un test, donc $\mathcal{O}(1)$ opérations
* la ligne 7 : c'est le retour de fonction : $\mathcal{O}(1)$ opérations
* la ligne 8 : c'est le retour de fonction : $\mathcal{O}(1)$ opérations

Dans le pire des cas, le retour de fonction est fait en ligne 8. On aura parcouru les boucles imbriquées des lignes 1 et 3 en entier. La complexité de l'algorithme est alors en :

$$ \mathcal{O}(l) *(\mathcal{O}(1)+\mathcal{O}(k)* \mathcal{O}(1) + \mathcal{O}(1)) + \mathcal{O}(1)$$

On a donc une complexité de : $\mathcal{O}(l * k)$

**Erreurs fréquentes :**

* on cherche si une colonne est disponible. Il ne faut pas s'arrêter si une colonne ne fonctionne pas. Le `return False` n'est présent que si l'on a regardé toutes les colonne et aucune ne marche. En revanche, on peut sortir avec un `return True` dès la première colonne qui fonctionne
* la complexité est $\mathcal{O}(largeur\times k)$ et non $\mathcal{O}(largeur \times hauteur)$ : $k$ est une entrée de notre problème, on doit donc l'utiliser si on peut. La première réponse n'est pas fausse (puisque $hauteur > k$) mais elle est moins précise

## Question 4

```python

def descente(grille, x, y, k):
    
    if (y <= 0) or (grille[x][y-1] != VIDE):
        return
    
    for position in range(k):
        grille[x][y + position - 1] = grille[x][y + position]

    grille[x][y + k - 1] = VIDE
```

fonctionnement de la fonction :

* on vérifie que l'on peut déplacer le barreau. Si on ne peut pas le faire, on sort de la fonction
* On fait descendre le barreau en commençant par la dernière ligne pour ne pas écraser le barreau et perdre des données
* ne pas oublier que la première case où était le barreau devient vide

**Erreurs fréquentes :**

* n'oubliez pas les sentinelles qui sont des tests qui vérifient que l'on peut bien accéder aux cases du tableau comme vérifier que $y > 0$ avant de chercher l'élément d'indice $y-1$ dans un tableau
* on ne descend que **d'une seule case**
* attention au dernier élément qu'il faut placer à vide une fois le barreau descendu

## Question 5

```python

def deplacerBarreau(grille, x, y, k, direction):
    
    if (x + direction < 0) or (x + direction >= len(grille)):
        return
    
    for position in range(k):
        if (grille[x + direction][y + k] != VIDE):
            return

    for position in range(k):
        grille[x + direction][y + k] = grille[x][y + k]
        grille[x][y + k] = VIDE

```

fonctionnement de la fonction :

* on vérifie que l'on peut déplacer le barreau. Si on ne peut pas le faire, on sort de la fonction :
  * on vérifie que l'on est pas au bord
  * on vérifie qu'il n'y à personne là où l'on veut déplacer le barreau
* on déplace le barreau et on oublie pas d'effacer sa position antérieure

**Erreurs fréquentes :**

* attention, l'usage des `break` et `continue`n'est pas triviale (voir le [tutoriel python](https://docs.python.org/fr/3.8/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)). Vaut mieux s'en passer plutôt que de mal les utiliser
* attention aux sentinelle pour vérifier que l'on peux décaler le barreau
* comme on demande de ne pas modifier le barreau si on ne peut pas le déplacer, on sépare les 2 actions : 1- on vérifie que c'est bon 2- on modifie grille. C'est plus simple que remettre les valeurs d'origine si on se rend compte au milieu de l'algorithme que ça ne marche pas
* on peut factoriser les 2 directions en une seule boucle

## Question 6

```python

def permuterBarreau(grille, x, y, k):
    
    premier_element = grille[x][y + k - 1]
    for position in range(k - 2, -1, -1):
        grille[x][y + position + 1] = grille[x][y + position]
            
    grille[x][y] = premier_element

```

On est obligé de sauver le premier élément (l'élément le plus haut) pour le placer à la fin au dernier élément du barreau (à la position y).  Puis on parcourt le barreau du deuxième

## Question 7

```python

def descenteRapide(grille, x, y, k):
    descente = y
    while (descente > 0) and (grille[x][descente - 1] == VIDE)
        descente -= 1
    
    for position in range(k):
        grille[x][descente + position] = grille[x][y + position]
        grille[x][y + position] = VIDE
```

On commence par trouver la hauteur maximale de descente du barreau, puis on téléporte le barreau à cette place. Comme on ne déplace le barreau qu'une seule fois la complexité demandée est bien atteinte. Comme le barreau est *téléporté* de bas en haut il n'est pas effacé si l'on descend de moins de *k* lignes.

## Question 8

Position initiale :

``` text
...B..  
...R..  
...JN.  
...RN.  
....R.  
.BB.NJ
.NR.VN
NRR.RV
NBJBVV
VNJBVJ
```

Descente :

``` text
......  
......  
....N.  
....N.  
...BR.  
.BBRNJ
.NRJVN
NRRRRV
NBJBVV
VNJBVJ
```

on a :

* une ligne de quatre `R` horizontaux : 2pt
* rien en vertical
* quatre `R` en diagonal 2pt

On supprime les résultats :

``` text
......  
......  
....N.  
....N.  
...B..  
.BB.NJ
.N.JVN
N....V
NBJBVV
VNJBVJ
```

On tasse :

``` text
......  
......  
......  
......  
....N.  
....NJ
.B.BNN
NNBJVV
NBJBVV
VNJBVJ
```

on a :

* trois `N` verticaux et 3 `V` verticaux, tous deux à 1pt
* deux diagonales de 3 `B` (les `B` qui forment un X), tous deux à 1pt

On supprime les positifs :

``` text
......  
......  
......  
......  
......  
.....J
.....N
NN.J.V
N.JI.V
VNJB.J
```

Puis on tasse :

``` text
......  
......  
......  
......  
......  
.....J
.....N
N..J.V
NNJI.V
VNJB.J
```

Plus aucun positifs, d'où un total de 8pts.

## Question 9

```python

def detecteAlignement(rangee):
    
A:    marking = []
      score = 0
B:    couleur = rangee[0]
      nombre_couleur_identique = 1
C:    for position in range(1, len(rangee)):
D:        if couleur == rangee[position]:
              nombre_couleur_identique += 1
E:        else:
F:            if (couleur != VIDE) and (nombre_couleur_identique >= 3):
                  score += nombre_couleur_identique - 2
              for i in range(nombre_couleur_identique):
                  if (couleur != VIDE) and (nombre_couleur_identique >= 3):
                      marking.append(True)
                  else:
                      marking.append(False)
G:            couleur = rangee[position]
              nombre_couleur_identique = 1

      if (couleur != VIDE) and (nombre_couleur_identique >= 3):
          score += nombre_couleur_identique - 2

H:    for i in range(nombre_couleur_identique):
          if (couleur != VIDE) and (nombre_couleur_identique >= 3):
              marking.append(True)
          else:
              marking.append(False)
      return (marking, score)

```

On parcourt chaque position de la liste jusqu'à trouver une couleur différente de la couleur précédente. A ce moment là on ajoute à la liste `marking` autant de fois que la couleur à été trouvée `True` si  la couleur était non vide et qu'il y en avait >= 3, `False` sinon. On met à jour les scores si nécessaire. Plus précisément :

* marque `A` : on crée un tableau `marking` initialement vide, on va le remplir petit à petit
* marque `B` : Le premier élément de `rangee` commence une nouvelle couleur
* marque `C` : le parcourt des éléments de rangée à partir du 2ème élément.
* marque `D` : si la couleur de la case actuelle est la même que celle stockée, on ajoute 1 au compteur. Il y a `nombre_couleur_identique` éléments consécutifs de cette couleur jusqu'à `position`.
* marque `E` : on change de couleur. Il faut ajouter ce que l'on sait de l'ancienne couleur dans `marking` (marque `F`) et changer la couleur actuelle (marque `G`)
* marque `F` : On change le score si nécessaire puis on remplit le tableau parking avec les éléments de la couleur précédente. Si cette couleur était non vide et qu'il y en avait plus de 3, on ajoute `True` sinon on ajoute `False`.
* marque `G` : il y a une nouvelle couleur.
* marque `H` : à la fin de l'itération, on fini la dernière couleur.

On peut noter que la complexité de cette fonction est en $\mathcal{O}(\mbox{len(rangee)})$.

## Question 10

```python

def scoreRangée(grille, g, i, j, dx, dy):
A:  rangee = []
    while (0 <= i < largeur) and (0 <= j < hauteur):
        rangee.append(rangee[i][j])        
        i += dx
        j += dy
        
B:  marking, score = detecteAlignement(rangee)
   
C:  for position in range(len(rangee)):
       if marking[position] == true:
           g[i + position * dx][j + position * dy] = VIDE

   return score
```

La fonction est séparée en plusieurs bouts :

* A: on crée la rangée en décalant de `dx` et `dy` les positions tant que l'on reste à l'intérieur de la grille `(i < largeur) and (j < hauteur)`
* B: on crée les alignements.
* C: on met à jour la grille g en supprimant les cases où `rangee` est `True`

## Question 11

```python

def effaceAlignement(grille):

A:  g = []
    for colonne in grille:
        g.append(list(colonne))
    
    score = 0
    
B:  for i in range(largeur):
        score += scoreRangée(grille, g, i, 0, 0, +1)
        
C:  for j in range(hauteur):
        score += scoreRangée(grille, g, 0, j, +1, 0)

D:  for i in range(largeur):        
        score += scoreRangée(grille, g, i, 0, +1, +1)        
    for j in range(1, hauteur):
        score += scoreRangée(grille, g, 0, j, +1, +1)        

E:  for i in range(largeur):        
        score += scoreRangée(grille, g, i, hauteur - 1, +1, -1)        
    for j in range(hauteur - 1):
        score += scoreRangée(grille, g, 0, j, +1, -1)        
    
    return (g, score)
```

* A: on crée la copie de grille. Attention à la copie de liste !
* B: on regarde les colonnes
* C: on regarde les lignes
* D: on regarde les diagonales qui *"montent"*. Attention, pour ne pas compter 2 fois les même diagonales, la deuxième itération commence à 1
* E: on regarde les diagonales qui *"descendent"*. Attention, pour ne pas compter 2 fois les même diagonales, la deuxième itération fini à hauteur - 2.

## Question 12

```python

def tassementGrille(grille):
    for i in range(largeur):
        libre = None
        for j in range(hauteur):
            if (libre == None) and grille[i][j] == VIDE:
                libre = j
            elif (libre != None)  and grille[i][j] != VIDE:
                grille[i][libre] = grille[i][j]
                grille[i][j] = None
                libre += 1
```

Tasser un élément revient à le mettre au premier élément vide de la colonne que l'on considère. Si l'on parcourt une colonne de bas en haut, cet élément vide sera vu avant l' élément à tasser.
De là on parcourt chaque colonne de haut en bas et garder un pointeur vers la première place libre (lorsque `(libre == None) and grille[i][j] == VIDE`). A partir de cet indice `j` on a que `libre != None`. Un élément à tasser vérifiera la condition `(libre != None)  and grille[i][j] != VIDE`.

## Question 13

```python

def calculScore(grille):
    
    score_total = 0
    g, score = effacementGrille(grille)
    while score > 0:
        score_total += score
        tassementGrille(g)
        for i in range(largeur):
            for j in range(hauteur):
                grille[i][j] = g[i][j]
        g, score = effacementGrille(grille)
    
    return score_total
```

Tant que le score est strictement positif on met à jour la matrice (comme la fonction ne rend pas de grille, il faut modifier la grille initiale) et on calcul le nouveau score que l'on ajoute au score total.

## Question 14

```python

def tailleRegionUnicolore(grille, x, y):

    couleur = grille[x][y]
    if couleur == VIDE:
        return 0
    grille[x][y] = VIDE
    
    nombre = 1
    if (x > 0) and (grille[x - 1][y] == couleur):
        nombre += tailleRegionUnicolore(grille, x - 1, y)
    if (x < largeur - 1) and (grille[x + 1][y] == couleur):
        nombre += tailleRegionUnicolore(grille, x + 1, y)
    if (y > 0) and (grille[x][y - 1] == couleur):
        nombre += tailleRegionUnicolore(grille, x, y - 1)
    if (y < hauteur - 1) and (grille[x][y + 1] == couleur):
        nombre += tailleRegionUnicolore(grille, x, y + 1)
    
    return nombre

```

L'algorithme fonctionne ainsi. On commence par vérifier que la case n'est pas vide. Si ce n'est pas le cas, on vide la case pour s'assurer de ne pas repasser plusieurs fois par cette case lors de la récursion.

Puis, si c'est possible (on reste dans la grille et la case adjacente est de la même couleur), on relance l'algorithme sur les 4 cases à côté. Les résultats des algorithmes appelés sont ajoutés au score courant.

## Question 15

La stratégie proposée ne fonctionne pas. En effet, la méthode `exploreVertical` ne regarde que la colonne courante et la méthode `exploreHorizontal` ne fait appel qu'à `exploreVertical` puis se décale dans même direction. De là une région qui fait un *escargot* ne sera pas trouvée puisqu'il faudrait aller horizontalement dans les 2 directions :

Exemple :

``` text
XRR
RXR
RRR
```

En partant de (0, 1) on ne retrouvera jamais (1, 2)

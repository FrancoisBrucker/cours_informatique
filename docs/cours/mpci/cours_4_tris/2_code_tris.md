---
layout: page
title:  "Code Méthodes de tris"
category: cours
tags: informatique cours 
---

## Introduction

On va s'amuser avec les tris ! On va implémenter des méthodes de tris, mesurer leurs complexités et visualiser leurs méthodes de tri.

Créez un nouveau projet vscode et commencez tout de suite par créer les fichiers :

* _"main.py"_,
* _"tests_tris.py"_
* _"tris.py"_

## tris simple

### algorithmes

Dans _"tris.py"_ et _"tests_tris.py"_ implémentez les tris par sélection et par insertion du cours.

Lorsque l'on teste des méthodes de tris, on a coutume de tester :

* sur une liste vide,
* sur une liste aléatoire,
* sur une liste triées par ordre croissant,
* sur une liste triées par ordre décroissant.

Assurez vous que toutes vos méthodes de tris soient testées par au moins ces 4 types de tests.

### visualisation

Reprenez l'exemple du cours qui représente graphiquement les tris. Adaptez le code pour qu'il puisse être intégrer à votre programme principal (*"main.py"*).

Pour rendre votre programme interactif, vous pourrez demander à l'utilisateur quel tri il veut voir représenté (sélection ou insertion) et la taille de la liste à utiliser.

### complexité

Pour vérifier expérimentalement nos calculs de complexité, on va procéder comme pour la fonction exponentiation : on va mesurer le temps avant et après l'exécution de notre fonction. Ce temps est proportionnel au nombre d'opérations effectué par la fonction pour les entrées données.

On voit par là que l'on ne peut avec cette méthode que calculer la complexité en moyenne d'un algorithme : on va calculer pour $p$ entrées prises au hasard le temps moyen pris par l'algorithme

On va ici considérer que $p = 10$ et la mesure pour chaque algorithme sera la suivante :

* pour un algorithme donné
  * on crée une liste `temps_pris` initialement vide
  * pour une taille $n$ allant de 0 à 1000 (voir plus si c'est pas assez ou moins si ça rame)
    * on utilise la liste `L` des $n$ premiers entiers strictement positif
    * on répète $p$ fois :
      * on mélange la liste `L` (on pourra utiliser la fonction [shuffle du module random](https://docs.python.org/3/library/random.html#random.shuffle))
      * on mesure le temps pris pour trier cette liste
    * on calcule la moyenne du temps pris et on l'ajoute à la fin de la liste `temps_pris`
  * on affiche le résultat avec matplotlib (on pourra également représenter la courbe de la complexité maximale théorique et moyenne si elle est différente)

Faite la procédure ci-dessus pour les algorithme par sélection et insertion. Vous pourrez mettre votre code dans deux nouveaux fichiers : *"complexite_sélection.py"* et *"complexite_insertion.py"*.

## tri rapide

Implémentez le tri rapide (avec ses tests bien sur !) et, avoir l'avoir regardé trier des listes (en l'ajoutant à votre programme principal de visualisation) vérifiez que les complexités maximales, minimale et en moyenne correspondent à la théorie (vous pourrez créer un fichier *"complexité_rapide.py"* pour y mettre votre code)

## tri de python

Vérifiez expérimentalement que la complexité en moyenne du tri de python (méthode [sort des listes](https://docs.python.org/3/howto/sorting.html)) est bien en $\mathcal{O}(n\ln_2(n))$ où $n$ est la taille de la liste à trier.

L'algorithme utiliser est de plus de complexité maximale $\mathcal{O}(n\ln_2(n))$, mais on ne peut pas le vérifier expérimentalement.

## tri fusion

Le [tri fusion](https://fr.wikipedia.org/wiki/Tri_fusion) est un tri de complexité $\mathcal{O}(n\ln_2(n))$ opérations où $n$ est la taille de la liste en entrée.

Une proposition de code est ci-après :

```python
def fusion(tab):
    if len(tab) < 2:
        return tab
    else:
        milieu = len(tab) // 2
    return fusion_colle(fusion(tab[:milieu]), fusion(tab[milieu:]))


def fusion_colle(tab1, tab2):
    i1 = i2 = 0
    tab_colle = []
    while i1 < len(tab1) and i2 < len(tab2):
        if tab1[i1] < tab2[i2]:
            tab_colle.append(tab1[i1])
            i1 += 1
        else:
            tab_colle.append(tab2[i2])
            i2 += 1
    if i1 == len(tab1):
        tab_colle.extend(tab2[i2:])
    else:
        tab_colle.extend(tab1[i1:])
    return tab_colle
```

L'algorithme fonctionne ainsi :

1. on coupe la liste à trier en 2
2. on trie chacune des sous-listes à part
3. on recolle les deux listes triées en une unique liste (c'est `fusion_colle`)

Comme on peut utiliser n'importe quel algorithme pour trier les 2 sous-listes, autant s'utiliser soit-même ! L'algorithme fusion utilise donc l'algorithme fusion pour trier les sous-listes de l'algorithme fusion.

La complexité de l'algorithme est alors :

$$C(n) = 2 * C(n/2) + D(n)$$

Où :
* $C(n)$ est la complexité de l'algorithme fusion pour une liste à $n$ éléments (algorithme `fusion`)
* $D(n)$ est la complexité de fusionner deux listes triées en une unique liste triées (algorithme `fusion_colle`). 

Comme l'algorithme `fusion_colle` est en $\mathcal{O}(n)$, l'équation de récurrence de la complexité est :

$$C(n) = 2 * C(n/2) + \mathcal{O}(n)$$

Pour connaître la valeur de la complexité on utilise le [master theorem](https://fr.wikipedia.org/wiki/Master_theorem) qui est **LE** théorème des complexités pour les algorithmes récursifs. Sa preuve dépasse (de loin) le cadre de ce cours, mais son énoncé sous la  [notation de Landau](https://fr.wikipedia.org/wiki/Master_theorem#%C3%89nonc%C3%A9_avec_la_notation_de_Landau), nous permet de déterminer aisément la complexité de nombreux algorithmes récursifs, dont le notre : $\mathcal{O}(n\ln_2(n))$, puisque $1 = \ln_2(2)$.

Cet algorithme a la particularité d'avoir toujours le même nombre d'opérations quelque soit la liste en entrée. Il est donc aisé de mesurer sa complexité. Faites le et vérifier que c'est bien $\mathcal{O}(n\ln_2(n))$. 

## mélanger des listes ?

On s'est appuyé sur la fonction [shuffle du module random](https://docs.python.org/3/library/random.html#random.shuffle) pour mélanger des listes.

Mais sommes-nous bien sur que le mélange est bien équiprobable ? Sinon nos mesures de complexité en moyenne seraient tous faux...

Rassurez vous c'est le cas. Elle utilise la méthode de mélange de [Fisher-Yates](https://fr.wikipedia.org/wiki/M%C3%A9lange_de_Fisher-Yates), qui est un algorithme linéaire permettant d'obtenir toutes les permutations possibles de façon équiprobable.

Ce qui est marrant c'est que cet algorithme est *"l'inverse"* d'un tri par sélection. 

Implémentez cet algorithme et vérifiez que pour la liste des 4 premiers entiers vous obtenez bien (sur un grand nombre d'essais) à peut prêt le même nombre des 24 permutations possibles.

Si vous voulez en savoir un peu plus sur cet algorithme et de comment générer un nombre aléatoire en python : <https://www.stashofcode.fr/tri-aleatoire-des-elements-dun-tableau/>
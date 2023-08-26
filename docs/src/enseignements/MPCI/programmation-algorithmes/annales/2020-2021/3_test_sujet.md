---
layout: layout/post.njk

title:  "sujet Test 3 : preuve"
authors:
    - François Brucker
---

## 1. Suppression de valeur

Donnez la complexité et prouvez  que l'algorithme-1 suivant rend  une liste `L2`{.language-}, restriction de `L`{.language-} aux valeurs différentes de val.

```text
Nom : Algorithme-1
Entrées : 
    val : une valeur
    L : une liste de n valeurs
Programme :
    création d’une liste L2 vide
    pour chaque élément x de L :
        si x ≠ val : 
            ajoute x à la fin de L2
    Retour L2
```

## 2. Suppression de doublon

Donnez la complexité et prouvez que l'algorithme-2 suivant retourne une liste `L2`{.language-} ne contenant qu’une seule occurrence de chaque valeur de `L`{.language-}, en conservant le même ordre.

```text
Nom : Algorithme-2
Entrées : 
    L : une liste de n valeurs
Programme :
    création d’une liste L2 vide
    tant que L est non vide:
        x = L[0]
        ajoute x à la fin de L2
        L = algorithme-1(L, x)    
    Retour L2
```
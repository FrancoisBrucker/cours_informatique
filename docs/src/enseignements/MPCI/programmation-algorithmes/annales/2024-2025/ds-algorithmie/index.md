---
layout: layout/post.njk
title: "DS Algorithmie"
---

{% note "**Sujet**" %}

[X/ENS informatique B 2024](./Banque_X-ÉNS_2024_MP-PC-PSI_Informatique_B_e.pdf){.fichier}

Durée du contrôle : 2h.

{% endnote %}

## Barème

Le sujet était l'épreuve commune d'informatique pour X/ENS en 2024. C'est l'informatique commune à tous les concours (ce n'est donc **pas** l'épreuve uniquement réservée aux informaticiens), mais c'est tout de même un sujet long à faire en 2 heures et d'un niveau assez relevé.

L'idée est de faire au mieux, quite à choisir ses questions ou à ajouter des hypothèses si on en a besoin.

J'ai noté uniquement les questions 1 à 9 pour un total de 20 points. Une seule personne a abordé la question 10. Ce qui donne une note sur 25 répartie comme suit :

- 2pt pour les questions 1 à 3
- 2pt pour la question 4.1
- 1pt pour la question 4.2
- 2pt pour la question 5
- 3pt pour la question 6
- 2pt pour les questions 7 à 9
- 1pt pour les questions 10 à 14

{% note "**Objectif du test**" %}

En 2 heures :

- **un élève *normal*** doit parvenir à faire parfaitement les question 1 à 4.1, pour un total de 8 points. Il doit pouvoir enfin glaner quelques points dans les questions faciles suivantes (en particulier les questions 5 et 8) pour arriver à 12.
- **un bon élève** doit parvenir à réussir la question 6 qui était la plus dure du DS
- **un très bon élève** à en plus parfaitement fait la question 9 qui était la seconde question la plus dure.

{% endnote %}

Pour vous comparer, vous pouvez consulter : [rapport de l'épreuve 2024](https://diplome.di.ens.fr/informatique-ens/annales/2024_InfoB-rapport.pdf). Vous voyez qu'en moyenne les élèves ont répondus à plus de questions que vous (vous 9 questions et eux 11). Il faut donc que vous gagniez en rapidité, car vous avez été noté sur 25 et non sur 20.

### Ventilation des notes

|note/20  |< 10  | [10, 11] | ]11, 13]      | ]13, 15] | ]15, 18[  | = 18  
|---------|----|------------|------------|-------------|-----------|-------
|nombre   | 6  |  16        |  10        |  6          |  5        | 1

- moyenne : 11.59/20
- écart-type : 2.87/20
- médiane : 11.13/20

Je suis globalement satisfait, vous avez quasi tous la moyenne. Vous êtes encore beaucoup entre 10 et 11, si vous continuez sur cette lancée et gardez votre travail régulier vous ne pourrez que progresser et avoir une meilleure note à l'ET.

### Erreurs fréquentes

- 2 : la complexité est celle la complexité de `case_noires`{.language-}
- 4.1 : on suppose que les entrées sont correctes, donc sol est une liste de liste d'entiers valant 0 ou 1.
- 6 : ne passez pas trop de temps à essayer de faire une question visiblement très dure.
- 7 : question facile mais presque personne ne l'a tentée.

## Corrigé

Nous allons écrire toutes les fonctions demandées en python.

### Partie I

#### Question 1

On somme chaque élément de la liste de listes d'entiers passé en paramètre.

```python
def cases_noires(cle_l):
    total = 0
    for ligne in cle_l:
        for nombre in ligne:
            total += nombre
    return total
```

La complexité est en $\mathcal{O}(\text{nc} \cdot \text{nl})$ puisque toute les lignes sont en $\mathcal{O}(1)$ et on parcourt tous les éléments d'une matrice à $\text{nl}$ lignes et $\text{nc}$ colonnes.

{% info %}
Si on voulait faire le malin (mais ce n'est jamais conseillé), on aurait pu écrire cette fonction :

```python
def cases_noires(cle_l):
    return sum(sum(ligne) for ligne in cle_l)
```

Qui est de même complexité car la complexité de la fonction `sum([entier]) -> entier`{.language-} de python est de l'ordre de la taille de la liste passée en paramètre.

{% endinfo %}

#### Question 2

La plus simple des fonction est :

```python
def compatibles(cle_l, cle_c):
    return cases_noires(cle_l) == cases_noires(cle_c)
```

Qui est de complexité égale à la complexité de `case_noires([[entier]]) -> entier`{.language-} de la question précédente.

{% info %}
Cette version est également possible, mais est très lourde et inélégante puisque le retour de `==` est déjà un booléen :

```python
def compatibles(cle_l, cle_c):
    if cases_noires(cle_l) == cases_noires(cle_c):
        return True
    else:
        return False
```

{% endinfo %}

#### Question 3

On compte toute les cases noires et on ajoute les cases blanches nécessaires :

```python
def taille_minimale(ligne):
    return sum(ligne) + len(ligne) - 1
```

Notez que l'hypothèse selon laquelle le tableau est nom vide est importante, sinon le code de la fonction précédente est faux.

La complexité de la fonction est de l'ordre de celle de la fonction `sum([entier]) -> entier`{.language-}, c'est à dire de la taille de la liste passée en paramètre.

#### Question 4

Pour arriver ligne 13 il faut que :

1. le `if` de la ligne 8 soit vrai
2. le `if` de la ligne 9 soit faux

- l'exécution de `verif_ligne([[1, 0]], [[2]], 0)`{.language-} va stopper ligne 13 par ce que `taille != cle_l[0][0]`{.language-}
- `verif_ligne([[1, 0, 1]], [[2]], 0)`{.language-} va stopper ligne 13 par ce que `i_block == len(cle_l[0])`{.language-}

L'algorithme vérifie que la succession de blocs de la solution est compatible avec la clé. Il ne vérifie pas leur nombre. Ainsi, si la solution est vierge, l'algorithme va tout le temps répondre vrai : `verif_ligne([[0]], [[1]], 0)`{.language-}.

Une solution serait de ne rendre vrai que si le nombre de blocs de la solution est compatible avec celui de la clé. On peut alors remplacer la ligne 14 par :

```python
    return i_bloc == len(cle_l[i])
```

Notez que ceci est dans notre cas équivalent (mais c'est plus long) à vérifier que le no,bre de cases noires de la solution est identique à celui de la clé :

```python
    return sum(sol) == sum(cle_l[i])
```

### Partie II

#### Question 5

Les constantes $n_c$ et $n_l$ font parti du problème on peut donc les utiliser.

On a dans l'exemple suivant $n_c = 6$, $n_l = 4$ et $n = 15$ (d'où $k = 2$ et $l=3$) :

```
xxxxxx
xxxxxx
xxx...
......
```

On a donc que $n = k \cdot n_c + l$ ce qui donne les relations suivantes :

- $n \div n_c = k$ ($15 \div 6 = 2$)
- $n \mod n_c = l$ ($15 \mod 6 = 3$)

#### Question 6

Commençons par supposer que la fonction auxiliaire `liste_solution_aux`{.language-} est créée.

```python
def liste_solutions(cle_l, cle_c):
    solutions_valides = []
    liste_solutions_aux(init_sol(nc, nl, -1), 0, solutions_valides)

    return solutions_valides
```

Il faut maintenant fabriquer la fonction récursive `liste_solutions_aux`{.language-} :

```python

def liste_solutions_aux(sol_partielle, n, solutions):

    if n == nc * nl:
        if verif(sol_partielle):
            solutions.append(copy_sol(sol_partielle))
    else:
        k , l = n // nc , n % nc

        sol_partielle[k][l] = 0
        liste_solutions_aux(sol_partielle, n + 1, solutions)

        sol_partielle[k][l] = 1
        liste_solutions_aux(sol_partielle, n + 1, solutions)

    return solutions
```

L'équation de récurrence vérifiant `liste_solutions_aux`{.language-} est :

<div>
$$
C(n) = \mathcal{O}(1) + 2 \cdot C(n + 1)
$$
</div>

et $C(n_c \cdot n_l) = \mathcal{O}(n_c \cdot n_l)$. On en déduit que $C(0) = 2^{n_c \cdot n_l} C(n_c \cdot n_l)= 2^{n_c \cdot n_l} \cdot n_c \cdot n_l$ et donc que la complexité de `liste_solution`{.language-} vaut $C(0) + \mathcal{O}(1) = \mathcal{O}(n_c \cdot n_l \cdot 2^{n_c \cdot n_l})$

#### Question 7

Pour tous les $n$ multiple de $n_c$, on vérifie que la dernière ligne a le bon nombre de cases noires (on utilise `verif_ligne`{.language-}) avant de lancer la récursion.

De même, on peut également compter le nombre de cases noire de chaque colonne jusqu'à $n \div n_c$ et stopper la récursion s'il y a déjà trop de cases noires.

### Partie III

#### Question 8

```python
def conflit(c, s):
    ligne = sol_p [i_ligne] # énoncé

    # cas (a)
    if (c >=1) and (linge[c-1] == 1):
        return c
    
    # cas (b)
    for i in range(c, s):
        if ligne[i] == 0:
            return i

    # cas (c)
    if (c + s < nc) and (linge[c + s] == 0):
        return c + s
    
    return nc
```

La complexité est clairement en $\mathcal{O}(s)$ et l'algorithme vérifie bien les 3 cas de conflit possible.

#### Question 9

On utilise itérativement `conflit`{.language-} jusqu'à trouver la solution ou dépasser la ligne :

```python
def prochain(c, s):
    ligne = sol_p [i_ligne] # énoncé

    c2 = conflit(c, s)
    while c2 + s <= nc:
        if c2 < nc:
            c = c2 + 1

        c2 = conflit(c, s)

    if c + s > nc:
        return -1
    
    return c
```

Comme on ne revient jamais en arrière, chaque case de la ligne est examinée 1 fois : la complexité est bien en $\mathcal{O}(nc)$.

### Partie IV

> TBD à faire

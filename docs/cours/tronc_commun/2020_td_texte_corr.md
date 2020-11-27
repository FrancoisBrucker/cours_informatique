TD5 correction
--------------

### exo1

on note `d` le texte et `t` le motif recherché dans le texte

    Algo : recherche_simple 
    Données : d, t : chaînes de caractères
        n = len (d)    
        m = len (t)
        i <-- 0
        tant que i < n - m:
            j <-- i
            tant que j < m et d[i+j] = t[j] :
                j += 1
            si j == m :
               return i
            sinon :
               i <-- i + 1

Le deuxième est plus ou moins pareil

    Algo : recherche_multiple
    Données : d, t : chaînes de caractères
        n = len (d)    
        m = len (t)
        l = []
        i <-- 0
        tant que i < n - m:
            j <-- i
            tant que j < m et d[i+j] = t[j] :
                j += 1
            si j == m :
               l.append(i)
            i <-- i + 1   

Cette approche a un inconvénient : après une comparaison infructueuse,
la comparaison suivante débutera à la position i + 1, sans tenir aucun
compte de celles qui ont déjà eu lieu à l\'itération précédente, à la
position i.

L\'algorithme de Knuth-Morris-Pratt examine d\'abord la chaîne `t` et en
déduit des informations permettant de ne pas comparer chaque caractère
plus d\'une fois.

On regardera une version simplifiée de l\'algo de Knuth-Morris-Pratt :

-   On suppose qu\'on peut tester si un caractère `c` appartient au
    motif `t` en temps constant
-   Le but est de calculer un décalage permettant de ne pas inspecter
    les positions où il n\'y a aucune chance de trouver le motif `t`.
-   On commence par chercher la position `i = m - 1`
-   On inspecte la chaîne `d` de `i` à `i - m` décroissant, et on
    s\'arrête au premier caractère commun (i.e. `j`\<= `i` t.q. `d[i-j]`
    appartient à `t`)
-   Soit `c` = `d[i-j]` le caractère commun
-   On note `k` la position de la première occurrence de `c` dans
    `t[:m-j-1]`
-   Le décalage est égal à `m - 1 - j - k`
-   Si on ne trouve rien, le décalage vaut `m`

A illustrer au tableau :
![](/tc_info/corr/reherche-chine.png){width="400"}

Si vous en avez le courage, voici le code :

    Algo : recherche améliorée
    Données : d, t : chaînes de caractères
        n = len (d)    
        m = len (t)
        i <-- m - 1
        tant que i < n :
          # PRE-TRAITEMENT
          j <-- 0
          tant que j < m  - 1:
            c = d[i - j]  
            si c appartient à t[:m-j-1]
               k <-- dernière_occurrence(c, t[:m-j-1])  
               decalage <--  m - 1 - j  - k
               break
            sinon
               j += 1  
          si j == m - 1:
             decalage <-- m
          # TRAITEMENT
          j <-- 0
          tant que j < m :
             si t[m - j - 1] = d[i - j]
                j += 1
             sinon
                break
          si j = m:
            retourner i - m + 1          
          # DECALAGE      
          i <-- i + decalage      
        retourner -1 

### exo 2

Algorithme à expliquer avec un petit automate fini à deux états
![](/tc_info/corr/automate-s5-1.png){width="400"}

``` {.python}
def compte_mots(d):
    state = 0
    cpt = 0
    for i in range(len(d)):
        if state == 0 and is_alpha(d[i]):
            state = 1
            cpt += 1
        if state == 1 and is_sep(d[i]):
            state = 0
    return cpt
```

Si vous êtes à l\'aise avec les automates finis, vous pouvez aussi leur
montrer un automate qui reconnaît les nombres entiers

-   le chiffre commence par +, - ou rien du tout
-   il n'y a pas de 0 au début de la partie entière
-   il n'y a pas de caractère entre, seulement des chiffres au milieu.

![](/tc_info/automate-s5-2-alt.png){width="400"}

}

### Exo 4

#### 1. Appariements

    -rob-e
    ar-bre

dist = 3

    rob-e
    porte

dist = 3

    a-rbre
    port-e

dist = 4

    cloche-
    h-ochet

dist = 3

    clo-che
    -louche

dist = 2

    ho-chet
    louche-

dist = 3

#### 2. Calcul complet cloche/hochet

La résolution de ce problème repose sur les principes de la
programmation dynamique.

-    on représente l'ensemble des transformations de d1 vers d2 sous la
    forme d'un tableau de (m + 1) lignes et (n + 1) colonnes, avec m =
    \|d1\| et n = \|d2\|
-   pour chaque case (i,j) du tableau,
    -   le passage vers la case (i, j+1) correspond à ins(d2\[j\])
    -   le passage vers la case (i+1, j) correspond à del(d1\[i\])
    -   le passage vers la case (i+1, j+1) correspond à
        perm(d1\[i\],d2\[j\]) ou id(d1\[i\],d2\[j\]) si d1\[i\]=d2\[j\]
-   la valeur de la distance au niveau de la case (i,j) est égale au
    minimum de :
    -   1 + dist(i, j+1)
    -   1 + dist(i+1, j)
    -   dist(i+1, j+1) si d1\[i\]=d2\[j\], ou 1 + dist(i+1, j+1) sinon
-   la distance au niveau de la case (m,n) vaut 0
-   la distance d\'édition est donnée par la valeur dans la case (0,0)

![](/tc_info/corr/td3-alignement.png){width="400"}

#### 3. Algorithme

Préparation

    variables globales : d1, d2 : chaînes de caractères
    m = |d1|
    n = |d2|

Récursif!!

    algo : distance
    données : 
      i, j : etape de calcul
    début  
      si i = m et j = n :
         retourner 0
      sinon si i = m :
         retourner dist(i, j+1) + 1
      sinon si j = n :
         retourner dist(i + 1, j) + 1
      sinon si d1[i] = d2[j] :
         retourner min(dist(i, j+1) + 1, dist(i + 1, j) + 1, dist(i + 1, j + 1))
      sinon
         retourner min(dist(i, j+1) + 1, dist(i + 1, j) + 1, dist(i + 1, j + 1) + 1)
    fin

#### 4.Alignement glouton

![](/tc_info/corr/alignement_glouton.png){width="600"}

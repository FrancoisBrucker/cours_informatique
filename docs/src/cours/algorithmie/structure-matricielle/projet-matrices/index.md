---
layout: layout/post.njk

title: Utilisation des listes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



## Triangle de Pascal

> - **Utilité** : à connaître car exercice classique réduction de complexité spatiale.
> - **Difficulté** : facile


Formule du coefficient binomial dit du [triangle de Pascal](https://fr.wikipedia.org/wiki/Triangle_de_Pascal), avec $1\leq k \leq n$ :

<div>
$$
\binom{n}{k} = \binom{n-1}{k-1} \mathrel{+} \binom{n-1}{k}
$$
</div>

et :

<div>
$$
\binom{n}{0} = \binom{n}{n} = 1 \text{ pour tout } n\geq 0
$$
</div>

{% info %}
[On a déjà vu](../../exercices-calculs-compexités/#triangle-de-pascal){.interne} l'approche récursive. Passons à l'approche itérative. 
{% endinfo %}

### Calcul de la matrice

Le type matrice ne spécifie pas la longueur de chaque tableau, ceci permet de créer des matrices triangulaires inférieures, dans notre cas, une partie du [triangle de Pascal](https://fr.wikipedia.org/wiki/Triangle_de_Pascal) :

<div>
$$
\begin{align*}
&\binom{0}{0} \\
&\binom{1}{0} \binom{1}{1} \\
&\binom{2}{0} \binom{2}{1} \binom{2}{2} \\
&\binom{3}{0} \binom{3}{1} \binom{3}{2} \binom{3}{3} \\
&\binom{4}{0} \binom{4}{1} \binom{4}{2} \binom{4}{3} \binom{4}{4} \\
&\binom{5}{0} \binom{5}{1} \binom{5}{2} \binom{5}{3} \binom{5}{4} \binom{5}{5} \\
\end{align*}
$$
</div>


{% exercice %}
Créez un algorithme rendant une matrice triangulaire inférieure $B$ telle que $B[n][k] = \binom{n}{k}$.

Sa signature devra être :

```pseudocode
algorithme binom_matrice(n: entier) → [[entier]]:
```
{% endexercice %}
{% info %}
Vous pourrez créer itérativement chaque ligne en utilisant la ligne créé à l'itération précédente.
{% endinfo %}
{% details "corrigé" %}
Première version qui calcule toute la matrice triangulaire inférieure :

<span id="algorithme-binom-matrice"></span>

```pseudocode/
algorithme binom_matrice(n: entier) → [[entier]]:
    matrice := [[entier]]
    matrice ← [[entier]]{longueur: n+1}

    ligne := [entier]
    pour chaque i de [0 .. n]:
        ligne ← [entier]{longueur: i+1} 

        matrice[i] ← ligne
        pour chaque j de [0 .. i]:
            si (j == i) ou (j == 0):
                ligne[j] ← 1
            sinon:
                précédent ← matrice[i-1]
                ligne[j] ← précédent[j-1] + précédent[j]

    rendre matrice
```

Il y a deux boucles imbriquées, donc deux invariants à trouver !

L'invariant de la boucle 4-13 peut être :

> **Invariant de la boucle 4-13** : `matrice[i-1]`{.language-} contient la $i$ème ligne de la matrice triangulaire inférieure de Pascal.

Pour le prouver, il faut trouver un invariant à la boucle 8-13. Par exemple :

> **Invariant de la boucle 8-13** : si `matrice[i-2]`{.language-} contient la $i-1$ème ligne de la matrice triangulaire inférieure de Pascal, alors `ligne`{.language-} contient la $i$ème ligne de la matrice triangulaire inférieure de Pascal.

Ce dernier invariant est évidemment vrai par construction de la boucle (c'est la relation de récurrence). Une fois la boucle 8-13 prouvée, cela prouve l'invariant de la boucle 4-13.

{% enddetails %}

{% exercice %}
Utilisez l'algorithme `binom_matrice(n: entier) → [[entier]]`{.language-} pour créer l'algorithme itératif de signature :

```pseudocode
algorithme binom(n: entier, k:entier) → entier
```

calculant $\binom{n}{k}$.

Donnez-en sa complexité spatiale et temporelle.

{% endexercice %}
{% details "corrigé" %}
On utilise alors l'algorithme précédent pour déterminer la binomiale :

<span id="algorithme-binom-1"></span>

```pseudocode
algorithme binom(n: entier, k:entier) → entier:
    matrice ← binom_matrice(n)

    rendre matrice[n][k]
```

La complexité est en $\mathcal{O}(1)$ plus la complexité de la fonction `binom_matrice(n: entier) → [[entier]]`{.language-}.

En utilisant [la règle de calcul de complexité sur les boucles dépendantes mais croissantes](../../complexité-calculs/complexité-algorithmes/#règle-croissance){.interne}, cette complexité est en $\mathcal{O}(n^2)$.

On en déduit que la complexité de l'algorithme `binom`{.language-} est en $\mathcal{O}(nk)$. Comme il faut de plus stocker toute la matrice triangulaire inférieure, sa complexité spatiale est en $\mathcal{O}(nk)$

{% enddetails %}

### Deux lignes suffisent

Comme l'algorithme `binom_matrice(n: entier) → [[entier]]`{.language-} n'a besoin que de la ligne précédente pour créer la ligne de l'itération actuelle, on peut améliorer la complexité spatiale de l'algorithme `binom(n: entier, k:entier) → entier`{.language-} :

{% exercice %}
Créez l'algorithme `ligne_suivante(l: [entier]) → [entier]`{.language-} qui à partir de la liste $l= [\binom{n}{0}, \dots, \binom{n}{n}]$ rend la liste $[\binom{n+1}{0}, \dots, \binom{n+1}{n+1}]$

Donnez-en sa complexité spatiale et temporelle.

{% endexercice %}
{% details "corrigé" %}
On va créer un algorithme qui rend uniquement la dernière ligne de la matrice :

```pseudocode
algorithme ligne_suivante(l: [entier]) → [entier]:
    (l2 := [entier]) ← [entier]{longueur: l.longueur +1}

    l2[0] ← 1
    l2[-1] ← 1

    pour chaque i de [1 .. l2.longueur - 1[:
        l2[i] ← l[i] + l[i-1]

    rendre l2
```

L'algorithme `ligne_suivante(l: [entier]) → [entier]`{.language-} est correct si $l= [\binom{n}{0}, \dots, \binom{n}{n}]$ puisque on applique directement l'équation de récursion. Sa complexité spatiale et temporelle est en $\mathcal{O}(l.\text{\small longueur})$.

{% enddetails %}

{% exercice %}
Utilisez l'algorithme `ligne_suivante(l: [entier]) → [entier]`{.language-} pour améliorer la complexité spatiale de l'algorithme `binom(n: entier, k:entier) → entier`{.language-}.

{% endexercice %}
{% details "corrigé" %}
On a alors la version améliorée de `binom(n: entier, k:entier) → entier`{.language-} :

<span id="algorithme-binom-2"></span>

```pseudocode
algorithme binom(n: entier, k:entier) → entier:
    (l := [entier]) ← [0]
    répéter n fois:
       l ← ligne_suivante(l)

    rendre l[k]
```

Si la complexité temporelle ne change pas, la complexité spatiale est maintenant de $\mathcal{O}(l.\text{\small longueur})$.

{% enddetails %}


Enfin, pour calculer `binom(n: entier, k:entier) → entier`{.language-} on a pas besoin de toute la ligne de la matrice :

{% exercice %}
Modifiez l'algorithme `ligne_suivante`{.language-} pour le rendre de signature `ligne_suivante(l: [entier], k: entier) → [entier]`{.language-} tel que si  $l= [\binom{n}{0}, \dots, \binom{n}{\min(k, n)}]$ rend le tableau $[\binom{n+1}{0}, \dots, \binom{n+1}{\min(k, n+1)}]$.

Utilisez le dans `binom(n: entier, k:entier) → entier`{.language-} pour que sa complexité spatiale soit en $\mathcal{O}(k)$.
{% endexercice %}
{% details "corrigé" %}
On peut faire mieux en ne calculant que les $k+1$ premiers éléments de chaque ligne. Il faut pour cela modifier l'algorithme en créant une version alternative de `ligne_suivante`{.language-} : `ligne_suivante(l: [entier]) → [entier]`{.language-}

<span id="algorithme-binom-3"></span>

```pseudocode
fonction ligne_suivante(l: [entier], k: entier) → [entier]:
    (l2 := [entier]) ← [entier]{longueur: min(k + 1, l.longueur + 1)}

    l2[0] ← 1
    l2[-1] ← 1

    pour chaque i de [1 .. l.longueur[:
        l2[i] ← l[i] + l[i-1]

    rendre l2

algorithme binom(n: entier, k:entier) → entier:
    (l := [entier]) ← [0]
    répéter n fois:
       l ← ligne_suivante(l, k)

    rendre l[k]

```

{% enddetails %}

### Une ligne suffit

La partie précédente montre que l'on peut se passer de matrices et n'utiliser que 2 lignes que l'on échange itérativement. On peut encore faire mieux en n'utilisant qu'une seule ligne !

On va ici utiliser un tableau de taille $k + 1$ qui va contenir tout ce qu'on a besoin, l'astuce étant de commencer à remplir la ligne à la fin.

{% exercice %}
En remplissant la ligne courante de droite à gauche montrez que l'on peut modifier `ligne_suivante`{.language-} pour le rendre de signature `ligne_suivante(l: [entier], n:entier k: entier) → [entier]`{.language-} telle que si $l= [\binom{n}{0}, \dots, \binom{n}{\min(k, n)}]$ en entrée, elle est modifiée en la liste $[\binom{n+1}{0}, \dots, \binom{n+1}{\min(k, n+1)}]$.

Utilisez le dans `binom(n: entier, k:entier) → entier`{.language-}.

{% endexercice %}
{% details "corrigé" %}
<span id="algorithme-binom"></span>

```pseudocode
fonction ligne_suivante(l: [entier], n: entier, k: entier) → ∅:
    de j=min(n, k) à j=1 par pas de -1:
        l[j] ← l[j] + l[j-1]

algorithme binom(n: entier, k:entier) → entier:
    (l := [entier]) ← [entier]{longueur: k+1}
    l[:] ← 1

    pour j dans [0 .. n-1] fois:
       ligne_suivante(l, j, k)

    rendre l[k]

```

{% enddetails  %}

Cette dernière optimisation ne change pas la complexité spatiale en $\mathcal{O}(k)$, elle ne fait que la diminuer par 2. Cette optimisation est cependant significative si $k$ est grand et, surtout, rend l'algorithme très élégant, avec une seule boucle et un seul tableau.

### Code

{% exercice %}
Codez les différents exercices en python. Vous pourrez vérifier vos algorithmes en testant que $\binom{10}{4} = 210$
{% endexercice %}
{% details "corrigé" %}
```python


# V1

def binom_matrice(n):

    matrice = []
    
    for i in range(n+1):
        ligne = [0] * (i+1)

        matrice.append(ligne)
        for j in range(i+1):
            if (j == i) or (j == 0):
                ligne[j] = 1
            else:
                précédent = matrice[i-1]
                ligne[j] = précédent[j-1] + précédent[j]

    return matrice


def binom(n, k):
    matrice = binom_matrice(n)

    return matrice[n][k]

for l in binom_matrice(10):
    print(" ".join(str(x).rjust(3) for x in l))
print("nombre 4 parmi 10 :", binom(10, 4))

# deux lignes suffisent 1

def ligne_suivante(l):
    l2 = [0] * (len(l) + 1)

    l2[0] = 1
    l2[-1] = 1

    for i in range(1, len(l2)-1):
        l2[i] = l[i] + l[i-1]

    return l2


def binom(n, k):
    l = [0]
    for _ in range(n):
       l = ligne_suivante(l)

    return l[k]

print("nombre 4 parmi 10 :", binom(10, 4))


# deux lignes suffisent 2

def ligne_suivante(l, k):
    l2 = [0] * min(k + 1, len(l) + 1)

    l2[0] = 1
    l2[-1] = 1

    for i in range(1, len(l)):
        l2[i] = l[i] + l[i-1]

    return l2

def binom(n, k):
    l = [0]
    for _ in range(n):
       l =ligne_suivante(l, k)

    return l[k]

print("nombre 4 parmi 10 :", binom(10, 4))


# une ligne suffit

def ligne_suivante(l, n, k):
    for j in range(min(n, k), 0, -1):
        l[j] = l[j] + l[j-1]

def binom(n, k):
    l = [1] * (k+1)

    for j in range(n):
       ligne_suivante(l, j, k)
       print(l)

    return l[k]

print("nombre 4 parmi 10 :", binom(10, 4))
```
{% enddetails %}

## 8 reines

> - **Utilité** : à connaître car problème historique
> - **Difficulté** : moyen

{% info "**Anecdote cocasse**" %}
Quand le CEA, qui avait financé les travaux, a demandé à Colmerauer un exemple de problème pratique que pouvait résoudre son nouveau langage [Prolog](https://fr.wikipedia.org/wiki/Prolog), il a répondu le problème des 8 reines.

Pas sûr que les deux interlocuteurs aient la même notion de ce qu'était un _"problème pratique"_.
{% endinfo %}

Ce problème initial consiste à placer 8 reines sur un échiquier (possédant 8 lignes et 8 colonnes) sans qu'aucune reine ne puisse en prendre une autre.
Une reine peut prendre toute pièce qui est sur sa ligne, sa colonne ou sur ses diagonales.

Nous verrons ici un cas un peu plus général consistant à placer $n$ reines sur un échiquier à $n$ lignes et $n$ colonnes. On vous demande de donner la complexité de vos algorithmes en fonction de cette taille $n$.

### Modélisation

On modélise l'échiquier par une matrice `E` à $n$ lignes et $n$ colonnes ($n=8$ pour un échiquier traditionnel): `E[i][j]` correspond à la case à l'intersection de la ligne `i` et de la colonne `j`. Cette case est vraie si une reine y est placée et fausse sinon.

{% exercice %}
Créez un algorithme de signature `échiquier(n: entier) → [[booléen]]`{.language-} permettant de créer un échiquier $n \times n$ vide.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme échiquier(n: entier) → [[booléen]]:
    (E := [[booléen]]) ← [[booléen]]{longueur: n}

    pour chaque i de [0 .. n[:
        E[i] ← [booléen]{longueur: n}
        E[:] ← Faux

    rendre E
```

{% enddetails %}

{% exercice %}
Écrivez un algorithme de signature `position_correcte(E: [[booléen]], i: entier, j: entier) → booléen`{.language-} permettant de savoir si on peut placer une reine à la ligne `i`{.language-} et la colonne `j`{.language-} pour un échiquier donné (de taille quelconque). Elle rendra `Vrai`{.language-} si la reine peut être placée et `Faux`{.language-} sinon.
{% endexercice %}
{% details "corrigé" %}

On regarde les lignes, les colonnes et les diagonales. Il faut faire attention à :

- ne pas regarder la case (i, j)
- rester dans les bornes de l'échiquier

```pseudocode
algorithme position_correcte(E: [[booléen]], i: entier, j: entier) → booléen:
    (n := entier) ← E.longueur
    k := entier

    pour k dans [0 .. n[:
        si (k ≠i) ET E[k][j]:
            rendre Faux

    pour k dans [0 .. n[:
        si (k ≠ j) ET E[i][k]:
            rendre Faux

    pour k dans [1 .. n[:
        si (i + k < n) ET (j + k < n) ET E[i + k][j + k]:
            rendre Faux
        si (i + k < n) ET (j - k > -1) ET E[i + k][j - k]:
            rendre Faux
        si (i - k > -1) ET (j + k < n) ET E[i - k][j + k]:
            rendre Faux
        si (i - k > -1) ET (j - k > -1) ET E[i - k][j - k]:
            rendre Faux
        
    rendre Vrai
```

{% enddetails %}
{% exercice %}
Quelle est la complexité de votre algorithme `position_correcte(E: [[booléen]], i: entier, j: entier) → booléen`{.language-} ?
{% endexercice %}
{% details "corrigé" %}
Elle est en $\mathcal{O}(n)$ avec $n$ le nombre de lignes de l'échiquier.
{% enddetails %}

{% exercice %}
En déduire un algorithme de signature `échiquier_correct(E: [[booléen]]) → booléen`{.language-} qui, à partir d'un échiquier de taille quelconque $n$, rend `Vrai`{.language-} si l'échiquier résout le problème des 8 reines et `Faux`{.language-} sinon.
{% endexercice %}
{% details "corrigé" %}


```pseudocode
algorithme échiquier_correct(E: [[booléen]]) → booléen:
    (n := entier) ← E.longueur

    pour (i:= entier) de [0 .. n[:
        pour (j:= entier) de [0 .. n[:
            si E[i][j] ET (NON position_correcte(E, i, j)):
                rendre Faux
        
    rendre Vrai
```
{% enddetails %}
{% exercice %}
Quelle est la complexité de votre algorithme `échiquier_correct(E: [[booléen]]) → booléen`{.language-} ?
{% endexercice %}
{% details "corrigé" %}
Elle est en $\mathcal{O}(n^2)$ avec $n$ le nombre de lignes de l'échiquier.
{% enddetails %}



### Solution par énumération naïve

Comme toute solution correcte ne peut contenir plus d'une reine par ligne, on peut se contenter de ne générer que toutes les positions avec exactement 1 reine par ligne.

{% exercice %}
Créez un algorithme récursif génère récursivement tous les échiquiers de taille $n$ avec exactement 1 reine par ligne et affiche à l'écran ceux qui sont corrects.
{% endexercice %}
{% info %}
Vous pourrez créer un algorithme de signature `tous_les_échiquiers_rec(E: [[booléen]], i: entier)`{.language-} qui prend en entrée un échiquier `E`{.language-} donné de taille $n$ ayant une reine sur chaque ligne d'indice strictement inférieur à $i$. Cet algorithme vérifie que $E$ est correct si $i\geq n$ et sinon génère les reines de la ligne $i$ et appelle `tous_les_échiquiers_rec(E, i + 1)`{.language-} pour générer les autres

{% endinfo %}
{% details "corrigé" %}

```pseudocode
algorithme tous_les_échiquiers_rec(E: [[booléen]], i: entier):
    (n := entier) ← E.longueur

    si i ≥ n:
        si échiquier_correct(E):
            affiche E à l'écran
        rendre ∅
    pour (j := entier) de [0 .. n[:
        E[i][j] ← Vrai
        tous_les_échiquiers_rec(E, i+1)
        E[i][j] ← Faux

tous_les_échiquiers_rec(échiquier(n), 0)
```

{% enddetails %}
{% exercice %}
Quelles sont les échiquiers corrects à 4 lignes ?
{% endexercice %}
{% details "corrigé" %}

```
▢ ♕ ▢ ▢     ▢ ▢ ♕ ▢
▢ ▢ ▢ ♕     ♕ ▢ ▢ ▢
♕ ▢ ▢ ▢     ▢ ▢ ▢ ♕
▢ ▢ ♕ ▢     ▢ ♕ ▢ ▢
```
{% enddetails %}
{% exercice %}
Quelle est la complexité de votre algorithme `tous_les_échiquiers_rec(E: [[booléen]], i: entier)`{.language-} en supposant que l'affichage se fait en $\mathcal{O}(1)$ ? 
{% endexercice %}
{% details "corrigé" %}
Il génère tous les échiquiers possibles avec 1 reine par ligne, il y en a $n^n$ et les vérifient en $\mathcal{O}(n^2)$. Sa complexité est donc égale à $\mathcal{O}(n^2 \cdot n^n)$.

On peut le démontrer rigoureusement en résolvant l'équation de complexité satisfaite par l'algorithme, à savoir :

<div>
$$
\begin{cases}
C(n) = \mathcal{O}(n^2)\\
C(i) = n \cdot C(i+1)
\end{cases}
$$
</div>

{% enddetails %}


### Solution par énumération V2

Il n'est souvent pas nécessaire de générer toutes les $n$ reines avant de savoir si la position est correcte ou non (par exemple dès que l'on a deux reines sur une même colonne) : 

{% exercice %}
En utilisant l'algorithme `position_correcte(E: [[booléen]], i: entier, j: entier) → booléen`{.language-} la partie précédente, améliorez l'algorithme `tous_les_échiquiers_rec(E: [[booléen]], i: entier)`{.language-} en arrêtant l'ajout de reines dès que la position est incorrecte.
{% endexercice %}
{% details "corrigé" %}
```pseudocode
algorithme tous_les_échiquiers_rec(E: [[booléen]], i: entier):
    (n := entier) ← E.longueur

    si i ≥ n:
        affiche E à l'écran
        rendre ∅
    pour (j := entier) de [0 .. n[:
        
        si position_correcte(E, i, j):
          E[i][j] ← Vrai
          tous_les_échiquiers_rec(E, i+1)
          E[i][j] ← Faux

tous_les_échiquiers_rec(échiquier(n), 0)
```

{% enddetails %}
{% exercice %}
Quelle est la complexité de votre algorithme `tous_les_échiquiers_rec(E: [[booléen]], i: entier)`{.language-} en supposant que l'affichage se fait en $\mathcal{O}(1)$ ? 
{% endexercice %}
{% details "corrigé" %}
On vérifie à chaque positionnement de reines en $\mathcal{O}(i)$, l'équation de complexité satisfaite par l'algorithme est alors :

<div>
$$
\begin{cases}
C(n) = \mathcal{O}(1)\\
C(i) = n \mathcal{O}(i) \cdot \cdot C(i+1)
\end{cases}
$$
</div>

On retrouve notre complexité de $\mathcal{O}(n^2 \cdot n^n)$.
{% enddetails %}


### Solution par permutation

On peut cependant faire mieux que juste créer des échiquiers

{% exercice %}
Montrez que l'on peut représenter le problème des $n$ reines par une permutation $P$ du tableau `[0, ..., n-1]`{.language-}.
{% endexercice %}
{% details "corrigé" %}
Comme deux reines ne peuvent partager une même ligne ou une même colonne : chaque ligne et chaque colonne possèdent exactement une reine. Le tableau $P$ de longueur $n$ tel que $P[i]$ corresponde à l'indice de la colonne de la reine de la ligne $i$ est une permutation de `[0, ..., n-1]`{.language-}.
{% enddetails %}

{% exercice %}
Créez l'algorithme `permutation_correcte(P: [entier], i: entier) → booléen`{.language-} qui prend en paramètre une permutation $P$ et un indice de ligne $i$ et qui rend `Vrai` si la reine à la ligne d'indice $i$ n'est sur aucune diagonales des reine d'indice $j < i$.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme permutation_correcte(P: [entier], i:entier) → booléen:
    (n := entier) ← P.longueur

    pour (k:= entier) de [0 .. i[:
        si (0 ≤ P[i] - i + k < n) ET (P[i] - i + k == P[k]):
            rendre Faux
        si (0 ≤ P[i] + i - k < n) ET (P[i] + i - k == P[k]):
            rendre Faux
        
    rendre Vrai

```

{% enddetails %}
{% exercice %}
Quelle est la complexité de votre algorithme `permutation_correcte(P: [entier], i:entier) → booléen`{.language-}  ? 
{% endexercice %}
{% details "corrigé" %}
Elle est clairement en $\mathcal{O}(n^2)$.

{% enddetails %}


{% exercice %}
Montrez que l'algorithme suivant permet de résoudre le problème des $n$ reine. Quelle est sa complexité ?

```pseudocode
algorithme toutes_les_permutations_rec(P: [entier], i: entier) → booléen:
    (n := entier) ← P.longueur

    si i == n:
        affiche_permutation(P)
        return
    pour (j:= entier) dans [i .. n[:
        P[i], P[j] ← P[j], P[i]
        Si permutation_correcte(P, i):
            toutes_les_permutations_rec(P, i+1)
        P[i], P[j] ← P[j], P[i]

toutes_les_permutations_rec([0 .. n-1])

```

{% endexercice %}
{% details "corrigé" %}
Si $P$ est une permutation et si les $i-1$ premières reines sont placées dans la permutation, les valeurs de $P[i:]$ contiennent toutes les positions restantes possible pour la reine que l'on doit placer à la ligne d'indice $i$. L'algorithme teste alors toutes les possibilités et ne continue que lorsqu'il a trouvé une position cohérente pour la reine de la ligne d'indice $i$.
{% enddetails %}
{% exercice %}
Quelle est la complexité de votre algorithme `toutes_les_permutations_rec(E: [[booléen]], i: entier)`{.language-} en supposant que l'affichage se fait en $\mathcal{O}(1)$ ? 
{% endexercice %}
{% info %}
Vous pourrez utiliser le fait que : 

<div>
$$
$\sum_{0 \leq i \leq n} i! \leq \sum_{0 \leq i \leq n} n! \leq (n+1)!$
$$
</div>>
{% endinfo %}
{% details "corrigé" %}
On vérifie à chaque positionnement de reines en $\mathcal{O}(i)$, l'équation de complexité satisfaite par l'algorithme est alors :

<div>
$$
\begin{cases}
C(n) = \mathcal{O}(1)\\
C(i) = (n-i) \mathcal{O}(i) \cdot \cdot C(i+1)
\end{cases}
$$
</div>

On à alors $C(0) = \mathcal{O}(\sum_{0 \leq i \leq n} i!)$, donc

<div>
$$
C(0) = \mathcal{O}((n+1)!)
$$
</div>

 Ce résultat est très bon puisqu'a priori il faut considérer toutes les permutations **et** les vérifier, ce qui nous prendrait $\mathcal{O}(n^2/cdot n!)$ si on vérifiait uniquement à la fin !
{% enddetails %}

### Code

{% exercice %}
Codez les différents exercices en python. Vérifiez expérimentalement que :

- l'optimisation de l'algorithme `tous_les_échiquiers_rec(E: [[booléen]], i: entier)`{.language-}  est pertinente en pratique
- l'algorithme `toutes_les_permutations_rec(E: [[booléen]], i: entier)`{.language-} est plus rapide

{% endexercice %}
{% info %}
Vous pourrez vérifier vos algorithmes en testant qu'il n'y a que 10 échiquiers corrects pour 5 lignes :

```
♕ ▢ ▢ ▢ ▢     ♕ ▢ ▢ ▢ ▢     ▢ ♕ ▢ ▢ ▢     ▢ ♕ ▢ ▢ ▢     ▢ ▢ ♕ ▢ ▢
▢ ▢ ♕ ▢ ▢     ▢ ▢ ▢ ♕ ▢     ▢ ▢ ▢ ♕ ▢     ▢ ▢ ▢ ▢ ♕     ♕ ▢ ▢ ▢ ▢
▢ ▢ ▢ ▢ ♕     ▢ ♕ ▢ ▢ ▢     ♕ ▢ ▢ ▢ ▢     ▢ ▢ ♕ ▢ ▢     ▢ ▢ ▢ ♕ ▢
▢ ♕ ▢ ▢ ▢     ▢ ▢ ▢ ▢ ♕     ▢ ▢ ♕ ▢ ▢     ♕ ▢ ▢ ▢ ▢     ▢ ♕ ▢ ▢ ▢
▢ ▢ ▢ ♕ ▢     ▢ ▢ ♕ ▢ ▢     ▢ ▢ ▢ ▢ ♕     ▢ ▢ ▢ ♕ ▢     ▢ ▢ ▢ ▢ ♕


▢ ▢ ♕ ▢ ▢     ▢ ▢ ▢ ♕ ▢     ▢ ▢ ▢ ♕ ▢     ▢ ▢ ▢ ▢ ♕     ▢ ▢ ▢ ▢ ♕
▢ ▢ ▢ ▢ ♕     ♕ ▢ ▢ ▢ ▢     ▢ ♕ ▢ ▢ ▢     ▢ ♕ ▢ ▢ ▢     ▢ ▢ ♕ ▢ ▢
▢ ♕ ▢ ▢ ▢     ▢ ▢ ♕ ▢ ▢     ▢ ▢ ▢ ▢ ♕     ▢ ▢ ▢ ♕ ▢     ♕ ▢ ▢ ▢ ▢
▢ ▢ ▢ ♕ ▢     ▢ ▢ ▢ ▢ ♕     ▢ ▢ ♕ ▢ ▢     ♕ ▢ ▢ ▢ ▢     ▢ ▢ ▢ ♕ ▢
♕ ▢ ▢ ▢ ▢     ▢ ♕ ▢ ▢ ▢     ♕ ▢ ▢ ▢ ▢     ▢ ▢ ♕ ▢ ▢     ▢ ♕ ▢ ▢ ▢
```

Et seulement 4 pour 6 lignes :

```
▢ ♕ ▢ ▢ ▢ ▢      ▢ ▢ ♕ ▢ ▢ ▢      ▢ ▢ ▢ ♕ ▢ ▢      ▢ ▢ ▢ ▢ ♕ ▢
▢ ▢ ▢ ♕ ▢ ▢      ▢ ▢ ▢ ▢ ▢ ♕      ♕ ▢ ▢ ▢ ▢ ▢      ▢ ▢ ♕ ▢ ▢ ▢
▢ ▢ ▢ ▢ ▢ ♕      ▢ ♕ ▢ ▢ ▢ ▢      ▢ ▢ ▢ ▢ ♕ ▢      ♕ ▢ ▢ ▢ ▢ ▢
♕ ▢ ▢ ▢ ▢ ▢      ▢ ▢ ▢ ▢ ♕ ▢      ▢ ♕ ▢ ▢ ▢ ▢      ▢ ▢ ▢ ▢ ▢ ♕
▢ ▢ ♕ ▢ ▢ ▢      ♕ ▢ ▢ ▢ ▢ ▢      ▢ ▢ ▢ ▢ ▢ ♕      ▢ ▢ ▢ ♕ ▢ ▢
▢ ▢ ▢ ▢ ♕ ▢      ▢ ▢ ▢ ♕ ▢ ▢      ▢ ▢ ♕ ▢ ▢ ▢      ▢ ♕ ▢ ▢ ▢ ▢

```

{% endinfo %}
{% details "corrigé" %}
```python
def échiquier(n):
    E = []
    for _ in range(n):
        E.append([False] * n)
    return E

def affiche(E):
    print()
    for l in E:
        print(" ".join((x and "♕" or "▢") for x in l))
    print()

affiche(échiquier(10))

def position_correcte(E, i, j):
    n = len(E)

    for k in range(n):
        if (k != i) and E[k][j]:
            return False

    for k in range(n):
        if (k != j) and E[i][k]:
            return False

    for k in range(1, n):
        if (i + k < n) and (j + k < n) and E[i + k][j + k]:
            return False
        if (i + k < n) and (j - k > -1) and E[i + k][j - k]:
            return False
        if (i - k > -1) and (j + k < n) and E[i - k][j + k]:
            return False
        if (i - k > -1) and (j - k > -1) and E[i - k][j - k]:
            return False
        
    return True

E = échiquier(8)
print(position_correcte(E, 4, 6))
E = échiquier(8)
E[4][6] = True
print(position_correcte(E, 4, 6))
print(position_correcte(E, 4, 7))

def échiquier_correct(E):
    n = len(E)

    for i in range(n):
        for j in range(n):
            if E[i][j] and not position_correcte(E, i, j):
                return False
        
    return True


E = échiquier(8)
E[4][6] = True
print(échiquier_correct(E))
E[4][7] = True
print(échiquier_correct(E))

# V1 : on pose toutes les reines et on vérifie

def tous_les_échiquiers_rec(E, i=0):
    n = len(E)

    if i == n:
        if échiquier_correct(E):
            affiche(E)
        return
    for j in range(n):
        E[i][j] = True
        tous_les_échiquiers_rec(E, i+1)
        E[i][j] = False

tous_les_échiquiers_rec(échiquier(4))

# V2 : on pose les reines une à une

def tous_les_échiquiers_rec(E, i=0):
    n = len(E)

    if i == n:
        affiche(E)
        return
    for j in range(n):
        
        if position_correcte(E, i, j):
            E[i][j] = True
            tous_les_échiquiers_rec(E, i+1)
            E[i][j] = False

tous_les_échiquiers_rec(échiquier(5))


# Permutations

def permutation_correcte(P, i):
    n = len(P)

    for k in range(i):
        if (0 <= P[i] - i + k < n) and (P[i] - i + k == P[k]):
            return False
        if (0 <= P[i] + i - k < n) and (P[i] + i - k == P[k]):
            return False
        
    return True


def affiche_permutation(P):
    E = échiquier(len(P))
    for i in range(len(P)):
        E[i][P[i]] = True
    affiche(E)

def toutes_les_permutations_rec(P, i=0):
    n = len(P)

    if i == n:
        affiche_permutation(P)
        return
    for j in range(i, n):
        P[i], P[j] = P[j], P[i]
        if permutation_correcte(P, i):
            toutes_les_permutations_rec(P, i+1)
        P[i], P[j] = P[j], P[i]

toutes_les_permutations_rec(list(range(4)))
```
{% enddetails %}

### Généralisation

{% lien %}
<https://interstices.info/le-probleme-des-8-reines-et-au-dela/>
{% endlien %}

## Multiplication de matrices

Le problème de la multiplication de matrice est un problème intéressant avec une grande histoire :

{% lien %}
<https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm>
{% endlien %}

Nous allons montrer deux algorithmes.

### Naif

{% exercice %}
Écrivez l'algorithme naïf (en $\mathcal{O}(n^3)$)
{% endexercice %}
{% details "corrigé" %}
{% enddetails %}
> TBD algo en n^3

### Strassen

{% lien %}
- <https://fr.wikipedia.org/wiki/Algorithme_de_Strassen>
- <https://www.youtube.com/watch?v=HdysaWNs1g8>
{% endlien %}

> <https://www.youtube.com/watch?v=leONsS4LiV4>

### Code

> python naif et Strassen puis comparaison temps (ref exponentiel)

### On peut faire mieux !

> TBD on peut faire encore mieux.... limite étant n2

{% lien %}
<https://www.youtube.com/watch?v=HdysaWNs1g8>
{% endlien %}

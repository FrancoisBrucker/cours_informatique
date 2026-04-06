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

{% lien %}
[`pascal.py`{.fichier}](https://github.com/FrancoisBrucker/cours_informatique/blob/main/docs/src/cours/algorithmie/structure-matricielle/projet-matrices/pascal.py)
{% endlien %}


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

{% lien %}
[`reines.py`{.fichier}](https://github.com/FrancoisBrucker/cours_informatique/blob/main/docs/src/cours/algorithmie/structure-matricielle/projet-matrices/reines.py)
{% endlien %}
{% enddetails %}

### Généralisation

{% lien %}
<https://interstices.info/le-probleme-des-8-reines-et-au-dela/>
{% endlien %}

## Multiplication de matrices

Le problème de la multiplication de matrice est un problème intéressant [avec une grande histoire](https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm). Nous allons montrer ici la méthode naïve et le plus célèbre des algorithme, celui de Strassen. Notez qu'actuellement on peut faire mieux.

### Création

{% exercice %}
Écrivez un algorithme de signature `création_matrice(n: entier, m: entier)  → [[entier]]`{.language-} qui crée une matrice à $n$ lignes et $m$ colonnes dont les valeurs valent toutes 0.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme création_matrice(n: entier, m: entier)  → [[entier]]:
    M := [[entier]]
    M  ← [[entier]]{longueur: n}
    pour i dans [0 .. m[:
        M[i] ← [entier]{longueur: m}
        M[i][:] ← 0

    rendre M
```

{% enddetails %}
{% exercice %}
Écrivez un algorithme de signature `extraction_matrice(M: [[entier]], n1: entier, n2: entier, m1: entier, m2: entier)  → [[entier]]`{.language-} qui rend une nouvelle matrice valant `M[n1:n2][m1:m2]`{.language-}
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme extraction_matrice(M: [[entier]], n1: entier, n2: entier, m1: entier, m2: entier)  → [[entier]]:
    C = création_matrice(n2-n1, m2-m1)
    pour chaque i de [n1, n2[:
        pour chaque j de [m1, m2[:
            C[i][j] = M[i][j]
    rendre C
```

{% enddetails %}

### Somme 

{% exercice %}
Écrivez un algorithme de signature `somme(A: [[entier]], B: [[entier]])  → [[entier]]`{.language-} qui rend une nouvelle matrice valant `A + B`{.language-}

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme somme(A: [[entier]], B: [[entier]])  → [[entier]]:
    C ← création_matrice(A.longueur, A[0].longueur)

    pour (i:= entier) dans [0 .. C.longueur[:
        pour (j:= entier) dans [0 .. C[0].longueur[:
            C[i][j] ← A[i][j] + B[i][j]
    rendre C
```
{% enddetails %}

### Multiplication Naive

{% exercice %}
Écrivez l'algorithme naïf de la multiplication de deux matrices (sa complexité sera en $\mathcal{O}(n^3)$ avec $n$ le maximum du nombre de ligne et de colonnes dex deux matrices à multiplier). Il devra être de signature 
Écrivez un algorithme de signature `multiplication(A: [[entier]], B: [[entier]])  → [[entier]]`{.language-}
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme multiplication(A: [[entier]], B: [[entier]]) → [[entier]]:
    C ← création_matrice(A.longueur, B[0].longueur)

    pour (i:= entier) dans [0 .. C.longueur[:
        pour (j:= entier) dans [0 .. C[0].longueur[:
            pour k dans [0 .. B.longueur[:
                C[i][j] ← C[i][j] + A[i][k] * B[k][j]
    rendre C
```
{% enddetails %}

### Multiplication de matrices carrées

{% exercice %}
Montrer que pour le cas d'une multiplication de 2 matrices carrées à $n$ lignes, on peut toujours se ramener au cas où les deux matrices on un nombre de lignes égale à une puissance de 2 sans changer la complexité.
{% endexercice %}
{% details "corrigé" %}

Si $n$ est un entier, il existe $p$ tel que $ 2^{p-1} < n \leq 2^p$, donc $2^p\leq 2n$. Si $A$ est une matrice carrée à $n$ on peut alors créer la matrice $A'$ à $2^p$ lignes telles que : 

<div>
$$
A'=\begin{pmatrix}
A & 0\\
0 & 0
\end{pmatrix}
$$
</div>

Et on aura clairement $A \cdot B = (A' \cdot B')[:n][:n]$. Enfin, comme $A'$ a au pire 4 fois plus d'éléments que $A$, les complexités vont rester les même en $\Theta$.

{% enddetails %}

On va donc considérer pour la suite de ces exercices que les matrices carrées ont un nombre de lignes égale à une puissance de 2.

Avant de décrire d'algorithme de Strassen (pour les matrices carrées avec un nombre de lignes égale à une puissance de 2), commençons par en voir le principe en remarquant que l'on peut écrire la multiplication de 2 matrices carrées $A$ et $B$ ainsi :


<div>
$$
\begin{matrix}
&
\begin{pmatrix}
    B_{11} &  B_{12}\\
    B_{21} &  B_{22}\\
\end{pmatrix}
\\
\begin{pmatrix}
    A_{11} &  A_{12}\\
    A_{21} &  A_{22}\\
\end{pmatrix}
&
\begin{pmatrix}
    C_{11} &  C_{12}\\
    C_{21} &  C_{22}\\
\end{pmatrix}
\\
\end{matrix}
$$
</div>

Avec $A_{ij}$, $B_{ij}$ et $C_{ij}$ des matrices carrées telles que pour $1\leq i, j \leq 2$ : $C_{ij} = A_{i1} \cdot B_{1j} + A_{i2} \cdot B_{2j}$

{% exercice %}
Écrivez un algorithme récursif de multiplication de matrices carrées (avec un nombre de lignes égale à une puissance de 2) de signature `multiplication_rec(A: [[entier]], B: [[entier]]) → [[entier]]`{.language-} utilisant les matrices $A_{ij}$, $B_{ij}$ et $C_{ij}$.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme multiplication_rec(A: [[entier]], B: [[entier]]) → [[entier]]:
    (n := entier) ← A.longueur

    Si n ≤ 1:
        rendre [[A[0][0] * B[0][0]]]
    
    (A11 := [[entier]]) ← [[entier]{longueur: n // 2}]{longueur: n // 2}
    A11[:][:] ← A[:n //2][:n //2]
    (A12 := [[entier]]) ← [[entier]{longueur: n // 2}]{longueur: n // 2}
    A12[:][:] ← A[:n //2][n //2:]
    (A21 := [[entier]]) ← [[entier]{longueur: n // 2}]{longueur: n // 2}
    A21[:][:] ← A[n //2:][:n //2]
    (A22 := [[entier]]) ← [[entier]{longueur: n // 2}]{longueur: n // 2}
    A22[:][:] ← A[n //2:][n //2:]

    (B11 := [[entier]]) ← [[entier]{longueur: n // 2}]{longueur: n // 2}
    B11[:][:] ← B[:n //2][:n //2]
    (B12 := [[entier]]) ← [[entier]{longueur: n // 2}]{longueur: n // 2}
    B12[:][:] ← B[:n //2][n //2:]
    (B21 := [[entier]]) ← [[entier]{longueur: n // 2}]{longueur: n // 2}
    B21[:][:] ← B[n //2:][:n //2]
    (B22 := [[entier]]) ← [[entier]{longueur: n // 2}]{longueur: n // 2}
    B22[:][:] ← B[n //2:][n //2:]

    (C11 := [[entier]]) ← somme(multiplication_rec(A11, B11), multiplication_rec(A12, B21))
    (C12 := [[entier]]) ← somme(multiplication_rec(A11, B12), multiplication_rec(A12, B22))
    (C21 := [[entier]]) ← somme(multiplication_rec(A21, B11), multiplication_rec(A22, B21))
    (C22 := [[entier]]) ← somme(multiplication_rec(A21, B12), multiplication_rec(A22, B22))

    (C := [[entier]]) ← [[entier]{longueur: n}]{longueur: n}
    C[:n // 2][:n // 2] ← C11[:][:]
    C[:n // 2][n // 2:] ← C12[:][:]
    C[n // 2]:[:n // 2] ← C21[:][:]
    C[n // 2:][n // 2:] ← C22[:][:]

    rendre C
```
{% enddetails %}
{% exercice %}
Montrez que la complexité de cet algorithme satisfait l'équation de recurrence :

<div>
$$
\begin{cases}
C(1) = \Theta(1)\\
C(n) = \Theta(n^2) + 8 C(n // 2)
\end{cases}
$$
</div>


En conclure que sa complexité est en $Theta(n^3)$ où $n$ est le nombre de lignes des matrices.
{% endexercice %}
{% details "corrigé" %}
L'équation de complexité est claire car toutes les opérations de création et de some sont en $\Theta(n^2)$ et qu'il y a 8 appels récursifs. En triturant cette équation on trouve que pour tout $i$ on a :

<div>
$$
\begin{cases}
C(1) = \Theta(1)\\
C(n) = i \cdot \Theta(n^2) + 8^i C(n // 2^i)
\end{cases}
$$
</div>

Et donc au final 

<div>
$$
\begin{array}{lcl}
C(n) &=& \Theta(\ln(n)n^2) + 8^{\log_2(n)}\Theta(1)\\
&=& \Theta(\ln(n)n^2) + 2^{3\log_2(n)}\Theta(1)\\
&=& \Theta(\ln(n)n^2) + (2^{\log_2(n)})^3\Theta(1)\\
&=& \Theta(\ln(n)n^2) + n^3\Theta(1)\\
&=& \Theta(n^3)\\
\end{array}
$$
</div>

{% enddetails %}

Pour gagner en complexité il faut diminuer le nombre d'appels récursif et c'est exactement ce que fait l'algorithme de Strassen avec une astuce de calcul comme on les aime.

### Strassen

{% lien %}
[page wikipédia sur l'algorithme Strassen](https://fr.wikipedia.org/wiki/Algorithme_de_Strassen)

{% endlien %}

L'astuce qu'a utilisé Strassen est peu ou prou la même que celle utilisée par [Karastuba pour multiplier des entiers](../../projet-complexité-problème/#Karastuba){.interne}. En reprenant les matrices $A_{ij}$ et $B_{ij}$ précédente, il montre que l'on peut créer les matrices $C_{ij}$ en passant par 7 matrices $M_k$ :

<div>
$$
\begin{array}{lcl}
M_1 & =& (A_{11} + A_{22}) \cdot (B_{11} + B_{22}) \\
M_2 & =& (A_{21} + A_{22}) \cdot B_{11} \\
M_3 & =& A_{11} \cdot (B_{12} - B_{22}) \\
M_4 & =& A_{22} \cdot (B_{21} - B_{11}) \\
M_5 & =& (A_{11} + A_{12}) \cdot B_{22} \\
M_6 & =& (A_{21} - A_{11}) \cdot (B_{11} + B_{12}) \\
M_7 & =& (A_{12} - A_{22}) \cdot (B_{21} + B_{22}) 
\end{array}
$$
</div>

Qui permettent d'écrire les matrices $C_{ij}$ :

<div>
$$
\begin{array}{lcl}
C_{11} & =& M_1 + M_4 - M_5 + M_7\\
C_{12} & =& M_3 + M_5\\
C_{21} & =& M_2 + M_4\\
C_{22} & =& M_1 - M_2 - M_3 + M_6\\
\end{array}
$$
</div>

{% exercice %}
Montrer qu'il suffit de 7 récursion pour écrire l'algorithme de Strassen. En déduire l'équation de complexité que satisfait l'algorithme de Strassen.
{% endexercice %}
{% details "corrigé" %}

Il faut une récursion pur chaque matrice M. Comme le reste des opérations est toujours en $\Theta(n^2)$, on obtient l'équation de récursion :

<div>
$$
\begin{cases}
C(1) = \Theta(1)\\
C(n) = \Theta(n^2) + & \cdot C(n // 2)
\end{cases}
$$
</div>

{% enddetails %}
{% exercice %}
Montrer que la complexité de l'algorithme de Strassen est en $\mathcal{O}(n^{2.807}).
{% endexercice %}
{% details "corrigé" %}

En triturant l'équation de récursion on obtient :

<div>
$$
\begin{cases}
C(1) = \Theta(1)\\
C(n) = i \cdot \Theta(n^2) + 7^i C(n // 2^i)
\end{cases}
$$
</div>

Et donc au final 

<div>
$$
\begin{array}{lcl}
C(n) &=& \Theta(\ln(n)n^2) + 7^{\log_2(n)}\Theta(1)\\
&=& \Theta(\ln(n)n^2) + e^{\ln(7)\log_2(n)}\Theta(1)\\
&=& \Theta(\ln(n)n^2) + e^{\ln(7)\ln(n)/\ln(2)}\Theta(1)\\
&=& \Theta(\ln(n)n^2) + e^{\log_2(7)\ln(n)}\Theta(1)\\
&=& \Theta(\ln(n)n^2) + n^{\log_2(7)}\Theta(1)\\
&=& \mathcal{O}(n^{2.807})\\
\end{array}
$$
</div>

L'astuce qui consiste à remarquer que $p^{\log_k(q)} = q^{\log_k(p)}$ est à garder sous le coude. Cela ne sert pas tout le temps, mais quand ça sert, ça sert.

{% enddetails %}

### Code

{% exercice %}
implémentez l'algorithme de Strassen et comparez son exécution à une multiplication naive pur des puissances de 2 allant jusqu'à 1024. Conclusion ?
{% endexercice %}
{% details "corrigé" %}

{% lien %}
[`strassen.py`{.fichier}](https://github.com/FrancoisBrucker/cours_informatique/blob/main/docs/src/cours/algorithmie/structure-matricielle/projet-matrices/strassen.py)
{% endlien %}


La création des différentes matrices rend l'algorithme bien plus gourmand que l'algorithme naïf ! C'est pourquoi l'algorithme de Strassen n'est utilisé que pour de grandes matrices et avec d'autres optimisation que ce que l'on a pu faire.
{% enddetails %}

### Généralisation

> TBD

- Matrices non carrées : On peut les puissances de 2 supérieures en ligne et en colonnes.
- Inverse de matrices

### On peut faire mieux !

> TBD on peut faire encore mieux.... limite étant n2

{% lien %}
[histoire des différents algorithmes](https://www.youtube.com/watch?v=xsZk3c7Oxyw)
[Une expérimentation par LaurieWired](https://www.youtube.com/watch?v=HdysaWNs1g8)
{% endlien %}

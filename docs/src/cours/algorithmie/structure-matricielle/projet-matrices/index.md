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
        l2[1] ← l[i] + l[i-1]

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
    m ← min(k, l.longueur + 1)
    (l2 := [entier]) ← [entier]{longueur: m + 1}

    l2[0] ← 1
    l2[-1] ← 1

    pour chaque i de [1 .. m]:
        l2[1] ← l[i] + l[i-1]

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
    l[0] ← 1
    l[min(n + 1, k)] ← 1

    de j=min(n, k) à j=1 par pas de -1:
        l[j] ← l[j] + l[j-1]

algorithme binom(n: entier, k:entier) → entier:
    (l := [entier]) ← [entier]{longueur: k+1}

    l[0] ← 1
    pour j dans [0 .. n-1] fois:
       ligne_suivante(l, j, k)

    rendre l[k]

```

{% enddetails  %}

Cette dernière optimisation ne change pas la complexité spatiale en $\mathcal{O}(k)$, elle ne fait que la diminuer par 2. Cette optimisation est cependant significative si $k$ est grand et, surtout, rend l'algorithme très élégant, avec une seule boucle et un seul tableau.

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

{% faire %}
Créez un algorithme permettant de créer un échiquier $n \times n$ vide.
{% endfaire %}

{% faire %}
Écrivez une fonction permettant de savoir si on peut placer une reine à la ligne `i`{.language-} et la colonne `j`{.language-} pour un échiquier donné (de taille quelconque). Elle rendra `Vrai`{.language-} si la reine peut être placée et `Faux`{.language-} sinon.
{% endfaire %}

{% faire %}
En déduire Éun algorithme qui, à partir d'un échiquier de taille quelconque $n$, rend `Vrai`{.language-} si l'échiquier résout le problème des 8 reines et `Faux`{.language-} sinon.
{% endfaire %}

### Solution par énumération naïve

> On teste tout
> On positionne les 8 reines une à une : 
> - ixj pour tous 
> - en petit train

### Solution par énumération V2

> on s'arrête lorsque impossible

### Solution par permutation

On peut cependant faire mieux que juste créer tous les échiquiers possibles.

{% faire %}
Montrez que l'on peut représenter le problème des $n$ reines par une permutation du tableau `[0, ..., n-1]`{.language-}.
{% endfaire %}

{% faire %}
Écrivez un algorithme prenant en paramètre une permutation de `[0, ..., n-1]`{.language-} et rendant `Vrai`{.language-} si la permutation est une solution du problème des 8 reines et `Faux`{.language-} sinon.
{% endfaire %}

> TBD donner un algo qui crée une permutation itérativement (en faisant le petit train)

{% faire %}

Montrez qu'il est inutile d'examiner toutes les permutations et qu'il suffit souvent de connaître le début d'une permutation pour l'invalider. En déduire une méthode de résolution du problème n'examinant pas toutes les permutations.
{% endfaire %}

### Généralisation

{% lien %}
<https://interstices.info/le-probleme-des-8-reines-et-au-dela/>
{% endlien %}



## Multiplication de matrice


### Naif

> TBD algo en n^3

### Strassen

> TBD à partir de la multiplication d'entier qu'on a déjà vu
> TBD <https://fr.wikipedia.org/wiki/Algorithme_de_Strassen>

> TBD on peut faire encore mieux.... limite étant n2


---
layout: layout/post.njk
title: "DS Algorithmie"
---

{% note "**Sujet**" %}

[Recherche de sous-mots](./sujet/main.pdf){.fichier}

Durée du contrôle : 2h.

{% endnote %}
{% info %}
Il y avait deux petites erreurs dans l'énoncé originel. Elles sont corrigés ici.
{% endinfo %}

## Barème

> TBD

### Ventilation des notes

> TBD

## Corrigé

### Exercice 1

#### 1.1 Algorithme python

##### 1.1.1

```pseudocode
algorithme est_sous_chaîne(a: chaîne, b: chaîne) → booléen:
    trouvé := booléen
    j := entier
    pour chaque (i := entier) de [0 .. a.longueur - b.longueur + 1[:
        trouvé ← Vrai
        j ← 0
        tant que j < b.longueur:
            si b[j] ≠ a[i + j]:
                trouvé ← Faux
                j ← j + 1 
        si trouvé:
            rendre Vrai
    rendre Faux

```

##### 1.1.2

- au minimum on ne fait qu'une seule itération pour la boucle `pour chaque`{.language-}. On ne peut sortir de l'algorithme que si `trouvé`{.language-} est vrai en sortie de la boucle `tant que`{.language-} on a alors fait $\mathcal{O}(b.\text{\small longueur})$ itérations de cette dernière. Comme les autres instructions sont toutes en $\mathcal{O}(1)$, la complexité minimale est alors de $\mathcal{O}(b.\text{\small longueur})$. Ceci arrive si `a`{.language-} commence par `b`{.language-}.
- Dans le pire des cas, on fait $\mathcal{O}(a.\text{\small longueur} - b.\text{\small longueur})$ itérations de la boucle `pour chaque`{.language-} et $\mathcal{O}(b.\text{\small longueur})$ itération de la boucle `tant que`{.language-}. Comme les autres instructions sont toutes en $\mathcal{O}(1)$, la complexité minimale est alors de $\mathcal{O}(a.\text{\small longueur} \cdot b.\text{\small longueur})$. Ceci arrive si `a = x .. x`{.language-} et `b = x ... xy`{.language-}.

##### 1.1.3

```pseudocode
sous_chaîne(a: chaîne, b: chaîne) → entier
```

##### 1.1.4

Il faut rendre un indice, pas juste un booléen :

```pseudocode
algorithme sous_chaîne(a: chaîne, b: chaîne) → entier:
    trouvé := booléen
    j := entier
    pour chaque (i := entier) de [0 .. a.longueur - b.longueur + 1[:
        trouvé ← Vrai
        j ← 0
        tant que j < b.longueur:
            si b[j] ≠ a[i + j]:
                trouvé ← Faux
                j ← j + 1 
        si trouvé:
            rendre i
    rendre -1
```

La boucle `pour chaque`{.language-} va faire varier $i$ pour toutes ses positions de sous-chaînes possibles et la variable `trouvé`{.language-} ne peut valoir `Vrai` à la sortie de la boucle `tant que`{.language-} que si $b[j] == a[i + j]$ pour tout $0 \leq j < b.\text{\small longueur}$, donc que si $b$ est une sous-chaîne de $a$

#### 1.2 Bornes

##### 1.2.1

Il faut au minimum lire les données, c'est à dire vérifier tous les caractères de $a$ et de $b$, la complexité du problème est en $\Omega(a.\text{\small longueur} + b.\text{\small longueur})$.

On peut être plus précis en analysant des algorithmes fictifs :

-  s'il existe un algorithme résolvant le problème qui ne regarde jamais tous les caractères de $b$ sinon on prend `b = xxxxx` et `a = xxxxx` et si l'algorithme ne regarde pas tout `b` on change une des lettres non regardées en `y`.
- s'il existe un algorithme résolvant le problème qui regarde strictement moins de $a.\text{\small longueur} - b.\text{\small longueur}$ caractères de $a$ on prend `b = yxxxx` et `a = xxxxx` et si l'algorithme regarde moins de $n-m$ caractères de `a` on change le plus à gauche des caractères non regardés en `y`

Les deux conditions montrent que la complexité du problème est en $\Omega(b.\text{\small longueur}) + \Omega(a.\text{\small longueur} - b.\text{\small longueur}) =  \Omega(a.\text{\small longueur} + b.\text{\small longueur})$
##### 1.2.2

Comme la complexité de l'algorithme de la question 1.1.4 est en $\mathcal{O}(a.\text{\small longueur} \cdot b.\text{\small longueur})$, la complexité problème est :

- $\Omega(a.\text{\small longueur} + b.\text{\small longueur})$.
- $\mathcal{O}(a.\text{\small longueur} \cdot b.\text{\small longueur})$

#### 1.3 Complexité en moyenne

##### 1.3.1

Si les caractères sont équiprobables alors la position dans la chaîne de caractères importe peu. La probabilité que 2 caractères de $a$ et de $b$ soient égaux est donc la même que la probabilité de tirer deux fois le même caractère : c'est $\frac{1}{\vert \mathcal{A} \vert}$ où $\mathcal{A}$ est l'ensemble des caractères possibles.

##### 1.3.2

On note $p$ la probabilité de tirer avec remise deux lettres identiques. La probabilité que $a[i + j] == b[j]$ pour tout $0 \leq j < k$ et que $a[i + k] \neq b[k]$ vaut alors (puisqu'il y a équiprobabilité) : $P_k = p^{k}(1-p)$

Pour une position $i$ donnée dans l'algorithme, le nombre moyen de passage dans la boucle `tant que`{.language-} pour un $i$ fixé vaut alors : $\sum_{k=0}^{b.\text{\small longueur} - 1}P_k \cdot (k + 1)$, que l'on peut majorer par :

<div>
$$
\sum_{k=0}^{b.\text{\small longueur} - 1}P_k \cdot (k + 1) = \sum_{k=0}^{b.\text{\small longueur} - 1} (k + 1) \cdot p^{k}(1-p) = \frac{1}{p} \cdot \sum_{k=1}^{b.\text{\small longueur}} (k) \cdot p^{k}(1-p) \leq \frac{1}{1-p}
$$
</div>

Comme $p$ est une constante, le nombre moyen de passage dans la boucle à $i$ fixé est en $\mathcal{O}(1)$. De plus comme toutes les instructions de la boucle sont en $\mathcal{O}(1)$, on on en conclut que pour $i$ fixé il y a en moyenne $\mathcal{O}(1)$ opérations d'effectuées. Enfin, comme $0 \leq i \leq a.\text{\small longueur} - b.\text{\small longueur}$ i y a $\mathcal{O}(a.\text{\small longueur} - b.\text{\small longueur})$ valeur différentes de $i$ et donc la complexité moyenne vaut : $\mathcal{O}(a.\text{\small longueur} - b.\text{\small longueur})$

### Exercice 2

#### 2.1 Principe

##### 2.1.1

Pour une position de $i$ donnée si $a[i + j] = b[j]$ pour tout $0 \leq j < m$ $b$ est bien une sous-chaîne de $a$ en position $i$. Sinon soit :

- $a[i + m -1] \neq b[m-1]$ et n'est pas dans $b[:-1]$ : $b$ ne peut-être une sous-chaîne de $a$ pour tout $i'$ tel que $i \leq i' < i + m$
- $a[i + m -1]  \neq b[m-1]$ et est dans $b[:-1]$ : la première position plus strictement plus grande que $i$ où $b$ pourra être une sous-chaîne de $a$ sera celle où on fera correspondre $a[i + m -1]$ avec sa plus grande position dans $b$.
- $a[i + m -1] = b[m-1]$ et n'est pas dans $b[:-1]$ : $b$ ne peut-être une sous-chaîne de $a$ pour tout $i'$ tel que $i < i' < i + m$
- $a[i + m -1] = b[m-1]$ et est dans $b[:-1]$ : la première position plus strictement plus grande que $i$ où $b$ pourra être une sous-chaîne de $a$ sera celle où on fera correspondre $a[i + m -1]$ avec sa plus grande position dans $b$.

##### 2.1.2

Contrairement à l'algorithme naïf l'indice $i$ peut augmenter de plus que 1 unité. Il peut même augmenter de $m$ si le dernier élément de $a$ n'est pas dans $b$.


##### 2.2.1

Le décalage pour l'indice $i$ de $a$ ne dépend que des caractères de $b$ et de leurs positions :

- si le caractère n'est pas dans $b$ on décale de $m$
- si le caractère est dans $b$ on décale de $m - k - 1$ où $k$ est le plus grand indice où apparaît le caractère. Ceci donne l'algorithme suivant :

```pseudocode
algorithme décalage(b: chaîne) → [entier]:
    (m := entier) ← b.longueur
    T := [entier] ← [entier]{longueur: L}
    pour chaque (i := entier) de [0 .. L[:
        T[i] ← m
    pour chaque (k := entier) de [0 .. b.longueur - 1[:
        T[ord(b[k])] ← min(T[ord(b[k])], m - k - 1)

    rendre T
```


##### 2.2.2

L'algorithme a deux boucles la première possède $\mathcal{O}(L)$ itérations et la seconde $\mathcal{O}(b.\text{longueur})$ itérations. Comme la fonction `ord`{.language-} est de complexité $\mathcal{O}(1)$ la complexité de l'algorithme est $\mathcal{O}(b.\text{longueur} + L)$.

Comme le nombre de caractères pouvant à priori être aussi grand qu'on veut, $L$ dépend du problème (4, pour de l'ADN, 20 pour des protéines et $2^{28}$ pour des chaînes de caractères Unicode) et ne peut être assimilé à une constante.

#### 2.3 Recherche

##### 2.3.1

```pseudocode
fonction décalage(b: chaîne) → [entier]:
    (m := entier) ← b.longueur
    T := [entier] ← [entier]{longueur: L}
    pour chaque (i := entier) de [0 .. L[:
        T[i] ← m
    pour chaque (k := entier) de [0 .. b.longueur - 1[:
        T[ord(b[k])] ← min(T[ord(b[k])], m - k - 1)

    rendre T

algorithme BMH(a: chaîne, b: chaîne) → [entier]:
    (m := entier) ← b.longueur
    T := [entier] ← [entier]{longueur: L}
    pour chaque (i := entier) de [0 .. L[:
        T[i] ← m
    pour chaque (k := entier) de [0 .. b.longueur - 1[:
        T[b[k]] ← min(T[b[k]], m - k - 1)

    rendre T
```
##### 2.3.2

Dans le pire des cas on se comportera comme l'algorithme naïf. Par exemple si a = "aaaaaaaaaaaaaaaaaa" et b = "baaa" on incrémentera toujours l'indice `i`{.language-} de 1 et l'indice `j`{.language-} ira de $m$ à 0 pour tout indice $i$. Dans ce cas là la complexité sera de $\mathcal{O}(b.\text{longueur} + L + a.\text{longueur} \cdot b.\text{longueur})$.

Dans le meilleur des cas, on augmente $i$ de $m$ a chaque itération, par exemple si a = "aaaaaaaaaaaaaaaaaa" et b = "bbbb". Dans ce cas là la complexité sera de $\mathcal{O}(b.\text{longueur} + L + a.\text{longueur} / b.\text{longueur})$.

##### 2.3.3

La complexité spatiale sera égale a la taille du tableau `T`{.language-} c'est à dire : $\mathcal{O}(L)$ (qui peut être gigantesque).

##### 2.3.4

On utiliserait cet algorithme lorsque $L$ est petit. Dans ce cas là, l'algorithme ira plus vite que l'algorithme naïf puisque sa complexité minimale sera en $\mathcal{O}(b.\text{longueur} + a.\text{longueur} / b.\text{longueur})$.

### Exercice 3

#### 3.1 Complexité de l'algorithme

##### 3.1.1 

En analysant les cas de l'algorithme, on a soit :

- `j ← j + 1`{.language-} et :
  - `i+j`{.language-} augmente strictement
  - `i`{.language-} est constant
- `i ← i + 1`{.language-} et :
  - `i+j`{.language-} augmente strictement
  - `i`{.language-}  augmente strictement
- `i ← i + j - T[j]`{.language-} et `j ← T[j]`{.language-} :
    - `i+j`{.language-} est constant
  - `i`{.language-}  augmente strictement puisque par définition $T[j] < j$ pour tout $j$

##### 3.1.2

Les variables $i$ et $i+j$ sont croissantes et l'un des deux augmente strictement à chaque itérations de la boucle `tant que`{.language-}. De là comme :

- après $n$ augmentations de $i$ $i+j \geq n$ 
- après $n$ augmentations de $i+j$ on a aussi $i+j \geq n$ 

Il y a au mieux $n + n$ itérations de la boucle `tant que`{.language-}. Comme toutes les instructions de la boucle sont en $\mathcal{O}(1)$ la complexité totale de l'exécution de la boucle `tant que`{.language-} est en $\mathcal{O}(n)$ et donc la complexité totale de l'algorithme en $\mathcal{O}(n + f(m))$

#### 3.2 Preuve de l'algorithme

Supposons que l'on soit dans le cas ci-après :

```
          i
a : aaaaaaaaaaaaXaaaaaaaaaaaaaa
b :       bbbbbbYbbbbbb
                j
```

Avec :

- $a[i+k] = b[k]$ pour $0\leq k < j$
- $a[i+j] \neq b[j]$

S'il existe $i < i' \leq i + j$ tel que $a[i'+k] = b[k]$ pour $0\leq k < j + i'-i$ :

```
          i  i'
a : aaaaaaaaabbbXaaaaaaaaaaaaaa
b :          BBBbbbYbbbbbb
                j
```


alors on a aussi $b[k] = b[j + i' - i + k]$ pour $0\leq k < j + i'-i$. Le plus petit indice $i'$ est donné par la fonction de décalage ! Comme au pire $i' = i + j$ si aucun autre décalage n'est possible on progresse dans la recherche de la sous-chaîne comme le fait l'algorithme.

#### 3.3

##### 3.3.1

On montre par une récurrence triviale qu'au début de chaque itération :

- $0 \leq T[l] < l$ pour tout $l>0$ et $T[0] = 0$,
- $k  < j - 1 < i$ 

De là, les conditions sur $k$ sont également vérifiées.

##### 3.3.2

La variable $i$ est croissante. Lorsque $i$ n'augmente pas c'est $k$ qui diminue strictement et $k$ ne peut augmenter que si $i$ croit strictement. De là $i$ ne peut rester constant qu'au plus le nombre d'itération ou il a crût strictement : il y a au mieux $2m$ iterations.

##### 3.3.3

L'idée est de procéder itérativement. Si on suppose que l'on a toutes les valeurs de $T[l]$ pour $l < i$, on peut trouver $T[l]$ en procédant ainsi :

- si $b[T[i-1]] = b[i-1]$ alors $T[i] = T[i-1] + 1$ puisque l'on peut prolonger la sous-chaîne
- si $b[T[i-1]] \neq b[i-1]$ on peut poser $j = T[i-1] + 1$. De là :
  - si $b[T[j-1]] = b[i-1]$ alors $T[i] = T[j-1] + 1$ puisque l'on peut prolonger la sous-chaîne
  - sinon, si $T[j-1] > 1$, on peut recommencer avec une plus petite chaîne en posant $j = T[j-1] + 1$ et en revenant à l'étape précédente
  - si $T[j-1] \leq 1$ c'est fini et on a $T[i] = 0$

C'est exactement ce que fait l'algorithme.

### Exercice 4

- on a $\Omega(n+m)$ question 1.2.1
- et KMP en $\mathcal{O}(n+m)$

### Code python

#### Naïf

```python
def naïf(a, b):
    for i in range(len(a) - len(b) + 1):
        trouvé = True
        j = 0
        while j < len(b):
            if b[j] != a[i + j]:
                trouvé = False
                j = len(b)
            else:
                j += 1
        if trouvé:
            return i
    return -1
```

#### BMH


```python
def décalage(b):
    d = {}
    for j in range(len(b) - 1):
        c = b[j]
        d[c] = j

    return d


def BMH(a, b):
    décalé = décalage(b)

    i = 0
    j = len(b) - 1
    while i <= len(a) - len(b):
        if a[i + j] != b[j]:
            if a[i + j] not in décalé:
                i += len(b)
            else:
                i += len(b) - décalé[a[i + j]] - 1
            j = len(b) - 1
        elif j == 0:
            return i
        else:
            j -= 1
    return -1

```

#### KMP

```python
def décalage_KMP(b):
    T_b = [0] * len(b)

    i, j, k = 2, 2, 0
    c = b[j-1]

    while i < len(b):
        k = T_b[j-1]

        if c == b[k]:      
            T_b[i] = k + 1
            i += 1
            j = i
            c = b[j-1]
        elif k <= 1:
            T_b[i] = 0
            i += 1
            j = i
            c = b[j-1]
        else:
            j = k + 1

    return T_b

def KMP(a, b):
    Tb = décalage_KMP(b)
    
    i = 0
    j = 0

    while i + j < len(a):
        if a[i + j] == b[j]:
            j += 1

            if j >= len(b):
                return i

        else:
            if j == 0:
                i += 1
            else :
                l = j - Tb[j]
                i += l
                j -= l
    return -1
```

#### Affichages

```python
def affiche(a, b, algo):
    i = algo(a, b)
    print(i)
    if i > -1:
        print(a)
        print(" " * i + b)
    else:
        print(b, "n'est pas une sous-chaîne de", a)


for algo in (naif, BMH, KMP):
    affiche("ABABAAABABACABCBAB",
            "ABABACA", algo)

    affiche("ABABAAABABACABCBAB",
            "ABABABA", algo)

```


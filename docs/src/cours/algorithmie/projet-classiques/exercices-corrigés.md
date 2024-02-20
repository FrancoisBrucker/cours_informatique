---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Fibonacci

### Récursif

En notant $A(n)$ le nombre d'appels à la fonction, on a :

- l'appel proprement dit,
- le nombre d'appel à `fibonacci_rec(n-1)`{.language-}
- le nombre d'appel à `fibonacci_rec(n-2)`{.language-}

Ce qui donne l'équation suivante :

<div>
$$
A(n) = 1 + A(n-1) + A(n-2)
$$
</div>

En notant $C(n)$ la complexité de la fonction, on a l'équation de récurrence suivante :

<div>
$$
C(n) = \mathcal{O}(1) + C(n-1) + C(n-2)
$$
</div>

La complexité étant croissante, on a que : $C(n-1) \geq C(n-2)$ et on a bien l'inégalité :

<div>
$$
\mathcal{O}(1) + 2 \cdot C(n-2) \leq C(n) \leq \mathcal{O}(1) + 2 \cdot C(n-1)
$$
</div>

<div>
$$
\begin{array}{ccll}
C(n) &\leq & \mathcal{O}(1) + 2 \cdot C(n-1)&\\
     &\leq & \mathcal{O}(1) + 2 \cdot (\mathcal{O}(1) + 2 \cdot C(n-2)) & \text{en réapplicant l'inégalité pour } C(n-1)\\
     &\leq & \mathcal{O}(1)\cdot (1 + 2) + 4 \cdot C(n-2)&\\
     &\leq & \mathcal{O}(1)\cdot (1 + 2) + 4 \cdot (\mathcal{O}(1) + 2 \cdot C(n-3)) & \text{en réapplicant l'inégalité pour } C(n-2)\\
     &\leq & \mathcal{O}(1)\cdot (1 + 2 + 4) + 8 \cdot C(n-3)&\\
\end{array}
$$
</div>

On peut reappliquer l'inégalité de récurrence autant de fois que l'on veut ce qui donne, en l'appliquant $K$ fois :

<div>
$$
\begin{array}{ccll}
C(n) &\leq & \mathcal{O}(1)\cdot (\sum_{i=0}^{K-1}2^i) + 2^K \cdot C(n-K)&\\
\end{array}
$$
</div>

Les seules valeurs de $C(n)$ connues sont celles pour $n=1$ ou $n=2$. Il faut donc appliquer notre formule pour $K=n-2$, ce qui donne l'inégalité :

<div>
$$
\begin{array}{ccll}
C(n) &\leq & \mathcal{O}(1)\cdot (\sum_{i=0}^{n-3}2^i) + 2^{n-2} \cdot C(2)&\\
\end{array}
$$
</div>

De même, en utilisant l'inégalité $\mathcal{O}(1) + 2 \cdot C(n-2) \leq C(n)$, on obtient :

<div>
$$
\begin{array}{ccll}
C(n) &\geq & \mathcal{O}(1) + 2 \cdot C(n-2)&\\
     &\geq & \mathcal{O}(1) + 2 \cdot (\mathcal{O}(1) + 2 \cdot C(n-4)) & \text{en réapplicant l'inégalité pour } C(n-2)\\
     &\geq & \mathcal{O}(1)\cdot (1 + 2) + 4 \cdot C(n-4)&\\
     &\geq & \mathcal{O}(1)\cdot (1 + 2) + 4 \cdot (\mathcal{O}(1) + 2 \cdot C(n-6)) & \text{en réapplicant l'inégalité pour } C(n-4)\\
     &\geq & \mathcal{O}(1)\cdot (1 + 2 + 4) + 8 \cdot C(n-6)&\\
\end{array}
$$
</div>

De même que précédemment, en applicant l'inégalité de récurrence $K$ fois :

<div>
$$
\begin{array}{ccll}
C(n) &\geq & \mathcal{O}(1)\cdot (\sum_{i=0}^{K-1}2^i) + 2^K \cdot C(n-2\cdot K)&\\
\end{array}
$$
</div>

Les seules valeurs de $C(n)$ connues sont celles pour $n=1$ ou $n=2$. Il faut donc appliquer notre formule pour $K=\frac{n-2}{2}$, ce qui donne l'inégalité :

<div>
$$
\begin{array}{ccll}
C(n) &\geq & \mathcal{O}(1)\cdot (\sum_{i=0}^{(n-4)/2}2^i) + {(\sqrt{2})}^{n-2} \cdot C(2)&\\
\end{array}
$$
</div>

La fin est facile en utilisant le fait que $\sum_{i=0}^{K}2^i = 2^{K+1} - 1$

### Valeur de $F(n)$

On prouve la propriété par récurrence.

Initialisation :

- $F(1) = 1 = \frac{1}{\sqrt{5}}(\frac{1+\sqrt{5}}{2} - \frac{1-\sqrt{5}}{2}) = \frac{1}{\sqrt{5}}(\varphi - \frac{1}{-\varphi})$
- $F(2) = \frac{1}{\sqrt{5}}(\varphi^2-\frac{1}{(-\varphi)^2}) = \frac{1}{\sqrt{5}}(\varphi + 1 -(\frac{1}{(-\varphi)} + 1) = \frac{1}{\sqrt{5}}(\varphi + \frac{1}{\varphi}) = F(1)$

On suppose la propriété vrai jusqu'à $n-1$. Pour $n$ :

$F(n) = F(n-1) + F(n-2) = \frac{1}{\sqrt{5}}(\varphi^{n-1}-\frac{1}{(-\varphi)^{n-1}}) + \frac{1}{\sqrt{5}}(\varphi^{n-2}-\frac{1}{(-\varphi)^{n-2}}) = \frac{1}{\sqrt{5}}(\varphi^{n-2}(1 + \varphi) - \frac{1}{(-\varphi)^{n-2}}(1+ \frac{1}{\varphi}))$

Comme $\varphi$ et $-\frac{1}{\varphi}$ sont les racines du polynôme $P(X) = X^2 - X -1$ on a :

$F(n) = \frac{1}{\sqrt{5}}(\varphi^{n-2}(\varphi^2) - \frac{1}{(-\varphi)^{n-2}}(\frac{1}{\varphi^2})) = \frac{1}{\sqrt{5}}(\varphi^n-\frac{1}{(-\varphi)^n})$

### Itératif

```python
def fibo_iter(n):
    a = 1
    b = 1
    for i in rang(n):
        a, b = a+b, a
    return a
```

### Récursif terminal

La complexité étant terminale, il y a $\mathcal{O}(n)$ appels récursifs. Comme le reste de la fonction est en $\mathcal{O}(1)$ la complexité totale est en $\mathcal{O}(n)$.

Le fait que la fonction calcule bien la suite de Fibonacci se fait par récurrence. On va montrer par récurrence que `fibo_rec2(n, a, b)` rend la valeur de la suite pour $F(1) = b$ et $F(2) = a$.

- Initialisation : `fibo_rec2(1, a, b) = b` et `fibo_rec2(2, a, b) = a`
- On suppose la propriété vraie pour `fibo_rec2(n-1, a, b)`. Comme `fibo_rec2(n, a, b) = fibo_rec2(n-1,a+b , a)`, la propriété est vérifiée.

## Noob trap

C'est bien la troisième proposition qui est la bonne !

La troisième ligne de l'algorithme a pour complexité :

- le calcul de $f(n//2)$
- le calcul de $f(n//4)$
- la multiplication des deux valeurs obtenues

En reprenant ce que l'on a fait pour Fibonacci, on a l'inégalité :

<div>
$$
C(n) \leq \mathcal{O}(1) + 2 \cdot C(n/2)
$$
</div>

Ce qui donne en réitérant cette inégalité :

<div>
$$
C(n) \leq \mathcal{O}(1)(\sum_{i=0}^K2^i) + 2^K \cdot C(n/2^K)
$$
</div>

Comme la seule complexité que l'on connait est $C(1) = \mathcal{O}(1)$, on doit prendre $K$ tel que $2^K \simeq n$, c'est à dire $k = \log_2(n)$. On a alors :

<div>
$$
C(n) \leq \mathcal{O}(1)(\sum_{i=0}^{\log_2(n)}2^i) + 2^{\log_2(n)} \cdot C(1)
$$
</div>

Et donc :

<div>
$$
C(n) \leq \mathcal{O}(1)(2^{\log_2(n) +1}) + 2^{\log_2(n)} \cdot C(1)
$$
</div>

Et comme $2^{\log_2(n)} = n$, on trouve bien $C(n) \leq \mathcal{O}(n)$.

## Tours de Hanoï

{% lien %}
[Tours de Hanoï sur Wikipédia](https://fr.wikipedia.org/wiki/Tours_de_Hano%C3%AF)
{% endlien %}

On suppose que l'on a les trois emplacements de tours A, B et C ; et que l'on veuille déplacer les disques de la tours A vers la tour C.

1. pour pouvoir déplacer le plus grand disque de la tour A, il faut avoir déplacé tous les disques au-dessus de lui. Comme c'est le plus grand disque, il est de plus seul sur son emplacement
2. une fois le plus grand disque seul sur sa tour, il faut le déplacer en C. Ceci n'est possible que si tous les autres disques sont en B. Il donc de plus qu'ils forment une tour
3. une fois le plus grand disque à sa place, il convient de déplacer la tour formée des autres disques, en B, sur l'emplacement C.

Donc si on possède un algorithme optimal, disons `hanoï(départ, arrivée, intermédiaire, n-1)`{.language-} pour une tour de taille $n-1$, alors l'algorithme optimal pour déplacer une tour de taille $n$ de A à C sera :

1. `hanoï(A, B, C, n-1)`{.language-}
2. déplace le disque restant en A sur l'emplacement C
3. `hanoï(B, C, A, n-1)`{.language-}

On obtient alors l'algorithme optimal suivant, en considérant que les tours sont des listes :

```python
A = list(range(5, -1, -1))
B = []
C = []

def hanoi(départ, arrivée, intermédiaire, n):
    if n == 0:
        return
    hanoi(départ, intermédiaire, arrivée, n-1)
    disque = départ.pop()
    arrivée.append(disque)
    print(A, B, C)
    hanoi(intermédiaire, arrivée, départ, n-1)

print(A, B, C)
hanoi(A, C, B, len(A))
```

On a montré que notre stratégie était optimale. Comptons le nombre d'appels récursif. Il suit l'équation de récurrence :

<div>
$$
C(n) = 2 + C(n-1) + C(n-1) = 2 + 2\cdot C(n-1)
$$
</div>

Et la terminaison : $C(0) = 0$

On obtient facilement l'expression, pour $n\geq 1$ :

<div>
$$
C(n) = \sum_{i=1}^n2^i + 2\cdot C(0) = \sum_{i=1}^n2^i
$$
</div>

La somme des $n>0$ premières puissances de 2 est à savoir facilement retrouver (c'est [une série géométrique](https://fr.wikipedia.org/wiki/S%C3%A9rie_g%C3%A9om%C3%A9trique#Terme_g%C3%A9n%C3%A9ral)) et vaut $2^{n+1}-2$.

## Suppression de valeurs

La structure de donnée utilisée ici est la **_liste_**. On considérera que :

- la création d'une liste vide se fait en $\mathcal{O}(1)$ opérations,
- l'ajout d'un élément en fin de liste se fait en $\mathcal{O}(1)$ opérations,
- lire un élément d'une liste se fait en $\mathcal{O}(1)$ opérations.

### Suppression d'une valeur

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

#### complexité de l'algorithme 1

On considère que la création d'une liste et l'ajout d'un élément en fin de liste sont des opérations en $\mathcal{O}(1)$ opérations. De là, notre algorithme est en $\mathcal{O}(n)$ opérations où $n$ st la taille de la liste `L`{.language-}.

#### preuve de l'algorithme 1

L'algorithme va parcourir la liste et ajouter un à un à `L2`{.language-} tous les éléments de `L`{.language-} différents de `val`{.language-}. Notre invariant de boucle pourrait donc être : à la fin de l'itération $i$ `L2`{.language-} est la restriction de `L[:i]`{.language-} aux valeurs différentes de `val`{.language-}.

- **initialisation** : à la fin de la première itération ($i=1$), `L2`{.language-} est vide si `x = L[0]`{.language-} vaut `val`{.language-} et vaut `[x]`{.language-} sinon. Ok.
- **récurrence** : On suppose la propriété vraie à la fin de l'itération $i$. L'itération $i+1$ a considéré $x = L[i]$. Notons `L2'`{.language-} la valeur de `L2`{.language-} à la fin de l'itération $i+1$. Au début de l'itération $i+1$, par hypothèse de récurrence, `L2`{.language-} est la restriction de `L[:i]`{.language-} aux valeurs différentes de `val`{.language-}. La restriction de `L[:i+1]`{.language-} aux valeurs différentes de `val`{.language-} est alors soit égal à `L2`{.language-} si `L[i] = val`{.language-} soit `L2 + L[i]`{.language-} sinon. C'est exactement ce que vaut `L2'`{.language-}.

A la fin de la dernière itération, `L2`{.language-} vaut donc la restriction de `L[:n]`{.language-} (avec `n = len(L)`{.language-}) aux valeurs différentes de val.

### Suppression d'une valeur in-place

On échange l'élément à supprimer avec le dernier de la liste puis on pop.

```text
Nom : Algorithme-1'
Entrées :
    val : une valeur
    L : une liste de n valeurs
Programme :
    i = 0
    k = n - 1
    tant que i <= k:
    si L[i] == val
        échange L[i] et L[k]
        supprime le dernier élément de L
        k = k - 1
    sinon:
        i = i + 1
```

La preuve et la complexité de l'algorithme 1' est identique à celle de l'algorithme 1.

## Suppression de doublons

Même structure que pour l'exercice précédent.

La structure de donnée utilisée ici est la **_liste_**. On considérera que :

- la création d'une liste vide se fait en $\mathcal{O}(1)$ opérations,
- l'ajout d'un élément en fin de liste se fait en $\mathcal{O}(1)$ opérations,
- lire un élément d'une liste se fait en $\mathcal{O}(1)$ opérations.

### Suppression de doublon en conservant l'ordre

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

#### complexité de l'algorithme 2

Commençons par compter le nombre de fois où la boucle `tant que`{.language-} sera exécutée. `L`{.language-} est modifiée à chaque fin de boucle `L = algorithme-1(L, x)`{.language-} avec `x = L[0]`{.language-}. Comme l'algorithme de la question 1 rend la restriction de de `L`{.language-} aux valeurs différentes de `x`{.language-}, elle va forcément être strictement plus petite (puisque `x=L[0]`{.language-} il est forcément dans la liste) : la longueur de la liste diminue strictement à chaque itération, on ne peut y rentrer que la longueur de `L`{.language-} initiale fois.

La seule ligne de l'algorithme qui n'est pas de complexité $\mathcal{O}(1)$ est : `L = algorithme-1(L, x)`{.language-}. Sa complexité est égale à une affectation ($\mathcal{O}(1)$) plus la complexité de l'algorithme de la question 1, qui vaut de l'ordre de la taille de la liste passée en entrée.

Cette taille diminue strictement à chaque itération : on peut utiliser l'astuce du cours pour ne garder que la complexité la plus importante, c'est à dire $\mathcal{O}(len(L))$ avec `L`{.language-} la liste initiale.

Notre complexité est donc de l'ordre : $\mathcal{O}(1) + A * (\mathcal{O}(1) + B)$ où :

- A est le nombre de fois où l'on rentre dans la boucle tant que : $\mathcal{O}(len(L))$
- B est la complexité maximale de l'algorithme de la question 1 : $\mathcal{O}(len(L))$

Notre algorithme est de complexité : $\mathcal{O}(len(L)^2)$

#### preuve algorithme 2

La liste `L`{.language-} contient $k$ valeurs différentes que l'on note $v_1, \dots v_k$ dans l'ordre de la liste (le 1er indice où l'on rencontre $v_i$ est strictement plus petit que le 1er indice où l'on rencontre $v_j$ si $i < j$).

Notre invariant de boucle sera : au bout de la $i$ème itération :

- $L2 = [v_1, \dots, v_i]$.
- `L`{.language-} vaut la restriction de `L`{.language-} initiale aux valeurs différentes de $v_1$ jusqu'à $v_i$.

- **initialisation** : comme $v_1= L[0]$ notre invariant est vrai puisque l'algorithme 1 rendra la restriction de `L`{.language-} initiale aux éléments différents de $v_1$.
- **récurrence** : On suppose la propriété vraie à la fin de l'itération $i$. Au début de l'itération $i+1$, on a par hypothèse de récurrence que $L2 = [v_1, \dots, v_i]$ et que `L`{.language-} vaut la restriction de la liste `L`{.language-} initiale aux valeurs différentes de $v_1$ jusqu'à $v_i$. Donc $L[0] = v_{i+1}$ et tout se passe comme à la 1ère itération.

A la fin de l'algorithme, notre invariant est toujours juste : $L2 = [v_1, \dots, v_k]$

### Suppression de doublon d'une liste ordonnée

Il suffit de parcourir tous les éléments de `L`{.language-} dans l'ordre :

```text
Nom : Algorithme-2'
Entrées :
    L : une liste de n valeurs
Programme :
    création d’une liste L2 contenant le premier élément de L
    pour i allant de 1 à n-1:
        si L[i] != L[i-1]:
            ajoute L[i] à la fin de L2
    Retour L2
```

#### complexité de l'algorithme 2'

Clairement en $\mathcal{O}(n)$

#### preuve de l'algorithme 2'

L'invariant de boucle et sa preuve est identique à celle de la preuve de l'algorithme 2 en tenant compte du fait que `L`{.language-} est trié.

### Suppression de doublon d'une liste sans ordre

On commence par trier la liste on utilise l'algorithme de la question précédente. Ceci fait passer la complexité de $\mathcal{O}(len(L)^2)$ à $\mathcal{O}(len(L)\log(len(L)))$

## Triangle de Pascal

### Coefficient binomiaux récursif

```python
def comb_rec(n, p):

    if p <= 1 or n ==p :
        return 1
    else:
        return comb_rec(n-1, p-1) + comb_rec(n-1, k)
```

### Coefficient binomiaux itératif et $\mathcal{O}(n^2)$ en mémoire

On stocke une matrice triangulaire inférieure que l'on construit ligne à ligne.

```python
def comb_iter(n, p):
    C = [[1]]

    for i in range(1, n):
        C.append([])
        for j in range(i):
            c_i_j = C[i-1][j-1] + C[i-1][j]
            C[-1].append(c_i_j)

    return C[-1][p-1]
```

### Coefficient binomiaux itératif et $\mathcal{O}(n)$ en mémoire

On remarque que seule la dernière ligne est importante dans le calcul.

```python
def comb_iter2(n, p):
    C = [1]
    for i in range(1, n):
        C.append(0)
        r = C[0]
        for j in range(1, i):
            tempo = C[j]
            C[j] += r
            r = tempo

    return C[p-1]
```

## Compteur binaire

La complexité va dépendre du nombre d'éléments dans la liste en entré. Notons $N = len(n)$.

On remarque (facilement) que cette complexité vaut $C(N) = K \cdot \mathcal{O}(1)$ où $K$ est le nombre de fois où l'on rentre dans la boucle.

- complexité max : parcourt toute la liste (pour une liste uniquement constituée): $\mathcal{O}(N)$
- complexité min : parcourt 1 seul élément de la liste (pour une liste se terminant par un 0): $\mathcal{O}(1)$

Séparons les $2^N$ nombres possibles en classes selon le nombre d'itérations dans la boucle :

- dernier élément vaut 0 : 0 itération. Vrai pour $2^N/2$ nombres. Probabilité de 1/2.
- derniers éléments valent `[0, 1]`{.language-} : 1 itération. Vrai pour $(2^N/2)/2 = 2^N/4$ nombres. Probabilité de 1/4.
- derniers éléments valent `[0, 1, 1]`{.language-} : 2 itérations. Vrai pour $(2^N/4)/2 = 2^N/8$ nombres. Probabilité de 1/8.
- ...
- derniers éléments valent `[0] + i *[1]`{.language-} : i itérations. Vrai pour $(2^N/4)/2 = 2^N/2^{i+1}$ nombres. Probabilité de 1/2^{i+1}.
- le premier élément vaut 0 et tous les autres valent 1 : $N-1$ itérations Vrai pour 1 nombre. Probabilité de 1/2^{N}.

Le nombre moyen d'itérations dans la boucle vaut alors :

<div>
$$
W_\text{moy}(N) = \mathcal{O}(1) \cdot \sum_{i=0}^{N-1} i \cdot \frac{1}{2^{i+1}}
$$
</div>

### Vérification expérimentale

```python
def successeur(n):
    K = 0

    while i >= 0 and (n[i] == 1):
        K += 1

        n[i] = 0
        i -= 1

    if i >= 0:
        n[i] = 1

    return K


def tous(N):

    n = [0] * N
    total = 0
    for i in range(2**N):
        total += successeur(n)
        print(n)

    return total / 2 ** N


x = tous(5)
print(x)

```

## Cols

### Existence

On donne trois preuves possibles

#### En reprenant la définition

Si la première condition ($i=0$) est vérifiée, le tableau contient un col. On la suppose donc non vérifiée : $T[0] > T[1]$. De même, si la seconde condition ($i=n-1$) est vérifiée, le tableau contient également un col. Supposons la donc également non vérifiée : $T[n-2] < T[n-1]$.

Les deux conditions précédentes montrent qu'il existe $n-1 > i^\star > 0$ le plus petit indice tel que $T[i^\star] \leq T[i^\star +1]$. On a alors : $T[i^\star -1] > T[i^\star ] \leq T[i^\star +1]$ et $i^\star$ est un col.

#### Une astuce

Un tableau d'entier possède forcément un élément minimum. Il existe donc $i^\star$ tel que $T[i^\star] \leq T[i]$ pour tout $0 \leq i < n$. De là :

- soit $i^\star = 0$ et $T[i^\star] \leq T[1]$
- soit $i^\star = n-1$ et $T[i^\star] \leq T[n-2]$
- soit $0 < i^\star < n-1$ et $T[i^\star] \leq \min(T[i^\star-1], T[i^\star+1])$

Simple et efficace, non ?

#### Par récurrence

On montre par récurrence sur la taille $n$ du tableau qu'il existe toujours un col.

1. Initialisation. Si $n=2$ soit $T[0] \leq T[1]$ soit $T[0] \geq T[1]$ (ce qui est équivalent pour $n=2$ à $T[n-1] \leq T[n-2]$). Ces deux cas correspondent aux deux premières possibilités pour un col
2. on suppose la propriété vrai pour $n \geq 2$. Et on se donne un tableau $T$ de taille $n+1$.
3. l'hypothèse de récurrence stipule que le tableau $T'$ constitué des $n$ premières cases de $T$ ($T'= T[:-1]$) possède un col, disons à l'indice $i^\star$. 3 cas sont possibles :
   1. $i^\star = 0$ et $T'[0] \leq T'[1]$ ce qui implique $T[0] \leq T[1]$ : $i^\star$ est aussi un col pour $T$
   2. $0 < i^\star < n-1$ et $T'[i^\star] \leq \min(T'[i-1], T'[i+1])$ ce qui implique $T[i^\star] \leq \min(T[i^\star-1], T[i^\star+1])$ : $i^\star$ est aussi un col pour $T$
   3. $i^\star = n-1$ et $T'[n-1] \leq T'[n-2]$ ce qui implique $T[n-1] \leq T[n-2]$. On conclut en remarquant que :
      1. soit $T[n] \geq T[n-1]$ et $T[i^\star] \leq \min(T[i^\star-1], T[i^\star+1])$ : $i^\star$ est aussi un col pour $T$
      2. soit $T[n] < T[n-1]$ et $n$ est un col pour $T$.

### Découverte

La preuve de la 1ère question montrant qu'il existe forcément un col, l'algorithme suivant qui mime directement la définition (lignes 2-3 : 1ère condition, lignes 5-6 : 2ème condition et lignes 8-10 la troisième condition) trouvera forcément un col :

```python#
def trouve(T):
    if T[0] <= T[1]:
        return 0

    if T[-1] <= T[-2]:
        return len(T) - 1

    for i in range(1, len(T) - 1):
        if T[i] <= min(T[i-1], T[i + 1]):
            return i

```

Sa complexité dans le cas le pire a lieu pour les tableaux dont le premier et seul col se trouve à l'avant dernier indice (comme pour la liste $[5, 4, 3, 2, 1, 2]$ par exemple), forçant l'algorithme à :

- faire échouer le 1er test de la ligne 2 en $\mathcal{O}(1)$ opérations
- faire échouer le 2er test de la ligne 5 en $\mathcal{O}(1)$ opérations
- faire les $\mathcal{O}(n)$ itérations de la boucle for en :
  - faisant échouer tous les tests sauf le dernier $\mathcal{O}(1)$ opérations
  - réussissant le dernier test et en faisant un retour de fonction en $\mathcal{O}(1)$ opérations

La complexité totale maximale est alors :

$$
C(n) = \mathcal{O}(1) + \mathcal{O}(1) + \mathcal{O}(n) \cdot (\mathcal{O}(1) + \mathcal{O}(1)) = \mathcal{O}(n)
$$

On peut aussi utiliser la preuve précédente et _simplifier_ la boucle `for`{.language-} en gardant la même complexité :

```python
def trouve(T):
    if T[0] <= T[1]:
        return 0

    if T[-1] <= T[-2]:
        return len(T) - 1

    for i in range(1, len(T) - 1):
        if T[i] <= T[i + 1]:
            return i

```

### Rapidité

La preuve d'existence du 1 montre que pour tout $i + 1 < j$, si $T[i] > T[i+1]$ et $T[j] > T[j-1]$, alors il existe un indice $i < k < j$ tel que $k$ soit un col de la matrice.

L'invariant de boucle de la boucle `while`{.language-} est alors :

{% note "**invariant**" %}
A la fin de chaque itération de la boucle `while`{.language-}, soit :

- `T[milieu]`{.language-} est un col
- `T[milieu]`{.language-} n'est pas un col et :
  - `début + 1 < fin`{.language-}
  - `T[début] > T[début+1]`{.language-} et `T[fin] > T[fin-1]`{.language-}
    {% endnote %}

A la fin de la première itération, on a soit :

- `T[milieu] <= min(T[milieu - 1], T[milieu + 1])`{.language-} et `milieu`{.language-} est un col
- `fin' = milieu`{.language-} et `début' = début`{.language-} si `T[milieu] > T[milieu -1]`{.language-}. Comme initialement `0 = début + 1 < fin = len(T) - 1`{.language-} on a également `milieu - 1 > début`{.language-} puisque `T[0] > T[1]`{.language-} et l'invariant est vérifié.
- `fin' = fin`{.language-} et `début' = milieu`{.language-} si `T[milieu] <= T[milieu -1]`{.language-} et `T[milieu] > T[milieu + 1]`{.language-}. Comme `0 = début + 1 < fin = len(T) - 1`{.language-} on a également `milieu + 1 < fin`{.language-} puisque `T[-1] > T[-2]`{.language-} et l'invariant est vérifié.

La même démonstration fonctionne à l'identique à la fin de l'itération $i+1$ si l'invariant est vrai à la fin de l'itération $i$.

Comme `fin - début >= 0` et diminue strictement à chaque itération de la boucle `while`{.language-}, il arrivera **forcément** un moment où `milieu`{.language-} sera un col.

### Complexité

La procédure de la boucle `while`{.language-} est identique à la recherche dichotomique puisque l'on se place toujours au milieu de l'espace de recherche. Le cours nous indiquant que la complexité de la recherche dichotomique est $\mathcal{O}(\log_2(n)) = \mathcal{O}(\ln(n))$, on en conclut que l'algorithme `trouve_vite(T)`{.language-} est également en $\mathcal{O}(\ln(n))$ opérations.

### Complexité du problème

Il existe des tableaux ayant tous un unique col en position $i$ pour tout $0 \leq i < n$ (prenez les tableaux $[0, -1, \dots, -i, -i+1, -i +2, \dots, -i + (n - i - 1)]$). Tout algorithme trouvant les col des tableaux doit donc pouvoir distinguer parmi $n$ cas : il est au moins de complexité $\mathcal{O}(\log_2(n)) = \mathcal{O}(\ln(n))$.

Comme l'algorithme `trouve_vite(T)`{.language-} est de complexité $\mathcal{O}(\ln(n))$, c'est borne min est atteinte.

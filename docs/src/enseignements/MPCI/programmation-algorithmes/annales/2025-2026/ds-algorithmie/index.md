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

- au minimum on ne fait qu'une seule itération pour la boucle `pour chaque`{.language-} et pour la boucle `tant que`{.language-}. Comme les autres instructions sont toutes en $\mathcal{O}(1)$, la complexité minimale est alors de $\mathcal{O}(1)$. Ceci arrive si `a`{.language-} et `b`{.language-} sont de même taille mais ne commencent pas par le même lettre.
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

##### 1.2.2

Comme la complexité de l'algorithme de la question 1.1.4 est en $\mathcal{O}(a.\text{\small longueur} \cdot b.\text{\small longueur})$, la complexité problème est :

- $\Omega(a.\text{\small longueur} + b.\text{\small longueur})$.
- $\mathcal{O}(a.\text{\small longueur} \cdot b.\text{\small longueur})$

#### 1.3 Complexité en moyenne

##### 1.3.1

Si les caractères sont équiprobables alors la position dans la chaîne de caractères importe peu. La probabilité que 2 caractères de $a$ et de $b$ soient égaux est donc la même que la probabilité de tirer deux fois le même caractère : c'est $\frac{1}{\vert \mathcal{A} \vert}$ où $\mathcal{A}$ est l'ensemble des caractères possibles.

##### 1.3.2

On note $p$ la probabilité de tirer avec remise deux lettres identiques. La probabilité que $a[i + j] == b[j]$ pour tout $0 \leq j < k$ et que $a[i + k] \neq b[k]$ vaut alors (puisqu'il y a équiprobabilité) : $p(k) = p^{k}(1-p)$

Pour une position $i$ donnée dans l'algorithme, le nombre moyen de passage dans la boucle `tant que`{.language-} vaut alors :

<div>
$$
\sum_{k=0}^{b.\text{\small longueur} - 1} (k + 1) \cdot p^{k}(1-p) = \frac{1}{p} \cdot \sum_{k=1}^{b.\text{\small longueur}} (k) \cdot p^{k}(1-p) \leq \frac{1}{1-p}
$$
</div>

Comme :

- $p$ est une constante le nombre moyen de passage dans la boucle à $i$ fixé est en $\mathcal{O}(1)$
- chaque passage dans la boucle comptera pour $\mathcal{O}(1)$ opération

On on en conclut que pour $i$ fixé il y a en moyenne $\mathcal{O}(1)$ opérations d'effectuées.

Enfin, comme $0 \leq i \leq a.\text{\small longueur} - b.\text{\small longueur}$ i y a $\mathcal{O}(a.\text{\small longueur} - b.\text{\small longueur})$ valeur différentes de $i$ et donc la complexité moyenne vaut : $\mathcal{O}(a.\text{\small longueur} - b.\text{\small longueur})$

#### Code python

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

### Exercice 2

#### 2.1 Principe

##### 2.1.1

Pour une position de $i$ donnée si $a[i + j] = b[j]$ pour tout $0 \leq j < m$ $b$ est bien une sous-chaîne de $a$ en position $i$. Sinon :

- soit $a[i + m -1]$ n'est pas dans $b$ : $b$ ne peut-être une sous-chaîne de $a$ pour tout $i'$ tel que $i \leq i' < i + m$
- soit $a[i + m -1] = b[m-1]$ et n'est pas dans $b[:-1]$ : $b$ ne peut-être une sous-chaîne de $a$ pour tout $i'$ tel que $i < i' < i + m$
- soit $a[i + m -1]$ est dans $b[:-1]$ et la première position plus grande que $i$ où $b$ pourra être une sous-chaîne de $a$ sera celle où on fera correspondre $a[i + m -1]$ avec sa plus grande position dans $b$.


##### 2.1.2

Contrairement à l'algorithme naïf l'indice $i$ peut augmenter de plus que 1 unité. Il peut même augmenter de $m$ si le dernier élément de $a$ n'est pas dans $b$.

#### Code python


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
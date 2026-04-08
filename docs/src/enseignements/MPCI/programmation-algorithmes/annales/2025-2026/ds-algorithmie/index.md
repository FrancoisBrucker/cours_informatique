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

Si les caractères sont équiprobables alors la position dans la chaîne de caractère importe peut. La probabilité que 2 caractères de $a$ et de $b$ soient égaux est donc la même que la probabilité de tirer deux fois le même caractère : c'est $\frac{1}{\vert \mathcal{A} \vert}$ où $\mathcal{A}$ est l'ensemble des caractères possibles.

##### 1.3.2

> TBD
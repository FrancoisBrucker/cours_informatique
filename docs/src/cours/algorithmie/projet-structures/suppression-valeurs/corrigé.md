---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La structure de donnée utilisée ici est la **_liste_**. On considérera que :

- la création d'une liste vide se fait en $\mathcal{O}(1)$ opérations,
- l'ajout d'un élément en fin de liste se fait en $\mathcal{O}(1)$ opérations,
- lire un élément d'une liste se fait en $\mathcal{O}(1)$ opérations.

## Suppression d'une valeur

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

### complexité de l'algorithme 1

On considère que la création d'une liste et l'ajout d'un élément en fin de liste sont des opérations en $\mathcal{O}(1)$ opérations. De là, notre algorithme est en $\mathcal{O}(n)$ opérations où $n$ st la taille de la liste `L`{.language-}.

### preuve de l'algorithme 1

L'algorithme va parcourir la liste et ajouter un à un à `L2`{.language-} tous les éléments de `L`{.language-} différents de `val`{.language-}. Notre invariant de boucle pourrait donc être : à la fin de l'itération $i$ `L2`{.language-} est la restriction de `L[:i]`{.language-} aux valeurs différentes de `val`{.language-}.

- **initialisation** : à la fin de la première itération ($i=1$), `L2`{.language-} est vide si `x = L[0]`{.language-} vaut `val`{.language-} et vaut `[x]`{.language-} sinon. Ok.
- **récurrence** : On suppose la propriété vraie à la fin de l'itération $i$. L'itération $i+1$ a considéré $x = L[i]$. Notons `L2'`{.language-} la valeur de `L2`{.language-} à la fin de l'itération $i+1$. Au début de l'itération $i+1$, par hypothèse de récurrence, `L2`{.language-} est la restriction de `L[:i]`{.language-} aux valeurs différentes de `val`{.language-}. La restriction de `L[:i+1]`{.language-} aux valeurs différentes de `val`{.language-} est alors soit égal à `L2`{.language-} si `L[i] = val`{.language-} soit `L2 + L[i]`{.language-} sinon. C'est exactement ce que vaut `L2'`{.language-}.

A la fin de la dernière itération, `L2`{.language-} vaut donc la restriction de `L[:n]`{.language-} (avec `n = len(L)`{.language-}) aux valeurs différentes de val.

## Suppression d'une valeur in-place

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

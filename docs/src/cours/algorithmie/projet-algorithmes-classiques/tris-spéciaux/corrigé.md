---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Tri par paquets (bucket sort)

On peut utiliser l'algorithme suivant, qui modifie le tableau passé en paramètre :

<span id="algorithme-tri-paquet"></span>

```pseudocode
algorithme tri_paquet(E: [entier], f:(entier) → entier) → ∅:
    m ← max(f(x) | x de E)
    T ← un nouveau tableau d'entier de taille m + 1
    T[:] ← ∅  # ou m + 1 si on a pas accès à ∅ pour un tableau d'entiers

    pour chaque x de E:
        T[f(x)] ← x
    
    i ← 0
    pour chaque x de T:
        si x ≠ ∅:
            E[i] ← x
            i ← i + 1
```

La complexité est en $\mathcal{O}(m)$ en temps **et** en mémoire.

Cet algorithme marche car $f$ est une injection, tout éléments de $E$ sera dans T à un indice différent des autres.

Si l'on veut trier $n$ entiers deux à deux différents, on utilise la fonction identité et la complexité est en $\mathcal{O}(\max(E))$.

{% attention %}
Il n'y **aucune** relation entre $n$ et $\max(E)$. On peut par exemple tenter de trier le tableau $[1, 2^{10000000}]$, la complexité de notre algorithme sera de $2^{10000000}$ et non pas de 2.

Ce n'est donc **pas** un algorithme linéaire...
{% endattention %}

Cet algorithme est utile si on doit trier des objets via une fonction $f: \mathcal{E} \to [0, m[$ où $m$ borné pas trop grand. C'est souvent le cas lorsque l'on utilise des données complexes, pensez à un tableau excel où nos données sont les lignes et l'index le numéro de la ligne (ou une colonne spécifique dont la valeur va de 1 au nombre de lignes).

Si l'on veut trier des entiers pouvant être égaux, on peut utiliser l'algorithme suivant qui compte dans $T[i]$ le nombre de fois où $i$ est présent dans $E$.

```pseudocode
algorithme tri_paquet(E: [entier]) → ∅:
    m ← max(x | x de E)
    T ← un nouveau tableau d'entier de taille m + 1
    T[:] ← 0  # ou m + 1 si on a pas accès à ∅ pour un tableau d'entiers

    pour chaque x de E:
        T[x] ← T[x] + 1
    
    i ← 0
    pour x allant de 0 à m:
        tant que T[x] > 0:
            E[i] = x
            i ← i + 1
            T[x] ← T[x] - 1

```

Ce tri est très efficace si les nombres ne sont pas trop grand devant $n$. Ce qui est souvent le cas en pratique. Rappelez-vous en, on s'en sert parfois dans des problèmes algorithmiques.

## Tri par base

{% lien %}
[Tri par pase](https://fr.wikipedia.org/wiki/Tri_par_base)
{% endlien %}

L'algorithme suivant mime exactement le procédé décrit dans le sujet. Nos données étant des tableaux de bits, l'entrée de l'algorithme est un tableau de tableaux de bit. Cela s'écrit : `[[bit]]`{.language-} :

<span id="algorithme-tri-base"></span>

```pseudocode
algorithme tri_base(T: [[bit]]) → ∅
    L0 ← un tableau de T.longueur [bit]
    i0 ← 0

    L1 ← un tableau de T.longueur [bit]
    i1 ← 0

    pour i allant de 1 à T.longueur:
        pour chaque x de T:
            si x[-i] == 0:
                L0[i0] ← x
                i0 ← i0 + 1
            sinon:
                L1[i1] ← x
                i1 ← i1 + 1
        pour j allant 0 à i0-1:
            T[j] ← L0[j]
        pour j allant 0 à i1-1:
            T[j + i0] ← L1[j]
```

On prouve cet algorithme par invariant de boucle.

> **Invariant de boucle** : À la fin de la ième itération, $T$ est trié si on considère uniquement les i derniers bits de chaque élément.

1. initialisation : à la fin de la première boucle il est clair que les élément finissant par 0 sont placés avant les éléments se finissant par 1.
2. récursion : si l'invariant de boucle est vrai à la fin de la i-1 ème itération, les éléments de L0et de L1 seront trié si on considère uniquement les i derniers bits de chaque élément. Comme le $-i$ bit des éléments de L0 vaut 0 et le $-i$ bit des éléments de L1 valent 1 tous les éléments de L0 sont inférieur aux éléments de L1 et en les concaténant on a bien que les $i$ derniers bit des éléments de T sont triées.
3. à la fin des `T.longueur`{.language-} itérations, l'invariant de boucle montre que les éléments de $T$ sont bien triés.

En notant $m$ la taille des tableaux en entrée et $n$ le nombre de données à trier, on a clairement une complexité de $\mathcal{O}(nm)$.

Si la taille des entiers est fixée, ce qui est le cas au niveau du processeur où tous les entiers sont codés sur 64bits, ce tri est le plus efficace possible : il est linéaire.

{% attention %}
Il n'y **aucune** relation entre $n$ et $m$. On peut par exemple tenter de trier les tableaux de taille $m=2^n$, la complexité de notre algorithme sera exponentielle.

Ce n'est donc **pas** un algorithme linéaire...
{% endattention %}

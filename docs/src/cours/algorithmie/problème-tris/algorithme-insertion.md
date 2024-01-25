---
layout: layout/post.njk 
title: "Algorithme du tri par insertion"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le tri par insertion est un exemple d'algorithmes dont les complexité minimum et maximum sont très différentes. Il est alors nécessaire de calculer la complexité en moyenne pour avoir une idée de la complexité attendu pour un tableau aléatoire (*ie* inconnu).

Cet algorithme est une extension de [l'algorithme `est_trie`{.language-}](../reconnaissance/#algo-est-trie){.interne}. Plutôt que de rendre `False`{.language-} il répare. L'algorithme `est_trie`{.language-} répond `False`{.language-} au plus petit `i`{.language-} tel que `T[i] < T[i-1]`{.language-}. On est alors dans le cas où :

- `T[:i]`{.language-} est trié
- et `T[i] < T[i-1]`{.language-}

Pour que l'on puisse continuer, il faut s'arranger pour que `T[:i+1]`{.language-} soit trié. Pour cela, on peut utiliser le fait que `T[:i+1]`{.language-} est trié si et seulement si :

- `T[1] >= T[0]`{.language-}
- `T[2] >= T[1]`{.language-}
- ...
- `T[i] >= T[i-1]`{.language-}

Dans notre cas, toutes les conditions sont vérifiées sauf la dernière. Si l'on échange `T[i]`{.language-} et `T[i-1]`{.language-} toutes les conditions seront vérifiées sauf peut-être l'avant-dernière. Si elle n'est pas vérifiée on peut échanger `T[i-1]`{.language-} et `T[i-1]`{.language-} et alors toutes les conditions seront vérifiées sauf peut-être l'avant-avant-dernière, que l'on peut à nouveau échanger, et ainsi de suite jusqu'à ce que toutes les conditions soient vérifiées.

Cette analyse (ce n'est pas encore une preuve formelle) nous permet de dégager le principe suivant :

On vérifie itérativement que `T[i] >= T[i-1]`{.language-} et si ce n'est pas le cas on fait *remonter* `T[i]`{.language-} par échanges successifs à la première place où il sera plus grand que le précédent.

Ce qui se traduit en pseudo-code :

```python#
def insertion(T):
    for i in range(1, len(T)):
        j = i
        while (j > 0) and (T[j] < T[j - 1]):
            T[j], T[j - 1] = T[j - 1], T[j]
            j -= 1
```

L'algorithme `insertion`{.language-}, comme l'algorithme `sélection`{.language-}, **modifie** le tableau passé en paramètre.

Pour garantir que `T[j - 1]`{.language-} soit toujours valide (il faut que $j-1 \geq 0$), on place en tête de la condition `(courant < T[j - 1])`{.language-} de la ligne 5 [la sentinelle](https://en.wikipedia.org/wiki/Sentinel_value) `(j > 0)`{.language-}. Les deux conditions étant liées par un `and`{.language-}, python (et tout autre langage de programmation) n'évaluera la seconde condition **que si la première est vérifiée** (un `and`{.language-} ne peut être vrai que si les deux conditions sont vraies. Si la première condition est fausse, il est impossible que le `and`{.language-} soit vrai il est donc inutile de vérifier la seconde condition).

{% note "**À retenir**" %}
La technique [des sentinelles](https://en.wikipedia.org/wiki/Sentinel_value) est très pratique, cela vaut le coup de la connaître.
{% endnote %}

## <span id="fonctionnement-insertion"></span> Fonctionnement

Tout comme pour l'algorithme de tri par sélection, on vérifie que l'algorithme fonctionne pour :

- un petit tableau trié : `[1, 2, 3]`{.language-}
- un petit tableau non trié où le plus petit est en dernière place : `[3, 2, 1]`{.language-}

## <span id="preuve-insertion"></span> Preuve

Le principe de programmation du tri par insertion est correct puisque `est_trie`{.language-} est prouvé. Mais il faut vérifier qu'il est bien mis en œuvre dans l'algorithme.

On a ici deux boucles imbriquée (lignes 2 et 5), il nous faut donc a priori deux invariants de boucles, le second (du `while`{.language-}) nous servant à prouver le premier (du `for`{.language-})

Comme l'algorithme du tri par insertion mime l'algorithme de reconnaissance, le premier invariant, celui de la boucle `for`{.language-} de la ligne 2 va être le même :

{% note "**Invariant de boucle**" %}
À la fin d'un itération de la boucle `for`{.language-} de la ligne 2, les $i + 1$ premiers éléments du tableau sont triés.
{% endnote %}

Pour prouver cet invariant, il nous faut comprendre ce que fait la boucle `while`{.language-} de la ligne 5, c'est à dire lui trouver un invariant.

{% note "**Invariant de la boucle `while`{.language-}**" %}
Chaque itération de la boucle `while`{.language-} va échanger les éléments placées en $j-1$ et $j$ et décrémenter $j$ jusqu'à ce que soit $j=0$ soit $T[j-1] \leq T[j]$. On a donc l'invariant :

> A la fin de chaque itération de la boucle `while`{.language-} $T[j] \leq T[j+1]$ si $j <i$

{% endnote %}
{% details "preuve", "open" %}

Cet invariant est clairement vérifié.

{% enddetails %}

On peut donc maintenant démontrer l'invariant de la boucle `for`{.language-} :

{% note "**Invariant de la boucle `for`{.language-}**" %}
> A la fin d'un itération de la boucle `for`{.language-} de la ligne 2, les $i + 1$ premiers éléments du tableau sont triés.

{% endnote %}
{% details "preuve", "open" %}

On a $i = 1$ pour la première itération donc à l'issue de la boucle while :

- soit $j=i=1$ et $T[0] \leq T[1]$ (car la boucle s'est arrêtée)
- soit $j=0$ et $T[0] \leq T[1]$ (invariant de boucle)

Dans les 2 cas, les 2 premiers éléments de $T$ sont triées. L'initialisation de l'invariant est Ok.

On suppose l'invariant vrai à la fin de la $i-1$ ème boucle et on regarde à la fin de la $i$ boucle.

La $i$ ème itération de la boucle `for`{.language-} (ligne 2), a fonctionné ainsi :

- ligne 3 : on a : `T[:i+1] = T[:i] + [T[j]]`{.language-} ($j = i$)
- à la sortie de la boucle `while`{.language-}, en notant `T`{.language-} le tableau avant la boucle `while`{.language-} et `T'`{.language-} le tableau en fin de `while`{.language-}, on a :
  1. `T'[:i+1] = T[:j] + [T[j]] + T[j:i]`{.language-}
  2. `T[:j]`{.language-} trié (invariant de la boucle `for`{.language-}) et `T[j] >= T[j-1]`{.language-} (car on est sorti de la boucle `while`{.language-})
  3. `T[j:i]`{.language-} trié (invariant de la boucle `for`{.language-}) et `T[j] < T[j+1]`{.language-} (invariant de la boucle `while`{.language-})

Les constatations précédentes nous montrent que $T'[:i+1]$ est trié, ce qui termine la preuve de l'invariant de la boucle `for`{.language-}.
{% enddetails %}

On conclut la preuve de l'algorithme insertion en constatant que l'invariant de la boucle `for`{.language-} est vrai en sortie de boucle où  $i=n-1$ : les $n$ premier éléments de $T$ sont triés.

## <span id="complexités-insertion"></span> Complexités

Ligne à ligne :

1. appel de fonction : $\mathcal{O}(1)$
2. $n-1$ itérations, avec $n$ la taille du tableau
3. affectation d'une variable et récupération d'un élément d'un tableau : $\mathcal{O}(1)$
4. affectation d'une variable : $\mathcal{O}(1)$
5. $K$ itérations ($K$ inconnu) et deux tests en $\mathcal{O}(1)$ pour chaque itération
6. affectation d'une variable et récupération d'un élément d'un tableau : $\mathcal{O}(1)$
7. une soustraction et une affectation : $\mathcal{O}(1)$
8. affectation d'une variable et récupération d'un élément d'un tableau : $\mathcal{O}(1)$

Comme $K$ n'est pas constant pour chaque itération de la boucle `for`{.language-} il faut regarder les valeurs extrêmes que peut prendre $K$ :

- si le tableau est déjà trié : on ne rentre jamais dans la boucle `while`{.language-} : $K = 0$ pour chaque itération.
- si le tableau est trié à l'envers : pour la $i$-ème itération de la boucle `for`{.language-}, on aura $K=i$. C'est de plus le maximum théorique possible ($j=i$ initialement et j décroît de 1 à chaque itération de la boucle `while`{.language-}).

On a donc 2 cas extrêmes pour le calcul :

1. $K = 0$ à chaque itération
2. $K$ croit de $1$ à $n-1$ à chaque itération : [la règle de croissance](../../complexité-calculs/règles-de-calcul#règle-croissance){.interne} nous indique qu'on peut considérer que $k=n-1$ pour le calcul de la complexité

Ce qui donne une complexité de :

<div>
$$
\begin{array}{lcl}
C & = & \mathcal{O}(1) + \\
&& (n-1) \cdot (\\
&& \mathcal{O}(1) + \\
&& \mathcal{O}(1) + \\
&& K \cdot (\mathcal{O}(1) + \\
&& \mathcal{O}(1) + \\
&& \mathcal{O}(1)) + \\
&& \mathcal{O}(1)) \\
& = & \mathcal{O}(1) + (n-1) \cdot (\mathcal{O}(1) + K \cdot (\mathcal{O}(1))\\
& = & \mathcal{O}(n \cdot (K + 1)) \\
& = & \mathcal{O}(K \cdot n) \\
\end{array}
$$
</div>

{%note %}
La complexité de l'algorithme `insertion`{.language-} est ($n$ est la taille du tableau passé en entrée) :

- la **complexité min** est atteinte pour $k=0$, c'est à dire lorsque le tableau est déjà trié, et vaut $\mathcal{O}(n)$
- la **complexité (max)** est atteinte pour $k=n-1$, c'est à dire lorsque le tableau est trié par ordre décroissant, et vaut $\mathcal{O}(n^2)$

{% endnote %}

La complexité min est différente de la complexité maximale. On va donc calculer la complexité en moyenne pour connaître la complexité pour des données *standard*.
Pour savoir ce que veut dire *standard*, il faut déterminer le modèle de données : prenons le équiprobable.

Cela signifie que pour chaque itération $i$ :

- `T[i]`{.language-} sera bien placé pour une proportion de $\frac{1}{i + 1}$ tableaux
- `T[i]`{.language-} devra être positionné en $i-1$ pour une proportion de $\frac{1}{i + 1}$ tableaux,
- ...
- `T[i]`{.language-} devra être positionné en $i-j$ pour une proportion de $\frac{1}{i + 1}$ tableaux,
- ...
- `T[i]`{.language-} devra être positionné en $0$ pour une proportion de $\frac{1}{i + 1}$ tableaux.

La complexité en moyenne sera donc égale à :

<div>
$$
\begin{array}{lcl}
C_m &=& \mbox{complexité hors boucle for} + \sum_{i=1}^{n-1}(\mbox{complexité hors boucle while} + i \cdot (\mbox{complexité boucle while}))\\
&=& \mathcal{O}(1) + \sum_{i=1}^{n-1} (\mathcal{O}(1) + i \cdot \mathcal{O}(1))\\
&=& \mathcal{O}(1) \cdot \sum_{i=1}^{n-1} i \\
&=& \mathcal{O}(1) \cdot \frac{n(n-1)}{2} \\
&=& \mathcal{O}(n^2)\\
\end{array}
$$
</div>

{% note %}
La **complexité en moyenne** de l'algorithme `insertion`{.language-} est $\mathcal{O}(n^2)$ où $n$ est la taille du tableau passé en entrée.
{% endnote %}

Le cas le meilleur arrive très rarement par rapport au cas le pire (parmi les $n!$ ordres possibles, il y en a très peu qui sont presque triés).

Si l'on change le modèle de données et que l'on considère des tableaux *presque triées*, la complexité en moyenne va être de l'ordre de la complexité minimale, à savoir : $\mathcal{O}(n)$

{% note %}
On utilise le tri par insertion lorsque nos données seront presque toujours déjà triées ou très peu en désordre.
{% endnote %}

Ce calcul de complexité nous permet d'utiliser la règle suivante, qui va se révéler très utile :

{% note %}
Soit $A$ un ensemble de $n$ nombres aléatoires, et $x$ un nombre également aléatoire.
Pour tout $ y \in A$, il y a 50% de chances que $x \leq y$. Il y a donc en moyenne $\frac{n}{2}$ éléments de $A$ qui sont plus grand que $x$.
{% endnote %}

## Optimisation

Une implémentation courante du tri par insertion est la suivante :

```python#
def insertion(T):
    for i in range(1, len(T)):
        courant = T[i]
        j = i
        while (j > 0) and (courant < T[j - 1]):
            T[j] = T[j - 1]
            j -= 1
        T[j] = courant
```

Remarquez qu'elle ne fait pas d'échange à chaque fois. Elle se contente de faire de la place pour l'élément que l'on va insérer en décalant uniquement les valeurs  du tableau. Une fois la place trouvée, il suffit de placer l'élément une fois. Finaud, non ?

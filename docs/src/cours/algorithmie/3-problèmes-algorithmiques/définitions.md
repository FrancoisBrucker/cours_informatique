---
layout: layout/post.njk
title: "Complexité d'un problème algorithmique"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[Un problème algorithmique](../../1-algorithme/problème-preuve/#problème-algorithmique) est une question solvable par un algorithme. 

## Définitions

{% definition %}
La **_Un problème algorithmique_** possède : 
- un nom,
- des paramètres d'entrée,
- une sortie qui doit vérifier des conditions que l'on explicite,
- un algorithme dont les entrée et la sortie satisfont le problème.

{% enddefinition %}

Par exemple :

{% note "**Problème**" %}

- **Nom** : max
- **Entrée** :
  - un tableau d'entiers $T$
- **Sortie** : la valeur valant $\max(\\{T[i] \mid 0\leq i < T.\text{\small longueur}\\})$ ?

{% endnote %}

Le problème _max_ est bien algorithmique puisqu'il existe un algorithme pour le résoudre : [lui par exemple](../../1-algorithme/problème-preuve/#algorithme-max-tableau-iter).

Lorsque la sortie est un booléen, on parlera alors plutôt de problèmes de décision :

{% definition %}
La **_Un problème de décision_** est un problème algorithmique dont la sortie est un booléen. Plutôt qu'une sortie, on parle pour ces problèmes de **_question_**.
{% enddefinition %}
{% info %}
[Les problèmes de décision](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_d%C3%A9cision){.externe} sont très important en informatique théorique. On le verra (bien) plus tard.
{% endinfo %}

Par exemple :

<span id="définition-problème-décision"></span>

{% note "**Problème de décision**" %}

- **Nom** : recherche
- **Entrées** :
  - un entier $x$
  - un tableau d'entiers $T$
- **Question** : existe-t-il un indice $0\leq i < T.\mbox{\small longueur}$ tel que $T[i] = x$  ?

{% endnote %}

Un même problème peut cependant avoir plusieurs algorithmes solutions, certains étant meilleurs que d'autres. On peut alors se poser la question de la complexité d'un problème algorithmique. C'est à dire :

{% definition %}
La **_complexité (maximale) d'un problème_** algorithmique est **la complexité du meilleur algorithme** (celui de complexité maximale la plus faible) qui le résout.
{% enddefinition %}

Cette complexité existe toujours car :

1. le problème étant algorithmique il admet au moins un algorithme pour le résoudre.
2. Les algorithmes résolvant le problème peuvent être classées selon leurs complexités et admettent donc un minimum.

Elle peut cependant être difficile à trouver car il faut pouvoir raisonner sans avoir tous les algorithmes (une infinité) à sa disposition. Mais :

- si l'on possède déjà un algorithme pour résoudre le problème, sa complexité est **une borne maximale** de la complexité du problème qu'il résout
- il est facile de se donner **une borne minimale** de la complexité du problème (même si l'on ne sait pas s'il existe un algorithme pour le résoudre) qui est la taille de la sortie de l'algorithme. On a lors l'encadrement :

<div>
$$
\Omega(\text{taille sortie}) = \text{complexité du problème} = \mathcal{O}(\text{complexité d'un algorithme le résolvant})
$$
</div>

Cet encadrement est général pour tout problème algorithmique et s'écrit :

<div>
$$
\Omega(\text{borne minimale du problème}) = \text{complexité du problème} = \mathcal{O}(\text{borne maximale du problème})
$$
</div>

Si on arrive à mettre la même valeur à gauche et à droite on aura trouvé la complexité du problème :

{% retenir %}
Si l'on arrive à encadrer le problème à gauche par un $\Omega$ et à droite par un $\mathcal{O}$ avec le même algorithme :

$$
\Omega(\text{complexité de l'algorithme A le résolvant}) = \text{complexité du problème} = \mathcal{O}(\text{complexité de l'algorithme A le résolvant})
$$

on aura trouvé la complexité du problème : $\Theta(\text{complexité de l'algorithme A le résolvant})$.

{% endretenir %}

Nous illustrerons ici cette problématique avec deux exemples qui nous permettrons de voir plusieurs techniques de calcul de la complexité d'un problème algorithmique.

## <span id="max"></span> Complexité du problème max

Ce qu'on peut déjà dire de notre problème :

- une **borne minimale** : $\mathcal{O}(1)$ puisque la taille la sortie est un entier
- une **borne maximale** : $\mathcal{O}(n)$ où $n$ est la longueur du tableau puisque l'algorithme ci-dessous (dont on [on a déjà calculé la complexité](../../2-complexités/projet-calcul-max-min-moy/#max-tableau)) résout le problème

```pseudocode
algorithme maximum(T: []int) → int:
    ref m ← T[0]
    pour chaque x de T:
        si m < x:
            m ← x
    rendre m
```

Notre borne minimale de $\mathcal{O}(1)$ semble irréaliste. Supposons en effet qu'il existe un algorithme $A$ qui résout le problème de recherche pour tous les tableaux de longueur $n$ en prenant strictement moins de $n$ instructions : l'algorithme $A$ n'a pas besoin de regarder toutes les cases du tableau de longueur $n$ en entrée pour répondre.

Soit alors un tableau $T$ de longueur $n$ dont le max est `m`{.language-}. Notre algorithme va rendre $m$ en strictement moins de $n$ instructions. Ceci signifie qu'il existe une case du tableau, disons $T[i^\star]$, que l'algorithme n'a jamais regardé lors de son exécution : il ne sait pas ce que contient cette case.

On crée alors un tableau $T'$ de $n$ cases tel que :

- $T'[i] = T[i]$ si $i \neq i^\star$
- $T'[i^\star] = m + 1$

Comme $T$ et $T'$ sont identiques sauf pour la case d'indice $i^\star$,
si l'algorithme ne regarde pas la case $T[i^\star]$ lors de son exécution pour $T$, il ne regardera pas non plus la case $T'[i^\star]$ lors de son exécution pour $T'$. Il ne pourra donc répondre que la même chose pour $T$ et $T'$, ce qui est impossible puisque la réponse est $m$ pour $T$ et $m+1$ pour $T'$.

Notre hypothèse était fausse : un algorithme qui résout le problème max doit accéder au moins une fois à toutes les cases du tableau passé en entrée. Tout algorithme résolvant le problème max doit au moins être de complexité $\mathcal{O}(n)$. On peut donc une nouvelle borne minimale pour notre problème : $\Omega(n)$.

Au final on a :

- une borne minimale de la complexité de la recherche de $\Omega(n)$
- un algorithme qui résout le problème en $\mathcal{O}(n)$

Donc :

{% note "**Proposition**" %}
La complexité du problème max est en $\Theta(n)$ où $n$ est la longueur du tableau passé en entrée.
{% endnote %}

On peut en déduire une règle générale de la complexité d'un problème :

{% retenir %}
Si les données n'ont pas de structure particulière — très souvent — la complexité d'un problème est au moins égale à la taille de ses données.

Si ce n'est pas vrai, c'est que notre problème est vraisemblablement mal posé et qu'on peut se passer de certaines entrées.
{% endretenir %}

## <span id="recherche"></span> Complexités des problèmes recherche et recherche ordonnée

Ce qu'on peut déjà dire de notre problème :

- une **borne minimale** : $\mathcal{O}(1)$ puisque la taille la sortie est un booléen
- une **borne maximale** : $\mathcal{O}(n)$ où $n$ est la longueur du tableau puisque l'algorithme ci-dessous (dont on [on a déjà calculé la complexité](../../2-complexités/complexité-moyenne/#exemple-recherche)) résout le problème

```pseudocode/
algorithme recherche(T: []int, x: int) → bool:
    pour chaque e de T:
        si e == x:
            rendre Vrai
    rendre Faux
```

<span id="problème-max-tableau-complexité"></span>
{% exercice %}
Montrer que la complexité du problème recherche est en $\Theta(n)$
{% endexercice %}
{% details "corrigé" %}

Il faut montrer deux choses :

1. un algorithme qui résout le problème en $\mathcal{O}(n)$
2. une borne minimale de la complexité de la recherche de $\Omega(n)$

Pour le premier point, l'algorithme juste au-dessus fonctionne et pour le second point on raisonne exactement comme pour le problème max :

1. Supposons qu'il existe un algorithme résolvant le problème recherche en strictement moins de $n$ opérations.
2. On prend un tableau $T$ de longueur $n$ et ne contenant pas $x$. L'algorithme hypothétique répond NON à la présence de $x$ dans $T$ en strictement moins de $n$ opérations : il n'a pas regardé la case $T[i^\star]$ lors de son exécution.
3. On crée le tableau $T'$ de longueur $n$ tel que :
   - $T'[i] = T[i]$ si $i \neq i^\star$
   - $T'[i^\star] = x$
4. Comme  $T'$ et  $T'$ ne diffèrent que d'une case que l'algorithme hypothétique n'a pas examiné, il va donner la même réponse pour les entrées $(T, x)$ et $(T', x)$ ce qui est impossible.
5. on arrive à une contradiction : l'algorithme hypothétique n'existe pas et tout algorithme résolvant recherche est en $\Omega(n)$.

{% enddetails %}

{% attention %}
Ca ne veut pas dire qu'il n'existe pas des instances où l'algorithme va plus vite (si valeur est le 1er élément du tableau par exemple), mais que pour toute longueur $n$ du tableau, il existe des tableaux pour lesquels on est obligé de vérifier toutes les cases (si valeur n'est pas dans tableau).
{% endattention %}

On va s'intéresser maintenant à un cas particulier de problème recherche, celui où le tableau en entrée est tré par ordre croissant :

{% note "**Problème de décision**" %}

- **Nom** : recherche ordonnée
- **Entrées** :
  - un entier $x$
  - un tableau d'entiers $T$ trié par ordre croissant
- **Question** : existe-t-il un indice $0\leq i < T.\mbox{\small longueur}$ tel que $T[i] = x$  ?

{% endnote %}

Le problème _"recherche ordonnée"_ est un sous problème de _"recherche"_, on a donc une borne maximale de $\mathcal{O}(n)$ (où $n$ est la longueur du tableau) pour le résoudre puisqu'il suffit d'utiliser l'algorithme `recherche(T)`{.language-}.

On a cependant vu un algorithme permettant d'aller plus vite dans ce cas : [la recherche dichotomique](../../2-complexités/projet-calcul-max-min-moy/#dichotomie). Rappelons cet algorithme :

```pseudocode
algorithme recherche_dichotomique(T: []int, x: int) → bool:
  ref a, b ← 0, T.longueur - 1
  ref m int

  tant que a ≤ b:
      m ← (a + b) // 2  # division entière

      si (T[m] == x):
          rendre Vrai
      si (T[m] < x):
          a ← m + 1
      si (T[m] > x):
          b ← m - 1

  rendre Faux

```

Sa complexité est en $\mathcal{O}(\ln(n))$ : il n'a pas besoin de connaître toutes les cases du tableau pour répondre à la question car le tableau est trié. Une borne maximum de la complexité du problème "recherche ordonnée" est alors $\mathcal{O}(\ln(n))$ (avec $n$ la longueur du tableau). Nous allons montrer que l'on ne peut pas faire mieux !

{% info %}
Remarquez bien que la preuve que l'on a donné pour la complexité de _"recherche"_ ne fonctionne pas dans le cas de "recherche ordonnée". On ne peut pas fabriquer comme précédemment de tableau $T'$ car les valeurs doivent être ordonnées.
{% endinfo %}

Commençons par remarquer que `x`{.language-} peut se trouver à chaque position du tableau de longueur $n$. Tout algorithme qui résout "recherche ordonnée" doit ainsi réussir à distinguer parmi $n + 1$ cas :

- soit `x`{.language-} n'est pas dans tableau
- soit `x`{.language-} est à l'indice 0 du tableau
- soit `x`{.language-} est à l'indice 1 du tableau
- ...
- soit `x`{.language-} est à l'indice $n-1$ du tableau

En algorithmie, distinguer parmi plusieurs cas se fait par des tests (on utilise l'instruction `si (expression) alors: ...`{.language-}). De là :

<span id="n-test-2n"></span>
{% note "**Proposition**" %}
Si un algorithme doit distinguer parmi $n$ cas, il devra posséder au moins $\log_2(n)$ tests. Sa complexité sera ainsi en $\Omega(\ln(n))$.
{% endnote %}
{% details "preuve", "open" %}

- s'il y a 0 test, un algorithme ne peut pas distinguer de cas.
- s'il y a 1 test, un algorithme peut distinguer au plus 2 cas :
  - 1 cas si le test est vrai
  - 1 cas si le test est faux
- s'il y a 2 tests, un algorithme peut distinguer au plus $2 \cdot 2 = 4$ cas :
  - 1 cas si les deux tests sont vrai
  - 1 cas si le premier test est vrai et le second test faux
  - 1 cas si le premier test est faux et le second test vrai
  - 1 cas si les deux tests sont faux
- s'il y a 3 tests, un algorithme peut distinguer au plus $2 \cdot 2 \cdot 2 = 2^3 = 8$ cas :
  - 1 cas si les trois tests sont vrai
  - 1 cas si les deux premiers tests sont vrai et le troisième test faux
  - ...
  - 1 cas si les trois tests sont faux
- ...
- s'il y a $K$ tests, un algorithme peut distinguer au plus $2^K$ cas

{% enddetails %}

Comme dans le cas de la recherche il y a $n+1$ cas au moins à traiter, notre algorithme sera de complexité $\Omega(\ln(n + 1)) = \Omega(\ln(n))$ opérations.

Au final, le problème de la _"recherche ordonnée"_ pour un tableau à $n$ éléments  est de complexité $\mathcal{O}(\ln(n))$ :

- une borne minimale de complexité égal à $\Omega(\ln(n))$
- la complexité de l'algorithme `recherche_dichotomique`{.language-} est en $\mathcal{O}(\ln(n))$


{% retenir %}
La borne minimale d'un problème est supérieure au log du nombre de cas à distinguer parmi ses entrées.
{% endretenir %}

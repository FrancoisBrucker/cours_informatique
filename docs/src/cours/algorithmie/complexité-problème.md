---
layout: layout/post.njk
title: "Complexité d'un problème algorithmique"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[Un problème algorithmique](../écrire-algorithmes/problème/){.interne} est une question solvable par un algorithme. Un même problème peut cependant avoir plusieurs algorithmes solutions, certains étant meilleurs que d'autres. On peut alors se poser la question de la complexité d'un problème algorithmique. C'est à dire :

{% note "**Définition**" %}
La **_complexité (maximale) d'un problème_** algorithmique est la complexité (maximale) du meilleur algorithme (celui de complexité a plus faible) qui le résout.
{% endnote %}

Cette complexité existe toujours car :

1. le problème étant algorithmique il admet au moins un algorithme pour le résoudre.
2. Les algorithmes résolvant le problème peuvent être classées selon leurs complexités, entières, et admettent donc un minimum.

Mais elle peut être difficile à trouver il faut pouvoir raisonner sans avoir tous les algorithmes (une infinité) à sa disposition.

Cependant, si l'on possède déjà un algorithme pour résoudre le problème, sa complexité est **une borne maximale** de la complexité du problème qu'il résout. Il est également souvent facile de se donner **une borne minimale** de la complexité du problème (même si l'on ne sait pas s'il existe un algorithme pour le résoudre), c'est la taille de la sortie de l'algorithme. On a lors l'encadrement :

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

{% attention2 "**À retenir**" %}
Si l'on arrive à encadrer le problème à gauche par un $\Omega$ et à droite par un $\mathcal{O}$ avec le même algorithme :

$$
\Omega(\text{complexité de l'algorithme A le résolvant}) = \text{complexité du problème} = \mathcal{O}(\text{complexité de l'algorithme A le résolvant})
$$

on aura trouvé la complexité du problème : $\Theta(\text{complexité de l'algorithme A le résolvant})$.

{% endattention2 %}

Nous illustrerons ici cette problématique avec l'exemple de la recherche d'un élément dans un tableau qui permet d'illustrer plusieurs facettes de ce qu'est un problème algorithmique.

## <span id="recherche"></span>Exemple : recherche d'un élément dans un tableau

On va chercher à résoudre le problème suivant :
<span id="définition-problème-décision"></span>

{% note "**Problème**" %}

- **Nom** : recherche
- **Entrées** :
  - un entier $x$
  - un tableau d'entiers $T$
- **Question** : existe-t-il un indice $0\leq i < T.\mbox{\small longueur}$ tel que $T[i] = x$  ?

{% endnote %}
{% info %}
On a utilisé ici le mot clé **question** plutôt que **sortie**. On utilisera cette convention lorsque la sortie est soit OUI soit NON.

On les appelle [problèmes de décision](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_d%C3%A9cision) et sont très important en informatique théorique. On le verra (bien) plus tard.
{% endinfo %}

Ce qu'on peut déjà dire de notre problème :

- une **borne minimale** : $\mathcal{O}(1)$ puisque la taille la sortie est un booléen
- une **borne maximale** : $\mathcal{O}(n)$ où $n$ est la taille du tableau puisque l'algorithme ci-dessous (dont on [on a déjà calculé la complexité](../complexité-calculs/O-pour-l-algorithmie/#exemple-recherche){.interne}) résout le problème

```pseudocode/
algorithme recherche(T: [entier], x: entier) → booléen:
    pour chaque e de T:
        si e == x:
            rendre Vrai
    rendre Faux
```

### <spans id="complexité-recherche"></span> Complexité du problème "recherche"

Notre borne minimale de $\mathcal{O}(1)$ semble irréaliste. Supposons de façon plus générale qu'il existe un algorithme $A$ qui résout le problème de recherche pour tous les tableaux de longueur $n$ en prenant strictement moins de $n$ instructions : ceci signifie l'algorithme $A$ n'a pas besoin de regarder toutes les cases d'un tableau de longueur $n$ pour répondre.

Soit alors un tableau $T$ de taille $n$ qui ne contient pas `x`{.language-}. Notre algorithme va répondre NON à la question _"est-ce que valeur est dans $T$ ?"_ en strictement moins de $n$ instructions. Ceci signifie qu'il existe une case du tableau, disons $T[i^\star]$, que l'algorithme n'a jamais regardé lors de son exécution : il ne sait pas ce que contient cette case.

On crée alors un tableau $T'$ de $n$ cases tel que :

- $T'[i] = T[i]$ si $i \neq i^\star$
- $T'[i^\star] = \mbox{valeur}$

Comme $T$ et $T'$ sont identiques sauf pour la case d'indice $i^\star$,
si l'algorithme ne regarde pas la case $T[i^\star]$ lors de son exécution pour $T$, il ne regardera pas non plus la case $T'[i^\star]$ lors de son exécution pour $T'$. Il ne pourra donc répondre que la même chose pour $T$ et $T'$, ce qui est impossible puisque la réponse est NON pour $T$ et OUI pour $T'$.

Notre hypothèse était fausse : un algorithme qui résout le problème de la recherche doit accéder au moins une fois à toutes les cases du tableau, il doit au moins être de complexité $\mathcal{O}(n)$ : la complexité du problème de la recherche est en $\Omega(n)$.

{% attention %}
Ca ne veut pas dire qu'il n'existe pas des instances où l'algorithme va plus vite (si valeur est le 1er élément du tableau par exemple), mais que pour toute taille $n$ du tableau, il existe des tableaux pour lesquels on est obligé de vérifier toutes les cases (si valeur n'est pas dans tableau).
{% endattention %}

Au final on a :

- une borne minimale de la complexité de la recherche de $\Omega(n)$
- un algorithme qui résout le problème en $\mathcal{O}(n)$

Donc :

{% note "**Proposition**" %}
La complexité du problème de la recherche est en $\Theta(n)$ où $n$ est la taille du tableau.
{% endnote %}

On peut en déduire une règle générale de la complexité d'un problème :

{%  attention "**À retenir**" %}
Si les données n'ont pas de structure particulière — très souvent — la complexité d'un problème est au moins égale à la taille de ses données.

Si ce n'est pas vrai, c'est que notre problème est vraisemblablement mal posé et qu'on peut se passer de certaines entrées.
{% endattention %}

À vous :

<span id="problème-max-tableau-complexité"></span>
{% exercice %}
Montrer que le problème de [la recherche d'un élément maximal d'un tableau d'entiers](../#problème-max-tableau){.interne} est en $\Theta(n)$
{% endexercice %}
{% details "corrigé" %}

Il faut montrer deux choses :

1. une borne minimale de la complexité de la recherche de $\Omega(n)$
2. un algorithme qui résout le problème en $\mathcal{O}(n)$

Pour le premier point on raisonne exactement comme pour le problème de la recherche. Pour le second point [on a déjà vu un algorithme](../projet-calcul-complexite/#algorithme-max-tableau-complexité){.interne} de ce type.

{% enddetails %}

### Cas particulier des tableaux ordonnés

Un cas particulier courant de recherche est le problème :

{% note "**Problème de décision**" %}

- **nom** : recherche ordonnée
- **données** : une valeur et un tableau d'entiers triés par ordre croissant
- **question** : valeur est-elle présente dans le tableau ?

{% endnote %}

Le problème _"recherche ordonnée"_ est un sous problème de _"recherche"_, on a donc une borne maximale de $\mathcal{O}(n)$ (où $n$ est la taille du tableau) pour le résoudre puisqu'il suffit d'utiliser l'algorithme `est_dans_tableau(T)`{.language-}.

Cependant, on utilise souvent un autre algorithme : la recherche dichotomique.

#### Algorithme de la recherche dichotomique

Le principe de [la recherche dichotomique](https://fr.wikipedia.org/wiki/Recherche_dichotomique) permet de savoir si un entier donné est dans un tableau d'entier trié.

On cherche à savoir si l'entier $v$ est entre les indices $a$ et $b \geq a$ d'un tableau d'entiers $t$. On procède récursivement selon la valeur de $t[\lfloor (a + b)/2 \rfloor]$ :

- si $t[\\,\lfloor (a + b)/2 \rfloor\\,] = v$ on a trouvé l'élément
- si $t[\\,\lfloor (a + b)/2 \rfloor\\,] > v$, l'indice recherché est forcément **avant** $\lfloor (a + b)/2 \rfloor$. On recommence alors la procédure avec :
  - $a = \lfloor (a + b)/2 \rfloor + 1$
  - $b$ inchangé
- si $t[\\,\lfloor (a + b)/2 \rfloor\\,] < v$, l'indice recherché est forcément **après** $\lfloor (a + b)/2 \rfloor$. On recommence alors la procédure avec :
  - $a$ inchangé
  - $b' = \\,\lfloor (a + b)/2 \rfloor\\, - 1$

Ce principe donne l'algorithme suivant :

<span id="algorithme-dichotomie"></span>

```pseudocode
algorithme recherche_dichotomique(T: [entier], x: entier) → booléen:
  a ← 0
  b ← t.longueur - 1
  si b > a:
  tant que a ≤ b:
    m ← (a + b) // 2  # division entière

    si (t[m] == v):
        rendre Vrai  # m est l'indice
    si (t[m] < v):
        a ← m + 1
    si (t[m] > v):
        b ← m - 1

  rendre Faux

```

Étudions l'algorithme :

- **fonctionnement**. On vérifie que pour :
  - un tableau `[1, 3, 7]`{.language-} l'algorithme trouve bien `7`{.language-} et ne trouve pas `8`{.language-}
  - un tableau `[1, 3, 3, 7]`{.language-} l'algorithme trouve bien `7`{.language-} et ne trouve pas `9`{.language-}
- **preuve** :
  - **finitude**. La quantité entière `b - a`{.language-} **décroît strictement** à chaque itération, elle sera donc strictement négative après un nombre fini d'opération et l'algorithme s'arrêtera.
  - **preuve**.
    1. on montre trivialement l'invariant de boucle suivant: si valeur est dans `T`{.language-}, alors sa position est plus grande que `a`{.language-} et plus petite que `b`{.language-}
    2. si l'on sort de la boucle l'invariant est toujours vérifié mais comme `a`{.language-} > `b`{.language-}, `x`{.language-} ne peut être dans `T`{.language-}

Les remarques ci-dessus prouvent que l'algorithme `recherche_dichotomique`{.language-} résout bien le problème _"recherche ordonnée"_.

Étudions sa complexité. Ligne à ligne :

1. initiation de la fonction $\mathcal{O}(1)$
2. affection : $\mathcal{O}(1)$
3. affection : $\mathcal{O}(1)$
4. —
5. boucle de $K$ itérations (pour l'instant, la valeur de $K$ est **inconnue**)
6. affection : $\mathcal{O}(1)$
7. —
8. test d'une valeur dans un tableau : $\mathcal{O}(1)$
9. retour de fonction : $\mathcal{O}(1)$
10. test d'une valeur dans un tableau : $\mathcal{O}(1)$
11. addition plus une affectation : $\mathcal{O}(1)$
12. —
13. soustraction plus une affectation : $\mathcal{O}(1)$
14. retour de fonction : $\mathcal{O}(1)$

Ce qui donne comme complexité :

<div>
$$
\begin{array}{lcl}
C(n) & = & 3 \cdot \mathcal{O}(1) + \\
& & K \cdot (6 \cdot \mathcal{O}(1)) + \\
& & \mathcal{O}(1) \\
& = & \mathcal{O}(K)
\end{array}
$$
</div>

Comme à chaque itération, `b - a`{.language-} est divisé par 2, il y a autant d'itérations que l'on peut diviser $T.\mbox{\small longueur}$ par 2.

Si $K$ est ce nombre d'itérations, on a que : $2^{K} \leq T.\mbox{\small longueur}$. Il existe un nombre $p$ tel que $2^p \leq T.\mbox{\small longueur} < 2^{p + 1}$. On ne peut donc pas diviser $T.\mbox{\small longueur}$ par 2, ou un nombre plus petit que lui, plus de $p$ fois. Ce nombre est exactement la partie entière de $\log_2(T.\mbox{\small longueur})$ puisque :

<div>
$$
\begin{array}{lcccl}
    2^p &\leq &T.\mbox{\small longueur} &<& 2^{p + 1}\\
    \log_2(2^p) &\leq &\log_2(T.\mbox{\small longueur}) &< &\log_2(2^{p + 1}) \mbox{ (car la fonction est croissante)} \\
    p &\leq &\log_2(T.\mbox{\small longueur}) &<& p + 1
\end{array}
$$
</div>

On en conclut le théorème fondamental d la dichotomie : le nombre de fois où l'on peut diviser par 2 un nombre $n$ est $\log_2(n)$ : il y a donc au plus $K \leq \log_2(n)$ itérations (avec $n$ la taille du tableau). Comme $\log_2(n) = \frac{\ln(n)}{\ln(2)}$ on a :

{% note "**Proposition**" %}
L'algorithme `recherche_dichotomique`{.language-} résout le problème "recherche ordonnée" en $\mathcal{O}(\ln(n))$ (avec $n$ la taille du tableau).
{% endnote %}

#### <span id="complexité-recherche-ordonnée"></span> Complexité du problème "recherche ordonnée"

L'algorithme de la recherche dichotomique résout le problème de la "recherche ordonnée" de façon bien plus efficace que l'algorithme `recherche`{.language-} : il n'a pas besoin de connaître toutes les cases du tableau pour répondre à la question car le tableau est trié. Une borne maximum de la complexité du problème "recherche ordonnée" est alors $\mathcal{O}(\ln(n))$ (avec $n$ la taille du tableau).

Nous allons montrer que l'on ne peut pas faire mieux en montrant que $\mathcal{O}(\ln(n))$ est une borne minimum de notre problème.

{% info %}
Remarquez bien que la preuve que l'on a donné pour la complexité de _"recherche"_ ne fonctionne pas dans le cas de "recherche ordonnée". On ne peut pas fabriquer comme précédemment de tableau $T'$ car les valeurs doivent être ordonnées.
{% endinfo %}

Commençons par remarquer que `x`{.language-} peut se trouver à chaque position du tableau. Tout algorithme qui résout "recherche ordonnée" doit ainsi réussir à distinguer parmi $n + 1$ cas :

- soit `x`{.language-} n'est pas dans tableau
- soit `x`{.language-} est à l'indice 0 du tableau
- soit `x`{.language-} est à l'indice 1 du tableau
- ...
- soit `x`{.language-} est à l'indice $n-1$ du tableau

En algorithmie, distinguer parmi plusieurs cas se fait par des tests (on utilise les opérations `si alors sinon`). De là :

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

Au final, le problème de la _"recherche ordonnée"_ pour un tableau à $n$ éléments :

- une borne minimale de complexité égal à $\Omega(\ln(n))$
- la complexité de l'algorithme `recherche_dichotomique`{.language-} est en $\mathcal{O}(\ln(n))$

{% note "**Proposition**" %}
La complexité du problème de la _"recherche ordonnée"_ est en $\Theta(\ln(n))$ où $n$ est la taille du tableau.
{% endnote %}


À vous :

<span id="problème-max-tableau-complexité"></span>
{% exercice %}
Montrer que le problème de [la recherche d'un élément maximal d'un tableau d'entiers](../#problème-max-tableau){.interne} ordonné est en $\Theta(1)$
{% endexercice %}
{% details "corrigé" %}

Il suffit de toujours prendre le dernier élément qui est forcément le plus grand si le tableau est trié.

{% enddetails %}


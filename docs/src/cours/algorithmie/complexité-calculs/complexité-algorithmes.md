---
layout: layout/post.njk

title: Calculer la complexité d'algorithmes avec les O

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On va donner ici quelques règles de calcul de complexité pour que vous puissiez estimer rapidement la complexité d'un algorithme simple.

## Une boucle simple

Lorsque l'on a une boucle où le nombre de fois où l'on va rentrer dedans est évident.

Par exemple :

```pseudocode
tant que condition:
    bloc d'instructions
```

{% note "**Complexité d'une boucle tant que**" %}

<div>
$$
\mathcal{O}(\text{nombre de fois ou la condition est remplie}) \cdot (\mathcal{O}(\text{complexité de la vérification de la condition}) + \mathcal{O}(\text{complexité du bloc d'instruction}))
$$
</div>
{% endnote %}

Souvent, $\mathcal{O}$(complexité de la vérification de la condition) sera égal à $\mathcal{O}(1)$ et pourra ne pas en tenir compte dans le calcul. C'est le cas, entre autre pour une boucle tant que :

```pseudocode
pour chaque élément de structure:
    bloc d'instructions
```

{% note "**Complexité d'une boucle pour chaque**" %}

<div>
$$
\mathcal{O}(\text{nombre d'éléments de la structure}) \cdot \mathcal{O}(\text{complexité du bloc d'instruction})
$$
</div>
{% endnote %}

Si le bloc d'instructions est une suite d'instructions de complexité $\mathcal{O}(1)$, on pourra ne pas en tenir compte dans le calcul et la complexité est alors égale à la taille de la structure.

Illustrons ceci avec l'algorithme qui calcule [le nombre d'occurrences](../pseudo-code/#algorithme-nombre-occurrences){.interne} :

```pseudocode/
algorithme nombre(T: [entier], x: entier) → entier:
    nb ← 0
    pour chaque e de T:
        si e == x:
            nb ← nb + 1
    rendre nb
```

Lignes :

2. une affectation : $\mathcal{O}(1)$ opérations
3. une boucle de $T.\mbox{\small longueur}$ itérations : $\mathcal{O}(T.\mbox{\small longueur})$ opérations
4. un test : $\mathcal{O}(1)$ opérations
5. une affectation : $\mathcal{O}(1)$ opérations
6. retour en $\mathcal{O}(1)$ opération

Les lignes 2,3 et 4 sont effectuées $T.\mbox{\small longueur}$ fois, la complexité totale est donc en :

<div>
$$
\mathcal{O}(1) + T.\mbox{\small longueur} \cdot (\mathcal{O}(1) + \mathcal{O}(1)) + \mathcal{O}(1)
$$
</div>

Ce qui donne une complexité totale de $\mathcal{O}(T.\mbox{\small longueur})$.

{% note "**À retenir**"%}
Si le bloc d'instruction est une suite d'instructions de complexité $\mathcal{O}(1)$ et que la vérification de la fin de la boucle est $\mathcal{O}(1)$, la complexité de la boucle est égal au nombre de fois où l'on effectue la boucle
{% endnote %}

### Boucles imbriquées indépendantes

Plusieurs boucles imbriquées dont dont le nombre de fois où l'on va rentrer dedans est indépendant des autres boucles. Par exemple :

```pseudocode
boucle 1 exécutée n1 fois:
    boucle 2 exécutée n2 fois:
        ...
            boucle i exécutée ni fois:
                bloc d'instructions
```

On peut utiliser la règle précédente de façon récursive, la partie $\mathcal{O}$(complexité du bloc d'instruction) contenant elle même une ou plusieurs boucles.

<div id="complexité-boucles-indépendantes"></div>
{% note "**Complexité de boucles imbriquées indépendantes**" %}
La complexité des boucles imbriquées est le produit du nombre de fois où l'on rentre dans chaque boucle pris indépendamment multiplié par la complexité du bloc d'instructions.
{% endnote %}

Exemple le calcul de $\sum_{1\leq i \leq n}\sum_{1\leq j \leq n} (i+j)$ :

```pseudocode
total ← 0
pour chaque i de [1, n]:
    pour chaque j de [1, n]:
        total ← i + j
rendre total
```

La boucle en $i$ est exécuté $n$ fois ($i$ va de 1 à $n$), donc $\mathcal{O}(n)$ fois. La boucle en $j$ va également être exécutée $\mathcal{O}(n)$ fois indépendamment de la boucle en $i$. Enfin la complexité de la ligne 5 est $\mathcal{O}(1)$, la complexité totale des deux boucles imbriquées 2-5 vaut :

<p>
\[
\underbracket{\mathcal{O}(n)}_{\mbox{boucle en i}} \cdot \underbracket{\mathcal{O}(n)}_{\mbox{boucle en j}} \cdot \underbracket{\mathcal{O}(1)}_{\mbox{ligne 5}}
 = \mathcal{O}(n^2)
\]
</p>

{% note "**À retenir**" %}
Compter le nombre d'itération d'une boucle avec les $\mathcal{O}()$. Une boucle de $n-3$ exécutions pouvant être avantageusement remplacée par $\mathcal{O}(n)$

{% endnote %}

### <span id="règle-croissance"></span>Boucles dépendantes mais monotones

Il arrive souvent que les boucles imbriquées d'un algorithme soient dépendantes les unes des autres. Dans le cas général on ne peut pas factoriser le calcul de la complexité et il faut alors dérouler tout l'algorithme en additionnant les complexités de chaque ligne comme s'il n'y avait pas de boucles.

Il existe cependant un cas pratique (et qui arrive assez souvent) où l'on peut factoriser :

{% note "**Complexité de boucles dépendantes monotones**" %}
Si une boucle s'exécute un nombre variable de fois, mais que cette variation est croissante (respectivement décroissante), on peut considérer pour le calcul de la complexité qu'elle s'exécute à chaque fois de l'ordre du maximum de fois et se ramener au cas [des boucles indépendantes](./#complexité-boucles-indépendantes).
{% endnote %}

Exemple le calcul de $\sum_{1\leq i < n}\sum_{i < j \leq n} (i+j)$ :
On va vérifier cela avec un exemple :

```pseudocode
total ← 0
pour chaque i de [1, n-1]:
    pour chaque j de [i+1, n]:
        total ← i + j
Rendre total
```

Le nombre de fois où la boucle en $j$ est exécutée est un nombre variable de fois qui dépend de la valeur de $i$. Comme $i$ va croître, le nombre de fois où cette boucle va s'exécuter va décroître. Si l'on applique la règle on peut dire qu'elle va s'exécuter de l'ordre de $\mathcal{O}(n)$ fois comme dans l'exemple de la partie précédente. La complexité de l'algorithme est donc de $\mathcal{O}(n^2)$.

Refaisons le calcul en décomposant toutes les instructions, comme on le ferait dans le cas général, pour voir que notre règle est valide (et donnera aussi une idée de la preuve de cette règle) :

- ligne 1 : $\mathcal{O}(1)$
- itération pour $i=1$:
  - ligne 2 : une affectation $i=1$ : $\mathcal{O}(1)$
  - boucle pour $j=1$:
    - ligne 3 : une affectation de $j$ : $\mathcal{O}(1)$
    - ligne 4 : $\mathcal{O}(1)$
    - le tout $n-1$ fois
- itération pour $i=2$:
  - ligne 2 : une affectation $i=2$ : $\mathcal{O}(1)$
  - boucle pour $j=2$:
    - ligne 3 : une affectation de $j$ : $\mathcal{O}(1)$
    - ligne 4 : $\mathcal{O}(1)$
    - le tout $n-2$ fois
- ...
- itération pour $i=n-1$:
  - ligne 2 : une affectation $i=n-1$ : $\mathcal{O}(1)$
  - boucle pour $j=n-1$:
    - ligne 3 : une affectation de $j$ : $\mathcal{O}(1)$
    - ligne 4 : $\mathcal{O}(1)$
    - le tout $1$ fois
- ligne 5 : $\mathcal{O}(1)$

Notre complexité totale est donc :

<p>\[
\begin{aligned}
    \mathcal{O}(1) + \\
    (\mathcal{O}(1) + (n-1) \cdot (\mathcal{O}(1) + \mathcal{O}(1))) + \\
    (\mathcal{O}(1) + (n-2) \cdot (\mathcal{O}(1) + \mathcal{O}(1))) + \\
    \dots\\
  (\mathcal{O}(1) + (1) \cdot (\mathcal{O}(1) + \mathcal{O}(1))) +\\
 \mathcal{O}(1)
\end{aligned}
\]</p>

Comme $\mathcal{O}(1) + \mathcal{O}(1) = \mathcal{O}(1)$, on a :

<p>\[
\begin{aligned}
    \mathcal{O}(1) + \\
    (\mathcal{O}(1) + (n-1) \cdot \mathcal{O}(1)) + \\
    (\mathcal{O}(1) + (n-2) \cdot \mathcal{O}(1)) + \\
    \dots\\
 (\mathcal{O}(1) + 1 \cdot \mathcal{O}(1)) +\\
 \mathcal{O}(1)
\end{aligned}
\]</p>

Ce qui donne :

<p>\[
\begin{aligned}
    \mathcal{O}(1) + \\
    n \cdot \mathcal{O}(1) + \\
    (n-1) \cdot \mathcal{O}(1) + \\
    \dots\\
 \mathcal{O}(1)
\end{aligned}
\]</p>

et donc notre complexité vaut :

$$\mathcal{O}(1) + \sum_{1\leq i \leq n} i \cdot \mathcal{O}(1)$$

Comme la somme des n premiers entiers vaut $\frac{(n+1)(n)}{2}$ notre complexité devient :

$$\mathcal{O}(1) + \frac{(n+1)(n)}{2} \mathcal{O}(1)$$

Ce qui est de l'ordre de : $\mathcal{O}(\frac{(n+1)(n)}{2})$. Or :

$$\mathcal{O}(\frac{(n+1)(n)}{2}) = \mathcal{O}(\frac{n^2 + n}{2}) = \mathcal{O}(n^2 +n) = \mathcal{O}(n^2)$$

On retrouve bien le résultat attendu.

### Complexité d'algorithmes récursifs

Un algorithme récursif est un algorithme qui s'appelle lui-même jusqu'à ce qu'on arrive à une condition d'arrêt qui stope la récursion. On en calcule la complexité en posant une équation qu'il faut résoudre :

{% note "**À retenir**" %}
Pour calculer la complexité d'un algorithme récursif en fonction de la taille $n$ de l'entrée, on pose que $C(n)$ est la complexité et l'on utilise cette fonction pour estimer la complexité des appels récursifs. Une fois les complexités des éléments d'arrêts estimés, trouver $C(n)$ revient à résoudre une équation de récurrence.
{% endnote %}

Pour illustrer ce calcul, reprenons [le calcul récursif de la factorielle](../prouver-un-algorithme/#algorithme-factorielle-rec) :

```pseudocode/
algorithme factorielle(n: entier) → entier:
    si n == 1:
        rendre 1

    f ← factorielle(n-1)
    rendre n * f
```

On exécute cette fonction avec comme paramètres initiaux un tableau nommé `t`{.language-} de taille `n = t.longueur - 1`{.language-}. On sait que cet algorithme fonctionne (on l'a déjà prouvé). Le calcul de la complexité se fait en résolvant une équation de récurrence. On pose que la complexité de notre algorithme pour un tableau de taille $n$ est : $C(n)$. De là, ligne à ligne :

1. définition d'une fonction $\mathcal{O}(1)$
2. une comparaison entre une constante et une variable : $\mathcal{O}(1)$
3. retour de fonction d'un élément d'un tableau : $\mathcal{O}(1)$
4. —
5. une affectation, plus l'appel à la fonction avec un tableau de taille $n-1$ (sa complexité est donc de $C(n-1)$ par définition) : $\mathcal{O}(1) + C(n-1)$
6. une multiplication et un retour de fonction : $\mathcal{O}(1)$

Ce qui donne en sommant le tout :

<div>
$$
\begin{array}{lcl}
C(n) & = & \mathcal{O}(1) + \\
&  & \mathcal{O}(1) + \\
&  & \mathcal{O}(1) + \\
&  & \mathcal{O}(1) + C(n-1) + \\
& & \mathcal{O}(1) \\
& = & 6 \cdot \mathcal{O}(1) + C(n-1) \\
& = & \mathcal{O}(1) + C(n-1) \\
\end{array}
$$
</div>

La complexité est définie par l'équation de récurrence $C(n) = \mathcal{O}(1) + C(n-1)$. Notre condition d'arrêt est obtenue pour `n`{.language-} valant 1 et dans ce cas on a $C(1) = \mathcal{O}(1)$

Trouver $C(n)$ revient à résoudre :

<div>
$$
\left\{
    \begin{array}{lcl}
        C(n) & = & \mathcal{O}(1) + C(n-1)\\
        C(1) & = & \mathcal{O}(1)
    \end{array}
\right.
$$
</div>

On a alors :

<div>
$$
\begin{array}{lcl}
    C(n) & = & \mathcal{O}(1) + C(n-1) \\
    & = & \mathcal{O}(1) + \mathcal{O}(1) + C(n-2) = 2 \cdot \mathcal{O}(1) + C(n-2)\\
    & = & 3 \cdot \mathcal{O}(1) + C(n-3) \\
    & = & \dots \\
    & = & i \cdot \mathcal{O}(1) + C(n-i) \\
    & = & \dots \\
    & = & (n-1) \cdot \mathcal{O}(1) + C(1) = (n-1) \cdot \mathcal{O}(1) + \mathcal{O}(1) \\
    & = & n \cdot \mathcal{O}(1) = \mathcal{O}(n) \\
\end{array}
$$
</div>

On va pouvoir écrire la complexité de nombreux algorithmes récursifs sous cette forme, n'oubliez pas comment faire :

{% note "**À retenir**" %}
La solution aux équations de récursion :

<div>
$$
\left\{
    \begin{array}{lcl}
        C(n) & = & \mathcal{O}(1) + C(n-1)\\
        C(1) & = & \mathcal{O}(1)
    \end{array}
\right.
$$
</div>

Sont :

<div>
$$
C(n) = \mathcal{O}(n)
$$
</div>

{% endnote %}

## Cas le pire

On ne peut pas toujours trouver une équation de récurrence fonctionnant pour toutes les entrées. Mais come le calcul de complexité ne s'intéresse qu'au cas le pire, il suffit de trouver une relation pour des donnant engendrant le plus d'instructions.

Pour illustrer cela, nous allons considérer deux algorithmes permettant de calculer le PGCD de deux nombres.

### Itératif

[Algorithme du PGCD récursif itératif](../#algorithme-PGCD){.interne} :

```pseudocode/
algorithme PGCD(a: entier, b: entier) → entier:  # a, b ≥ 0
    tant que min(a, b) > 0:
        a' ← max(a, b) - min(a, b)
        b' ← min(a, b)
        a, b ← a', b'
    
    rendre max(a, b)
```

En notant $K$ le nombre d'itérations de la boucle tant que, comme toutes les lignes sont en $\mathcal{O}(1)$ itérations, la complexité $C(a, b)$ de l'algorithme vaut :

<div>
$$
C(a, b) = K \cdot /mathcal{O}(1)
$$
</div>

On ne peut pas simplifier car $K$ dépend de $a$ et de $b$. A chaque itération $\max(a, b)$ va décroître strictement jusqu'à ce que $\max(a, b) = \min(a, b)$ ce qui stoppera la boucle à l'itération suivante.

On a donc que $K = \mathcal{O}(\max(a, b))$ (pas la peine d'être plus précis que cela) ce qui nous permet de conclure que : $C(a, b) = \mathcal{O}(\max(a, b))$.

### Récursif

Reprenons l'exemple [l'algorithme du PGCD récursif](../prouver-un-algorithme/#algorithme-PGCD-rec){.interne} :

```pseudocode/
algorithme PGCD(a, b):  # a, b > 0
    si a == b:
        rendre a
    si a < b:
        rendre PGCD(b-a, a)
    sinon
        rendre PGCD(a-b, b)
```

La complexité de cet algorithme dépend de ses paramètres. Notons là : $C(a, b)$. Comme toutes les lignes sont en $\mathcal{O}(1)$ opérations on obtient l'équation de récurrence :

<div>
$$
C(a, b) = \mathcal{O}(1) + C(\max(a, b) - \min(a, b), \min(a, b))
$$
</div>

En itérant sur cette équation comme on l'a fait précédemment avec le calcul de la complexité l'algorithme factoriel récursif on obtient :

<div>
$$
C(a, b) = K(a, b) \cdot \mathcal{O}(1)
$$
</div>

Où $K(a, b)$ est le nombre de récursion de l'algorithme avec les paramètres $a$ et $b$. De même que pour l'algorithme itératif on peut montrer que $\max(a, b)$ va décroître strictement à chaque itération, et donc que $K(a, b) \leq \max(a, b)$. De là :

<div>
$$
C(a, b) = K(a, b) \cdot \mathcal{O}(1) \leq \max(a, b) \cdot \mathcal{O}(1) = \mathcal{O}(\max(a, b))
$$
</div>

Comme les $\mathcal{O}$ sont des majorants, on a donc également $C(a, b) = \mathcal{O}(\max(a, b))$.

---
layout: layout/post.njk

title: Calculer la complexité d'algorithmes avec les O

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On va donner ici quelques règles de calcul de complexité pour que vous puissiez calculer rapidement la complexité d'un algorithme.

## Une boucle simple

{% retenir "**Quand utiliser**" %}
Lorsque l'on a une boucle où le nombre de fois où l'on va rentrer dedans est évident.
{% endretenir %}

Par exemple :

```pseudocode
tant que <condition>:
    # bloc d'instructions
```

{% note "**Complexité d'une boucle tant que**" %}

<div>
$$
\mathcal{O}(\text{nombre de fois ou la condition est remplie}) \cdot (\mathcal{O}(\text{complexité de la vérification de la condition}) + \mathcal{O}(\text{complexité des instructions du bloc}))
$$
</div>
{% endnote %}

Souvent, $\mathcal{O}$(complexité de la vérification de la condition) sera égal à $\mathcal{O}(1)$ et on pourra ne pas en tenir compte dans le calcul. C'est le cas, entre autres, pour une boucle `pour chaque`{.language-} :

```pseudocode
pour chaque e de <itérable>:
    # bloc d'instructions
```

{% note "**Complexité d'une boucle pour chaque**" %}

<div>
$$
\mathcal{O}(\text{nombre d'éléments de la structure}) \cdot \mathcal{O}(\text{complexité du bloc d'instruction})
$$
</div>
{% endnote %}

Si le bloc d'instructions est une suite d'instructions de complexité $\mathcal{O}(1)$, on pourra ne pas en tenir compte dans le calcul et la complexité est alors égale à la taille de la structure.

Illustrons ceci avec l'algorithme qui calcule [le nombre d'occurrences](../../1-algorithme/projet-itératif-récursif/#algorithme-nombre-occurrences) :

```pseudocode/
algorithme nombre(T: []int, x: int) → int:
    ref nb ← 0
    pour chaque e de T:
        si e == x:
            nb ← nb + 1
    rendre nb
```

Lignes :

1. une affectation : $\mathcal{O}(1)$ opérations
2. une boucle de $T.\mbox{\small longueur}$ itérations : $\mathcal{O}(T.\mbox{\small longueur})$ opérations
3. un test : $\mathcal{O}(1)$ opérations
4. une affectation : $\mathcal{O}(1)$ opérations
5. retour en $\mathcal{O}(1)$ opération

Les lignes 2,3 et 4 sont effectuées $T.\mbox{\small longueur}$ fois, la complexité totale est donc en :

<div>
$$
\mathcal{O}(1) + T.\mbox{\small longueur} \cdot (\mathcal{O}(1) + \mathcal{O}(1)) + \mathcal{O}(1)
$$
</div>

Ce qui donne une complexité totale de $\mathcal{O}(T.\mbox{\small longueur})$.

{% attention "**À retenir**"%}
Si le bloc d'instruction est une suite d'instructions de complexité $\mathcal{O}(1)$ et que la vérification de la fin de la boucle est $\mathcal{O}(1)$, la complexité de la boucle est égal au nombre de fois où l'on effectue la boucle
{% endattention %}

### Boucles imbriquées indépendantes

{% retenir "**Quand utiliser**" %}
Lorsque plusieurs boucles imbriquées où le nombre de fois où l'on rentre dans chaque boucle est indépendant des autres. 
{% endretenir %}

Par exemple :

```pseudocode
boucle 1 exécutée n1 fois:
    boucle 2 exécutée n2 fois:
        ...
            boucle i exécutée ni fois:
                # bloc d'instructions
```

On peut utiliser la règle précédente de façon récursive, la partie $\mathcal{O}$(complexité du bloc d'instruction) contenant elle même une ou plusieurs boucles.

<div id="complexité-boucles-indépendantes"></div>
{% note "**Complexité de boucles imbriquées indépendantes**" %}
La complexité des boucles imbriquées est le produit du nombre de fois où l'on rentre dans chaque boucle pris indépendamment multiplié par la complexité du bloc d'instructions.
{% endnote %}

Exemple le calcul de :

<div>
$$
\sum\limits_{1\leq i \leq n}(\sum\limits_{1\leq j \leq n} (i+j))
$$
</div>

```pseudocode
ref total ← 0
pour chaque i de [1 .. n]:
    pour chaque j de [1 .. n]:
        total ← i + j
rendre total
```

La boucle en $i$ est exécutée $n$ fois ($i$ va de 1 à $n$) donc $\mathcal{O}(n)$ fois. La boucle en $j$ va également être exécutée $\mathcal{O}(n)$ fois indépendamment de la boucle en $i$. Enfin la complexité de la ligne 5 est $\mathcal{O}(1)$, la complexité totale des deux boucles imbriquées 2-5 vaut :

<p>
\[
\underbracket{\mathcal{O}(n)}_{\mbox{boucle en i}} \cdot \underbracket{\mathcal{O}(n)}_{\mbox{boucle en j}} \cdot \underbracket{\mathcal{O}(1)}_{\mbox{ligne 5}}
 = \mathcal{O}(n^2)
\]
</p>

{% retenir %}
Compter le nombre d'itération d'une boucle avec les $\mathcal{O}()$. Une boucle de $n-3$ exécutions pouvant être avantageusement remplacée par $\mathcal{O}(n)$

{% endretenir %}

### <span id="règle-croissance"></span>Boucles dépendantes mais monotones

Il arrive souvent que les boucles imbriquées d'un algorithme soient dépendantes les unes des autres. Dans le cas général on ne peut pas factoriser le calcul de la complexité et il faut alors dérouler tout l'algorithme en additionnant les complexités de chaque ligne comme s'il n'y avait pas de boucles.

Il existe cependant un cas pratique (et qui arrive assez souvent) où l'on peut factoriser :

{% retenir "**Quand utiliser**" %}
Lorsqu'une boucle s'exécute un nombre variable de fois, mais que cette variation est croissante (_respectivement_ décroissante).
{% endretenir %}

{% note "**Complexité de boucles dépendantes monotones**" %}
Si une boucle s'exécute un nombre croissant (respectivement décroissant) de fois, on peut considérer pour le calcul de la complexité qu'elle s'exécute à chaque fois de l'ordre de son maximum et se ramener au cas [des boucles indépendantes](./#complexité-boucles-indépendantes).
{% endnote %}


Exemple le calcul de (notez la dépendance de $j$ par rapport à $i$) :

<div>
$$
\sum\limits_{1\leq i \leq n}(\sum\limits_{i < j \leq n} (i+j))
$$
</div>

```pseudocode
ref total ← 0
pour chaque i de [1 .. n-1]:
    pour chaque j de [i+1 .. n]:
        total ← i + j
affiche total
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

<div>
$$
\begin{array}{lcr}
    \mathcal{O}(1) &+ \\
    (\mathcal{O}(1) + (n-1) \cdot (\mathcal{O}(1) + \mathcal{O}(1))) &+ & (i = 1) \\
    (\mathcal{O}(1) + (n-2) \cdot (\mathcal{O}(1) + \mathcal{O}(1))) &+ & (i = 2) \\
    \dots\\
    (\mathcal{O}(1) + (n-i) \cdot (\mathcal{O}(1) + \mathcal{O}(1))) &+  \\
    \dots\\
  (\mathcal{O}(1) + (1) \cdot (\mathcal{O}(1) + \mathcal{O}(1))) &+ & (i = n-1) \\
 \mathcal{O}(1)
\end{array}
$$
</div>

Comme $\mathcal{O}(1) + \mathcal{O}(1) = \mathcal{O}(1)$, on a :

<div>
$$
\begin{array}{lcr}
    \mathcal{O}(1) &+ \\
    (\mathcal{O}(1) + (n-1) \cdot \mathcal{O}(1)) &+ & (i = 1) \\
    (\mathcal{O}(1) + (n-2) \cdot \mathcal{O}(1)) &+ & (i = 2) \\
    \dots\\
    (\mathcal{O}(1) + (n-i) \cdot \mathcal{O}(1)) &+  \\
    \dots\\
  (\mathcal{O}(1) + 1 \cdot \mathcal{O}(1)) &+ & (i = n-1) \\
 \mathcal{O}(1)
\end{array}
$$
</div>

Ce qui donne :

<div>
$$
\begin{array}{lcr}
    \mathcal{O}(1) &+ \\
    n \cdot \mathcal{O}(1) &+ & (i = 1) \\
    (n-1) \cdot \mathcal{O}(1) &+ & (i = 2) \\
    \dots\\
    (n-i) \cdot \mathcal{O}(1) &+  \\
    \dots\\
    2 \cdot \mathcal{O}(1) &+ & (i = n-1) \\
 \mathcal{O}(1)
\end{array}
$$
</div>

et donc notre complexité vaut :

<div>
$$
\mathcal{O}(1) + \sum_{1\leq i \leq n} i \cdot \mathcal{O}(1)
$$
</div>

Comme la somme des n premiers entiers vaut $\frac{(n+1)(n)}{2}$ notre complexité devient :

<div>
$$
\mathcal{O}(1) + \frac{(n+1)(n)}{2} \mathcal{O}(1)
$$
</div>

Ce qui est de l'ordre de : $\mathcal{O}(\frac{(n+1)(n)}{2})$. Or :

<div>
$$
\mathcal{O}(\frac{(n+1)(n)}{2}) = \mathcal{O}(\frac{n^2 + n}{2}) = \mathcal{O}(n^2 +n) = \mathcal{O}(n^2)
$$
</div>

On retrouve bien le résultat attendu.

### Complexité d'algorithmes récursifs


Un algorithme récursif est un algorithme qui s'appelle lui-même jusqu'à ce qu'on arrive à une condition d'arrêt qui stope la récursion. 

{% retenir "**Quand utiliser**" %}
Pour calculer la complexité d'un algorithme récursif.
{% endretenir %}



{% note "**Complexité d'un algorithme récursif**" %}
Pour calculer la complexité d'un algorithme récursif en fonction de la taille $n$ de l'entrée, on pose que $C(n)$ est la complexité et l'on utilise cette fonction pour estimer la complexité des appels récursifs. Une fois les complexités des éléments d'arrêts estimés, trouver $C(n)$ revient à résoudre une équation de récurrence.
{% endnote %}

Pour illustrer ce calcul, reprenons [le calcul récursif de la factorielle](../../1-algorithme/problème-preuve/#algorithme-factorielle-rec) :

```pseudocode/
algorithme factorielle(n: int) → int:
    si n == 1:
        rendre 1

    ref f ← factorielle(n-1)
    rendre n * f
```

On exécute cette fonction avec un entier $n$ comme paramètre initial. On sait que cet algorithme fonctionne (on l'a déjà prouvé) et on pose que sa complexité est $C(n)$. Son calcul effectif se fait en calculant $C(n)$ comme on le ferait avec un algorithme itératif, ligne à ligne :

1. définition d'une fonction $\mathcal{O}(1)$
2. une comparaison entre une constante et une variable : $\mathcal{O}(1)$
3. retour de fonction d'un élément d'un tableau : $\mathcal{O}(1)$
4. —
5. une affectation, plus l'appel à la fonction avec un tableau de taille $n-1$ (sa complexité est donc de $C(n-1)$ par définition) : $\mathcal{O}(1) + C(n-1)$
6. une multiplication et un retour de fonction : $\mathcal{O}(1)$


On a alors :

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


L'équation de récurrence $C(n) = \mathcal{O}(1) + C(n-1)$. peut se résoudre en y ajoutant notre condition d'arrêt (obtenue pour `n`{.language-} valant 1) qui va nous donner $C(1) = \mathcal{O}(1)$ comme condition limite :

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

On résout le tout en appliquant itérativement l'équation :

<div>
$$
\begin{array}{lcl}
    C(n) & = & \mathcal{O}(1) + C(n-1) \\
    & = & \mathcal{O}(1) + \mathcal{O}(1) + C(n-2) = 2 \cdot \mathcal{O}(1) + C(n-2)\\
    & = & 3 \cdot \mathcal{O}(1) + C(n-3) \\
    & = & \dots \\
    & = & i \cdot \mathcal{O}(1) + C(n-i) \\
    & = & \dots \\
    & = & (n-1) \cdot \mathcal{O}(1) + C(1)\\
    & = & \mathcal{O}(n) + C(1)\\
\end{array}
$$
</div>

Et on conclut avec notre condition limite :

<div>
$$
\begin{array}{lcl}
    C(n) & = & \mathcal{O}(n) + C(1)\\
    & = & \mathcal{O}(n) + \mathcal{O}(1)\\
    & = & \mathcal{O}(n) \\
\end{array}
$$
</div>

On va pouvoir écrire la complexité de nombreux algorithmes récursifs sous cette forme, n'oubliez pas comment faire :

{% retenir %}
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

Est :

<div>
$$
C(n) = \mathcal{O}(n)
$$
</div>

{% endretenir %}

## Cas le pire

On ne peut pas toujours trouver une équation de récurrence fonctionnant pour toutes les entrées. Mais come le calcul de complexité ne s'intéresse qu'au cas le pire, il suffit de trouver une relation pour des donnant engendrant le plus d'instructions.

{% retenir "**Quand utiliser**" %}
Lorsque l'on peut borner le nombre d'itérations et/ou de récursions d'un algorithme.
{% endretenir %}


Pour illustrer cela, nous allons considérer deux algorithmes permettant de calculer le pgcd de deux nombres.

### Itératif

Reprenons un de nos algorithmes fil rouge
Reprenons l'exemple [l'algorithme du pgcd itératif](../../1-algorithme/pseudo-code/récursifs-itératifs/#algorithme-pgcd) :
 :

```pseudocode/
algorithme pgcd(a: int, b: int) → int:  # a, b ≥ 0
    tant que min(a, b) > 0:
        a, b ← max(a, b) - min(a, b), min(a, b)
    rendre max(a, b)
```

En notant $K$ le nombre d'itérations de la boucle tant que, comme toutes les lignes sont en $\mathcal{O}(1)$ itérations, la complexité $C(a, b)$ de l'algorithme vaut :

<div>
$$
C(a, b) = K \cdot \mathcal{O}(1)
$$
</div>

On ne peut pas simplifier car $K$ dépend de $a$ et de $b$. A chaque itération soit $a$ soit $b$ va décroître strictement jusqu'à ce que $\min(a, b) = 0$ ce qui stoppera la boucle.

Donc au bout de $K = \mathcal{O}(\max(a, b))$ itérations on aura forcément soit $a$ soit $b$ qui vaudra 0 (pas la peine d'être plus précis que cela)  :

<div>
$$
C(a, b) = \mathcal{O}(\max(a, b))
$$
</div>

### Récursif

Reprenons l'exemple [l'algorithme du pgcd récursif](../../1-algorithme/pseudo-code/récursifs-itératifs/#algorithme-pgcd-rec) :

```pseudocode
algorithme pgcd(a: int, b: int) → int:  # a, b ≥ 0
    si min(a, b) == 0:
        rendre max(a, b)
    sinon:
        rendre pgcd(max(a, b) - min(a, b), min(a, b))
```

La complexité de cet algorithme dépend de ses paramètres, notons là : $C(a, b)$. Comme toutes les opérations hors récursion sont en $\mathcal{O}(1)$ opérations on obtient l'équation de récurrence :

<div>
$$
C(a, b) = \mathcal{O}(1) + C(\max(a, b) - \min(a, b), \min(a, b))
$$
</div>

En itérant sur cette équation comme on l'a fait précédemment avec le calcul de la complexité de l'algorithme factoriel récursif on obtient :

<div>
$$
C(a, b) = K(a, b) \cdot \mathcal{O}(1)
$$
</div>

Où $K(a, b)$ est le nombre de récursions de l'algorithme avec les paramètres $a$ et $b$. De même que pour l'algorithme itératif soit $a$ soit $b$ va décroître strictement à chaque récursion, donc que $K(a, b) \leq \max(a, b)$, ce qui implique :

<div>
$$
C(a, b) = K(a, b) \cdot \mathcal{O}(1) \leq \max(a, b) \cdot \mathcal{O}(1) = \mathcal{O}(\max(a, b))
$$
</div>

Comme les $\mathcal{O}$ sont des majorants, on a donc également $C(a, b) = \mathcal{O}(\max(a, b))$.

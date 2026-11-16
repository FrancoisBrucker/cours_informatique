---
layout: layout/post.njk

title: Calculer la complexité d'algorithmes avec les O

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le calcul de complexité d'un algorithme se fait via l'utilisation de fonctions asymptotiques qui nous permettent de donner son comportement lorsque les données deviennent grandes. C'est le seul cas qui nous intéresse puisque lorsque les données sont petites, l'algorithme ira vite quoi qu'il arrive. Les différentes formes de complexités qui nous intéresses sont les suivantes :

{% retenir %}

On cherchera à borner la complexité par une allure de complexité :

- ***complexité constante*** en $\mathcal{O}(1)$
- ***complexité logarithmique*** en $\mathcal{O}(\log_2(n)) = \mathcal{O}(\ln(n))$
- ***complexité linéaire*** en $\mathcal{O}(n)$
- ***complexité polynomiale*** en $\mathcal{O}(n^k)$ avec $k>1$ constant le plus petit possible
- ***complexité exponentielle*** en $\mathcal{O}(k^n)$ avec $k>1$ constant le plus petit possible
{% endretenir %}

Si nos approximations ne sont pas disproportionnées (genre en disant que $\log_2(n) = \mathcal{O}(2^n)$) ou que l'on arrive à utiliser des $\Theta$ pour calculer nos complexités, on aura trouvé l'allure de la complexité de notre algorithme sans trop de soucis.

Pour qu'un algorithme puisse avoir des complexité différentes selon les entrées il est **nécessaire** qu'il possède des boucles sinon on pourra toujours borner sa complexité par un $\mathcal{O}(1)$. Regardons un peu comment calculer rapidement ces complexités dans les cas simples où les boucles sont indépendantes.

## Complexité blocs et boucles

### Complexité d'une boucle simple

Par exemple :

```pseudocode
tant que <condition>:
    # bloc d'instructions
```

{% note "**Complexité d'une boucle tant que**" %}

<div>
$$
\mathcal{O}(\text{nombre de fois où la condition est remplie}) \cdot (\mathcal{O}(\text{complexité de la vérification de la condition}) + \mathcal{O}(\text{complexité des instructions du bloc}))
$$
</div>
{% endnote %}

Souvent, $\mathcal{O}$(complexité de la vérification de la condition) sera égal à $\mathcal{O}(1)$ et on pourra ne pas en tenir compte dans le calcul. C'est le cas, entre autres, pour une boucle `pour chaque`{.language-} :

```pseudocode
pour chaque e de <structure itérable>:
    # bloc d'instructions
```

{% note "**Complexité d'une boucle pour chaque**" %}

<div>
$$
\mathcal{O}(\text{nombre d'éléments de la structure}) \cdot \mathcal{O}(\text{complexité du bloc d'instructions})
$$
</div>
{% endnote %}

Si le bloc d'instructions est une suite d'instructions de complexité $\mathcal{O}(1)$, on pourra ne pas en tenir compte dans le calcul et la complexité est alors égale à la taille de la structure.

Exemple le calcul de :

<div>
$$
\sum\limits_{1\leq i \leq n}i
$$
</div>

```pseudocode/
algorithme somme(int n):
    ref total ← 0
    pour chaque i de [1 .. n]:
        total ← i + j
    rendre total
```

Lignes à ligne :

1. affectation des paramètres : $\mathcal{O}(1)$
2. création et affectation d'une variables : $\mathcal{O}(1)$
3. une boucle de $n$ itérations : $\mathcal{O}(n)$ itérations
4. opération élémentaire et affectation : $\mathcal{O}(1)$
5. retour d'algorithme : $\mathcal{O}(1)$

On en conclut que la complexité totale de l'algorithme vaut :

<div>
$$
\underbracket{\mathcal{O}(1)}_{\mbox{ligne 1}} + \underbracket{\mathcal{O}(1)}_{\mbox{ligne 2}} + \underbracket{\mathcal{O}(n)}_{\mbox{boucle en i}} \cdot \underbracket{\mathcal{O}(1)}_{\mbox{ligne 4}} + \underbracket{\mathcal{O}(1)}_{\mbox{ligne 5}}
 = \mathcal{O}(1)
$$
</div>


{% retenir %}
Si le bloc d'instructions est une suite d'instructions de complexité $\mathcal{O}(1)$ et que la vérification de la fin de la boucle est $\mathcal{O}(1)$, la complexité de la boucle est égale au nombre de fois où l'on effectue la boucle.
{% endretenir %}


À vous :

{% exercice %}
Calculez la complexité de [l'algorithme qui calcule le nombre d'occurrences](../../1-algorithme/projet/#algorithme-nombre-occurrences) :

```pseudocode/
algorithme nombre(T: []int, x: int) → int:
    ref nb ← 0
    pour chaque e de T:
        si e == x:
            nb ← nb + 1
    rendre nb
```
{% endexercice %}
{% details "corrigé" %}
Ligne à ligne :

1. affectation des paramètres : $\mathcal{O}(1)$
2. une affectation : $\mathcal{O}(1)$ opérations
3. une boucle de $T.\mbox{\small longueur}$ itérations : $\mathcal{O}(T.\mbox{\small longueur})$ opérations
4. un test : $\mathcal{O}(1)$ opérations
5. une affectation : $\mathcal{O}(1)$ opérations
6. retour en $\mathcal{O}(1)$ opération

Le bloc constitué des lignes 4 et 5 est effectué $T.\mbox{\small longueur}$ fois, la complexité totale est donc en :

<div>
$$
\underbracket{\mathcal{O}(1)}_{\mbox{ligne 1}} + \underbracket{\mathcal{O}(1)}_{\mbox{ligne 2}} + \underbracket{\mathcal{O}(T.\mbox{\small longueur})}_{\mbox{nombre d'itérations}} \cdot (\underbracket{\mathcal{O}(1)}_{\mbox{test}} + \underbracket{\mathcal{O}(1)}_{\mbox{ligne 5}}) + \underbracket{\mathcal{O}(1)}_{\mbox{ligne 6}} = \mathcal{O}(T.\mbox{\small longueur})
$$
</div>

{% enddetails %}

### Boucles imbriquées indépendantes

Par exemple :

```pseudocode
boucle 1 exécutée n1 fois:
    boucle 2 exécutée n2 fois:
        ...
            boucle i exécutée ni fois:
                # bloc d'instructions
```

On peut utiliser la règle précédente de façon récursive, la partie $\mathcal{O}$(complexité du bloc d'instructions) contenant elle-même une ou plusieurs boucles :

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

```pseudocode/
algorithme somme2(int n):
    ref total ← 0
    pour chaque i de [1 .. n]:
        pour chaque j de [1 .. n]:
            total ← i + j
    rendre total
```

Faisons une dernière fois l'analyse ligne à ligne :

1. affectation des paramètres : $\mathcal{O}(1)$
2. création et affectation d'une variables : $\mathcal{O}(1)$
3. une boucle de $n$ itérations : $\mathcal{O}(n)$ itérations
4. une boucle de $n$ itérations : $\mathcal{O}(n)$ itérations
5. opération élémentaire et affectation : $\mathcal{O}(1)$
6. retour d'algorithme : $\mathcal{O}(1)$

On en conclut que la complexité totale de l'algorithme vaut :

<div>
$$
\underbracket{\mathcal{O}(1)}_{\mbox{lignes 1 et 2}} + \underbracket{\mathcal{O}(n)}_{\mbox{boucle en i}} \cdot \underbracket{\mathcal{O}(n)}_{\mbox{boucle en j}} \cdot \underbracket{\mathcal{O}(1)}_{\mbox{bloc interne de la ligne 5}} + \underbracket{\mathcal{O}(1)}_{\mbox{lignes 6}}
 = \mathcal{O}(n^2)
$$
</div>

{% retenir %}
Compter le nombre d'itérations d'une boucle avec les $\mathcal{O}()$. Une boucle de $n-3$ exécutions pouvant être avantageusement remplacée par $\mathcal{O}(n)$
{% endretenir %}

À vous :

{% exercice %}
Calculez la complexité de l'algorithme suivant qui calcule le nombre de couples $(i, j)$ ayant une somme donnée :

```pseudocode/
algorithme nombre2(T1: []int, T2: []int, x: int) → int:
    ref nb ← 0
    pour chaque e1 de T1:
        pour chaque e2 de T2:
            si e1 + e2 == x:
                nb ← nb + 1
    rendre nb
```
{% endexercice %}
{% details "corrigé" %}
Ligne à ligne :

1. affectation des paramètres : $\mathcal{O}(1)$
2. une affectation : $\mathcal{O}(1)$ opérations
3. une boucle de $T.\mbox{\small longueur}$ itérations : $\mathcal{O}(T.\mbox{\small longueur})$ opérations
4. une boucle de $T.\mbox{\small longueur}$ itérations : $\mathcal{O}(T.\mbox{\small longueur})$ opérations
5. un test : $\mathcal{O}(1)$ opérations
6. une affectation : $\mathcal{O}(1)$ opérations
7. retour en $\mathcal{O}(1)$ opération

Le bloc constitué des lignes 3, 4 et 5 est effectué $T.\mbox{\small longueur}$ fois, et celui constitué des lignes 4 et 5 $T.\mbox{\small longueur}$ fois. La complexité totale est donc :

<div>
$$
\underbracket{\mathcal{O}(1)}_{\mbox{lignes hors itération}} + \underbracket{\mathcal{O}(T.\mbox{\small longueur})}_{\mbox{nombre d'itérations bloc externe}} \cdot \underbracket{\mathcal{O}(T.\mbox{\small longueur})}_{\mbox{nombre d'itération bloc interne}} \cdot \underbracket{\mathcal{O}(1)}_{\mbox{bloc intérieur}} = \mathcal{O}(T.\mbox{\small longueur}^2)
$$
</div>


{% enddetails %}

### Règle des polynômes

Lorsque l'on travaille avec des blocs s'exécutant un nombre $n$ variable de fois, tout se passe comme si on travaillait avec des polynômes. Si le paramètre du calcul de la complexité vaut $n$ on peut voir :

- la complexité $C(n)$ d'un bloc comme un polynôme,
- le nombre $P(n)$ de fois où le bloc est exécuté est aussi un polynôme

La complexité totale vaut le produit de polynôme $C(n) \cdot P(n)$.

L'utilisation des comparaisons asymptotiques va encore une fois grandement nous aider car elles ont des propriétés très sympathiques pour les polynômes :

{% note "**Règle des polynômes**" %}
- $\mathcal{O}(N^p) \Rightarrow \mathcal{O}(N^q)$ pour $p \leq q$
- $\Omega(N^q) \Rightarrow \Omega(N^p)$ pour $p \leq q$
{% endnote %}
{% details "preuve", "open" %}
On ne va faire la démonstration qu'avec les $\mathcal{O}$, le raisonnement est identique pour les $\Omega$.


Soit $f(N) = \mathcal{O}(N^p)$. Il existe donc $c_0$ et $N_0$ tels que $f(N) \leq c_0 \cdot N^p$ pour $N > N_0$.

Comme $1 < 2 \cdot N^\alpha$ pour $\alpha \geq 0$ et $N> 1$, on a $N^p \leq N^p \cdot (2 \cdot N^{q-p}) = c_0 \cdot N^q$ pour $c_0 = 2$, $N > 1 = N_0$ et $p \leq q$. Donc $N^p = \mathcal{O}(N^q)$ pour tout $p \leq q$

{% enddetails %}

Et pour les $\Theta$ :

{% note "**Proposition**" %}

On a :

<div>
$$
\sum_{i=0}^na_i x^i = \Theta(x^n) \mbox{ si } a_n \neq 0
$$
</div>
{% endnote %}
{% details "preuve", "open" %}

Comme $x^i = \mathcal{O}(x^{j})$ et $x^{j} = \Omega(x^i)$ pour tous $i \leq j$, on peut facilement montrer que $\Theta(x^i) + \Theta(x^{i + 1}) = \Theta((x^{i + 1}))$. En itérant l'égalité précédente on obtient $\sum_{i=0}^n\Theta(x^i) = \Theta(x^n)$ ce qui permet de conclure puisque $\sum_{i=0}^na_i x^i = \Theta(\sum_{i=0}^na_i x^i) = \sum_{i=0}^n\Theta(x^i)$.

{% enddetails %}

## <span id="dichotomie"></span>Exemple 1 : Recherche dichotomique

Le principe de [la recherche dichotomique](https://fr.wikipedia.org/wiki/Recherche_dichotomique){.externe} permet de savoir si un entier donné est dans un tableau d'entiers trié.

On cherche à savoir si l'entier $x$ est entre les indices $a$ et $b \geq a$ d'un tableau d'entiers $T$. On procède récursivement selon la valeur de $T[\lfloor (a + b)/2 \rfloor]$ :

- si $T[\\,\lfloor (a + b)/2 \rfloor\\,] = x$ on a trouvé l'élément
- si $T[\\,\lfloor (a + b)/2 \rfloor\\,] > x$, l'indice recherché est forcément **avant** $\lfloor (a + b)/2 \rfloor$. On recommence alors la procédure avec :
  - $a$ inchangé
  - $b = \\,\lfloor (a + b)/2 \rfloor\\, - 1$
- si $T[\\,\lfloor (a + b)/2 \rfloor\\,] < x$, l'indice recherché est forcément **après** $\lfloor (a + b)/2 \rfloor$. On recommence alors la procédure avec :
  - $a = \lfloor (a + b)/2 \rfloor + 1$
  - $b$ inchangé

Ce principe donne l'algorithme suivant :

<span id="algorithme-dichotomie"></span>

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

Commençons par se persuader qu'il fonctionne (et commencer à se forger une intuition de son fonctionnement) avec de petits exemples :

{% faire %}
Déroulez l'algorithme `recherche_dichotomique(T: []int, x: int) → bool`{.language-} pour ces différentes valeurs de `T`{.language-} et de `x`{.language-} :

- `T = [1, 3, 7]`{.language-} et `x = 7`{.language-} ou `x = 8`{.language-} l'algorithme fonctionne
- `T =[1, 3, 3, 7]`{.language-} et `x = 7`{.language-} ou `x = 9`{.language-} l'algorithme fonctionne
{% endfaire %}

On peut maintenant passer à sa preuve :

{% exercice %}
Démontrez que l'algorithme `recherche_dichotomique(T: []int, x: int) → bool`{.language-} :

- termine quelles que soient ses entrées,
- est bien un algorithme de recherche.
{% endexercice %}
{% details "corrigé" %}

- **finitude**. La quantité entière `b - a`{.language-} **décroît strictement** à chaque itération, elle sera donc strictement négative après un nombre fini d'opérations et l'algorithme s'arrêtera.
- **preuve** :
  1. on montre trivialement l'invariant de boucle suivant : si `x`{.language-} est dans `T`{.language-}, alors sa position est plus grande ou égale à `a`{.language-} et plus petite ou égale à `b`{.language-}
  2. si l'on sort de la boucle l'invariant est toujours vérifié mais comme `a`{.language-} > `b`{.language-}, `x`{.language-} ne peut être dans `T`{.language-}

Les remarques ci-dessus prouvent que l'algorithme `recherche_dichotomique`{.language-} fonctionne.
{% enddetails %}

{% exercice %}
Démontrez que la complexité de l'algorithme `recherche_dichotomique(T: []int, x: int) → bool`{.language-} vaut $\mathcal{O}(K)$ avec $K$ le nombre de fois où l'algorithme rentre dans la boucle `tant que`{.language-}

{% endexercice %}
{% details "corrigé" %}

Étudions sa complexité. Ligne à ligne :

1. initiation de la fonction $\mathcal{O}(1)$
2. affectation : $\mathcal{O}(1)$
3. affectation : $\mathcal{O}(1)$
4. —
5. boucle de $K$ itérations (pour l'instant, la valeur de $K$ est **inconnue**)
6. affectation : $\mathcal{O}(1)$
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
{% enddetails %}

Avant de conclure, démontrons une petite proposition qui sera utile tout au long de ce cours :

<div id="proposition-log"></div>

{% note "**Proposition**" %}
Le plus grand entier $k$ tel que $\frac{n}{p^k} \geq 1$ pour deux entiers $n\geq p$ vaut $k = \lfloor\log_p(n)\rfloor$.
{% endnote %}
{% details "preuve", "open" %}

Le nombre $k$ recherché est tel que $p^k \leq n < p^{k + 1}$. On a alors :

<div>
$$
\begin{array}{lcccl}
    p^k &\leq &n &<& p^{k + 1}\\
    \log_p(p^k) &\leq & \log_p(n) &< &\log_p(p^{k + 1}) \mbox{ (car la fonction $\log_p$ est croissante)} \\
    k\cdot \log_p(p) &\leq & \log_p(n) &< &(k + 1)\cdot \log_p(p) \\
    k &\leq &\log_p(n) &<& k + 1
\end{array}
$$
</div>
{% enddetails %}

La proposition précédente nous permet de conclure sur la complexité :

{% exercice %}
Démontrez que la complexité de l'algorithme `recherche_dichotomique(T: []int, x: int) → bool`{.language-} vaut $\mathcal{O}(\ln(T.\mbox{\small longueur}))$.

{% endexercice %}
{% details "corrigé" %}
Comme à chaque itération, `b - a`{.language-} est divisé par 2, il y a autant d'itérations que l'on peut diviser $T.\mbox{\small longueur}$ par 2, donc au plus $\log_2(T.\mbox{\small longueur}) + 1$ itérations. Comme $\log_2(n) = \frac{\ln(n)}{\ln(2)}$ on a bien la complexité recherchée.

{% enddetails  %}

Cette complexité est vraiment très bonne puisque la valeur de $\ln(n)$ est en effet très petite devant $n$.

<div id="importance-log"></div>

{% retenir %}
Pour se fixer les idées, et comme tous les log sont proportionnels, pensez à la différence entre :

- $t = 4.35 \cdot 10^{17}$ secondes qui est l'âge estimé de l'univers ($1.38 \cdot 10^8$ siècles),
- $\log_{10}(t) \simeq 17.65$ secondes qui est la durée moyenne que prend un mammifère pour faire pipi (on peut en effet estimer cette durée à 21s±13s selon une étude menée par Yang et Hu en 2014 et qui a été récompensée par le [Ig Nobel](https://fr.wikipedia.org/wiki/Prix_Ig-Nobel){.externe} de physique en 2015)
{% endretenir %}

En conclusion si l'on manipule des tableaux triés la recherche dichotomique est énormément plus performante que la recherche naïve.

## Boucles imbriquées dépendantes

### <span id="règle-croissance"></span>Boucles dépendantes mais monotones

Il arrive souvent que les boucles imbriquées d'un algorithme soient dépendantes les unes des autres. Dans le cas général on ne peut pas factoriser le calcul de la complexité et il faut alors dérouler tout l'algorithme en additionnant les complexités de chaque ligne comme s'il n'y avait pas de boucles.

Il existe cependant un cas pratique (et qui arrive assez souvent) où l'on peut factoriser : lorsqu'une boucle s'exécute un nombre variable de fois, mais que cette variation est croissante (_respectivement_ décroissante). Par exemple (notez la dépendance de $j$ par rapport à $i$) :

<div>
$$
\sum\limits_{1\leq i \leq n}(\sum\limits_{i < j \leq n} (i+j))
$$
</div>

```pseudocode
algorithme somme3(int n):
    ref total ← 0
    pour chaque i de [1 .. n-1]:
        pour chaque j de [i+1 .. n]:
            total ← i + j
    affiche total
```

Le nombre de fois où la boucle en $j$ est exécutée est un nombre variable de fois qui dépend de la valeur de $i$. Comme $i$ va croître, le nombre de fois où cette boucle va s'exécuter va décroître. Si l'on applique la règle on peut dire qu'elle va s'exécuter de l'ordre de $\mathcal{O}(n)$ fois comme dans l'exemple de la partie précédente. La complexité de l'algorithme est donc de $\mathcal{O}(n^2)$.

Refaisons le calcul en décomposant toutes les instructions, comme on le ferait dans le cas général, pour voir que notre règle est valide (et donnera aussi une idée de la preuve de cette règle) :

- ligne 1 + 2 : $\mathcal{O}(1)$
- itération pour $i=1$:
  - ligne 3 : une affectation $i=1$ : $\mathcal{O}(1)$
  - boucle pour $j=1$:
    - ligne 4 : une affectation de $j$ : $\mathcal{O}(1)$
    - ligne 5 : $\mathcal{O}(1)$
    - le tout $n-1$ fois
- itération pour $i=2$:
  - ligne 3 : une affectation $i=2$ : $\mathcal{O}(1)$
  - boucle pour $j=2$:
    - ligne 4 : une affectation de $j$ : $\mathcal{O}(1)$
    - ligne 5 : $\mathcal{O}(1)$
    - le tout $n-2$ fois
- ...
- itération pour $i=n-1$:
  - ligne 3 : une affectation $i=n-1$ : $\mathcal{O}(1)$
  - boucle pour $j=n-1$:
    - ligne 4 : une affectation de $j$ : $\mathcal{O}(1)$
    - ligne 5 : $\mathcal{O}(1)$
    - le tout $1$ fois
- ligne 6 : $\mathcal{O}(1)$

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

Cet exemple se généralise :

{% note "**Complexité de boucles dépendantes monotones**" %}
Si une boucle s'exécute un nombre croissant (respectivement décroissant) de fois, on peut considérer pour le calcul de la complexité qu'elle s'exécute à chaque fois de l'ordre de son maximum et se ramener au cas [des boucles indépendantes](./#complexité-boucles-indépendantes).
{% endnote %}

À vous :

{% exercice %}
Calculez la complexité de l'algorithme suivant qui calcule le nombre de paires $\\{i, j\\}$ ayant une somme donnée :

```pseudocode/
algorithme nombre3(T: []int, x: int) → int:
    ref nb ← 0
    pour chaque i de [0 .. T.longueur-1[:
        e1 = T[i]
        pour chaque e2 de T[i+1:]: 
            si e1 + e2 == x:
                nb ← nb + 1
    rendre nb
```
{% endexercice %}
{% details "corrigé" %}
Ligne à ligne :

1. affectation des paramètres : $\mathcal{O}(1)$
2. une affectation : $\mathcal{O}(1)$ opérations
3. une boucle de $T.\mbox{\small longueur}$ itérations : $\mathcal{O}(T.\mbox{\small longueur})$ opérations
4. un test : $\mathcal{O}(1)$ opérations
5. une affectation : $\mathcal{O}(1)$ opérations
6. retour en $\mathcal{O}(1)$ opération

Les lignes 2, 3 et 4 sont effectuées $T.\mbox{\small longueur}$ fois, la complexité totale est donc en :


{% enddetails %}

### Cas général

Dans le cas général, on peut toujours utiliser notre approximation précédente et multiplier les nombres maximum d'itérations pour obtenir un majorant de notre complexité. Mais il se peut que l'on surestime grandement la complexité comme dans l'exemple suivant :

<div>
$$
\sum\limits_{i=1}^n\sum\limits_{j=1}^i\sum\limits_{k=1}^{n/i}(i+j+k)
$$
</div>

```pseudocode/
algorithme somme4(n):
    ref ref nb ← 0
    pour chaque i de [1, n]:
        pour chaque j de [1, i]:
            pour chaque k de [1, n / i]:
                nb ← i + j + k
    rendre nb
```

Commençons par utiliser nos approximations :

- boucle en `i`{.language-} $\mathcal{O}(n)$ itérations au maximum,
- boucle en `j`{.language-} $\mathcal{O}(n)$ itérations au maximum, lorsque $i = 1$,
- boucle en `k`{.language-} $\mathcal{O}(n)$ itérations au maximum, lorsque $i = 1$,

On en conclut que la complexité de l'algorithme est en $\mathcal{O}(n^3)$. Ce résultat est **forcément** juste, mais peut-être pourrait-on trouver une meilleurs approximation.

Examinons le nombre de fois où chaque boucle est exécutée selon la valeur de $i$ :

- $i = 1$ : 
  - la boucle en $j$ est exécutée 1 fois
  - la boucle en $k$ est exécutée $n$ fois
- $i = 2$ : 
  - la boucle en $j$ est exécutée 2 fois
  - la boucle en $k$ est exécutée $\lfloor n / 2\rfloor$ fois
- ...
- $i$ : 
  - la boucle en $j$ est exécutée $i$ fois
  - la boucle en $k$ est exécutée $\lfloor n / i\rfloor$ fois
- ...
- $i = n$ : 
  - la boucle en $j$ est exécutée $n$ fois
  - la boucle en $k$ est exécutée $1$ fois

Comme la complexité de la ligne 6 est en $\mathcal{O}(1)$ on en déduit que la complexité $C(n)$ de notre algorithme vaut :

<div>
$$
C(n) = \sum\limits_{i=1}^n((i \cdot n/i) \cdot \mathcal{O}(1)) = \sum\limits_{i=1}^n( n \cdot \mathcal{O}(1)) = \sum\limits_{i=1}^n( \mathcal{O}(n)) = \mathcal{O}(n) \cdot \sum\limits_{i=1}^n 1 = \mathcal{O}(n^2)
$$
</div>

Lorsque le nombre d'itérations en $j$ augmente celle en $k$ diminue et leur produit est toujours de l'ordre de $\mathcal{O}(n)$ pour une complexité totale quadratique plutôt que cubique !

{% retenir %}
Pour calculer la complexité d'imbrication complexe de boucles, on écrit une à une toutes les instructions exécutés les une après les autres, comme s'il n'y a avait pas de boucles.

On peut ensuite additionner ces complexités pour obtenir la complexité exacte de l'algorithme.
{% endretenir %}


À vous :

{% exercice %}
Calculez la complexité de l'algorithme suivant qui calcule le nombre de paires $i \leq j$ telles que $\sum(T[i:j]) = x$ :

```pseudocode/
algorithme nombre4(T: []int, x: int) → int:
    ref nb ← 0
    ref s int
    pour chaque i de [0 .. T.longueur - 1[:
        pour chaque j de [i .. T.longueur]:
            s ← 0
            pour chaque e de T[i:j]:
                s ← s + e
            si s == x:
                nb ← nb + 1
    rendre nb
```

{% endexercice %}
{% details "corrigé" %}

Le boucle en $e$ va s'exécuter 1 fois pour tous les intervalles de $[1 .. T.\text{\small longueur}]$ c'est à dire de l'ordre de $\mathcal{O}(T.\text{\small longueur}^2)$ fois.

Comme les lignes 1 à 3 vont s'exécuter 1 fois et les lignes 6, 9 et 10 $\mathcal{O}(T.\text{\small longueur}^2)$ fois la complexité totale de l'algorithme vaut $\mathcal{O}(T.\text{\small longueur}^2)$.

{% enddetails %}

## Exemple 2 : plus longue sous-séquence croissante.

Pour illustrer les boucles imbriquées on va étudier l'algorithme suivant qui rend la longueur $k$ de la plus grande suite strictement positives d'indice $i_1 < i_2 < \dots < i_k$ telle que $T[i_1] \leq \dots \leq T[i_j] \leq \dots \leq T[i_k]$.

Par exemple si $T = [5, 2, 8, 6, 3, 6, 2, 9, 7]$, une plus longueur sous-suite strictement croissante vaut : $[2, 3, 6, 9]$, mais il y en a d'autres comme par exemple $[2, 3, 6, 7]$.

On pourrait essayer de chercher toutes les sous-suites strictement croissantes puis de prendre la plus grande, mais il peut y en avoir beaucoup puisque si $T$ est déjà trié toute suite strictement croissante de $[1 .. n]$ va fonctionner et il y en a $\sum_{k=0}^n\binom{n}{k} = 2^n$ (puisque $(1 + 1)^n = \sum_{k=0}^n\binom{n}{k}1^{k}\cdot 1^{n-k}$).

On peut en revanche se poser la question suivante : "quelle est la longueur de la plus longue sous-séquence strictement croissante finissante en $T[-1]$ ?". Et ceci est bien plus facile à faire puisque ce problème satisfait la récursion suivante :

- soit $T$ est de longueur 1 et la réponse est 1
- soit la réponse correspond au maximum des des réponses pour les tableaux $T[:i+1]$ plus 1, pour tout $i$ tel que $T[i] < T[-1]$.

Ce s'écrit en pseudo-code ainsi :

```pseudocode
algorithme max_sous_séquence_fin(T: []int)  → int:
    si T.longueur == 1:
        rendre 1
    
    ref n ← 1
    ref temp int
    pour chaque i de [0 .. T.longueur-1[:
        si T[i] < T[-1]:
            temp ← max_sous_séquence_fin(T[:i+1])
            si temp ≥ n:
                n ← temp + 1
    rendre n
```

Et on en déduit l'algorithme suivant :

```pseudocode
algorithme max_sous_séquence(T: []int)  → int:
    ref n ← max_sous_séquence_fin(T)
    ref temp int
    pour chaque i de [0 .. T.longueur - 1[:
            temp ← max_sous_séquence_fin(T[:i+1])
            si temp ≥ n:
                n ← temp + 1
    rendre n
```

Mais cet algorithme est loin d'être optimal. Par exemple pour notre tableau : $T = [5, 2, 8, 6, 3, 6, 2, 9, 7]$ on va recalculer `max_sous_séquence_fin(T[:i+1])`{.language-} pour $0\leq i \leq 6$ lors du calcul de `max_sous_séquence_fin(T[:7+1])`{.language-} et de `max_sous_séquence_fin(T[:8+1])`{.language-}. Et ce n'est pas la seule répétition !

Pour éviter tous ces re-calculs on va utiliser [la mémoïsation](https://fr.wikipedia.org/wiki/M%C3%A9mo%C3%AFsation) : on stocke les valeurs déjà calculées ce qui permet d'écrire l'algorithme itératif suivant :

```pseudocode/
algorithme max_sous_séquence(T: []int)  → int:
    ref memoisation ← [1 pour _ dans [0 .. T.longueur[] 

    pour chaque i de [0 .. T.longueur[:
        pour chaque j de [0 .. i[:
            si (T[j] < T[i]) ET (memoisation[j] + 1 > memoisation[i]):
                memoisation[i] ← memoisation[j] + 1
    
    rendre max(memoisation)
```

Toute notre analyse montre clairement que `memoisation[i] = max_sous_séquence_fin(T[:i+1])`{.language-} ce qui prouve notre algorithme. Reste à en calculer la complexité. 

- la ligne 2 de l'algorithme est en $\mathcal{O}(T.\text{small longueur})$ puisque l'on crée un tableau.
- on a deux boucle imbriquées mais monotones, [la règle de croissance monotone](./#règle-croissance) nous indique que l'on va répéter $\mathcal{O}(T.\text{small longueur}) \cdot \mathcal{O}(T.\text{small longueur}) = \mathcal{O}(T.\text{small longueur}^2)$ fois le bloc intérieur
- le bloc intérieur est en $\mathcal{O}(1)$
- le retour intérieur est en $\mathcal{O}(n)$ puisqu'il faut prendre le max d'un tableau

On en conclut que si $n$ est la longueur du tableau en entrée, la complexité de l'algorithme vaut :

<div>
$$
C(n) = \mathcal{O}(n) + \mathcal{O}(n^2) + \mathcal{O}(n) = \mathcal{O}(n^2)
$$
</div>

En stockant $n$ valeurs intermédiaires on a grandement accéléré l'algorithme.

{% retenir %}
La **_mémoïsation_** est une illustration du [principe du compromis temps-mémoire](https://simple.wikipedia.org/wiki/Space-time_tradeoff) qui fait gagner du temps en stockant les valeurs intermédiaires.

Si l'on a peut de valeurs à stocker par rapport au gain, cela vaut le coup !
{% endretenir %}

## <span id="règle-récursif"></span>Complexité d'algorithmes récursifs

Un algorithme récursif est un algorithme qui s'appelle lui-même jusqu'à ce qu'on arrive à une condition d'arrêt qui stoppe la récursion. 

{% retenir "**Quand utiliser**" %}
Pour calculer la complexité d'un algorithme récursif.
{% endretenir %}



{% note "**Complexité d'un algorithme récursif**" %}
Pour calculer la complexité d'un algorithme récursif en fonction de la taille $n$ de l'entrée, on pose que $C(n)$ est la complexité et l'on utilise cette fonction pour estimer la complexité des appels récursifs. Une fois les complexités des éléments d'arrêt estimées, trouver $C(n)$ revient à résoudre une équation de récurrence.
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


L'équation de récurrence $C(n) = \mathcal{O}(1) + C(n-1)$ peut se résoudre en y ajoutant notre condition d'arrêt (obtenue pour `n`{.language-} valant 1) qui va nous donner $C(1) = \mathcal{O}(1)$ comme condition limite :

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

À vous :

{% exercice %}
Calculez la complexité de [l'algorithme qui calcule le nombre d'occurrences](../../1-algorithme/projet/#algorithme-nombre-occurrences) mais de façon récursive :

```pseudocode/
algorithme nombre_rec(T: []int, x: int, i: int) → int:
    si i ≥ T.longueur:
        rendre 0
    si T[i] == x:
        rendre 1 + nombre_rec(T, x, i + 1)
    sinon:
        rendre nombre_rec(T, x, i + 1)

algorithme nombre(T: []int, x: int) → int:
    rendre nombre_rec(T, x, 0)
```
{% endexercice %}
{% details "corrigé" %}

L'équation de complexité de l'algorithme `nombre_rec`{.language-} est :

<div>
$$
\left\{
    \begin{array}{lcl}
        C(n, i) & = & \mathcal{O}(1) + C(n, i+1)\\
        C(n, n) & = & \mathcal{O}(1)
    \end{array}
\right.
$$
</div>

Elle va se résoudre comme l'équation $C_r(n) = \mathcal{O}(1) + C_r(n-1)$ puisque $i$ ne fait qu'augmenter. On obtient $C_r(n, i) = \mathcal{O}(n-i)$ et donc l'algorithme `nombre`{.language-} est de complexité $C(n) = C_r(n, 0) = \mathcal{O}(n)$.

{% enddetails %}

## Exemple 3 : calcul du pgcd

On ne peut pas toujours trouver une équation de récurrence fonctionnant pour toutes les entrées. Mais comme le calcul de complexité ne s'intéresse qu'au cas le pire, il suffit de trouver une relation pour des données engendrant le plus d'instructions. Pour illustrer cela, nous allons considérer deux algorithmes permettant de calculer le pgcd de deux nombres.

### Itératif

Reprenons un de nos algorithmes fil rouge, [l'algorithme du pgcd itératif](../../1-algorithme/pseudo-code/récursifs-itératifs/#algorithme-pgcd) :

```pseudocode/
algorithme pgcd(a: int, b: int) → int:  # a, b ≥ 0
    tant que min(a, b) > 0:
        a, b ← max(a, b) - min(a, b), min(a, b)
    rendre max(a, b)
```

En notant $K$ le nombre d'itérations de la boucle tant que, comme toutes les lignes sont en $\mathcal{O}(1)$ opérations, la complexité $C(a, b)$ de l'algorithme vaut :

<div>
$$
C(a, b) = K \cdot \mathcal{O}(1)
$$
</div>

On ne peut pas simplifier car $K$ dépend de $a$ et de $b$. À chaque itération soit $a$ soit $b$ va décroître strictement jusqu'à ce que $\min(a, b) = 0$ ce qui stoppera la boucle.

Donc au bout de $K = \mathcal{O}(\max(a, b))$ itérations on aura forcément soit $a$ soit $b$ qui vaudra 0 (pas la peine d'être plus précis que cela) :

<div>
$$
C(a, b) = \mathcal{O}(\max(a, b))
$$
</div>

### Récursif

Reprenons l'exemple de [l'algorithme du pgcd récursif](../../1-algorithme/pseudo-code/récursifs-itératifs/#algorithme-pgcd-rec) :

```pseudocode
algorithme pgcd(a: int, b: int) → int:  # a, b ≥ 0
    si min(a, b) == 0:
        rendre max(a, b)
    sinon:
        rendre pgcd(max(a, b) - min(a, b), min(a, b))
```

La complexité de cet algorithme dépend de ses paramètres, notons-la : $C(a, b)$. Comme toutes les opérations hors récursion sont en $\mathcal{O}(1)$ opérations on obtient l'équation de récurrence :

<div>
$$
C(a, b) = \mathcal{O}(1) + C(\max(a, b) - \min(a, b), \min(a, b))
$$
</div>

En itérant sur cette équation comme on l'a fait précédemment avec le calcul de la complexité de l'algorithme factorielle récursif on obtient :

<div>
$$
C(a, b) = K(a, b) \cdot \mathcal{O}(1)
$$
</div>

Où $K(a, b)$ est le nombre de récursions de l'algorithme avec les paramètres $a$ et $b$. De même que pour l'algorithme itératif soit $a$ soit $b$ va décroître strictement à chaque récursion, donc $K(a, b) \leq \max(a, b)$, ce qui implique :

<div>
$$
C(a, b) = K(a, b) \cdot \mathcal{O}(1) \leq \max(a, b) \cdot \mathcal{O}(1) = \mathcal{O}(\max(a, b))
$$
</div>

Comme les $\mathcal{O}$ sont des majorants, on a donc également $C(a, b) = \mathcal{O}(\max(a, b))$.









---
layout: layout/post.njk

title: "Projet : Algorithmes classiques de recherche"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les trois exercices sont des variations d'algorithme cherchant un élément particulier dans un tableau. Ils sont fondamentaux pour le calcul de complexités, en particulier la complexité en moyenne.

Apprenez les car ils sont souvent utilisés comme briques d'algorithmes plus complexes. Apprenez également les méthodes utilisés pour leurs calculs de complexité : elles vous permettront de vous en sortir pour une grande majorité des calculs que vous aurez besoin de faire.

{% attention %}
Ces exercices sont plus durs que ceux précédemment vus et sont de difficulté croissante. Donc :

1. commencez par faire et intégrer les exercices précédents,
2. faites ces exercices, quite à regarder les solutions, et comprenez les raisonnements fait. 
3. ajoutez à votre besace de techniques et méthodes de calcul de complexité les différentes astuces et outils utilisés ici.
{% endattention %}

## <span id="dichotomie"></span>Recherche dichotomique

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

Cette complexité est vraiment très bonne ! La valeur de $\ln(n)$ est en effet très petite devant $n$. 
> TBD rappelez vous (partie complexité en moyenne)


## <span id="sous-mot"></span> Recherche de sous-mots

On va analyser un algorithme permettant de rechercher des sous-mots d'[un mot d'un alphabet $\mathcal{A}^\star$](../../1-algorithme/bases-théoriques/définition/#définition-mot). Si $m = m_0 \dots m_p$ est un mot de $\mathcal{A}^\star$, un mot $n = n_0\dots n_q$ est un sous-mot de $m$ s'il existe $0\leq i \leq p - q$ tel que $m_{i + k} = n_{k}$ pour tous $0\leq k \leq q$.

<div id="algorithme-sous-mot"></div>

```pseudocode/
algorithme sous_mot(m: str, n: str)  → bool:
    ref j ← 0
    si n.longueur > m.longueur:
        rendre Faux
    pour chaque i de [0 .. m.longueur - n.longueur]:
        tant que (j < n.longueur) ET (m[i + j] == n[j]):
            j ← j + 1
        si j == n.longueur:
            rendre Vrai
        sinon:
            j ← 0
    rendre Faux
```

Notez que l'algorithme `sous_mot(m: str, n: str)  → bool`{.language-} ne plantera jamais grâce à l'utilisation de l'instruction `(j < n.longueur) ET ...`{.language-} ligne 6. En effet, si ce test est faux (donc $j \geq n.\text{\small longueur}$) le pseudocode n'évaluera jamais la partie droite de l'instruction `ET`{.language-} et rendra directement `Faux`{.language-} (une instruction `ET`{.language-} n'est vraie que si sa partie gauche et sa partie droite le sont). De là on garantit que les lectures `m[i + j]`{.language-} et `n[j]`{.language-} seront correctes puisque $m.\text{\small longueur} \geq n.\text{\small longueur}$,  $0 \leq j < n.\text{\small longueur}$ et $0 \leq i \leq  m.\text{\small longueur} - n.\text{\small longueur}$.

{% retenir %} 
Le garde-fou de la ligne 6 s'appelle une **_sentinelle_**. C'est une technique utile à connaître pour simplifier le pseudo-code.
{% endretenir %} 

La remarque précédente nous assurant que le pseudo-code du programme `sous_mot(m: str, n: str)  → bool`{.language-} est correct, à vous de montrer qu'il fait bien ce qu'il est censé faire :

{% exercice %}
Montrez que l'algorithme `sous_mot(m: str, n: str)  → bool`{.language-} rend `Vrai`{.language-} si et seulement si `n`{.language-} est un sous-mot de `m`{.language-}.
{% endexercice %}
{% details "corrigé" %}

Pour démontrer la finitude, il suffit de démontrer que la boucle `tant que`{.language-} se termine puisque la boucle `pour chaque`{.language-} est forcément finie. Ceci est clair car `j`{.language-} est un entier qui vaut toujours 0 au début de la boucle et qui croît strictement à chaque itération.

Il est clair que la boucle `tant que`{.language-} vérifie l'invariant de boucle *à la fin de chaque boucle $m[i +k] = n[k]$ pour tout $0 \leq k < j$*. Comme on n'est sorti de la boucle que si :
- soit $j < n.\text{\small longueur}$ et $m[i + j] \neq n[j]$. Donc $m[i:i+j+1] \neq n[:j+1]$
- soit $j = n.\text{\small longueur}$. Donc $m[i:i+j] = n$

Comme $i$ parcourt tous les débuts possibles de $n$ dans $m$ on en conclut que l'algorithme ne va répondre vrai que si et seulement si $n$ est un sous-mot de $m$.

{% enddetails %}

On peut maintenant déterminer les complexités de notre algorithme.

{% exercice %}

- Donnez la complexité min et max de l'algorithme `sous_mot(m: str, n: str)  → bool`{.language-} à partir de paramètres que vous définirez.
- donnez des exemples pour lesquels la complexité min et max est atteinte.

{% endexercice %}
{% details "corrigé" %}

Si $n.\text{\small longueur} > m.\text{\small longueur}$, l'algorithme s'arrête en $\mathcal{O}(1)$ opérations. On suppose donc dans la suite que $n.\text{\small longueur} \leq m.\text{\small longueur}$. Il y a alors deux façons de sortir de l'algorithme :

- en répondant `Vrai`{.language-} : il faut que `j == n.longueur`{.language-}. Comme `j`{.language-} part de 0 et est incrémenté de 1, il faut au moins $n.\text{\small longueur}$ itérations de la boucle `tant que`{.language-}. Ce minimum est atteint pour les entrées telles que $m$ débute par $n$ : la complexité minimale dans ce cas est en $\mathcal{O}(n.\text{\small longueur})$.
- en répondant `Faux`{.language-} : il faut avoir effectué toutes les $m.\text{\small longueur} - n.\text{\small longueur} + 1$ itérations de la boucle `pour chaque`{.language-}. Ce minimum est atteint si la boucle `tant que`{.language-} n'est jamais exécutée, c'est-à-dire si $m[i] \neq n[0]$ pour tout $0 \leq i \leq m.\text{\small longueur} - n.\text{\small longueur}$ : la complexité minimale dans ce cas est en $\mathcal{O}(m.\text{\small longueur} - n.\text{\small longueur} + 1)$.

La complexité minimale de l'algorithme est donc en $\mathcal{O}(\min(n.\text{\small longueur}, m.\text{\small longueur} - n.\text{\small longueur} + 1))$. Elle peut valoir $\mathcal{O}(1)$, par exemple si $m$ et $n$ ont la même longueur et des premières lettres différentes.

La complexité maximale est atteinte si on fait de l'ordre de $n.\text{\small longueur}$ itérations pour chaque $i$ et vaut $\mathcal{O}(m.\text{\small longueur} \cdot n.\text{\small longueur})$. La complexité maximale est atteinte par exemple pour des mots $m$ valant tout le temps le même caractère, disons `0` et des mots $n$ constitués eux aussi de `0` sauf le dernier de leurs caractères qui vaut `1`.

{% enddetails %}

Les complexités maximale et minimale sont très différentes ! Quelle est alors la complexité en moyenne ? On va utiliser comme d'habitude un modèle uniforme où chaque lettre a la probabilité $p = \frac{1}{\vert \mathcal{A}\vert}$ d'apparaître à chaque position. 

{% exercice %}

Montrez que la complexité en moyenne de l'algorithme `sous_mot(m: str, n: str)  → bool`{.language-} vaut :

<div>
$$
\begin{array}{c}
\mathcal{O}(m.\text{\small longueur} \cdot (\sum\limits_{j=0}^{n.\text{\small longueur}}p^j))
\end{array}
$$
</div>

{% endexercice %}
{% info %}
Vous pourrez utiliser le fait que $\mathbb{E}[Y] = \sum\limits_k P(Y \geq k)$ pour toute variable aléatoire discrète $Y$.
{% endinfo %}
{% details "corrigé" %}
Pour calculer la complexité en moyenne de l'algorithme il faut estimer le nombre de fois moyen où la boucle tant que est exécutée. Notre modèle étant uniforme cela ne dépendra pas de $i$ puisque $P(m[i+j] = n[j]) = p$ quels que soient $i$ et $j$. On en conclut que la probabilité que la boucle tant que soit exécutée au moins $j$ fois vaut : $p^j$.

De là, si $X(m, n)$ est une variable aléatoire qui rend le nombre de fois où l'on est passé dans la boucle `tant que`{.language-}, on a :

<div>
$$
\begin{array}{lclr}
\mathbb{E}[X] &=& \sum\limits_{j=0}^{n.\text{\small longueur}}P(X \geq j) & \text{on a } E[Y] = \sum\limits_k P(Y \geq k) \text{ pour toute variable aléatoire discrète }Y\\
&=&  \sum\limits_{j=0}^{n.\text{\small longueur}} p^j
\end{array}
$$
</div>

Comme ceci arrive pour tout $0 \leq i \leq m.\text{\small longueur} - n.\text{\small longueur}$ on arrive bien à la quantité demandée.

{% enddetails %}

On peut maintenant utiliser le résultat suivant :


<div id="série-géométrique"></div>

{% note "**Proposition**" %}

Pour tout réel $\alpha$ on a :

<div>
$$
\sum_{i=0}^{k}\alpha^i = \frac{1-\alpha^{k+1}}{1-\alpha}
$$
</div>

{% endnote %}
{% details "preuve", "open" %}
Par une récurrence triviale sur $k$. On a bien $\sum_{i=0}^{0}\alpha^i = 1 = \frac{1-\alpha^{0+1}}{1-\alpha}$ et si la proposition est vraie à $k$, on a pour $k+1$ :

<div>
$$
\sum_{i=0}^{k+1}\alpha^i = \sum_{i=0}^{k}\alpha^i + \alpha^{k+1} = \frac{1-\alpha^{k+1}} {1-\alpha} + \alpha^{k+1} = \frac{1-\alpha^{k+2}}{1-\alpha}
$$
</div>


{% enddetails %}

<div id="série-géométrique-limite"></div>


{% note "**Corollaire**" %}

Si $\vert \alpha \vert <1 $ alors pour tout $k$:

<div>
$$
\sum_{i=0}^{k}\alpha^i \leq \lim_{k \to +\infty}\sum_{i=0}^{k}\alpha^i = \frac{1}{1-\alpha}
$$
</div>

{% endnote %}

Pour démontrer le résultat principal de cette partie :


{% exercice %}

Montrez que la complexité en moyenne de l'algorithme `sous_mot(m: str, n: str)  → bool`{.language-} vaut : $\mathcal{O}(m.\text{\small longueur})$

{% endexercice %}
{% details "corrigé" %}

La somme $\sum_{j=0}^{n.\text{\small longueur}}p^j$ de l'équation est bornée par $\frac{1}{1-p}$ qui est une constante dépendant uniquement de l'alphabet et pas des entrées : on peut donc la sortir du $\mathcal{O}$.
{% enddetails %}

Ce résultat est remarquable puisque l'on a que :

- la complexité minimale vaut $\mathcal{O}(\min(n.\text{\small longueur}, m.\text{\small longueur} - n.\text{\small longueur} + 1))$
- la complexité moyenne vaut $\mathcal{O}(m.\text{\small longueur})$
- la complexité maximale vaut $\mathcal{O}(m.\text{\small longueur} \cdot n.\text{\small longueur})$

La complexité maximale est donc très éloignée de la complexité en moyenne !

{% retenir %}
L'argument utilisé dans le dernier exercice est fondamental à retenir. Il sert (assez) souvent pour des calculs fins de complexité.
{% endretenir %}

## $k$-ème plus petit élément

On connaît un algorithme pour trouver le plus petit élément d'un tableau. On s'intéresse ici au moyen de trouver un $k$-ème plus petit élément.

Un $k$-ème plus petit élément $T[i]$ d'un tableau d'entiers $T$ de longueur $n$ est tel que l'on peut séparer les $n-1$ autres éléments de $T$ en deux ensembles : l'un de $k-1$ éléments plus petits ou égaux à $T[i]$ et l'autre de $n-k$ éléments plus grands ou égaux à $T[i]$.


```pseudocode
algorithme k_select(T: []int, k: int) → int:
    ref inf ← 0
    pour chaque x de T[1:]:
        si x < T[0]:
            inf ← inf + 1
    
    ref T' []int
    si inf ≥ k: 
        T' ← [x pour chaque x de T[1:] si x < T[0]]
        rendre k_select(T', k)
    sinon si k-inf-1 > 0:
        T' ← [x pour chaque x de T[1:] si x ≥ T[0]]
        rendre k_select(T', k-inf-1)
    sinon:
        rendre T[0]

```


{% exercice %}

Démontrez que l'algorithme `k_select(T: []int, k: int) → int`{.language-} rend bien un $k$-ème plus petit élément de $T$.

{% endexercice %}
{% details "corrigé" %}
Par récurrence sur la longueur $n$ du tableau. Si $n=1$, on ne peut avoir que $k=1$ et dans ce cas `inf = 0`{.language-}, `k-inf-1 = 0`{.language-} et on rend bien `T[0]`{.language-}.

On suppose la propriété vraie pour une longueur de $n$ et on considère un tableau de longueur $n+1$. On a alors 3 cas :

- soit `inf ≥ k`{.language-} et il y a au moins $k$ éléments strictement plus petits que `T[0]`{.language-}, le $k$-ème plus petit élément de `T`{.language-} est le $k$-ème plus petit élément de `[x pour chaque x de T[1:] si x < T[0]]`{.language-} qui est trouvé par la récursion par hypothèse de récurrence,
- soit `inf < k`{.language-} et `k-inf-1 > 0`{.language-}. `T[0]`{.language-} est alors le `inf + 1`{.language-} ème plus petit élément de $T$ et le $k$-ème plus petit élément de `T`{.language-} est le `k-inf-1{.language-}`-ème plus petit élément de `[x pour chaque x de T[1:] si x ≥ T[0]]`{.language-} qui est trouvé par la récursion par hypothèse de récurrence,
- soit `k = inf + 1`{.language-} et `T[0]`{.language-} est le $k$-ème plus petit élément de `T`{.language-}.

{% enddetails %}

On peut maintenant s'atteler au calcul des complexités min, max et en moyenne de l'algorithme. Pour cela on note $X_k(T)$ le nombre d'opérations élémentaire effectué par l'exécution de `k_select(T, k)`{.language-}. 

{% exercice %}
Montrez que pour un tableau $T$ et un en entier $k$, s'il y a une récursion on a :

<div>
$$
X_k(T) = \Theta(T.\text{\small longueur}) + X_{k'}(T')
$$
</div>

Avec $T'$ un tableau tel que $T'.\text{\small longueur} < T.\text{\small longueur}$ et $k' \leq k$.

{% endexercice %}
{% details "corrigé" %}
La boucle affectant la variable `inf`{.language-} ainsi que la création du tableau `T'`{.language-} est en $\Theta(T.\text{\small longueur})$ quels que soient `T`{.language-} et `k`{.language-}. 

Puis on effectue une récursion sur :

- un tableau de longueur strictement plus petit que $T$ puisque $T[0]$ n'y est pas
- un entier plus petit ou égal à $k$.

{% enddetails %}

Cette équation nous permet de déduire les complexités minimales et maximales de l'algorithme :

{% exercice %}
Montrez que la complexité minimale de l'algorithme `k_select(T: []int, k: int) → int`{.language-}est en $\Theta(n)$ et donnez un exemple pour lequel elle est réalisée pour un $k$ donné.
{% endexercice %}
{% details "corrigé" %}
La boucle affectant la variable `inf`{.language-} ainsi que la création du tableau `T'`{.language-} est en $\Theta(n)$ quels que soient `T`{.language-} et `k`{.language-}. La complexité min est ainsi plus grande que $\Theta(n)$.

De plus si le tableau `T`{.language-} contient exactement $k-1$ éléments strictement plus petits que `T[0]`{.language-} il n'y a pas de récursion, c'est bien la complexité minimale.

Un exemple simple pour lequel cette complexité arrive est lorsque $T[1:] = [2, 4, ... , 2p]$ et que $T[0] = 2k -1$.

{% enddetails %}
{% exercice %}
Montrez que la complexité maximale de l'algorithme `k_select(T: []int, k: int) → int`{.language-} est en $\Theta(n^2)$ et donnez un exemple pour lequel elle est réalisée pour un $k$ donné.
{% endexercice %}
{% details "corrigé" %}
La formule récursive précédente montre que pur un tableau $T$ donné, $X(T, k)$ sera la somme des longueurs des différents tableaux appelés récursivement. Comme cette longueur diminue strictement à chaque appel cette somme est inférieure à $\sum_{i = n-1}^1\Theta(i) = \Theta(n^2)$.

Un exemple simple pour lequel cette complexité arrive est lorsque $T[:-1] = [2p, 2(p-1), ... , 2]$ et que $T[-1] = 2k -1$.

{% enddetails %}

Les complexité maximale et minimale ne dépendent que de la longueur $n$ du tableau, pas de $k$. On va montrer que ceci est aussi vrai lorsque l'on cherche la complexité en moyenne de l'algorithme. Pour les calculs en moyenne, on supposera (comme précédemment) que $T$ est un tableau aléatoire. 

{% exercice %}
Lorsque $T$ est un tableau aléatoire, montrez que la moyenne de la longueur $n'$ du tableau de la récursion vaut :

<div>
$$
\mathbb{E}[n'] = \frac{n-1}{2} + \frac{(k-1)(n-k)}{n}
$$
</div>
{% endexercice %}
{% details "corrigé" %}

La longueur $n'$ va dépendre de la valeur de `T[0]`{.language-} :

- si `T[0] < k`{.language-} alors `n' = n - T[0]`{.language-}
- si `T[0] = k`{.language-} il n'y a pas de récursion
- si `T[0] > k`{.language-} alors `n' = T[0] - 1`{.language-}

Comme $P(T[0] = i) = 1/n$ pour tout $i$ on a :

<div>
$$
\begin{array}{lcl}
\mathbb{E}[n'] 
&=& \sum\limits_{1\leq i < k}\frac{1}{n}\cdot (n - i) + \sum\limits_{k < i \leq n}\frac{1}{n}\cdot (i -1)\\
&=& \frac{1}{n}\cdot((k -1)\cdot n - \frac{k(k-1)}{2}) + \frac{1}{n}\cdot(\frac{n(n-1)}{2} -\frac{k(k-1)}{2})\\
&=&\frac{n-1}{2} + \frac{(k-1)(n-k)}{n}
\end{array}
$$
</div>

{% enddetails %}

On déduit de l'exercice précédent que $\mathbb{E}[n']$ est maximum pour $k = n/2$, c'est-à-dire lorsque l'on recherche la médiane, et vaut alors $\frac{3n}{4}$. Ceci nous donne une idée pour calculer la complexité en moyenne de notre algorithme. À $k$ fixé et pour notre modèle probabiliste, si on pose $C(n, k) \coloneqq \mathbb{E}[X_k]$ comme étant la complexité en moyenne à $k$ fixe pour une permutation de $[1 .. n]$. La remarque précédente nous incite à penser que :

- $C(n, k)$ va être maximum pour $k = n/2$
- qu'en moyenne la récursion va conserver un tableau de longueur $3n/4$.

Posons $C(n) \coloneqq \max_k(C(n, k))$ et montrons le.

On va commencer par démontrer deux résultats intermédiaires qui vont nous permettre de conclure rapidement :

{% exercice %}
Montrez que $C(n)$ est une fonction croissante.
{% endexercice %}
{% info %}
Vous pourrez commencer par montrer que $C(n+1, k) \geq C(n, k)$.
{% endinfo %}
{% details "corrigé" %}
On a l'équation $X_k(T) = \Theta(T.\text{\small longueur}) + X_{k'}(T')$, mais on pourrait compter précisément le nombre d'opérations et avoir l'équation exacte : $X_k(T) = \alpha \cdot (T.\text{\small longueur}) + \beta + X_{k'}(T')$.

De là :

<div>
$$
\begin{array}{lcl}
C(n+1, k) &=  & \alpha \cdot (n+1) + \beta + \frac{1}{n+1}(\sum_{i = 1}^{k-1}C(n-i, k-i) + \sum_{i = k+1}^{n}C(i, k))\\
&=& \alpha \cdot (n+1) + \beta + \frac{1}{n+1}(n \cdot (C(n, k) - \alpha \cdot (n) - \beta) + C(n, k))\\
&=& \alpha \cdot (n+1) + \beta - \frac{n}{n+1} \alpha - \frac{1}{n+1} \cdot \beta + C(n, k)\\
&=& \alpha \cdot n - \frac{1}{n+1} \alpha + \frac{n}{n+1} \cdot \beta + C(n, k)\\
&\geq&  C(n, k)\\
\end{array}
$$
</div>

Puis comme $C(n, k)= \max_k C(n, k)$, il existe $k^\star$ tel que $C(n)= C(n, k^\star)$ ce qui permet de conclure puisque : $C(n)= C(n, k^\star) \leq C(n+1, k^\star) \leq C(n+1)$
{% enddetails %}


{% exercice %}
Montrez que pour tout $1\leq k \leq n$ :

<div>
$$
\vert \{ n - i \leq \frac{3n}{4} \mid 1 \leq i \leq k - 1\} \vert + \vert \{ i \leq \frac{3n}{4} \mid k \leq i \leq n\} \vert \geq \frac{n}{2}
$$
</div>

{% endexercice %}
{% details "corrigé" %}

- Si $k < \frac{n}{4}$ ou $k > \frac{3n}{4}$, alors tous les $i$ tels que $\frac{n}{4} \leq i \leq \frac{3n}{4}$ seront soit dans le premier ensemble soit dans le deuxième. Comme il y a $\frac{n}{2}$ possibles, la condition est vérifiée.
- Si $\frac{n}{4} \leq k \leq \frac{3n}{4}$ les $i$ tels que $\frac{n}{4} \leq i \leq k$ seront dans le premier ensemble et les $i$ tels que $k \leq i \leq \frac{3n}{4}$ seront dans le second. 
Comme il y a $\frac{n}{2}$ possibles, la condition est vérifiée.

{% enddetails %}
On peut maintenant montrer l'équation de récurrence principale :
{% note "**Proposition**" %}
Montrez que l'on a l'équation :

<div>
$$
C(n) \leq \Theta(n) + C(\frac{3n}{4})
$$
</div>

{% endnote %}
{% details "preuve", "open" %}

Reprenons la définition de $C(n, k)$ :

<div>
$$
\begin{array}{lcl}
C(n, k) &=& \mathbb{E}[X_k]\\
&=& \Theta(n) + \frac{1}{n}(\sum_{i = 1}^{k-1}C(n-i, k-i) + \sum_{i = k+1}^{n-1}C(i, k))\\
&\leq& \Theta(n) + \frac{1}{n}(\sum_{i = 1}^{k-1}C(n-i) + \sum_{i = k+1}^{n-1}C(i))\\
&\leq& \Theta(n) + \frac{1}{n}(\sum_{i = 1}^{k-1}C(n-i) + \sum_{i = k}^{n}C(i))\\
\end{array}
$$
</div>

Les deux résultats précédant nous montrent alors que :

- plus de la moitié des $n$ valeurs $C(n-i)$ ou $C(i)$ sont inférieures à $C(\frac{3n}{4})$,
- la moitié restante est inférieure à $C(n)$.

Cette méga astuce nous permet d'écrire :

<div>
$$
\begin{array}{lcl}
C(n, k) &\leq& \Theta(n) + \frac{1}{2}\cdot C(\frac{3n}{4}) + \frac{1}{2}\cdot C(n)\\
\end{array}
$$
</div>

Cette équation étant vraie quelque soit $k$ on a :

<div>
$$
\begin{array}{lcl}
C(n) &\leq& \Theta(n) + \frac{1}{2}\cdot C(\frac{3n}{4}) + \frac{1}{2}\cdot C(n)\\
\end{array}
$$
</div>

Et donc :
<div>
$$
\begin{array}{lcl}
C(n) &\leq& \Theta(n) + C(\frac{3n}{4})\\
\end{array}
$$
</div>

{% enddetails %}

Et je vous laisse conclure ce (magnifique) exercice :


{% exercice %}
Déduire de la question précédente que  :

<div>
$$
C(n) = \Theta(n)
$$
</div>

{% endexercice %}
{% details "corrigé" %}

Il suffit de réappliquer l'inégalité :

<div>
$$
\begin{array}{lcl}
C(n) &\leq& \Theta(n) + C(\frac{3n}{4})\\
&\leq& \Theta(n) + \Theta(\frac{3n}{4}) + C(n\cdot (\frac{3}{4})^2)\\
&\leq& \Theta(n) + \dots +\Theta(n\cdot (\frac{3}{4})^i)  + \dots + \Theta(n\cdot (\frac{3}{4})^{\log_{4/3}(n)}) + C(1)\\
&\leq& \Theta(n\sum\limits_{i = 0}^{\log_{4/3}(n)} (3/4)^i) \\
\end{array}
$$
</div>

On peut maintenant utiliser [le résultat précédent](./#série-géométrique) qui permet de borner par 4 la somme $\sum_{i = 0}^{\log_{4/3}(n)} (3/4)^i$ pour avoir : $C(n) \leq \Theta(n)$. Comme de plus $C(n) \geq \Theta(n)$ on a bien l'égalité demandée.

{% enddetails %}
La complexité en moyenne de l'algorithme `k_select(T: []int, k: int) → int`{.language-} est donc linéaire en la longueur du tableau ! C'est optimal.

{% info %}
C'est une autre histoire que l'on verra ensemble bien plus tard mais il est totalement possible de choisir judicieusement un élément du tableau pour garantir que même la complexité maximale soit linéaire en la taille du tableau.
{% endinfo %}

L'astuce de la preuve de la proposition précédente est magnifique car elle permet de se ramener à une somme que l'on sait calculer.

{% retenir %}
La solution d'une équation de la forme suivante (avec $\alpha < 1$) :

<div>
$$
C(n) = \theta(n) + C(\alpha \cdot n)
$$
</div>

est :

<div>
$$
C(n) = \theta(n)
$$
</div>

Les algorithmes récursifs pour lesquels on peut garantir cette relations pour leurs complexité maximale ou en moyenne sont donc très performant !
{% endretenir %}


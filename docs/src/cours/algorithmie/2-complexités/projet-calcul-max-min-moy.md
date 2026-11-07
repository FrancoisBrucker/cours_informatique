---
layout: layout/post.njk

title: "Projet : Complexités d'algorithmes classiques"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les exercices ci-après sont fondamentaux pour le calcul de complexités, en particulier la complexité en moyenne. Apprenez leurs méthodes de résolution : elles vous permettront de vous en sortir pour une grande majorité des calculs qu'on vous demandera de faire.

{% attention %}
Ces exercices sont plus durs que ceux précédemment vus et sont de difficulté croissante. Faites et, surtout, comprenez bien les exercices précédents avant de vous lancer dans la résolution de ceux-ci.
{% endattention %}

## Recherche dichotomique

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

Cette complexité est vraiment très bonne ! La valeur de $\ln(n)$ est en effet très petite devant $n$. Pour se fixer les idées, et comme tous les log sont proportionnels, pensez à la différence entre :

- $t = 4.35 \cdot 10^{17}$ secondes qui est l'âge estimé de l'univers ($1.38 \cdot 10^8$ siècles),
- $\log_{10}(t) \simeq 17.65$ secondes qui est la durée moyenne que prend un mammifère pour faire pipi (selon une étude menée par Yang et Hu en 2014 et qui a été récompensée par le [Ig Nobel](https://fr.wikipedia.org/wiki/Prix_Ig-Nobel){.externe} de physique en 2015, on peut estimer cette durée à 21s±13s)

## Maximum d'un tableau

On pourrait penser que l'on n'a plus rien à dire sur les algorithmes permettant de trouver le maximum d'un tableau d'entiers (on en a déjà [une version itérative](../../1-algorithme/problème-preuve/#algorithme-max-tableau-iter) et [une version récursive](../../1-algorithme/projet/#algorithme-max-tableau-rec)), mais si, si, il nous reste au moins un résultat intéressant à démontrer. 

On va utiliser ici la version itérative de l'algorithme :

```pseudocode
algorithme maximum(T: []int) → int:
    ref m ← T[0]
    pour chaque x de T:
        si m < x:
            m ← x
    rendre m
```

Un petit échauffement avant le vrai résultat :

{% exercice %}
Donnez les complexités minimale, maximale et en moyenne de l'algorithme `maximum([]int) → int`{.language-}

{% endexercice %}
{% details "corrigé" %}

- complexité minimale et maximale $\mathcal{O}(n)$ puisqu'il faut parcourir chaque élément du tableau et que le reste des lignes est en $\mathcal{O}(1)$
- la complexité moyenne étant forcément entre la complexité minimale et maximale elle est également en $\mathcal{O}(n)$.

{% enddetails  %}

Maintenant regardons combien de fois la variable `m`{.language-} est affectée :

{% exercice %}
Donnez les nombres minimaux et maximaux de fois où la variable `m`{.language-} est affectée.

{% endexercice %}
{% details "corrigé" %}

La variable `m`{.language-} est affectée dans tous les cas au moins une fois. De plus :

- si le tableau est trié par ordre décroissant, `m`{.language-} n'est affectée qu'une fois
- si le tableau est trié par ordre croissant, `m`{.language-} est affectée à chaque itération, donc la longueur du tableau fois.

{% enddetails  %}

On s'intéresse à la complexité en moyenne de ce nombre d'affectations. Pour cela on va considérer que le tableau $T$ est une permutation aléatoire de [1 .. n].

{% exercice %}
Donnez un argument pour lequel sous ce modèle la complexité en moyenne du nombre d'affectations est $\log_2(T.\mbox{\small longueur})$

{% endexercice %}
{% details "corrigé" %}
Lorsque l'on met à jour $m$, c'est pour une valeur strictement plus grande. La probabilité que cette valeur soit $m+1$, $m+2$, ..., $T.\mbox{\small longueur}$ est la même, donc en moyenne elle sera de l'ordre de la moitié : $\frac{T.\mbox{\small longueur} + m}{2}$. À chaque affectation on divise par deux le nombre de valeurs plus grandes restantes : on le fait donc au maximum $\log_2(T.\mbox{\small longueur})$.
{% enddetails  %}
{% retenir %}
Il est important de retenir cet argument. Il va servir à de nombreuses reprises pour estimer des complexités en moyenne.
{% endretenir %}

L'argument précédent est souvent suffisant, mais, pour cette fois, faites-le proprement pour vous convaincre que l'argument est bon :

{% exercice %}
Démontrez que sous ce modèle, la probabilité que $T[i] = \max(T[:i])$ pour $0 \leq i < n$ vaut $\frac{1}{i+1}$.
{% endexercice %}
{% info %}
Vous pourrez lier cette complexité au nombre de fois où $T[i] = \max(T[:i])$ pour $0 \leq i < n$ et au fait ([démontré là](https://fr.wikipedia.org/wiki/S%C3%A9rie_harmonique#%C3%89quivalent_de_Hn){.externe}) que $\sum_{1\leq i \leq n} \frac{1}{i}$ est équivalent à $\ln(n)$ en $+\infty$.
{% endinfo %}
{% details "corrigé" %}
Pour construire une permutation $T$ de $[1 .. n]$ telle que $T[i] = \max(T[:i])$ il faut :

1. choisir les $i+1$ premiers éléments de $T$ : il y a $\binom{n}{i+1}$ choix possibles.
2. placer le plus grand des éléments choisis en 1. à la position $T[i]$ : 1 choix possible
3. placer les $i$ éléments restants aux $i$ premières places : $(i)!$ choix possibles
4. placer les $n-i-1$ éléments restants aux $n-i-1$ dernières places : $(n-i-1)!$ choix possibles

Il y a donc : $\binom{n}{i+1} \cdot 1 \cdot (i)! \cdot (n-i-1)! = \frac{n!}{(i+1)! \cdot (n-i-1)!} \cdot i! \cdot (n-i-1)! = \frac{n!}{i+1}$.

On en conclut que la probabilité $p_i$ qu'une permutation $T$ soit telle que $T[i] = \max(T[:i-1])$ vaut $\frac{\frac{n!}{i+1}}{n!} = \frac{1}{i+1}$.

{% enddetails  %}

De là, on peut définir $X_i$ la variable aléatoire telle que $X_i(T) = 1$ si $T[i] = \max(T[:i-1])$ et $X_i(T) = 0$ sinon. En notant $X(T) = \sum_{0\leq i < n} X_i(T)$, la complexité en moyenne $C_{\text{moy}}(n)$ pour une longueur $n$ de tableau vaut son espérance $\mathbb{E}[X]$ et donc :

<div>
$$
\begin{array}{lclr}
C_{\text{moy}}(n) &=& \mathbb{E}[X] \\
&=& \mathbb{E}[\sum\limits_{0\leq i < n}X_i] \\
&=& \sum\limits_{0\leq i < n}\mathbb{E}[X_i] &\text{par linéarité de l'espérance}\\
&=& \sum\limits_{0\leq i < n} (p_i\cdot 1)& \text{par définition } E[Y] = \sum\limits_k P(Y = k)\cdot k \text{ pour toute variable aléatoire discrète }Y\\
& =& \sum\limits_{1\leq i \leq n} \frac{1}{i}
\end{array}
$$
</div>

On peut maintenant utiliser le résultat classique suivant pour conclure :

{% note "**Proposition**" %}
<div>
$$
\sum\limits_{i=1}^{n} \frac{1}{i} \underset{+\infty}{\sim} \ln(n)
$$
</div>

{% endnote %}
{% retenir %}
Retenez ce résultat, cela est souvent utile.
{% endretenir %}
{% details "preuve", "open"%}

Soit $f(x) = \ln(1+x) - x$ définie sur $]-1, +\infty[$. Comme $f'(x) = \frac{1}{1+x} -1 = \frac{-x}{1+x}$, on a que $f$ atteint son minimum en 0 : $f(x) \geq f(0) = 0$ pour tout $x$ de $]-1, +\infty[$ : $x \geq \ln(1+x)$ sur $]-1, +\infty[$.

De là pour tout entier $i > 1$ : 

- $-\frac{1}{i} \geq \ln(1-\frac{1}{i}) = \ln(i-1) - \ln(i)$
- $\frac{1}{i} \geq \ln(1+\frac{1}{i}) = \ln(i+1) - \ln(i)$

Ce qui donne l'encadrement pour $i > 1$ : 

<div>
$$
\ln(i+1) - \ln(i) \leq \frac{1}{i} \leq \ln(i) - \ln(i-1)
$$
</div>

En sommant le tout on obtient une série télescopique :

<div>
$$
\begin{array}{c}
\sum\limits_{2\leq i \leq n} (\ln(i+1) - \ln(i)) \leq \sum\limits_{2\leq i \leq n}\frac{1}{i} \leq \sum\limits_{2\leq i \leq n} (\ln(i) - \ln(i-1))
\end{array}
$$
</div>

Qui se simplifie en :
<div>
$$
\begin{array}{c}
\ln(n+1) - \ln(2) \leq \sum\limits_{2\leq i \leq n}\frac{1}{i} \leq \ln(n) - \ln(1)
\end{array}
$$
</div>

On en déduit donc l'encadrement :

<div>
$$
\begin{array}{c}
\ln(n+1) \leq \sum\limits_{i=1}^n\frac{1}{i} \leq \ln(n) + 1
\end{array}
$$
</div>

Ce qui montre que $\lim\limits_{+\infty}\frac{\sum\limits_{i=1}^n\frac{1}{i}}{\ln{n}} = 1$ et conclut la preuve.
{% enddetails %}

On en conclut que la complexité en moyenne du nombre d'affectations est en $\Theta(\ln(T.\mbox{\small longueur}))$ (chouette résultat, non ?).


## Recherche de sous-mots

On va analyser un algorithme permettant de rechercher des sous-mots d'[un mot d'un alphabet $\mathcal{A}^\star$](../../1-algorithme/bases-théoriques/définition/#définition-mot). Si $m = m_0 \dots m_p$ est un mot de $\mathcal{A}^\star$, un mot $n = n_0\dots n_q$ est un sous-mot de $m$ s'il existe $0\leq i \leq p - q$ tel que $m_{i + k} = n_{k}$ pour tous $0\leq k \leq q$.

<div id="sous-mot"></div>

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

{% exercice %}
Donnez la complexité minimale de l'algorithme `k_select(T: []int, k: int) → int`{.language-} et des exemples pour lesquels elle est réalisée.
{% endexercice %}
{% details "corrigé" %}
La boucle affectant la variable `inf`{.language-} ainsi que la création du tableau `T'`{.language-} est en $\mathcal{O}(n)$ quels que soient `T`{.language-} et `k`{.language-}. La complexité min est ainsi plus grande que $\mathcal{O}(n)$.

De plus si le tableau `T`{.language-} contient exactement $k-1$ éléments strictement plus petits que `T[0]`{.language-} il n'y a pas de récursion, c'est bien la complexité minimale.

Un exemple simple pour lequel cette complexité arrive est lorsque $T[1:] = [2, 4, ... , 2p]$ et que $T[0] = 2k -1$.

{% enddetails %}
{% exercice %}
Montrez que la complexité maximale de l'algorithme `k_select(T: []int, k: int) → int`{.language-} $C(n, k)$ respecte l'équation suivante :

<div>
$$
C(n, k) = \mathcal{O}(n) + C(n', k')
$$
</div>

Avec $n' < n$ et $k' \leq k$ les paramètres de la récursion. 

{% endexercice %}
{% details "corrigé" %}
La boucle affectant la variable `inf`{.language-} ainsi que la création du tableau `T'`{.language-} est en $\mathcal{O}(n)$ quels que soient `T`{.language-} et `k`{.language-}. Le reste des opérations de l'algorithme est en $\mathcal{O}(1)$. La complexité de l'algorithme est alors en :


<div>
$$
C(n, k) = \mathcal{O}(n) + C(n', k')
$$
</div>

Avec $n' < n$ et $k' \leq k$ les paramètres de la récursion. 
{% enddetails %}
{% exercice %}
Déduire de l'exercice précédent la complexité maximale de l'algorithme `k_select(T: []int, k: int) → int`{.language-} et des exemples pour lesquels elle est réalisée.
{% endexercice %}
{% details "corrigé" %}
La formule récursive précédente montre que la complexité $C(n, k)$ de l'algorithme sera la somme des longueurs des différents tableaux appelés récursivement. Comme cette longueur diminue strictement à chaque appel cette somme est en $\mathcal{O}(n^2)$.


Un exemple simple pour lequel cette complexité arrive est lorsque $T[:-1] = [2p, 2(p-1), ... , 2]$ et que $T[-1] = 2k -1$.

{% enddetails %}

Notre algorithme est très utilisé en pratique car sa complexité en moyenne est très faible. Nous allons ici juste faire fonctionner notre intuition pour en estimer la complexité en moyenne.

Pour ce calcul, on supposera (comme précédemment) que $T$ est une permutation aléatoire de $[1 .. n]$. 

{% exercice %}
Lorsque $T$ est une permutation aléatoire de $[1 .. n]$, montrez que la longueur moyenne du tableau de la récursion vaut :

<div>
$$
\mathbb{E}[n'] = \frac{n-1}{2} + \frac{(k-1)(n-k)}{n}
$$
</div>
{% endexercice %}
{% details "corrigé" %}

La longueur $n'$ va dépendre de la valeur de `T[0]`{.language-} :

- si `T[0] < k`{.language-} alors `n' = n - T[0]`{.language-}
- si `T[0] = k`{.language-} alors `n' = 0`{.language-}
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

On déduit de l'exercice précédent que $E[n']$ est maximum pour $k = n/2$, c'est-à-dire lorsque l'on recherche la médiane.

Si $C_{m}(n, k)$ est la complexité moyenne on a alors l'inégalité :

<div>
$$
C_{m}(n, k) \leq \mathcal{O}(n) + C_{m}(3n/4, k')
$$
</div>

{% exercice %}
Déduire de la question précédente que la complexité en moyenne de l'algorithme pour le calcul de la médiane respecte l'inégalité :

<div>
$$
C_{m}(n, k) = \mathcal{O}(n)
$$
</div>

{% endexercice %}
{% details "corrigé" %}

Il suffit de réappliquer l'inégalité :

<div>
$$
\begin{array}{lcl}
C_{m}(n, k) &\leq& \mathcal{O}(n) + C_{m}(3n/4, k')\\
&\leq& \mathcal{O}(n) +\mathcal{O}(3n/4) + C_{m}((3/4)^2n, k'')\\
&\leq& \mathcal{O}(n) + \dots + \mathcal{O}(n\cdot(3/4)^i) + \dots + \mathcal{O}(n\cdot(3/4)^{\log_{4/3}(n)}) + C_{m}(1, 1)\\
&\leq& \mathcal{O}(n\sum_{0 \leq i\leq \log_{4/3}(n)} (3/4)^i) \\
\end{array}
$$
</div>

On peut maintenant utiliser [le résultat précédent](./#série-géométrique) qui permet de borner par 4 la somme $\sum_{i = 0}^{\log_{4/3}(n)} (3/4)^i$ et de conclure que :

<div>
$$
C_{m}(n, k) \leq \mathcal{O}(n)
$$
</div>

{% enddetails %}



La complexité en moyenne de l'algorithme `k_select(T: []int, k: int) → int`{.language-} est donc linéaire en la longueur du tableau ! C'est optimal.

{% info %}
C'est une autre histoire que l'on verra ensemble bien plus tard mais il est totalement possible de choisir judicieusement un élément du tableau pour garantir que même la complexité maximale soit linéaire en la taille du tableau.
{% endinfo %}
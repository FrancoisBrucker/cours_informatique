---
layout: layout/post.njk

title: Calculer la complexité d'algorithmes avec les O

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD 
> recherche max/min
> recherche dichotomique
> plus longue sequence croissante
> le piège de claude trois boucles imbiquées qui font n2
>

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

Cette complexité est vraiment très bonne puisque la valeur de $\ln(n)$ est en effet très petite devant $n$ ([rappelez-vous l'ordre de grandeur qu'on a déjà vu](../complexité-moyenne/#importance-log)).

{% retenir %}
Si l'on manipule des tableaux triés, la recherche dichotomique est énormément plus performante que la recherche naïve.
{% endretenir %}
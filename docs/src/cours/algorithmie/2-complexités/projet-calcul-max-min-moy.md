---
layout: layout/post.njk

title: "Projet : calcul de complexités"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les exercice ci-après sont fondamentaux pour le calcul de complexités. Apprenez leurs méthodes de résolutions ils vous permettrons de vous en sortir pour une grande majorité des calculs qu'on vous demandera de faire.

{% attention %}
Ces exercice sont plus durs que ceux précédemment vus. Faites et comprenez bien les exercices précédents avant de vous lancer dans la résolution de ceu-ci.
{% endattention %}

## Recherche dichotomique


Le principe de [la recherche dichotomique](https://fr.wikipedia.org/wiki/Recherche_dichotomique){.externe} permet de savoir si un entier donné est dans un tableau d'entier trié.

On cherche à savoir si l'entier $x$ est entre les indices $a$ et $b \geq a$ d'un tableau d'entiers $T$. On procède récursivement selon la valeur de $t[\lfloor (a + b)/2 \rfloor]$ :

- si $T[\\,\lfloor (a + b)/2 \rfloor\\,] = x$ on a trouvé l'élément
- si $T[\\,\lfloor (a + b)/2 \rfloor\\,] > x$, l'indice recherché est forcément **avant** $\lfloor (a + b)/2 \rfloor$. On recommence alors la procédure avec :
  - $a = \lfloor (a + b)/2 \rfloor + 1$
  - $b$ inchangé
- si $T[\\,\lfloor (a + b)/2 \rfloor\\,] < x$, l'indice recherché est forcément **après** $\lfloor (a + b)/2 \rfloor$. On recommence alors la procédure avec :
  - $a$ inchangé
  - $b' = \\,\lfloor (a + b)/2 \rfloor\\, - 1$

Ce principe donne l'algorithme suivant :

<span id="algorithme-dichotomie"></span>

```pseudocode
algorithme recherche_dichotomique(T: []int, x: int) → bool:
  ref a ← 0
  ref b ← T.longueur - 1
  ref m int

  tant que a ≤ b:
      m ← (a + b) // 2  # division entière

      si (t[m] == x):
          rendre Vrai  # m est l'indice
      si (t[m] < x):
          a ← m + 1
      si (t[m] > x):
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

On en conclut le théorème fondamental de la dichotomie : le nombre de fois où l'on peut diviser par 2 un nombre $n$ est $\log_2(n)$ : il y a donc au plus $K \leq \log_2(n) + 1$ itérations (avec $n$ la longueur du tableau). Comme $\log_2(n) = \frac{\ln(n)}{\ln(2)}$ on a :

{% note "**Proposition**" %}
L'algorithme `recherche_dichotomique`{.language-} résout le problème "recherche ordonnée" en $\mathcal{O}(\ln(n))$ (avec $n$ la longueur du tableau).
{% endnote %}

L'algorithme recherche que l'on a déjà utilisé à ne nombreuses reprise

> TBD théorique puis en pratique. Vérifier que log ok avec régression linéaire

## Maximum d'un tableau

> TBD no,bre de d'exécution d'une f
> TBD nb de mise à jour du maximum. 
> 1. calcul max
> 2. nombre de mise a jour de l'algo simple : Max n et en moyenne ln(n) (Knuth) (avec les main le prochain > est à la moitié.)




> TBD pour aller plus loin
> TBD ajouter pyperf pour les perf d'un programme et cprofile pour le profilage des bootleneck <https://www.stephane-robert.info/docs/developper/programmation/python/profiling/>
> 3. modif pour mise a jour dans une fonction et vérifier que cprofile ou pyperf le voit

>

<span id="algorithme-max-tableau-complexité"></span>
{% exercice %}
 Donnez sa complexité de l'algorithme `maximum_rec`{.language-}.

{% endexercice %}
{% details "corrigé" %}

Toutes les lignes de l'algorithme sont en $\mathcal{O}(1)$ à part la récursion. Comme la récursion est faite sur la taille du tableau, on va noter $C(n)$ sa complexité où $n$ est la taille du tableau passé en paramètre. Elle satisfait alors l'équation :

<div>
$$
C(n) = \mathcal{O}(1) + C(n-1)
$$
</div>

On a vu en cours que cette équation se résout en : $C(n) = \mathcal{O}(n)$.

{% enddetails %}



## Algorithme de texte

> Naif et en moyenne
### sous-mot
1 seul puis tous.

### sous-sequence

complexité en moyenne.

### Egalité 

> TBD ressemble à égalité de tableau.
> TBD moyenne pour mot aléatoire
> 

### Mot de 01

> cas particulier.
> égalité mots de 01
> max/moyenne ?
> TBD faire les tests et séparer main et fct pour qu'ils puissent reprendre le code fait dans les prochains tds.


> TBD : une fois qu'on a un algorithme qui fait ce qu'on veut on essaie de le faire le plus vite possible (en moins d'instruction possible)
> TBD égalité de mots binaires. max O(n) en moyenne O(2)
> TBD faire 2 parties. Une avec ceux d'avant et une nouvelle avec de nouveaux algorithmes
> 

## $k$-ème plus petit élément

> TBD corrigé dans 20/21 test. Ajouter complexité min et en moyenne.
> 
On considère le pseudo-code suivant :

```pseudocode
fonction copie(T: []int) → []int:

    ref T' ← []int{longueur: T.longueur}
    T' ← T[:]

    rendre T'


fonction maximum(T: []int) → int:
    ref m ← 0
    pour chaque i de [0 .. T.longueur[:
        if T[m] < T[i]:
            m ← i
    rendre m


fonction minimum(T):
    ref m ← 0
    pour chaque i de [0 .. T.longueur[:
        if T[m] > T[i]:
            m ← i
    rendre m


algorithme recherche(T: []int, k: int) → int:
    ref max_value ← T[maximum(T)]
    ref min ← 0

    ref T_copie ← copie(T)
    pour chaque i de [0 .. k - 1[:
        min ← minimum(T_copie)
        T_copie[min] ← max_value + 1

    rendre minimum(T_copie)
```

### 1

{% faire %}

Donnez la complexité de l'algorithme `recherche(T, k)`{.language-}

{% endfaire %}
{% info %}
Pour calculer la complexité de l'algorithme, il vous faudra également calculer les complexités des fonctions utilisées par celui-ci.
{% endinfo %}

### 2

{% faire %}

Quel est l'intérêt de la fonction `copie(T)`{.language-} ?

{% endfaire %}

### 3

{% faire %}

Démontrez que l'algorithme `recherche(T, k)`{.language-} rend l'indice du $k$ème plus petit élément de $T$.

{% endfaire %}
{% info %}
Pour démontrer ce que fait recherche, il vous faudra également trouver et démontrer ce que font les fonctions utilisées par celui-ci.
{% endinfo %}

### 4

{% faire %}

Utilisez `recherche(T, k)`{.language-} pour créer un algorithme déterminant l'indice de [la médiane d'un tableau](https://fr.wikipedia.org/wiki/M%C3%A9diane_(statistiques)){.externe}. Quelle est sa complexité ?

{% endfaire %}
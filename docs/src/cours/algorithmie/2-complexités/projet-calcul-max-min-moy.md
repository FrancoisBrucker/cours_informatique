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

On cherche à savoir si l'entier $x$ est entre les indices $a$ et $b \geq a$ d'un tableau d'entiers $T$. On procède récursivement selon la valeur de $T[\lfloor (a + b)/2 \rfloor]$ :

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
  ref a, b ← 0, T.longueur - 1
  ref m int

  tant que a ≤ b:
      m ← (a + b) // 2  # division entière

      si (t[m] == x):
          rendre Vrai
      si (t[m] < x):
          a ← m + 1
      si (t[m] > x):
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

- termine quelque soient ses entrées,
- est bien un algorithme de recherche.
{% endexercice %}
{% details "corrigé" %}

- **finitude**. La quantité entière `b - a`{.language-} **décroît strictement** à chaque itération, elle sera donc strictement négative après un nombre fini d'opérations et l'algorithme s'arrêtera.
- **preuve** :
  1. on montre trivialement l'invariant de boucle suivant: si valeur est dans `T`{.language-}, alors sa position est plus grande ou égale à `a`{.language-} et plus petite ou égale à `b`{.language-}
  2. si l'on sort de la boucle l'invariant est toujours vérifié mais comme `a`{.language-} > `b`{.language-}, `x`{.language-} ne peut être dans `T`{.language-}

Les remarques ci-dessus prouvent que l'algorithme `recherche_dichotomique`{.language-} fonctionne.
{% enddetails %}


{% exercice %}
Démontrez que la complexité de l'algorithme `recherche_dichotomique(T: []int, x: int) → bool`{.language-} vaut $\mathcal{O}(K)$ avec $K$ le nombre de fois où l'algorithme rentre dans la boucle `tant que`{.language-}

{% endexercice %}
{% details "corrigé" %}

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
{% enddetails %}

Avant de conclure, démontrons une petite proposition qui sera utile tout au long de ce cours :


{% note "**Proposition**" %}
Le plus grand entier $k$ tel que $\frac{n}{p^k} \geq 1$ pour deux entiers $n\geq p$ vaut  $k = \lfloor\log_p(n)\rfloor$.
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
Comme à chaque itération, `b - a`{.language-} est divisé par 2, il y a autant d'itérations que l'on peut diviser $T.\mbox{\small longueur}$ par 2,  donc au plus $\log_2(T.\mbox{\small longueur}) + 1$ itérations . Comme $\log_2(n) = \frac{\ln(n)}{\ln(2)}$ on a bien la complexité recherchée.

{% enddetails  %}

Cette complexité est vraiment très bonne ! La valeur de $\ln(n)$ est en effet très petite devant $n$, Pour se fixer les idée et comme tous les log sont proportionnels pensez à la différence entre :

- $t = 4.35 \cdot 10^{17}$ secondes qui est l'age estimé de l'univers ($1.38 \cdot 10^8$ siècles),
- $\log_10(t) \simeq 17.65$ secondes qui est la durée moyenne que prend un mammifère pour faire pipi (selon une étude menée par Yang et Hu en 2014 et qui a été récompensée par le [Ig Nobel](https://fr.wikipedia.org/wiki/Prix_Ig-Nobel){.externe} de physique en 2015, on peut estimer cette durée à 21s±13s)

## Maximum d'un tableau

On pourrait penser que l'on a plus rien à dire sur les algorithmes permettant de trouver le maximum d'un tableau d'entiers (on en a déjà un [une version itérative](../../1-algorithme/problème-preuve/#algorithme-max-tableau-iter) et [une version récursive](../../1-algorithme/projet/#algorithme-max-tableau-rec)), mais si si il nous reste au moins un résultat intéressant à démontrer. 

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

Maintenant regardons combien de fois la variable `m`{.language-} est affectée,

{% exercice %}
Donnez les nombres minimaux et maximaux de fois où la variable `m`{.language-} est affectée.

{% endexercice %}
{% details "corrigé" %}

La variable `m`{.language-} est affectée est affecté dans tous les cas au moins une fois. De plus :

- si le tableau est trié par ordre décroissant, `m`{.language-} n'est affecté qu'une fois
- si le tableau est trié par ordre croissant, `m`{.language-} est affecté à chaque itération, donc la longueur du tableau fois.

{% enddetails  %}

On s'intéresse à la complexité en moyenne de ce nombre d'affectation. Pour cela on va considérer que le tableau $T$ est une permutation aléatoire de [1 .. n].

{% exercice %}
Donnez un argument pour lequel sous ce modèle la complexité en moyenne du nombre d'affectation est $\log_2(T.\mbox{\small longueur})$

{% endexercice %}
{% details "corrigé" %}
Lorsque l'on met à jour $m$, c'est pour une valeur strictement plus grande. La probabilité que cette valeur soit $m+1$, $m+2$, ..., $T.\mbox{\small longueur}$ est la même, donc en moyenne elle sera de l'ordre de la moitié : $\frac{T.\mbox{\small longueur} + m}{2}$. À chaque affectation on divise par deux le nombre de valeurs plus grandes restantes : on le fait donc au maximum $\log_2(T.\mbox{\small longueur})$.
{% enddetails  %}
{% info %}
Il est important de retenir cet argument. Il va servir à de nombreuse reprises pour estimer des complexités en moyenne.
{% endinfo %}

L'argument précédent est souvent suffisant, mais, pour cette fois, faites le proprement pour vous convaincre que l'argument est bon :

{% exercice %}
Démontrez que sous ce modèle, la probabilité que $T[i] = \max(T[:i])$ pour $0 \leq i < n$ vaut $\frac{1}{i+1}$.
{% endexercice %}
{% info %}
Vous pourrez lier cette complexité au nombres de fois où $T[i] = \max(T[:i])$ pour $0 \leq i < n$ et au fait ([démontré là](https://fr.wikipedia.org/wiki/S%C3%A9rie_harmonique#%C3%89quivalent_de_Hn){.externe}) que $\sum_{1\leq i \leq n} \frac{1}{i}$ est équivalent à $\ln(n)$ en $+\infty$.
{% endinfo %}
{% details "corrigé" %}
Pour construire une permutation $T$ de $[1 .. n]$ telle que $T[i] = \max(T[:i])$ il faut :

1. choisir les $i+1$ premiers éléments $T$ : il y a $\binom{n}{i+1}$ choix possible.
2. placer le plus grand des éléments choisi en 1. à la position $T[i]$ : 1 choix possible
3. placer les $i$ éléments restant aux $i$ premières places : $(i)!$ choix possible
4. placer les $n-i-1$ éléments restant aux $n-i-1$ dernières places : $(n-i-1)!$ choix possible

Il y a donc : $\binom{n}{i+1} \cdot 1 \cdot (i)! \cdot (n-i-1)! = \frac{n!}{(i+1)! \cdot (n-i-1)!} \cdot i! \cdot (n-i-1)! = \frac{n!}{i+1}$.

On en conclut que la probabilité $p_i$ qu'une permutation $T$ soit telle que $T[i] = \max(T[:i-1])$ vaut $\frac{\frac{n!}{i+1}}{n!} = \frac{1}{i+1}$.

{% enddetails  %}

De là, la complexité en moyenne $C_{\text{moy}}(n)$ pour une longueur $n$ de tableau vaut : 

<div>
$$
C_{\text{moy}}(n) = \sum_{0\leq i < n} p_i\cdot 1 = \sum_{1\leq i \leq n} \frac{1}{i}
$$
</div>

Et on conclut en utilisant [le fait que](https://fr.wikipedia.org/wiki/S%C3%A9rie_harmonique#%C3%89quivalent_de_Hn){.externe} (on le démontrera plus tard) $\sum_{1\leq i \leq n} \frac{1}{i}$ est équivalent à $\ln(n)$ en $+\infty$.

On en conclut que la complexité en moyenne du nombre d'affectations est en $\Theta(\ln(T.\mbox{\small longueur}))$.

{% info %}
Retenez (on le démontrera plus tard) que $\sum_{1\leq i \leq n} \frac{1}{i}$ est équivalent à $\ln(n)$ en $+\infty$, cela est souvent utile.
{% endinfo %}

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
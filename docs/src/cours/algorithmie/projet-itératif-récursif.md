---
layout: layout/post.njk
title: "Projet : Écrire et prouver des algorithmes itératifs et récursifs"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD que les simples
> TBD mettre les classiques dans la partie classique.
> TBD decurrification à mettre plus tard. Lorsque l'on parle des listes par exemple. Et on décurrifie Ackerman avant comme exemple.
Écrire des algorithmes (simples) en pseudo-code pour résoudre des problèmes algorithmiques.

## Maximum d'un tableau

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
maximum_rec(t: [réel], n: entier) → entier
```

Qui rend un indice $0 \leq j \leq n$ tel que $t[j] = \max(\{t[k] \vert 0\leq k \leq n\})$.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme maximum_rec(t: [réel], n: entier) → entier:
    si n == 0:
        rendre 0
    sinon:
        x ← maximum_rec(t, n-1)
        si t[x] > t[n]:
            rendre x
        sinon:
            rendre n
```

Le paramètre `n`{.language-} est un entier qui diminue strictement. Il sera donc à un moment égal à 0 ce qui stoppera la récursion.

La correction se fait par récurrence sur `n`{.language-} allant de `n = 0`{.language-} à `n = t.longueur - 1`{.language-}.

1. initialisation : pour `n = 0`{.language-}, le résultat est clair.
2. hypothèse de récurrence : on suppose que l'algorithme fonctionne pour `n - 1`{.language-}
3. preuve pour `n - 1`{.language-}. Si l'algorithme fonctionne pour `n - 1`{.language-}, `x`{.language-} contient l'indice max des indices allant de 0 à `n - 1`{.language-} et on rend `x` si `t[x] > t[n]` et `n` sinon : on rend bien l'indice de la valeur maximale du tableau.

{% enddetails %}

## <span id="concaténation"></span>Concaténation

{% exercice %}
Donnez et prouvez **un algorithme itératif** de signature :

```pseudocode
concaténation(début: [entier], fin: [entier]) → [entier]
```

Qui rend **un nouveau tableau** contenant la concaténation de `début`{.language-} et de `fin`{.language-}.
{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme concaténation(début: [entier], fin: [entier]) → [entier]
    t ← tableau de taille début.longueur + fin.longueur
    i ← -1

    pour chaque j de [0, début.longueur[:
        i ← i + 1
        t[i] ← début[j]

    pour chaque j de [0, fin.longueur[:
        i ← i + 1
        t[i] ← fin[j]

    rendre t
```

La finitude est claire puisqu'il n'y a que deux boucles de type `pour chaque`{.language-}.

On a deux boucles, il faut donc à priori 2 invariants, un pour chaque boucle. Ici il est clair que l'on va remplir tous les éléments des tableaux `début`{.language-} et `fin`{.language-} dans `t`{.language-}. L'invariant peut être :

> si $i_0$ est la valeur de $i$ à la ligne 4 (resp. 8) alors à chaque fin d'itération on a $t[i_0 + 1 + k] == \mbox{début}[k]$ (resp. `fin`{.language-}) pour tout $0\leq k \leq j$.

Démontrons l'invariant rigoureusement pour la première boucle.

À la fin de la première itération, on a bien :

- $t[i_0 + 1] == \mbox{début}[0]$
- $j = 0$
- $i = i_0 + 1 + j$

Supposons la propriété vraie après une itération donnée. Après une itération supplémentaire, les variables $i$ et $j$ ont été modifiées telles que :

- $j' = j + 1$
- $i' = i + 1 = i_0 + 1 + j'$

L'hypothèse de l'invariant de boucle stipule que $t[i_0 + k] == \mbox{début}[k]$ pour tout $0\leq k \leq j = j'-1$ et comme la boucle a effectué l'affectation : `t[i'] ← début[j']`{.language-}, l'invariant continue d'être vérifié. Ce qui conclut la preuve.

Il faut juste faire très attention à l'endroit on commence dans `t`{.language-}. ici c'est Ok car avant la première boucle `i = -1`{.language-} et `i = début.longueur - 1`{.language-} au début de la seconde boucle. Les éléments de `début`{.language-} et `fin`{.language-} ne vont pas se chevaucher dans `t`{.language-} et se suivre sans interruption.

{% enddetails %}

La preuve de l'invariant dans le corrigé est formelle mais évidente. Il n'est pas nécessaire (et on ne le fera plus) d'être aussi rigoureux pour des boucles aussi simple :

{% note %}
Lorsque le résultat d'une boucle est évidente, il n'est n'est pas nécessaire de faire une preuve formelle (qui sera souvent lourde et inintéressante).

Dans ces cas, contentez vous de donner l'invariant ou le résultat de la boucle.
{% endnote %}

## <span id="égalité-tableaux"></span>Égalité de tableaux

> TBD commencer par dire même valeurs, puis même nombre (=permutation)

{% exercice %}
Écrivez un algorithme itératif permettant de vérifier que deux tableaux d'entiers $T$ et $T'$ contiennent les mêmes valeurs.

C'est à dire qu'il existe une permutation $\sigma$ de $[0, n-1]$ telle que $T[i] = T[\sigma(i)]$ pour tout $i \in [0, n-1]$.

{% endexercice %}
{% details "corrigé" %}

Il faut pouvoir trouver tous les éléments de $T$ dans $T'$. autant de fois qu'ils sont dans $T$. En utilisant [notre algorithme `nombre`{.language-}](../pseudo-code/#exercice-nombre-occurrences){.interne} Ce qui donne un l'algorithme suivant :

```pseudocode
algorithme égalité(t1: [entier], t2: [entier]) → entier
    pour chaque e de t1:
        si nombre(t1, e) ≠ nombre(t2, e):
            rendre Faux
        rendre Vrai
```

On ne peut rendre Vrai que si tous les éléments de t1 sont dans t2 avec un même montant. Donc uniquement s'il existe une existe une permutation $\sigma$ de $[0, n-1]$ telle que $T[i] = T[\sigma(i)]$ pour tout $i \in [0, n-1]$.

{% enddetails %}

## <span id="suppression-valeur"></span>Suppression de valeurs

Trouver un invariant permet de prouver efficacement un algorithme itératif. Pour des algorithmes simples, les bons invariants sont évidents à prouver une fois trouvé (on ne le donc fera pas explicitement) et permettent une preuve aisée. Entraînez vous avec l'exercice suivant :

<span id="suppression-valeur-itératif"></span>

{% exercice %}
Donnez et prouvez **un algorithme itératif** de signature :

```pseudocode
supprime(t: [entier], v: entier) → [entier]
```

Qui rend **un nouveau tableau** contenant la restriction de `t`{.language-} aux valeurs différentes de `v`{.language-}.
{% endexercice %}
{% details "corrigé" %}

Pour que l'algorithme fonctionne, il faut commencer par connaître la taille du tableau à créer et donc compter le nombre d’occurrences de `v`{.language-} dans `t`{.language-}. Ensuite, il sera possible de remplir le tableau.

```pseudocode/
algorithme supprime(t: [entier], v: entier) → [entier]
    nombre ← 0
    pour chaque e de t:
        si e == v:
            nombre ← nombre + 1
    t2 ← tableau de taille t.longueur - nombre

    j ← 0
    pour tout i de [0, t.longueur[:
        si t[i] ≠ v:
            t2[j] ← t[i]
            j ← j + 1
    
    rendre t2
```

La finitude du programme est clair puisque l'on a que des boucles de type `pour chaque`{.language-}.

On commence à avoir l'habitude des invariants, on peut donc se permettre d'uniquement écrire le résultat d'une boucle **si celle ci est évidente**. C'est le cas de la première boucle : à l'issue de la boucle des lignes 3-5 `nombre`{.language-} vaut le nombre d'occurrences de `v`{.language-} dans `t`{.language-}.

Pour prouver la seconde boucle, l'invariant peut-être :

> à la fin de chaque itération, `t2`{.language-} contient la restriction des `i + 1`{.language-} premiers éléments de `t` différents de `v`{.language-}.

La preuve de l'invariant est évidente et permet de prouver l'algorithme en se plaçant à la fin de la dernière itération.

{% enddetails %}

Utilisez l'algorithme `concaténation`{.language-} de la question précédente pour résoudre l'exercice suivant :

<span id="suppression-valeur-récursif"></span>

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
supprime_rec(t: [entier], v: entier) → [entier]
```

Qui rend **un nouveau tableau** contenant la restriction de `t`{.language-} aux valeurs différentes de `v`{.language-}. Le nouveau tableau aura la même taille que le tableau `t`{.language-} passé en premier paramètre.
{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme supprime_rec(t: [entier], v: entier) → [entier]
    si t.longueur == 0:
        rendre t

    t2 ← tableau de longueur t.longueur - 1
    pour i de [0, t2.longueur[:
        t2[i] ← t[i + 1]
    
    si t[0] == v:
        rendre concaténation([], supprime_rec(t2, v))
    sinon:
        rendre concaténation([t[0]], supprime_rec(t2, v))
```

Il n'y a qu'une seule récursion par algorithme et la taille du tableau passé en paramètre est strictement plus petite : il y a un nombre finie de récursion puisque la condition terminale est basée sur une taille nulle de tableau.

Pour la correction une récurrence immédiate sur la taille du tableau nous permet de conclure.

{% enddetails %}

## <span id="retournement"></span>Retournement d'un tableau

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
reverse_indice(t: [entier], i: entier) → ∅
```

Qui **modifie le tableau** passé en entrée (il ne rend rien !) de telle sorte que les éléments $t[j]$ et $t[t.\mbox{longueur} - 1 - j]$ soit échangés pour tous $i \leq j < t.\mbox{longueur} - i$
{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme reverse_indice(t: [entier], i: entier) → ∅
    si t.longueur - 1 - i > i:
        temp ← t[i]
        t[i] ← t[t.longueur - 1 - i]
        t[t.longueur - 1 - i] ← temp

        reverse_indice(t, i + 1)
```

Les lignes 3-5 permettent d'échanger les valeurs `t[i]`{.language-} et `t[t.longueur - 1 - i]`{.language-} du tableau. On peut aussi écrire `t[i], t[t.longueur - 1 - i] ← t[t.longueur - 1 - i], t[i]`{.language-}, comme on le ferait en python, si l'on autorise le fait d'affecter 2 valeurs **en même temps**.

Le finitude est claire puisque :

1. il n'y a qu'un appel récursif
2. chaque appel se rapproche strictement de la condition d'arrêt

La correction vient du fait que l'on échange bien des valeurs symétriques du tableau par rapport à l'indice du milieu du tableau qui est ici la partie entière de $t.\mbox{longueur} - 1/ 2$.

{% enddetails %}
{% attention %}
Lorsque l'on manipule des indices de tableau il faut **toujours** :

1. attentivement vérifier que tout se passe bien.
2. faire attention aux divisions entières.

{% endattention %}

Lorsque l'on crée des algorithmes récursif, on a souvent besoin d'initialiser les paramètres. Par exemple si l'on veut retourner complètement un tableau il faudrait écrire `reverse_indice(t: [entier], 0)`{.language-}. Le paramètre $i$ est un paramètre important pour la récursion mais inutile pour l'appel global. Pour éviter d'avoir des paramètres inutile on _encapsulera_ la fonction récursive dans un algorithme dont le seul but est d'initialiser la récursion. Pour le retournement d'un tableau, l'algorithme sera :

```pseudocode
fonction reverse_indice(t: [entier], i: entier) → ∅
    ...  # code de la fonction récursive

algorithme reverse(t: [entier]) → ∅
    reverse_indice(t, 0)
```

La méthode ci-dessus est indispensable à connaître car lorsque l'on manipule des algorithmes récursifs les paramètres font office de variables que l'opn pourrait avoir pour des algorithmes itératifs.

Entraînons nous :

{% exercice %}
Encapsulez la fonction récursive `maximum_rec(t: [réel], i: entier) → entier`{.language-pseudocode} du premier exercice dans une fonction permettant de rendre le maximum d'un tableau passé en paramètre.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme maximum(t: [entier]) → entier
    rendre maximum_rec(t, 0)
```

{% enddetails %}

## Récursion terminale

{% lien %}
[Récursion terminale](https://fr.wikipedia.org/wiki/R%C3%A9cursion_terminale)
{% endlien %}

```pseudocode

algorithme f(n: A) → B:
    si c(n) == Vrai:
        rendre g(n)
    sinon:
        rendre f(h(n))
```

Où `c: A → Booléen`{.language-}, `g: A → B`{.language-} et `h: A → A`{.language-} sont trois fonctions parfaitement définies.

Pour que la définition de `f`{.language-} ait du sens il faut bien sur que chaque récursion sr _rapproche_ de la condition d'arrêt. C'est ce qu'il faut démontrer pour chaque algorithme sous la forme d'une récursion terminale.

La récursion terminale est sympathique car équivalente à la forme itérative suivante :

```pseudocode
algorithme f(n: A) → B:
    tant que c(n) est Faux:
        n ← h(n)
    rendre g(n)
```

Ce qui permet une implémentation en machine efficace (c'est ce que font les compilateur lorsque'ils repèrent une telle forme).

Le type `A`{.language-} peut être de toute forme, c'est souvent un type composé comme on le verra.

### Puissance de deux

{% exercice %}

Écrivez sous la forme d'une récursion terminale l'algorithme de signature :

```pseudocode
algorithme puissance_2(m: entier, n: entier) → entier
```

Qui rend le plus petit entier de la forme $2^p \cdot m$ plus grand que $n$.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme puissance_2(m: entier, n: entier) → entier:
    si m ≥ n:
        rendre m
    sinon:
        rendre f(2 * m, n)
```

C'est bien une récursion terminale puisque le code est équivalent à :

```pseudocode
fonction c(m: entier, n: entier) → entier:
    rendre m ≥ n

fonction g(m: entier, n: entier) → entier:
    rendre m

algorithme puissance_2(m: entier, n: entier) → entier:
    si c(m, n) == Vrai:
        rendre g(m, n)
    sinon:
        rendre f(2 * m, n)
```

Avec le type `A` étant un couple d'entier et `B` le type entier.

{% enddetails %}

### Transformer en une forme terminale

La récursion terminale ne fait aucun calcul en propre, il envoie de nouveaux paramètres. Cela semble très restrictif. Par exemple notre [fonction factorielle récursive](../prouver-un-algorithme/#fact-rec) n'est pas sous forme terminale puisque l'on fait un calcul en plus de la récursion :

```pseudocode
algorithme factorielle(n: entier  # n > 1
                      ) → entier:
    si n == 1:
        rendre 1
    rendre n * factorielle(n-1)
```

Le rendre récursif terminal est impossible en ne gardant qu'un seul paramètre. L'astuce est d'ajouter un paramètre, appelé **_accumulateur_** qui va transmettre à la fonction récursive les calculs intermédiaire, dans notre cas le début du calcul de factoriel. Dans notre cas :

```pseudocode
function factorielle_term(n: entier, acc: entier) → entier:
    si n == 1:
        rendre acc
    rendre factorielle(n-1, n * acc)


algorithme factorielle(n: entier  # n > 1
                      ) → entier:
    rendre factorielle_term(n, 1)
```

{% exercice %}

Montrer que l'algorithme précédent :

1. est bien sous la forme terminale
2. calcule bien la factorielle

{% endexercice %}
{% details "corrigé" %}

Il est clairement sous la forme récursive terminale. Il fini car chaque récursion se rapproche strictement de la condition d'arrêt.

Enfin, `acc`{.language-} va contenir la factorielle comme le prouve une récursion triviale sur $n$.

{% enddetails %}

La récursion terminale est un moyen efficace d'implémenter des [suites arithmétiques](https://fr.wikipedia.org/wiki/Suite_arithm%C3%A9tique) ou [géométriques](https://fr.wikipedia.org/wiki/Suite_g%C3%A9om%C3%A9trique). Montrez le :

{% exercice %}

Donner un prouvez un algorithme écrit sous la forme d'une récursion terminale permettant de calculer tout élément $u_n$ d'une suite arithmétique définie telle que :

<div>
$$
u_n = \left\{
    \begin{array}{ll}
        u_0 & \mbox{si } n = 0 \\
        r + n_{n-1} & \mbox{sinon.}
    \end{array}
\right.
$$
</div>

{% endexercice %}
{% details "corrigé" %}

```pseudocode
function u_n_term(n: entier, 
                 u0: entier, 
                 r: entier, 
                 acc: entier) → entier:
    si n == 0:
        rendre u0 + acc
    rendre u_n_term(n-1, u0, r, r + acc)


algorithme u_n(n : entier, 
               u0: entier, 
               r : entier
              ) → entier:
    rendre u_n_term(n, u0, r, 0)
```

{% enddetails %}
{% exercice %}

Transformez l'algorithme récursif précédent en un algorithme itératif.

{% endexercice %}
{% details "corrigé" %}

Le but de la récursion terminale est de facile,ent transformer un algorithme récursif en un algorithme itératif cr la récursion est une boucle `tant que`{.language-pseudocode}.

```pseudocode
algorithme u_n(n : entier, 
               u0: entier, 
               r : entier
              ) → entier:
    acc ← 0
    tant que n > 0:
        acc ← r + acc
        n ← n - 1
    
    rendre u0 + acc
```

{% enddetails %}

## <span id="dichotomie"></span>Dichotomie

Le principe de [la recherche dichotomique](https://fr.wikipedia.org/wiki/Recherche_dichotomique) permet de savoir si un entier donné est dans un tableau d'entier trié.

On cherche à savoir si l'entier $v$ est entre les indices $a$ et $b \geq a$ d'un tableau d'entiers $t$. On procède récursivement selon la valeur de $t[\lfloor (a + b)/2 \rfloor]$ :

- si $t[\lfloor (a + b)/2 \rfloor] == v$ on a trouvé l'élément
- si $t[\lfloor (a + b)/2 \rfloor] > v$ on recommence la procédure avec $a' = \lfloor (a + b)/2 \rfloor + 1$ et $b' =b$
- si $t[\lfloor (a + b)/2 \rfloor] < v$ on recommence la procédure avec $a' = a$ et $b' = \lfloor (a + b)/2 \rfloor - 1$

{% exercice %}

Implémentez cet algorithme de façon récursive avec la signature :

```pseudocode
dichotomie_rec(t: [entier], 
               v: entier,
               a: entier,
               b: entier  # b > a
               ) → entier:  #rend -1 si v n'est pas dans t, l'indice où il est présent sinon
```

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme dichotomie_rec(t: [entier], v: entier, a: entier, b: entier) → entier:
    si b > a:
        rendre -1

    m ← (a + b) // 2  # division entière
    si (t[m] == v):
        rendre m
    si (t[m] < v):
        rendre dichotomie_rec(t, v, m + 1, b)
    si (t[m] > v):
        rendre dichotomie_rec(t, v, a, m - 1)
```

Pour la preuve, il suffit de montrer que l'intervalle entre $a$ et $b$ se réduit strictement. **Faites attention**, on a tendance à uniquement remplacer a ou b par m et en oubliant le +1 ou le -1, mais cela va rater si $a = b$ ou si $a + 1 = b$. Ces +1 et -1 ne sont donc pas uniquement des optimisations, ils garantissent le bon fonctionnement de l'algorithme.

{% enddetails %}
{% attention %}
Lorsque l'on code la recherche dichotomique, il faut faire **très attention** à ce que l'on prend comme milieu et comme condition d'arrêt. Sans quoi votre algorithme risque de tourner indéfiniment.

{% endattention %}

A priori l'algorithme précédent n'est pas terminal. Le faire :

{% exercice %}
Utilisez l'algorithme précédent pour écrire l'algorithme récursif terminal qui recherche un élément dans une liste triée de signature :

```pseudocode
recherche(t: [entier], v: entier) → entier
```

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme recherche(t: [entier], v: entier) → entier:
    rendre dichotomie_rec(t, v, 0, t.longueur -1)
```

{% enddetails %}

En déduire une version itérative :

{% exercice %}
Utilisez l'algorithme précédent pour écrire l'algorithme itératif qui recherche un élément dans une liste triée de signature :

```pseudocode
recherche(t: [entier], v: entier) → entier
```

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme recherche(t: [entier], v: entier) → entier:
    a ← 0
    b ← t.longueur -1

    tant que a ≤ b: 
        m ← (a + b) // 2  # division entière
        si (t[m] == v):
            rendre m
        si (t[m] < v):
                a ← m + 1
        si (t[m] > v):
            b ← m - 1

    rendre -1

```

{% enddetails %}

## Fonction 91 de McCarty

{% lien %}
[John McCarty](https://fr.wikipedia.org/wiki/John_McCarthy) fût un informaticien de renom et le créateur [du langage Lisp](https://fr.wikipedia.org/wiki/Lisp) en 1958. Lisp est le premier langage fonctionnel et a été [le deuxième langage de programmation](https://fr.wikipedia.org/wiki/Histoire_des_langages_de_programmation) au monde, deux ans après le Fortran.

{% endlien %}

[La fonction 91 de McCarty](https://fr.wikipedia.org/wiki/Fonction_91_de_McCarthy) est définie telle que :

<div>
$$
M(n) = \left\{
    \begin{array}{ll}
        n-10 & \mbox{si } n > 100 \\
        M(M(n + 11))& \mbox{sinon.}
    \end{array}
\right.
$$
</div>

{% exercice %}
Implémentez l'algorithme récursif qui mime la définition.

{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme M(n: entier) → entier:
    si n > 100:
        rendre n - 10
    sinon:
        x ← M(n + 11)
        rendre M(x)
```

Mais est-ce que ce programme se termine ? Rien n'est moins sur.
{% enddetails %}

Le programme de la question précédente n'est pas forcément un algorithme puisqu'on ne sait pas si les récursion vont s'arrêter. Avant de répondre à cette question, montrons que l'on peut transformer cet algorithme en un programme itératif en appliquant les techniques de la récursion terminale :

{% exercice %}

Montrez que $M^k(n) = g(n, k)$ avec :

<div>
$$
g(n, k) = \left\{
    \begin{array}{ll}
        n & \mbox{si } c = 0 \\
        g(n-10, c-1) & \mbox{si } n > 100 \mbox{ et } c \neq 0 \\
        g(n+11, c+1)& \mbox{sinon.}
    \end{array}
\right.
$$
</div>

En déduire une version itérative pour résoudre McCarty.

{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme M(n: entier) → entier:
    c ← 1

    tant que c ≠ 0:
        si n > 100:
            n ← n - 10
            c ← c - 1
        sinon:
            n ← n + 11
            c ← c + 1
    rendre n
```

{% enddetails %}

On est pas vraiment sur que cette fonction soit bien définie et donc que le programme ci-dessus soit un algorithme ! Montrons le.

{% exercice %}
Démontrez que pour tout entier $n$ tel que $90 \leq n < 101$, on a $M(n) = M(n+1)$ et que l'on arrive à cette égalité en un nombre fini de récursion.

{% endexercice %}
{% details "corrigé" %}

Pour $90 \leq n < 101$, on a :

<div>
$$
\begin{array}{lcl}
M(n) & = & M(M(n + 11))\\
     &   & M((n + 11) - 10)\\
     &   & M(n + 1)
\end{array}
$$
</div>

On arrive à ce résultat en 1 récursion : la ligne 5 de l'algorithme en pseudocode de la question précédente.
{% enddetails %}

{% exercice %}
Déduire de l'exercice précédent que pour tout $n < 101$, il existe $k\geq 1$ et $90 \leq n < 101$ tel que $M(n) = M^k(n')$.
{% endexercice %}
{% details "corrigé" %}

<div>
$$
\begin{array}{lcl}
M(n) & = & M^{2}(n + 11)\\
     &   & M(M(n + 11))\\
     &   & M(M^{2}(n + 22))\\
     &   & M^{3}(n + 22)\\
     &   & \dots\\
     &   & M^{k}(n')\\
\end{array}
$$

</div>

{% enddetails %}

{% exercice %}
Donnez la valeur de $M(n)$ pour tout $n< 101$ et en déduire que la fonction de McCarty est bien définie pour tout entier positif (ie le calcul se fait en un no,bre fini de récursion).

{% endexercice %}
{% details "corrigé" %}

On a $M(91) = M(91 + 1 + \dots + 1) = M(101) = 91$ et pour tout $n < 90$ on il existera $k > 1$ tel que $M(n) = M^k(91) = 91$

Comme il faut un nombre fini d'itération pour passer de $M(n)$ à $M(n+1)$ on en déduit qu'il faut bien un nombre fini d'itération pour calculer $M(91)$ (disons $I$), et donc également pour calculer $M^k(91)$ quelque soit $k>0$ (il en faut $k\cdot I$).

{% enddetails %}

{% exercice %}
En donner un algorithme itératif simple pour la calculer.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme M(n: entier) → entier:
    si n > 100:
        rendre n - 10
    sinon:
        rendre 91
```

Dans le même ordre d'idée que la fonction de Takeuchi.

{% enddetails %}

## Récursion croisée

Une dernière technique qui peut être utile est la récursion croisée qui définie une fonction par rapport à une autre et réciproquement :

{% exercice %}
Écrire les deux fonctions récursives suivantes sans utiliser de division entière :

```pseudocode
algorithme pair(n: entier) → booléen
algorithme impair(n: entier) → booléen
```

Vous pourrez utiliser le fait que `pair(0)`{.language-} est `Vrai`{.language-pseudocode} alors que'`impair(0)`{.language-} est `Faux`{.language-pseudocode}.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme pair(n: entier) → booléen
    si n == 0:
        rendre Vrai
    rendre non impair(n - 1)

algorithme impair(n: entier) → booléen
    si n == 0:
        rendre Faux
    rendre non pair(n - 1)

```

La finitude est claire puisque :

1. il n'y a qu'un appel récursif
2. chaque appel se rapproche strictement de la condition d'arrêt

La correction est évidente par définition de la parité.

{% enddetails %}

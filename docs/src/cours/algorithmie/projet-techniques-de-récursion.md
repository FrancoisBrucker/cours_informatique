---
layout: layout/post.njk
title: "Techniques de Récursion"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Nous y verrons divers moyens de manipuler la récursion de nos algorithmes.

## <span id="encapsulation-récursion"></span>Encapsulation de la récursion

Commençons par deux exercices préparatoires :

<span id="algorithme-palindrome"></span>

{% exercice %}
Donnez et prouvez **un algorithme itératif** de signature :

```pseudocode
palindrome(T: [entier]) → booléen
```

Qui rend Vrai si le tableau est [un palindrome](https://fr.wikipedia.org/wiki/Palindrome).
{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme palindrome(T: [entier]) → booléen
    pour chaque i de [0, T.longueur // 2[:
        si T[i] ≠ T[T.longueur - 1 - i]:
            rendre Faux
    rendre Vrai
```

{% enddetails %}

Et maintenant la version récursive :

<span id="algorithme-palindrome-récursif"></span>

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
palindrome_rec(T: [entier], i: entier) → booléen
```

{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme palindrome_rec(T: [entier], i: entier) → booléen
    si T.longueur - 1 - i ≤ i:
        rendre Vrai
    si  T[i] ≠ T[T.longueur - 1 - i]:
        rendre Faux
    
    rendre palindrome_rec(T, i + 1)
```

Il faut monter que l'algorithme rend Vrai si $T[j] = T[T.\mbox{longueur} - 1 - j]$ pour tous $i \leq j < T.\mbox{longueur} - 1 - i$

La premiere condition est la condition d'arrêt de la récursion puisque dans ce cas là $i$ a dépassé la moitié du tableau.

Puis on utilise l'équation de récurrence :

```pseudocode
palindrome(T) = (T[0] == T[-1]) et palindrome(T[1:-1])
```

{% enddetails %}

Lorsque l'on crée des algorithmes récursif, on a souvent besoin d'initialiser les paramètres. Par exemple si on veut savoir si un tableau est un palindrome en utilisant l'algorithme récursif `palindrome_rec(T: [entier], i: entier) → booléen`{.language-}, il faut écrire `palindrome_rec(T, T.longueur)`{.language-}. Le paramètre $i$ est un paramètre important pour la récursion mais inutile pour l'appel global.

Pour éviter d'avoir des paramètres inutile on _encapsulera_ la fonction récursive dans un algorithme dont le seul but est d'initialiser la récursion.

{% attention "**À retenir**" %}

Cette technique est **à utiliser** dès que l'on a besoin de paramètres récursifs mais non utile pour l'algorithme général.

{% endattention %}

Pour savoir si un tableau est un palindrome, l'algorithme sera :

```pseudocode
fonction palindrome_rec(T: [entier], i: entier) → booléen
    ...  # code de la fonction récursive

algorithme palindrome(T: [entier]) → booléen
    rendre palindrome_rec(T, T.longueur)
```

Entraînons nous :

{% exercice %}
Encapsulez la fonction récursive `maximum_rec(t: [réel], i: entier) → entier`{.language-pseudocode} du premier exercice dans une fonction permettant de rendre le maximum d'un tableau passé en paramètre.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme maximum(T: [entier]) → entier
    rendre maximum_rec(t, T.longueur - 1)
```

{% enddetails %}

## <span id="récursion-terminale"></span>Récursion terminale

{% lien %}
[Récursion terminale](https://fr.wikipedia.org/wiki/R%C3%A9cursion_terminale)
{% endlien %}

Soit l'algorithme `f`{.language-} suivant où `c: A → Booléen`{.language-}, `g: A → B`{.language-} et `h: A → A`{.language-} sont trois fonctions parfaitement définies :

```pseudocode

algorithme f(n: A) → B:
    si c(n) == Vrai:
        rendre g(n)
    sinon:
        rendre f(h(n))
```

L'algorithme `f`{.language-} est sous la forme d'une **_récursion terminale_**, c'est à dire que :

1. **soit** il s'arrête si une condition d'arrêt est vérifiée
2. **soit** il rend une récursion de lui même

Pour que la définition de `f`{.language-} ait du sens il faut bien sur que chaque récursion se _rapproche_ de la condition d'arrêt. C'est ce qu'il faut démontrer pour chaque algorithme sous la forme d'une récursion terminale.

La récursion terminale est sympathique car équivalente à la forme itérative suivante :

```pseudocode
algorithme f(n: A) → B:
    tant que c(n) est Faux:
        n ← h(n)
    rendre g(n)
```

Ce qui permet une implémentation en machine efficace (c'est ce que font les compilateur lorsque'ils repèrent une telle forme).

Le type `A`{.language-} peut être de toute forme, c'est souvent un type composé comme on le verra.

Entraînons nous.

{% exercice %}

L'algorithme `palindrome_rec(T: [entier], i: entier) → booléen`{.language-pseudocode} est sous forme terminale, transformez le en programme itératif.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme palindrome_pas_rec(T: [entier], i: entier) → booléen
    tant que (T.longueur - 1 - i > i): 
        si  T[i] ≠ T[T.longueur - 1 - i]:
            rendre Faux
        i ← i + 1
    rendre Vrai
```

{% enddetails %}

{% exercice %}

L'algorithme `retournement_indice(T: [entier], i: entier) → ∅`{.language-pseudocode} [que l'on a déjà vu](../projet-itératif-récursif/#algorithme-retournement){.interne} est sous forme terminale, transformez le en programme itératif.

En déduire un algorithme itératif permettant de retourner un tableau.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme retournement_indice(t: [entier], i: entier) → ∅
    temp := entier
    tant que (t.longueur - 1 - i > i):
        temp ← t[i]
        t[i] ← t[t.longueur - 1 - i]
        t[t.longueur - 1 - i] ← temp

        i ← i + 1
```

Et donc, en utilisant un petit abus de pseudocode :

```pseudocode
algorithme retournement(t: [entier], i: entier) → ∅
    tant que (t.longueur - 1 - i > i):
        t[i], t[t.longueur - 1 - i] ← t[t.longueur - 1 - i], t[i] 
        i ← i + 1
```

{% enddetails %}

Notez que l'opération consistant à transformer un algorithme récursif sous forme terminale en algorithme itératif est exactement l'opération inverse que l'on a faite pour prouver certains algorithmes itératifs, [comme la factorielle](../prouver-un-algorithme/#facto-iter){.interne}. On retrouve encore une fois que recursion et itération sont deux faces d'une même pièce.

### Construire un algorithme sous forme terminale

{% exercice %}
Écrivez sous la forme d'une récursion terminale l'algorithme de signature :

```pseudocode
algorithme puissance_2(m: entier, n: entier) → entier
```

Qui rend le plus grand entier de la forme $2^p \cdot m$ plus petit que $n$.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme puissance_2(m: entier, n: entier) → entier:
    si 2 * m ≥ n:
        rendre m
    sinon:
        rendre f(2 * m, n)
```

C'est bien une récursion terminale puisque le code est équivalent à :

```pseudocode
fonction c(m: entier, n: entier) → booléen:
    rendre 2 * m ≥ n

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

### <span id="transformer-rec-terminale"></span>Transformer en une forme terminale

La récursion terminale ne fait aucun calcul en propre, il envoie de nouveaux paramètres. Cela semble très restrictif. Par exemple notre [fonction factorielle récursive](../prouver-un-algorithme/#algorithme-factorielle-rec) n'est pas sous forme terminale puisque l'on fait un calcul en plus de la récursion :

```pseudocode
algorithme factorielle(n: entier) → entier:
    si n == 1:  # condition d'arrêt
        rendre 1
    (f := entier) ← factorielle(n-1)
    rendre n * f
```

Le rendre récursif terminal est impossible en ne gardant qu'un seul paramètre. L'astuce est d'ajouter un paramètre, appelé **_accumulateur_** qui va transmettre à la fonction récursive les calculs intermédiaires, dans notre cas le début du calcul de factoriel. Dans notre cas :

```pseudocode
fonction factorielle_term(n: entier, acc: entier) → entier:
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
fonction u_n_term(n: entier, 
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
    (acc := entier) ← 0
    tant que n > 0:
        acc ← r + acc
        n ← n - 1
    
    rendre u0 + acc
```

{% enddetails %}

Transformer un algorithme récursif en un algorithme avec une récursion terminale revient à ajouter des variables à un programme récursif (ses variables sont ses paramètres).

{% attention "**À retenir**" %}
La technique de l'accumulateur (_ie._ l'ajout de variables) est fondamentale pour la création d'algorithme récursif.
{% endattention %}

## Récursion croisée

Une dernière technique qui peut être utile est la récursion croisée qui définie une fonction par rapport à une autre et réciproquement :

<span id="algorithme-pair-impair"></span>

{% exercice %}
Écrire les deux fonctions récursives suivantes sans utiliser de division entière :

```pseudocode
algorithme pair(n: entier) → booléen
algorithme impair(n: entier) → booléen
```

Vous pourrez utiliser le fait que `pair(0)`{.language-} est `Vrai`{.language-pseudocode} alors que `impair(0)`{.language-} est `Faux`{.language-pseudocode}.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme pair(n: entier) → booléen
    si n == 0:
        rendre Vrai
    rendre NON impair(n - 1)

algorithme impair(n: entier) → booléen
    si n == 0:
        rendre Faux
    rendre NON pair(n - 1)

```

La finitude est claire puisque :

1. il n'y a qu'un appel récursif
2. chaque appel se rapproche strictement de la condition d'arrêt

La correction est évidente par définition de la parité.

{% enddetails %}

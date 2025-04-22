---
layout: layout/post.njk
title: "Projet : Écrire et prouver des algorithmes itératifs et récursifs"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous y verrons divers moyens de triturer des tableaux de façon itérative et récursive ainsi que deux techniques fondamentales à connaître :

- [encapsulation de la récursion](./#encapsulation-récursion){.interne}
- [recursion terminale et programme itératif](./#récursion-terminale){.interne}

{% attention "**À retenir**" %}
Une fois un algorithme créé, on le teste toujours sur de petites instances en se mettant à la place de l'ordinateur.

- on numérote chaque ligne
- on note sur une feuille les variables
- on exécute ligne à ligne en notant les différents résultats
- à la fin on vérifie que le retour de l'algorithme est bien correct

{% endattention %}

## Maximum d'un tableau

On a déjà vue [une version itérative de cet algorithme](../prouver-un-algorithme/#algorithme-max-tableau-iter){.interne}, voyons (ou plutôt voyez) comme en faire un version recursive :

<span id="algorithme-max-tableau-rec"></span>

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
maximum_rec(T: [réel], n: entier) → entier
```

Qui rend un indice $0 \leq j \leq n$ tel que $t[j] = \max(\{t[k] \vert 0\leq k \leq n\})$.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme maximum_rec(T: [réel], n: entier) → entier:
    si n == 0:
        rendre 0
    sinon:
        x ← maximum_rec(T, n-1)
        si t[x] > t[n]:
            rendre x
        sinon:
            rendre n
```

Le paramètre `n`{.language-} est un entier qui diminue strictement. Il sera donc à un moment égal à 0 ce qui stoppera la récursion.

La correction se fait par récurrence sur `n`{.language-} allant de `n = 0`{.language-} à `n = T.longueur - 1`{.language-}.

1. initialisation : pour `n = 0`{.language-}, le résultat est clair.
2. hypothèse de récurrence : on suppose que l'algorithme fonctionne pour `n - 1`{.language-}
3. preuve pour `n - 1`{.language-}. Si l'algorithme fonctionne pour `n - 1`{.language-}, `x`{.language-} contient l'indice max des indices allant de 0 à `n - 1`{.language-} et on rend `x` si `T[x] > T[n]` et `n` sinon : on rend bien l'indice de la valeur maximale du tableau.

{% enddetails %}

## Concaténation

<span id="algorithme-concaténation"></span>

{% exercice %}
Donnez et prouvez **un algorithme itératif** de signature :

```pseudocode
concaténation(début: [entier], fin: [entier]) → [entier]
```

Qui rend **un nouveau tableau** contenant la concaténation de `début`{.language-} et de `fin`{.language-}.

Vous utiliserez des invariants de boucle pour le prouver.
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

> si $i_0$ est la valeur de $i$ à la ligne 5 (resp. 9) alors à chaque fin d'itération on a $t[i_0 + 1 + k] == \mbox{début}[k]$ (resp. `fin`{.language-}) pour tout $0\leq k \leq j$.

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

### Intersection non vide

<span id="algorithme-intersection-non-vide"></span>

{% exercice %}
Écrivez **un algorithme itératif** de signature :

```pseudocode
algorithme intersection_non_vide(T1: [entier], T2: [entier]) → booléen
```

Permettant de vérifier que deux tableaux d'entiers $T$ et $T'$ contiennent les mêmes valeurs.
{% endexercice %}
{% info %}
Il faut vérifier qu'il existe $0\leq i < T.\text{\small longueur}$ et $0\leq i' < T'.\text{\small longueur}$ tels que $T[i] = T'[i']$.
{% endinfo %}
{% details "corrigé" %}

```pseudocode/
algorithme intersection_non_vide(T1: [entier], T2: [entier]) → booléen
    pour chaque x de T1:
        pour chaque y de T2:
            si x == y:
                rendre Vrai
    rendre Faux
```

La boucle 3-5 va chercher à trouver x dans T2 : `trouvé`{.language-} ne peut valoir `Vrai`{.language-} que si c'est le cas. Si ce n'est pas le cas, `x`{.language-} n'est pas dans `T2`{.language-} et il faut chercher une autre possibilité d'égalité.

Comme on répète cette boucle intérieure pour tout `x`{.language-} de `T1`{.language-}, l'algorithme ne peut arriver ligne 6 que si $x \not in T2$ pour tout $x \in T1$.

Prouver cet algorithme ne nécessite pas d'invariant de boucle formel.

{% enddetails %}

### Mêmes valeurs

<span id="algorithme-égalité-valeurs"></span>

{% exercice %}
Écrivez **un algorithme itératif** de signature :

```pseudocode
algorithme égalité_valeurs(T1: [entier], T2: [entier]) → booléen
```

Permettant de vérifier que deux tableaux d'entiers $T$ et $T'$ contiennent les mêmes valeurs.
{% endexercice %}
{% info %}
Il faut vérifier que pour pour tout $0\leq i < T.\text{\small longueur}$ il existe $0\leq i' < T'.\text{\small longueur}$ tel que $T[i] = T'[i']$.
{% endinfo %}
{% details "corrigé" %}

```pseudocode/
algorithme égalité_valeurs(T1: [entier], T2: [entier]) → booléen
    pour chaque x de T1:
        trouvé ← Faux
        pour chaque y de T2:
            si x == y:
                trouvé ← Vrai
        si trouvé == Faux:
            rendre Faux

    rendre Vrai
```

Prouver cet algorithme ne nécessite pas d'invariant de boucle formel, mais il faut faire attention à sa construction.

La boucle 4-6 va chercher à trouver x dans T2 : `trouvé`{.language-} ne peut valoir `Vrai`{.language-} que si c'est le cas. Si ce n'est pas le cas, on peut sortir de l'algorithme (ligne 7-8) puisque `x`{.language-} n'est pas dans `T2`{.language-}.

Comme on répète cette boucle intérieure pour tout `x`{.language-} de `T1`{.language-}, l'algorithme est bien correct.

{% enddetails %}

### Permutations

Terminons cette partie avec l'algorithme suivant :

<span id="algorithme-permutation"></span>

{% exercice %}
Écrivez **un algorithme itératif** de signature :

```pseudocode
algorithme permutation(T1: [entier], T2: [entier]) → booléen
```

Permettant de vérifier que deux tableaux d'entiers $T$ et $T'$ contiennent les mêmes éléments (même valeurs répétées le même nombre de fois), c'est à dire de savoir s'il existe une permutation $\sigma$ de $[0, T.\mbox{\small \longueur}[$ telle que $T1[i] = T2[\sigma(i)]$ pour tout $i \in [0, T.\mbox{\small \longueur}[$ (on a pas besoin de la donner).
{% endexercice %}
{% info %}
Vous pourrez utiliser [l'algorithme `nombre`{.language-}](../pseudo-code/#algorithme-nombre-occurrences){.interne} qu'on a déjà étudié.
{% endinfo %}
{% details "corrigé" %}

Il faut pouvoir trouver tous les éléments de $T$ dans $T'$. autant de fois qu'ils sont dans $T$. En utilisant `nombre`{.language-}, on a l'algorithme suivant :

```pseudocode
algorithme égalité(T1: [entier], T2: [entier]) → entier
    pour chaque x de T1:
        si nombre(T1, x) ≠ nombre(T2, x):
            rendre Faux
    rendre Vrai
```

On ne peut rendre Vrai que si tous les éléments de T1 sont dans T2 avec un même montant. Donc uniquement s'il existe une existe une permutation $\sigma$ de $[0, n-1]$ telle que $T[i] = T[\sigma(i)]$ pour tout $i \in [0, n-1]$.

{% enddetails %}

## <span id="suppression-valeur"></span>Suppression de valeurs

<span id="algorithme-suppression-valeur-itératif"></span>

{% exercice %}
Donnez et prouvez **un algorithme itératif** de signature :

```pseudocode
supprime(T: [entier], v: entier) → [entier]
```

Qui rend **un nouveau tableau** contenant la restriction de `t`{.language-} aux valeurs différentes de `v`{.language-}.
{% endexercice %}
{% info %}
Vous pourrez la encore utiliser [l'algorithme `nombre`{.language-}](../pseudo-code/#algorithme-nombre-occurrences){.interne}.
{% endinfo %}
{% details "corrigé" %}

Pour que l'algorithme fonctionne, il faut commencer par connaître la taille du tableau à créer et donc compter le nombre d’occurrences de `v`{.language-} dans `T`{.language-}. Ensuite, il sera possible de remplir le tableau.

```pseudocode/
algorithme supprime(T: [entier], v: entier) → [entier]
    T2 ← tableau de taille t.longueur - nombre(T, v)

    j ← 0
    pour tout i de [0, t.longueur[:
        si T[i] ≠ v:
            T2[j] ← t[i]
            j ← j + 1
    
    rendre T2
```

La finitude du programme est clair puisque l'on a que des boucles de type `pour chaque`{.language-}.

On commence par créer un tableau permettant exactement de stocker tous les éléments de `T`{.language-} différents de `v`{.language-}. Ce que fera la boucle. On peut prouver celle-ci par l'invariant :

> à la fin de chaque itération, `T2`{.language-} contient la restriction des `i + 1`{.language-} premiers éléments de `T` différents de `v`{.language-}.

La preuve de l'invariant est évidente et permet de prouver l'algorithme en se plaçant à la fin de la dernière itération.

{% enddetails %}

Et maintenant la version récursive :

<span id="algorithme-suppression-valeur-récursif"></span>

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
supprime_rec(T: [entier], v: entier) → [entier]
```

Qui rend **un nouveau tableau** contenant la restriction de `T`{.language-} aux valeurs différentes de `v`{.language-}.
{% endexercice %}
{% info %}
Vous pourrez utiliser [l'algorithme `concaténation`{.language-}](./#algorithme-concaténation){.interne} de la question précédente.
{% endinfo %}
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
    pour tout i de [0, T.longueur // 2[:
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

Qui rend Vrai si $T[j] = T[T.\mbox{longueur} - 1 - j]$ pour tous $i \leq j < T.\mbox{longueur} - 1 - i$
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

## Retournement d'un tableau

<span id="algorithme-retournement"></span>

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
retournement_indice(t: [entier], i: entier) → ∅
```

Qui **modifie le tableau** passé en entrée (il ne rend rien !) de telle sorte que les éléments $t[j]$ et $t[t.\mbox{longueur} - 1 - j]$ soient échangés pour tous $i \leq j < t.\mbox{longueur} - i$
{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme retournement_indice(T: [entier], i: entier) → ∅
    si T.longueur - 1 - i > i:
        temp ← T[i]
        T[i] ← T[T.longueur - 1 - i]
        T[T.longueur - 1 - i] ← temp

        retournement_indice(T, i + 1)
```

Les lignes 3-5 permettent d'échanger les valeurs `t[i]`{.language-} et `t[t.longueur - 1 - i]`{.language-} du tableau. On peut aussi écrire `t[i], t[t.longueur - 1 - i] ← t[t.longueur - 1 - i], t[i]`{.language-}, comme on le ferait en python, si l'on autorise le fait d'affecter 2 valeurs **en même temps**.

Le finitude est claire puisque :

1. il n'y a qu'un appel récursif
2. chaque appel se rapproche strictement de la condition d'arrêt

La correction vient du fait que l'on échange bien des valeurs symétriques du tableau par rapport à l'indice du milieu du tableau qui est ici la partie entière de $t.\mbox{longueur} - 1/ 2$.

{% attention %}
Lorsque l'on manipule des indices de tableau il faut **toujours** :

1. attentivement vérifier que tout se passe bien.
2. faire attention aux divisions entières.

{% endattention %}
{% enddetails %}

{% exercice %}
Encapsulez la fonction récursive `retournement_indice(t: [entier], i: entier) → ∅`{.language-pseudocode} pour qu'elle puisse retourner un tableau passer en paramètre.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
fonction retournement_indice(T: [entier], i: entier) → ∅
    ...  # code de la fonction récursive

algorithme retournement(T: [entier]) → ∅
    retournement_indice(T, 0)
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

L'algorithme `retournement_indice(T: [entier], i: entier) → ∅`{.language-pseudocode} est sous forme terminale, transformez le en programme itératif.

En déduire un algorithme itératif permettant de retourner un tableau.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme retournement_indice(t: [entier], i: entier) → ∅
    tant que (t.longueur - 1 - i > i):
        temp ← t[i]
        t[i] ← t[t.longueur - 1 - i]
        t[t.longueur - 1 - i] ← temp

        i ← i + 1
```

Et donc, en utilisant un petit abus de pseudocode :

```pseudocode
algorithme retournement(t: [entier], i: entier) → ∅
    i ← 0
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
fonction c(m: entier, n: entier) → entier:
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

### Transformer en une forme terminale

La récursion terminale ne fait aucun calcul en propre, il envoie de nouveaux paramètres. Cela semble très restrictif. Par exemple notre [fonction factorielle récursive](../prouver-un-algorithme/#algorithme-factorielle-rec) n'est pas sous forme terminale puisque l'on fait un calcul en plus de la récursion :

```pseudocode
algorithme factorielle(n: entier) → entier:
    si n == 1:  # condition d'arrêt
        rendre 1
    f ← factorielle(n-1)
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

## <span id="fonction-McCarty"></span>Fonction 91 de McCarty

Terminons cette partie par une bizarrerie algorithmique comme on les aime. Elle vient de [John McCarty](https://fr.wikipedia.org/wiki/John_McCarthy), informaticien de renom et créateur [du langage Lisp](https://fr.wikipedia.org/wiki/Lisp) en 1958. Lisp est le premier langage fonctionnel et a été [le deuxième langage de programmation](https://fr.wikipedia.org/wiki/Histoire_des_langages_de_programmation) au monde, deux ans après [le Fortran](https://fr.wikipedia.org/wiki/Fortran).

{% lien %}
[La fonction 91 de McCarty](https://fr.wikipedia.org/wiki/Fonction_91_de_McCarthy) :
{% endlien %}

Définition :

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

<span id="algorithme-mc-carty"></span>

{% exercice %}
Implémentez **un algorithme récursif** qui mime la définition.

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

Comme on peut écrire cette fonction comme une recursion terminale, l'écriture iterative est aisée :
Pour $90 \leq n < 101$, on a :

<div>
$$
\begin{array}{lcl}
M(n) & = & M(M(n + 11))\\
     & = & M((n + 11) - 10)\\
     & = & M(n + 1)
\end{array}
$$
</div>

On arrive à ce résultat en 1 récursion : la ligne 5 de l'algorithme en pseudocode de la question précédente.
{% enddetails %}

{% exercice %}
Déduire de l'exercice précédent que pour tout $n < 101$, il existe $k\geq 1$ et $90 \leq n' < 101$ tels que $M(n) = M^k(n')$.
{% endexercice %}
{% details "corrigé" %}

<div>
$$
\begin{array}{lclr}
M(n) & = & M^{2}(n + 11)&\\
     & = & M(M(n + 11))&\\
     & = & M(M^{2}(n + 22))&\\
     & = & M^{3}(n + 22)&\\
     & = & \dots&\\
     & = & M^{p}(n + (p-1) \cdot 11)&\\
     & = & M^{k}(n') &\mbox{ avec $k$ le premier entier tel que } n+(k-1)\cdot 11 \geq 90\\
\end{array}
$$

</div>

{% enddetails %}

{% exercice %}
Donnez la valeur de $M(n)$ pour tout $n< 101$ et en déduire que la fonction de McCarty est bien définie pour tout entier positif (_ie._ le calcul se fait en un nombre fini de récursion).

{% endexercice %}
{% details "corrigé" %}

On a $M(91) = M(92) = \dots = M(101) = 91$ et pour tout $n < 90$ on il existera $k > 1$ et $91\leq n'< 101 tels que $M(n) = M^k(n') = 91$

Comme il faut un nombre fini d'itération pour passer de $M(n)$ à $M(n+1)$ on en déduit qu'il faut bien un nombre fini d'itération pour calculer $M(91)$ (disons $I$), et donc également pour calculer $M^k(91)$ quelque soit $k>0$ (il en faut $k\cdot I$).

{% enddetails %}

{% exercice %}
En déduire **un algorithme itératif** ultra simple pour la calculer.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme M(n: entier) → entier:
    si n > 100:
        rendre n - 10
    sinon:
        rendre 91
```

Dans le même ordre d'idée que [la fonction de Takeuchi](../bases-théoriques/calculabilité/#fonction-Takeuchi){.interne}, c'est un leurre.

{% enddetails %}

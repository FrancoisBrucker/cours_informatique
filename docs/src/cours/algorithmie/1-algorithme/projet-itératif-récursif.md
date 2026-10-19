---
layout: layout/post.njk
title: "Projet : Écrire et prouver des algorithmes itératifs et récursifs"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% retenir %}
Une fois un algorithme créé, on le teste toujours sur de petites instances en se mettant à la place de l'ordinateur.

- on numérote chaque ligne
- on note sur une feuille les variables
- on exécute ligne à ligne en notant les différents résultats
- à la fin on vérifie que le retour de l'algorithme est bien correct

{% endretenir %}

<!-- TBD

-  ajouter le code en python + invariant de boucle avec le débugueur
 -->


## Démontrer un invariant donné

L'algorithme suivant est variante itérative de l'algorithme factoriel que nous avons déjà vu :

<div id="algo-factorielle_variante"></div>

```pseudocode
algorithme factorielle_variante(n: int):
    ref r ← 1
    ref i ← n
    tant que i ≥ 1:
        r ← r * i
        i ← i - 1
    rendre r
```

{% details "code python" %}

```python
def factorielle_variante(n):
    r = 1
    i = n
    while i > 1:
        r *= i
        i -= 1
    return r
```

{% enddetails %}

Vous allez démontrer que cet algorithme calcule également la factorielle :

{% exercice %}
Démontrez la finitude du programme `factorielle_variante`{.language-}.
{% endexercice %}
{% details "corrigé" %}

Si $i$ est un nombre  qui décroît de 1 à chaque itération : à une itération il sera forcément plus petit ou égal à 1.
{% enddetails %}

{% exercice %}
Montrez que la boucle `tant que`{.language-} de l'algorithme `factorielle_variante`{.language-} admet l'invariant de boucle suivant :

> **Invariant de boucle :**  À la fin d'une itération de la boucle `tant que`{.language-} : $r = \frac{n!}{i!}$

{% endexercice %}
{% details "corrigé" %}

1. à la fin de la première itération $i = n - 1$ et $r = n = (i+1)$ : notre invariant est vérifié.
2. on suppose la propriété vraie à la fin de la $k$ème itération. A la fin de l'itération suivante on a :
   - $r' = r \cdot i$ (le $r$ de la fin de la $k+1$ème boucle est égal à celui de la fin de la $k$ème boucle fois le $i$ de la fin de $k$ème boucle)
   - $i' = i - 1$ (le $i$ de la fin de la $k+1$ème boucle est le $i$ de la fin de la $k$ème boucle moins 1)
   - $r = (i+1) \cdot \dots n$ (c'est notre invariant, vrai à la fin de l'itération $k$ ar hypothèse)
3. on a donc : $r' = ((i+1) \cdot \dots \cdot n) \cdot (i) = i \cdot \dots \cdot n = (i'+1) \cdot \dots \cdot n = \frac{n!}{i'!}$ : **notre invariant est vérifié**.

{% enddetails %}

{% exercice %}
Déduire de l'exercice précédent que l'algorithme `factorielle_variante`{.language-} calcule bien la factorielle de son entrée.
{% endexercice %}
{% details "corrigé" %}

L'invariant étant vérifié à la fin de chaque itération, il est donc aussi vrai à la fin de la dernière itération. A ce moment là, on a $i=1$ et donc $r = 1 \cdot 2 \cdot \dots \cdot n = n!$

{% enddetails %}

## Trouver un invariant

Vous trouverez ci-après une version itérative de l'algorithme de la division euclidienne que vous allez prouver par invariant de boucle.

<span id="algorithme-division-euclidienne"></span>

```pseudocode
algorithme division_euclidienne(a: int,
                                b: int) → []int:
    ref r ← a
    ref q ← 0
    
    tant que r ≥ b:
        r ← r - b
        q ← q + 1
    
    rendre [q, r]
```

{% details "code python" %}

```python
def division_euclidienne(a, b):
    r = a
    q = 0
    while r >= b:
        r -= b
        q += 1
    return (q, r)
```

Le retour de la fonction python est un [tuple](https://docs.python.org/fr/3/tutorial/datastructures.html#tuples-and-sequences){.externe} à 2 éléments (c'est à dire un tableau à 2 éléments que l'on ne peut pas modifier)
{% enddetails %}

Le retour de notre algorithme est un tableau à deux éléments.

{% exercice %}
Démontrez la finitude du programme `division_euclidienne`{.language-}.
{% endexercice %}
{% details "corrigé" %}

Si a et b sont des entiers positifs le programme s'arrête car :

- `r`{.language-} est un entier
- `r`{.language-} après une itération est **strictement plus petit** que le `r`{.language-} avant itération
- on s'arrête si `r`{.language-} est strictement plus petit que `b`{.language-}.

{% enddetails %}

On veut montrer que l'on obtient bien une division euclidienne de $a$ par $b$. C'est à dire que $a = bq + r$ avec $r < b$. Regardez bien comment fonctionne la boucle de l'algorithme pour garantir ce résultat.

{% exercice %}
Proposez un invariant de boucle que vous démontrerez.
{% endexercice %}
{% details "corrigé" %}

> **Invariant de boucle :**  `a = r + q * b`{.language-}

Prouvons l'invariant :

1. l'invariant est bien vrai à la fin de la première boucle puisque $q=1$ et $r=a-b$ à ce moment là.
2. on doit prouver que `a' = r' + q' * b'`{.language-} à la fin de la $i+1$ème itération.
3. si l'on est passé dans la boucle on a `a'=a`{.language-}, `r' = r - b`{.language-}, `b' = b`{.language-} et `q' = q + 1`{.language-}
4. donc `r' + q' * b' = r-b + (q+1) * b = r + q * b = a = a'`{.language-} puisque l'invariant est vrai à la fin de la $i$ème itération. On a bien `a' = r' + q' * b'`{.language-}, l'invariant est démontré.

{% enddetails %}
{% exercice %}
Utilisez votre invariant de boucle pour démontrer la correction de l'algorithme `division_euclidienne`{.language-}.
{% endexercice %}
{% details "corrigé" %}
L'invariant étant juste tout le temps, il l'est en particulier à l'issue de la dernière boucle. A ce moment là on a `a = r + qb`{.language-} avec `r < b`{.language-} ce qui est bien ce qu'il fallait démontrer.

{% enddetails %}

## Créer un algorithme simple

### Itératif

<span id="algorithme-nombre-occurrences"></span>

{% exercice %}
Créer et prouver un algorithme itératif de signature `nombre(T: []int, x: int) → bool`{.language-} qui rend le nombre d’occurrences d'une valeur dans un tableau d'entier.

{% endexercice %}
{% details "corrigé" %}

L'algorithme rend le nombre de fois où `x`{.language-} est présent dans `T`{.language-}

```pseudocode
algorithme nombre(T: []int, x: int) → int:
    ref nb ← 0

    pour chaque e de T:
        si e == x:
            nb ← nb + 1
    rendre nb
```

La finitude est claire puisque on a une unique boucle `pour chaque`{.langage-} qui a forcément un nombre fini d'itérations. On peut très bien dire que l'exactitude est claire aussi puisque l'on parcourt chaque valeur de `T`{.language-}, mais si on veut être plus explicite on peut remarquer que : 

- `nombre(T, x) = nombre(T[:-1], x) + 1`{.language-} si `T[-1] == x`{.language-},
- `nombre(T, x) = nombre(T[:-1], x)`{.language-} si `T[-1] ≠ x`{.language-}.

Et conclure avec une récurrence triviale sur la longueur du tableau.

{% enddetails %}

### Récursif

On a déjà vue [une version itérative de cet algorithme](../problème-preuve/#algorithme-max-tableau-iter), voyons (ou plutôt voyez) comme en faire un version recursive :

<span id="algorithme-max-tableau-rec"></span>

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
maximum_rec(T: []float, n: int) → int
```

Qui rend un indice $0 \leq j \leq n$ tel que $t[j] = \max(\{t[k] \vert 0\leq k \leq n\})$.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme maximum_rec(T: []float, n: int) → int:
    ref x int

    si n == 0:
        rendre T[0]
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
3. preuve pour `n - 1`{.language-}. Si l'algorithme fonctionne pour `n - 1`{.language-}, `x`{.language-} contient l'indice max des indices allant de 0 à `n - 1`{.language-} et on rend `x`{.language-} si `T[x] > T[n]`{.language-} et `n`{.language-} sinon : on rend bien l'indice de la valeur maximale du tableau.

{% enddetails %}


Lorsque l'on crée des algorithmes récursif, on a souvent besoin d'initialiser les paramètres. Ici, si on veut connaître le maximum d'un tableau en utilisant l'algorithme récursif `maximum_rec(T: []float, n: int) → int`{.language-}, il faut écrire `maximum_rec(T, T.longueur - 1)`{.language-}. Le paramètre $n$ est un paramètre important pour la récursion mais inutile pour l'appel global.

Pour éviter d'avoir des paramètres inutile on _encapsulera_ la fonction récursive dans un algorithme dont le seul but est d'initialiser la récursion, c'est à dire que l'on appellera la fonction récursive via un algorithme dont le seul but est de fixer les paramètres de la récursion.

{% exercice %}
Encapsulez la fonction récursive `maximum_rec(T: []float, n: int) → int`{.language-pseudocode} dans un algorithme de signature `maximum(T: []float) → int`{.language-pseudocode} permettant de rendre le maximum d'un tableau passé en paramètre.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme maximum(T: []int) → int
    rendre maximum_rec(t, T.longueur - 1)


fonction maximum_rec(T: []float, n: int) → int:
    ref x int

    si n == 0:
        rendre T[0]
    sinon:
        x ← maximum_rec(T, n-1)
        si t[x] > t[n]:
            rendre x
        sinon:
            rendre n
```

{% enddetails %}

{% retenir %}

La technique de l'encapsulation est **à utiliser** dès que l'on a besoin de paramètres récursifs mais non utile pour l'algorithme général.

{% endretenir %}


## Concaténation

<span id="algorithme-concaténation"></span>

{% exercice %}
Donnez et prouvez **un algorithme itératif** de signature :

```pseudocode
concaténation(début: []int, fin: []int) → []int
```

Qui rend **un nouveau tableau** contenant la concaténation de `début`{.language-} et de `fin`{.language-}.

Vous utiliserez des invariants de boucle pour le prouver.
{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme concaténation(début: []int, fin: []int) → []int
    ref T ← [longueur: début.longueur + fin.longueur]int
    ref i ← -1

    pour chaque j de [0 .. début.longueur[:
        i ← i + 1
        T[i] ← début[j]

    pour chaque j de [0 .. fin.longueur[:
        i ← i + 1
        T[i] ← fin[j]

    rendre T
```

La finitude est claire puisqu'il n'y a que deux boucles de type `pour chaque`{.language-}.

On a deux boucles, il faut donc à priori 2 invariants, un pour chaque boucle. Ici il est clair que l'on va remplir tous les éléments des tableaux `début`{.language-} et `fin`{.language-} dans `t`{.language-}. L'invariant peut être :

> **Invariant de boucle :** si $i_0$ est la valeur de $i$ à la ligne 5 (resp. 9) alors à chaque fin d'itération on a $t[i_0 + 1 + k] == \mbox{début}[k]$ (resp. `fin`{.language-}) pour tout $0\leq k \leq j$.

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

La preuve de l'invariant dans le corrigé est formelle mais évidente. Il n'est pas nécessaire (et on ne le fera plus) d'être aussi rigoureux pour des boucles aussi simple.

{% retenir %}
Lorsque le résultat d'une boucle est évidente, il n'est n'est pas nécessaire de faire une preuve formelle (qui sera souvent lourde et inintéressante).

Dans ces cas, contentez vous de donner l'invariant ou le résultat de la boucle.
{% endretenir %}

## <span id="égalité-tableaux"></span>Égalité de tableaux

### Intersection non vide

<span id="algorithme-intersection-non-vide"></span>

{% exercice %}
Écrivez **un algorithme itératif** de signature :

```pseudocode
algorithme intersection_non_vide(T1: []int, T2: []int) → bool
```

Permettant de vérifier s'il existe un élément de `T1`{.language-} qui est égal à un élément de `T2`{.language-}.
{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme intersection_non_vide(T1: []int, T2: []int) → bool
    pour chaque x de T1:
        pour chaque y de T2:
            si x == y:
                rendre Vrai
    rendre Faux
```

La boucle 3-5 va chercher à trouver `x`{.language-} dans `T2`{.language-} : `trouvé`{.language-} ne peut valoir `Vrai`{.language-} que si c'est le cas. Si ce n'est pas le cas, `x`{.language-} n'est pas dans `T2`{.language-} et il faut chercher une autre possibilité d'égalité.

Comme on répète cette boucle intérieure pour tout `x`{.language-} de `T1`{.language-}, l'algorithme ne peut arriver ligne 6 que si $x \not in T2$ pour tout $x \in T1$.

Prouver cet algorithme ne nécessite pas d'invariant de boucle formel.

{% enddetails %}

### Mêmes valeurs

<span id="algorithme-égalité-valeurs"></span>

{% exercice %}
Écrivez **un algorithme itératif** de signature :

```pseudocode
algorithme égalité_valeurs(T1: []int, T2: []int) → bool
```

Permettant de vérifier que deux tableaux d'entiers `T1`{.language-} et `T2`{.language-} contiennent les mêmes valeurs.
{% endexercice %}
{% info %}
Il faut vérifier que pour pour tout $0\leq i < T1.\text{\small longueur}$ il existe $0\leq i' < T2.\text{\small longueur}$ tel que $T1[i] = T2[i']$.
{% endinfo %}
{% details "corrigé" %}

```pseudocode/
algorithme égalité_valeurs(T1: []int, T2: []int) → bool
    ref trouvé bool
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

La boucle 4-6 va chercher à trouver `x`{.language-} dans `T2`{.language-} : `trouvé`{.language-} ne peut valoir `Vrai`{.language-} que si c'est le cas. Si ce n'est pas le cas, on peut sortir de l'algorithme (ligne 7-8) puisque `x`{.language-} n'est pas dans `T2`{.language-}.

Comme on répète cette boucle intérieure pour tout `x`{.language-} de `T1`{.language-}, l'algorithme est bien correct.

{% enddetails %}

### Permutations

Terminons cette partie avec l'algorithme suivant :

<span id="algorithme-permutation"></span>

{% exercice %}
Écrivez **un algorithme itératif** de signature :

```pseudocode
algorithme permutation(T1: []int, T2: []int) → bool
```

Permettant de vérifier que deux tableaux d'entiers $T$ et $T'$ contiennent les mêmes éléments (même valeurs répétées le même nombre de fois), c'est à dire de savoir s'il existe une permutation $\sigma$ de $[0, T.\mbox{\small longueur}[$ telle que $T1[i] = T2[\sigma(i)]$ pour tout $i \in [0, T.\mbox{\small longueur}[$ (on a pas besoin de la donner).
{% endexercice %}
{% info %}
Vous pourrez utiliser [l'algorithme `nombre`{.language-}](./#algorithme-nombre-occurrences).
{% endinfo %}
{% details "corrigé" %}

Il faut pouvoir trouver tous les éléments de $T$ dans $T'$. autant de fois qu'ils sont dans $T$. En utilisant `nombre`{.language-}, on a l'algorithme suivant :

```pseudocode
algorithme égalité(T1: []int, T2: []int) → int
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
supprime(T: []int, v: int) → []int
```

Qui rend **un nouveau tableau** contenant la restriction de `t`{.language-} aux valeurs différentes de `v`{.language-}.
{% endexercice %}
{% info %}
Vous pourrez utiliser [l'algorithme `nombre`{.language-}](./#algorithme-nombre-occurrences).
{% endinfo %}
{% details "corrigé" %}

Pour que l'algorithme fonctionne, il faut commencer par connaître la taille du tableau à créer et donc compter le nombre d’occurrences de `v`{.language-} dans `T`{.language-}. Ensuite, il sera possible de remplir le tableau.

```pseudocode/
algorithme supprime(T: []int, v: int) → []int
    ref T2 ← []int{longueur: taille t.longueur - nombre(T, v)}

    ref j ← 0
    pour chaque i de [0, t.longueur[:
        si T[i] ≠ v:
            T2[j] ← t[i]
            j ← j + 1
    
    rendre T2
```

La finitude du programme est clair puisque l'on a que des boucles de type `pour chaque`{.language-}.

On commence par créer un tableau permettant exactement de stocker tous les éléments de `T`{.language-} différents de `v`{.language-}. Ce que fera la boucle. On peut prouver celle-ci par l'invariant :

> **Invariant de boucle :** à la fin de chaque itération, `T2`{.language-} contient la restriction des `i + 1`{.language-} premiers éléments de `T` différents de `v`{.language-}.

La preuve de l'invariant est évidente et permet de prouver l'algorithme en se plaçant à la fin de la dernière itération.

{% enddetails %}

Et maintenant la version récursive :

<span id="algorithme-suppression-valeur-récursif"></span>

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
supprime_rec(T: []int, v: int) → []int
```

Qui rend **un nouveau tableau** contenant la restriction de `T`{.language-} aux valeurs différentes de `v`{.language-}.
{% endexercice %}
{% info %}
Vous pourrez utiliser [l'algorithme `concaténation`{.language-}](./#algorithme-concaténation) de la question précédente.
{% endinfo %}
{% details "corrigé" %}

```pseudocode/
algorithme supprime_rec(t: []int, v: int) → []int
    si t.longueur == 0:
        rendre t

    ref t2 ← []int{longueur: t.longueur - 1}
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

## Retournement d'un tableau

<span id="algorithme-retournement"></span>

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
retournement_indice(t: []int, i: int) → ∅
```

Qui **modifie le tableau** passé en entrée (il ne rend rien !) de telle sorte que les éléments $t[j]$ et $t[t.\mbox{longueur} - 1 - j]$ soient échangés pour tous $i \leq j < t.\mbox{longueur} - i$
{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme retournement_indice(T: []int, i: int) → ∅
    si T.longueur - 1 - i > i:
        ref temp ← T[i]
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
Encapsulez la fonction récursive `retournement_indice(t: []int, i: int) → ∅`{.language-pseudocode} pour qu'elle puisse retourner un tableau passer en paramètre.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
fonction retournement_indice(T: []int, i: int) → ∅
    ...  # code de la fonction récursive

algorithme retournement(T: []int) → ∅
    retournement_indice(T, 0)
```

{% enddetails %}
{% exercice %}
L'algorithme `retournement_indice(T: []entier, i: entier) → ∅`{.language-pseudocode} devrait-être est sous forme de [récursion terminale](../pseudo-code/récursifs-itératifs/#récursion-terminale), transformez le en programme itératif.

En déduire un algorithme itératif permettant de retourner un tableau.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme retournement_indice(t: []entier, i: entier) → ∅
    ref temp int
    tant que (t.longueur - 1 - i > i):
        temp ← t[i]
        t[i] ← t[t.longueur - 1 - i]
        t[t.longueur - 1 - i] ← temp

        i ← i + 1
```

Et donc en simplifiant l'écriture :

```pseudocode
algorithme retournement(t: []entier, i: entier) → ∅
    tant que (t.longueur - 1 - i > i):
        t[i], t[t.longueur - 1 - i] ← t[t.longueur - 1 - i], t[i] 
        i ← i + 1
```

{% enddetails %}


## Palindromes

<span id="algorithme-palindrome"></span>

{% exercice %}
Donnez et prouvez **un algorithme itératif** de signature :

```pseudocode
palindrome(s: str) → bool
```

Qui rend Vrai si le tableau est [un palindrome](https://fr.wikipedia.org/wiki/Palindrome){.externe}.
{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme palindrome(s: str) → bool
    pour chaque i de [0, s.longueur // 2[:
        si s[i] ≠ s[T.longueur - 1 - i]:
            rendre Faux
    rendre Vrai
```

La finitude et l'exactitude sont évidents puisque l'on ne fait qu'implémenter la définition.

{% enddetails %}

Et maintenant la version récursive :

<span id="algorithme-palindrome-récursif"></span>

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
palindrome_rec(s: str, i: int) → bool
```

Qui vérifie si : 

- `s`{.language-} est un palindrome si $i=0$,
- `s[i:-i]`{.language-} est un palindrome pour tout $1 \leq i \leq s.\text{longueur}-1$

{% endexercice %}
{% info %}
On considérera qu'un tableau vide (ce qui est le cas si $s.\text{longueur} - 1 - i ≤ i$) est un palindrome.
{% endinfo %}
{% details "corrigé" %}

```pseudocode/
algorithme palindrome_rec(s: str, i: int) → bool
    si s.longueur - 1 - i ≤ i:
        rendre Vrai
    si  s[i] ≠ s[s.longueur - 1 - i]:
        rendre Faux
    
    rendre palindrome_rec(s, i + 1)
```

Il faut monter que l'algorithme rend Vrai si $s[j] = s[s.\mbox{longueur} - 1 - j]$ pour tous $i \leq j < s.\mbox{longueur} - 1 - i$

La premiere condition est la condition d'arrêt de la récursion puisque dans ce cas là $i$ a dépassé la moitié du tableau.

Puis on utilise l'équation de récurrence :

```pseudocode
palindrome(s) = (s[0] == s[-1]) ET palindrome(s[1:-1])
```

{% enddetails %}
{% exercice %}
Encapsulez la fonction récursive `palindrome_rec(s: str, i: int) → bool`{.language-pseudocode} dans une fonction permettant de savoir si une chaîne de caractères est un palindrome.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
fonction palindrome_rec(s: str, i: int) → bool
    si s.longueur - 1 - i ≤ i:
        rendre Vrai
    si  s[i] ≠ s[s.longueur - 1 - i]:
        rendre Faux
    
    rendre palindrome_rec(s, i + 1)

algorithme palindrome(T: str) → bool
    rendre palindrome_rec(s, 0)
```

{% enddetails %}

{% exercice %}

L'algorithme `palindrome_rec(s: str, i: int) → bool`{.language-pseudocode} devrait être écrit sous une forme de [récursion terminale](../pseudo-code/récursifs-itératifs/#récursion-terminale), transformez le en programme itératif.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme palindrome_pas_rec(s: str, i: int) → bool
    tant que (s.longueur - 1 - i > i): 
        si  s[i] ≠ s[s.longueur - 1 - i]:
            rendre Faux
        i ← i + 1
    rendre Vrai
```

{% enddetails %}


## Construire un algorithme sous forme terminale

{% exercice %}
Écrivez sous la forme d'une [récursion terminale](../pseudo-code/récursifs-itératifs/#récursion-terminale) l'algorithme de signature :

```pseudocode
algorithme puissance_2(m: int, n: int) → int
```

Qui rend le plus grand entier de la forme $2^p \cdot m$ plus petit que $n$.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme puissance_2(m: int, n: int) → int:
    si 2 * m ≥ n:
        rendre m
    sinon:
        rendre f(2 * m, n)
```

C'est bien une récursion terminale puisque le code est équivalent à :

```pseudocode
fonction c(m: int, n: int) → booléen:
    rendre 2 * m ≥ n

fonction g(m: int, n: int) → int:
    rendre m

algorithme puissance_2(m: int, n: int) → int:
    si c(m, n) == Vrai:
        rendre g(m, n)
    sinon:
        rendre f(2 * m, n)
```

Avec le type `A` étant un couple d'entier et `B` le type entier.

{% enddetails %}

### <span id="transformer-rec-terminale"></span>Transformer en une forme terminale

La récursion terminale ne fait aucun calcul en propre, il envoie de nouveaux paramètres. Cela semble très restrictif. Par exemple notre fonction factorielle récursive n'est pas sous forme terminale puisque l'on fait un calcul en plus de la récursion :

```pseudocode
algorithme factorielle(n: int) → int:
    si n == 1:  # condition d'arrêt
        rendre 1
    ref f ← factorielle(n-1)
    rendre n * f
```

Le rendre récursif terminal est impossible en ne gardant qu'un seul paramètre. L'astuce est d'ajouter un paramètre, appelé **_accumulateur_** qui va transmettre à la fonction récursive les calculs intermédiaires, dans notre cas le début du calcul de factoriel. Dans notre cas :

```pseudocode
fonction factorielle_term(n: int, acc: int) → int:
    si n == 1:
        rendre acc
    rendre factorielle(n-1, n * acc)


algorithme factorielle(n: int  # n > 1
                      ) → int:
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

La récursion terminale est un moyen efficace d'implémenter des [suites arithmétiques](https://fr.wikipedia.org/wiki/Suite_arithm%C3%A9tique){.externe} ou [géométriques](https://fr.wikipedia.org/wiki/Suite_g%C3%A9om%C3%A9trique){.externe}. Montrez le :

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
fonction u_n_term(n: int, 
                 u0: int, 
                 r: int, 
                 acc: int) → int:
    si n == 0:
        rendre u0 + acc
    rendre u_n_term(n-1, u0, r, r + acc)


algorithme u_n(n : int, 
               u0: int, 
               r : int
              ) → int:
    rendre u_n_term(n, u0, r, 0)
```

{% enddetails %}
{% exercice %}

Transformez l'algorithme récursif précédent en un algorithme itératif.

{% endexercice %}
{% details "corrigé" %}

Le but de la récursion terminale est de facile,ent transformer un algorithme récursif en un algorithme itératif cr la récursion est une boucle `tant que`{.language-pseudocode}.

```pseudocode
algorithme u_n(n : int, 
               u0: int, 
               r : int
              ) → int:
    ref acc ← 0
    tant que n > 0:
        acc ← r + acc
        n ← n - 1
    
    rendre u0 + acc
```

{% enddetails %}

Transformer un algorithme récursif en un algorithme avec une récursion terminale revient à ajouter des variables à un programme récursif (ses variables sont ses paramètres).

{% retenir %}
La technique de l'accumulateur (_ie._ l'ajout de variables) est fondamentale pour la création d'algorithme récursif.
{% endretenir %}

## <span id="fonction-McCarty"></span>Fonction 91 de McCarty

Terminons cette partie par une bizarrerie algorithmique comme on les aime. Elle vient de [John McCarty](https://fr.wikipedia.org/wiki/John_McCarthy){.externe}, informaticien de renom et créateur [du langage Lisp](https://fr.wikipedia.org/wiki/Lisp){.externe} en 1958. Lisp est le premier langage fonctionnel et a été [le deuxième langage de programmation](https://fr.wikipedia.org/wiki/Histoire_des_langages_de_programmation){.externe} au monde, deux ans après [le Fortran](https://fr.wikipedia.org/wiki/Fortran){.externe}.

{% lien %}
[La fonction 91 de McCarty](https://fr.wikipedia.org/wiki/Fonction_91_de_McCarthy){.externe} :
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
algorithme M(n: int) → int:
    si n > 100:
        rendre n - 10
    sinon:
        ref x ← M(n + 11)
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
algorithme M(n: int) → int:
    ref c ← 1

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
algorithme M(n: int) → int:
    si n > 100:
        rendre n - 10
    sinon:
        rendre 91
```

Dans le même ordre d'idée que [la fonction de Takeuchi](../bases-théoriques/calculabilité/#fonction-Takeuchi), c'est un leurre.

{% enddetails %}

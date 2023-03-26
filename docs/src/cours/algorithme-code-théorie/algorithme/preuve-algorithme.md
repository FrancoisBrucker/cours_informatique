---
layout: layout/post.njk 
title: Prouver un algorithme

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "../pseudo-code/"
---

<!-- début résumé -->

Comprendre et démontrer ce que fait un algorithme.

<!-- end résumé -->

Un algorithme a **toujours** un but, quelque chose pour quoi il est fait. Dans ce cours, nous cherchons à créer des algorithmes qui calculent la solution d'un problème. Pour chaque algorithme que vous créerez ou que l'on demandera d'étudier il faudra démontrer :

   1. qu'il s'arrête
   2. qu'il résout le problème

Prouver qu'un algorithme s'arrête fait partie des problèmes théoriques difficiles en informatique. En algorithmie, les algorithmes résolvent des problèmes, ils sont sensés s'arrêter et il sera (normalement) facile de le voir. En revanche, la preuve de l'algorithme est parfois plus délicate. Le problème étant souvent (toujours ?) concentré dans les boucles ou les récursions de l'algorithme, on cherchera à trouver des propriétés qui sont conservées avant et après une itération ou une récursion :

{% note "Pour prouver un algorithme on cherchera à établir :" %}

* une équation de récurrence plus une condition d'arrêt pour prouver un algorithme récursif.
* [un invariant de boucle](https://fr.wikipedia.org/wiki/Invariant_de_boucle) pour des algorithme itératifs. Ces invariants vont alors être conservés jusqu'à la fin de l'algorithme et nous permettre de prouver son résultat.

{% endnote %}

Notez que bien souvent prouver un algorithme et le créer est la même chose. Comprendre comment on peut résoudre un problème donné nous donnera l'algorithme et réciproquement.

A part la recommandation ci-dessus, il n'existe pas vraiment de règles à appliquer pour prouver un algorithme. Seule l'expérience et l'étude des algorithmes classiques vous permettra de trouver facilement comment prouver un algorithme.

{% info %}
Dans la suite, les algorithmes seront tous donnés en python
{% endinfo %}

## Factorielle

### <span id="facto-rec"></span> Algorithme récursif

{% note "Schéma de preuve :" %}
Pour les preuves d'algorithme récursif, le schéma de preuve est quasi-toujours le même : faire une preuve par récurrence.
{% endnote %}

```python
def factorielle(n):
    if n <= 1:
        return 1
    return n * factorielle(n-1)
```

#### Finitude

Si $n$ est un entier, l'algorithme précédent va s'arrêter car $n$ décroît strictement de 1 à chaque appelle récursif et on stoppe si $n \leq 1$.

#### Preuve

Par récurrence sur $n$, avec $n$ entier positif.

Pour $n \leq 1$ `factorielle(0)`{.language-} et `factorielle(1)`{.language-} valent bien bien $1 = 0! = 1!$.
On suppose notre hypothèse de récurrence vraie pour $n-1 \geq 1$. Pour $n > 1$, le retour de `factorielle(n)`{.language-} est `n * factorielle(n-1)`{.language-} qui vaut donc $n \cdot (n-1)! = n!$ par hypothèse de récurrence.

### <span id="facto-iter"></span> Algorithme itératif

On va voir ici 2 versions du même algorithme. L'un qui construit la factorielle en *montant*, et l'autre qui la construit en *descendant*. On prouvera ces 2 algorithmes en utilisant des invariants de boucles :

{% note "Schéma de preuve :" %}
Pour les preuves par invariant de boucle, le schéma de preuve est le suivant :

1. démontrer l'invariant
   1. on vérifie que l'invariant est vrai à la fin de la première itération de la boucle
   2. on suppose l'invariant à la fin de l'itération $k$ de la boucle et on vérifie qu'il est toujours vérifié à la fin de l'itération $k + 1$.
2. l'invariant étant toujours vrai, il est vrai à la sortie de la boucle. A ce moment là, sa valeur doit servir à démontrer le résultat voulu.

Pour simplifier l'écriture, on note avec un `'` (prim) les variables à la fin de la boucle d'itération $k+1$ pour les différentier des variables de la fin de l'itération $k$.
{% endnote %}

Un invariant doit résumer ce que fait la boucle avec une équation qui est toujours vérifiées, même si on modifie des variables.

{% info %}
Il existe des variantes dans les preuves par invariants selon que l'on vérifie juste à la fin de la boucle ou au début et à la fin de l'itération. Les deux formes sont équivalentes, mais il est parfois plus aisée d'utiliser l'une que l'autre.
{% endinfo %}

#### Première version

```python
def factorielle(n):
    r = 1
    i = 1
    while i <= n:
        r *= i
        i += 1
    return r
```

{% info %}
On utilise la possibilité que donne python d'écrire `x += y`{.language-} (*resp.* `x -= y`{.language-}, `x *= y`{.language-} ou encore `x /= y`{.language-}) à la place de `x = x + y`{.language-} (*resp.* `x = x - y`{.language-}, `x = x * y`{.language-}, `x = x / y`{.language-}).
{% endinfo %}

##### <span id="F-iter-1"></span> Finitude

Si $n$ est un entier non nul, l'algorithme va s'arrêter car l'entier $i$ croît strictement de 1 à chaque itération de la boucle `while`{.language-}.

##### <span id="P-iter-1"></span> Preuve

Par invariant de boucle !

{% note %}
Trouver un invariant de boucle peut-être intimidant. Ne le cherchez donc pas tout de suite : commencez par comprendre l'algorithme.

Souvent (toujours ?), c'est dans les boucles que se forme la solution :

1. comprendre l'algorithme c'est comprendre la boucle
2. comprendre la boucle c'est comprendre comment se modifient les variables
3. la modification des variables peut s'exprimer sous la forme d'un invariant

{% endnote %}

Allons-y :

1. l'algorithme retourne $r$ à la fin : ce doit donc être le résultat et il doit valoir $n!$
2. $r$ est multiplié par $i$ à chaque itération
3. $i$ est incrémenté de 1 à chaque itération et commence à 1.

On doit donc avoir un invariant du type *$r \simeq i!$ à la fin de chaque itération* à plus ou moins 1 près. Pour en être sur regardons ce que valent nos variables à la fin de la première itération :

* $r = 1$
* $i = 2$ (on a modifié $i$ après l'avoir multiplié par $r$)

Notre invariant doit donc être :

>$r = (i-1)!$ à la fin de chaque itération.

1. c'est vrai à la fin de la 1ère itération (on a tout fait pour)
2. si c'est vrai à la fin de la $k$ème itération, à la fin de la $k+1$ème itération on a :
   * $r'=r \cdot i$ (le $r$ de la fin de la $k+1$ème boucle est égal à celui de la fin de la $k$ème boucle fois le $i$ de la fin de $k$ème boucle)
   * $i' = i + 1$ (le $i$ de la fin de la $k+1$ème boucle est le $i$ de la fin de la $k$ème boucle plus 1)
   * $r = (i-1)!$ (c'est notre invariant, vrai à la fin de l'itération $k$ ar hypothèse)
3. on a donc : $r' = (i-1)! \cdot i = i! = (i'-1)!$ : **notre invariant est vérifié**.

L'invariant étant vérifié à la fin de chaque itération, il est donc aussi vrai à la fin de la dernière itération. A ce moment là, on a $i=n+1$ et donc $r = n!$

#### Seconde version

```python
def factorielle(n):
    r = 1
    i = n
    while i > 1:
        r *= i
        i -= 1
    return r
```

{% info %}
L'algorithme construit la factorielle en *descendant*.
{% endinfo %}

##### <span id="F-iter-2"></span>  Finitude

Si $n$ est un entier non nul, l'algorithme va s'arrêter car $n$ décroît strictement à chaque itération de la boucle `while`{.language-}.

##### <span id="P-iter-2"></span>  Preuve

par invariant de boucle (et oui).

{% exercice %}
Trouvez un invariant de boucle et servez-vous en pour prouver l'algorithme.
{% endexercice %}
{% details "preuve" %}

Montrons qu'un invariant de boucle de notre algorithme peut-être :

> A la fin d'une itération de la boucle while : $r = (i+1) \cdot (i+2) \dots (n-1) \cdot n$

1. à la fin de la première itération $i = n - 1$ et $r = n = (i+1)$ : notre invariant est vérifié.
2. on suppose la propriété vraie à la fin de la $k$ème itération. A la fin de l'itération suivante on a :
   * $r' = r \cdot i$ (le $r$ de la fin de la $k+1$ème boucle est égal à celui de la fin de la $k$ème boucle fois le $i$ de la fin de $k$ème boucle)
   * $i' = i - 1$ (le $i$ de la fin de la $k+1$ème boucle est le $i$ de la fin de la $k$ème boucle moins 1)
   * $r = (i+1) \cdot \dots n$ (c'est notre invariant, vrai à la fin de l'itération $k$ ar hypothèse)
3. on a donc : $r' = (i+1) \cdot \dots n \cdot (i) = i \cdot (i+1) \dots n = (i'+1) \dots \cdot n$ : **notre invariant est vérifié**.

L'invariant étant vérifié à la fin de chaque itération, il est donc aussi vrai à la fin de la dernière itération. A ce moment là, on a $i=1$ et donc $r = 1 \cdot 2 \cdot \dots \cdot n = n!$

{% enddetails %}

## Maximum d'un tableau

On va voir 2 algorithmes pour calculer la valeur maximum d'un tableau de réels.

### <span id="max-rec"></span> Algorithme récursif

```python
def maximum(tab):
    if len(tab) == 1:
        return tab[0]
    x = maximum(tab[1:])
    if tab[0] < x
        return tab[debut]
    else:
        return x
```

{% info %}
On a utilisé la [copie de sous-listes (*slicing*)]({{"/cours/coder-en-python/listes/"  }}#slice) de python : `tab[1:]`{.language-} est la liste contenant les éléments de `tab`{.language-} à partir de l'index 1 (donc sans le premier élément de `tab`{.language-}).
{% endinfo %}

#### <span id="M-F-rec-1"></span> Finitude

Début augmente strictement et s'arrête lorsqu'il vaut `len(tab) - 1`{.language-}

#### <span id="M-P-rec-1"></span> Preuve

Par récurrence sur la longueur d'un tableau. On vérifie que l'algorithme fonctionne pour une longueur de tableau valant 1, puis on effectue preuve par récurrence sur la longueur du tableau.

### <span id="max-iter"></span> Algorithme itératif

```python
def maximum(t):
    m = t[0]
    for x in t:
        if m < x:
            m = x
    return m
```

#### <span id="M-F-iter-1"></span> Finitude

Clair car une unique boucle for.

#### <span id="M-P-iter-1"></span> Preuve

par invariant de boucle.

Pour trouver l'invariant, on remarque que si $t'$ est le tableau des $n-1$ premiers éléments de $t$ (`t'= t[:-1]`{.language-}), l'algorithme va :

1. faire exactement pareil que pour $t'$
2. vérifiera $m$ avec le dernier élément de $t$.

Notre invariant doit donc lier les $i$ premiers éléments du tableaux à la $i$ème itération : $m$ doit être le plus grand éléments des $i$ premiers éléments du tableaux pour que notre algorithme puisse fonctionner et avec $t'$ et avec $t$.

Lorsque l'on étudie des algorithmes avec des boucles `for`{.language-} il est parfois plus simple d'exhiber directement le nombre d'itérations pour formaliser l'invariant. On utilise alors l'algorithme suivant (qui est strictement équivalent à l'algorithme `maximum`{.language-}) :

```python
def maximum(t):
    m = t[0]
    for i in range(len(t)):
        x = t[i]
        if m < x:
            m = x
    return m
```

L'invariant est alors :

> A la fin d'une itération, $m$ vaut le maximum des $i+1$ premiers élément du tableau.

Après la première itération de la boucle, comme $m$ vaut initialement le premier élément du tableau, on a que $m=t[0]$ qui est bien le maximum des $0+1=1$ premiers éléments du tableau. L'invariant est vérifié à la fin  de la première itération où $i=0$.

On suppose l'invariant vrai à la fin d'une itération. A la fin de l'itération suivante, $m'$ (la valeur de $m$ à l'issue de cette itération) vaut soit $m$ (la valeur de $m$ au début de l'itération) soit $x'=t[i']$ ($i'$ étant la valeur de $i$ pour cette nouvelle itération). Comme $i' = i+1$ et que l'invariant est vrai à la fin de l'itération précédente :

* $m$ vaut le maximum du tableau sur les $i+1$ premiers éléments (hypothèse de récurrence)
* $m' = \max(m, x') = \max(m, t[i']) = \max(m, t[i + 1])$ (ce qu'il se passe dans l'itération suivante)

On en conclut que $m'$ vaut bien le maximum du tableau sur les $i + 2$ premiers éléments.

Notre invariant est vérifié.

L'invariant est donc aussi vrai à la fin des itérations : $m$ vaut le maximum du tableau à la fin de la boucle `for`{.language-} : $m$ est le maximum des valeurs du tableau.

## Division euclidienne

Prouvons l'algorithme de la division euclidienne ci-après :

```python
def euclide(a, b):
    r = a
    q = 0
    while r >= b:
        r -= b
        q += 1
    return (q, r)
```

{% info %}
Notez que le retour de la fonction est un [tuple](https://docs.python.org/fr/3/tutorial/datastructures.html#tuples-and-sequences) à 2 éléments (c'est à dire un tableau à 2 éléments que l'on ne peut pas modifier)
{% endinfo %}

### <span id="div-fini"></span> Finitude

le programme s'arrête ? : Oui si a et b sont des entiers positifs. Car

* `r`{.language-} est un entier
* `r`{.language-} après une itération est **strictement plus petit** que le `r`{.language-} avant itération
* on s'arrête si `r`{.language-} est strictement plus petit que `b`{.language-}.

### <span id="div-preuve"></span> Preuve

On veut montrer que l'on obtient bien une division euclidienne de $a$ par $b$. C'est à dire que $a = bq + r$ avec $r < b$. Pour cela on va s'aider de l'invariant de boucle :

> `a = r + q * b`{.language-}

Prouvons l'invariant :

1. l'invariant est bien vrai à la fin de la première boucle puisque $q=1$ et $r=a-b$ à ce moment là.
2. on doit prouver que `a' = r' + q' * b'`{.language-} à la fin de la $i+1$ème itération.
3. si l'on est passé dans la boucle on a `a'=a`{.language-}, `r' = r - b`{.language-}, `b' = b`{.language-} et `q' = q + 1`{.language-}
4. donc `r' + q' * b' = r-b + (q+1) * b = r + q * b = a = a'`{.language-} puisque l'invariant est vrai à la fin de la $i$ème itération. On a bien `a' = r' + q' * b'`{.language-}, l'invariant est démontré.

L'invariant étant juste tout le temps, il l'est en particulier à l'issue de la dernière boucle. A ce moment là on a `a = r + qb`{.language-} avec `r < b`{.language-} ce qui est bien ce qu'il fallait démontrer.

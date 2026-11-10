---
layout: layout/post.njk
title: Projet Suite additive

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[Les suite multiplicatives](../étude-algorithmique/#suite-multiplicative) vues dans l'étude de l'exponentiation sont une adaptation d'un problème plus ancien, concernant les _suite additives_ :

{% definition %}
Une **_suite additive pour $n$_** est une suite finie d'entiers $(a_i)_{0\leq i \leq r}$ telle que :

- $a_0 = 1$
- $a_r = n$
- $a_i = a_j + a_k$ avec $k \leq j < i$

On note **_$l(n)$_** la longueur minimale d'une chaîne additive pour $n$.
{% enddefinition %}

{% info %}
Comme les exposants se composent de manière additive, les problèmes des suites additives et multiplicatives sont identiques.
{% endinfo %}

Le problème de trouver une valeur exacte à $l(n)$ est compliqué. Nous allons ici utiliser l'approche constructive en créant des algorithmes permettant de générer toutes les possibilités. Le lecteur curieux pourra se reporter volume 2 de _The Art of Programming_ de Knuth pour une histoire détaillée de $l(n)$.

{% attention %}
Testez vos algorithmes en python. Le but de ce projet est d'expérimenter et de voir les différences entre la solution optimale et celle donnée par l'exponentiation indienne.
{% endattention %}

## Utilitaires

### Vérification

{% exercice %}
Écrivez un algorithme qui prend un tableau d'entiers en paramètre et rend `Vrai`{.language-} s'il est additif et `Faux`{.language-} sinon.

Vous pourrez tester sur les tableaux suivants :

- `[2, 4]`{.language-} : non car $T[1] \neq T[0] + T[0]$
- `[1, 2, 3, 4]`{.language-} : oui car :
  - $T[1] = T[0] + T[0]$,  
  - $T[2] = T[1] + T[0]$
  - $T[3] = T[1] + T[1]$
- `[1, 2, 4, 7]`{.language-} : non car $T[3]$ n'est la somme d'aucuns de ses prédécesseurs.
{% endexercice %}
{% details "corrigé" %}

Un tableau $T$
Il faut à chaque indice vérifier si on peut générer $T[i]$ en sommant deux valeurs d'indices précédent :

<div>
$$
T[i] = 
\begin{cases}
1 & \text{si }i = 0\\
T[j] + T[k] \text{avec } j \leq k < i
\end{cases}
$$
</div>

Ce qui peut se faire avec deux boucles `pour chaque`{.language-} imbriquées :

```pseudocode
algorithme est_une_suite_additive(T: []int) → bool:
    si T[0] ≠ 1:
        rendre Faux
    ref ok bool
    pour chaque i de [1 .. u.longueur[:
        ok ← Faux
        pour chaque j de [0 .. i[:
            pour chaque k de [j  .. i [:
                Si T[i] == T[j] + T[k]:
                    ok = True

        si ok est Faux:
            rendre Faux

    rendre Vrai
```

{% enddetails %}
{% details "code python" %}

```python
def est_une_suite_additive(T):

    if T[0] != 1:
        return False
    for i in range(1, len(u)):
        ok = False
        for k in range(i):
            for l in range(k, i):
                if T[i] == T[k] + T[l]:
                    ok = True

        if not ok:
            return False

    return True
```
{% enddetails %}

Cet algorithme ne rend pas 
{% faire %}
Écrivez une fonction qui rende pour une suite additive $a$ une suite $b$ tel que $b[0] = \text{None}$ et $b[i] = (k, j)$ avec :

- $k \leq j < i$
- $a[k] + a[j] = a[i]$
- si $a[k'] + a[j'] = a[i]$ alors soit $j > j'$ soit $j = j'$ et $k \geq k'$

Vous pourrez tester que la fonction rende :

- `[None, (0, 0), (0, 1), (0, 2)]`{.language-} pour `[1, 2, 3, 4]`{.language-}
- `[None, (0, 0), (1, 1), (2, 2), (0, 0), (3, 4)]`{.language-} pour `[1, 2, 4, 8, 2, 10]`{.language-}

{% endfaire %}

### Suite strictement croissante

{% exercice %}
Montrer que d'un suite additive quelconque on peut extraire :

- une suite additive où tous les éléments sont différents
- une suite additive où $a[i] < a[j]$ si $i < j$
  {% endexercice %}
  {% details "solution" %}
  Si $a[i] = a[i']$ avec $i < i'$ supprimer $i'$ ne change pas l'additivité de la suite puisque si $a[u] = a[i'] + a[v]$, alors $u \geq i' > i$ et donc on a aussi $a[u] = a[i] + a[v]$

Enfin, si $a[i] = a[j] + a[k]$ avec $k \leq j < i$ on a $a[i] \geq \max(a[j], a[k])$ les valeurs $a[j]$ et $a[k]$ seront placés avant $a[i]$ si l'on trie les valeurs de $a$ par ordre croissant.
{% enddetails %}

{% faire %}
Écrivez et testez une fonction qui rend la suite passée en paramètre triée et sans doublons. Attention, la suite passée en paramètre ne **doit pas** être modifiée

Vous pourrez utiliser la fonction [`sorted`{.language-}](https://docs.python.org/3/library/functions.html#sorted){.externe} de python pour cela.

Vous pourrez tester sur la suite `[1, 2, 4, 8, 3, 2, 11]`{.language-} (qui doit rendre `[1, 2, 3, 4, 8, 11]`{.language-} sans modifier la liste en entrée)
{% endfaire %}

## Exponentiation vers suite additives

### Suite additive naïve

{% faire %}
Adaptez [la suite multiplicative naïve](../projet-exponentiation/étude-algorithmique/#multiplicatif-naif) pour créer une fonction qui rende une suite additive.

Vous pourrez tester que pour n=5 on obtienne : $[1, 2, 3, 4, 5]$
{% endfaire %}

### Suite additive indienne

{% faire %}
Adaptez [la suite multiplicative indienne](../projet-exponentiation/étude-algorithmique/#multiplicatif-indienne) pour créer une fonction qui rende une suite additive.

Vous pourrez tester que pour n=15 on obtienne : $[1, 2, 4, 8, 3, 7, 15]$
{% endfaire %}

{% faire %}
Optimisez le résultat de l'addition indienne en rendant une suite additive strictement croissante.
{% endfaire %}

{% faire %}
Comparez les coefficients donnés pour la suite indienne classique et optimisée.
{% endfaire %}

## Algorithme exact

{% faire %}
Créez une fonction qui à partir d'une suite additive strictement croissante $a$ à $n$ éléments rend une liste contenant toutes les suites strictement croissantes de la forme $a + [a[j] + a[k]]$ où $k \leq j < \mid a \mid$.

Il faut que toutes les suites rendues soient :

- strictement croissantes
- deux à deux différentes
- les éléments de la liste rendues devront être triés par dernier élément croissant

Vous pourrez tester que la suite `[1, 2, 3]`{.language-} rende `[[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6]]`{.language-}
{% endfaire %}

{% faire %}
Créez une fonction qui à partir de la liste de toutes les suites additives strictement croissantes de taille $n$ triées par dernier élément croissant rende la liste de toutes suites additives strictement croissantes de taille $n+1$ triées par dernier élément croissant.

Vous pourrez tester que :

- `[[1, 2]]`{.language-} rende : `[[1, 2, 3], [1, 2, 4]]`{.language-}
- `[[1, 2, 3], [1, 2, 4]]`{.language-} rende `[[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6], [1, 2, 4, 5], [1, 2, 4, 6], [1, 2, 4, 8]]`{.language-}
  {% endfaire %}

{% faire %}
Rendez la liste :

- des suites strictement croissantes de taille 5
- de toutes les suites strictement croissantes de taille inférieure ou égale à 4
  {% endfaire %}

{% faire %}
Créez une fonction qui prend un entier $n$ en paramètre et rend une liste $l$ où $l[i]$ est la taille de la plus petite suite additive pour $i$.
{% endfaire %}

{% faire %}
pour $n\leq 100$ donnez les différences avec la suite additive indienne.
{% endfaire %}

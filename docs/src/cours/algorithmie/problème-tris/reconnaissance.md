---
layout: layout/post.njk
title: "Reconnaissance d'un tableau trié"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Définissions [le problème de décision](../../complexité-problème/#définition-problème-décision){.interne} associé au problème de savoir si OUI ou NON un tableau d'entiers est trié :

{% note "**Problème de décision**" %}

- **Nom** : est trié ?
- **Entrée** : un tableau $T$ d'entiers
- **Question** : $T$ est-il trié de façon croissante ?

{% endnote %}

## <span id="algorithme-est-trie"></span> Algorithme

Il existe un algorithme très simple pour le résoudre :

```pseudocode/
algorithme est_trie(T: [entier]) → booléen:
    pour chaque (i := entier) de [1 .. T.longueur[:
        si T[i] < T[i-1]:
            rendre Faux
    rendre Vrai
```

### Tests de Fonctionnement

L'algorithme rend bien :

- `Vrai`{.language-} pour `est_trie([42])`{.language-}
- `Faux`{.language-} pour `est_trie([4, 2])`{.language-}
- `Vrai`{.language-} pour `est_trie([2, 4])`{.language-}

### Preuve

La finitude de l'algorithme est claire puisqu'il n'y a qu'une boucle for avec autant d'itérations que la taille du tableau passé en paramètre.

La preuve de correction est tout aussi évidente. Si on arrive en ligne 5 c'est que $T[i-1] \leq T[i]$ pour tout $i \in [1, T.\mbox{\small longueur}[$, donc que le tableau est trié.

{% note "**Proposition**" %}
L'algorithme `est_trie`{.language-} est une solution au problème _"est trié ?"_
{% endnote %}

### Complexité

Ligne à ligne :

1. définition de la fonction $\mathcal{O}(1)$
2. —
3. une boucle for de $K$ itérations
4. un tests de deux valeurs dans un tableau : $\mathcal{O}(1)$
5. un retour de fonction $\mathcal{O}(1)$
6. un retour de fonction $\mathcal{O}(1)$

Que l'on sorte par le retour de la ligne 5 ou 6, le complexité est : $\mathcal{O}(k)$.

#### Cas le pire

Dans le cas le pire, on parcourt tout le tableau, donc :

{% note "**Proposition**" %}
La complexité de l'algorithme `est_trie`{.language-} est $\mathcal{O}(n)$ avec $n$ la taille du tableau en entrée.
{% endnote %}

#### Cas les meilleur

Dans le cas le meilleur, on s'arrête dès la première itération :

{% note "**Proposition**" %}
La complexité minimale de l'algorithme `est_trie`{.language-} est $\mathcal{O}(1)$ avec $n$ la taille du tableau en entrée.
{% endnote %}

#### Complexité en moyenne

La question est délicate. Il faut se demander quel est le modèle sous-jacent à notre tableau de nombres. Si on a aucune information sur la répartition des nombres, on a coutume d'utiliser le modèle suivant :

<span id="définition-modèle-tableau-aléatoire"></span>

{% note "**Définition**" %}

Un tableau $T$ d'entiers de longueur $n$ est **_un tableau aléatoire_** s'il résulte de la procédure suivante :

- on tire [une permutation](https://fr.wikipedia.org/wiki/Permutation) $\sigma$ de $[0, n-1]$ de façon équiprobable (la probabilité de choisir $\sigma$ est $\frac{1}{n!}$)
- $T[i] = \sigma(i)$ pour tout $i \in [0, n-1]$
{% endnote %}

On utilise ce modèle par ce qu'il est simple à mettre en œuvre et à manipuler, tout en possédant de nombreuses propriétés :

{% note "**Proposition**" %}
Si $T$ est un tableau aléatoire, on a que la probabilité que $T[i] = k$, donc que $T[i]$ soit le $k$ plus petit élément du tableau, vaut :

<div>
$$
\mathbb{P}(T[i] = k) = \frac{1}{n}
$$
</div>
{% endnote %}
{% details "preuve", "open" %}

Parmi les $n!$ permutations de $[0, n-1]$ il y en a $(n-1)!$ telles que $\sigma(i) = k-1$. La probabilité d'obtenir une telle permutation est alors $\frac{(n-1)!}{n!} = \frac{1}{n}$.

{% enddetails %}
{% note "**Corollaire**" %}
Si $T$ est un tableau aléatoire, si $k \leq i$ on a :

<div>
$$
\mathbb{P}(T[i] = k)) = \frac{1}{i+1}
$$
</div>
{% endnote %}
{% details "preuve", "open" %}

Tout se passe comme si on considérait un tableau aléatoire de taille $i+1$.

{% enddetails %}

Ce modèle véhicule de nombreuse propriété l'on aimerait avoir pour un tableau de nombres quelconques :

{% exercice %}
Montrez que si $T$ est un tableau aléatoire on a pour tout $u \neq v$ :

<div>
$$
\mathbb{P}(T[u] > T[v]) = \frac{1}{2}
$$
</div>
{% endexercice %}
{% details "corrigé" %}
Prenons $u$ et $v$ deux indices différents du tableau. Tout se passe comme si on avait un tableau aléatoire de taille 2.

{% enddetails %}

Les propriétés précédentes nous permettent de voir que pour notre algorithme de reconnaissance, si $T$ est un tableau aléatoire alors la probabilité :

- $p_1$ de ne faire que 1 itération est $\mathbb{P}(T[0] > T[1])$ et vaut $1/2$
- $p_2$ de ne faire que 2 itérations est $\mathbb{P}(T[0] < T[1], T[1] > T[2])$, donc que $T[:2]$ est trié mais que $T[:3]$ ne l'est pas : cette probabilité vaut $\frac{1}{2!} - \frac{1}{3!}$ (attention, $T[0] < T[1]$ et $T[1] > T[2]$ ne sont pas indépendant, on a donc pas $\mathbb{P}(T[0] < T[1], T[1] > T[2]) = \mathbb{P}(T[0] < T[1])\cdot \mathbb{P}(T[1] > T[2])$)
- ...
- $p_i$ de ne faire que i itérations est la probabilité que $T[:i]$ soit trié mais que $T[:i+1]$ ne le soit pas :  : cette probabilité vaut $\frac{1}{i!} - \frac{1}{(i+1)!}$
- ...
- $p_i$ de ne faire que $n$ itérations est la probabilité que $T[:n]$ soit trié mais que $T$ ne le soit pas :  : cette probabilité vaut $\frac{1}{(n-1)!} - \frac{1}{n!}$

Comme chaque itération est de complexité $\mathcal{O}(1)$, la complexité en moyenne sous ce modèle de probabilité vaut :

<div>
$$
C= \sum_{i=1}^n[p_i \cdot (i \cdot \mathcal{O}(1))] = \sum_{i=1}^{n-1}(\frac{1}{i!} - \frac{1}{(i+1)!}) \cdot \mathcal{O}(i)) = \mathcal{O}(\sum_{i=1}^{n-1}(\frac{i^2}{(i+1)!}))
$$
</div>

Comme $i^4 \leq (i+1)!$ pour $i \geq 5$ on a que :

<div>
$$
C \leq \mathcal{O}(\sum_{i=1}^{n}(\frac{1}{i^2})) = \mathcal{O}(1)
$$
</div>

{% info %}
On a utilisé le fait, [on le démontrera](../../projet-sommes-classiques/){.interne}, que la série est convergente et donc :

<div>
$$
\sum_{i=1}^n\frac{1}{i^2} = \mathcal{O}(1)
$$
</div>

{% endinfo %}

Ce résultat est remarquable sous (au moins) deux aspects :

- la complexité en moyenne est égale à la complexité minimale et est en temps constant !
- ce n'est pas parce que la complexité augmente qu'elle en devient forcément infinie.

{% attention2 "**À retenir**" %}
Borner une complexité par [une série convergente](https://fr.wikipedia.org/wiki/S%C3%A9rie_convergente) est un truc utile pour démontrer qu'un algorithme est en temps constant !
{% endattention2 %}

## Complexité du problème de la reconnaissance

Comme toute case du tableau peut rendre le tableau non trié, on utilise l'argument de [la complexité du problème de la _"recherche"_](../../complexité-problème/#complexité-recherche){.interne}, un algorithme résolvant ce problème doit considérer toutes les cases du tableau et donc une borne min du problème _"est trié ?"_ est $\Omega(n)$ où $n$ est la taille du tableau en entrée. Comme la complexité de `est_trie`{.language-} est de $\mathcal{O}(n)$. On en conclut :

{% note "**Proposition**" %}
La complexité du problème _"est trié ?"_ est de $\Theta(n)$ où $n$ est la taille du tableau en entrée.
{% endnote %}

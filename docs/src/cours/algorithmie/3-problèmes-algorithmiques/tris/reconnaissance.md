---
layout: layout/post.njk
title: "Reconnaissance d'un tableau trié"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Définissions [le problème de décision](../../complexité-problème/#définition-problème-décision) associé au problème de savoir si OUI ou NON un tableau d'entiers est trié :

{% note "**Problème de décision**" %}

- **Nom** : est trié ?
- **Entrée** : un tableau $T$ d'entiers
- **Question** : $T$ est-il trié de façon croissante ?

{% endnote %}

## <span id="algorithme-est-trie"></span> Algorithme

Il existe un algorithme très simple pour le résoudre :

```pseudocode/
algorithme est_trie(T: []int) → bool:
    pour chaque i de [1 .. T.longueur[:
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

## Complexités de l'algorithme `est_trié`{.language-}

Ligne à ligne :

1. définition de la fonction $\mathcal{O}(1)$
2. —
3. une boucle for de $K$ itérations
4. un tests de deux valeurs dans un tableau : $\mathcal{O}(1)$
5. un retour de fonction $\mathcal{O}(1)$
6. un retour de fonction $\mathcal{O}(1)$

Que l'on sorte par le retour de la ligne 5 ou 6, le complexité est : $\mathcal{O}(k)$.

### Cas le pire

Dans le cas le pire, on parcourt tout le tableau, donc :

{% note "**Proposition**" %}
La complexité de l'algorithme `est_trie`{.language-} est $\mathcal{O}(n)$ avec $n$ la taille du tableau en entrée.
{% endnote %}

### Cas le meilleur

Dans le cas le meilleur, on s'arrête dès la première itération :

{% note "**Proposition**" %}
La complexité minimale de l'algorithme `est_trie`{.language-} est $\mathcal{O}(1)$ avec $n$ la taille du tableau en entrée.
{% endnote %}

### Complexité en moyenne

Comme on a pas d'information relative à la répartition des nombre du tableau et que seul l'ordre interne des valeurs du tableau importe pour vérifier s'il est trié ou non, on utilise [le modèle du tableau aléatoire](../../../2-complexités/projet-calcul-max-min-moy/#définition-modèle-tableau-aléatoire) pour nos calculs de complexité en moyenne.

Sous ce modèle pour $T$, la probabilité pour notre algorithme de reconnaissance fasse exactement :

- 1 itération est $p_1 = {\Pr}[T[0] > T[1]]$ et vaut $1/2$
- 2 itérations est $p_2 = {\Pr}[(T[0] < T[1]) \text{ et } (T[1] > T[2])]$
- ...
- i itérations est  $p_i = {\Pr}[(T[0] < T[1]) \text{ et } (T[1] < T[2]) \text{ et } \\;\dots\\; \text{ et } (T[i-2] < T[i-1]) \text{ et } (T[i-i] > T[i])]$
 
Les évènements ne sont pas indépendant donc pour $p_2$ on a que :

<div>
$$
p_2 = {\Pr}[(T[0] < T[1]) \text{ et } (T[1] > T[2])] \neq {\Pr}[T[0] < T[1]] \;\cdot\; {\Pr}[T[1] > T[2]]
$$
</div>

Mais comme :

<div>
$$
{\Pr}[(T[0] < T[1]) \text{ et } (T[1] > T[2])] = {\Pr}[(T[0] < T[1])] \;\cdot\; {\Pr}[T[1] > T[2] \;\mid\; T[1] > T[0]]
$$ 
</div>

et que :

<div>
$$
{\Pr}[T[1] > T[2] \;\mid\; T[1] > T[0]] \leq {\Pr}[T[1] > T[2]]
$$
</div>

puisque la partie gauche est plus contrainte pour $T[2]$ que la partie de droite (on a la valeur de $T[0]$ qui serait favorable en moins). On en conclut que :

<div>
$$
p_2 \leq  {\Pr}[T[0] < T[1]] \;\cdot\; {\Pr}[T[1] > T[2]] = \frac{1}{2} \;\cdot\; \frac{1}{2} = \frac{1}{4}
$$
</div>

Un raisonnement identique nous permet de minorer $p_i$ :

<div>
$$
p_i \leq {\Pr}[T[0] < T[1]] \cdot {\Pr}[T[1] < T[2]]\cdot \;\dots\; \cdot {\Pr}[T[i-2] < T[i-1]]\cdot {\Pr}[ T[i-i] > T[i]] = \frac{1}{2^i}
$$
</div>

Comme chaque itération est de complexité $\mathcal{O}(1)$, la complexité en moyenne sous ce modèle de probabilité vaut :

<div>
$$
\begin{array}{lcl}
C_{\text{moy}}(n) &=& \sum\limits_{i=1}^{n-1}(p_i \cdot (i \cdot \mathcal{O}(1)))\\
 &\leq& \sum\limits_{i=1}^{n-1}(\mathcal{O}(\frac{i}{2^i})) \\
 &\leq& \mathcal{O}(\sum\limits_{i=1}^{n-1}(\frac{i}{2^i}))
\end{array}
$$
</div>

Comme $i \leq (\sqrt{2})^i$ pour tout $i \geq i$ on a :

<div>
$$
\begin{array}{lcl}
C_{\text{moy}}(n)
 &\leq& \mathcal{O}(\sum\limits_{i=1}^{n-1}(\frac{1}{\sqrt{2}})^i)\\
\end{array}
$$
</div>

Et on utilise [un résultat qu'on a déjà démontré](../../../2-complexités/projet-calcul-max-min-moy/#série-géométrique-limite) pour finir la majoration :


<div>
$$
\begin{array}{lcl}
C_{\text{moy}}(n)
 &\leq& \mathcal{O}(\sum\limits_{i=1}^{n-1}(\frac{1}{\sqrt{2}})^i)\\
 &\leq& \mathcal{O}(\sum\limits_{i=0}^{n-1}(\frac{1}{\sqrt{2}})^i)\\
&\leq& \mathcal{O}(\frac{1}{1-\frac{1}{\sqrt{2}}})\\
&\leq& \mathcal{O}(1)
\end{array}
$$
</div>

On a donc la proposition surprenante suivante (mais qu'on a déjà rencontré lors de la [recherche d'un sous-mot](../../../2-complexités/projet-calcul-max-min-moy/#sous-mot)) :

{% note "**Proposition**" %}
La complexité en moyenne du problème de la reconnaissance est en temps constant.
{% endnote %}

Ce résultat est remarquable :

{% retenir %}

- Pour le problème de la reconnaissance : la complexité en moyenne est égale à la complexité minimale et est en temps constant !
- Ce n'est pas parce que la complexité augmente qu'elle en devient forcément infinie.

{% endretenir %}

Je vois bien dans votre regard que vous ne me croyez pas. Essayez donc par vous même :

{% faire %}
Testez le code suivant (chez moi le max était de 4) pour voir que le nombre maximum d'itération est très inférieur à la longueur du tableau (chez moi le max était de 4). 

Puis essayez avec des tableaux plus contraints (comme `T = 5 * list(range(4))`{.language-} par exemple) pour voir que c'est toujours vrai si le tableau possède quelques égalités.
{% endfaire %}


```python
from random import shuffle

def compte(T):
    for i in range(len(T)-1):
        if T[i] > T[i+1]:
            return i +1
    return len(T) - 1


T = list(range(20))


nb = []
for i in range(100):
    shuffle(T)
    nb.append(compte(T))

print(nb)
print(max(nb))

```

On peut aussi comprendre ce résultat remarquant que les tableaux pour lesquels l'algorithme fait exactement $i$ iterations sont ceux pour lesquels :

- le $i+1$ ème élément n'est pas le plus grand
- les $i$ premiers éléments sont triées

Et il y en a très (très) peu : il n'y en a que $i$ tableaux de longueur $i$ sur les $(i+1)!$ possibles qui vérifient cette condition. La probabilité $p_i = \frac{i}{(i+1)!}$ d'en attraper un tend très (très) vite vers 0 :

- $p_1 = \frac{1}{2!} = 0.5$
- $p_2 = \frac{2}{3!} \simeq 0.3$
- $p_3 = \frac{3}{4!} = .1$
- $p_4 = \frac{4}{5!} \simeq 0.003$
- ...
- $p_{9} = \frac{9}{10!} \simeq 2.5 \cdot 10^{-6}$
- ...
- $p_{19} = \frac{19}{20!} \simeq 7.8 \cdot 10^{-18}$

## Complexité du problème de la reconnaissance

Comme toute case du tableau peut rendre le tableau non trié, on utilise l'argument de [la complexité du problème de la _"recherche"_](../complexité-problème/#complexité-recherche), un algorithme résolvant ce problème doit considérer toutes les cases du tableau et donc une borne min du problème _"est trié ?"_ est $\Omega(n)$ où $n$ est la taille du tableau en entrée. Comme la complexité de `est_trie`{.language-} est de $\mathcal{O}(n)$. On en conclut :

{% note "**Proposition**" %}
La complexité du problème _"est trié ?"_ est de $\Theta(n)$ où $n$ est la taille du tableau en entrée.
{% endnote %}


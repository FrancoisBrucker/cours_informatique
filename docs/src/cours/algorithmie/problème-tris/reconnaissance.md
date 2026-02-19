---
layout: layout/post.njk
title: "Reconnaissance d'un tableau trié"

eleventyNavigation:
  prerequis:
    - /cours/misc/probabilités/

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

- on tire [une permutation](https://fr.wikipedia.org/wiki/Permutation) $\sigma$ de $[0 \\, ..\\, n-1]$ de façon équiprobable (la probabilité de choisir $\sigma$ est $\frac{1}{n!}$)
- $T[i] = \sigma(i)$ pour tout $[0 \\, ..\\, n-1]$
{% endnote %}
{% info %}
Dans un tableau aléatoire, toutes les valeurs sont différentes.
{% endinfo %}

On utilise ce modèle par ce qu'il est simple à mettre en œuvre et à manipuler, tout en possédant de nombreuses propriétés :

{% note "**Proposition**" %}
Si $T$ est un tableau aléatoire, la probabilité que $T[i] = k$ vaut :

<div>
$$
{\Pr}[T[i] = k] = \frac{1}{n}
$$
</div>
{% endnote %}
{% details "preuve", "open" %}

Parmi les $n!$ permutations de $[0 \\, ..\\, n-1]$ il y en a $(n-1)!$ telles que $\sigma(i) = k$ (on fixe une valeur parmi $n$, il en reste $n-1$ qui font ce qu'elles veulent). La probabilité d'obtenir une telle permutation est alors $\frac{(n-1)!}{n!} = \frac{1}{n}$.

{% enddetails %}

Comme les valeurs d'un tableau aléatoires sont deux à deux différentes, la proposition précédente peut s'interpréter aussi comme :

<div id="proba-k-tableau-aléatoire"></div>

{% note "**Corollaire**" %}

La probabilité que $T[i]$ soit le $k$ plus petit élément d'un tableau aléatoire de longueur $n$  vaut $\frac{1}{n}$, quelque soit $k$.

{% endnote %}

Enfin, dernière propriété qui va être utile dans les calculs :

{% note "**Corollaire**" %}
Si $T$ est un tableau aléatoire, on a :

<div>
$$
{\Pr}[T[i] > k] = \frac{n-1-k}{n}
$$
</div>

{% endnote %}
{% details "preuve", "open" %}

<div>
$$
\begin{array}{lcl}
{\Pr}[T[i] > k] &=& \sum\limits_{u > k}{\Pr}[[T[i] = u]\\
&=& \sum\limits_{u > k}\frac{1}{n}\\
&=& \frac{n-1-k}{n}\\
\end{array}
$$
</div>


{% enddetails %}

Ce modèle véhicule de nombreuse propriété l'on aimerait avoir pour un tableau de nombres quelconques :


{% exercice %}
Montrez que si $T$ est un tableau aléatoire on a pour tout $u \neq v$ :

<div>
$$
{\Pr}[T[u] > T[v]] = {\Pr}[T[u] < T[v]] = \frac{1}{2}
$$
</div>
{% endexercice %}
{% details "corrigé" %}

Par définition :

<div>
$$
\begin{array}{lcl}
{\Pr}[T[u] > T[v]] &=& \sum\limits_{0\leq i< n}{\Pr}[(T[u] = i) \text{ et } (T[v] > i)]
\end{array}
$$
</div>

Puisque les valeurs de $T[u]$ et de $T[v]$ sont différentes mais indépendantes l'une de l'autre, on a :

<div>
$$
\begin{array}{lcl}
{\Pr}[T[u] > T[v]] &=& \sum\limits_{0\leq i< n}({\Pr}[T[u] = i] \cdot {\Pr}[(T[v] > i) \text{ et } (T[v] \neq i)])
\end{array}
$$
</div>


D'après la proposition précédente et ses deux corollaires :

- ${\Pr}[T[u] = i] = \frac{1}{n}$
- ${\Pr}[(T[v] > i) \text{ et } (T[v] \neq i)] = \frac{\Pr[(T[v] > i) \text{ et } (T[v] \neq i)]}{\Pr[T[v] \neq i]} = \frac{n-1-i}{n} \cdot \frac{1}{\frac{n-1}{n}} = \frac{n-1-i}{n-1}$ (on a que $n-1$ possibilité pour $T[v]$ puisqu'il ne peut pas être égal à $i$)

Ce qui nous permet de conclure :

<div>
$$
\begin{array}{lcl}
{\Pr}[T[u] > T[v]] &=& \sum\limits_{0\leq i< n}({\Pr}[T[u] = i] \cdot {\Pr}[(T[v] > i) \text{ et } (T[v] \neq i)])\\
&=& \sum\limits_{0\leq i< n}(\frac{1}{n} \cdot \frac{n-1-i}{n-1})\\
&=& \frac{1}{n(n-1)}\sum\limits_{0\leq i< n}(n-1-i)\\
&=& \frac{1}{n(n-1)}\sum\limits_{0\leq j< n}(j)\\
&=& \frac{1}{n(n-1)}\cdot \frac{n(n-1)}{2}\\
&=& \frac{1}{2}\\
\end{array}
$$
</div>

{% enddetails %}

Les propriétés précédentes nous permettent de voir que si $T$ est un tableau aléatoire alors la probabilité pour notre algorithme de reconnaissance fasse exactement :


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
C_{\text{moy}}(n) &=& \sum_{i=1}^{n-1}(p_i \cdot (i \cdot \mathcal{O}(1)))\\
 &\leq& \sum_{i=1}^{n-1}(\frac{1}{2^i} \cdot \mathcal{O}(i)) \\
 &\leq& \mathcal{O}(\sum_{i=1}^{n-1}(\frac{i}{(2^i)!}))
\end{array}
$$
</div>

Or la série des $\sum_{i=1}^{n}(\frac{i}{2^i})$ est toujours plus petite que 2 ([on le démontrera](../../projet-sommes-classiques/#problème-i/2^i){.interne}) donc :

<div>
$$
C_\text{moy}(n) \leq \mathcal{O}(\sum_{i=1}^{n}(\frac{i}{2^i})) \leq \mathcal{O}(2) = \mathcal{O}(1)
$$
</div>

On a donc la proposition surprenante suivante :

{% note "**Proposition**" %}
La complexité en moyenne du problème de la reconnaissance est en temps constant.
{% endnote %}

Ce résultat est remarquable :

{% attention2 "**À retenir**" %}

- Pour le problème de la reconnaissance : la complexité en moyenne est égale à la complexité minimale et est en temps constant !
- Ce n'est pas parce que la complexité augmente qu'elle en devient forcément infinie.
- Borner une complexité par [une série convergente](https://fr.wikipedia.org/wiki/S%C3%A9rie_convergente) est très utile pour démontrer qu'un algorithme est en temps constant.

{% endattention2 %}


Notez que l'on a utilisé un majorant des $p_i$ pour que le calcul soit aisé, mais on peut très bien calculer la valeur exacte de $p_i$ en comptant le nombre de tableaux où ces conditions sont vérifiées. Ce sont exactement les tableaux où :

- le $i+1$ ème élément n'est pas le plus grand
- les $i$ premiers éléments sont triées

Pour des tableaux de longueur $i$ il n'y a que $i$ tableaux possibles sur les $(i+1)!$ possibles pour une probabilité de $\frac{i}{(i+1)!}$. Le raisonnement est identique si on ne considère que les $i+1$ premiers éléments de tout tableau et donc $p_i = \frac{i}{(i+1)!}$ pour tout tableau de longueur $n\geq i+1$. On obtient alors :

<div>
$$
\begin{array}{lcl}
C_\text{moy}(n) &=& \sum_{i=1}^n(p_i \cdot (i \cdot \mathcal{O}(1)))\\
 &=& \sum_{i=1}^{n-1}(\frac{i}{(i+1)!} \cdot \mathcal{O}(i)) \\
 &=& \mathcal{O}(\sum_{i=1}^{n-1}(\frac{i^2}{(i+1)!}))
\end{array}
$$
</div>

Comme $i^4 \leq (i+1)!$ pour $i \geq 5$ on a que :

<div>
$$
C_\text{moy}(n) \leq \mathcal{O}(\sum_{i=1}^{n}(\frac{1}{i^2}))
$$
</div>

La série $\sum_{i=1}^{n}\frac{1}{i^2}$ est appelée [Problème de Bâle](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_B%C3%A2le) et est une série convergente ([on le démontrera](../../projet-sommes-classiques/#problème-Bâle){.interne}) et on retombe bien sur le même résultat.

#### Vérification

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


## Complexité du problème de la reconnaissance

Comme toute case du tableau peut rendre le tableau non trié, on utilise l'argument de [la complexité du problème de la _"recherche"_](../../complexité-problème/#complexité-recherche){.interne}, un algorithme résolvant ce problème doit considérer toutes les cases du tableau et donc une borne min du problème _"est trié ?"_ est $\Omega(n)$ où $n$ est la taille du tableau en entrée. Comme la complexité de `est_trie`{.language-} est de $\mathcal{O}(n)$. On en conclut :

{% note "**Proposition**" %}
La complexité du problème _"est trié ?"_ est de $\Theta(n)$ où $n$ est la taille du tableau en entrée.
{% endnote %}


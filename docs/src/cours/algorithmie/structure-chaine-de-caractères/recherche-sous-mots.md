---
layout: layout/post.njk
title: "Recherche de sous chaines"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD rabin karp avec dictionnaire
> TBD horspool en exercice : cf ET 21/22 à mettre en exercice
> Mettre le knuth morris pratt en "pour aller plus loin" complexité linéaire dans le cas le pire.


Nous allons dans cette partie analyser le problème de la _recherche d'une sous-chaîne_ :

{% note "**Problème de la recherche d'une sous-chaîne**" %}
- **Données** :
  - une chaîne de caractère de $a$ de longueur $n$
  - une chaîne de caractère de $b$ de longueur $m$, avec $m \leq n$
- **question** : $b$ est-il une _sous-chaîne_ de $a$ ?
- **réponse** : l'indice d'un début de $b$ dans $a$ si $b$ est une sous chaine de $a$ et $-1$ sinon
{% endnote %}

Une définition formelle de _sous-chaîne_ étant :

{% note "**Définition**" %}
Soient $a$ et $b$ deux chaines de caractères de longueurs $n$ et $m <n$ respectivement.

La chaîne $b$ est une **sous-chaîne** de $a$ s'il existe $0 \leq i < n$ tel que l'on ait pour tout $0 \leq j < m$ :

$$
b[j] = a[i + j]
$$

{% endnote %}

## Algorithme naïf

La première idée pour résoudre le problème de _la recherche d'une sous-chaîne_ est de vérifier pour pour tout $0 \leq i < n$ si la définition est correcte :

```python#
def sous_chaine_naif(a, b):
    for i in range(len(a) - len(b) + 1):
        trouvé = True
        for j in range(len(b)):
            if b[j] != a[i + j]:
                trouvé = False
        if trouvé:
            return True
    return False
```

### Pièges

L'algorithme semble une application directe de la définition, et pourtant... Attention aux multiples pièges de ce genre d'algorithme. Il faut **toujours** vérifier très consciencieusement :

- les limites de boucles
- les conditions d'arrêt

Essayez de comprendre pourquoi les solutions suivantes ne fonctionnent pas en exhibant un contre-exemple.

#### Limites de boucles

Attention aux limites des boucles `for`{.language-} ! Il faut **toujours** vérifier les bornes.

{% exercice %}

Le programme suivant contient une erreur, laquelle ?

```python
def sous_chaine_naif_FAUX_1(a, b):
    for i in range(len(a)):
        trouvé = True
        for j in range(len(b)):
            if b[j] != a[i + j]:
                trouvé = False
        if trouvé:
            return True
    return False
```

{% endexercice %}
{% details "corrigé" %}
Pas de sentinelle sur le positionnement. On peut avoir $i + j \geq m$ et donc `a[i + j]`{.language-} provoquer une erreur. Par exemple `sous_chaine_naif("aaa", "ca")`{.language-}
{% enddetails %}

Allez, une autre :

{% exercice %}

Le programme suivant contient une erreur, laquelle ?

```python
def sous_chaine_naif_FAUX_2(a, b):
    for i in range(len(a) - len(b)):
        trouvé = True
        for j in range(len(b)):
            if b[j] != a[i + j]:
                trouvé = False
        if trouvé:
            return True
    return False
```
{% endexercice %}
{% details "corrigé" %}
On ne va pas assez loin. Par exemple `sous_chaine_naif("ab", "b")`{.language-}

{% enddetails %}

#### Conditions d'arrêt

Une erreur classique :

{% exercice %}

Le programme suivant contient une erreur, laquelle ?

```python
def sous_chaine_naif_FAUX_3(a, b):
    for i in range(len(a) - len(b) + 1):
        for j in range(len(b)):
            if b[j] != a[i + j]:
                return False
    return True
```
{% endexercice %}
{% details "corrigé" %}
Ce n'est pas parce que l'on ne trouve pas la sous-chaine en $i=$ que ce n'est pas vrai pour $i=1$...

Exemple : `sous_chaine_naif("ab", "b")`{.language-}

{% enddetails %}

Une variation sur l'erreur précédente :

{% exercice %}

Le programme suivant contient une erreur, laquelle ?
```python
def sous_chaine_naif_FAUX_4(a, b):
    trouvé = True
    for i in range(len(a) - len(b) + 1):
        for j in range(len(b)):
            if b[j] != a[i + j]:
                trouvé = False
    return trouvé
```
{% endexercice %}
{% details "corrigé" %}

Erreur inverse du cas précédent. Il suffit que l'on ne trouve pas le sous-mot à une position pour que l'algorithme réponde faux : `sous_chaine_naif("ba", "b")`{.language-}.

{% enddetails %}

### Complexité

#### Complexité maximale

Calculons la complexité ligne à ligne :

1. définition d'un fonction : $\mathcal{O}(1)$ opérations
2. boucle de $\mathcal{O}(n - m)$ itérations.
3. affectation : $\mathcal{O}(1)$ opérations
4. boucle de $\mathcal{O}(m)$ itérations.
5. positionnement dans 2 tableaux et test : $\mathcal{O}(1)$ opérations
6. affectation : $\mathcal{O}(1)$ opérations
7. test : $\mathcal{O}(1)$ opérations
8. retour de fonction : $\mathcal{O}(1)$ opérations
9. retour de fonction : $\mathcal{O}(1)$ opérations

On en conclut que la complexité totale se niche dans l'exécution des deux boucles `for`{.language-} imbriquées, et est donc de complexité : $\mathcal{O}((n - m) \cdot m) = \mathcal{O}(nm + m^2) \sim \mathcal{O}(n\cdot m)$ si $n \gg m$ ce qui est généralement le cas.

#### Complexité minimale

La complexité minimale est atteinte lorsque la sous-chaine est trouvée dès $i=0$. Dans ce cas là, il aura fallu $\mathcal{O}(m)$ opérations.

#### Complexité en moyenne

On pourrait envisager deux calculs possibles :

- complexité en moyenne lorsque $b$ est une sous-chaine de $a$
- complexité en moyenne lorsque $b$ n'est pas une sous-chaine de $a$

Le premier cas dépend uniquement de la position de la sous-chaine $b$ dans $a$, pas de la _structure_ de $a$ ou de $b$. Il est donc très dépendant de l'application et il n'y a aucune raison de choisir un modèle purement aléatoire (il y a très peu d'applications où il faut chercher si un mot aléatoire est présent dans une chaine également aléatoire)

Le second cas est le cas le pire et à un nombre constant d'opérations : $\mathcal{O}(nm)$.

#### Attention

Attention ! L'algorithme suivant, qui utilise la comparaison de listes en python, n'est **pas** de complexité inférieure.

```python
def sous_chaine_naif_2(a, b):
    for i in range(len(a) - len(b) + 1):
        if b == a[i : i + len(b) + 1]:
            return True
    return False
```

En effet, la complexité de l'égalité entre deux liste est égale à la taille de la plus petite des listes.

### Une amélioration subtile

La boucle en $j$ (lignes 4-6) de l'algorithme `sous_chaine_naif`{.language-} pourrait être améliorée en l'arrêtant dès que `trouvé`{.language-} est mis à `False`.

On peut pour cela utiliser l'instruction `break`{.language-} qui permet de sortir de la boucle la plus imbriquée (ici la boucle for en $j$ de la ligne 4). Lisez la [documentation](https://docs.python.org/fr/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) à ce sujet, elle est éclairante.

On a alors l'algorithme suivant :

```python
def sous_chaine_naif_amélioré(a, b):
    for i in range(len(a) - len(b) + 1):
        trouvé = True
        for j in range(len(b)):
            if b[j] != a[i + j]:
                trouvé = False
                break
        if trouvé:
            return True
    return False
```

Dès le premier élément qui ne correspond pas, on sort de la boucle for. Cela peut sembler une amélioration de bout de chandelles car cela ne change pas la complexité maximale de l'algorithme. Mais on le verra, cela va changer la complexité en moyenne lorsque $b$ n'est pas une sous-chaine de $a$.

#### `break`{.language-}, `continue`{.language-} et `while`{.language-}

L'instruction `break`{.language-} de l'algorithme `sous_chaine_naif_amélioré`{.language-} aurait très bien pu s'écrire avec une boucle `while`{.language-} :

```python
def sous_chaine_naif_amélioré_sans_break(a, b):
    for i in range(len(a) - len(b) + 1):
        trouvé = True
        j = 0
        while j < len(b):
            if b[j] != a[i + j]:
                trouvé = False
                j = len(b)
            else:
                j += 1
        if trouvé:
            return True
    return False
```

**Mais** la lecture aurait été moins aisée. L'utilisation de l'instruction `break` permet :

- d'expliciter le cas général (la boucle for)
- le cas particulier : le `break`{.language-}.

Le pendant de l'instruction `break`{.language-} est l'instruction `continue`{.language-} qui permet d'aller à la prochaine itération de la boucle la plus imbriquée.

Comparez par exemple ces 2 implémentations d'un même algorithme dont le but est à partir d'une liste d'entiers $L$ de faire un traitement uniquement si l'élément est non nul.

Sans utilisation de `continue`{.language-}, le cas général est traité dans un bloc `if`{.language-} :

```python
for element in L:
    if element != 0:
        # ...
```

Utilisation de `continue`{.language-}, le cas particulier est évacué directement.

```python
for element in L:
    if element == 0:
        continue

    # ...
```

Le second cas est bien plus clair.

{% note "**Bonne pratique algorithmique**" %}
L'utilisation de `break` et de `continue` permet de distinguer clairement dan l'algorithme ce qui est de l'ordre du cas général (la boucle) et du cas particulier (sortie de boucle)
{% endnote %}

#### Calcul de la complexité en moyenne

On suppose que l'on ait dans le cas où $b$ n'est pas une sous-chaine de $a$. Pour ce calcul on va se placer dans le cas fictif où chaque lettre est équiprobable. La probabilité que deux lettres soient égales est alors $p = \frac{1}{A}$ où $A$ est la taille de l'alphabet utilisé. C'est le cas le plus défavorable pour notre calcul.

A $i$ fixé, on a alors :

1. la probabilité que $b[0] \neq a[i]$ vaut $1-p$
2. la probabilité que $b[0] = a[i]$ et $b[1] \neq a[i + 1]$ vaut $p\cdot (1-p)$
3. la probabilité que $b[j] = a[i + j]$ pour $0\leq j < 2$ et $b[1] \neq a[i + 2]$ vaut $p^2\cdot (1-p)$
4. ...
5. la probabilité que $b[j] = a[i + j]$ pour $0 \leq j < k$ et $b[k] \neq a[i + k]$ vaut $p^k\cdot (1-p)$
6. ...
7. la probabilité que $b[j] = a[i + j]$ pour $0\leq j < m - 1$ et $b[m-1] \neq a[i + m - 1]$ vaut $p^{m-1}\cdot (1-p)$

Cette probabilité devient vite très faible. Par exemple, si on a un alphabet à 2 caractères (0 et 1), la probabilité de s'arrêter au bout de 10 itérations vaut : $(\frac{1}{2})^10 = 0.1\%$.

De là, la probabilité que l'on s'arrête après :

- 1 itérations de la boucle `for`{.language-} en $j$ est égale à $(1-p)$
- 2 itérations de la boucle `for`{.language-} en $j$ est égale à $p(1-p)$
- ...
- $j$ itérations de la boucle `for`{.language-} en $j$ est égale à $p^{j-1}(1-p)$
- ...
- $m$ itérations de la boucle `for`{.language-} en $j$ est égale à $p^{m-1}(1-p)$

Le nombre moyens d'itérations de la boucle `for`{.language-} en $j$ est alors :

$$
1\cdot (1-p) + 2 \cdot p(1-p) + 3 \cdot p^2(1-p) + ... + m \cdot p^{m-1}(1-p) = \frac{1-p}{p}\sum_{k=1}^{m}k\cdot p^k
$$

Et comme chaque itération se fait en $\mathcal{O}(1)$ opérations, La complexité en moyenne du passage dans la boucle `for`{.language-} en $j$ vaut :

$$
\mathcal{O}(1) \cdot \frac{1-p}{p}\sum_{k=1}^{m}k\cdot p^k = \mathcal{O}(\frac{1-p}{p}\sum_{k=1}^{m}k\cdot p^k) = \mathcal{O}(\sum_{k=1}^{m}k\cdot p^k)
$$

Comme :

$$
\sum_{k=1}^mk\cdot p^k = \frac{p}{(p-1)^2}\cdot(mp^{m+1}-(m+1)p^m + 1)
$$

{% details "preuve" %}

Si l'on note $f_m(x) = \sum_{k=1}^mx^k$, on a : $\sum_{k=1}^mk\cdotp^k = p\cdot f'_m(p)$. De là, une récurrence immédiate montre que $f_m(x) = \frac{x^{m+1} - 1}{x-1}$. Ainsi :

$$
\sum_{k=1}^mk\cdot p^k = p \frac{(m+1)p^m(p-1)-(p^{m+1}-1)}{(p-1)^2} = \frac{p}{(p-1)^2}\cdot(mp^{m+1}-(m+1)p^m + 1)
$$

{% enddetails %}

Comme $p < 1$, on a que :

$$
\lim_{m \rightarrow +\infty} \frac{p}{(p-1)^2}\cdot(mp^{m+1}-(m+1)p^m + 1) = \frac{p}{(p-1)^2}
$$

Et donc, pour tout $m$ :

$$
\sum_{k=1}^mk\cdot p^k \leq \frac{p}{(p-1)^2}
$$

Donc :

$$
\mathcal{O}(\sum_{k=1}^{m}k\cdot p^k) = \mathcal{O}(\frac{p}{(p-1)^2}) = \mathcal{O}(1)
$$

Le nombre moyen d'itérations de la boucle for en $j$ est donc toujours plus petit qu'une constante : c'est indépendant de $m$ et ne dépend que de $p$ !

Ceci s'explique par le fait que la probabilité de s'arrêter au bout de $j$ itération devient très vite très petite, et d'autant plus petite que l'alphabet augmente. On s'arrêtera quasi toujours avant d'arriver à la fin de $b$.

Ce résultat surprennent amène à un autre résultat tout aussi surprenant : comme le reste de l'algorithme est de complexité $\mathcal{O}(n)$ :

{% note %}
La complexité en moyenne de l'algorithme naif est $\mathcal{O}(n)$.
{% endnote %}

Un simple `break`{.language-} a rendu linéaire la complexité en moyenne de l'algorithme.

### Trouver toutes les sous-chaines

Si l'on cherche à trouver tous les indices où se trouvent $b$ dans $a$, il faut modifier l'algorithme pour stocker les indices où $b$ commence. Ceci se fait aisément :

```python
def sous_chaine_naif_tous(a, b):
    indices = []
    for i in range(len(a) - len(b) + 1):
        trouvé = True
        for j in range(len(b)):
            if b[j] != a[i + j]:
                trouvé = False
                break
        if trouvé:
            indices.append(i)
    return indices
```

{% exercice %}
Donnez les complexités de ce nouvel algorithme.
{% endexercice %}
{% details "solution" %}

Les complexités maximale et en moyenne de l'algorithme n'ont pas changé. Seule la complexité minimale est passé de $\mathcal{O}(m)$ à $\mathcal{O}(n)$ puisque l'on parcours toute la chaine à chaque fois.

{% enddetails %}

## Améliorations

it autour de la boucle `for`{.language-} en `i`{.language-} qui teste si $b$ est présent à partir de chaque position de $a$. A chaque étape on compare un élément de $b$ à l'élément de l'index $i + j$ de $a$. Le principal soucis de l'algorithme est que le nombre $i+j$ peut diminuer.

Par exemple si on cherche la chaine `b=CGT`{.language-} dans la chaine `a=CGACGACGACGA`{.language-} $i+j$ vaudra :

1. $i+j=0+0 = 0$
2. $i+j=0+1 = 1$
3. $i+j=0+2 = 2$
4. $i+j=1+0 = 1$
5. $i+j=1+1 = 2$
6. $i+j=1+2 = 3$
7. $i+j=2+0 = 2$
8. ...

Chaque élément de $a$ sera vu $m$ fois.

Accélérer l'algorithme revient à faire en sorte que le nombre $i+j$ soit croissant le plus souvent possible.

### Prétraitement utilisant $a$

Une première idée que l'on peut avoir pour accélérer le processus et de remarquer que ça ne sert à rien de faire commencer la recherche de $b$ dans $a$ à l'index $i$ si $a[i] \neq b[0]$.

Ceci peut se faire en $\mathcal{O}(n)$ opérations en utilisant `sous_chaine_naif_tous(a, b[0])`{.language-}. On utilise ensuite ces indices dans notre algorithme accéléré :

```python
def sous_chaine_naif_acceleration_1(a, b):
    for i in sous_chaine_naif_tous(a, b[0]):
        trouvé = True
        for j in range(len(b)):
            if b[j] != a[i + j]:
                trouvé = False
        if trouvé:
            return True
    return False
```

Il faut maintenant tenir compte du prétraitement dans le calcul de la complexité.

- ce qu'on fait en plus : on parcourt toute la chaine $a$ pour rendre le tableau d'indices. Cela se fait en $\mathcal{O}(n)$ opérations
- ce qu'on fait en moins : on ne parcourt plus que certains indices $i$ et pas tous.

Mais au final, on ne gagne rien... En effet le temps gagné pour ne parcourir que certains indices est compensé par le fait qu'il faut les trouver.
L'algorithme naïf ne prend pas plus de temps que notre optimisation car si $a[i] \neq b[0]$ on passe tout de suite à l'indice suivant.

Si on veut augmenter la rapidité de l'algorithme, il faut travailler sur $b$ pour optimiser les décalages.

### Prétraitement sur $b$

Notre objectif est toujours de rendre la somme $i+j$ la plus croissante possible pour éviter les répétitions. Comment adapter l'idée précédente en ne travaillant que sur $b$ ?

Pour comprendre, regardons tous les cas possibles avec notre algorithme naïf :

On débute une recherche en comparant $a[i + 0]$ à $b[0] :

```text
             i
a:     ...aaa?aaaaaaaa....
b:           bbbbbb
             j
```

Si $a[i] = b[0]$ alors on décale $j$ d'un cran :

```text
             i
a:     ...aaab?aaaaaaa....
b:           bbbbbb
              j
```

Sinon, on a pas vraiment d'autre choix que de décaler i de 1 :

```text
              i
a:     ...aaaa?aaaaaaa....
b:            bbbbbb
              j
```

Il n'y a pas vraiment de moyen de gagner des opérations dans ce cas là.

Supposons maintenant que l'on ait un peu avancé :

```text
             i
a:     ...aaabbb?aaaaa....
b:           bbbbbb
                j
```

On a $a[i + k] = b[k]$ pour tout $0 \leq k < j$. Et on compare $a[i + j]$ à $b[j]$.

Si $a[i + j] = b[j]$ alors on décale $j$ d'un cran et on recommence si $j < m$ et sinon on s'arrête puisque l'on a trouvé $b$ dans $a$. Mais si $a[i + j] \neq b[j]$ on replace $j$ à 0 et on augmente $i$. Cette augmentation peut être de 1 à $j$ :

- augmentation de 1 (comme pour le l'algorithme naïf)

  ```text
               i
  a:     ...aaabbb?aaaaa....
  b:            bbbbbb
                j
  ```

- augmentation max :

  ```text
                  i
  a:     ...aaabbb?aaaaa....
  b:              bbbbbb
                  j
  ```

- augmentation entre les deux :

  ```text
                 i
  a:     ...aaabbb?aaaaa....
  b:             bbbbbb
                 j
  ```

En réutilisant la partie précédente, on a clairement que l'augmentation minimale de $i$ que l'on peut avoir est :

- $i=i+j$ s'il n'existe pas $0 < k < j$ tel que $a[i+k] = b[j]$
- $i=i+k$ avec $0 < k \leq j$ le plus petit entier tel que $a[i+k] = b[0]$, sinon

Comme on sait que $a[i:i+j]$ vaut $b[:j]$ on peut précalculer ces déplacements !

On commence par chercher le premier endroit où $b[0]$ est répété dans $b$. On peut utiliser `sous_chaine_naif_tous(b, b[0])` et prendre, s'il existe, le deuxième élément de la sortie, disons $p$. Si cet élément n'existe pas, on note $p=m$

Ensuite, si :

- $a[i + k] = b[k]$ pour tout $0 \leq k < j$
- $a[i + j] \neq b[j]$

On peut déplacer $i$ de :

- 1 si $j=0$
- $p$ si $p < j$
- $j$ sinon

Pour préparer la suite, on va ranger ces informations dans un tableau $T_b$ de longueur $m-1$ tel que :

- $T_b[j-1] = 0$ pour tout $1 \leq j \leq p$
- $T_b[j-1] = j - p$ pour tout $p < j \leq m-1$

Par exemple, pour $b=ACATGA$, on aurait : $T_b = [0, 0, 1, 2, 3]$

Avec ce tableau, notre algorithme devient alors :

```python
def sous_chaine_naif_acceleration_2(a, b):
    T_b = creation_tableau_opti_1(b)

    i = 0
    j = 0

    while i + j < len(a):
        if a[i + j] == b[j]:
            j += 1

            if j >= len(b):
                return True

        else:
            if j == 0:
                i += 1
            else :
                i = i + j - T_b[j - 1]
                j = 0
    return False
```

On a donc 2 décalages possibles :

- soit on déplace $i$ sur $j$ (on est avant le nouveau début)
- soit on déplace i pour que a[i] soit un début de b (lorsque l'on a $j \geq p$ et que que l'on connaît le début de $a$)

Plus il y a de 0 dans $T_b$ plus les décalages seront importants

Cependant, la forme de $T_b$ sera toujours $[0, 0, ..., 0, 1, 2, ..., k]$. On gagne de l'optimisation puisque l'on avance toujours du maximum possible jusqu'à la 1ère répétition.

### Amélioration de l'amélioration

L'amélioration précédente permet d'avancer $i$ jusqu'au second départ de $b$ — le premier indice $p > 0$ tel que $b[0] = b[p]$ — si $j > p$. Plaçons nous dans ce cas là :

```text
            i
a:     .....abbbaa?aaa....
b:          bbbbbbbb
                p j
```

On a :

- $p>0$ le premier indice tel que $b[0] = b[p]$
- $a[i + k] = b[k]$ pour tout $0 \leq k < j$
- $p < j$
- $a[i + j] \neq b[j]$

On sait donc aussi que $a[i + p] = b[0]$.

L'amélioration précédente revient à poser :

- $i' = i + p$
- $j' = 0$

On se retrouve alors dans ce cas là :

```text
            i
                i'
a:     .....abbbaa?aaa....
b:              bbbbbbbb
                j'
                  j
```

Avec :

- $a[i'] = b[0] = b[p]$
- $a[i' + k] = b[p + k]$ pour tout $k < j-p$

On a alors deux choix :

- soit $b[k] = b[p + k]$ pour tout $k < j-p$ et on peut poser $j' = i + j - p$ (on remet j' au niveau du ?)
- soit ce n'est pas le cas et ça ne sert à rien de regarder si $b$ commence en $i'$ parce que ce n'est pas possible

Remarquez que ceci peut se faire sans $a$. Ceci nous donne une nouvelle possibilité d'amélioration :

{% note %}
Si :

- $j > 0$
- $a[i + k] = b[k]$ pour tout $0 \leq k < j$
- $a[i + j] \neq b[j]$

Soit $k'$ le plus petit entier tel que $b[:k'] == b[j-k':j]$ (au pire $k'=0$).
Alors en notant :

- $i' = i + j - k$
- $j' = k$

On a que :

- $i'$ est le prochain indice de $a$ où $b$ peut être une sous-chaine de $a$
- $a[i' + l] = b[l]$ pour tout $0 \leq l < j'$

On a de plus l'égalité : $i + j = i' + j'$
{% endnote %}

Remplir le Tableau $T_b$ avec les valeurs de $k'$ pour tout $j$ nous donne un moyen encore pus efficace de décalage puisque l'on va décaler $i$ **et** $j$ de sorte que la somme $i+j$ soit croissante.

C'est cette procédure que met (optimalement) en œuvre l'algorithme de Knuth, Morris et Pratt.

## Algorithme de Knuth-Morris-Pratt

L'algorithme de [Knuth, Morris et Pratt](https://fr.wikipedia.org/wiki/Algorithme_de_Knuth-Morris-Pratt) publié en 1977, reprend l'idée de l'optimisation précédente mais la sublime. Il trouve un tableau $T_b$ optimal permettant de trouver un algorithme en $\mathcal{O}(n +m)$, c'est à dire de façon optimale.

Nous allons procéder par étape pour essayer de le comprendre.

### Décalage adapté

L'idée force de l'algorithme est que les éléments $T_b[j]$ ne sont plus la distance à la première répétition du premier caractère, mais compte le nombre de caractères dont la fin de $b[:j+1]$ sont un début de $b$ différent de $b[:j+1]$.

Ce tableau permet également d'avancer $i$ plus que l'algorithme naïf. Avant de formaliser tout ça regardons ce que ça donne sur un exemple :

```text
0123456789    : index
ACGAGACGACT   : la chaîne b
   A          : une répétition de 1 caractères
     ACGA     : une répétition de 4 caractères
        AC    : une répétition de 2 caractères
```

Le tableau $T_b$ vaudra alors : $[0, 0, 0, 1, 0, 1, 2, 3, 4, 2]$.

0. $j=0$ par convention on note $T_b[0] = 0$
1. $j=1$. On a `b[:2] = "AC"`. La fin ne correspond à aucun début de $b$ à part $b[:2]$ : $T[1] = 0$
2. $j=2$. On a `b[:3] = "ACG"`. La fin ne correspond à aucun début de $b$ à part $b[:3]$: $T[2] = 0$
3. $j=3$. On a `b[:4] = "ACGA"`. La fin correspond à `b[:1] = "A"` : $T[3] = 1$
4. $j=4$. On a `b[:5] = "ACGAG"`. La fin ne correspond à aucun début de $b$ à par $b[:5]$ : $T[4] = 0$
5. $j=5$. On a `b[:6] = "ACGAGA"`. La fin correspond à `b[:1] = "A"` : : $T[5] = 1$
6. $j=6$. On a `b[:7] = "ACGAGAC"`. La fin correspond à `b[:2] = "AC"` : $T[6] = 2$
7. $j=7$. On a `b[:8] = "ACGAGACG"`. La fin correspond à `b[:3] = "ACG"` : $T[7] = 3$
8. $j=8$. On a `b[:9] = "ACGAGACGA"`. La fin correspond à `b[:4] = "ACGA"` : $T[8] = 4$
9. $j=9$. On a `b[:10] = "ACGAGACGAC"`. La fin correspond à `b[:1] = "AC"` : $T[9] = 2$

Formalisons ça.

{% note %}
Soit $T_b$ un tableau de longueur $m-1$

- T_b[0] = 0
- pour tout $1 \leq j < m-1$, on note $T_b[j]$ le plus grand entier $k < j +1$ tel que $b[:k] = b[j+1-k:j+1]$.

{% endnote %}

On peut noter que $T_b[j]$ existe toujours puisque $b[:0]$ et $b[k:k]$ sont la chaine vide pour tout $k$.

On peut facilement calculer $T_b$, par exemple avec cet algorithme :

```python
def algo_naif_construction_t(b):
    T_b = []

    for j in range(1, len(b)):
        T_b.append(0)
        chaîne = b[1:j]
        for k in range(len(chaîne)):
            if b[:k] == chaîne[-k:]:
                T_b[-1] = k

    return T_b
```

La complexité de cet algorithme est cependant assez grande, puisqu'elle est en $\mathcal{O}(m^3)$.

### Algorithme

Avec le tableau $T_b$ défini comme précédemment, on a un gain monumental par rapport à l'optimisation précédente. On a plus besoin de revenir en arrière : on peut faire augmenter (au sens large) $i+j$ à chaque étape.

Prenons un cas concret. Supposons que l'on se trouve dans cette configuration :

```text
i + j :         v
a:       ....ATATGACT....
b:           ATATCG
i/j:         i  j
```

Comme les caractères $a[i +j]$ et $b[j]$ coïncident, l'étape suivante consistera à augmenter $j$ pour continuer la vérification :

```text
i + j :          v
a:       ....ATATGACT....
b:           ATATCG
i/j:         i   j
```

Le nombre $i+j$ aura augmenté strictement.

Si en revanche, la comparaison échoue, par exemple dans ce cas là :

```text
i + j :          v
a:       ....ATATGACT....
b:           ATATCG
i/j:         i   j
```

On peut continuer la comparaison à la même position, mais en décalant $i$ de $T_b[j-1] = T_b[3] = 2$ :

```text
i + j :          v
a:       ....ATATGACT....
b:             ATATCG
i/j:           i j
```

Le nombre $i+j$ n'augmentera pas, mais $i$ aura augmenté strictement.

En supposant que la fonction `cree_tableau(b)` crée $T_b$, l'algorithme de recherche d'une sous-chaine de Knuth, Morris et Pratt est alors :

```python
def sous_chaine_KMP(a, b):
    Tb = cree_tableau(b)

    i = 0
    j = 0

    while i + j < len(a):
        if a[i + j] == b[j]:
            j += 1

            if j >= len(b):
                return True

        else:
            if j == 0:
                i += 1
            else :
                l = j - Tb[j - 1]
                i += l
                j -= l
    return False
```

{% info %}
Par rapport à l'algorithme précédent, $T_b$ est différent et la mise à jour de $j$ n'est plus forcément égale à 0.
{% endinfo %}

Comme à chaque itération, soit $i+j$ croit strictement, soit $i$ croit strictement il y a au plus $2n$ étapes à l'algorithme et donc sa complexité est de l'ordre $\mathcal{O}(n + K(m))$ où $K(m)$ est la complexité de la fonction `cree_tableau(b)`

### Création de la table de décalage

L'algorithme naïf de création de la table est en $\mathcal{O}(m^3)$ ce qui n'est pas vraiment optimal. L'algorithme utilisé par Knutt, Morris-et Pratt est de complexité bien meilleure puisqu'il permet de créer le tableau $T_b$ en $\mathcal{O}(m)$ opérations !

Décrivons l'idée. On commence avec un tableau où seul $T_b[0] = 0$ est rempli (pour $j=1$). On considère que $j \geq 2$ et on note $c = b[j-1]$

On cherche $i$ tel que $b[:i]$ coïncide avec la fin de la chaîne $b[1:j-1] + [c]$ : il y a 2 cas à considérer :

1. on peut continuer la chaine commencée avec $j-1$. Ceci se passe si $b[k] = c$ avec $T_b[(j-1)-1] = k$. Dans ce cas là $T_b[j-1] = k + 1$
2. on ne peut pas continuer la chaine commencée avec $j-1$. Ceci se passe si $b[k] \neq c$ avec $T_b[(j-1) -1] = k$. On a alors 2 sous-cas :

   - $k \leq 1$ (et $b[k] \neq c$) : on a $T_b[j-1] = 0$
   - $k > 1$ (et $b[k] \neq c$). Ce problème est équivalent à trouver :

     - le plus grand $k'$ possible tel que début de $b$ qui coïncide avec la fin de $b[1:(j-1)-1]$
     - et tel que $b[k' + 1] = c$

     On a déjà fait une grande partie du travail puisque : $k'$ est aussi le plus grand entier tel que la fin de $b[1:k + 1]$ coincide avec le début de $b$.

     On peut donc poser $j = k + 1$ et continuer l'algorithme.

Cette procédure peut s'écrire très simplement avec l'algorithme suivant :

```python
def cree_tableau(b):
    T_b = [0]

    j = len(T_b) + 1
    c = b[j-1]

    while len(T_b) < len(b) - 1:
        k = T_b[j-2]

        if c == b[k]:
            T_b.append(k + 1)

            j = len(T_b) + 1
            c = b[j-1]
        elif k <= 1:
                T_b.append(0)

                j = len(T_b) + 1
                c = b[j-1]
        else:
            j = k + 1

    return T_b
```

Calculons la complexité de cette algorithme. Elle est proportionnelle au nombre d'étapes puisque toutes les autres opérations sont en $\mathcal{O}(1)$.

À chaque étape :

- soit $k$ reste constant à 0
- soit $k$ augmente de 1
- soit $k$ diminue strictement

Il y a donc au plus autant d'étapes où $k$ diminue que d'étapes où $k$ augmente ou reste constant.

Comme $j$ augmente lorsque $k$ reste constant ou augmente, et que l'on s'arrête lorsque $j$ vaut $m-1$, il y a au plus $m$ étapes où $k$ reste constant ou augmente.

On en déduit qu'il a donc également au plus $m$ étapes où $k$ diminue.

Le nombre total d'étape est en $\mathcal{O(m)}$.

{% note "**Proposition**" %}
La complexité de la création de $T_b$ est en $\mathcal{O(m)}$.

La complexité de l'algorithme de Knuth-Morris-Pratt est en $\mathcal{O}(n +n)$ opérations : elle est minimale.
{% endnote %}

## Autres algorithmes

Nous ne détaillerons pas les autres algorithmes, nous nous contenteront de donner les liens wikipedia et d'indiquer leur intérêt

- [Rabin-Karp](https://fr.wikipedia.org/wiki/Algorithme_de_Rabin-Karp). Cet algorithme est intéressant car :
  - plutôt que de chercher la sous-chaine directement, on passe par une fonction de hashage. On compare donc des valeur de hash plutôt que des sous-chaine ce qui est plus rapide en général
  - la fonction de hashage utilisée (nommée [empreinte de Rabin](https://fr.wikipedia.org/wiki/Algorithme_de_Rabin-Karp#Empreinte_de_Rabin)) est très facilement itérativement calculable.
- [Boyer-Moore-Horspool](https://fr.wikipedia.org/wiki/Algorithme_de_Boyer-Moore-Horspool). Intéressant car on compare de la fin au début et la fonction de saut est plus simple à comprendre que celle de Knuth-Morris-Pratt. En revanche, sa complexité est en $\mathcal{O}(mn)$ et n'a donc que peu d'intérêt à part historique
- [Boyer-Moore](https://fr.wikipedia.org/wiki/Algorithme_de_Boyer-Moore). Algorithme également linéaire. Sa fonction de saut est compliquée à comprendre (presque autant que celle de Knuth-Morris-Pratt). Son intérêt — à part historique — est le calcul de la complexité qui est tout sauf trivial. On la doit à [Knuth, Morris et Pratt (p343-346)](http://static.cs.brown.edu/courses/csci1810/resources/ch2_readings/kmp_strings.pdf) (oui oui, c'est dans le même article où ils présentent leur propre algorithme).


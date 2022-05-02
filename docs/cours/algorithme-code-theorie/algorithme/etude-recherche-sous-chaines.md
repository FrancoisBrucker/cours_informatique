---
layout: page
title:  "étude / recherche de sous-chaines"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [algorithmie]({% link cours/algorithme-code-theorie/algorithme/index.md %}) / [étude : recherche de sous-chaines]({% link cours/algorithme-code-theorie/algorithme/etude-recherche-sous-chaines.md %})
>
> prérequis :
>
> * [complexité en moyenne]({% link cours/algorithme-code-theorie/algorithme/complexite-moyenne.md %})
> * [structure : chaine de caractères]({% link cours/algorithme-code-theorie/algorithme/structure-chaine-de-caracteres.md %})
> * [fonctions de hash]({% link cours/algorithme-code-theorie/theorie/fonctions-hash.md %})
>
{: .chemin}

Nous allons dans cette partie analyser le problème de la *recherche d'une sous-chaîne* :

> **Problème de la recherche d'une sous-chaîne** :
>
> * **Données** :
>   * une chaîne de caractère de $a$ de longueur $n$
>   * une chaîne de caractère de $b$ de longueur $m$, avec $m \leq n$
> * **question** :
>   * $b$ est-il une *sous-chaîne* de $a$ ?
> * **réponse** :
>   * oui ou non.
{: .note}

Une définition formelle de *sous-chaîne* étant :

> Soient $a$ et $b$ deux chaines de caractères de longueurs $n$ et $m <n$ respectivement.
>
> La chaîne $b$ est une **sous-chaîne** de $a$ s'il existe $0 \leq i < n$ tel que l'on ait pour tout $0 \leq j < m$  :
>  
> $$
> b[j] = a[i + j]
> $$
>
{: .note}

## algorithme naïf

La première idée pour résoudre le problème de *la recherche d'une sous-chaîne* est de vérifier pour pour tout $0 \leq i < n$ si la définition est correcte :

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight python linenos %}
def sous_chaine_naif(a, b):
    for i in range(len(a) - len(b) + 1):
        trouvé = True
        for j in range(len(b)):
            if b[j] != a[i + j]:
                trouvé = False
        if trouvé:
            return True
    return False
{% endhighlight %}

### pièges

L'algorithme semble une application directe de la définition, et pourtant... Attention aux multiples pièges de ce genre d'algorithme. Il faut **toujours** vérifier très consciencieusement :

* les limites de boucles
* les conditions d'arrêt

Essayez de comprendre pourquoi les solutions suivantes ne fonctionnent pas en exhibant un contre-exemple.

#### limites de boucles

Attention aux limites des boucles `for` ! Il faut **toujours** vérifier les bornes.

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

{% details quelle est l'erreur ? %}
Pas de sentinelle sur le positionnement. On peut avoir  $i + j \geq m$ et donc `a[i + j]` provoquer une erreur. Par exemple `sous_chaine_naif("aaa", "ca")`

{% enddetails %}

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

{% details quelle est l'erreur ? %}
On ne va pas assez loin. Par exemple `sous_chaine_naif("ab", "b")`

{% enddetails %}

#### conditions d'arrêt

Une erreur classique :

```python
def sous_chaine_naif_FAUX_3(a, b):
    for i in range(len(a) - len(b) + 1):
        for j in range(len(b)):
            if b[j] != a[i + j]:
                return False
    return True
```

{% details quelle est l'erreur ? %}
Ce n'est pas parce que l'on ne trouve pas la sous-chaine en $i=$ que ce n'et pas vrai pour $i=1$...

Exemple : `sous_chaine_naif("ab", "b")`

{% enddetails %}

Une variation sur l'erreur précédente :

```python
def sous_chaine_naif_FAUX_4(a, b):
    trouvé = True
    for i in range(len(a)):
        for j in range(len(b)):
            if b[j] != a[i + j]:
                trouvé = False
    return trouvé
```

{% details quelle est l'erreur ? %}

Erreur inverse du cas précédent. Il suffit que l'on ne trouve pas le sous-mot à une position pour que l'algorithme réponde faux : `sous_chaine_naif("ba", "b")`.

{% enddetails %}

### complexité

#### complexité maximale

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

On en conclut que la complexité totale se niche dans l'exécution des deux boucles `for` imbriquées, et est donc de complexité : $\mathcal{O}((n - m) \cdot m) \simeq \mathcal{O}(n\cdot m)$ si $m \gg n$ ce qui est généralement le cas.

#### complexité minimale

La complexité minimale est atteinte lorsque la sous-chaine est trouvée dès $i=0$. Dans ce cas là, il aura fallu $\mathcal{O}(m)$ opérations.

#### complexité en moyenne

On pourrait envisager deux calculs possible :

* complexité en moyenne $b$ est une sous-chaine de $a$
* complexité en moyenne lorsque $b$ n'est pas une sous-chaine de $a$

Le premier cas dépend uniquement de la position de la sous-chaine $b$ dans $a$, pas de la *structure* de $a$ ou de $b$. Il est donc très dépendant de l'application et il n'y a aucune raison de choisir un modèle purement aléatoire (il  y a très peu d'application où il faut chercher si un mot aléatoire est présent dans une chaine également aléatoire)

Le second cas est le cas le pire et à un nombre constant d'opérations : $\mathcal{O}(nm)$.

#### attention

Attention ! L'algorithme suivant, qui utilise la comparaison de listes en python, n'est **pas** de complexité inférieure.

```python
def sous_chaine_naif_2(a, b):
    for i in range(len(a) - len(b) + 1):
        if b == a[i : i + len(b) + 1]:
            return True
    return False
```

En effet, la complexité de l'égalité entre deux liste est égale à la taille de la plus petite des listes.

### une amélioration subtile

La boucle en $j$ (lignes 4-6) de l'algorithme `sous_chaine_naif` pourrait être améliorée en l'arrêtant dès que `trouvé` est mis à `False`.

On peut pour cela utiliser l'instruction `break` qui permet de sortir de la boucle la plus imbriquée (ici la boucle for en $j$ de la ligne 4). Lisez la [documentation](https://docs.python.org/fr/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) à ce sujet, elle est éclairante.

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

Cela peut sembler une amélioration de bout de chandelles car cela ne change pas la complexité maximale de l'algorithme. Mais... Cela va changer la complexité en moyenne lorsque $b$ n'est pas une sous-chaine de $a$.

#### calcul de la complexité en moyenne

On suppose que l'on ait dans le cas où $b$ n'est pas une sous-chaine de $a$. Pour ce calcul on va se placer dans le cas fictif où chaque lettre est équiprobable. La probabilité que deux lettres soient égales est alors $p = \frac{1}{A}$ où $A$ est la taille de l'alphabet utilisé. C'est le cas le plus défavorable pour notre calcul.

A $i$ fixé, on a alors :

1. la probabilité que $b[0] \neq a[i]$ vaut $1-p$
2. la probabilité que $b[0] = a[i]$ et $b[1] \neq a[i + 1]$ vaut $p\cdot (1-p)$
3. la probabilité que $b[j] = a[i + j]$ pour $0\leq j < 2$ et $b[1] \neq a[i + 2]$ vaut $p^2\cdot (1-p)$
4. ...
5. la probabilité que $b[j] = a[i + j]$ pour $0 \leq j < k$ et $b[k] \neq a[i + k]$ vaut $p^k\cdot (1-p)$
6. ...
7. la probabilité que $b[j] = a[i + j]$ pour $0\leq j < m - 1$ et $b[m-1] \neq a[i + m - 1]$ vaut $p^{m-1}\cdot (1-p)$

Le nombre moyens d'itérations de la boucle `for` en $j$ est alors :

$$
1\cdot (1-p) + 2 \cdot p(1-p) + 3 \cdot p^2(1-p) + ... + m \cdot p^{m-1}(1-p) = \frac{1-p}{p}\sum_{k=1}^{m}k\cdot p^k
$$

Comme $p < 1$ la série $\sum_{k=1}^{m}k\cdot p^k$ est convergente et est toujours inférieure à $\sum_{k=1}^{+\infty}k\cdot p^k$ qui ne dépend plus de $m$.

{% details preuve de la convergence de la série %}

Si l'on note $f_m(x) = \sum_{k=1}^mx^k$, on a : $\sum_{k=1}^mk\cdotp^k = p\cdot f'_m(p)$.

Comme une récurrence immédiate montre que $f_m(x) = \frac{x^{m+1} - 1}{x-1}$, on a :

$$
\sum_{k=1}^mk\cdot p^k = p \frac{(m+1)p^m(p-1)-(p^{m+1}-1)}{(p-1)^2} = \frac{p}{(p-1)^2}\cdot(mp^{m+1}-(m+1)p^m + 1)
$$

comme $p < 1$, $mp^m$ tend vers $0$ lorsque $m$ tend vers $+\infty$ et donc $\sum_{k=1}^mk\cdot p^k$ tend vers $ \frac{p}{(p-1)^2}$ lorsque $m$ tend vers $+\infty$.

On en conclut :

$$
\sum_{k=1}^{+\infty}k\cdot p^k =  \frac{p}{(p-1)^2}
$$

{% enddetails %}

Le nombre moyen d'itérations de la boucle for en $j$ est donc indépendant de $m$ ! Il ne dépend que de $p$. De là, la complexité moyenne de l'algorithme est ainsi $\mathcal{O}(n)$.

Enfin, comme le cas où $$ n'est pas une sous-chaine de $a$ est le cas le plus défavorable, on en conclut que la complexité en moyenne de l'algorithme est de $\mathcal{O}(n)$ opérations.

> Un simple `break` a rendu linéaire la complexité en moyenne de l'algorithme.
{: .note}

#### `break`, `continue` et `while`

L'instruction `break` de l'algorithme `sous_chaine_naif_amélioré` aurait très bien pu s'écrire avec une boucle `while` :

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

* d'expliciter le cas général (la boucle for)
* le cas particulier : le `break`.

Le pendant l'instruction `break` est l'instruction `continue` qui permet d'aller à la prochaine itération de la boucle la plus imbriquée.

Comparez par exemple ces 2 implémentations d'un même algorithme dont le but est à partir d'une liste d'entiers $L$ de faire un traitement uniquement si l'élément est non nul.

Sans utilisation de `continue`, le cas général est traité dans un bloc `if` :

```python
for element in L:
    if element != 0:
        # ...
```

Utilisation de `continue`, le cas particulier est évacué directement.

```python
for element in L:
    if element == 0:
        continue
    
    # ...
```

Le second cas est bien plus clair.

> L'utilisation de `break` et de `continue` permet de distinguer clairement dan l'algorithme ce qui est de l'ordre du cas général (la boucle) et du cas particulier (sortie de boucle)
{: .note}

## Algorithme de Knuth-Morris-Pratt

L'algorithme `sous_chaine_naif_amélioré` est construit autour de la boucle for en `i` qui teste si $b$ est présent à partir de chaque position de $a$. A chaque étape on compare un élément de $b$ à l'élément de l'index $i + j$ de $a$. Le principal soucis de l'algorithme est que le nombre $i+j$ peut diminuer.

Par exemple si on cherche la chaine `aab` dans la chaine `aaaaaaaa` $i+j$ vaudra :

1. $i+j=0+0 = 0$
2. $i+j=0+1 = 1$
3. $i+j=0+2 = 2$
4. $i+j=1+0 = 1$
5. $i+j=1+1 = 2$
6. $i+j=1+2 = 3$
7. $i+j=2+0 = 2$
8. ...

Chaque élément de $a$ sera vu $m$ fois.

L'algorithme de [Knuth, Morris et Pratt](https://fr.wikipedia.org/wiki/Algorithme_de_Knuth-Morris-Pratt) publié en 1977 est une réponse optimale à ce problème. Il permet de trouver une sous-chaine $b$ d'une chaine $a$ en $\mathcal{O}(m + n)$ opérations. Il est basée sur une optimisation du décalage de $i$ et $j$ que permet de rendre la somme $i+j$ croissante (on ne se répète plus).

### décalage adapté

Pour accélérer l'algorithme il faut pouvoir garantir que :

* soit $i+j$ augmente à chaque étape
* soit $i+j$ est constant mais $i$ augmente (ce qui signifie que l'on a décalé la comparaison).

Il faut donc que si on est dans la position suivante à la fin d'une étape :

```text
i + j :         v
a:       ....aaaaaaaaa....
b:           bbbbbb         
i/j:         i  j
```

Alors à l'étape suivante on a :

1. soit :

    ```text
    i + j :          v
    a:       ....aaaaaaaaa....
    b:           bbbbbb         
    i/j:         i   j
    ```

    Qui correspond au fait que l'on continue de chercher si $b$ est une sous-chaine de $a$ à commençant à la position $i$
2. soit :

    ```text
    i + j :         v
    a:       ....aaaaaaaaa....
    b:            bbbbbb         
    i/j:          i j
    ```

    Qui correspond au fait que l'on chercher si $b$ est une sous-chaine de $a$ à commençant à une nouvelle position. Dans ce cas là, on est pas obligé de recommencer à $j=0$ car on connait déjà les premiers caractères de $a$.

Prenons un cas concret. Supposons que l'on se trouve dans cette configuration :

```text
i + j :         v
a:       ....ATATGACT....
b:           ATATCG          
i/j:         i  j
```

Comme les caractères $a[i +j$ et $b[j]$ coincident, l'étape suivante consistera à augmenter $j$ pour continuer la vérification :

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

On peut continuer la comparaison à la même position, mais en décalant $i$ :

```text
i + j :          v
a:       ....ATATGACT....
b:             ATATCG          
i/j:           i j
```

Le nombre $i+j$ n'augmentera pas, mais $i$ aura augmenté strictement.

Le nombre minimum de décalage possible peut être formalisé comme suit :

> Si à la fin d'une étape on a :
>
> * $j > 0$
> * $a[i + k] = b[k]$ pour tout $0 \leq k < j$
> * $a[i + j] \neq b[j]$
>
> Soit $l$ le plus petit entier strictement positif tel que $a[i + l + k] = b[k]$ pour tout $0 \leq k < j - l$.
>
> On peut continuer l'étape suivante avec :
>
> * $i' = i + l$
> * $j' = j - l$
>
{: .note}

On peut noter que $l$ existe toujours, au pire il vaut $j$ et que comme $a[i + l + k] = b[l + k]$, cela revient à chercher $l$ tel que :

* $0 < l \leq j < m$
* $b[l + k] = b[k]$ pour tout $0 \leq k < j - l$

> On a plus besoin de $a$ dans le calcul de $l$ !
{: .note}

On peut donc considérer, pour toute chaine $b$ de longueur $m$ un tableau $T_b$ tel que :

* $T_b$ soit de longueur $m - 1$
* $T_b[j - 1] = j - l$ pour $0 < j < m$, avec $l$ le plus petit entier tel que :
  * $0 < l \leq j < m$
  * $b[l + k] = b[k]$ pour tout $0 \leq k < j - l$

> La valeur $T_b[j-1]$ correspond à la longueur maximale d'un début de $b$ qui correspond à une fin de $b[1:j]$.
{: .note}

Nous donnerons plus tard un moyen efficace de le calculer. Mais si $b$ vaut `ATATCG` on aurait par exemple $T_b = [0, 0, 1, 2, 0]$.

```text
 00120 
ATATCG
  ATATCG
```

### algorithme

En supposant que l'on connaisse un moyen de créer $T_b$, l'algorithme de recherche d'une sous-chaine de Knuth, Morris et Pratt est alors :

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

Comme à chaque itération, soit $i+j$ croit strictement, soit $i$ croit strictement il y a au plus $2n$ étapes à l'algorithme et donc sa complexité est de l'ordre $\mathcal{O}(n + K(m))$ où $K(m)$ est la complexité de la fonction `cree_tableau(b)`

### création de la table de décalage

Créer la table de décalage revient à chercher les répétitions dans la chaîne $b$.

En reprenant la chaine $b$ valant `ACGAGACGACT` on note les répétitions possibles  :

```text
0123456789    : index
ACGAGACGACT   : la chaîne b
   A          : une répétition de 1 caractères
     ACGA     : une répétition de 4 caractères
        AC    : une répétition de 2 caractères
```

On peut maintenant construire le tableau $T_b$ tel que $T_b[j-1]$, $1 \leq j < m$, correspond à la longueur maximale d'un début de $b$ qui correspond à une fin de $b[1:j]$ :

1. $j=1$. On a `b[1:1] = ""`. La fin  ne correspond à aucun début de $b$ : $T[1-1] = 0$
2. $j=2$. On a `b[1:2] = "C"`. La fin ne correspond à aucun début de $b$ : $T[2-1] = 0$
3. $j=3$. On a `b[1:3] = "CG"`. La fin ne correspond à aucun début de $b$ : $T[3-1] = 0$
4. $j=4$. On a `b[1:4] = "CGA"`. La fin correspond à `b[:1] = "A"` : $T[4-1] = 1$
5. $j=5$. On a `b[1:5] = "CGAG"`. La fin ne correspond à aucun début de $b$ : $T[5-1] = 0$
6. $j=6$. On a `b[1:6] = "CGAGA"`. La fin correspond à `b[:1] = "A"` :  : $T[6-1] = 1$
7. $j=7$. On a `b[1:7] = "CGAGAC"`. La fin correspond à `b[:2] = "AC"` : $T[7-1] = 2$
8. $j=8$. On a `b[1:8] = "CGAGACG"`. La fin correspond à `b[:3] = "ACG"` : $T[8-1] = 3$
9. $j=9$. On a `b[1:9] = "CGAGACGA"`. La fin correspond à `b[:4] = "ACGA"` : $T[9-1] = 4$
10. $j=10$. On a `b[1:10] = "CGAGACGAC"`. La fin correspond à `b[:1] = "AC"` : $T[10-1] = 2$

Le tableau $T_b$ vaut : $[0, 0, 0, 1, 0, 1, 2, 3, 4, 2]$.

Ceci nous permet de créer un algorithme naïf pour trouver $T_b$. 
{% details écrivez cet algorithme %}

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

{% enddetails %}

Cependant, sa complexité est de l'ordre de $\mathcal{O}(m^2)$, ce qui est trop...

L'idée géniale de Knuth, Morris et Pratt est d'avoir remarqué que l'on peut construire le tableau de façon itérative et en $\mathcal{O}(m)$ opérations !

On commence avec un tableau où seul $T_b[0] = 0$ est rempli (pour $j=1$), puis on considère que $j=2$. 
On note :

* $T_b[j-1] = k_0$
* $c = b[j-1]$

On cherche $k$ tel que $b[:k_0]$ coincide avec la fin de la chaîne $b[1:j-1] + [c]$ : il y a 2 cas à considérer :

1. on peut continuer la chaine commencée avec $j-1$. Ceci se passe si $b[k] = c$ avec  $T_b[(j-1)-1] = k$. Dans ce cas là $T_b[j-1] = k + 1$
2. on ne peut pas continuer la chaine commencée avec $j-1$. Ceci se passe si $b[k] \neq c$ avec  $T_b[j-2] = k$. On a alors 2 sous-cas :
    * $k \leq 1$ et $b[k] \neq c$ : on a $T_b[j-1] = 0$
    * $k > 1$ et $b[k] \neq c$. Ce problème est équivalent à trouver :
        * le plus grand $k'$ possible tel que début de $b$ qui coïncide avec la fin de $b[1:j-2]$
        * et tel que $b[k' + 1] = c$

        On a déjà fait une grande partie du travail puisque : $k'$ est aussi le plus grand entier tel que la fin de $b[1:k + 1]$ coincide avec le début de $b$ et tel que $b[k' + 1] = c$
        
        Ceci revient a faire une récurrence en posant : j = k + 1 (c'est le cas $j=10$ de l'exemple)
        

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

La complexité de cette fonction est en $\mathcal{O(m)}$ car à chaque étape :

* soit $k$ augmente de 1
* soit $k$ diminue strictement
* soit $k$ reste constant à 0

Il y a au plus $m$ étapes où $k$ reste constant ou augmente donc au plus $m$ étapes où $k$ diminue.

## Autre algorithmes

Nous dne détaillerons pas les autres algorithmes, nous nous contenteront de donner les liens wikipedia et d'indiquer leur intérêt

* [Rabin-Karp](https://fr.wikipedia.org/wiki/Algorithme_de_Rabin-Karp). Cet algorithme est intéressant car :
    * plutôt que de chercher la sous-chaine directement, on passe par une fonction de hashage. On compare donc des valeur de hash plutôt que des sous-chaine ce qui est plus rapide en général
    * la fonction de hashage utilisée (nommée [empreinte de Rabin](https://fr.wikipedia.org/wiki/Algorithme_de_Rabin-Karp#Empreinte_de_Rabin)) est très facilement itérativement calculable. 
* [Boyer-Moore-Horspool](https://fr.wikipedia.org/wiki/Algorithme_de_Boyer-Moore-Horspool). Intéressant car on compare de la fin au début et la fonction de saut est plus simple à comprendre que celle de Knuth-Morris-Pratt. En revanche, sa complexité est en $\mathcal{O}(mn)$ et n'a donc que peu d'intérêt à part historique
* [Boyer-Moore](https://fr.wikipedia.org/wiki/Algorithme_de_Boyer-Moore). Algorithme également linéaire. Sa fonction de saut est compliquée à comprendre (presque autant que celle de Knuth-Morris-Paratt). Son intérêt — à part historique — est le calcul de la complexité qui est tout sauf trivial. On la doit à [Knuth, Morris et Pratt (p343-346)](http://static.cs.brown.edu/courses/csci1810/resources/ch2_readings/kmp_strings.pdf) (oui oui, c'est dans le même article où ils présentent leurs propre algorithme).

## vers les expressions régulières

La recherche de sous-chaine n'est presque jamais utilisée en tant que tel en informatique car il faut trouver l'expression exacte :

* on ne cherche pas les formes proches (ce qui est possible en utilisant l'alignement de séquences)
* on ne cherche pas de motifs (on appelle celà des [expression régulières](https://fr.wikipedia.org/wiki/Expression_r%C3%A9guli%C3%A8re))

Les expressions régulières dépassent de loin le cadre de ce cours mais c'est un sujet à la fois marrant, utile et intéressant. Si vous voulez vous initier en douceur, liser [le tuto python](https://docs.python.org/fr/3/howto/regex.html) qui y est consacré, ou passez directement à [O'reilly](https://www.oreilly.com/library/view/introducing-regular-expressions/9781449338879/).

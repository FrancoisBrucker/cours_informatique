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
> * [fonctions]({% link cours/algorithme-code-theorie/theorie/fonctions.md %})
>
{: .chemin}

Nous allons dans cette partie analyser le problème de la *recherche d'une sous-chaine* :

> **Problème de la recherche d'une sous-chaîne** :
>
> * **Données** :
>   * une chaine de caractère de $a$ de longueur $n$
>   * une chaine de caractère de $b$ de longueur $m$, avec $m \leq n$
> * **question** :
>   * $b$ est-il une *sous-chaine* de $a$ ?
> * **réponse** :
>   * oui ou non.
{: .note}

Une définition formelle de *sous-chaine* étant :

> Soient $a$ et $b$ deux chaines de caractères de longueurs $n$ et $m <n$ respectivement.
>
> La chaine $b$ est une **sous-chaine** de $a$ s'il existe $0 \leq i < n$ tel que l'on ait pour tout $0 \leq j < m$  :
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

#### break: continue et while

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

L'algorithme `sous_chaine_naif_amélioré` est construit autour de la boucle for en `i` qui teste si $b$ est présent à chaque position de $a$.

Ceci n'est pas optimal dans de nombreux cas. Par exemple considérons supposons que $a$ soit la chaine `abcabcabd` et $b$ la chaine `abd`.

```text
    
    abcabcabde
    abd         -> dernière lettre pas bonne
     abd        -> inutile, car on sait que la chaine ne commence pas par un b
      abd       -> autant commencer là tout de suite.
      ^
```

Ou encore :

```text
    ababcabde
    ababd        -> dernière lettre pas bonne
     ababd       -> inutile, il n'y a pas de c dans la chaine à trouver.
      ababd      -> autant commencer là tout de suite.
        ^
```

Il faut faire en sorte de n'avoir à regarder les éléments de $a$ qu'un nombre constant de fois : il ne faut pas refaire des choses que l'on sait déjà. Supposons que l'on soit dans cette configuration générale :

```text
           i
a : .......xxxxxYttttt.........
b :        xxxxxZuuuuu
                j
```

Avec :

* $a[i + k] = b[k]$ pour $0 \leq k < j$
* $a[i + j] \neq b[j]$

Comme on connait tous les caractères de $a[i]$ à $a[i + j - 1]$ et qu'ils coïncident avec $b$, dans l'idéal pour ne pas se répéter il faudrait arriver à la situation suivante :

```text
              i'
a : .......xxxxxYttttt.........
b :           xxxxxZuuuuu
                j'
```

C'est à dire de trouver le plus grand $k$ possible tel que $a[(i+j-1)-k:i+j] = b[:k]$ (la fin de $a[i:i+j]$ corresponde au début de $b$), puis poser :

* $i'= i + j - k$
* $j' = j - k$

Exemple :

```text
         i     
a : .....bababac......
b :      babababa 
               j 
```

On continue du coup avec la configuration :

```text
         i     
a : .....bababac......
b :        babababa 
               j 
```

Là encore $a[i+j] \neq b[j]$, la prochaine configuration sera :

```text
         i     
a : .....bababac......
b :          babababa 
               j 
```

Encore une fois $a[i+j] \neq b[j]$, la prochaine configuration sera :

```text
         i     
a : .....bababac......
b :            babababa 
               j 
```

1. on suppose qu'on connaisse le max, algo
2. complexité de l'algo
3. calcul du décalage

Automates : [Knuth-Morris-Pratt](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)

## Autre algorithmes

### prétraitements

Rabin-Karp


### Autre décalages

[Boyer-Moore-Horspool](https://fr.wikipedia.org/wiki/Algorithme_de_Boyer-Moore-Horspool), on part de la fin.

Et [Boyer-Moore](https://fr.wikipedia.org/wiki/Algorithme_de_Boyer-Moore) qui rajoute une règle et est aussi linéaire (preuve dans KMP, mais c'est plus chaud à démontrer...)

Pour implémenter cette idée, il est plus simple de comparer le mot et la séquence en partant de la fin du mot :

```python
def début_algorithme_BMH(a, b):
    i = 0
    while i < len(a) - len(b) + 1:
        trouvé = True
        for j in range(len(b)-1, -1, -1):
            if b[j] != a[i + j]:
                trouvé = False
                
                # décalage de i
        
        if trouvé:
            return True
    return False
```

L'algorithme de Boyer–Moore implémente 2 tables de saut permettant de décaler efficacement l'indice $i$

### première table de saut

Positionnement des deux chaines lors de la 1ère discordance $a[i + j] \neq b[j]$ :

```text
        i    x
a: .....COUCOU......
b:      POUTOU
           j
```

On va alors décaler $i$ du minimum possible, c'est à dire :

* de $m$ (la longueur de $b$) si $a[i + m - 1]$ (le caractère à la position `x` du dessin) n'apparait pas dans les $m-1$ premiers caractères de $b$
* de $m$ moins la position du dernier caractère $a[i + m - 1]$ dans les $m-1$ premiers caractères de $b$ (la chaine `b[:-1]` avec la notation de python). Ceci fera coïncider le caractère à la position `x` de $a$ avec le même caractère dans `b[:-1]`

```text
        i
a: .....COUCOU......
b:         POUTOU
                j
```

Pour notre exemple avec $b$ valant `POUTOU`, ceci donne la table de décalage suivante :

lettre | décalage
-------|---------
P | 5
O | 1
U | 3
T | 2
autre | 6

Cette technique est très efficace si le mot à chercher n'a pas beaucoup de répétition. Pour que le décalage aille vite (en $\mathcal{O}(1)$ opération), l'idée est de créer un tableau de longueur le maximum du numéro unicode de `mot` et de mettre le décalage qu'il faut. On ne peut pas prendre tous les code unicode possible, un tableau de plus de 100000 cases n'est pas raisonnable. Pour un texte avec l'alphabet latin, on aura des codes plus petit que 256 ce qui est raisonnable.

```python
def creation_decalage(mot):
    unicode_max = max(ord(x) for x in mot)
    decalage = []
    for i in range(unicode_max + 1):
        decalage.append(len(mot))

    for i in range(len(mot) - 1):
        decalage[ord(mot[i])] = len(mot) - 1 - i

    return decalage
```

La complexité de la fonction `creation_decalage` est en $\mathcal{O}(m + A)$ opérations, où $A$ est la taille de l'alphabet utilisé, c'est à dire une constante.

L'algorithme devient alors :

```python
def suite_algorithme_BMH(a, b):
    decalage = creation_decalage(b)  # à faire

    i = 0
    while i < len(a) - len(b) + 1:
        trouvé = True
        for j in range(len(b)-1, -1, -1):
            if b[j] != a[i + j]:
                trouvé = False
                
                i += decalage[ord(a[i + len(b) - 1])]
        
        if trouvé:
            return True
    return False
```

Ce n'est cependant pas suffisant pour garantir que l'on ne va pas vérifier 2 fois de suite le même caractère de $a$. Par exemple si la chaîne $a$ vaut `xxxx` et $b$ vaut `Yxx`

Chaque caractère de $a$ (à partir du troisième) va être comparé à chaque caractère de $b$. La complexité maximale de l'algorithme est donc toujours en $\mathcal{O}(nm)$.

### deuxième table de saut

Pour améliorer la complexité de l'algorithme il faut faire en sorte que l'on ne compare chaque caractère de $a$ qu'un nombre constant de fois.

Ceci est possible en utilisant une autre table.

> décrire la table + algo + preuve O(m)
{: .tbd}

décrite là <https://fr.wikipedia.org/wiki/Algorithme_de_Boyer-Moore>. [Knuth, Morris et Pratt](http://static.cs.brown.edu/courses/csci1810/resources/ch2_readings/kmp_strings.pdf) on démontré qu'en utilisant cette deuxième table, chaque caractère de $a$ est au plus examiné 6 fois (la preuve est p343-346 du papier). Mais ceci dépasse le cadre de ce cours.

## vers les expressions régulières

expressions régulières : <https://docs.python.org/fr/3/howto/regex.html>
---
layout: layout/post.njk
title: "DS 1"
---

{% note "**Sujet**" %}

[Étude de l'élément majoritaire](./ds1_2023_2024.pdf){.fichier}

Durée du contrôle : 3h.

{% endnote %}

## Barème

> TBD

## Corrigé

### Exercice 1 : encadrement du problême

#### 1.1

> Combien d'éléments majoritaires peut avoir un tableau ? Prouvez-le rigoureusement

Il ne peut y avoir qu'un seul élément majoritaire car il contient strictement plus de la moitié des éléments. S'il y en avait 2 avec respectivement $n_1$ et $n_2$ éléments on aurait $n = n_1 + n_2 \geq (E(n / 2) + 1) + (E(n / 2) + 1) \geq n + 1$ ce qui est impossible ($E()$ désignant la partie entière).

#### 1.2.1

> Montrez que quelle que soit la taille $n > 2$ du tableau et quel que soit $0 \leq i < n$, il existe un tableau $T$ d'élément majoritaire $e$ tel que $T[i] \neq e$.

Pour tout $n > 2$ on a $\frac{n}{2} + 1 < n$, on peut donc créer un tableau de taille $n$ ayant un deux valeurs distinctes une pour tous les $T[j]$ avec $j\neq i$ (qui sera donc l'élément majoritaire) et l'autre pour $T[i]$.

#### 1.2.2

> Montrez que quelle que soit la taille $n \geq 1$ du tableau et quel que soit $0 \leq i < n$, il existe un tableau $T$ d'élément majoritaire $e$ tel que $T[i] = e$.

Le tableau avec une unique valeur répond trivialement à la question.

#### 1.2.3

> Montrez que quels que soient $n>2$ et $0 \leq i < n$, il existe toujours deux tableaux d'entiers $T$ et $T'$ de taille $n$ tels que :
>
> - $T[j] = T'[j]$ pour tout $j \neq i$,
> - $T$ admet un élément majoritaire,
> - $T'$ n'admet pas d'élément majoritaire.

La question 1.2.1 nous montre que l'on peut créer un tableau possédant un élément majoritaire et tel que $T[i]$ ne soit pas cet élément. On peut de plus s'arranger pour que cet élément majoritaire soit exactement présent la partie entière de $\frac{n}{2}$ plus 1 fois (on remplace si nécessaire les éléments surnuméraires par $T[i]$).

Le tableau $T'$ tel que :

- $T[j] = T'[j]$ pour tout $j \neq i$
- $T'[i]$ vaut l'élément majoritaire de $T$

Répond à la question.

#### 1.2.4

> Déduisez-en que la complexité du problème de l'élément majoritaire est en $\Omega(n)$, avec $n$ la taille du tableau (il n'existe pas d'algorithme permettant de résoudre le problème de l'élément majoritaire en strictement moins de $n$ opérations pour tout $n > N_0$).

On procède comme dans le cours pour démontrer [la complexité du problème de la recherche](/cours/algorithmie/complexité-problème/#complexité-recherche).

On suppose qu'il existe un algorithme prenant strictement moins que $n$ opérations pour trouver l'élément majoritaire de tout tableau de taille $n > N_0$. Prenons un tableau $T$ comme dans la question précédente. On a alors deux cas :

- soit l'algorithme a parcouru toutes les cases de $T$ possédant l'élément majoritaire et il a eu besoin d'au moins $\frac{n}{2} + 1 = \Omega(n)$ opérations,
- soit il n'a pas parcouru toutes les cases de $T$ possédant l'élément majoritaire, disons $T[i]$, et on crée le tableau $T'$ identique à $T$ sauf pour la case d'indice $i$ : $T'$ ne possède pas d'élément majoritaire mais l'algorithme va donner la même réponse que pour $T$. Contradiction.

#### 1.3.1

> Donnez le pseudo-code et la preuve d'une fonction `compte`{.language-} de complexité $\mathcal{O}(n)$ telle que `compte(T, x)`{.language-} est le nombre d'occurrences de $x$ dans $T$ (si $x\notin T$, `compte(T, x)`{.language-} vaut 0).

```python

def compte(T, x):

    nombre = 0
    for element in T:
        if element == x:
            nombre += 1
    return nombre
```

La complexité de la fonction est en $\mathcal{O}(n)$ où $n$ est la taille de $T$ puisque :

- toutes les lignes sont de complexité $\mathcal{O}(1)$
- la boucle `for`{.language-} est exécutée la taille de $T$ fois, c'est à dire $\mathcal{O}(n)$ fois.

L'invariant de boucle que l'on va utiliser pour prouver l'algorithme `compte`{.language-} est : au bout de la $i$ ème itération, `nombre`{.language-} vaut le nombres de fois où `x`{.language-} est présent dans les $i$ premières cases de $T$.

1. l'invariant est clairement vérifié à la fin de la première itération
2. si l'invariant est vérifié à la fin de la $i$ ème itération, , comme la $i+1$ itération vérifie si `x == T[i]`{.language-} et ajoute 1 à `nombre`{.language-} si c'est le cas, l'invariant est toujours vérifié à la fin de la $i + 1$ ème itération.
3. l'invariant est vrai en sortie de boucle, c'est à dire après avoir parcouru tous les éléments de $T$ : `nombre`{.language-} vaut bien le nombre de fois où `x`{.language-} est présent dans $T$.

#### 1.3.2

> Utilisez la question précédente pour créer algorithme en $\mathcal{O}(n^2)$ qui prend un tableau d'entiers en paramètre et rend un élément majoritaire de ce tableau s'il existe, ou `None` sinon.

```python#

def élément_majoritaire(T):
    for x in T:
        if compte(T, x) > len(T) / 2:
            return x
    return None
```

Le test de la ligne 4 est en $\mathcal{O}(n)$ où $n$ est la taille de $T$ puisqu'il faut exécuter `compte`{.language-}. Toutes les autres lignes sont de complexité $\mathcal{O}(1)$ et comme la boucle `for`{.language-} est exécutée la taille de $T$ fois, on exécute `compte`{.language-} $n$ fois ce qui porte la complexité de l'algorithme à $\mathcal{O}(n^2)$.

L'invariant de boucle que l'on va utiliser pour prouver l'algorithme `élément_majoritaire`{.language-} est : au bout de la $i$ ème itération,aucun des $i$ premières cases de $T$ n'est un élément majoritaire.

1. l'invariant est clairement vérifié à la fin de la première itération
2. si l'invariant est vérifié à la fin de la $i$ ème itération, comme la $i+1$ itération vérifie si `T[i]`{.language-} est un élément majoritaire, l'invariant est toujours vérifié à la fin de la $i + 1$ ème itération.
3. l'invariant est vrai en sortie de boucle, c'est à dire après avoir parcouru tous les éléments de $T$ : si on arrive en ligne 6, c'est que $T$ n'a pas d'élément majoritaire. Si l'on s'arrête à la fin de la $i$ ème itération c'est que `T[i-1]`{.language-} est l'élément majoritaire de $T$.

#### 1.3.3

> Explicitez en quelques phrases le fonctionnement de l'algorithme de la question précédente si, en entrée, on lui donne les deux exemples du début de l'énoncé.

En utilisant le premier tableau, la fonction va parcourir tous les éléments de $T$ et pour chacun effectuer la fonction `compte`{.language-} sans trouver d'élément présent 5 fois ou plus.

En utilisant le premier tableau, la fonction sortir au bout de la première itération puisque 2 est l'élément majoritaire de $T$.

#### 1.3.4

> En déduire que la complexité du problème de l'élément majoritaire est en $\mathcal{O}(n^2)$

L'algorithme de la question 1.3.2 résoud le problème de la recherche d'un élément majoritaire, sa complexité est donc un majorant de la complexité du problème.

### Exercice 2 : Tris

#### 2.1.1

> Donnez le nom d'un algorithme de tri ayant une complexité de $\mathcal{O}(n\ln(n))$ avec $n$ la taille du tableau à trier. Vous expliciterez son fonctionnement en quelques phrases.

L'algorithme vu en cours qui a cette complexité est [le tri fusion](/cours/algorithmie/problème-tris/algorithme-fusion){.interne} il utilise le principe algorithmique _diviser pour régner_. L'idée est de composer une liste triée à partir de deux listes elles même triées. L'algorithme est le suivant :

1. on scinde la liste en 2 parties égale que l'on trie en utilisant la récursion
2. on crée une liste triée à partir des deux sous-listes triées (ceci peut se faire en $\mathcal{O}(n)$ opérations)
3. on rend la liste finale triée

La complexité nous est donnée par le master théorème.

#### 2.1.2

> Justifiez en quelques phrases que le problème du tri est en $\Omega(n\ln(n))$.

Il faut pouvoir distinguer parmi tous les ordres possibles et il y en a $n!$. Il faut donc au moins $\Omega(\ln(n!))$ tests pour disinguer tous les cas. On conclut en remarquant que $\Omega(\ln(n!)) = \Omega(n\ln(n))$.

#### 2.1.3

> Déduisez-en que le problème du tri est en $\Theta(n\ln(n))$.

1. On a un algorithme en $\mathcal{O}(n\ln(n))$ pour résoudre le problème
2. On sait qu'il faut au moins $\Omega(n\ln(n))$ opérations

Les deux conditions ci-dessus montrent, par définiton, que le problème du tri est en $\Theta(n\ln(n))$.

#### 2.2.1

> Si $T$ est trié, démontrez l'existence d'un indice $i$ (que vous expliciterez) tel que, si $T$ admet un élément majoritaire $x$, alors $x=T[i]$.

Si le tableau `T`{.language-} est trié et qu'il contient un élément majoritaire, alors c'est l'élément à la position `len(T) // 2`{.language-} (`//`{.language-} est la division entière). Supposons en effet que `T[len(T) // 2]`{.language-} ne soit pas un élément majoritaire de `T`{.language-}. Comme les éléments de `T`{.language-} strictement plus grand (_resp._ strictement plus petit) que `T`{.language-} sont tous d'indices strictement plus grand (_resp._ strictement plus petit) que `len(T) // 2`{.language-} il y en a au plus `len(T) // 2`{.language-} : ils ne peuvent pas être majoritaire. Ainsi si `T[len(T) // 2]`{.language-} n'est pas un élément majoritaire de `T`{.language-}, le tableau ne possède pas d'éléments majoritaire.

#### 2.2.2

> Déduisez-en un algorithme itératif, dont vous donnerez le pseudo-code et la preuve, plus efficace que celui de l'exercice 1.3.2 pour résoudre le problème de l'élément majoritaire.

 ```python

 def element_majoritaire(T):
     T.sort()
     if compte(T[len(T) // 2], T) > len(T) / 2:
         return T[len(T) // 2]
     return None
 ```

L'algorithme commence par trier le tableau et compte le nombre d'occurence de l'élément au milieu. Ci cette occurence est majoritaire, on a trouvé notre  élément majoritaire et si elle ne l'est pas, la question 2.2.1 montre que le tableau ne peut avoir d'élément majoritaire,

Sa complexité est ramené à la complexité du tri plus une fois la complexité de `compte`{.language-} : la complexité est donc en $\mathcal{O}(len(T) \ln(len(T)))$.

#### 2.2.3

> Explicitez en quelques phrases le fonctionnement de l'algorithme de la question précédente si, en entrée, on lui donne les deux exemples du début de l'énoncé.

- En utilisant le premier tableau, son tri va donner le tableau `T = [2, 4, 4, 4, 4, 4, 5, 5, 5]`{.language-} et son milieu `T[4]`{.language-} vaut 4 qui est majoritaire.
- En utilisant le second tableau, son tri va donner le tableau `T = [2, 2, 2, 2, 2, 2, 3, 3, 3, 3,  4, 6]`{.language-} et son milieu `T[6]`{.language-} vaut 3 n'est pas majoritaire : le tableau n'a pas d'élément majoritaire.

### Exercice 3 : Diviser pour régner

### Exercice 4 : Piles

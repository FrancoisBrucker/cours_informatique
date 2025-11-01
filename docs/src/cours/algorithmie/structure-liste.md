---
layout: layout/post.njk
title: "La liste"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD comme en go : len et cap.


Une liste est une amélioration de [la structure de tableau](../pseudo-code/briques-de-base/#tableaux){.interne} et sont les conteneurs de base du langage python. Tout comme les tableaux ce sont des objets pouvant contenir une succession d'autres objets auxquels on peut accéder par un _index_, mais on peut facilement ajouter/supprimer un nombre infini d'éléments en fin de liste.

{% info %}
Vous devriez savoir manipuler des listes comme personne. Mais si vous avez besoin d'une piqûre de rappel, n'hésitez pas à consulter [la partie consacrée aux listes](/cours/coder-et-développer/bases-programmation/conteneurs/listes/){.interne} du cours sur les bases du code.
{% endinfo %}

## <span id="structure"></span>Définition de la structure

<span id="structure-liste"></span>

```pseudocode
structure Liste<Type>:
    attributs:
        longueur: entier ← 0
        T: [Type] de longueur longueur
    méthodes:
        fonction get(i: entier) → Type:  # valeur ← self[i] = valeur ← self.get(i)
            rendre T[i]
        fonction set(i: indice, valeur: Type) → ∅:  # self[clé] ← valeur = self.set(clé, valeur)
            T[i] ← valeur

        fonction append(x: Type)  → ∅:
            si longueur == T.longueur:
                T2 ← T

                longueur ← 0
                T ← un nouveau tableau de Type de longueur 2 * T2.longueur
                pour chaque y de T2:
                    append(y)

                append(x)
            sinon:
                T[longueur] ← x
                longueur ← longueur + 1
        fonction pop()  → Type:
            longueur ← longueur - 1
            rendre T[longueur]

        fonction insert(pos: entier, x: Type) → ∅:
            self.append(T[-1])
            pour chaque i allant de T.longueur - 1 à pos + 1 par pas de -1:
                T[i] ← T[i-1]
            T[pos] ← x
        fonction delete(pos: entier) → Type:
            r ← T[pos]
            pour chaque i de [pos .. T.longueur - 1[:
                T[i] ← T[i+1]
            self.pop()

            return r

```

<span id="structure-getter-setter"></span>

{% note "**Getter et setter**" %}
On utilise l'abus de notation suivant, classique en programmation, permettant de masquer des méthodes par un accès direct. Pour une liste `l`{.language-} :

- accès à un élément : on écrira `e ← l[i]` à la place de `e ← l.get(i)`
- changer un élément : on écrira `l[i] ← e` à la place de `l.set(i, e)`

{% endnote %}

Ceci permet d'utiliser une liste comme un tableau, en ajoutant en plus 4 méthodes permettant de modifier sa longueur :

- `append`{.language-} qui ajoute un élément en fin de liste
- `insert`{.language-} qui insère un élément à une position quelconque de la liste en décalant les éléments après vers la droite
- `pop`{.language-} qui rend le dernier élément de la liste et le supprime de la liste
- `delete`{.language-} qui rend un élément à une position quelconque de la liste et le supprime de la liste en décalant les éléments après vers la gauche

Lorsque la longueur du tableau devient trop petite pour contenir toutes les valeurs, on crée un tableau de longueur double : on peut ajouter autant d'éléments à une liste que l'on souhaite ! Le code suivant est donc légitime :

```pseudocode
l ← Liste<entier>
pour chaque i de [0 .. 2^42]:
    l.append(i)

pour chaque i de [0 .. 2^42[:
    l[i] ← l[i + 1]
```

{% attention "**À retenir**" %}
La liste est une généralisation du tableau permettant de modifier sa longueur.
{% endattention %}

## Complexités

Examinons les complexités des méthodes de listes.

### Création

A la création de la liste, on crée un tableau de longueur $K$, une constante ni trop petite, ni trop grande :

{% note %}
La complexité de la création d'une liste est $\mathcal{O}(1)$.
{% endnote %}

### Ajout d'un élément

L'ajout d'un élément en fin de liste va être de complexité $\mathcal{O}(T.\mbox{\small longueur})$ dans le pire des cas puisqu'il faut créer un nouveau tableau puis tout recopier. Notez bien que l'on ne peut pas faire mieux puisqu'il est impossible de contrôler l'endroit où l'on crée un nouveau tableau (on ne peut pas le coller à l'ancien tableau).

**Cependant**, on va y revenir plus tard, si l'on vient de créer un nouveau tableau $T$, il ne sera qu'à moitié plein : les $T.\mbox{\small longueur} / 2$ prochains ajout d'éléments se feront en $\mathcal{O}(1)$
 opérations !

{% note %}
La complexité de l'ajout d'un élément en fin de liste avec `Liste.append`{.language-} est en $\mathcal{O}(T.\mbox{\small longueur})$ (cas le pire), **mais s'il reste de la place**, elle est en $\mathcal{O}(1)$.
{% endnote %}

Si l'on insère un élément au milieu de la liste, on commence par faire l'algorithme précédent pour ajouter une case au tableau, puis on décale d'une case vers la droite les éléments à partir du $i$ème et enfin on affecte le nouvel élément à sa place. Comme il faut toujours déplacer des éléments :

{% note %}
La complexité de l'**insertion d'un élément à une position quelconque** dans une liste  avec `Liste.insert`{.language-}  est en $\mathcal{O}(T.\mbox{\small longueur})$.
{% endnote %}

### Suppression d'un élément

Pour supprimer le dernier élément d'une liste on n'a qu'une opération à faire :

{% note %}
La complexité de la **suppression du dernier élément d'une liste** avec `Liste.pop`{.language-} est $\mathcal{O}(1)$.
{% endnote %}

Si l'on supprime un élément au milieu de la liste, on commence par décaler d'une case vers la droite les éléments à partir du i+1 ème et enfin on fait $n=n-1$ :

{% note %}
La complexité de la suppression d'un élément à une position quelconque dans une liste  avec `Liste.delete`{.language-}  est en $\mathcal{O}(T.\mbox{\small longueur})$.
{% endnote %}

## Complexité d'ajout de $N$ éléments à la fin de la structure

Ajouter un élément à la fin de la structure peut très mal tomber : cela peut être juste au moment où l'on doit doubler la taille de la structure. C'est donc de complexité $\mathcal{O}(n)$ opérations s'il y avait $n$ élément dans la liste au moment de l'ajout... Mais ensuite, les $n-1$ suivants ajout vont **forcément** bien se passer et auront tous une complexité de $\mathcal{O}(1)$ opérations.

On a le résultat suivant :

<div id="preuve-liste-ajout"></div>
{% note "**Proposition**" %}
L'ajout de $N$ éléments à une liste initialement vide prend $\mathcal{O}(N)$ opérations au maximum
{% endnote %}
{% details "preuve", "open" %}

Dans le cas le pire le dernier ajout entraîne un doublement de la taille de la structure.

- lors de l'ajout du $N$ ème élément, un nouveau tableau de longueur $2\cdot N$ est créé en $\mathcal{O}(1)$ puis les $N-1$ éléments de l'ancien tableau sont copiés dans le nouveau en $\mathcal{O}(N)$ opérations enfin, l'élément final est ajouté à la liste en $\mathcal{O}(1)$ opérations. Tout ceci à pris $\mathcal{O}(N)$ opérations
- l'ajout du $N-1$ ème élément s'est fait sans créer de nouveau tableau et à donc nécessité que $\mathcal{O}(1)$ opérations
- ...
- l'ajout du $\frac{N}{2} + 1$ ème élément s'est fait sans créer de nouveau tableau et à donc nécessité que $\mathcal{O}(1)$ opérations
- l'ajout du $\frac{N}{2}$ ème élément s'est fait en créant un nouveau tableau et à donc nécessité au total $\mathcal{O}(\frac{N}{2})$ opérations
- l'ajout du $\frac{N}{2}-1$ ème élément s'est fait sans créer de nouveau tableau et à donc nécessité que $\mathcal{O}(1)$ opérations
- ...
- l'ajout du $\frac{N}{4} + 1$ ème élément s'est fait sans créer de nouveau tableau et à donc nécessité que $\mathcal{O}(1)$ opérations
- l'ajout du $\frac{N}{4}$ ème élément s'est fait en créant un nouveau tableau et à donc nécessité au total $\mathcal{O}(\frac{N}{4})$ opérations
- ...
- le $\log_2(N)$ tableau précédent était de longueur $\frac{N}{2^{\log_2(N)}} = 1$ et son remplissage a pris un nombre d'opérations de $\mathcal{O}(\frac{N}{2^{\log_2(N)}}) = \mathcal{O}(1)$ opérations

La complexité totale du remplissage de la liste en partant de la liste vide est donc la somme de tout ça :

<div>
$$
\begin{array}{lcl}
C(N) &=& \mathcal{O}(N + \underbracket{1 + \cdot + 1}_{N/2 - 1} + \frac{N}{2} + \underbracket{1 + \cdot + 1}_{N/4 - 1} + \frac{N}{4} + \cdot + \frac{N}{2^{\log_2(N)}})\\
& \leq &\mathcal{O}(N + 2 \cdot \frac{N}{2} + 2 \cdot \frac{N}{4} + \cdot + 2 \cdot \frac{N}{2^{\log_2(N)}})\\
& \leq & \mathcal{O}(N + N \cdot \sum_{i=1}^{\log_2(N)}{\frac{1}{2^i}})\\
& \leq & \mathcal{O}(N \cdot \sum_{i=0}^{\log_2(N)}{\frac{1}{2^i}})
\end{array}
$$
</div>

Comme, [on l'a vu](../projet-sommes-classiques/){.interne}, $\sum_{i=0}^{n} \frac{1}{2^i} \to_{+\infty} 2$ :

<div>
$$
\begin{array}{lcl}
C(N) &\leq & \mathcal{O}(2 \cdot N) = \mathcal{O}(N)
\end{array}
$$
</div>

{% enddetails %}
{% info %}
Le calcul est toujours vrai si l'on part d'une liste non vide au départ.
{% endinfo %}

{% note %}
Comme la complexité de l'ajout de $N$ élément en fin de liste est en $\mathcal{O}(N)$ opérations, on considère (sans approximation) que **la complexité de l'ajout d'un élément en fin de liste** vaut $\mathcal{O}(\frac{N}{N}) = \mathcal{O}(1)$.

{% endnote %}

On appelle ce genre de raisonnement [analyse en complexité amortie](../complexité-amortie/){.interne} et sera étudié un peu plus tard. C'est très utile lorsque la même opération (ici l'ajout d'un élément en fin de liste) peut prendre des complexité très différentes, mais pas de façon indépendante.

La structure de liste est un cas _simple_ où la complexité amortie est très utile car elle permet de mieux estimer la complexité : lorsque l'on ajoute $n$ fois un élément, cette opération n'est coûteuse qu'un petit nombre de fois :

{% attention "**À retenir**" %}
Dans nos calculs de complexité on utilisera $\mathcal{O}(1)$ comme complexité d'**ajout d'un élément en fin de liste** puisque c'est sa _complexité amortie_.

{% endattention %}

## Bilan

{% note "**Quand utiliser cette structure**" %}

 À chaque fois que l'on pourrait utiliser un tableau **et** que l'on est pas contraint  par la taille mémoire (on peut allouer/désallouer de la mémoire et l'endroit de la mémoire où est stocké la liste importe peu).

{% endnote%}

La complexité des opérations de la liste commune avec un tableau (lecture écriture à index fixé) est de même complexité et on peut ajouter/supprimer des éléments se fait en $\mathcal{O}(1)$ en amorti.

## Améliorations possibles

### Gérer la suppression

Pour ne pas gâcher de la place, une amélioration courante des listes est de réduire la longueur du tableau si après la suppression du dernier élément de la liste, sa longueur $m$ est deux fois plus grande que le nombre $n$ d'éléments stockés.

Même si l'ajout en fin de liste et la suppression en fin de liste ont des complexités variables, ceci ne change cependant pas la complexité amortie (même si la preuve est autrement plus difficile à démontrer) de l'utilisation d'une liste :

{% note "**Proposition**" %}
La complexité amortie de l'ajout et de la suppression d'un élément en fin de liste est en $\mathcal{O}(1)$.
{% endnote %}
{% details "preuve" %}
Voir [exercice de la complexité amortie](../complexité-amortie/#exercice-liste-suppression-ajout){.interne}.
{% enddetails %}

La plupart des implémentations des listes ont cette implémentation, ceci en fait une structure idéale pour stocker des objets.

### De combien augmenter la longueur ?

Doit-on augmenter la longueur du tableau de 2 ? De 1.5 ? D'autre chose ? La réponse à cette question est bien plus délicate qu'on ne le pense et dépend fortement de l'usage qu'on va avoir des listes. Regardez la vidéo ci-dessous pour vous en convaincre :

{% lien %}
<https://www.youtube.com/watch?v=GZPqDvG615k>
{% endlien %}

## Utilisation

L'intérêt d'une liste par rapport à un tableau est que l'on peut modifier sa longueur en ajoutant et supprimant des éléments.

Si l'ajout et la suppression d'un élément en fin de liste est de complexité $\mathcal{O}(1)$, ce n'est pas garantie si on doit ajouter/supprimer des éléments en milieu de liste.

Nous allons voir ici différentes stratégies selon que l'ordre des éléments stockés nous intéresse ou non. Notez que l'ajoute d'un élément en milieu de liste se fait de la même manière.

{% exercice %}

Écrire un algorithme permettant de supprimer un indice donné d'une liste :

1. sans créer de liste annexe
2. de façon optimale

Pour cet exercice, l'ordre doit être conservé.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme suppression_indice(L: Liste<T>, i: indice) → ∅:
    pour chaque j de [i + 1 .. L.longueur[:
        L[j-1] ← L[j]
    L.pop()
```

La complexité est optimale puisqu'il faut décaler tous les éléments après ceux d'indice $i$ et que la complexité de la méthode `Liste.pop`{.language-} est $\mathcal{O}(1)$.
{% enddetails %}

Si l'on ne se préoccupe pas de l'ordre dans la liste, on peut très facilement supprimer un élément _in place_ :

{% exercice %}

Écrire un algorithme permettant de supprimer un indice d'une liste :

1. sans créer de liste annexe
2. de façon optimale

Pour cet exercice, on ne se préoccupe pas de l'ordre des éléments dans la liste.

{% endexercice %}
{% details "corrigé" %}

Puisqu'on ne se préoccupe pas de l'ordre entre éléments, on échange l'élément à supprimer avec le dernier de la liste puis on pop.

```pseudocode
algorithme suppression_indice(L: Liste<T>, i: indice) → ∅:
    L[i], L[-1] ← L[-1], L[i]
    L.pop()
```

La complexité de cet algorithme est de complexité $\mathcal{O}(1)$, donc optimale.

{% enddetails %}

On veut maintenant supprimer tous les éléments de la liste égaux à une valeur donnée :

{% exercice %}

Écrire un algorithme permettant de supprimer une valeur d'une liste :

1. sans créer de liste annexe
2. de façon optimale

Pour cet exercice, l'ordre doit être conservé.

{% endexercice %}
{% details "corrigé" %}

On décale les éléments petit à petit.

```pseudocode
algorithme suppression_indice(L: Liste<T>, v: T) → ∅:
    j ← 0
    i ← 0
    tant que i + j < L.longueur:
        L[i] ← L[i + j]
        si L[i] == v:
            j ← j + 1
        sinon:
            i ← i + 1
            
    répéter j fois:
        L.pop()
```

La complexité est en $\mathcal{O}(L.\text{\small longueur})$ et donc optimale puisqu'il faut parcourir tous les éléments de la liste (chacun d'entre eux pouvant valoir $v$).

On prouve cet algorithme par invariant que l'on démontre aisément :

> **Invariant de boucle :** À la fin de chaque itération la liste $L[\;:i]$ est la restriction de la liste $L[\;:i + j]$ aux éléments différents de $v$.

{% enddetails %}

{% exercice %}

Écrire un algorithme permettant de supprimer une valeur d'une liste :

1. sans créer de liste annexe
2. de façon optimale

Pour cet exercice, on ne se préoccupe pas de l'ordre des éléments dans la liste.

{% endexercice %}
{% details "corrigé" %}

Comme il faut tout de même parcourir tous les éléments de la liste, on peut utiliser l'algorithme précédent ! Relâcher la contrainte de l'ordre ne fait rien gagner ici.

{% enddetails %}

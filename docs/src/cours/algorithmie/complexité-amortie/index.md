---
layout: layout/post.njk

title: Analyse et complexité amortie

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

L'analyse amortie (et la complexité amortie qui en découle) est une technique utilisée pour calculer la complexité lorsque plusieurs exécution successive d'un même bloc de code va être de complexité différente.

Par l'exemple lors de l'utilisation de structures complexes où les instructions coûteuses ne sont faites qu'un petit nombre de fois lorsque l'on exécute la méthode plusieurs fois (comme pour [les listes](/cours/coder-et-développer/bases-python/structurer-son-code/conteneurs/listes){.interne} par exemple).

{% attention %}
Ce n'est **pas** une complexité en moyenne, c'est un moyen de calculer des complexités (maximum)
{% endattention %}

## Définitions

Si lors de l'exécution d'un algorithme $A$, une opération $O$ (ou une fonction) de celui-ci se répète plusieurs fois et que sa
complexité diffère selon les appels, le calcul de la complexité de $A$ va nécessiter une analyse fine de de **toutes** les exécutions de l'opération $O$ car borner la complexité par le maximum conduit (souvent) à surestimer grandement la complexité réelle.

{% note "**Définition**" %}
L'**_analyse amortie_** est regroupe un ensemble des techniques permettant de calculer globalement la complexité maximale $C$ de $m$ exécutions successives d'un algorithme.

La **_complexité amortie_** de cet algorithme est alors $\frac{C}{m}$.
{% endnote %}

Il ne faut pas le confondre avec la complexité en moyenne, c'est bien $n$ fois la complexité maximale que l'on considère lorsque l'on effectue les opération successivement.

La complexité amortie est une moyenne de complexité maximale, ce n'est **pas** [une complexité en moyenne](../complexité-moyenne){.interne} qui est une moyenne probabiliste. Lors d'un calcul de complexité amortie on connaît les paramètres de chaque exécution alors qu'il ne sont connu qu'en probabilité pour un complexité en moyenne.

Le temps moyen d'exécution pourra être supérieur à la complexité en moyenne si on a pas de chance alors qu'il ne pourra **jamais** excéder la complexité amortie.

{% attention "**À retenir**" %}

Pour des structures de données utilisées (très) souvent, on utilise la complexité amortie dans les calculs de complexités maximales.

Pour ces structures, complexité amortie et maximale sont par abus de langage considérés comme équivalentes.

{% endattention %}

La complexité amortie est un concept avancé, utilisée dans deux cas principalement :

- comme synonyme de complexité maximale pour des structures de données très utilisées (celui que vous verrez le plus souvent)
- comme moyen de calcul de complexité pour des algorithmes dont les boucles ou les exécutions successives ont des complexités très différentes

## Algorithmes exemples

Pour illustrer ces techniques d'analyse amortie nous allons utiliser deux exemples (ultra classiques) ci-dessous. Ils sont paradigmatiques de l'analyse amortie où une même opération peut avoir une complexité très faible ou très importante selon les cas. Une analyse fine de la complexité montrera que dans l'exécution globale de l’algorithme ces complexités sont liées et qu'une opération de complexité importante sera forcément suivie de c'opérations de faibles complexité.

### <span id="compteur-binaire"></span>Compteur binaire


Dans ce problème, on encode un nombre binaire de $n$ bits par une liste $N$ à $n$ éléments. Pour $n=3$ par exemple, $N = [0, 0, 1]$ correspondra à $1$ et $N = [1, 1, 0]$ à 6.

Soit lors l'algorithme suivant, écrit en python :

```python/
def successeur(N):
    i = len(N) - 1

    while (i >= 0) and (N[i] == 1):
        N[i] = 0
        i -= 1

    if i >= 0:
        N[i] = 1
```

A un nombre `N`{.language-} écrit au format binaire donné, `successeur(N)`{.language-} va l'incrémenter de 1.

On a déjà vu ce problème dans [la partie exercice](/cours/algorithmie/projet-classiques/compteur-binaire/){.interne} où on a calculé la complexité max et en moyenne d'une de ses exécutions. Nous allons ici exécuter cet algorithme pour afficher tous les entiers :

```python
def tous(n):

    N = [0] * n

    for i in range(2 ** n):
        successeur(N)
        print(N)
```

{% exercice "**Problème**" %}
La complexité de l'exécution `tous(n)`{.language-} dépend de l'exécution $2^n$ fois de l'algorithme `successeur(N)`{.language-}.

Quel est la complexité totale de l'exécution des $2^n$ opérations ? En déduire la complexité amortie de ces opérations.
{% endexercice %}

Comme pour l'exemple de la pile, la difficulté du calcul vient du fait que la complexité de la fonction `successeur(N)`{.language-} n'est pas constante :

- au mieux, $N[-1] = 0$ et la complexité de `successeur(N)`{.language-} est $\mathcal{O}(1)$,
- au pire, $N = [1, \dots, 1]$ et la complexité de `successeur(N)`{.language-} est $\mathcal{O}(n)$,

La complexité totale de l'exécution des $2^n$ instances de `successeur(N)`{.language-} est alors estimée à : $\mathcal{O}(n \cdot 2^n)$.

La aussi on le démontrera précisément, mais on peut intuitivement voir que cette borne surestime grandement la complexité réelle car si lors d'une exécution de l'algorithme `successeur(N)`{.language-}, $N[-1] = 1$ alors lors de l'exécution suivant on aura $N[-1] = 0$. La complexité de `successeur(N)`{.language-} ne peut donc être importante qu'au pire une fois sur deux.

### Piles

{% note "**Définition**" %}
Une **_[pile](<https://fr.wikipedia.org/wiki/Pile_(informatique)>)_** est une une structure de donnée informatique fondamentale. Qui possède 3 opérations :

- une méthode `push(x)`{.language-} qui ajoute l'élément `x`{.language-} à la structure en $\mathcal{O}(1)$ opérations
- une méthode `pop()`{.language-} qui supprime l'élément le plus **récemment** ajouté à la structure en $\mathcal{O}(1)$ opérations et le renvoie
- une fonction `len(P)`{.language-} qui renvoie le nombre d'éléments de la pile `P`{.language-} en $\mathcal{O}(1)$ opérations

{% endnote %}

Une pile peut être vue comme une pile d'assiette. On ajoute et on supprime les assiettes depuis le haut de la pile.

{% info %}
Ne confondez pas pile et [file](<https://fr.wikipedia.org/wiki/File_(structure_de_données)>). La file supprime l'élément le plus **anciennement** ajouté.
{% endinfo %}

{% exercice %}
Implémentez une structure de pile en python.
{% endexercice %}
{% details "solution" %}
On utilise une liste et les méthodes :

- `append`{.language-} pour ajouter un élément à la structure
- `pop`{.language-} pour supprimer un élément de la structure

La fonction `len`{.language-} nous permet de connaître le nombre d'élément dans la structure.

Dans un interpréteur python :

```python
>>> P = list()
>>> P.append(2)
>>> P.append(5)
>>> len(P)
2
>>> x = P.pop()
>>> print(x)
5
>>> x = P.pop()
>>> len(P)
0
>>> print(x)
2
>>>
```

{% enddetails %}

On crée la fonction suivante, dont la complexité de la fonction `K-pop(k, P)`{.language-} :

```text
Nom : k-pop
Entrées :
    k : un entier
    P : une pile
Programme :
    k = min(k, len(P))
    Soit L une liste de taille k
    répéter k fois:
        x = P.pop()
        ajoute x à la fin de L
    Retour L

```

Si $k = 0$ ou `P`{.language-} est vide la complexité de `K-pop(k, P)`{.language-} est $\mathcal{O}(1)$ et sinon elle est — clairement — de $\mathcal{O}(\min(k, \mbox{len}(P)))$. On peut donc dire que la complexité de `K-pop(k, P)`{.language-} est de $\mathcal{O}(1 + \min(k, \mbox{len}(P)))$ pour tous $k$ et `P`{.language-}.

{% exercice "**Problème**" %}
Soit $A$ un algorithme $A$ utilisant une pile $P$ via les opérations `len`{.language-}, `push`{.language-} et `k-pop`{.language-}. On suppose que l'algorithme effectue $m$ de ces opérations pendant son exécution.

Quel est la complexité totale de ces $m$ opérations ? En déduire la complexité amortie de ces opérations.
{% endexercice %}

La difficulté du calcul vient du fait que la complexité de la fonction `k-pop`{.language-} n'est pas constante. Bornons-là. On a effectué $m$ opérations, la taille maximale de la pile est donc de $m-1$ (si on a effectué $m-1$ opérations `push`{.language-} avant de la vider entièrement avec une instruction `k-pop`{.language-}) : la complexité de `k-pop`{.language-} est bornée par $\mathcal{O}(m)$.

On en conclut que la complexité de l'utilisation de la pile $P$ par l'algorithme $A$ est bornée par $m$ fois la complexité maximale des opérations `len`{.language-}, `push`{.language-} et `k-pop`{.language-} donc $\mathcal{O}(m^2)$.

On le démontrera précisément ci-après, mais on peut intuitivement voir que cette borne surestime grandement la complexité réelle :

- Pour que `k-pop`{.language-} ait une complexité de $\mathcal{O}(m)$, il faut avoir $\mathcal{O}(m)$ opérations `push`{.language-} avant. On ne peut donc pas avoir beaucoup d'opérations `k-pop`{.language-} avec cette grande complexité
- Après une exécution de `k-pop`{.language-} avec une complexité de $\mathcal{O}(m)$, la pile est vide. Les exécutions suivante de `k-pop`{.language-} seront de complexité très faible.

## Analyse par Agrégat

{% note %}
La technique de **_l'analyse par agrégat_** consiste à considérer l'ensemble des $m$ exécutions comme un **tout**.

On évalue la complexité des $m$ opérations en même temps, sans distinguer les différentes opérations.
{% endnote %}

### <span id="compteur-agrégat"></span> Exemple du compteur

Tout d'abord, on remarque que le nombre d'opérations de `successeur(N)`{.language-} dépend de l'indice du dernier `0`{.language-} dans la liste `N`{.language-} :

- si `N`{.language-} finit par la liste `[0]`{.language-} il faut de l'ordre de 1 opération à successeur (la boucle `while`{.language-} de la ligne 4 fait un test et aucune itération)
- si `N`{.language-} finit par la liste `[0, 1]`{.language-} il faut de l'ordre de 2 opérations à successeur (la boucle `while`{.language-} de la ligne 4 fait une itération)
- si `N`{.language-} finit par la liste `[0, 1, 1]`{.language-} il faut de l'ordre de 3 opérations à successeur (la boucle `while`{.language-} de la ligne 4 fait deux itérations)
- ...
- si `N`{.language-} finit par la liste `[0] + [1] * i`{.language-} il faut de l'ordre de $i+1$ opérations à successeur
- ...
- si `N`{.language-} finit par la liste `[0] + [1] * (n-1)`{.language-} il faut de l'ordre de $n$ opérations à successeur
- si `N`{.language-} finit par la liste `[1] + [1] * (n-1)`{.language-} il faut de l'ordre de $n$ opérations à successeur

Nous allons compter le nombre total d'opérations de façons différentes.

#### <span id="compteur-agrégat-partition"></span> Partitionnement de l'ensemble d'entrée

On peut partitionner l'ensemble des $2^n$ nombres binaires à $n$ bits en $n$ ensembles disjoints :

1. $\mathcal{N}_1$ tous les nombres qui finissent par `0`. Il y en a $\frac{2^n}{2}$
2. $\mathcal{N}_2$ tous les nombres qui finissent par `01`. Il y en a $\frac{2^n}{2^2}$
3. ...
4. $\mathcal{N}_i$ tous les nombres qui finissent par `0` suivi de (i-1) `1`. Il y en a $\frac{2^n}{2^i}$
5. $\mathcal{N}_n$ tous les nombres qui finissent par `0` suivi de (n-1) `1`. Il y en a $\frac{2^n}{2^n}$
6. $\mathcal{N}'_{n}$ contenant le nombre ne contenant que des `1`. Il y en a 1

Il faudra de l'ordre de $i$ opérations à `successeur(N)`{.language-} pour traiter un nombre de $\mathcal{N}_i$ et $n$ opérations pour traiter l'élément de $\mathcal{N}'_n$. Comme on a partitionné l'ensemble de toutes les entrées possibles et que notre algorithme va les utiliser tous une unique fois, on en conclut que la complexité totale de l'algorithme est :

$$
C = \sum_{i=1}^{n}i\cdot \frac{2^n}{2^i} + n = 2^n \cdot \sum_{i=1}^{n}\frac{i}{2^i} + n
$$

Calculons cette complexité :

<div>
$$
\begin{array}{rcl}
C&=& 2^n \cdot \sum_{i=1}^{n}\frac{i}{2^i} + n\\
&=& 2^n \cdot (\sum_{k=1}^n\sum_{i=k}^{n}\frac{1}{2^i}) + n\\
&=&2^n \cdot (\sum_{k=1}^n(\sum_{i=1}^{n}\frac{1}{2^i} - \sum_{i=1}^{k-1}\frac{1}{2^i})) + n\\
&=&2^n \cdot (n\cdot \sum_{i=1}^{n}\frac{1}{2^i} - \sum_{k=2}^n\sum_{i=1}^{k-1}\frac{1}{2^i}) + n
\end{array}
$$
</div>

On utilise alors le fait que : $\sum_{i=1}^{n} \frac{1}{2^i} = 1 - \frac{1}{2^{n}}$ (immédiat par récurrence mais il existe également [une preuve directe](https://fr.wikipedia.org/wiki/1/2_%2B_1/4_%2B_1/8_%2B_1/16_%2B_%E2%8B%AF)), ce qui permet d'obtenir :

<div>
$$
\begin{array}{rcl}
C&=&2^n \cdot (n\cdot \sum_{i=1}^{n}\frac{1}{2^i} - \sum_{k=2}^n\sum_{i=1}^{k-1}\frac{1}{2^i}) + n\\
&=&2^n \cdot (n\cdot (1-\frac{1}{2^n}) - \sum_{k=2}^n(1-\frac{1}{2^{k-1}})) + n\\
&=&2^n \cdot (n\cdot (1-\frac{1}{2^n}) - (n-1) -\sum_{i=1}^{n-1}(1-\frac{1}{2^{i}})) + n\\
&=&2^n \cdot (1-\frac{n}{2^n}+1-\frac{1}{2^{n-1}}) + n\\
&=&2^n \cdot (2-\frac{n+2}{2^n}) + n\\
&=&2^{n+1} \cdot (1-\frac{1}{2^n})
\end{array}
$$
</div>

### <span id="pile-agrégat"></span> Exemple de la pile

Au cours des $m$ exécutions, on peut considérer ue l'on a fait appel :

- $m'$ fois à la fonction `k-pop`{.language-},
- $m''$ fois à la fonction `push`{.language-},
- $m - m' - m''$ fois à la fonction `len`{.language-}.

Le nombre total d'éléments _popés_ au cours des $m'$ exécutions de la fonction `k-pop`{.language-} ne peut excéder le nombre total $m''$ d'éléments _pushés_. La complexité totale des $m'$ exécutions de `k-pop`{.language-} vaut donc $\mathcal{O}(m' + m'')$.

Comme la complexité d'un appel à `push`{.language-} ou à `len`{.language-} vaut invariablement $\mathcal{O}(1)$, on en conclut que la complexité totale recherchée vaut :

$$
C = \mathcal{O}(m' + m'') + \mathcal{O}(m'') + \mathcal{O}(m - m' - m'') = \mathcal{O}(m + m'') = \mathcal{O}(m)
$$

Cette complexité est bien inférieure à notre première estimation de la complexité (qui valait $\mathcal{O}(m^2)$). La complexité amortie d'une opération est ainsi de : $\frac{C}{m} = \mathcal{O}(1)$. Le coût amorti d'une opération `k-pop`{.language-}, `push`{.language-} ou `len`{.language-} est constant, sans distinction de l'opération !

## Méthode comptable

La méthode comptable va associer des coûts différents à chaque opération, appelé _coût amorti_ :

{% note %}
La **_méthode comptable_** pour calculer la complexité totale de $m$ exécutions successives d'un même algorithme consiste à associer à la $i$ème exécution de coût réel $c_i$ un **_coût amorti_** $\hat{c_i}$ tel que pour tout $1 \leq k \leq m$ :

$$
\sum_{i=1}^{k} \widehat{c_i} \geq \sum_{i=1}^{k} {c_i}
$$

L'inégalité ci-dessus assure que la complexité totale des $m$ exécutions de l'algorithme sera bien inférieure à la somme des $m$ coûts amortis.
{% endnote %}

Lorsque l'on utilise la méthode comptable, l'astuce est de choisir certains coûts supérieur au coût réel et certains coûts inférieur : certaines opérations sont crédités d'un coût additionnel qui sera débité lors d'opérations futures. Il faut cependant toujours s'assurer d'avoir un crédit suffisant pour payer les coûts futurs.

### <span id="compteur-comptable"></span> Exemple du compteur

La complexité totale à calculer est égale au nombre de bits modifiés. Or un bit n'est mit à 0 que s'il a été mis à 1 à une étape précédente. On peut donc donner comme coût amorti :

- 2 lorsqu'un bit est positionné à 1 (on compte son coût de positionnement à 1 **et** on crédite directement son coût de positionnement à 0)
- 0 lorsqu'un bit est positionné à 0

Ces coûts amortis assurent que la somme des $k$ premiers coûts amorti est supérieur à la somme réelle des $k$ coûts.

Enfin, comme à chaque exécution de `successeur`{.language-} un unique bit est mis à 1, on en conclut que le coût amorti d'une exécution de successeur est 2. Le coût amorti de $m$ exécutions successives de `successeur`{.language-} est donc de $C = m$ : l'exécution de `tous(n)`{.language-} est de complexité $\mathcal{O}(2^n)$.

### <span id="pile-comptable"></span> Exemple de la pile

La complexité de `k-pop`{.language-} étant égale au nombre d'éléments supprimés de la pile, on peut inclure son coût directement à l'empilage de chaque élément. De là si on associe les coûts amortis suivants :

- 1 à l'instruction `len`{.language-}
- 2 à l'instruction `push`{.language-} (on compte son coût d'empilage **et** on crédite directement son coût de dépilage)
- 1 à l'instruction `k-pop`{.language-}

On s'assure que l'exécution de $k$ instructions successives préserve bien l'inégalité $\sum_{i=1}^{k} \widehat{c_i} \geq \sum_{i=1}^{k} {c_i}$.

Au bout de $m$ exécutions, on aura :

$$
C \leq \sum_{i=1}^{m} \widehat{c_i} \leq \sum_{i=1}^{m} 2 = 2 \cdot m = \mathcal{O}(m)
$$

## Analyse par potentiel

Cette méthode de calcul est une généralisation des deux méthodes précédentes.

{% note %}
L'**_analyse par potentiel_** calcule la complexité totale de $m$ exécutions successives d'un même algorithme consiste à associer à la $i$ème exécution de coût réel $c_i$ un **_potentiel_** $\Omega(i)$ tel que $\Omega(i) \geq \Omega(0)$ pour tout $i \geq 1$ (on prend généralement $\Omega(0) = 0$)

Le **_coût amorti_** $\widehat{c_i}$ de la $i$ème exécution est alors défini tel que :

$$
\widehat{c_i} = c_i + \Omega(i) - \Omega(i-1)
$$

L'égalité ci-dessus assure que la complexité totale des $m$ exécutions de l'algorithme sera bien inférieure à la somme des $m$ coûts amortis.

$$
\sum_{i=1}^{m} \widehat{c_i} = \sum_{i=1}^{m} ({c_i} + \Omega(i) - \Omega(i-1)) = \sum_{i=1}^{m} {c_i} + \Omega(m) - \Omega(0) \geq \sum_{i=1}^{m} {c_i}
$$

{% endnote %}

Cette technique d'analyse vient de la physique où l'on peut associer à un système une énergie potentielle, qui sera modifiée après chaque action : $\Omega(i-1)$ correspond à l'état du système avant la $i$ème opération et $\Omega(i)$ son état après cette opération, rendant compte de la modification qu'à exercé l'opération sur le système.

En informatique, le potentiel sera souvent associé à la structure de donnée générale sous-tendant l'exécution de l'algorithme (ses paramètres, ses variables, etc).

Pour utiliser cette technique de façon efficace, on va chercher à obtenir un coût amorti le plus petit possible, si possible constant, en faisant en sorte que la différence de potentiel absorbe les variations de coût réel.

### <span id="compteur-potentiel"></span> Exemple du compteur

Le nombre de bits changés à chaque exécution de successeur dépend du nombre de 1 dans la liste passée en paramètre. Prenons cette mesure comme potentiel (on a $\Omega(0) = 0$, ce qui garanti que $\Omega(i) \geq \Omega(0)$ pour tout $i$).

A chaque exécution de `successeur`{.language-} on a :

- k bits passé à 0
- 1 bit passé à 1

On en déduit que :

- la complexité d'exécution est de k + 1
- la différence de potentiel $\Omega(i) - \Omega(i-1)$ vaut $1 - k$

Le coût amorti d'une exécution de successeur vaut alors $\widehat{c_i} = c_i + \Omega(i) - \Omega(i-1) = 1 + k + (1-k) = 2$ quelque soit $i$.

on a donc :

$$
C \geq \sum_{i=1}^m \widehat{c_i} = \sum_{i=1}^m 2 = 2 \cdot m = \mathcal{O}(m)
$$

### <span id="pile-potentiel"></span> Exemple de la pile

La seule opération ayant un coût variable est `k-pop`{.language-} et il dépend du nombre d'éléments à _poper_, c'est à dire indirectement au nombre d'élément dans la pile.

On choisi donc d'associer le potentiel à la structure de donnée pile : $\Omega(i)$ sera le nombre d'élément dans la pile après l'exécution de l'instruction $i$. Comme la pile est initialement vide on a bien $\Omega(i) \geq \Omega(0)$ pour tout $i$. Le coût amorti de chaque opération est alors :

- le coût amorti de `len`{.language-} est $1$ puisque la pile de change pas $\Omega(i) = \Omega(i - 1)$
- le coût amorti de `push`{.language-} est $2$ puisque le coût réel est 1 et la pile à un élément de plus après l'opération ($\Omega(i) = \Omega(i - 1) + 1$)
- le coût amorti de `k-pop`{.language-} est $1$ puisque le coût réel est de $1 + k$ et la pile à $k$ éléments de moins après l'opération ($\Omega(i) = \Omega(i - 1) - k$)

Le coût amorti peut être borné par 2 pour chaque opération, on a donc :

$$
C \geq \sum_{i=1}^m \widehat{c_i} \leq \sum_{i=1}^m 2 = 2 \cdot m = \mathcal{O}(m)
$$


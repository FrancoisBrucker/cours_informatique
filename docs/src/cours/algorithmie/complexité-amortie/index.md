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

Par l'exemple lors de l'utilisation de structures complexes où les instructions coûteuses ne sont faites qu'un petit nombre de fois lorsque l'on exécute la méthode plusieurs fois (comme pour [les listes](../structure-liste){.interne} par exemple).

Ce n'est **pas** une complexité en moyenne, c'est un moyen de calculer des complexités (maximum)

{% lien %}
<https://www.youtube.com/watch?v=3MpzavN3Mco>
{% endlien %}

## Définitions

Si lors de l'exécution d'un algorithme $A$, une opération $O$ (ou une fonction) de celui-ci se répète plusieurs fois et que sa
complexité diffère selon les appels, le calcul de la complexité de $A$ va nécessiter une analyse fine de de **toutes** les exécutions de l'opération $O$ car borner la complexité par le maximum conduit (souvent) à surestimer grandement la complexité réelle.

{% note "**Définition**" %}
L'**_analyse amortie_** est regroupe un ensemble des techniques permettant de calculer globalement la complexité maximale $C$ de $m$ exécutions successives d'un algorithme.

La **_complexité amortie_** de cet algorithme est alors $\frac{C}{m}$.
{% endnote %}
{% attention %}
Il ne faut pas le confondre avec la complexité en moyenne, c'est bien $m$ fois la complexité maximale que l'on considère lorsque l'on effectue les opération successivement.
{% endattention %}

La complexité amortie est une moyenne de complexité maximale, ce n'est **pas** [une complexité en moyenne](../complexité-moyenne){.interne} qui est une moyenne probabiliste. Lors d'un calcul de complexité amortie on connaît les paramètres de chaque exécution alors qu'il ne sont connu qu'en probabilité pour un complexité en moyenne.

Le temps moyen d'exécution pourra être supérieur à la complexité en moyenne si on a pas de chance alors qu'il ne pourra **jamais** excéder la complexité amortie.

{% note "**À retenir**" %}

Pour des structures de données utilisées (très) souvent, on utilise la complexité amortie dans les calculs de complexités maximales.

Pour ces structures, complexité amortie et maximale sont par abus de langage considérés comme équivalentes.

{% endnote %}

La complexité amortie est un concept avancé, utilisée dans deux cas principalement :

- comme synonyme de complexité maximale pour des structures de données très utilisées (celui que vous verrez le plus souvent)
- comme moyen de calcul de complexité pour des algorithmes dont les boucles ou les exécutions successives ont des complexités très différentes

Pour illustrer ces techniques d'analyse amortie nous allons utiliser deux exemples (ultra classiques) : le compteur binaire et une pile dépilant plusieurs éléments à la fois.

Ces deux exemples sont paradigmatiques de l'analyse amortie où une même opération peut avoir une complexité très faible ou très importante selon les cas. Une analyse fine de la complexité montrera que dans l'exécution globale de l’algorithme ces complexités sont liées et qu'une opération de complexité importante sera forcément suivie de c'opérations de faibles complexité.

## <span id="compteur-binaire"></span>Exemple du compteur binaire

Dans ce problème on encode un nombre binaire de $n$ bits par un tableau $N$ de taille $n$. Pour $n=3$ par exemple, $N = [0, 0, 1]$ correspondra à $n=1$ et $N = [1, 1, 0]$ à $n=6$.

Soit lors l'algorithme suivant :

```pseudocode/
algorithme successeur(N: [entier]) → vide:
    i ← N.longueur - 1

    tant que (i ≥ 0) ET (N[i] == 1):
        N[i] ← 0
        i ← i - 1

    si i ≥ 0:
        N[i] ← 1
```

{% details "code python" %}

```python
def successeur(N):
    i = len(N) - 1

    while (i >= 0) and (N[i] == 1):
        N[i] = 0
        i -= 1

    if i >= 0:
        N[i] = 1
```

{% enddetails %}

À un nombre `N`{.language-} écrit au format binaire donné, `successeur(N)`{.language-} va l'incrémenter de 1.

On reverra ce problème dans [la partie exercice](../projet-classiques/compteur-binaire/){.interne} où l'on calculera la complexité maximale, minimale et en moyenne d'une de ses exécutions. Nous allons ici calculer la complexité de l'algorithme suivant qui affiche tous les entiers :

```pseudocode
algorithme tous(n) → vide:

    N ← un tableau de taille n
    N[:] ← 0

    pour chaque i de [0, 2^n[:        
        successeur(N)
        affiche N à l'écran
        
```

{% details "code python" %}

```python
def tous(n):

    N = [0] * n

    for i in range(2 ** n):
        successeur(N)
        print(N)
```

{% enddetails %}

La complexité de l'exécution `tous(n)`{.language-} dépend de $2^n$ exécutions successives de l'algorithme `successeur(N)`{.language-}.

{% note "**Problème**" %}
Trouver la complexité de l'exécution `tous(n)`{.language-}, qui consiste en l'exécution $2^n$ exécutions successives de l'algorithme `successeur(N)`{.language-}.

{% endnote %}

La difficulté du calcul vient du fait que le nombre d'opération effectuée par l'exécution de `successeur(N)`{.language-} dépend de son paramètre :

- au mieux, $N[-1] = 0$ et la complexité de `successeur(N)`{.language-} est $\mathcal{O}(1)$,
- au pire, $N = [1, \dots, 1]$ et la complexité de `successeur(N)`{.language-} est $\mathcal{O}(n)$,

La complexité totale de l'exécution des $2^n$ instances de `successeur(N)`{.language-} est alors estimée à : $\mathcal{O}(n \cdot 2^n)$.

On le démontrera précisément mais on peut intuitivement voir que cette borne surestime grandement la complexité réelle car si lors d'une exécution de l'algorithme `successeur(N)`{.language-}, $N[-1] = 1$ alors lors de l'exécution suivante on aura $N[-1] = 0$. La complexité de `successeur(N)`{.language-} ne peut donc être importante qu'au pire une fois sur deux.

## Analyses

Il existe trois types d'analyses amortie possibles : par agrégat, comptable et par potentiel. La méthode par potentielle est la plus générale mais également la plus ardue à mettre en oeuvre. La méthode comptable est intermédiaire et la méthode par agrégat (que l'on a déjà utilisé pour les listes) est la méthode la plus simple et qui est souvent suffisante.

Pour l'exemple de l'algorithme `tous`{.language-}, l'analyse par agrégat suffit, mais on montrera aussi comment les résoudre avec la méthode comptable et par potentiel. Le résultat sera bien sur le même : $\mathcal{O}(2^n)$

### Analyse par Agrégat

{% note %}
La technique de **_l'analyse par agrégat_** consiste à considérer l'ensemble des $m$ exécutions comme un **tout**.

On évalue la complexité des $m$ opérations en même temps, sans distinguer les différentes opérations.
{% endnote %}

### <span id="compteur-agrégat"></span>Calcul de la complexité de l'algorithme `tous(n)`{.language-} avec l'analyse par agrégats

On remarque tout d'abord que le nombre d'opérations de `successeur(N)`{.language-} dépend de l'indice du dernier `0`{.language-} dans la liste `N`{.language-} :

- si `N`{.language-} finit par la liste `[0]`{.language-} il faut de l'ordre de 1 opération à successeur (la boucle `tant que`{.language-} de la ligne 4 fait un test et aucune itération)
- si `N`{.language-} finit par la liste `[0, 1]`{.language-} il faut de l'ordre de 2 opérations à successeur (la boucle `tant que`{.language-} de la ligne 4 fait une itération)
- si `N`{.language-} finit par la liste `[0, 1, 1]`{.language-} il faut de l'ordre de 3 opérations à successeur (la boucle `tant que`{.language-} de la ligne 4 fait deux itérations)
- ...
- si `N`{.language-} finit par la liste `[0] + [1] * i`{.language-} il faut de l'ordre de $i+1$ opérations à successeur
- ...
- si `N`{.language-} finit par la liste `[0] + [1] * (n-1)`{.language-} il faut de l'ordre de $n$ opérations à successeur
- si `N`{.language-} finit par la liste `[1] + [1] * (n-1)`{.language-} il faut de l'ordre de $n$ opérations à successeur

On peut partitionner l'ensemble des $2^n$ nombres binaires à $n$ bits en $n$ ensembles disjoints :

1. $\mathcal{N}_1$ tous les nombres qui finissent par `0`. Il y en a $\frac{2^n}{2}$
2. $\mathcal{N}_2$ tous les nombres qui finissent par `01`. Il y en a $\frac{2^n}{2^2}$
3. ...
4. $\mathcal{N}_i$ tous les nombres qui finissent par `0` suivi de (i-1) `1`. Il y en a $\frac{2^n}{2^i}$
5. $\mathcal{N}_n$ tous les nombres qui finissent par `0` suivi de (n-1) `1`. Il y en a $\frac{2^n}{2^n}$
6. $\mathcal{N}'_{n}$ contenant le nombre ne contenant que des `1`. Il y en a 1

Il faudra de l'ordre de $i$ opérations à `successeur(N)`{.language-} pour traiter un nombre de $\mathcal{N}_i$ et $n$ opérations pour traiter l'élément de $\mathcal{N}'_n$. Comme on a partitionné l'ensemble de toutes les entrées possibles et que notre algorithme va les utiliser tous une unique fois, on en conclut que la complexité totale de l'algorithme `tous(n)`{.language-} est :

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

### Méthode comptable

La méthode comptable va associer des coûts différents à chaque opération, appelé _coût amorti_ :

{% note %}
La **_méthode comptable_** pour calculer la complexité totale de $m$ exécutions successives d'un même algorithme consiste à associer à la $i$ème exécution de coût réel $c_i$ un **_coût amorti_** $\hat{c_i}$ tel que pour tout $1 \leq k \leq m$ :

$$
\sum_{i=1}^{k} \widehat{c_i} \geq \sum_{i=1}^{k} {c_i}
$$

L'inégalité ci-dessus assure que la complexité totale des $m$ exécutions de l'algorithme sera bien inférieure à la somme des $m$ coûts amortis.
{% endnote %}

Lorsque l'on utilise la méthode comptable, l'astuce est de choisir certains coûts supérieur au coût réel et certains coûts inférieur : certaines opérations sont crédités d'un coût additionnel qui sera débité lors d'opérations futures. Il faut cependant toujours s'assurer d'avoir un crédit suffisant pour payer les coûts futurs.

### <span id="compteur-comptable"></span>Calcul de la complexité de l'algorithme `tous(n)`{.language-} avec la méthode comptable

Appliquons cette méthode au compteur. La complexité totale à calculer est égale au nombre de bits modifiés. Or un bit n'est mit à 0 que s'il a été mis à 1 à une étape précédente. On peut donc donner comme coût amorti :

- 2 lorsqu'un bit est positionné à 1 (on compte son coût de positionnement à 1 **et** on crédite directement son coût de positionnement à 0)
- 0 lorsqu'un bit est positionné à 0

Ces coûts amortis assurent que la somme des $k$ premiers coûts amorti est supérieur à la somme réelle des $k$ coûts.

Enfin, comme à chaque exécution de `successeur`{.language-} un unique bit est mis à 1, on en conclut que le coût amorti d'une exécution de successeur est 2. Le coût amorti de $m$ exécutions successives de `successeur`{.language-} est donc de $C = m$ : l'exécution de `tous(n)`{.language-} est de complexité $\mathcal{O}(2^n)$.

### Analyse par potentiel

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

Cette technique d'analyse vient de la physique où l'on peut associer à un système une énergie potentielle, qui sera modifiée après chaque action : $\Omega(i-1)$. Cette énergie potentielle $\Omega(i-1)$ correspond à l'état du système avant la $i$ème opération et $\Omega(i)$ son état après cette opération, rendant compte de la modification qu'à exercé l'opération sur le système.

En informatique, le potentiel sera souvent associé à la structure de donnée sous-tendant l'exécution de l'algorithme (ses paramètres, ses variables, etc).

Remarquez que toute mesure de potentielle fonctionne si $\Omega(i) \geq \Omega(0)$ pour tout $i \geq 1$, mais que pour être efficace, on va chercher à obtenir un coût amorti le plus petit possible, si possible constant. Ce faisant, la différence de potentiel absorbera les variations de coût réel sans trop les surévaluer.

### <span id="compteur-potentiel"></span>Calcul de la complexité de l'algorithme `tous(n)`{.language-} avec l'analyse par potentiel

Le nombre de bits changés à chaque exécution de successeur dépend du nombre de 1 dans la liste passée en paramètre. Comme $\Omega(0) = 0$, on garanti que $\Omega(i) \geq \Omega(0)$ pour tout $i$, c'est une mesure de potentiel correct.

A chaque exécution de `successeur`{.language-} on a :

- k bits passés à 0
- 1 bit passé à 1

On en déduit que :

- la complexité d'exécution est de k + 1
- la différence de potentiel $\Omega(i) - \Omega(i-1)$ vaut $1 - k$

Le coût amorti d'une exécution de successeur vaut alors $\widehat{c_i} = c_i + \Omega(i) - \Omega(i-1) = 1 + k + (1-k) = 2$ quelque soit $i$.

On a donc que, encore une fois, la complexité de l'algorithme `tous(n)`{.language-} est :

$$
C \leq \sum_{i=1}^m \widehat{c_i} = \sum_{i=1}^m 2 = 2 \cdot m = \mathcal{O}(m) = \mathcal{O}(2^n)
$$

## Complexité amortie d'un compteur

La complexité de l'algorithme `successeur`{.language-} est en $\mathcal{O}(N.\mbox{\small longueur})$. Exécuter $m$ fois cet algorithme va donc être de complexité $\mathcal{O}(m\cdot N.\mbox{\small longueur})$ si on ne connaît pas le paramètre $N$ (on peut tout le temps choisir celui qui à une complexité maximale).

En revanche, considérons la structure suivante :

```pseudocode
structure Compteur:
    attributs
        N: [entier]
    création(n: entier) → Compteur:
        N ← un tableau de n entiers
        N[:] ← 0
    suivant() → vide:
        successeur(N)
```

Analysons la complexité de la méthode `suivant`{.language-} :

1. elle n'a pas de paramètre
2. une exécution peut prendre $\mathcal{O}(N.\mbox{\small longueur})$ opérations
3. pour 2 exécutions successives, la complexité de la seconde exécution dépend de l'exécution précédente (si N[-1] à été mis à 1 ou à 0)

Si un programme utilise $m$ fois la méthode `suivant`{.language-}, la complexité de ces $m$ exécutions va être égale à $\frac{m}{2^n}$ fois la complexité de `tous`{.language-}, c'est à dire $\mathcal{O}(m)$. On en déduit que :

{% note %}
La complexité amortie de la méthode `suivant`{.language-} est $\mathcal{O}(1)$.

Lorsqu'un programme utilise de nombreuses fois la méthode `suivant`{.language-}, on peut considérer que la complexité d'un appel vaut sa complexité amortie : $\mathcal{O}(1)$.
{% endnote %}

La complexité amortie est **une moyenne de complexités maximales** et permet un calcul plus aisé de la complexité : la complexité de tous les appels vaut le nombre d'appels fois la complexité amortie.

Attention, ce n'est pas une complexité en moyenne, la complexité des lignes 2 à 4 de l'algorithme suivant est $\cdot \mathcal{O}(m\cdot n)$ puisque $N$ peut contenir la suite $[1, 1, \dots, 1]$ :

```pseudocode/
N ← un tableau de m * n nombres 0 ou 1
pour chaque i de [0, m[:
    successeur(N[i * n: i * n + m])
    afficher N[i * n: i * n + m] à l'écran
```

Alors que la complexité des lignes 2 à 4 de l'algorithme suivant vaut $\cdot \mathcal{O}(m)$ :

```pseudocode/
c ← un nouveau compteur
pour chaque i de [0, m[:
    c.suivant()
    afficher c.N
```

Enfin, remarquez que la complexité amortie de `suivant` ne dépend par de la longueur de l'attribut $N$.

{% info %}
Réfléchissez à ce résultat, il est assez surprenant, non ?.
{% endinfo %}

## Exemple 2 : la pile

On va considérer [une pile](../structure-flux/pile/){.interne} et on crée l'algorithme suivant : `k-pop(k, P)`{.language-} :

```pseudocode
algorithme k-pop(k, P) → entier:
    k ← min(k, P.nombre())
    répéter k fois:
        x ← P.dépiler()
    rendre x
```

Si $k = 0$ ou `P`{.language-} est vide la complexité de `k-pop(k, P)`{.language-} est $\mathcal{O}(1)$ et sinon elle est — clairement — de $\mathcal{O}(\min(k, \mbox{len}(P)))$. On peut donc dire que la complexité de `k-pop(k, P)`{.language-} est de $\mathcal{O}(1 + \min(k, \mbox{len}(P)))$ pour tous $k$ et `P`{.language-}.

Soit $A$ un algorithme utilisant une pile $P$ via ses méthodes `nombre`{.language-} et `empiler`{.language-} et via la fonction `k-pop`{.language-}. On suppose que l'algorithme effectue $m$ de ces opérations pendant son exécution.

{% exercice "**Problème**" %}
Quelle est la complexité totale de ces $m$ opérations pour $A$ ?
{% endexercice %}

### Borner la complexité

La difficulté du calcul vient du fait que la complexité de la fonction `k-pop`{.language-} n'est pas constante. Bornons-là. On a effectué $m$ opérations, la taille maximale de la pile est donc de $m-1$ (si on a effectué $m-1$ opérations `empiler`{.language-} avant de la vider entièrement avec une instruction `k-pop`{.language-}) : la complexité de `k-pop`{.language-} est bornée par $\mathcal{O}(m)$.

On en conclut que la complexité de l'utilisation de la pile $P$ par l'algorithme $A$ est bornée par $m$ fois la complexité maximale des opérations `nombre`{.language-}, `empiler`{.language-} et `k-pop`{.language-} donc $\mathcal{O}(m^2)$.

On le démontrera précisément ci-après, mais on peut intuitivement voir que cette borne surestime grandement la complexité réelle :

- Pour que `k-pop`{.language-} ait une complexité de $\mathcal{O}(m)$, il faut avoir $\mathcal{O}(m)$ opérations `empiler`{.language-} avant. On ne peut donc pas avoir beaucoup d'opérations `k-pop`{.language-} avec cette grande complexité.
- Après une exécution de `k-pop`{.language-} avec une complexité de $\mathcal{O}(m)$, la pile est vide. Les exécutions suivante de `k-pop`{.language-} seront de complexité très faible.

### <span id="pile-agrégat"></span> Analyse par agrégat

Au cours des $m$ exécutions, on peut considérer ue l'on a fait appel :

- $m'$ fois à la fonction `k-pop`{.language-},
- $m''$ fois à la fonction `empiler`{.language-},
- $m - m' - m''$ fois à la fonction `nombre`{.language-}.

Le nombre total d'éléments dépilés au cours des $m'$ exécutions de la fonction `k-pop`{.language-} ne peut excéder le nombre total $m''$ d'éléments empilés. La complexité totale des $m'$ exécutions de `k-pop`{.language-} vaut donc $\mathcal{O}(m' + m'')$.

Comme la complexité d'un appel à `empiler`{.language-} ou à `nombre`{.language-} vaut invariablement $\mathcal{O}(1)$, on en conclut que la complexité totale recherchée vaut :

$$
C = \mathcal{O}(m' + m'') + \mathcal{O}(m'') + \mathcal{O}(m - m' - m'') = \mathcal{O}(m + m'') = \mathcal{O}(m)
$$

Cette complexité est bien inférieure à notre première estimation de la complexité (qui valait $\mathcal{O}(m^2)$).

### <span id="pile-comptable"></span> Méthode comptable

La complexité de `k-pop`{.language-} étant égale au nombre d'éléments supprimés de la pile, on peut inclure son coût directement à l'empilage de chaque élément. De là si on associe les coûts amortis suivants :

- 1 à l'instruction `nombre`{.language-}
- 2 à l'instruction `empiler`{.language-} (on compte son coût d'empilage **et** on crédite directement son coût de dépilage)
- 1 à l'instruction `k-pop`{.language-}

On s'assure que l'exécution de $k$ instructions successives préserve bien l'inégalité $\sum_{i=1}^{k} \widehat{c_i} \geq \sum_{i=1}^{k} {c_i}$.

Au bout de $m$ exécutions, on aura :

$$
C \leq \sum_{i=1}^{m} \widehat{c_i} \leq \sum_{i=1}^{m} 2 = 2 \cdot m = \mathcal{O}(m)
$$

### <span id="pile-potentiel"></span> Potentiel

La seule opération ayant un coût variable est `k-pop`{.language-} et il dépend du nombre d'éléments à dépiler, c'est à dire indirectement au nombre d'élément dans la pile.

On choisi donc d'associer le potentiel à la structure de donnée pile : $\Omega(i)$ sera le nombre d'élément dans la pile après l'exécution de l'instruction $i$. Comme la pile est initialement vide on a bien $\Omega(i) \geq \Omega(0)$ pour tout $i$. Le coût amorti de chaque opération est alors :

- le coût amorti de `nombre`{.language-} est $1$ puisque la pile de change pas $\Omega(i) = \Omega(i - 1)$
- le coût amorti de `empiler`{.language-} est $2$ puisque le coût réel est 1 et la pile à un élément de plus après l'opération ($\Omega(i) = \Omega(i - 1) + 1$)
- le coût amorti de `k-pop`{.language-} est $1$ puisque le coût réel est de $1 + k$ et la pile à $k$ éléments de moins après l'opération ($\Omega(i) = \Omega(i - 1) - k$)

Le coût amorti peut être borné par 2 pour chaque opération, on a donc :

$$
C \leq \sum_{i=1}^m \widehat{c_i} \leq \sum_{i=1}^m 2 = 2 \cdot m = \mathcal{O}(m)
$$

### Complexité amortie

Remarquer que pour l'algorithme $A$ on a pas fait attention :

- à l'ordre dans lequel les opérations ont été effectuées
- aux paramètres des opérations

De là, calculer une complexité amortie a un sens. La complexité totale des appels des 3 opérations vaut $\mathcal{O}(m)$. La complexité amortie d'une opération vaut alors : $\frac{1}{m} \cdot \mathcal{O}(m) = \mathcal{O}(1)$.

{% note %}

On peut utiliser cette complexité amortie pour calculer la complexité d'un programme utilisant ces 3 opérations.

{% endnote %}

Comme pour le compteur, remarquez que la complexité amortie de la fonction `k-pop` ne dépend pas de $k$ puisque'elle est en temps constant.

{% info %}
Réfléchissez à ce résultat, il est assez surprenant, non ?.
{% endinfo %}

## Exercices

### Potentiel

> TBD exo 4 <https://www.irif.fr/~francoisl/DIVERS/m1algo-td11-2324.pdf>

### File et pile

> complexité amortie file avec 2 piles : <https://www.irif.fr/~francoisl/DIVERS/m1algo-td11-2223.pdf>

### Ajout et suppression dans une liste

> faire un mix avec 8.2 : <https://www.di.ens.fr/~fouque/articles/poly-algo.pdf> avec comptage et potentiel pour l'ajout simple.

> TBD à faire (dire que c'est dur)

<div id="preuve-liste-suppression-ajout"></div>
{% note %}
$N$ utilisations successives des méthodes d'ajout ou de suppression du dernier élément d'une liste prend $\mathcal{O}(N)$ opérations au maximum.
{% endnote %}
{% details "preuve" %}

> TBD le faire.

{% enddetails %}

### Ajout et suppression dans série de listes triées

> TBD pas évident de pourquoi on fait ça : ie réduire le coup d'insertion. Reprendre l'idée du compteur.
> exercice 3 : <https://perso.ens-lyon.fr/laureline.pinault/Algo1/TD06-correction.pdf>

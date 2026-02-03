---
layout: layout/post.njk

title: Complexité amortie

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La complexité amortie est une moyenne de complexité maximale, ce n'est **pas** [une complexité en moyenne](../../complexité-moyenne){.interne} qui est une moyenne probabiliste.

De plus, lors d'un calcul de complexité amortie on connaît les paramètres de chaque exécution alors qu'il ne sont connu qu'en probabilité pour un complexité en moyenne.

Enfin, Le temps moyen d'exécution pourra être supérieur à la complexité en moyenne si on a pas de chance alors qu'il ne pourra **jamais** excéder la complexité amortie.

{% attention2 "**À retenir**" %}

Pour des structures de données utilisées (très) souvent, on utilise la complexité amortie dans les calculs de complexités maximales.

Pour ces structures, complexité amortie et maximale sont par abus de langage considérés comme équivalentes.

{% endattention2 %}

La complexité amortie est un concept avancé, utilisée dans deux cas principalement :

- comme synonyme de complexité maximale pour des structures de données très utilisées (celui que vous verrez le plus souvent)
- comme moyen de calcul de complexité pour des algorithmes dont les boucles ou les exécutions successives ont des complexités très différentes

## Exemple 1 : structure de compteur

Pour illustrer le concept de complexité amortie dans le cadre [du compteur binaire](../analyse/#algorithme-compteur-binaire){.interne}, calculer la complexité amortie de l'algorithme `tous`{.language-} ou de la a fonction `successeur`{.language-} n'a pas vraiment de sens :

- l'algorithme `tous`{.language-} a toujours la même complexité à chaque appel,
- la fonction `successeur`{.language-} a bien des complexités différentes selon ses paramètres, mais plusieurs appels successifs peuvent tous avoir la complexité maximale (on prend $N = [1, ..., 1]$ comme paramètre à chaque fois) et la complexité amorties sera égale à la complexité maximale

En revanche, considérons la structure suivante :

<span id="structure-compteur-binaire"></span>

```pseudocode
structure Compteur:
    attributs
        N: [bit]
    méthodes
        fonction suivant() → vide:
            successeur(N)
```

La méthode `suivant`{.language-} n'a pas de paramètres, analysons sa complexité amortie en l'exécutant successivement $m$ fois.

Par exemple le code suivant :

```pseudocode
c ← { N: [1, 0, 0, 1]}

pour chaque i de [1 .. 9]:
    c.suivant()
```

Va afficher à l'écran les valeurs de N suivantes après chaque itération (on a mis des rond autour de l'indice maximum parcouru par l'algorithme suivant):

```text
       : 1001
     1 : 0➀01
     2 : ➀101
     3 : 00➀1
     4 : ➀011
     5 : 0➀11
     6 : ➀111
     7 : 000⓪
     8 : ➀000
     9 : 0➀00

```

On voit clairement $N[i]$ est parcouru par la méthode suivant toutes les $2^i$ itérations. [L'analyse par agrégat](../analyses/#méthode-agrégat){.interne} nous indique alors que la complexité des $m$ itérations est :

<div>
$$
\sum_{0\leq i\leq log_2(m)} \mathcal{O}(1)\cdot2^i = \mathcal{O}(1)
$$
</div>

Puisque ([on l'a vu](../../projet-sommes-classiques/)) $\sum_{0\leq i \leq n}2^i = 2^{n+1}-1$ cette complexité totale vaut : $\mathcal{O}(m)$ et la complexité amortie $\frac{\mathcal{O}(m)}{m} = $\mathcal{O}(1)$ "

{% note %}
La complexité amortie de la méthode `suivant`{.language-} est $\mathcal{O}(1)$.

Lorsqu'un programme utilise de nombreuses fois la méthode `suivant`{.language-}, on peut considérer que la complexité d'un appel vaut sa complexité amortie : $\mathcal{O}(1)$.
{% endnote %}

La complexité amortie est **une moyenne de complexités maximales** et permet un calcul plus aisé de la complexité : la complexité de tous les appels vaut le nombre d'appels fois la complexité amortie.

Enfin, remarquez que la complexité amortie de `suivant` ne dépend par de la longueur de l'attribut $N$.

{% info %}
Réfléchissez à ce résultat, il est assez surprenant, non ?.
{% endinfo %}

## Exemple 2 : la pile

On modifie [la structure pile](../../structure-pile-file/pile/#structure-pile){.interne} pour y ajouter la méthode suivante: `k-dépile(k: entier) → Type`{.language-} :

```pseudocode
fonction k-dépile(k: entier) → Type:
    k ← min(k, nombre())
    répéter k fois:
        x ← dépile()
    rendre x
```

Si $k = 0$ ou la pile $P$ est vide, la complexité de `k-dépile`{.language-} est $\mathcal{O}(1)$ et sinon elle est — clairement — de $\mathcal{O}(\min(k, P.\text{nombre()}))$. La complexité de `k-dépile`{.language-} est ainsi de $\mathcal{O}(1 + P.\text{nombre()})$.

Soit $A$ un algorithme utilisant notre nouvelle pile $P$ via ses méthodes `nombre`{.language-} (de complexité $\mathcal{O}(1)$), `empile`{.language-} (de complexité $\mathcal{O}(1)$) et via la fonction `k-dépile`{.language-} (de complexité $\mathcal{O}(1 + P.\text{nombre()})$). On suppose que l'algorithme effectue $m$ de ces 3 méthodes pendant son exécution et que la somme de ses autres opérations est en $\mathcal{O}(1)$.

{% exercice %}
Quelle est la complexité totale de ces $m$ exécutions des 3 méthodes pour $A$ ?
{% endexercice %}

### Borner la complexité

La difficulté du calcul vient du fait que la complexité de la fonction `k-dépile`{.language-} n'est pas constante. Bornons-là. On a effectué $m$ opérations, la taille maximale de la pile est donc de $m-1$ (si on a effectué $m-1$ opérations `empile`{.language-} avant de la vider entièrement avec une instruction `k-dépile`{.language-}) : la complexité de `k-dépile`{.language-} est bornée par $\mathcal{O}(m)$.

On en conclut que la complexité de l'utilisation de la pile $P$ par l'algorithme $A$ est bornée par $m$ fois la complexité maximale des opérations `nombre`{.language-}, `empile`{.language-} et `k-dépile`{.language-} donc $\mathcal{O}(m^2)$.

On le démontrera précisément ci-après, mais on peut intuitivement voir que cette borne surestime grandement la complexité réelle :

- Pour que `k-dépile`{.language-} ait une complexité de $\mathcal{O}(m)$, il faut avoir $\mathcal{O}(m)$ opérations `empile`{.language-} avant. On ne peut donc pas avoir beaucoup d'opérations `k-dépile`{.language-} avec cette grande complexité.
- Après une exécution de `k-dépile`{.language-} avec une complexité de $\mathcal{O}(m)$, la pile est vide. Les exécutions suivante de `k-dépile`{.language-} seront de complexité très faible.

Calcul de la complexité amortie. Pour cela, on commence par calculer la complexité des $m$ exécutions en utilisant [la méthode comptable](../analyses/#méthode-comptable){.intene}.

La complexité de `k-dépile`{.language-} étant égale au nombre d'éléments supprimés de la pile, on peut inclure son coût directement à l'empilage de chaque élément. De là si on associe les coûts amortis suivants :

- 1 à l'instruction `nombre`{.language-}
- 2 à l'instruction `empile`{.language-} (on compte son coût d'empilage **et** on crédite directement son coût de dépilage)
- 0 à l'instruction `k-dépile`{.language-}

On s'assure que l'exécution de $k$ instructions successives préserve bien l'inégalité $\sum_{i=1}^{k} \widehat{c_i} \geq \sum_{i=1}^{k} {c_i}$.

Au bout de $m$ exécutions, on aura :

$$
C \leq \sum_{i=1}^{m} \widehat{c_i} \leq \sum_{i=1}^{m} 2 = 2 \cdot m = \mathcal{O}(m)
$$

Remarquer que pour l'algorithme $A$ on a pas fait attention :

- à l'ordre dans lequel les opérations ont été effectuées
- aux paramètres des opérations

De là, calculer une complexité amortie a un sens. La complexité totale des appels des 3 opérations vaut $\mathcal{O}(m)$. La complexité amortie d'une opération vaut alors : $\frac{1}{m} \cdot \mathcal{O}(m) = \mathcal{O}(1)$.

{% note %}

On peut utiliser cette complexité amortie pour calculer la complexité d'un programme utilisant ces 3 opérations.

{% endnote %}

Comme pour le compteur, remarquez que la complexité amortie de la fonction `k-dépile` ne dépend pas de $k$ puisque'elle est en temps constant.

{% info %}
Réfléchissez à ce résultat, il est assez surprenant, non ?.
{% endinfo %}

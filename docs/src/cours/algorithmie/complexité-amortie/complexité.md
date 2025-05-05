---
layout: layout/post.njk

title: Complexité amortie

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD chapeau

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

On va considérer [une pile](../structure-pile-file/pile/){.interne} et on crée l'algorithme suivant : `k-pop(k, P)`{.language-} :

```pseudocode
algorithme k-pop(k, P) → entier:
    k ← min(k, P.nombre())
    répéter k fois:
        x ← P.dépiler()
    rendre x
```

Si $k = 0$ ou `P`{.language-} est vide la complexité de `k-pop(k, P)`{.language-} est $\mathcal{O}(1)$ et sinon elle est — clairement — de $\mathcal{O}(\min(k, \mbox{len}(P)))$. On peut donc dire que la complexité de `k-pop(k, P)`{.language-} est de $\mathcal{O}(1 + \min(k, \mbox{len}(P)))$ pour tous $k$ et `P`{.language-}.

Soit $A$ un algorithme utilisant une pile $P$ via ses méthodes `nombre`{.language-} et `empiler`{.language-} et via la fonction `k-pop`{.language-}. On suppose que l'algorithme effectue $m$ de ces opérations pendant son exécution.

{% exercice %}
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

### <span id="exercice-liste-suppression-ajout"></span> Ajout et suppression dans une liste

> faire un mix avec 8.2 : <https://www.di.ens.fr/~fouque/articles/poly-algo.pdf> avec comptage et potentiel pour l'ajout simple.
> TBD voir aussi le poly de pascal.

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

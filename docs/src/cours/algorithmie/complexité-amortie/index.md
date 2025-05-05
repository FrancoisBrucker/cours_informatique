---
layout: layout/post.njk

title: Analyse et complexité amortie

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD Formalisation de ce que l'on a vu avec les listes. Certaines opérations n'ont pas toujours la même complexité mais la complexité importante n'arrive que rarement.


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

{% attention "**À retenir**" %}

Pour des structures de données utilisées (très) souvent, on utilise la complexité amortie dans les calculs de complexités maximales.

Pour ces structures, complexité amortie et maximale sont par abus de langage considérés comme équivalentes.

{% endattention %}

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

## Méthodes d'analyse amortie

{% aller %}
[Analyse amortie](./analyses){.interne}
{% endaller %}

## Complexité amortie

{% aller %}
[Complexité amortie](./complexité){.interne}
{% endaller %}

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

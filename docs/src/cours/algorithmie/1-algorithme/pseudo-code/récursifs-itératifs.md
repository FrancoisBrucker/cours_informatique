---
layout: layout/post.njk

title: "Algorithmes récursifs et itératifs"

eleventyComputed:  
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Il y a deux grandes familles d'algorithmes :

- les algorithmes itératifs, c'est-à-dire utilisant des boucles
- les algorithmes récursifs, c'est-à-dire écrits sous la forme d'une fonction qui s'appelle elle-même.

Tout algorithme pourra toujours s'écrire sous une forme itérative ou récursive (on va le montrer mais bien plus tard) mais certains problèmes se résolvent mieux sous une forme que sous l'autre.

Avant de définir formellement les deux approches commençons par deux remarques importantes :

{% retenir %}

Adaptation d'un algorithme aux données :

1. pour que la sortie d'un algorithme dépende de ses entrées, il est nécessaire qu'il possède des instructions conditionnelles (sinon il fera toujours la même chose),
2. pour qu'un algorithme puisse traiter des entrées de taille quelconque, il est nécessaire de répéter certaines de ses instructions (sinon il ne pourra traiter entièrement des données plus grandes que son nombre d'instructions).

**La différence entre les approches itératives et récursives est liée au traitement des deux points précédents.**

{% endretenir %}

Pour expliciter la différence entre les deux approches nous allons utiliser notre exemple fil rouge [du calcul du $\operatorname{pgcd}$](../../bases-théoriques/calculabilité/#algorithme-euclide).


## Algorithmes itératifs

{% definition %}

**Un algorithme itératif** va gérer les 2 points d'adaptation aux données en modifiant des variables locales et en utilisant des boucles `pour chaque`{.language-pseudocode} et `tant que`{.language-}. Il va avoir tendance à aller du cas particulier vers le cas général en stockant les éléments intermédiaires dans des variables.
{% enddefinition %}

Pour le calcul du $\operatorname{pgcd}$, l'algorithme itératif va tester tous les cas possibles :


<span id="algorithme-pgcd-naif"></span>

```pseudocode
algorithme pgcd(a: int, b: int) → int:  # a, b ≥ 0
    ref pgcd int

    pour chaque k de [1 .. min(a, b)]:
        si (a mod k == 0) ET (b mod k == 0):
            pgcd ← k
    
    rendre pgcd
```
{% details "code python" %}

```python
def pgcd(a, b):
    pgcd = 0
    for k in range(1, min(a, b) + 1):
        if (a % k == 0) and (b % k == 0):
            pgcd = k
    
    return pgcd
```

{% enddetails %}

Lorsque l'on construit un algorithme itératif, il faut faire attention au fait que les boucles finissent bien. C'est bien sûr toujours le cas avec les boucles de type `pour chaque`{.language-} mais pour des boucles de type `tant que`{.language-} ce n'est pas toujours évident.

## Algorithmes récursifs

{% definition %}

**Un algorithme récursif** va gérer les 2 points d'adaptation aux données en se rappelant lui-même (une **_récursion_**) avec de nouveaux paramètres d'entrée un nombre fini de fois (nécessite une **_condition d'arrêt_** pour stopper la récursion). Il va avoir tendance à aller du cas général vers le cas particulier en stockant les éléments intermédiaires dans ses paramètres d'entrée.

{% enddefinition %}

Pour le calcul du $\operatorname{pgcd}$ on va utiliser [l'algorithme binaire de Stein](https://fr.wikipedia.org/wiki/Algorithme_binaire_de_calcul_du_PGCD){.externe} :

```pseudocode/
algorithme pgcd(a: int, b: int) → int:  # a, b ≥ 0
    si min(a, b) == 0:
        rendre max(a, b)
    sinon si a == b:
        rendre a
    sinon si (a mod 2 == 0) ET (b mod 2 == 0):
        rendre 2 * pgcd(a // 2, b // 2)
    sinon si (a mod 2 == 0):
        rendre pgcd(a // 2, b)
    sinon si (b mod 2 == 0):
        rendre pgcd(a, b  // 2)
    sinon si a > b:
        rendre pgcd(a - b, b)
    sinon:
        rendre pgcd(a, b - a)
```
{% details "code python" %}

```python
def pgcd(a, b):
    if min(a, b) == 0:                     
        return max(a, b)
    elif a == b:
        return a    
    elif (a % 2 == 0) and (b % 2 == 0):
        return 2 * pgcd(a // 2, b // 2)
    elif (a % 2 == 0):
        return pgcd(a // 2, b)
    elif (b % 2 == 0):
        return pgcd(a, b  // 2)
    elif a > b:
        return pgcd(a - b, b)
    else:
        return pgcd(a, b - a)
```

{% enddetails %}

À chaque récursion soit $a$ soit $b$ ([ou les deux](https://www.youtube.com/watch?v=mIUwEoG7ssM&t=59s){.externe}) diminue strictement : à chaque itération on se rapproche donc des deux cas sans récursion qui mettent fin à l'algorithme.

Notre algorithme effectue 5 récursions avant de terminer pour calculer le pgcd entre 8 et 6 :

```text
pgcd(8, 6) = 2 * pgcd(4, 3)
                 pgcd(4, 3) = pgcd(2, 3)
                              pgcd(2, 3) = pgcd(1, 3)
                                           pgcd(1, 3) = pgcd(1, 2)
                                                        pgcd(1, 2) = pgcd(1, 1)
                                                                     pgcd(1, 1) = 1
```

Pour comprendre comment cela fonctionne il faut se rappeler qu'un algorithme passe à la ligne suivante **que** si l'instruction est terminée : lors d'une récursion l'algorithme attend que la récursion se termine pour continuer. Ainsi lors du 5e appel de récursion, il y a 5 algorithmes qui attendent :

- `pgcd(1, 2)`{.language-} attend en ligne 11 que la fonction `pgcd(1, 1)`{.language-} se termine pour continuer
- `pgcd(1, 3)`{.language-} attend en ligne 15 que la fonction `pgcd(1, 2)`{.language-} se termine pour continuer
- `pgcd(2, 3)`{.language-} attend en ligne 9 que la fonction `pgcd(1, 3)`{.language-} se termine pour continuer
- `pgcd(4, 3)`{.language-} attend en ligne 9 que la fonction `pgcd(2, 3)`{.language-} se termine pour continuer
- `pgcd(8, 6)`{.language-} attend en ligne 7 que la fonction `pgcd(4, 3)`{.language-} se termine pour continuer

Lorsque la dernière récursion s'arrête : `pgcd(1, 1)`{.language-} rend 1 sans récursion, qui permet à l'algorithme `pgcd(1, 2)`{.language-} de s'arrêter qui permet à l'algorithme `pgcd(1, 3)`{.language-} de s'arrêter qui permet à l'algorithme `pgcd(2, 3)`{.language-} de s'arrêter qui permet à l'algorithme `pgcd(4, 3)`{.language-} de s'arrêter qui permet à l'algorithme `pgcd(8, 6)`{.language-} de s'arrêter.

Notez que nous n'avons pas prouvé que le programme trouve bien le plus grand diviseur commun de deux entiers, juste qu'il se termine quelles que soient ses entrées et donc que c'est un algorithme. Démontrons-le :

{% note "**Proposition**" %}
L'algorithme binaire de Stein calcule bien le $\operatorname{pgcd}$ de deux entiers positifs donnés en paramètre.
{% endnote %}
{% details "preuve", "open" %}

L'algorithme effectue plusieurs cas que nous allons examiner :

- si `min(a, b) == 0`{.language-} : le $\operatorname{pgcd}$ est clairement $\max(a, b)$,
- si `min(a, b) > 0`{.language-} et `a == b`{.language-} : le $\operatorname{pgcd}$ est clairement $a$,
- si `a`{.language-} et `b`{.language-} sont pairs, 2 est un diviseur commun
- si seul `a`{.language-} ou `b`{.language-} est pair, 2 n'est pas un diviseur commun
- sinon, on retrouve [l'algorithme d'Euclide](../../bases-théoriques/calculabilité/#algorithme-euclide) que l'on a démontré correct.
{% enddetails %}

## <span id="récursion-terminale"></span>Récursion terminale

{% lien %}
[Récursion terminale](https://fr.wikipedia.org/wiki/R%C3%A9cursion_terminale){.externe}
{% endlien %}

La récursion terminale est un algorithme écrit sous une forme récursive pouvant facilement se mettre sous forme itérative :

{% definition %}

Soit l'algorithme `f`{.language-} suivant où `c: A → Booléen`{.language-}, `g: A → B`{.language-} et `h: A → A`{.language-} sont trois fonctions parfaitement définies :

```pseudocode

algorithme f(n: A) → B:
    si c(n) == Vrai:
        rendre g(n)
    sinon:
        rendre f(h(n))
```

L'algorithme `f`{.language-} est sous la forme d'une **_récursion terminale_**, c'est-à-dire que :

1. **soit** il s'arrête si une condition d'arrêt est vérifiée
2. **soit** il rend une récursion de lui-même

Pour que la définition de `f`{.language-} ait du sens il faut bien sûr que chaque récursion se _rapproche_ de la condition d'arrêt. C'est ce qu'il faut démontrer pour chaque algorithme sous la forme d'une récursion terminale.

{% enddefinition %}

La récursion terminale est sympathique car équivalente à la forme itérative suivante :

```pseudocode
algorithme f(n: A) → B:
    tant que c(n) est Faux:
        n ← h(n)
    rendre g(n)
```

Ce qui permet une implémentation en machine efficace (c'est ce que font les compilateurs lorsqu'ils repèrent une telle forme). 

Illustrons ceci en utilisant directement [l'algorithme d'Euclide](../../bases-théoriques/calculabilité/#algorithme-euclide) pour le calcul du $\operatorname{pgcd}$. On peut en effet écrire cet algorithme sous la forme d'une équation récurrente :

<div>
$$
\begin{equation}
  \operatorname{pgcd}(a, b) =
  \begin{cases}
    \max(a, b) & \text{si $\min(a, b) = 0$}\\
    \operatorname{pgcd}(\max(a, b) - \min(a, b), \min(a, b)) & \text{sinon}.
  \end{cases}
\end{equation}
$$
</div>

On a montré en exercice que cette équation est correcte et qu'elle se termine en un nombre fini d'étapes, c'est donc bien un algorithme qui s'écrit :

<span id="algorithme-pgcd-rec"></span>

```pseudocode
algorithme pgcd(a: int, b: int) → int:  # a, b ≥ 0
    si min(a, b) == 0:
        rendre max(a, b)
    sinon:
        rendre pgcd(max(a, b) - min(a, b), min(a, b))
```
{% details "code python" %}

```python
def pgcd(a, b):
    if min(a, b) == 0:
        return max(a, b)
    else:
        return pgcd(max(a, b) - min(a, b), min(a, b))
```

{% enddetails %}


Il est écrit sous forme terminale et est donc équivalent à l'algorithme itératif suivant :

<span id="algorithme-pgcd"></span>

```pseudocode
algorithme pgcd(a: int, b: int) → int:  # a, b ≥ 0
    tant que min(a, b) > 0:
        a, b ← max(a, b) - min(a, b), min(a, b)
    rendre max(a, b)
```

{% attention %}
Tous les algorithmes récursifs ne sont pas sous la forme terminale. Par exemple l'algorithme binaire de Stein n'est pas sous la forme récursive terminale en ligne 7.
{% endattention %}

## Récursion croisée

Une dernière utilisation de la récursion qui peut être utile est la récursion croisée qui définit une fonction par rapport à une autre et réciproquement :

<span id="algorithme-pair-impair"></span>

{% exercice %}
Écrire les deux fonctions récursives suivantes sans utiliser de division entière :

```pseudocode
algorithme pair(n: int) → bool
algorithme impair(n: int) → bool
```

Vous pourrez utiliser le fait que `pair(0)`{.language-} est `Vrai`{.language-pseudocode} alors que `impair(0)`{.language-} est `Faux`{.language-pseudocode}.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme pair(n: int) → bool
    si n == 0:
        rendre Vrai
    rendre NON impair(n - 1)

algorithme impair(n: int) → bool
    si n == 0:
        rendre Faux
    rendre NON pair(n - 1)

```

La finitude est claire puisque :

1. il n'y a qu'un appel récursif
2. chaque appel se rapproche strictement de la condition d'arrêt

La correction est évidente par définition de la parité.

{% enddetails %}

---
layout: layout/post.njk

title: "Problème algorithmique et preuve d'algorithme"

eleventyComputed:  
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un algorithme est censé faire quelque chose : à partir de données passées en entrée (ses paramètres) il va produire une sortie. Cette sortie dépend de ses paramètres et répond à une question ou plus généralement résout un problème. Définissons ceci sous la forme de "_problème_" à résoudre _via_ un algorithme.


## Problème algorithmique

{% definition %}
Un **_problème_** est un texte composé de 3 parties :

- **Nom** : le nom du problème
- **Entrées** : les paramètres dont on a besoin
- **Sortie** : la solution recherchée

{% enddefinition %}

Par exemple :

<span id="problème-max-tableau"></span>

{% note "**Problème**" %}

- **Nom** : MAX
- **Entrée** : un tableau d'entiers
- **Sortie** : l'entier maximum du tableau

{% endnote %}

Comme tout problème n'admet pas forcément un algorithme pour le résoudre (par exemple [la complexité de Kolmogorov](../bases-théoriques/calculabilité/#complexité-Kolmogorov), ["quand est-ce qu'on mange ?"](https://www.youtube.com/watch?v=w1hdRjPVejA&list=OLAK5uy_ntRz4sFNPNVhiGTyVR4VsePZzmGG7OPFM&index=11){.externe} ou encore ["le sens de la vie ?"](https://www.youtube.com/watch?v=LAwDWZoETk4){.externe}), on se restreindra ici aux problèmes algorithmiques :

<span id="problème-algorithmique"></span>

{% definition %}
**_Un problème est algorithmique_** s'il existe un algorithme pour le résoudre, c'est-à-dire que cet algorithme :

- prend en paramètres les entrées du problème
- donne en sortie la solution recherchée.

{% enddefinition %}

Il est clair qu'un problème algorithmique est [une propriété](../bases-théoriques/arrêt-rice/#définition-propriété), il n'existe donc aucun moyen automatique de savoir si un algorithme donné résout un problème : il faut le prouver à chaque fois.


## Preuve d'algorithme

{% definition %}

**_Prouver un algorithme_** $A$ c'est démontrer qu'il résout un problème $P$ (qu'il fait partie de la propriété des algorithmes résolvant $P$). Pour cela :

1. on explicitera le problème $P$ :
   - ses entrées
   - sa question
   - sa sortie
2. on démontrera que le résultat de l'exécution de $A$ avec une instance d'entrées de $P$ est bien une réponse à $P$.

{% enddefinition %}

À chaque fois que l'on nous demandera de créer un algorithme pour résoudre un problème il nous faudra :

1. s'assurer que l'on écrit un programme
2. s'assurer que ce programme s'arrête pour toute entrée (et donc que c'est un algorithme)
3. montrer qu'il résout le problème demandé.

Si l'étape 2, prouver qu'un programme s'arrête, fait partie des problèmes indécidables en général, il est souvent facile en pratique de montrer qu'un programme donné est un algorithme. En particulier les algorithmes qui résolvent des problèmes sont censés s'arrêter et il sera (normalement) facile de le voir.

{% retenir %}
Prouver qu'un programme résout un problème algorithmique nécessite deux vérifications :

- **_la finitude_** : le programme s'arrête pour toute entrée, c'est un algorithme
- **_la correction_** : sa sortie est une solution du problème

{% endretenir %}

En revanche l'étape 3, la preuve que l'algorithme fait bien ce qu'on attend de lui, est parfois plus délicate. On peut cependant donner des règles générales de preuve qui fonctionnent (souvent) pour des algorithmes récursifs ou itératifs.




Pour expliciter la différence entre les deux approches nous allons utiliser le calcul de la factorielle définie pour tout entier $n\geq 1$ telle que :

$$
n! \coloneqq \prod\limits_{1\leq i \leq n} i = 1 \times 2 \times \dots \times (n-1)\times n
$$

## Preuve d'algorithmes récursifs

Pour le calcul de la factorielle, si $(n-1)!$ est connu, $n! = n \times ((n-1)!)$, et en remarquant que l'on connaît $1!$ qui vaut $1$, on peut écrire l'équation de récurrence :

<div>
$$
n! \coloneqq \begin{cases}
1 &\text{si } n=1\\
n \cdot (n-1)! &\text{sinon }
\end{cases}
$$
</div>

Qui permet d'écrire l'algorithme récursif suivant :

<div id="algorithme-factorielle-rec"></div>

```pseudocode
algorithme factorielle(n: int     # n ≥ 1
                      ) → int:
    si n == 1:                    # condition d'arrêt
        rendre 1
    ref f ← factorielle(n-1)      # récursion
    rendre n * f
```

{% details "code python" %}

```python
def factorielle(n):
    if n == 1:
        return 1
    f = factorielle(n - 1)
    return n * f
```

{% enddetails %}


### Finitude

Un programme récursif est un algorithme s'il n'existe pas de récursion infinie :

{% retenir %}
Un programme récursif est un algorithme si quelles que soient ses entrées il n'y aura qu'un nombre fini de récursions.
{% endretenir %}


Notre programme factorielle est bien un algorithme puisque la récursion va se rapprocher strictement de sa condition d'arrêt ($n = 1$). On peut le prouver rapidement par récurrence sur $n$.

1. **initialisation** de la preuve : si $n=1$, l'algorithme va se finir sans exécuter la ligne 4, il y a un nombre fini de récursions.
2. **hypothèse de récurrence** : pour tout entier plus petit que $n-1\geq 1$, l'algorithme va avoir un nombre fini de récursions.
3. **pour $n$** : `factorielle(n)`{.language-} va exécuter la ligne 4 (`ref f ← factorielle(n-1)`{.language-}) qui, par hypothèse de récurrence, va se terminer au bout d'un nombre fini de récursions : le programme `factorielle(n)`{.language-} va également se terminer.

La preuve précédente donne un moyen simple de prouver qu'un algorithme récursif va s'arrêter :

{% retenir %}
Tout appel récursif doit se rapprocher strictement d'un état de terminaison.
{% endretenir %}

Ceci fonctionne même s'il y a plus d'un appel récursif. On peut donc simplement écrire pour prouver la convergence :

### Correction

{% retenir %}

Pour prouver un algorithme récursif on peut soit :

1. trouver une relation évidente caractérisant le but de la récursion
2. trouver une équation de récurrence plus une condition d'arrêt

{% endretenir %}

Ne vous lancez pas dans des démonstrations par récurrence interminables et besogneuses si la récursion est évidente ! Notre algorithme récursif retranscrit directement la définition récurrente de la factorielle, il est donc évidemment correct.

## Preuve d'algorithmes itératifs

Pour le calcul de la factorielle, on va commencer par calculer $1!$ puis remarquer que $(n + 1)! = (n!) \cdot (n + 1)$ :

<div id="algorithme-factorielle-iter"></div>

```pseudocode
algorithme factorielle(n: int) → int:
    ref r ← 1  # initialisation
    ref i ← 1
    tant que i ≤ n:  # condition d'arrêt
        r ← r * i
        i ← i + 1
    rendre r
```

{% details "code python" %}

```python
def factorielle(n):
    r = 1
    i = 1
    while i <= n:
        r *= i
        i += 1
    return r
```

On utilise la possibilité que donne python d'écrire `x += y`{.language-} (_resp._ `x -= y`{.language-}, `x *= y`{.language-} ou encore `x /= y`{.language-}) à la place de `x = x + y`{.language-} (_resp._ `x = x - y`{.language-}, `x = x * y`{.language-}, `x = x / y`{.language-}).

{% enddetails %}

On voit que la forme d'un algorithme itératif est inversée par rapport à un algorithme récursif.

### Finitude

Un programme itératif est un algorithme s'il n'existe pas de boucle infinie :

{% retenir %}

Un programme itératif est un algorithme s'il n'existe pas de boucle infinie. Ceci n'est possible que pour les boucles `tant que`{.language-} : il faut garantir que leurs conditions d'arrêt soient vérifiées au cours de l'exécution du programme quelles que soient ses entrées.

{% endretenir %}

Notre algorithme va forcément s'arrêter puisque $i$ croît strictement à chaque itération.




### Correction

Démontrer la correction d'un algorithme itératif est souvent plus compliqué que celle d'un algorithme récursif. Une méthode qui se révèle souvent efficace consiste à trouver des propriétés qui sont conservées à chaque itération.

{% retenir %}

Pour prouver un algorithme on cherchera à prouver ce que fait chaque boucle ou récursion. Pour cela on utilisera plusieurs techniques, par ordre de difficulté :

1. une relation évidente caractérisant le but de la boucle
2. une équation de récurrence plus une condition d'arrêt pour prouver une boucle itérative pouvant être écrite sous forme récursive
3. [un invariant de boucle](https://fr.wikipedia.org/wiki/Invariant_de_boucle){.externe}. Ces invariants vont alors être conservés jusqu'à la fin de l'algorithme et nous permettre de prouver son résultat.

{% endretenir %}

À part les recommandations ci-dessus, il n'existe pas vraiment de règles à appliquer pour prouver un algorithme. Seules l'expérience et l'étude des algorithmes classiques vous permettront de trouver facilement comment prouver un algorithme.

Nous allons montrer les 3 façons de faire avec notre algorithme.

#### Correction par relation évidente

L'algorithme suivant est une réécriture directe de la version `tant que`{.language-} de factorielle précédente :

```pseudocode
algorithme factorielle(n: int) → int:  # n ≥ 1
    ref produit ← 1
    pour chaque i de [2 .. n]:
        produit ← produit * i

    rendre produit
```

La preuve d'exactitude est alors évidente puisque l'on a juste réécrit la définition de $n!$.


#### Correction par une équation de récurrence


Nous allons montrer que l'on peut prouver notre algorithme par récurrence. Il peut en effet se réécrire de cette façon :

```pseudocode
algorithme factorielle(n: int) → int:
    ref r ← 1                 
    ref i ← 1

    tant que i ≤ n - 1:        # boucle de factorielle(n - 1)
        r ← r * i
        i ← i + 1
    
    # ici r et i sont égaux à ceux de la sortie de la boucle de factorielle(n - 1)

    r ← r * i
    i ← i + 1

    rendre r
```

On retrouve la boucle de `factorielle(n-1)`{.language-} dans `factorielle(n)`{.language-} ce qui montre que si `factorielle(n-1)`{.language-} fonctionne et rend $(n-1)!$ alors `factorielle(n)`{.language-} rendra bien $n\cdot (n-1)! = n!$. On est ramené à une preuve par récurrence, comme pour le cas récursif.

#### Correction par invariant

Lorsque l'on ne peut pas clairement et rapidement faire une preuve par récurrence, on peut chercher un invariant à la boucle : quelque chose qui est conservé à chaque itération. Cette technique de preuve n'est pas très éloignée des preuves par récurrence, elle est juste plus générale et (de l'avis des informaticiens) plus élégante.

Refaisons la preuve précédente en utilisant un invariant de boucle pour montrer comment tout ceci peut se faire :

```pseudocode
algorithme factorielle(n: int) → int:
    ref r ← 1
    ref i ← 1

    tant que i ≤ n:
        r ← r * i
        i ← i + 1
    rendre r
```

{% note "**Schéma de preuve des algorithmes itératifs par invariant :**" %}
Un invariant doit résumer ce que fait la boucle avec une équation qui est toujours vérifiée, même si on modifie des variables. Une fois l'invariant trouvé on commence par le démontrer :

 1. on vérifie que l'invariant est vrai à la fin de la première itération de la boucle
 2. on suppose l'invariant à la fin de l'itération $k$ de la boucle et on vérifie qu'il est toujours vérifié à la fin de l'itération $k + 1$.

Une fois l'invariant démontré, il va être toujours vrai, de la première itération à la sortie de la boucle. À ce moment-là, sa valeur doit servir à démontrer le résultat voulu.

Pour simplifier l'écriture, on note avec un `'` (prime) les variables à la fin de la boucle d'itération $k+1$ pour les différencier des variables de la fin de l'itération $k$.
{% endnote %}
{% info %}
Il existe des variantes dans les preuves par invariants selon que l'on vérifie juste à la fin de la boucle ou au début et à la fin de l'itération. Les deux formes sont équivalentes, mais il est parfois plus aisé d'utiliser l'une que l'autre.
{% endinfo %}

Un invariant possible est :

{% note "**Invariant**"%}

À la fin de chaque itération de l'algorithme :

<div>
$$
r = (i-1)!
$$
</div>

{% endnote %}
{% details "preuve", "open" %}
Démontrons-le :

1. c'est vrai à la fin de la 1ère itération
2. si c'est vrai à la fin de la $k$ème itération, à la fin de la $k+1$ème itération on a :
   - $r'=r \cdot i$ (le $r$ de la fin de la $k+1$ème boucle est égal à celui de la fin de la $k$ème boucle fois le $i$ de la fin de $k$ème boucle)
   - $i' = i + 1$ (le $i$ de la fin de la $k+1$ème boucle est le $i$ de la fin de la $k$ème boucle plus 1)
   - $r = (i-1)!$ (c'est notre invariant, vrai à la fin de l'itération $k$ par hypothèse)
3. on a donc : $r' = (i-1)! \cdot i = i! = (i'-1)!$ : **notre invariant est vérifié**.

{% enddetails %}
{% details "comment a-t-on trouvé l'invariant ?" %}

1. l'algorithme retourne $r$ à la fin : il doit valoir $n!$
2. $r$ est multiplié par $i$ à chaque itération
3. $i$ est incrémenté de 1 à chaque itération et commence à 1.

On doit donc avoir un invariant du type **$r \simeq i!$ à la fin de chaque itération** à _plus ou moins 1 près_. Pour en être sûr regardons ce que valent nos variables à la fin de la première itération :

- $r = 1$
- $i = 2$ (on a modifié $i$ après l'avoir multiplié par $r$)

Donc l'invariant doit certainement être $r = (i-1)!$ à la fin de chaque itération.

{% enddetails %}

L'invariant étant vérifié à la fin de chaque itération, il est donc aussi vrai à la fin de la dernière itération. À ce moment-là on a $i=n+1$ et donc $r = n!$ : notre algorithme calcule bien la factorielle de son entrée.

## Trouver des invariants de boucles


Trouver un invariant de boucle est souvent intimidant pour des débutants. Nous allons nous entraîner un peu pour acquérir quelques automatismes. L'idée principale pour trouver un invariant est de procéder par étapes :

1. comprendre l'algorithme
2. comprendre l'intérêt de la boucle le constituant (s'il y a plusieurs boucles on refait l'analyse pour chaque boucle)
3. voir comment on pourrait prouver l'algorithme
4. utiliser cette idée de preuve pour créer un invariant
5. prouver l'invariant
6. prouver la correction de l'algorithme

{% retenir %}
Trouver l'invariant est **à la fin du processus de création de la preuve**. C'est un moyen d'écrire une preuve que l'on a comprise (certainement) autrement.
{% endretenir %}


Appliquons ces recommandations sur l'algorithme itératif suivant :

<span id="algorithme-max-tableau-iter"></span>

```pseudocode
algorithme maximum(t: []int) → int:
    ref m ← t[0]
    pour chaque x de t:
        si m < x:
            m ← x
    rendre m
```

{% details "code python" %}

```python
def maximum(t):
    m = t[0]
    for x in t:
        if m < x:
            m = x
    return m
```

{% enddetails %}

### 1. Comprendre l'algorithme

L'algorithme va itérer sur chaque élément du tableau et conserver dans la variable `m`{.language-} la plus grande des valeurs vues jusqu'à présent.

### 2. Comprendre l'intérêt de la boucle le constituant (s'il y a plusieurs boucles on refait l'analyse pour chaque boucle)

Il faut parcourir tous les éléments du tableau pour connaître la plus grande des valeurs.

### 3. Voir comment on pourrait prouver l'algorithme

Il faut montrer que la variable `m`{.language-} contient la valeur maximale pour tous les éléments de `t`{.language-} vus jusqu'à présent. Comme à la fin de l'algorithme on aura vu toutes les valeurs de `t`{.language-} on aura prouvé que `m`{.language-} est bien le maximum.

### 4. Utiliser cette idée de preuve pour créer un invariant

Notre invariant doit lier, à la $i$ème itération, $m$ aux $i$ premiers éléments du tableau (il vaut le maximum). Pour que cela fonctionne facilement il faut pouvoir expliciter le numéro de l'itération actuelle de la boucle `pour chaque`{.language-}. On modifie alors notre algorithme pour rendre $i$ explicite :

```pseudocode
algorithme maximum(t: []int) → int:
    ref m ← t[0]
    ref x int
    pour chaque i de [0 .. t.longueur[:
        x ← t[i]
        si m < x:
            m ← x
    rendre m
```

{% details "code python" %}

```python
def maximum(t):
    m = t[0]
    for i in range(len(t)):
        x = t[i]
        if m < x:
            m = x
    return m
```

{% enddetails %}

Ce qui permet d'écrire l'invariant :

> **Invariant de boucle :**  à la fin d'une itération, $m$ vaut le maximum des $i+1$ premiers éléments du tableau.

#### 5. Prouver l'invariant

Après la première itération de la boucle, comme $m$ vaut initialement le premier élément du tableau, on a que $m=t[0]$ qui est bien le maximum des $0+1=1$ premiers éléments du tableau. L'invariant est vérifié à la fin de la première itération où $i=0$.

On suppose l'invariant vrai à la fin d'une itération. À la fin de l'itération suivante, $m'$ (la valeur de $m$ à l'issue de cette itération) vaut soit $m$ (la valeur de $m$ au début de l'itération) soit $x'=t[i']$ ($i'$ étant la valeur de $i$ pour cette nouvelle itération). Comme $i' = i+1$ et que l'invariant est vrai à la fin de l'itération précédente :

- $m$ vaut le maximum du tableau sur les $i+1$ premiers éléments (hypothèse de récurrence)
- $m' = \max(m, x') = \max(m, t[i']) = \max(m, t[i + 1])$ (ce qui se passe dans l'itération suivante)

On en conclut que $m'$ vaut bien le maximum du tableau sur les $i + 2$ premiers éléments.

Notre invariant est vérifié.

#### 6. Prouver la correction de l'algorithme

Cette partie-là est facile si on a le bon invariant. Il suffit de regarder la valeur de l'invariant à la fin de la boucle. Dans notre cas $m$ vaut le maximum de tous les éléments du tableau, c'est le maximum.

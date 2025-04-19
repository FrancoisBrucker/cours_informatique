---
layout: layout/post.njk
title: Prouver un algorithme

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le but d'un algorithme est de résoudre un problème algorithmique. Prouver un algorithme signifie qu'il fait bien ce qu'il est sensé faire :

{% note "**Définition**" %}

Prouver un algorithme $A$ c'est démontrer qu'il résout un problème $P$. Pour cela :

1. on explicitera le problème $P$ :
   - ses entrées
   - sa question
   - sa sortie
2. on démontrera que le résultat de l'exécution de $A$ avec une instance d'entrées de $P$ est bien une réponse à $P$.

{% endnote %}

A chaque fois que l'on nous de demandera de créer un algorithme pour résoudre un problème il nous faudra :

1. s'assurer que l'on écrit un programme
2. s'assurer que ce programme s'arrête pour toute entrée (et donc que c'est un algorithme)
3. montrer qu'il résout le problème demandé.

Si l'étape 2, prouver qu'un programme s'arrête, fait partie des problèmes indécidable en général, il est souvent facile en pratique de montrer qu'un programme donné est un algorithme. En particulier les algorithmes qui résolvent des problèmes sont sensés s'arrêter et il sera (normalement) facile de le voir.

En revanche l'étape 3, la preuve que l'algorithme fait bien ce qu'on attend de lui, est parfois plus délicate.

## Types d'algorithme

Il y a deux sortes d'algorithmes :

- les algorithmes itératifs, c'est à dire utilisant des boucles
- les algorithmes récursifs, c'est à dire écrit sous la forme d'une fonction qui s'appelle elle même.

Tout problème algorithmique pourra toujours s'écrire sous une forme itérative ou récursive, bien que certains problèmes se résolvent mieux sous une forme que l'autre.

Avant de définir formellement les deux approches commençons par deux remarques d'importance :

{% note "**À retenir**" %}

Adaptation d'un algorithme aux données :

1. pour que la sortie d'un algorithme dépende de ses entrées, il est nécessaire qu'il possède des instructions conditionnelles (sinon il fera toujours la même chose),
2. pour qu'un algorithme puisse traiter des entrées de taille quelconque, il est nécessaire de répéter certaines de ses instructions (sinon il ne ne pourra traiter entièrement des données plus grandes que son nombre d'instructions).

La différence entre les approches itératives et récursive est lié au traitement des deux points précédents.

{% endnote %}

Pour expliciter la différence entre les deux approches nous allons utiliser le calcul de la factorielle définie pour tout entier $n\geq 1$ telle que :

$$
n! = \prod\limits_{1\leq i \leq n} i = 1 \times 2 \times \dots \times (n-1)\times n
$$

### Récursif

{% note %}

**Un algorithme récursif** va gérer les 2 points d'adaptations aux données en se rappelant lui-même (une **_récursion_**) avec de nouveaux paramètres d'entrées un nombre fini de fois (nécessite une **_condition d'arrêt_**). Il va avoir tendance à aller du cas général vers le cas particulier en stockant les éléments intermédiaires dans ses paramètres d'entrées.

{% endnote %}

Pour le calcul de la factorielle, si $(n-1)!$ est connu, $n! = n \times ((n-1)!)$, et en remarquant que l'on connaît $1!$ qui vaut $1$, on peut écrire l'équation de récurrence :

<div>
$$
n! = \begin{cases}
1 \text{ si } n=1\\
n \cdot (n-1)!
\end{cases}
$$
</div>

Qui permet d'écrire l'algorithme récursif suivant :

<div id="fact-rec"></div>

```pseudocode
algorithme factorielle(n: entier  # n > 1
                      ) → entier:
    si n == 1:  # condition d'arrêt
        rendre 1
    f ← factorielle(n-1)  # récursion
    rendre n * f
```

{% details "code python" %}

```python
def factorielle(n):
    if n == 1:
        return 1
    f = factorielle(n-1)
    return n *f
```

{% enddetails %}

L'algorithme récursif suit directement l'équation de récurrence. Attention, il est nécessaire que la condition d'arrêt soit évaluée avant la récursion pour la stopper sin nécessaire.

### Itératif

{% note %}

**Un algorithme itératif** va gérer les 2 points d'adaptation aux données en modifiant des variables locales et en utilisant des boucles `pour chaque`{.language-pseudocode} et `tant que`{.language-}. Il va avoir tendance à aller du cas particulier vers le cas général en stockant les éléments intermédiaires dans des variables.
{% endnote %}

Pour le calcul de la factorielle, on va commencer par calculer $1!$ puis remarquer que $n! = ((n-1)!) \cdot n$ :

```pseudocode
algorithme factorielle(n: entier) → entier:
    r ← 1  # initialisation
    i ← 1
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

On voit que la forme d'un algorithme itératif est inversé par rapport à un algorithme récursif.

## Preuve

Prouver qu'un programme résout un problème algorithmique nécessite deux vérifications :

- **_la finitude_** : le programme s'arrête pour toute entrée, c'est un algorithme
- **_la correction_** : sa sortie est une solution du problème

### Finitude

Un programme récursif est un algorithme s'il n'existe pas de récursion infinie :

{% note %}

**Un programme récursif** est un algorithme si quelque soient ses entrées il n'y aura qu'un nombre fini de récursions.
{% endnote %}

Un programme itératif est un algorithme s'il n'existe pas de boucle infinie. Ceci n'est possible que pour les boucles `tant que`{.language-} :

{% note %}

**Un programme itératif** est un algorithme si les conditions d'arrêt des boucles `tant que`{.language-} seront vraies au court de l'exécution du programme quelque soit ses entrées.
{% endnote %}

### Correction

Il n'existe pas de schéma général permettant de prouver qu'un algorithme résout un problème donné mais comme l'adaptation aux données d'un algorithme se fait dans les boucles ou les récursions, une méthode qui se révèle souvent efficace consiste à trouver des propriétés qui sont conservées à chaque itération ou récursion.

{% note "**À retenir**" %}

Pour prouver un algorithme on cherchera prouver ce que fait chaque boucle ou récursion. Pour cela on utilisera plusieurs techniques, par ordre de difficulté :

1. une relation évidente caractérisant le but de la boucle
2. une équation de récurrence plus une condition d'arrêt pour prouver :
   - un algorithme récursif
   - une boucle itérative pouvant être écrite sous forme récursive
3. [un invariant de boucle](https://fr.wikipedia.org/wiki/Invariant_de_boucle) pour des algorithme itératifs. Ces invariants vont alors être conservés jusqu'à la fin de l'algorithme et nous permettre de prouver son résultat.

{% endnote %}

A part les recommandations ci-dessus, il n'existe pas vraiment de règles à appliquer pour prouver un algorithme. Seule l'expérience et l'étude des algorithmes classiques vous permettra de trouver facilement comment prouver un algorithme.

## Mise en application

Nous allons prouver que les deux algorithmes de calcul de factorielle calculent effectivement la factorielle. Cet exemple sera l'occasion de mener à bien les trois types de preuves préconisés.

### Une relation évidente

Considérons l'algorithme suivant, variation de la version itérative de factorielle précédente :

```pseudocode
algorithme factorielle(n: entier) → entier:  # n ≥ 1
    produit ← 1
    pour chaque i de [2, n]:
        produit ← produit * i

    rendre produit
```

1. **finitude** : puisque les boucles `pour chaque`{.language-} n'ont qu'un nombre fini d'itérations
2. **exactitude** : à la fin de la boucle `pour chaque`{.language-} la variable `produit`{.language-} vaut clairement $\Pi_{1\leq i \leq n} i$ qui est par définition la valeur de $n!$.

### Une relation de récurrence

#### <span id="facto-rec"></span> Algorithme récursif

Les preuves des algorithmes récursifs sont souvent les plus simples car ils sont souvent les plus proches de la définition récursive qu'ils implémentent. Reprenons une version (un peu modifiée) du programme du calcul de la factorielle récursif :

```pseudocode
algorithme factorielle(n: entier
                      ) → entier:
    si n ≤ 1:
        rendre 1
    f ← factorielle(n-1)
    rendre n * f
```

{% exercice %}
La version ci-dessus de l'algorithme factorielle récursif est différente de la première version. Quelle est la différence et pourquoi avons-nous fait ça ?
{% endexercice %}
{% details "corrigé" %}
On a mis un `≤`{.language-} plutôt qu'un `==`{.language-} dans le test.

Ceci permet de prendre en compte le cas où $n$ vaut 0, et évite des récursions infinie pour tout entier relatif $n$.

Ce genre d'optimisation n'est pas nécessaire, mais si on y pense autant le faire car cela ne complexifie pas l'algorithme.

{% enddetails %}

##### Finitude de Factorielle récursif

L'idée est de démontrer la finitude par récurrence sur $n$.

1. **initialisation** de la preuve : si $n=1$, l'algorithme va se finir sans exécuter la ligne 4, il y a un nombre fini de récursion.
2. **hypothèse de récurrence** : pour tout entier plus petit que $n-1\geq 1$, l'algorithme va avoir un nombre fini de récursions.
3. **pour $n$** : `factorielle(n)`{.language-} va exécuter la ligne 4 (`f ← factorielle(n-1)`{.language-}) qui, par hypothèse de récurrence,  va se terminer au bout d'un nombre fini de récursions : le programme `factorielle(n)`{.language-} va également se terminer.

La preuve précédente donne un moyen simple de prouver qu'un algorithme récursif va s'arrêter :

{% note "**À retenir**" %}
Tout appel récursif doit se rapprocher strictement d'un état de terminaison.
{% endnote %}

Ceci fonctionne même s'il y a plus d'un appel récursif. On peut donc simplement écrire pour prouver la convergence :

Si $n\geq 1$ est un entier, l'algorithme va s'arrêter car $n$ décroît strictement de 1 à chaque appelle récursif et on stoppe si $n \leq 1$.

##### Correction de Factorielle récursif

{% note "**Schéma de preuve des algorithmes récursifs :**" %}
Pour les preuves d'algorithmes récursifs, le schéma de preuve est quasi-toujours le même : faire une preuve par récurrence.
{% endnote %}

Par récurrence sur $n$, avec $n$ entier strictement positif.

1. **initialisation** : $n = 1$ `factorielle(1)`{.language-} vaut bien bien $1 = 1!$.
2. **hypothèse de récurrence** : pour tout entier plus petit que $n-1\geq 1$ on a `factorielle(n-1) = (n-1)!`{.language-}
3. **pour $n$** : le retour de `factorielle(n)`{.language-} est `(n) * factorielle(n-1)`{.language-} qui vaut donc $n \cdot (n-1)! = n!$ par hypothèse de récurrence.

#### <span id="facto-iter"></span> Algorithme itératif

Considérons l'algorithme itératif suivant :

```pseudocode
algorithme factorielle(n: entier) → entier:
    r ← 1
    i ← 1
    tant que i ≤ n:
        r ← r * i
        i ← i + 1
    rendre r
```

##### Finitude

Comme $i$ va croître strictement, la condition `i ≤ n`{.language-} sera fausse à un moment donné ce qui la fera sortir de la boucle et stopper le programme.

##### Correction

Nous allons montrer que l'on peut prouver notre algorithme par récurrence. Il peut en effet se récrire de cette façon :

```pseudocode/
algorithme factorielle'(n: entier) → entier:
    r ← 1
    i ← 1
    tant que i ≤ n - 1:
        r ← r * i
        i ← i + 1
    
    r ← r * i
    i ← i + 1

    rendre r
```

Qui est aussi équivalent à :

```pseudocode
algorithme factorielle''(n: entier) → entier:
    r ← factorielle''(n-1)
    r ← r * n

    rendre r
```

La boucle se comporte comme l'algorithme récursif précédent. On est ramené au cas précédent pour en prouver sa correction.

### Preuve par invariant

Lorsque l'on ne peut pas clairement et rapidement faire une preuve par récurrence, on peut chercher un invariant à la boucle : quelque chose qui est conservé à chaque itération. Cette technique de preuve n'est pas très éloignée des preuves par récurrences, elle est juste plus générale et (de l'avis des informaticiens) plus élégante.

Refaisons la preuve précédente en utilisant un invariant de boucle pour montrer comment tout ceci peut se faire :

```pseudocode
algorithme factorielle(n: entier) → entier:
    r ← 1
    i ← 1
    tant que i ≤ n:
        r ← r * i
        i ← i + 1
    rendre r
```

{% note "**Schéma de preuve des algorithmes itératifs par invariant :**" %}
Un invariant doit résumer ce que fait la boucle avec une équation qui est toujours vérifiées, même si on modifie des variables. Une fois l'invariant trouvé on commence par le démontrer :

 1. on vérifie que l'invariant est vrai à la fin de la première itération de la boucle
 2. on suppose l'invariant à la fin de l'itération $k$ de la boucle et on vérifie qu'il est toujours vérifié à la fin de l'itération $k + 1$.

Une fois l'invariant démontré, il va être toujours vrai, de la première itération à la sortie de la boucle. A ce moment là, sa valeur doit servir à démontrer le résultat voulu.

Pour simplifier l'écriture, on note avec un `'` (prim) les variables à la fin de la boucle d'itération $k+1$ pour les différentier des variables de la fin de l'itération $k$.
{% endnote %}
{% info %}
Il existe des variantes dans les preuves par invariants selon que l'on vérifie juste à la fin de la boucle ou au début et à la fin de l'itération. Les deux formes sont équivalentes, mais il est parfois plus aisée d'utiliser l'une que l'autre.
{% endinfo %}

Trouver un invariant de boucle peut-être intimidant. Ne le cherchez donc pas tout de suite : commencez par comprendre l'algorithme.

Souvent (toujours ?), c'est dans les boucles que se forme la solution :

1. comprendre l'algorithme c'est comprendre la boucle
2. comprendre la boucle c'est comprendre comment se modifient les variables
3. la modification des variables peut s'exprimer sous la forme d'un invariant

Allons-y :

1. l'algorithme retourne $r$ à la fin : ce doit donc être le résultat et il doit valoir $n!$
2. $r$ est multiplié par $i$ à chaque itération
3. $i$ est incrémenté de 1 à chaque itération et commence à 1.

On doit donc avoir un invariant du type _$r \simeq i!$ à la fin de chaque itération_ à plus ou moins 1 près. Pour en être sur regardons ce que valent nos variables à la fin de la première itération :

- $r = 1$
- $i = 2$ (on a modifié $i$ après l'avoir multiplié par $r$)

Notre invariant doit donc être :

> Invariant : $r = (i-1)!$ à la fin de chaque itération.

1. c'est vrai à la fin de la 1ère itération (on a tout fait pour)
2. si c'est vrai à la fin de la $k$ème itération, à la fin de la $k+1$ème itération on a :
   - $r'=r \cdot i$ (le $r$ de la fin de la $k+1$ème boucle est égal à celui de la fin de la $k$ème boucle fois le $i$ de la fin de $k$ème boucle)
   - $i' = i + 1$ (le $i$ de la fin de la $k+1$ème boucle est le $i$ de la fin de la $k$ème boucle plus 1)
   - $r = (i-1)!$ (c'est notre invariant, vrai à la fin de l'itération $k$ ar hypothèse)
3. on a donc : $r' = (i-1)! \cdot i = i! = (i'-1)!$ : **notre invariant est vérifié**.

L'invariant étant vérifié à la fin de chaque itération, il est donc aussi vrai à la fin de la dernière itération. A ce moment là, on a $i=n+1$ et donc $r = n!$

### A vous : invariant sur une variante

Entraînons nous avec l'algorithme suivant, variante itérative de l'algorithme factoriel :

<div id="algo-factorielle_variante"></div>

```pseudocode
algorithme factorielle_variante(n: entier):
    r ← 1
    i ← n
    tant que i ≤ n:
        r ← r * i
        i ← i - 1
    rendre r
```

{% details "code python" %}

```python
def factorielle_variante(n):
    r = 1
    i = n
    while i > 1:
        r *= i
        i -= 1
    return r
```

{% enddetails %}

Vous allez démontrer que cet algorithme calcule également la factorielle.

{% exercice %}
Démontrez la finitude du [programme `factorielle_variante`{.language-}](./#algo-factorielle_variante){.interne}.
{% endexercice %}
{% details "corrigé" %}

Si $i$ est un nombre  qui décroît de 1 à chaque itération : à une itération il sera forcément plus petit ou égal à 1.
{% enddetails %}

Pour démontrer la correction du l'algorithme, on utilise un invariant de boucle.

{% exercice %}
Montrez que la boucle `tant que`{.language-} de [l'algorithme `factorielle_variante`{.language-}](./#algo-factorielle_variante){.interne} admet l'invariant de boucle suivant :

> À la fin d'une itération de la boucle `tant que`{.language-} : $r = (i+1) \cdot (i+2) \dots (n-1) \cdot n$

{% endexercice %}
{% details "corrigé" %}

1. à la fin de la première itération $i = n - 1$ et $r = n = (i+1)$ : notre invariant est vérifié.
2. on suppose la propriété vraie à la fin de la $k$ème itération. A la fin de l'itération suivante on a :
   - $r' = r \cdot i$ (le $r$ de la fin de la $k+1$ème boucle est égal à celui de la fin de la $k$ème boucle fois le $i$ de la fin de $k$ème boucle)
   - $i' = i - 1$ (le $i$ de la fin de la $k+1$ème boucle est le $i$ de la fin de la $k$ème boucle moins 1)
   - $r = (i+1) \cdot \dots n$ (c'est notre invariant, vrai à la fin de l'itération $k$ ar hypothèse)
3. on a donc : $r' = (i+1) \cdot \dots n \cdot (i) = i \cdot (i+1) \dots n = (i'+1) \dots \cdot n$ : **notre invariant est vérifié**.

{% enddetails %}

{% exercice %}
Déduire de l'exercice précédent que [l'algorithme `factorielle_variante`{.language-}](./#algo-factorielle_variante){.interne} calcule bien la factorielle de son entrée.
{% endexercice %}
{% details "corrigé" %}

L'invariant étant vérifié à la fin de chaque itération, il est donc aussi vrai à la fin de la dernière itération. A ce moment là, on a $i=1$ et donc $r = 1 \cdot 2 \cdot \dots \cdot n = n!$

{% enddetails %}

## Trouver un invariant

Trouver un invariant de boucle est souvent intimidant pour des débutants. Nous allons nous entraîner un peu pour acquérir quelques automatismes.

L'idée principale pour trouver un invariant est de procéder par étapes :

1. comprendre l'algorithme
2. comprendre l'intérêt de la boucle le constituant (s'il y a plusieurs boucle on refait l'analyse pour chaque boucle)
3. voir comment on pourrait prouver l'algorithme
4. utiliser cette idée de preuve pour créer un invariant
5. prouver l'invariant
6. prouver la correction de l'algorithme

Ce qu'il faut retenir c'est que trouver l'invariant est **à la fin du processus de création de la preuve**.

### <span id="algorithme-max-iter"></span> Maximum d'un tableau

On considère l'algorithme itératif suivant :

```pseudocode
algorithme maximum(t: [entier]) → entier:
    m ← t[0]
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

La finitude du programme est clair puisqu'il n'y a qu'une boucle pour chaque. Analysons le programme pour comprendre quel invariant utiliser pour la correction. Reprenons les quatre étapes.

#### Comprendre l'algorithme

L'algorithme va itérer sur chaque élément du tableau et conserver dans la variable `m`{.language-} la plus grande des valeurs vues jusqu'à présent.

#### Comprendre l'intérêt de la boucle le constituant (s'il y a plusieurs boucle on refait l'analyse pour chaque boucle)

Il faut parcourir tous les éléments du tableau pour connaître la plus grande des valeurs.

#### Voir comment on pourrait prouver l'algorithme

Il faut montrer que la variable `m`{.language-} contient la valeur maximale pour toutes les éléments de `t`{.language-} vues jusqu'à présent. Comme à la fin de l'algorithme on aura vu toutes lees valeurs de `t`{.language-} on aura prouvé que `m`{.language-} est bien le maximum.

#### Utiliser cette idée de preuve pour créer un invariant

Notre invariant doit lier, à la $i$ème itération, $m$ aux $i$ premiers éléments du tableaux (il vaut le maximum). Pour que cela fonctionne facilement il faut pouvoir expliciter le numéro de l'itération actuelle de la boucle `pour chaque`{.language-}. On modifie alors notre algorithme pour rendre $i$ explicite :

```pseudocode
algorithme maximum(t: [entier]) → entier:
    m ← t[0]
    pour chaque i de [0, t.longueur[:
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

> Invariant : à la fin d'une itération, $m$ vaut le maximum des $i+1$ premiers élément du tableau.

#### Prouver l'invariant

Après la première itération de la boucle, comme $m$ vaut initialement le premier élément du tableau, on a que $m=t[0]$ qui est bien le maximum des $0+1=1$ premiers éléments du tableau. L'invariant est vérifié à la fin de la première itération où $i=0$.

On suppose l'invariant vrai à la fin d'une itération. A la fin de l'itération suivante, $m'$ (la valeur de $m$ à l'issue de cette itération) vaut soit $m$ (la valeur de $m$ au début de l'itération) soit $x'=t[i']$ ($i'$ étant la valeur de $i$ pour cette nouvelle itération). Comme $i' = i+1$ et que l'invariant est vrai à la fin de l'itération précédente :

- $m$ vaut le maximum du tableau sur les $i+1$ premiers éléments (hypothèse de récurrence)
- $m' = \max(m, x') = \max(m, t[i']) = \max(m, t[i + 1])$ (ce qu'il se passe dans l'itération suivante)

On en conclut que $m'$ vaut bien le maximum du tableau sur les $i + 2$ premiers éléments.

Notre invariant est vérifié.

#### Prouver la correction de l'algorithme

Cette partie là est facile si on a le bon invariant. Il suffit de regarder la valeur de l'invariant à la fin de la boucle. Dans notre cas $m$ vaut le maximum de tous les éléments du tableau tableau, c'est le maximum.

## À vous

### Nombre dans un tableau

Pour faire ceci sans invariant de boucle, on transforme notre algorithme itératif en sa version récursive que l'on peut aisément démontrer par récurrence.

{% exercice %}
Reprenez le premier pseudo-code que vous avez écrit : [nombre d'occurrences](../pseudo-code/#exercice-nombre-occurrences){.interne} et prouver qu'il fonctionne en exhibant sa version récursive.

{% endexercice %}
{% details "corrigé" %}
On remarque que l'algorithme fonctionne de la même manière si on prend une restriction du tableau. Explicitons cela.

On voit que notre algorithme itératif est équivalent au programme récursif suivant :

```pseudocode
algorithme nombre'(t: [entier], x: entier) → entier:
    si t.longueur == 0:
        rendre 0
    sinon si t[-1] == x:
        rendre nombre'(t[:-1]) + 1
    sinon:
        rendre nombre'(t[:-1])
```

On montre alors par récurrence que notre algorithme fonctionne :

1. si t.longueur == 0 : c'est OK
2. on suppose notre algorithme OK pour des tableaux de longueur n
3. pour un tableau de longueur n+1, la taille de t[:-1] est de n, et notre algorithme fonctionne. On ajoute ensuite 1 que si le dernier élément du tableau vaut x : notre algorithme fonctionne pour le tableau de longueur n+1 ce qui clot la preuve par récurrence.

{% enddetails %}

### PGCD, encore lui

```pseudocode
algorithme PGCD(a, b):  # a, b > 0
    si a == b:
        rendre a
    si a < b:
        rendre PGCD(b-a, a)
    sinon
        rendre PGCD(a-b, b)

```

{% exercice %}
Montrez que l'algorithme récursif précédent calcule bien le PGCD de eux entiers strictement positifs.
{% endexercice %}
{% details "corrigé" %}

- terminaison : La condition de terminaison est `a == b`{.language-}. Si `a \leq b`{.language-}, chaque itération va diminuer strictement la quantité $\vert\\, a = b \\,\vert$ et donc se rapprocher strictement de la condition d'arrêt : notre programme s'arrête pour toute entrée.

- correction : si `a == b`{.language-}, son PGCD est bien a (ou b) et sinon on respecte [la définition d'Euclide du PGCD](../bases-théoriques/calculabilité/#algorithme-euclide){.interne}.

{% enddetails %}

### Division euclidienne

Vous trouverez ci-après une version itérative de l'algorithme de la division euclidienne que vous allez prouver par invariant de boucle.

<span id="algorithme-division-euclidienne"></span>

```pseudocode
algorithme division_euclidienne(a: entier,
                                b: entier) → [entier]:
    r ← a
    q ← 0
    
    tant que r ≥ b:
        r ← r - b
        q ← q + 1
    
    rendre [q, r]
```

{% details "code python" %}

```python
def division_euclidienne(a, b):
    r = a
    q = 0
    while r >= b:
        r -= b
        q += 1
    return (q, r)
```

Le retour de la fonction python est un [tuple](https://docs.python.org/fr/3/tutorial/datastructures.html#tuples-and-sequences) à 2 éléments (c'est à dire un tableau à 2 éléments que l'on ne peut pas modifier)
{% enddetails %}

Le retour de notre algorithme est un tableau à deux éléments.

{% exercice %}
Démontrez la finitude du programme `division_euclidienne`{.language-}.
{% endexercice %}
{% details "corrigé" %}

Si a et b sont des entiers positifs le programme s'arrête car :

- `r`{.language-} est un entier
- `r`{.language-} après une itération est **strictement plus petit** que le `r`{.language-} avant itération
- on s'arrête si `r`{.language-} est strictement plus petit que `b`{.language-}.

{% enddetails %}

On veut montrer que l'on obtient bien une division euclidienne de $a$ par $b$. C'est à dire que $a = bq + r$ avec $r < b$. Regardez bien comment fonctionne la boucle de l'algorithme pour garantir ce résultat.

{% exercice %}
Proposez un invariant de boucle que vous démontrerez.
{% endexercice %}
{% details "corrigé" %}

> Invariant : `a = r + q * b`{.language-}

Prouvons l'invariant :

1. l'invariant est bien vrai à la fin de la première boucle puisque $q=1$ et $r=a-b$ à ce moment là.
2. on doit prouver que `a' = r' + q' * b'`{.language-} à la fin de la $i+1$ème itération.
3. si l'on est passé dans la boucle on a `a'=a`{.language-}, `r' = r - b`{.language-}, `b' = b`{.language-} et `q' = q + 1`{.language-}
4. donc `r' + q' * b' = r-b + (q+1) * b = r + q * b = a = a'`{.language-} puisque l'invariant est vrai à la fin de la $i$ème itération. On a bien `a' = r' + q' * b'`{.language-}, l'invariant est démontré.

{% enddetails %}
{% exercice %}
Utilisez votre invariant de boucle pour démontrer la correction de l'algorithme `division_euclidienne`{.language-}.
{% endexercice %}
{% details "corrigé" %}
L'invariant étant juste tout le temps, il l'est en particulier à l'issue de la dernière boucle. A ce moment là on a `a = r + qb`{.language-} avec `r < b`{.language-} ce qui est bien ce qu'il fallait démontrer.

{% enddetails %}

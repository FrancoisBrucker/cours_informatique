---
layout: layout/post.njk

title: "Mots de Bruijn"
authors: 
    - François Brucker

eleventyNavigation:
  key: "Mots de Bruijn"
  parent: "Graphes"
---

<!-- début résumé -->

Des graphes eulérien là où ne s'y attend pas. Une application qui montre encore une fois comme preuve d'existence et algorithme de création de structure sont intimement liés.

<!-- fin résumé -->

Commençons par motiver ce projet : **le problème du digicode**

> On a encore oublié ce fichu code de la porte d'entrée. Quel est le moyen le plus rapide de trouver le bon code ?

### Formalisation du problème

Il faut trouver un *mot* de longueur $p$ d'un *alphabet* $\mathcal{A}$ à $n$ caractères (un mot est une suite de $p$ caractère de $\mathcal{A}$).

**Exemple :**
Les mots de longueur $p=3$ de l'alphabet $\\{0, 1\\}$ à $n=2$ caractères. Il y a $n^p = 2^3 = 8$ mots de longueur 3 différents qui sont :

* $000$
* $001$
* $010$
* $011$
* $100$
* $101$
* $110$
* $111$

Si l'on veut trouver une chaîne de caractère qui contient tous les mots de longueur $p$ d'un alphabet à $n$ caractère on peut coller bout à bout tous les mots.

**Exemple :**
Dans l'exemple cela donne par exemple le mot : $000001010011100101110111$ de longueur $p \cdot n^p = 3 \cdot 2^3 = 24$.

### Tous les mots

Pour trouver tous les mots de longueur $p$ d'un alphabet $\mathcal{A} = [a_0, \dots, a_{q-1}]$, nous allons procéder par étapes.

Commencez par montrer que :
{% exercice %}
Si l'on possède l'ensemble $M$ de tous les mots de longueur $p$ de l'alphabet $\mathcal{N} = [0, 1, \dots, q-1]$, il est facile de trouver tous les mots de longueur $p$ de l'alphabet $\mathcal{A} = [a_0, \dots, a_{q-1}]$.
{% endexercice %}
{% details "solution" %}

On utilise la bijection $f$ qui a un mot $m=n_0\dots n_{p-1}$ associe $f(m) = a_{n_0}\dots a_{n_{p-1}}$
{% enddetails %}

On peut donc se focaliser sur l'énumération des mots de longueur $p$ de l'alphabet $\mathcal{N} = [0, 1, \dots, q-1]$. Soit $m = m_0\dots m_{p-1}$ un mot de longueur $p$ de l'alphabet $\mathcal{N} = [0, 1, \dots, q-1]$ tel qu'il existe $m_i \neq q-1$. On note : $\mbox{next}(n, q) = n_0 \dots  {n}_{p-1}$ le mot tel que :

* si $m_{p-1} < q-1$ alors :
  * $n_i = m_i$ pour $0 \leq i < p-1$
  * $n_{p-1}$ $= m_{p-1} + 1$
* si $m_{p-1} = q-1$ alors soit j le plus grand indice tel que $m_j \neq q-1$ :
  * $n_i = m_i$ pour $i < j$
  * $n_j = m_j + 1$
  * $n_i = 0$ pour $i > j$

{% exercice %}
Montrez que la fonction $\mbox{next}()$ permet d'énumérer tous les mots de longueur $p$ de l'alphabet $\mathcal{N} = [0, 1, \dots, q-1]$.
{% endexercice %}
{% details "solution" %}

```python
n = [0] * p

print(n)
while n != [q-1] * p:
    n = Next(n, q)
    print(n)
```

Les suites obtenues sont bien deux à deux différentes car elles sont ordonnées lexicographiquement.
{% enddetails %}

{% exercice %}
Codez la fonction `next(n, q)`{.language-} qui donne le successeur de $n$.
{% endexercice %}
{% exercice %}
En déduire un algorithme (que vous coderez), qui rend tous les mots de longueur $p$ d'un alphabet à $q$ caractères.
{% endexercice %}

### Le plus court

La longueur la plus petite possible d'une chaîne de caractère qui contiendrait tous les mots serait que les mots se chevauchent : les $p-1$ derniers caractères du i-ème mot seraient égaux aux $p-1$ derniers caractères du (i+1)-ème mot.

{% exercice %}
Montrez que la taille minimale théorique est de :
$$
1 \cdot p  + (n^p - 1) \cdot 1 = p - 1 + n^p
$$
caractères.
{% endexercice %}
{% details "solution" %}
Dans le cas où les mots se chevauchent, chaque mot de compterait que pour 1 nouveau caractère dans la chaîne, à part le premier mot qu'il faudrait écrire entièrement : le 1er mot compte pour $p$ caractères les autres comptent uniquement pour 1 caractère, d'où la formule demandée.
{% enddetails %}

Le gain serait de : $\frac{p-1 + n^p}{pn^p} \simeq \frac{1}{p}$, on diviserait donc la taille par $p$, ce qui n'est pas négligeable.

**Exemple :** La longueur minimale est de $3-1 + 2^3 = 10$, qui est bien plus petit que 24.

Sauf que l'on ne pas pas si une telle chaîne existe...

## Bruijn et Euler to the rescue

Considérons le graphe **orienté** suivant, appelé *graphe de Bruijn* $B(n, p+1) = (V, E)$ où :

* $V$ est l'ensemble des mots de longueur $p$ d'un alphabet à $n$ éléments
* $xy \in E$ si les $p-1$ derniers caractères de $x$ sont les $p-1$ premiers caractères de $y$

{% exercice %}
Donnez le graphe de Bruijn associé aux mots de longueur 3 de l'alphabet $\\{0, 1\\}$.
{% endexercice %}
{% details "solution" %}
![graphe de Bruijn](./mot_3_01.png)
{% enddetails %}

{% exercice %}
Codez l'algorithme qui crée le graphe $B(n, p+1)$ pour l'alphabet des entiers allant de 0 à $n-1$.

Si vous codez le graphe par dictionnaire, il faudra que vos sommets soient des [tuples](https://docs.python.org/fr/3/tutorial/datastructures.html#tuples-and-sequences) et non des listes (qui ne peuvent être des clés de dictionnaires ou d'éléments d'ensembles).
{% endexercice %}

### Propriétés

Si $xy$ est un arc du graphe, alors on a que $x = aX$ et $y= Xb$ où $X$ est un mot de longueur $p-1$ et $a$et $b$ des caractères : l'arc correspond au mot de longueur $p + 1$ = $aXb$ et **ce mot n'apparaît qu'une fois** (car à ce mot ne correspond qu'un unique $x$ et $y$).

Réciproquement chaque mot de longueur $p + 1$ pouvant s'écrire sous la forme $aXb$ avec $X$ un mot de longueur $p-1$ et $a$ et $b$ des caractères, tout mot de longueur $p + 1$ est associé à un arc.

Enfin, pour un sommet $x$ donné, il possède $n$ arc entrant (correspondant à tous les mots de longueur $p$ dont les $p-1$ derniers caractères correspondent aux $p-1$ premiers caractères de $x$) et $n$ arc sortant (correspondant à tous les mots de longueur $p$ dont les $p-1$ premiers caractères correspondent aux $p-1$ derniers caractères de $x$) :

**le graphe $B(n, p+1)$ est eulérien** pour tout $p$ et tout $n$.

### Cycle eulérien

Un cycle eulérien du graphe $B(n, p)$ correspond à une suite comprenant tous les mots de longueur $p$. En analysant 3 sommets successifs de ce cycle $u_{i-1}u_iu_{i+1}$ on remarque que le mot correspondant à l'arc $u_{i-1}u_i$ et celui correspondant à l'arc $u_iu_{i+1}$ sont tels
que les $p-1$ derniers caractères de l'un sont les $p-1$ premiers caractères de l'autre.

{% exercice %}
Donnez le cycle eulérien associé a un graphe $B(n, p)$ donné. Vous pourrez vous inspirer de l'[algorithme du cours](../parcours-euleriens#principe-algorithme){.interne} en adaptant chaque fonction au fait que notre graphe est **orienté**. En particulier :

* la découverte du cycle se fera avec l'algorithme [`circuit(G, a)`{.language-}](../chemins-cycles-connexite#algo-cycle-oriente){.interne}
* la suppression du cycle dans le graphe (fonction [`supprime(G, c)`{.language-}](../parcours-euleriens#fonction-supprime){.interne}) doit être adaptée en ne supprimant pas l'arc réciproque dans la structure

{% endexercice %}

### Mot de Bruijn

Un cycle eulérien $u_0\dots u_k$ (donc $u_k = u_0$) de $B(n, p)$ nous permet de construire les $n^p$ différents mots : c'est les mots correspondants aux arcs $u_iu_{i+1}$.

De là on construit le mot qui commence par le mot associé à $u_0u_1$ puis on ajoute itérativement le dernier caractère du sommet $u_i$ pour $i > 1$.

{% info %}
La construction ci-dessus est équivalente à commencer par le mot associé à $u_0$ et à ajouter itérativement les derniers caractères de tous les $u_i$, $i > 0$.
{% endinfo %}

Ce mot, appelé **mot de Bruijn** a bien les propriétés suivantes :

* il contient tous les mots de longueur $p$ de l'alphabet à n caractères,
* il a une taille de $p +(n^p -1)$ caractères

{% note "**Conclusion**" %}

Il existe bien un mot de taille minimale ($p +(n^p-1)$ caractères) contenant tous les mots de longueur $p$ d'un alphabet à $n$ lettres, et ce quelque soit $n$ et $p$.
{% endnote %}

### Exemple

Un cycle eulérien associé est alors **10**-0**1**-1**1**-1**1**-1**0**-0**0**-0**0**-0**1**-1**0** ce qui donne le mot de Bruijn associé : 1011100010.

{% exercice %}
Créez l'algorithme qui rend le mot de Bruijn associé à un cycle eulérien d'un graphe $B(n, p)$ donné.
{% endexercice %}

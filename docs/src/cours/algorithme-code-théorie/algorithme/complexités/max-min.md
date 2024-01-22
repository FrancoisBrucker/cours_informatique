---
layout: layout/post.njk 
title: Complexité max/min

eleventyNavigation:
    order: 1
    prerequis:
        - "../../pseudo-code/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

On se donne des outils pour mesurer (théoriquement et en pratique) les performances d'un algorithme

<!-- end résumé -->

## Mesures en $\mathcal{O}$

Mesurer les performances d'un algorithme se fera presque exclusivement en utilisant des $\mathcal{O}$ (*grand O*)

{% note %}
Une fonction <span>$f(N)$</span> est en $\mathcal{O}(f'(N))$ s'il existe 2 constantes $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot f'(N)$ pour tout $N > N_0$.
{% endnote %}

Cela permet :

* d'avoir un majorant de notre mesure lorsque $N$ devient grand
* de ne pas s'occuper des constantes puisque (on va le démontrer) une fonction en $\mathcal{O}(\text{constante})$ est également en $\mathcal{O}(1)$
* de ne pas s'occuper de la proportionnalité car (on va le démontrer) une fonction en $\mathcal{O}(\text{constante} \cdot f(N))$ est également en $\mathcal{O}(f(N))$

{% note %}
Connaître le comportement en $\mathcal{O}$ d'une mesure dépendant de $N$ nous donne un majorant de son comportement lorsque $N$ devient grand. Si le majorant n'est pas trop éloigné de la mesure originale, cela nous donne une **idée générale** de la valeur de la mesure lorsque $N$ devient grand.
{% endnote %}

Ceci est plutôt intéressant en algorithmie car l'on ne connaît pas toujours exactement le nombre d'opérations élémentaires utilisées, mais on peut les majorer de façon assez précise. On utilisera ainsi les $\mathcal{O}$ pour mesurer par rapport à la taille $N$ de l'entrée de l'algorithme :

* le nombre d'opérations élémentaires effectuées par l'algorithme avant de s'arrêter
* le temps mis par l'algorithme pour s'exécuter
* la taille de la mémoire utilisée pour par l'algorithme

{% attention %}
On considérera dans la suite de ce cours uniquement des fonctions **positives**. En particulier, certaines équivalences ne sont vraies que dans ce cas là.
{% endattention %}

### Arithmétique des $\mathcal{O}$

Par abus de langage, on notera :

* $\mathcal{O}(f(N))$ plutôt que : soit $f'(N)$ une fonction en $\mathcal{O}(f(N))$
* $f(N) = \mathcal{O}(g(N))$ plutôt que : "la fonction $f(N)$ est en $\mathcal{O}(g(N))$"
* $\mathcal{O}(f(N)) \Rightarrow \mathcal{O}(g(N))$ plutôt que : "une fonction en $\mathcal{O}(f(N))$ est également en $\mathcal{O}(g(N))$"
* $\mathcal{O}(f(N)) \Leftrightarrow \mathcal{O}(g(N))$ plutôt que : "une fonction en $\mathcal{O}(f(N))$ est également en $\mathcal{O}(g(N))$ et réciproquement"

On a les règles suivantes (si les fonctions sont positives) :

<span id="OA1"></span>
{% note %}
$\mathcal{O}(A) \Leftrightarrow \mathcal{O}(1)$, avec $A$ une constante strictement positive
{% endnote %}
{% details  "preuve" %}

Soit $f(N) = \mathcal{O}(A)$. Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) < c_0 \cdot A$.

En posant $c'_0 = c_0 \cdot A$, on a $f(N) < c'_0 \cdot 1$ pour tout $N > N_0$. Donc : $f(N) = \mathcal{O}(1)$.

Réciproquement, soit $f(N) = \mathcal{O}(1)$.

Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) < c_0 \cdot 1$. En posant $c'_0 = c_0 / A$, on a $f(N) < c'_0 \cdot A$ pour tout $N > N_0$. Donc $f(N) = \mathcal{O}(A)$.

{% enddetails %}

{% note %}
$\mathcal{O}(N^p) \Rightarrow \mathcal{O}(N^q)$ pour $q \geq p$
{% endnote %}
{% details "preuve" %}

Soit $f(N) = \mathcal{O}(N^p)$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot N^p$ pour $N > N_0$.

Comme $1 < 2 \cdot N^\alpha$ pour $\alpha \geq 0$ et $N> 1$, on a $N^p < N^p \cdot (2 \cdot N^{q-p}) = c_0 \cdot N^q$ pour $c_0 = 2$, $N > 1 = N_0$  et $p \leq q$. Donc $N^p = \mathcal{O}(N^q)$ pour tout $p \leq q$

{% enddetails %}

{% note %}
$f(N) = \mathcal{O}(g(N))$ implique $\mathcal{O}(f(N) + g(N) + h(N)) \Rightarrow \mathcal{O}(g(N) + h(N))$ pour f, g et h des fonctions positives.
{% endnote %}
{% details  "preuve" %}

Soit $f(N) = \mathcal{O}(g(N))$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot g(N)$ pour $N > N_0$.

Si $f'(N) = \mathcal{O}(f(N) + g(N) + h(N))$ il existe $c'_0$ et $N'_0$ tels que $f'(N) < c'_0(f(N) + g(N) + h(N))$ pour $N > N'_0$.

De là, $f'(N) < c'_0 c_0 g(N) + c'_0 g(N) + c'_0 h(N)$ pour $N > \max( N_0, N'_0 )$ ce qui implique $f'(N) < c'_0 \cdot (c_0 + 1) g(N) + c'_0h(N) < c'_0 \cdot (c_0 + 1) (g(N) + h(N))$ pour $N > \max(N_0, N'_0)$

On a bien : $f'(N) = \mathcal{O}(g(N) + h(N))$

{% enddetails %}

{% note %}
$f(N) = \mathcal{O}(g(N))$ implique $\mathcal{O}(f(N) \cdot g(N) \cdot h(N) + h'(N)) \Rightarrow \mathcal{O}((g(N))^2 \cdot h(N)+ h'(N))$ pour f, g, h et h' des fonctions positives.

{% endnote %}
{% details  "preuve" %}

Soit $f(N) = \mathcal{O}(g(N))$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot g(N)$ pour $N > N_0$. Les fonctions étant positives, on pet considérer sans perte de généralité que $c_0 > 1$

Si $f'(N) = \mathcal{O}(f(N)\cdot g(N) \cdot h(N) + h'(N))$ il existe $c'_0$ et $N'_0$ tels que $f'(N) < c'_0(f(N) \cdot g(N) \cdot h(N) + h'(N))$ pour $N > N_0$.

De là, $f'(N) < c'_0 (c_0 g(N) \cdot g(N) \cdot h(N) + h'(N)$ pour $N > \max(N_0, N'_0)$ ce qui implique $f'(N) < c'_0c_0 g^2(N) \cdot h(N) + c'_0 h'(N) < c'_0c_0 g^2(N) \cdot h(N) + c'_0 c_0h'(N) < c'_0c_0 \cdot (g(N)^2 \cdot h(N) + h'(N))$ pour $N > \max( N_0, N'_0)$.

On a bien : $f'(N) = \mathcal{O}((g(N))^2 \cdot h(N) + h'(N))$

{% enddetails %}

{% note %}
En combinant les $\mathcal{O}$ pour $f$ et $g$, deux fonctions positives :

$\mathcal{O}(f(N)) + \mathcal{O}(g(N)) \Rightarrow \mathcal{O}(f(N) + g(N))$

{% endnote %}
{% details  "preuve" %}

Soient $f'(N) = \mathcal{O}(f(N))$ et $g' = \mathcal{O}(g(N))$, il existe donc $c_0$, $c'_0$, $N_0$ et $N'_0$ tels que $f'(N) < c_0 f(N)$ pour $N > N_0$ et $g'(N) < c'_0 g(N)$ pour $N > N'_0$.

On a alors $f'(N) + g'(N) < c_0 f(N) +  c'_0 g(N) < \max(c_0, c'_0) \cdot (f(N) + g(N))$ pour $N > \max( N_0, N'_0)$.

On a bien : $f'(N) + g'(N) = \mathcal{O}(f(N) + g(N))$.

{% enddetails %}
{% note %}
En combinant les $\mathcal{O}$ pour $f$ et $g$ deux fonctions positives :

$\mathcal{O}(f(N)) \cdot \mathcal{O}(g(N)) \Rightarrow \mathcal{O}(f(N) \cdot g(N))$

{% endnote %}
{% details  "preuve" %}

Soient $f'(N) = \mathcal{O}(f(N))$ et $g' = \mathcal{O}(g(N))$, il existe donc $c_0$, $c'_0$, $N_0$ et $N'_0$ tels que $f'(N) < c_0 f(N)$ pour $N > N_0$ et $g'(N) < c'_0 g(N)$ pour $N > N'_0$.

On a alors $f'(N) \cdot g'(N) <  c_0f(N) \cdot c'_0g(N) = c_0c'_0 \cdot (f(N)g(N)) $ pour $N > \max(N_0, N'_0)$.

{% enddetails %}

### Conséquences algorithmiques

La [première règle](./#OA1){.interne} montre qu'un nombre constant est toujours en $\mathcal{O}(1)$. Pour un algorithme, il est souvent compliqué de savoir exactement de combien d'[opérations basiques](../pseudo-code#instruction-basique){.interne} est constituée une opération ou le temps exact qu'elle va prendre (pour un ordinateur, cela dépend du type de processeur. Par exemple, l'addition avec un x68 est faite [avec des registres](https://ensiwiki.ensimag.fr/index.php?title=Constructions_de_base_en_assembleur_x86), elle nécessite ainsi 2 opérations du processeur). On pourra cependant toujours montrer qu'il y en a un nombre constant (ou borné) :

{% note %}
La complexité d'une opération basique nécessite $\mathcal{O}(1)$ opérations.
{% endnote %}

De là :

{% note %}
Un nombre constant d'opérations basiques nécessite $\mathcal{O}(1)$ opérations.
{% endnote %}

Les règles précédentes permettent plus généralement de montrer :

{% note %}
$\mathcal{O}(A \cdot f(N)) \Leftrightarrow A \cdot \mathcal{O}(f(N)) \Leftrightarrow \mathcal{O}(f(N))$, avec $A$ une constante strictement positive et $f(N)$ une fonction strictement positive pour $N > N_0$
{% endnote %}

Ceci est pratique, car cela permet de ne pas compter toutes les opérations basiques précisément. Ainsi, en reprenant l'exemple de la partie [complexité des pseudo-code](../pseudo-code#complexité){.interne} :

```text#
x = 30
if ((x > 12) AND (x < 36)):
    z = x * "coucou"
```

1. on affecte un objet à x : 1 instruction, donc $\mathcal{O}(1)$ opérations.
2. un test avec 2 comparaisons et un `AND`{.language-} pour deux variables : 6 instructions, donc $\mathcal{O}(6) = \mathcal{O}(1)$ opérations.
3. on affecte le résultat d'une opération élémentaire : 3 instructions, donc $\mathcal{O}(3) = \mathcal{O}(1)$ opérations.

Un nombre total d'instructions de $3 \cdot \mathcal{O}(1) = \mathcal{O}(1)$ opérations.

En revanche, faites attention, cela ne marche que pour les constantes !

{% attention %}
Si le nombre d'opérations élémentaires est variable on a : $n \cdot \mathcal{O}(1) = \mathcal{O}(n)$. **On ne peut pas simplifier les éléments variables**.
{% endattention %}

Enfin, comme en algorithmie on manipulera souvent des polynômes, on peut montrer facilement avec les règles précédentes que :

{% note %}
$$\sum_{i=0}^na_i x^i = \mathcal{O}(x^n) \mbox{ si } a_n \neq 0$$
{% endnote %}

## Complexité d'un algorithme


> TBD : ici

### Nombre d'opérations basiques

{% note %}
La **complexité** (aussi parfois appelée **complexité maximale**) d'un algorithme est le **nombre maximum d'opérations basiques** effectué par celui-ci pour des entrées **de taille totale donnée**. Elle sera donnée en $\mathcal{O}(f(N))$, où $N$ est une variable rendant compte de la taille des données.
{% endnote %}

La **taille** d'une entrée est proportionnelle au nombre de cases mémoires que celle-ci nécessite.

{% info %}
Lorsque vous entendrez parler de *complexité* d'un algorithme, ce sera par défaut **toujours** la complexité maximale.
{% endinfo %}

Il arrive que certains algorithmes aient un comportement très différent selon les entrées. Parler seulement de la complexité (nombre maximum d'opérations) ne permet alors pas de le caractériser complètement. On parlera  aussi de :

{% note %}
La **complexité minimale** d'un algorithme est le **nombre minium d'opérations basiques** effectué par celui-ci pour des entrées **de taille totale donnée**. Elle sera donnée en $\mathcal{O}(f(N))$, où $N$ est une variable rendant compte de la taille des données.
{% endnote %}

Lorsque l'on calcule une complexité (maximale ou minimale) sous la forme d'un $\mathcal{O}(f(N))$, on tentera bien sur de trouver la fonction $f(N)$ la plus petite possible.

### <span id="temps-exécution"></span> Temps d'exécution

Un moyen efficace de mesurer la complexité d'un algorithme écrit sous la forme d'un code exécutable est de mesurer le temps mis par son exécution pour un jeu d'entrée donné.

{% note %}
La **complexité en temps** d'un algorithme est le temps mis pour l'exécuter en utilisant un jeu de donné **pour lequel la complexité (max) est atteinte** et d'une taille totale donnée.
{% endnote %}

Le temps pris sera bien sur différent si l'on prend une machine plus puissante ou si l'on change le code de l'algorithme mais **l'évolution de la complexité en temps par rapport à la taille des données est toujours proportionnelle à la complexité**. Pour le voir, il suffit de mesurer la durée d'exécution de chaque instruction basique et de la borner par le max :

{% note %}
Complexité et complexité en temps sont deux notions équivalentes.
{% endnote %}

{% attention %}
Si vous ne prenez **pas** un jeu de donné pour lequel la complexité de l'algorithme est atteinte, vous ne mesurez **pas** la complexité temporelle de l'algorithme...
{% endattention %}

### Taille mémoire

{% note %}
La **complexité en espace** d'un algorithme est le nombre maximum de cases mémoires utilisées pour l'exécuter en utilisant un jeu de donnés de taille donnée.
{% endnote %}

Comme la complexité, on la mesurera avec des $\mathcal{O}$.

La complexité en espace n'est pas forcément atteinte pour un jeu de données donnant la complexité de l'algorithme, mais **la complexité en espace sera toujours plus faible que la complexité** (visiter une case mémoire nécessitant une opération élémentaire).

### Complexité de méthodes ou de structures

Lorsque l'on code un algorithme, on a coutume (et c'est très bien) d'utiliser des fonctions, des méthodes ou des structures que l'on n'a pas écrites. Il faut en revanche bien connaître leurs complexités pour ne pas commettre d'erreur de calcul.

{% note %}
Lorsque l'on calcule une complexité toutes les méthodes et fonctions doivent être examinées
{% endnote %}

#### Complexité de structure

En informatique, les **objets que l'on manipule ont des types**. On connaît déjà des [objets basiques](../pseudo-code#objets-basique){.interne} qui sont de types booléens, entiers, réels ou encore chaines de caractères pour lesquels toutes les opérations basiques que l'on peut effectuer avec eux sont en $\mathcal{O}(1)$ opérations. Ce n'est plus le cas lorsque l'on utilise des type plus complexes, composé de types basiques comme les conteneurs comme les tableaux, ou encore les listes de python. Pour pouvoir calculer la complexité d'un algorithme les utilisant, il faut connaître les complexités de ses opérations. Souvent, les opérations suivantes suffisent :

{% note %}
Pour chaque type de donnée, il faut connaître la complexité de :

* la création d'un objet de ce type
* la suppression d'un objet de ce type
* chaque méthode liée au type

{% endnote %}

Prenons le type [tableau](../structure-de-données/tableau){.interne} comme exemple. Un tableau est un conteneur pouvant contenir $n$ objets (on appelle $n$ la taille d'un tableau). On peut accéder et affecter un objet au tableau grâce à un indice allant de $0$ à $n-1$ : si `t`{.language-} est un tableau `t[i]`{.language-} correspond à l'objet d'indice $i$ du tableau.

Avec un tableau on peut faire uniquement 3 choses :

* **créer un tableau** de taille $n$ en $\mathcal{O}(1)$ opérations
* **supprimer un tableau** est possible en $\mathcal{O}(1)$ opérations
* **récupérer et affecter** l'objet d'indice $i$ du tableau (objet `t[i]`{.language-}) se fait en $\mathcal{O}(1)$ opérations

{% attention %}
il est **impossible** de redimensionner un tableau. Sa taille est **fixée** à la création. Toute méthode qui vise à augmenter ou diminuer la taille d'un tableau recrée un nouveau tableau et copie tous les éléments de l'ancien tableau dans le nouveau.
{% endattention %}

Le langage python ne connaît pas les tableaux. Il utilise le type [liste](../structure-de-données/liste){.interne} à la place. Une liste peut être vue comme l'évolution du type tableau. On donne ici juste les complexités de cette structure pour que vous puissiez les utiliser dans vos programmes :

* **créer et supprimer une liste** de taille $n$ en $\mathcal{O}(1)$ opérations
* **récupérer et affecter** l'objet d'indice $i$ d'une liste (objet `t[i]`{.language-}) se fait en $\mathcal{O}(1)$ opérations
* **augmenter la taille** d'une liste d'un élément se fait en $\mathcal{O}(1)$ opérations
* **supprimer le dernier élément** d'une liste se fait en $\mathcal{O}(1)$ opérations

{% note %}
Une liste peut-être vue comme un tableau dont on peut augmenter ou diminuer la taille **par la fin** en $\mathcal{O}(1)$ opérations.
{% endnote %}

{% attention %}
Ne confondez pas liste et [liste chaînée](https://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e) ce n'est pas du tout la même structure !
{% endattention %}

#### Fonction et méthodes données

Il faut connaître les différentes complexités des méthodes et fonctions utilisées. Ne vous laissez pas méprendre. Ce n'est pas parce qu'elle font 1 seule ligne que leur complexité est en $\mathcal{O}(1)$. Par exemple la complexité de la méthode `max`{.language-} de python, qui prend en entrée une liste `l` :

```python
l = [1, 3, 2, 6, 4, 5]
print(l.max())
```

Est de complexité $\mathcal{O}(n)$  où $n$ est la taille de la liste `l` et pas $\mathcal{O}(1)$. Il **faut** en effet parcourir tous les éléments d'une liste (a priori non triée) pour en trouver le maximum.

{% attention %}
Lorsque vous utilisez des fonctions et des méthodes en python, **vérifier toujours** la complexité de celles-ci. Ce n'est pas toujours $\mathcal{O}(1)$.
{% endattention %}

## <span id="exemple-recherche"></span> Exemple de la recherche d'un élément dans un tableau

Prenons par exemple l'algorithme suivant, écrit en python :

```python#
def est_dans_tableau(valeur, tableau):
    for x in tableau:
        if x == valeur:
            return True
    return False
```

Cet algorithme recherche si le paramètre `valeur`{.language-} est un élément de `tableau`{.language-}.

Calculons ses complexités maximale et minimale. Commençons par regarder les complexités de chaque ligne :

1. définition de la fonction : $C_1 = \mathcal{O}(1)$
2. une boucle `for`{.language-} de $k$ itérations
3. un test entre 2 variables : $C_3 = \mathcal{O}(1)$
4. un retour de fonction $C_4 = \mathcal{O}(1)$
5. un retour de fonction : $C_5 = \mathcal{O}(1)$

Comme il y a 2 retours de fonctions (lignes 4 et 5), la complexité sera soit :

* $C = C_1 + k \cdot (C_3) + C_5 = \mathcal{O}(1) + k \cdot (\mathcal{O}(1)) + \mathcal{O}(1)$ si on utilise la sortie de la ligne 5 (on est jamais passé par le ligne 4)
* $C' = C_1 + k \cdot (C_3) + C_4 = \mathcal{O}(1) + k \cdot (\mathcal{O}(1) + \mathcal{O}(1))$ si on utilise la sortie de la ligne 4 en passant lors de la dernière itération de la boucle `for`{.language-} de la ligne 2

Les deux cas se simplifient en : $\mathcal{O}(k)$

En effet $\mathcal{O}(1) + \mathcal{O}(1) = \mathcal{O}(1)$ on a $C = C' = \mathcal{O}(1) + k \cdot (\mathcal{O}(1))$. De là, $C = C' = \mathcal{O}(1) + \mathcal{O}(k) = \mathcal{O}(k)$

On cherche le cas le pire, c'est à dire lorsque $k$ est maximum, donc lorsque la boucle `for`{.language-} parcourt tout le tableau, c'est à dire pour deux cas :

* l'élément recherché n'est pas dans le tableau
* l'élément recherché est le dernier élément du tableau

On en conclut que :

{% note %}
La complexité de l'algorithme `est_dans_tableau`{.language-} est $\mathcal{O}(n)$ où $n$ est la taille du tableau qui est un paramètre d'entrée.
{% endnote %}

La complexité minimale est quant à elle atteinte lorsque l'on ne parcourt pas notre boucle, c'est à dire lorsque la valeur recherchée est la 1ère valeur du tableau :

{% note %}
La complexité minimale de l'algorithme `est_dans_tableau`{.language-} est $\mathcal{O}(1)$.
{% endnote %}

## Types de complexité en algorithmie

> BD cut ici

## Règles de calcul de complexité

On va donner ici quelques règles de calcul de complexité pour que vous puissiez estimer rapidement la complexité d'un algorithme simple.

### Une boucle simple

Lorsque l'on a une boucle où le nombre de fois où l'on va rentrer dedans est évident.

Par exemple :

```text

tant que condition:
    bloc d'instructions

```

{% note %}
La complexité est : $\mathcal{O}$(nombre de fois ou la condition est remplie) $\cdot$ ($\mathcal{O}$(complexité de la vérification de la condition) + $\mathcal{O}$(complexité du bloc d'instruction))
{% endnote %}

Souvent, $\mathcal{O}$(complexité de la vérification de la condition) sera égal à $\mathcal{O}(1)$ et pourra ne pas en tenir compte dans le calcul. C'est le cas, entre autre pour une boucle tant que :

```text

pour chaque element de structure:
    bloc d'instructions

```

{% note %}
La complexité est : $\mathcal{O}$(nombre d'éléments de la structure) $\cdot$ $\mathcal{O}$(complexité du bloc d'instruction)
{% endnote %}

Si le bloc d'instructions est une suite d'instructions de complexité $\mathcal{O}(1)$, on pourra ne pas en tenir compte dans le calcul et la complexité est alors égale à la taille de la structure.

En conclusion :

{% note %}
Si le bloc d'instruction est une suite d'instructions de complexité $\mathcal{O}(1)$ et que la vérification de la fin de la boucle est $\mathcal{O}(1)$, la complexité de la boucle est égal au nombre de fois où l'on effectue la boucle
{% endnote %}

### Boucles imbriquées indépendantes

Plusieurs boucles imbriquées dont dont le nombre de fois où l'on va rentrer dedans est indépendant des autres boucles. Par exemple :

```text
boucle 1 exécutée n1 fois:
    boucle 2 exécutée n2 fois:
        ...
            boucle i exécutée ni fois:
                bloc d'instructions
```

On peut utiliser la règle précédente de façon récursive, la partie $\mathcal{O}$(complexité du bloc d'instruction) contenant elle même une ou plusieurs boucles.

{% note %}
Si la condition à remplir pour rentrer dans la boucle est en $\mathcal{O}(1)$, la complexité des boucles imbriquées est le produit du nombre de fois où l'on rentre dans chaque boucle pris indépendamment multiplié par la complexité du bloc d'instructions.
{% endnote %}

Exemple :

```python
total = 0
de i = 1 à n - 1 faire:
    de j = 1 à n faire:
        total = total + 1
Rendre total
```

La boucle en $i$ est exécuté $n-1$ fois ($i$ va de 1 à $n-1$), donc $\mathcal{O}(n)$ fois. La boucle en $j$ va également être exécutée $\mathcal{O}(n)$ fois indépendamment de la boucle en $i$. Enfin la complexité du bloc d'instruction est $\mathcal{O}(1)$, la complexité totale des deux boucles imbriquées vaut :

<p>
\[
\underbracket{\mathcal{O}(n)}_{\mbox{boucle en i}} \cdot \underbracket{\mathcal{O}(n)}_{\mbox{boucle en j}} \cdot \underbracket{\mathcal{O}(1)}_{\mbox{bloc d'instructions}}
 = \mathcal{O}(n^2)
\]
</p>

{% info %}
Ne comptez pas trop précisément le nombre de fois où l'on rentre dans une boucle $n-3$ exécutions de la boucle pouvant être avantageusement remplacé par $\mathcal{O}(n)$
{% endinfo %}

### <span id="règle-croissance"></span>Boucles dépendantes mais monotones

Il arrive souvent que les boucles imbriquées d'un algorithme soient dépendantes les unes des autres. Dans le cas général on ne peut pas factoriser le calcul de la complexité et il faut alors dérouler tout l'algorithme en additionnant les complexités de chaque ligne comme s'il n'y avait pas de boucles.

Il existe cependant un cas pratique (et qui arrive assez souvent) où l'on peut factoriser :

{% note %}
Si une boucle s'exécute un nombre variable de fois, mais que cette variation est croissante (respectivement décroissante), on peut considérer pour le calcul de la complexité qu'elle s'exécute à chaque fois de l'ordre du maximum de fois.
{% endnote %}

On va vérifier cela avec un exemple :

```python#
total=0
de i=1 à n-1 faire :
    de j=i+1 à n faire :
        total=total+1
Rendre total
```

Le nombre de fois où la boucle en $j$ est exécutée est un nombre variable de fois qui dépend de la valeur de $i$. Comme $i$ va croître, le nombre de fois où cette boucle va s'exécuter va décroître. Si l'on applique la règle  on peut dire qu'elle va s'exécuter de l'ordre de $\mathcal{O}(n)$ fois comme dans l'exemple de la partie précédente. La complexité de l'algorithme est donc de $\mathcal{O}(n^2)$.

Refaisons le calcul en décomposant toutes les instructions, comme on le ferait dans le cas général, pour voir que notre règle est valide (et donnera aussi une idée de la preuve de cette règle) :

* ligne 1 : $\mathcal{O}(1)$
* itération pour $i=1$:
  * une affectation $i=1$ : $\mathcal{O}(1)$
  * boucle pour $j=1$:
    * une affectation de $j$ :  $\mathcal{O}(1)$
    * la ligne 4 :  $\mathcal{O}(1)$
    * le tout $n-1$ fois
* itération pour $i=2$:
  * une affectation $i=2$ : $\mathcal{O}(1)$
  * boucle pour $j=2$:
    * une affectation de $j$ :  $\mathcal{O}(1)$
    * la ligne 4 :  $\mathcal{O}(1)$
    * le tout $n-2$ fois
* ...
* itération pour $i=n-1$:
  * une affectation $i=n-1$ : $\mathcal{O}(1)$
  * boucle pour $j=n-1$:
    * une affectation de $j$ :  $\mathcal{O}(1)$
    * la ligne 4 :  $\mathcal{O}(1)$
    * le tout $1$ fois
* ligne 5 : $\mathcal{O}(1)$

Notre complexité totale est donc :

<p>\[
\begin{aligned}
    \mathcal{O}(1) + \\
    (\mathcal{O}(1) + (n-1) \cdot (\mathcal{O}(1) + \mathcal{O}(1))) + \\
    (\mathcal{O}(1) + (n-2) \cdot (\mathcal{O}(1) + \mathcal{O}(1))) + \\
    \dots\\
 + (\mathcal{O}(1) + (1) \cdot (\mathcal{O}(1) + \mathcal{O}(1))) \\
 + \mathcal{O}(1)
\end{aligned}
\]</p>

Comme $\mathcal{O}(1) + \mathcal{O}(1) = \mathcal{O}(1)$, on a :

<p>\[
\begin{aligned}
    \mathcal{O}(1) + \\
    (\mathcal{O}(1) + (n-1) \cdot \mathcal{O}(1)) + \\
    (\mathcal{O}(1) + (n-2) \cdot \mathcal{O}(1)) + \\
    \dots\\
 + (\mathcal{O}(1) + 1 \cdot \mathcal{O}(1)) \\
 + \mathcal{O}(1)
\end{aligned}
\]</p>

Ce qui donne :

<p>\[
\begin{aligned}
    \mathcal{O}(1) + \\
    n \cdot \mathcal{O}(1) + \\
    (n-1) \cdot \mathcal{O}(1) + \\
    \dots\\
 + \mathcal{O}(1)
\end{aligned}
\]</p>

et donc notre complexité vaut :

$$\mathcal{O}(1) + \sum_{1\leq i \leq n} i \cdot \mathcal{O}(1)$$

Comme la somme des n premiers entiers vaut $\frac{(n+1)(n)}{2}$ notre complexité devient :

$$\mathcal{O}(1) + \frac{(n+1)(n)}{2} \mathcal{O}(1)$$

Ce qui est de l'ordre de : $\mathcal{O}(\frac{(n+1)(n)}{2})$. Or :

$$\mathcal{O}(\frac{(n+1)(n)}{2}) = \mathcal{O}(\frac{n^n + n}{2}) = \mathcal{O}(n^2 +n) = \mathcal{O}(n^2)$$

On retrouve bien le résultat attendu.

### Complexité d'algorithmes récursifs

Un algorithme récursif est un algorithme qui s'appelle lui-même jusqu'à ce qu'on arrive à une condition d'arrêt qui stope la récursion. On en calcule la complexité en posant une équation qu'il faut résoudre :

{% note %}
Pour calculer la complexité d'un algorithme récursif en fonction de la taille $n$ de l'entrée, on pose que $C(n)$ est la complexité et l'on utilise cette fonction pour estimer la complexité des appels récursifs. Une fois les complexités des éléments d'arrêts estimés, trouver $C(n)$ revient à résoudre une équation de récurrence.
{% endnote %}

Pour illustrer ce calcul, prenons l'exemple suivant :

```python#
fonction maximum(t, n):
    si n == 1
        rendre t[0]
    sinon:
        x = maximum(t, n-1)
        si x > t[n-1]:
            rendre x
        sinon:
            rendre t[n-1]
```

On exécute cette fonction avec comme paramètres initiaux un tableau nommé `t`{.language-} de taille `n`{.language-}. On vérifie qu'avec ces paramètres initiaux :

1. l'algorithme converge bien
2. il rend bien le maximum de `t`{.language-}

La taille des données est de l'ordre de la taille du tableau, c'est à dire le paramètre $n$. On pose alors que la complexité de notre algorithme pour un tableau de taille $n$ est : $C(n)$. De là, ligne à ligne :

1. définition d'une fonction $\mathcal{O}(1)$
2. une comparaison entre une constante et une variable : $\mathcal{O}(1)$
3. retour de fonction d'un élément d'un tableau : $\mathcal{O}(1)$
4. —
5. une affectation, plus l'appel à la fonction avec un tableau de taille $n-1$ (sa complexité est donc de $C(n-1)$ par définition) : $\mathcal{O}(1) + C(n-1)$
6. un test d'un élément dans un tableau et d'une variable : $\mathcal{O}(1)$
7. retour de fonction : $\mathcal{O}(1)$
8. —
9. retour de fonction d'un élément d'un tableau : $\mathcal{O}(1)$

Ce qui donne en sommant le tout :

$$
\begin{array}{lcl}
C(n) & = & \mathcal{O}(1) + \\\\
&  & \mathcal{O}(1) + \\\\
&  & \mathcal{O}(1) + \\\\
&  & \mathcal{O}(1) + C(n-1) + \\\\
& & \mathcal{O}(1) + \\\\
& & \mathcal{O}(1) + \\\\
& & \mathcal{O}(1) \\\\
& = & 8 \cdot \mathcal{O}(1) + C(n-1) \\\\
& = & \mathcal{O}(1) + C(n-1) \\\\
\end{array}
$$

La complexité est définie par l'équation de récurrence $C(n) = \mathcal{O}(1) + C(n-1)$. Notre condition d'arrêt est obtenue pour `n`{.language-} valant 1 et dans ce cas on a $C(1) = \mathcal{O}(1)$

Trouver $C(n)$ revient à résoudre :

<p>\[
\left\{
    \begin{array}{lcl}
        C(n) & = & \mathcal{O}(1) + C(n-1)\\
        C(1) & = & \mathcal{O}(1)
    \end{array}
\right.
\]<p>

On a alors :

<div>
$$
\begin{array}{lcl}
    C(n) & = & \mathcal{O}(1) + C(n-1) \\
    & = & \mathcal{O}(1) + \mathcal{O}(1) + C(n-2) = 2 \cdot \mathcal{O}(1) + C(n-2)\\
    & = & 3 \cdot \mathcal{O}(1) + C(n-3) \\
    & = & \dots \\
    & = & i \cdot \mathcal{O}(1) + C(n-i) \\
    & = & \dots \\
    & = & (n-1) \cdot \mathcal{O}(1) + C(1) = (n-1) \cdot \mathcal{O}(1) + \mathcal{O}(1) \\
    & = & n \cdot \mathcal{O}(1) = \mathcal{O}(n) \\
\end{array}
$$
</div>

Au final, on trouve que la complexité $C(n)$ de notre algorithme est en $\mathcal{O}(n)$ où $n$ est la taille du tableau placé initialement en paramètre.

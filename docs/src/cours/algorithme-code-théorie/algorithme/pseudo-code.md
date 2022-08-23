---
layout: layout/post.njk 
title: Pseudo-code

eleventyNavigation:
  key: "Pseudo-code"
  parent: Algorithme
---

{% chemin %}
{%- for page in collections.all | eleventyNavigationBreadcrumb(eleventyNavigation.key, { includeSelf: true}) -%}
{% if not loop.first %} / {%endif%} [{{page.title}}]({{ page.url | url }})
{%- endfor -%}
{% endchemin %}
{% prerequis "**Prérequis** :" %}

* [Définition d'un algorithme](../définition)

{% endprerequis %}

<!-- début résumé -->

Définition du pseudo-code et des différentes instructions utilisables.

<!-- end résumé -->

La [définition générale d'un algorithme](../définition) ne spécifie rien sur les instructions à utiliser, juste qu'elles doivent être décrites en un nombre fini de mots. Un ***pseudo-code*** est une proposition d'instructions possibles pour décrire un algorithme, compréhensibles par un humain.

Ce n'est cependant pas une langue car il n'y a pas de place pour l'ambiguïté ni les inventions : tout doit y être rigoureusement défini, et chaque étape élémentaire doit être réalisable en un temps fini par un humain.

Ce n'est pas non plus un langage informatique dont le but est d'être compris par un ordinateur.

## Éléments de pseudo-code { #règles }

Un pseudo-code est une succession de lignes qui seront exécutées ***en séquence*** les unes à la suite des autres. Chaque ligne est composée d'une instruction qu'il faut réaliser en entier avant de passer à la ligne suivante.

Il y a quelques instructions basiques qu'auront tous les pseudo-codes que vous pouvez utiliser, ce sont les ***instructions basiques***.

### Instruction basique { #instruction-basique }

Il y a 3 types d'instruction basique :

* [manipulation d'objets basiques](#objets-basique)
* [exécution conditionnelle d'instructions](#tests)
* [répétition d'instructions](#répétition)

Ce sont les atomes d'un pseudo-code. On considère qu'on ne peut pas les scinder en plusieurs autres instructions.

### Manipulations d'objets basiques { #objets-basique }

On doit pouvoir manipuler et stocker des *objets*. On appelle ici ***objets basiques*** les booléens, les entiers, les réels et les chaînes de caractères.

* **utiliser des objets**
  * opérations sur les entiers et/ou réels :
    * arithmétique : addition (`+`), soustraction (`-`), multiplication (`*`), division (`/`)
    * opérations usuelles : prendre la valeur entière, valeur absolue, le modulo
    * logique : égalité (avec le signe `==` ou `=`), plus petit que (`<`), plus grand que (`>`), plus petit ou égal (`≤`), plus grand ou égal (`≥`)
  * opérations sur les booléens : "négation logique" (non, `NOT`, $\neg$), "et logique" (et, `&&`, `AND`), "ou logique" (ou, `||`, `OR`)
* **utiliser des variables**. Une variable est un nom qui est associé à un objet.
  * affecter des variables : `a = 3` défini le nom `a` (appelé *variable*) qui vaut `3`. (vous verrez parfois utilisé $a \leftarrow 3$ à la place de $a = 3$ pour qu'il n'y ait pas de confusion si l'on utilise `=` pour l'égalité)
  * lire une variable. Si j'ai affecté `3` à la variable `a`, je dois pouvoir l'utiliser, par exemple en écrivant `b = a * 3`
* **utiliser un tableau**. Un tableau est un conteneur. Il contient $n$ objets où $n$ est sa **longueur**. On peut voir ça comme une variable contenant $n$ objets plutôt qu'un seul. On peut accéder à, et/ou modifier un élément stocké dans le tableau en lui donnant son **indice**, allant de $0$ à $n-1$ : `t[i]` correspond à l'objet d'indice $i$ d'un tableau stocké dans la variable `t`. On considère souvent une chaîne de caractère comme un tableau de caractères.

Les objets sont stockés en mémoire, que l'on identifiera à un gigantesque tableau fini. On considérera que l'on peut stocker sur une case mémoire :

* un entier
* un réel
* un caractère

Les chaînes de caractères et les tableaux sont stockées sur des cases mémoires continues, ce qui permet de connaître l'emplacement de l'élément d'indice $i$ en une opération basique si l'on connaît l'emplacement du 1er élément (emplacement du premier élément + i).

### Blocs

Lier les instructions en blocs. On va utiliser ici le formalisme de python pour définir un bloc :

```text
type de bloc:
    instruction 1
    instruction 2
    ...
    instruction n
```

On décale les instructions du bloc de sa définition. C'est un truc clair qui permet de voir du premier coup d'œil les instructions d'un bloc.

### Exécution conditionnelle d’instructions { #tests }

On veut pouvoir exécuter un bloc de code si une condition logique est vérifiée :

```text
si (condition logique) est vraie:
    instruction 1
    ...
    instruction n
```

Cette instruction basique peut avoir plein de variantes comme :

```text
si (condition logique) est vraie:
    instruction 1
    ...
    instruction n
sinon:
    instruction 1
    ...
    instruction n'
```

ou encore :

```text
si (condition logique) est vraie:
    instruction 1
    ...
    instruction n
sinon si (autre condition logique) est vraie:
    instruction 1
    ...
    instruction n'
```

Ou tout mix de tout ça, du moment que c'est clair !

{% info %}
On peut dériver toutes les variantes de la forme initiale.
{% endinfo %}

### Répétition { #répétition }

On doit pouvoir répéter un bloc tant qu'une condition logique est vérifiée (boucle *while*):

```text
tant que (condition logique) est vraie:
    instruction 1
    ...
    instruction n
```

Il existe une variation de ce bloc très utile (boucle *for*):

```text
pour chaque élément x d'un tableau:
    instruction 1
    ...
    instruction n
```

On exécutera alors le bloc autant de fois qu'il y a d'éléments dans le tableau et à chaque itération du bloc, la variable `x` vaudra un autre élément du tableau. On prendra les éléments du tableau par indice croissant.

{% info %}
On peut dériver la variante `pour chaque` de la forme initiale `tant que`.
{% endinfo %}

### Complexité { #complexité }

La complexité d'un pseudo-code est le nombre d'instructions basiques utilisées pour l'exécuter. La complexité d'un bloc d'instruction est égale à la somme des complexités des instructions qui le composent.

Par exemple le pseudo-code suivant :

```text#
x = 30
if ((x > 12) AND (x < 36)):
    z = x * "coucou"
```

1. on affecte un objet à x : 1 instruction
2. Pour faire cette instruction il faut :
   * faire `x > 12`. Pour cela :
     * on récupère la valeur de `x` : 1 instruction
     * on effectue la comparaison : 1 instruction
   * faire `x < 36`. Pour cela :
     * on récupère la valeur de `x` : 1 instruction
     * on effectue la comparaison : 1 instruction
   * faire l'instruction `AND`: 1 instruction
   * fair le `if`: 1 instruction
3. on commence par récupérer la valeur de `x` (1 instruction) puis affecte le résultat d'une opération élémentaire (2 instructions) : donc un total de 3 instructions

Un nombre total d'instructions de 10.

### Nom des termes utilisés ?

Leurs noms importent peu, seuls leurs fonctions sont importantes. Vous pouvez donc utiliser les mots qui vous plaisent, du moment qu'ils sont compréhensible pour vous et — surtout — pour votre lecteur. Le plus souvent, on utilisera un mix de python et de français, ou d'anglais.

Les trois pseudo-code suivant sont ainsi équivalent :

```python
for i in range(10):
    affiche à l'écran i
```

```python
pour chaque entier i allant de 0 à 9:
    print(i)
```

```c
for (i=0 ; i < 10 ; i++) {
    printf(i);
}
```

## Pseudo-code

Le pseudo-code d'un algorithme va contenir, en plus de ses instructions, un nom, des entrées et souvent une sortie. Par exemple :

```text
Nom : recherche
Entrées : 
    t : un tableau d'entiers
    x : un entier
Programme :
    pour chaque élément e de t:
        si e == x:
            Retour vrai
    Retour faux 
```

ou de manière équivalente, en un mélange de python et de français :

```python#
def recherche(t, x):
    pour chaque élément e de t:
        si e == x:
            return vrai
    return faux
```

Ceci permet ensuite de définir des fonctions pour écrire des algorithmes de façon plus concise.

### Fonctions

Une fonction est un algorithme. Une fois que sa complexité est connue, on peut l'utiliser comme une instruction dans un pseudo-code.

```text
nom(entrée 1, ..., entrée n)
```

{% attention %}
Ne confondez pas `nom`qui est l'algorithme et `nom(a, b)` qui est le résultat de son exécution avec les paramètres `a` et `b`
{% endattention %}

Si l'algorithme a un retour, on peut directement l'utiliser, en l'affectant à une variable par exemple :

```text
variable = nom(entrée 1, ..., entrée n)
```

{% info %}
Les fonctions nous donnent accès à la récursivité : Il suffit que notre pseudo-code s'appelle lui-même comme une fonction.
{% endinfo %}

Si on veut utiliser le pseudo code *recherche* défini plus haut, cela pourrait être une instruction du type : `trouve = recherche(tab, 3)`. On affecte la sortie de l'algorithme `recherche` avec comme paramètres `tab` (le tableau d'entier) et `3` (un entier) à la variable `trouve`.

Il est important de voir que lorsque l'on exécute une fonction, les variables qu'elle crée existeront dans un espace à elle, pas dans celui du pseudo-code appelant. Ainsi dans le code suivant :

```python#
e = 4
t = [1, 2, 6]
trouve = recherche(t, 6)
affiche à l'écran e
```

On affichera bien 4 à l'écran et pas 6 (le nom de variable `e` défini dans recherche reste dans recherche).

{% attention %}
Lorsque l'on calcule la complexité d'un pseudo-code utilisant des fonctions, il faut compter le nombre d'instructions de l'exécution des fonctions !
{% endattention %}

Prenons par exemple le code précédent et comptons les instructions utilisées ligne à ligne :

1. affectation d'un variable : 1 instruction
2. affectation d'un variable : 1 instruction
3. affectation d'une variable (1 instruction) plus l'exécution de la fonction recherche (ligne à ligne) :
   1. affectation des paramètres :
      * pour le premier paramètre il faut trouver l'objet associé à t : 1 instruction
      * pour le second paramètre, c'est un objet donc il n'y a rien à faire : 0 instruction
      * affectation du premier paramètre à la variable locale t : 1 instruction
      * affectation du second paramètre à la variable locale e : 1 instruction
   2. une boucle de 3 itérations
   3. un test
      * on trouve les objets associées à t et e : 2 instructions
      * on teste l'égalité : 1 instruction
      * on fait le `if` : 1 instruction
   4. on arrive à cette ligne à la troisième itération : 1 instruction
4. on ne sait pas combien d'opération est nécessaire pour afficher quelque chose à l'écran. disons que ça prend $P$ instructions

Au total on eu besoin de $1+1+1+\underbracket{(1+0+1+1+3 \cdot (2+1+1) + 1)}_{\mbox{recherche(t, 6)}} + P$
instructions c'est à dire $19+P$ instructions.

### Instructions avancées

Si l'on devait à chaque pseudo-code redéfinir tout les algorithmes qu'on utilise ce serait vraiment fastidieux. On utilise souvent des fonctions non basiques (comme l'affichage à l'écran qu'on a déjà vu) ou des structures plus élaborées (les listes par exemples qui sont des extensions des tableaux). Il faudra cependant toujours connaître les complexités de ce qu'on utilise.

Par exemple pour les listes, qui sont des tableaux redimensionnables :

* complexité d'ajout d'un élément à la fin de la liste : coût de 1 instruction
* complexité de l'ajout d'un élément pas à la fin de la liste : coût de la taille de la liste instructions
* complexité de la suppression d'un élément à la fin de la liste : coût de 1 instruction
* complexité de la suppression d'un élément pas à la fin de la liste : coût de la taille de la liste instructions
* usage comme un tableau : 1 instruction

Si vous utilisez des méthodes d'objets comme vous avez l'habitude de le faire en python (comme une `ma_liste.index("?")`{.language-}, `x in ma_chaîne_de_caractères`{.language-}) ou des structures compliquées (télécharger un fichier d'internet) vous avez le droit mais vous **devez** en connaître le coût : la complexité, les cas d'usage (comme être connecté à internet), etc.

## Comment écrire du pseudo-code

Le pseudo-code est une représentation d'un algorithme. Son but est de :

* démontrer que l'algorithme fait bien ce qu'on pense qu'il fait
* calculer ses performances :
  * nombre d'instructions utilisées
  * nombre de cases mémoire utilisées

Pour réaliser cela le plus simplement possible, on voudra **toujours** :

* qu'il soit lisible,
* qu'il soit juste,
* en connaître les performances.

### Lisible

Le but d'un algorithme papier est d'être compris. On utilisera pour l'écrire une série de règles compréhensibles par tout le monde : le pseudo-code. Ce n'est ni une langue ni un langage.

préférez des noms de variables explicites et n'hésitez pas à séparer votre pseudo-code en fonctions pour qu'il soit plus clair.

{% note "N'oubliez pas :" %}
Les fonctions doivent être décrites si elles ne sont pas immédiatement compréhensibles.
{% endnote %}

### Preuve

On **démontrera** le fonctionnement de l'algorithme en utilisant des preuves mathématiques.

### Performances

On calculera la complexité de l'algorithme :

* nombre d'instructions
* place en mémoire

Ces complexités dépendent des paramètres de l'algorithme et, parfois de circonstances extérieures comme l'état du réseau par exemple.

## Expressivité d'un pseudo-code

Un pseudo-code est a priori un cas particulier d'algorithme puisque l'on se limite à un nombre fixé d'instructions et à une construction rigide et normée de ceux ci (uniquement des blocs avec une instruction par ligne). Mais toutes les tentatives de généralisation ont échoués : elle n'ont jamais permis de faire des algorithmes impossible à réaliser en pseudo-code.

On pense donc (mais ce n'est pas démontré) que :

{% note "**Thèse de Church-Turing**" %}
Les notions d'algorithme et de pseudo-code sont équivalentes.

Tout algorithme peut être écrit en pseudo-code.
{% endnote %}

En bon informaticien, on considérera la thèse de Church-Turing vérifiée et :

* on écrira tous nos algorithmes en pseudo-code
* pseudo-code et algorithme seront considérés comme synonyme

{% note %}
Si ces considérations vous intéressent, n'hésitez pas à jeter un coup d'œil à ce lien :
<https://plato.stanford.edu/entries/turing-machine/#ThesDefiAxioTheo>

C'est en Anglais, mais c'est très bien.
{% endnote %}

Plus précisément, on peut ramener l'ensemble des [instructions d'un pseudo-code](https://en.wikipedia.org/wiki/Structured_program_theorem) (même si ce sera plus compliqué d'écrire le code) à trois types d'instructions et à trois façon de les exécuter :

{% note %}

Une ***instruction***  est soit :

* une affectation d'un entier (voir même juste un bit) à une variable
* une lecture d'une variable
* un test d'égalité entre deux variables

Un pseudo-code doit pouvoir :

* exécuter une instruction puis une autre, **séquentiellement**
* exécuter une instruction si un test d'égalité est vrai
* exécuter un bloc d'instructions tant qu'un test d'égalité est vrai

Tous les pseudo-codes utilisant les 6 règles ci-dessus auront alors la même expressivité : on pourra faire exactement les mêmes choses.

{% endnote %}

Nous n'utiliserons donc jamais des instructions aussi simple car elles ne permettent pas de faire plus (ou moins) de chose qu'avec notre pseudo-code.

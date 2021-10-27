---
layout: page
title:  "algorithme : pseudo-code"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithme]({% link cours/theorie-pratiques-algorithmique/1-algorithme/index.md %}) / [pseudo-code]({% link cours/theorie-pratiques-algorithmique/1-algorithme/pseudo-code.md %})
{: .chemin}

Le pseudo-code est la version papier d'un algorithme. Il décrit les différentes étapes permettant de dérouler un algorithme de son initialisation à son retour. Son but est d'être compréhensible par un humain. Ce n'est cependant pas une langue car il n'y a pas de place pour l'ambiguïté ni les inventions : tout doit y être rigoureusement défini, et chaque étape élémentaire doit être réalisable par un humain. Ce n'est pas un plus un langage informatique dont le but est d'être compris par un ordinateur.

## éléments de pseudo-code

Un pseudo-code est une succession de lignes qui seront exécutées **en séquence** les unes à la suite des autres. Chaque ligne est composée d'une instruction qu'il faut réaliser en entier avant de passer à la ligne suivante.

Il y a quelques instructions basiques qu'auront tous les pseudo-codes que vous pouvez utiliser, ce sont les **instructions basiques**. Elles sont de 3 ordres :

* [manipulation d'objets simples](#manipulations-dobjets-simples)
* [exécution conditionnelle d'instructions](#tests)
* [répétition d'instructions](#répétition)

### manipulations d'objets simples

On doit pouvoir manipuler et stocker des *objets*. On appelle ici objets simples les booléens, les entiers, les réels et les chaines de caractères.

* **utiliser des objets**
  * opérations sur les entiers et/ou réels :
    * arithmétique : addition (`+`), soustraction (`-`), multiplication (`*`), division (`/`)
    * opérations usuelles : prendre la valeur entière, valeur absolue, le modulo
    * logique : égalité (avec le signe `==` ou `=`), plus petit que (`<`), plus grand que (`>`), plus petit ou égal (`≤`), plus grand ou égal (`≥`)
  * opérations sur les booléens : négation (non, `NOT`, $\neg$), et logique (et, `&&`, `AND`), ou logique (ou, `||`, `OR`)
* **utiliser des variables**. Une variable est un nom qui est associé à un objet.
  * affecter des variables : `a = 3` défini le nom `a` (appelé *variable*) qui vaut `3`. (vous verrez parfois utilisé $a \leftarrow 3$ à la place de $a = 3$ pour qu'il n'y ait pas de confusion si l'on utilise `=` pour l'égalité)
  * lire une variable. Si j'ai affecté `3` à la variable `a`, je doit pouvoir l'utiliser, par exemple en écrivant `b = a * 3`
* **utiliser un tableau**. Un tableau est un conteneur. Il contient $n$ objets où $n$ est sa **longueur**. On peut voir ça comme une variable contenant $n$ objet plutôt qu'un seul. On peut accéder à, et/ou modifier un élément stocké dans le tableau en lui donnant son **indice**, allant de $0$ à $n-1$ : `t[i]` correpond à l'objet d'indice $i$ d'un tableau stocké dans la variable `t`. On considère souvent une chaine de caractère comme un tableau de caractères.

Les objets sont stockées en mémoire, que l'on identifiera à un gigantesque tableau. On considérera que l'on peut stocker sur une case mémoire :

* un entier
* un réel
* un caractère

Les chaines de caractères et les tableaux sont stockées sur des cases mémoires continues, ce qui permet de connaitre l'emplacement de l'élément d'indice $i$ en une opération basique si l'on connait l'emplacement du 1er élément (emplacement du premier élément + i).

### blocs

Lier les instruction en blocs. On va utiliser ici le formalisme de python pour définir un bloc :

```text
type de bloc:
    instruction 1
    instruction 2
    ...
    instruction n
```

On décale les instruction du bloc de sa définition. C'est un truc clair qui permet de voir du premier coup d'œil les instructions d'un bloc.

### tests

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

> On peut dériver toutes les variantes de la forme initiale.

### répétition

On doit pouvoir répéter un bloc tant qu'une condition logique est vérifiée :

```text
tant que (condition logique) est vraie:
    instruction 1
    ...
    instruction n
```

Il existe une variation de ce bloc très utile :

```text
pour chaque élément x d'un tableau:
    instruction 1
    ...
    instruction n
```

On exécutera alors le bloc autant de fois qu'il y a d'élément dans le tableau et à chaque itération du bloc, la variable `x` vaudra un autre élément du tableau. On prendra les éléments du tableau par indice croissant.

> On peut dériver la variante `pour chaque` de la forme initiale `tant que`.

### complexité

La complexité d'un pseudo-code est le nombre d'instructions basiques utilisées pour l'exécuter. La complexité d'un bloc d'instruction est égal à la somme des complexités des instructions qui le compose.

Par exemple le pseudo-code suivant :

```text
x = 30
if ((x > 12) AND (y < 36)):
    z = x * "coucou"
```

1. on affecte un objet à x : 1 instruction
2. un test avec 2 comparaisons et un `AND` : 3 instructions
3. on affecte le résultat d'une opération élémentaire : 2 instructions

Un nombre total d'instruction de 6.

### nom des termes utilisés ?

Leurs noms importent peu, seuls leurs fonctions sont importantes. Vous pouvez donc utiliser les mots qu'il vous plait, du moment qu'ils sont compréhensible pour vous et — surtout — pour votre lecteur. Le plus souvent, on utilisera un mix de python et de français, ou d'anglais.

Les trois pseudo-code suivant sont ainsi équivalent :

```test
for i in range(10):
    affiche à l'écran i
```

```test
pour chaque entier i allant de 0 à 9:
    print(i)
```

```test
for (i=0 ; i < 10 ; i++) {
    print(i)
}
```

## pseudo-code

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

Ceci permet ensuite de définir des fonctions pour écrire des algorithmes de façon plus concise.

### fonctions

Une fonction est un algorithme. Une fois que sa complexité est connue, on peut l'utiliser comme une instruction dans un pseudo-code.

```text
nom(entrée 1, ..., entrée n)
```

Si l'algorithme a un retour, on peut directement l'utiliser, en l'affectant à une variable par exemple :

```text
variable = nom(entrée 1, ..., entrée n)
```

Si on veut utiliser le pseudo code *recherche* défini plus haut, cela pourrait être une instruction du type : `trouve = recherche(tab, 3)`. On affecte la sortie de l'algorithme `recherche` avec comme paramètres `tab` (le tableau d'entier) et `3` (un entier) à la variable `trouve`.

Il est important de voir que lorsque l'on exécute une fonction, les variable qu'elle crée le seront dans un espace à elle, pas dans celui du pseudo-code appelant. Ainsi dans le code suivant :

```text
e = 4
t = [1, 2, 6]
trouve = recherche(t, 6)
affiche à l'écran e
```

On affichera bien 4 à l'écran et pas 6 (le nom de variable `e` défini dans recherche reste dans recherche).

### instructions avancées

Si l'on devait à chaque pseudocode redéfinir tout les algorithmes qu'on utilise ce serait vraiment fastidieux. On utilise souvent des fonctions non basiques (comme l'affichage à l'écran qu'on a déjà vu) ou des structures plus élaborées (les listes par exemples qui sont des extensions des tableaux). Il faudra cependant toujours connaitre les complexités de ce qu'on utilise.

Par exemple pour les listes, qui sont des tableau redimensionnables :

* complexité d'ajout d'un élément à la fin de la liste : coût de 1 instruction
* complexité de l'ajout d'un élément pas à la fin de la liste : coût de la taille de la liste instructions
* complexité de la suppression d'un élément à la fin de la liste : coût de 1 instruction
* complexité de la suppression d'un élément pas à la fin de la liste : coût de la taille de la liste instructions
* usage comme un tableau : 1 instruction

Si vous utilisez des méthodes d'objets comme vous avez l'habitude de le faire en python (comme une `ma_liste.index("?")`, `x in ma_chaine_de_caractères`) ou des structures compliquées (télécharger un fichier d'internet) vous avez le droit mais vous **devez** en connaître le coût : la complexité, les cas d'usage (être connecté), etc.

## comment écrire du pseudo-code

Le pseudo-code est une représentation d'un algorithme donc le but est :

* de démontrer que l'algorithme fait bien ce qu'on pense qu'il fait
* de calculer ses performances :
  * nombre d'opérations utilisées
  * nombre de cases mémoire utilisées

Pour réaliser cela le plus simplement possible, on voudra **toujours** :

* qu'ils soient lisibles,
* qu'ils soient justes,
* en connaître les performances.

### lisible

Le but d'un algorithme papier est d'être compris. On utilisera pour l'écrire une série de règles compréhensibles par tout le monde : le pseudo-code. Ce n'est ni une langue ni un langage.

préférez des noms de variables explicites et n'hésitez pas à séparer votre pseudo-code en fonction pour qu'il soit plus clair

> N'oubliez pas que les fonctions doivent être décrits si elles ne sont pas immédiatement compréhensibles.

### preuve

On **démontrera** le fonctionnement de l'algorithme en utilisant des preuves mathématiques.

### performances

On calculera la complexité de l'algorithme :

* nombre d'opérations
* place en mémoire

Ces complexités dépendent des paramètres de l'algorithme et, parfois de circonstances extérieures comme l'état du réseau par exemple.

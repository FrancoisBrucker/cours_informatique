---
layout: page
title:  "Algorithme Exponentiation rapide"
category: cours
tags: informatique cours 
---

# introduction

On veut écrire un algorithme qui, à partir de deux nombres $a$ et $b$ rend $a^b$.

On va voir 2 algorithmes dont l'un est bien plus rapide que l'autre.

## simple

```python
def puissance(nombre, exposant):
    resultat = 1
    compteur = exposant
    while compteur > 0:
    	resultat *= nombre
    	compteur -= 1
    return resultat
```

### est-ce que ça mache ?

On teste sur de petits nombres en se mettant à la place de l'ordinateur.

* on numérote chaque ligne
* on note sur une feuille les variable
* on exécute ligne à ligne en notant les différents résultats.
* à la fin on vérifie que `résultat` vaut bien ce qu'il doit valoir.

Les cas simples que l'on peut essayer sans peine, et permet de **tester les cas limites** :

* exposant vaut 0 ou 1
* nombre vaut 2 ou 3 (un peu plus que les cas triviaux)

Puis un cas un peu plus compliqué pour **tester si les boucles fonctionnent bien** :

* exposant vaut 2 ou 3
* nombre vaut 2 ou 3


Une fois qu'on est convaincu que ça fonctionne, on peut essayer de prouver la finitude, la complexité et la preuve.

### preuve de finitude

* `compteur` diminue strictement à chaque boucle et la condition d'arrêt est lorsqu'il vaut 0
* condition : il faut que `compteur` soit un nombre >= 0 pour que l'algorithme s'arrête. Donc `exposant` doit être un nombre positif.

**Remarque** : pour des nombres, on préférera toujours des conditions d'arrêt larges (plus petit que, plus grand que, différent de) plutôt que des conditions sur l'égalité stricte. Ceci pour deux raisons majeures :

* L'égalité entre réels n'existe pas en informatique par exemple.
* dans l'exemple ci-dessus mettre des exposants négatifs ou des nombres rées ne fait pas boucler infiniment notre algorithme


### preuve de l'algorihtme

En utilisant l'opération `**` qui signifie exposant en python, on a :

* invariant de boucle : `resultat * nombre ** compteur = nombre ** exposant`
* condition sur les entrées : `nombre` et `exposant` sont des entiers naturels

Juste avant la première itération de la boucle, `resulat = 1` et `compteur = exposant` notre invariant est donc vérifié.

Après une itération de la boucle on a :


* `nombre' = nombre`
* `exposant' = exposant`
* `resulat' = resultat * nombre`
* `compteur' = compteur - 1`


Ceci donne : `resultat' * nombre' ** compteur' = (resultat * nombre) * nombre ** (compteur - 1) = resultat * nombre ** compteur = nombre ** exposant = nombre' ** exposant'`

L'invariant est donc vrai aussi à la fin de l'algorithme, lorsque `compteur = 0`. Et là : `resultat * nombre ** compteur = resultat = nombre ** exposant`


### complexité

* un boucle en $\mathcal{O}(exposant)$
* des lignes en $\mathcal{O}(1)$

Donc : complexité en $\mathcal{O}(exposant)$

## rapide

```python
def puissance(nombre, exposant):
    resultat = 1
    compteur = exposant

    while compteur > 0:
    	if compteur % 2 != 0:
    		resultat *= nombre
    		compteur -= 1
    	else:
    		nombre *= nombre
    		compteur /= 2

    return resultat
```

**Remarques** :

* On utilise l'opérateur *modulo* qui se note `%` en python. Il retourne le reste de la divison entière.
* Ici on vérifie si `compteur` est pair (reste de la division entière par 2 vaut 0) ou impair (reste de la division entière par 2 vaut 1).


### est-ce que ça mache ?


Comme avant avec les cas simples :

* exposant vaut 0 ou 1
* nombre vaut 2 ou 3 (un peu plus que les cas triviaux)

L'algorithme vérifie si `compteur` est pair ou impair, donc pour rentrer dans les boucle on va prendre un exposant un peu plus grand, par exemple `exposant = 7`.
On peut garder nombre petit pour calculer facilement les résultats, comme `nombre = 2`.

### preuve de finitude

De même que pour l'algorithme simple, `compteur` diminue strictement à chaque boucle (ou il diminue de `-1` ou il est divisé par 2). Si `exposant` est un entier naturel en entrée, `compteur` reste entier après chaque boucle (on ne le divise par 2 que s'il est pair) et est strictement plus petit : l'algorihtme va s'arrêter à un moment.

### preuve de l'algorihtme

On a le même invariant de boucle que pour l'algorithme simple. En notant `compteur_initial`, la valeur de compteur en entrée de l'algorithme on a : `resultat * nombre ** compteur = nombre_initial ** exposant`

Pour le prouver, si on a une variable de nom `x` en entrée de boucle, on note sa valeur en sortie de boucle `x'`

de là :

* si compteur est impair on a :
	* `compteur' = compteur -1`
	* `resultat' = resultat * nombre`
	* `nombre' = nombre`
	* `resultat * nombre ** compteur = (resultat * nombre) * nombre ** (compteur - 1) = resultat' * nombre' ** compteur'`
* si compteur est impair on a :
	* `compteur' = compteur - 1`
	* `resultat' = resultat`
	* `nombre' = nombre * nombre`
	* `resultat * nombre ** compteur = resultat * (nombre * nombre) ** (compteur / 2)  = resultat' * nombre' ** compteur'`

L'invariant de boucle est démontré.


### complexité

Pourquoi s'embêter avec la parité de compteur ? Parce que ça permet d'aller vachement plus vite !

On va le démontrer petit à petit.

#### nombre de fois où compteur est impair

Si à l'itération numéro $i$ compteur est impair, il sera pair à l'itération $i + 1$ car `compteur' = compteur = 1` dans ce cas là. De là, **le nombre d'itérations où compteur est impair est au pire égal au nombre de fois où il est pair**

#### nombre de fois où le compteur est pair

A chaque fois où compteur est pair, on le divise par 2. Si $k$ est le nombre de fois où le compteur a été pair, on a que : `2 ** k <= nombre` (avec  `nombre` le paramètre d'entrée).


Comme le `nombre` est un entier, il existe un nombre $p$ tel que : `2 ** p <= nombre < 2 ** (p + 1)`.

On ne peut donc pas diviser par 2 `nombre` ou un nombre plus petit que lui plus de `p` fois : `<= p`.

**Remarque** :

* par définition, le nombre de fois où l'on peut diviser un nombre $x$ par 2 est la partie entière de $\log_2(x) = \mbox{ln}$
* pour tout nombre k, le nombre de fois où l'on peut diviser un nombre $x$ par $k$ est $\log_k(x)$
* comme $\log_k(x) = \mbox{ln}(x) / \mbox{ln}(k)$, les $\mbox{ln}$ et $\log_k$ sont proportionnels entres eux. D'un point de vue algorithmique ça signifie que $\mathcal{O}(\log_k(x)) = \mathcal{O}(\mbox{ln}(x))$ pour tout entier $k$

#### nombre de fois où l'on rentre dans la boucle

C'est au pire deux fois le nombre de fois où compteur est paire et donc au pire de l'ordre $2 * \mbox{ln}(\mbox{compteur})$ pour une valeur de compteur donnée. Comme `compteur` vaut initialement `exposant`, le nombre de fois où l'on rentre dans la boucle est de l'ordre de $\mathcal{O}(\log_2(\mbox{exposant}))$.

Comme les autres lignes sont en $\mathcal{O}(1)$ on a une compexité de l'algorithme en $\mathcal{O}(\log_2(\mbox{exposant}))$.

Comme la fonction $\mbox{ln}$ est proportionnelle à $\log_k$ pour tout $k$, on a aussi que notre algorithme est en : $\mathcal{O}(ln(\mbox{exposant}))$.


Cette complexité est très faible ! Comparez par exemple :

> $2^{16} = 65536$ opérations et $\log_2(65536) = 16$ opérations.


Cette différence va aller exponentiellement lorsque compteur augmente, par exemple entre

> $2^{100} = 1267650600228229401496703205376$ et $100$ opérations

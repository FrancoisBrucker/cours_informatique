---
layout: page
title:  "étude / algorithmes d'exponentiation"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithmie]({% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}) / [étude : l'exponentiation]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-exponentiation.md %})
>
> prérequis :
>
>* [complexité max/min]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-max-min.md %})
>* [preuve d'algorithme]({% link cours/theorie-pratiques-algorithmique/algorithmie/preuve-algorithme.md %})
{: .chemin}

On va étudiez deux algorithmes permettant de calculer $a^b$  à partir de deux entiers $a$ et $b$. On appliquera toujours la même méthode pour analyser un algorithme :

> Lorsque l'on étudie un algorithme, il faut faire trois choses :
>
> 1. vérifier le fonctionnement de l'algorithme sur de petits exemple que l'on peut tester à la main
> 2. preuve de l'algorithme (on commence par vérifier que l'algorithme se termine puis preuve)
> 3. calcul de la complexité de l'algorithme
>
{: .note}

> dans la suite, les algorithmes seront tous donnés en python

## algorithme naïf {#algo-naif}

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight python linenos %}

def puissance(nombre, exposant):
    résultat = 1
    compteur = exposant
    while compteur > 0:
        résultat *= nombre
        compteur -= 1
    return résultat

{% endhighlight %}

### est-ce que ça marche ? {#marche-naïf}

On test l'algorithme sur de petits exemples qui vont nous permettre d'appréhender son fonctionnement :

> On teste sur de petits nombres en se mettant à la place de l'ordinateur.
>
> * on numérote chaque ligne
> * on note sur une feuille les variables
> * on exécute ligne à ligne en notant les différents résultats.
> * à la fin on vérifie que `résultat` vaut bien ce qu'il doit valoir.
>
{: .note}

Les cas simples que l'on peut essayer sans peine, et permet de **tester les cas limites** :

* exposant vaut 0 ou 1
* nombre vaut 2 ou 3 (un peu plus que les cas triviaux)

Puis un cas un peu plus compliqué pour **tester si les boucles fonctionnent bien** :

* exposant vaut 2 ou 3
* nombre vaut 2 ou 3

> Vérifiez que l'algorithme donne bien les bons résultats sur les exemples ci-dessus.
{: .a-faire}

Une fois qu'on est convaincu que ça fonctionne, on peut essayer de prouver la finitude, la complexité et la preuve.

### preuve de finitude {#finitude-naif}

* `compteur` diminue strictement à chaque boucle et la condition d'arrêt est lorsqu'il vaut 0
* condition : il faut que `compteur` soit un nombre >= 0 pour que l'algorithme s'arrête. Donc `exposant` doit être un nombre positif.

> Pour des nombres, on préférera toujours des conditions d'arrêt larges (plus petit que, plus grand que, différent de) plutôt que des conditions sur l'égalité stricte. Ceci pour deux raisons majeures :
>
> * L'égalité entre réels n'existe pas en informatique par exemple.
> * dans l'exemple ci-dessus mettre des exposants négatifs ou des nombres rées ne fait pas boucler infiniment notre algorithme
>
{: .note}

### preuve de l'algorithme

Le fonctionnement de l'algorithme est *à peut prêt* clair si les entrées sont des entiers : il multiplie $a$ par lui-même $b$ fois grâce à une boucle. Une preuve par récurrence doit donc fonctionner, mais essayons de faire une *jolie* preuve en exhibant un invariant de boucle.

En utilisant l'opération `**` qui signifie exposant en python, on a :

* invariant de boucle : `resultat * nombre ** compteur = nombre ** exposant`
* condition sur les entrées : `nombre` et `exposant` sont des entiers naturels

#### conditions initiales {#invariant-naif-init}

Juste avant la première itération de la boucle, `resulat = 1` et `compteur = exposant` notre invariant est donc vérifié.

#### preuve de l'invariant {#invariant-naif-preuve}

On suppose l'invariant vrai au début de la boucle $i$. Comme expliqué dans la partie sur les [preuves d'algorithmes]({% link cours/theorie-pratiques-algorithmique/algorithmie/preuve-algorithme.md %}), on met un `'` aux variable après l'itération :

* `nombre' = nombre`
* `exposant' = exposant`
* `resulat' = resultat * nombre`
* `compteur' = compteur - 1`

On a alors :  `resultat' * nombre' ** compteur' = (resultat * nombre) * nombre ** (compteur - 1) = resultat * nombre ** compteur = nombre ** exposant = nombre' ** exposant'`

On a démontré notre invariant de boucle.

#### preuve de l'algorithme {#preuve-naif}

Notre invariant est vrai avant et après chaque itération, il est donc également vrai à la fin de l'algorithme, lorsque `compteur = 0`. Et là : `resultat * nombre ** compteur = resultat = nombre ** exposant`

### complexité {#complexite-naif}

* un boucle en $\mathcal{O}(\mbox{exposant})$
* des lignes en $\mathcal{O}(1)$

Donc : complexité en $\mathcal{O}(\mbox{exposant})$

## exponentiation indienne {#algo-rapide}

Aussi appelé [exponentiation rapide](https://fr.wikipedia.org/wiki/Exponentiation_rapide), l'algorithme suivant permet de calculer `nombre ** exposant`.

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

> L'opérateur `%` signifie *modulo* en python : il retourne le reste de la divison entière. L'algorithme s'en sert pour vérifier si `compteur` est pair (reste de la division entière par 2 vaut 0) ou impair (reste de la division entière par 2 vaut 1)

### est-ce que ça marche ? {#marche-rapide}

Comme pour l'algorithme naïf, on vérifie que tout fonctionne avec les cas simples :

* exposant vaut 0 ou 1
* nombre vaut 2 ou 3 (un peu plus que les cas triviaux)

Enfin, comme l'algorithme vérifie si `compteur` est pair ou impair, on peut essaier un exposant un peu plus grand, par exemple :

* `exposant = 7`
* `nombre = 2` (pas trop grand pour pouvoir calculer facilement les résultats de tête)

> Vérifiez que l'algorithme donne bien les bons résultats sur les exemples ci-dessus.
{: .a-faire}

### preuve de finitude {#finitude-rapide}

De même que pour l'algorithme simple, `compteur` diminue strictement à chaque boucle (ou il diminue de `-1` ou il est divisé par 2). Si `exposant` est un entier naturel en entrée, `compteur` reste entier après chaque boucle (on ne le divise par 2 que s'il est pair) et est strictement plus petit : l'algorihtme va s'arrêter à un moment.

### preuve de l'algorihtme {#preuve-rapide}

On va montrer que l'invariant de l'algorithme naïf fonctionne aussi. En notant `compteur_initial`, la valeur de compteur en entrée de l'algorithme, on a l'invariant suivant : `resultat * nombre ** compteur = nombre_initial ** exposant`

#### conditions initiales {#invariant-rapide-init}

Juste avant la première itération de la boucle, `resulat = 1` et `compteur = exposant` notre invariant est donc vérifié.

#### preuve de l'invariant {#invariant-rapide-preuve}

On suppose l'invariant vrai au début de la boucle d'itération $i$. Regardons comment les variables ont été modifiées lors de cette itération :

* si compteur est impair on a :
  * `compteur' = compteur -1`
  * `resultat' = resultat * nombre`
  * `nombre' = nombre`
  * l'invariant vaut alors en fin d'itération : `resultat * nombre ** compteur = (resultat * nombre) * nombre ** (compteur - 1) = resultat' * nombre' ** compteur'`
* si compteur est impair on a :
  * `compteur' = compteur - 1`
  * `resultat' = resultat`
  * `nombre' = nombre * nombre`
  * l'invariant vaut alors en fin d'itération : `resultat * nombre ** compteur = resultat * (nombre * nombre) ** (compteur / 2)  = resultat' * nombre' ** compteur'`

Dans tous les cas, l'invariant est toujours vérifié puisqu'en début de boucle notre invariant vaut `resultat * nombre ** compteur = nombre_initial ** exposant`.

#### preuve de l'algorithme {#preuve-rapide}

Notre invariant est vrai avant et après chaque itération, il est donc également vrai à la fin de l'algorithme, lorsque `compteur = 0`. Et là : `resultat * nombre ** compteur = resultat = nombre_initial ** exposant`

### complexité {#complexite-rapide}

Pourquoi s'embêter avec la parité de compteur ? Parce que ça permet d'aller vachement plus vite !

On va le démontrer petit à petit.

#### nombre de fois où compteur est impair

Si à l'itération numéro $i$ compteur est impair, il sera pair à l'itération $i + 1$ car `compteur' = compteur - 1` dans ce cas là.

On a donc que : **le nombre d'itérations où compteur est impair est au pire égal au nombre de fois où il est pair**

#### nombre de fois où le compteur est pair

A chaque fois où compteur est pair, on le divise par 2. Si $k$ est le nombre de fois où le compteur a été pair, on a que : $2^k \leq \mbox{nombre}$ (avec  `nombre` le paramètre d'entrée).

Comme `nombre` est un entier, il existe un nombre $p$ tel que $2^p \leq \mbox{nombre} < 2^{p + 1}$.

On ne peut donc pas diviser par 2 `nombre`, ou un nombre plus petit que lui, plus de `p` fois. Et $p$ vaut la partie entière de $\log_2(\mbox{nombre})$. En effet :

$$
\begin{array}{lcccl}
    2^p &\leq &\mbox{nombre} &<& 2^{p + 1}\\
    \log_2(2^p) &\leq &\log_2(\mbox{nombre}) &< &\log_2(2^{p + 1}) \mbox{ (car la fonction est croissante)} \\
    p &\leq &\log_2(\mbox{nombre}) &<& p + 1
\end{array}
$$

> Pour tout nombre k, le nombre de fois où l'on peut diviser un nombre $x$ par $k$ est $\log_k(x)$

On a donc que : **le nombre d'itérations où compteur est pair est au pire égal à $\log_2(\mbox{nombre})$**

#### nombre de fois où l'on rentre dans la boucle

Le nombre de fois où l'on rentre dans la boucle est égal au nombre de fois où le compteur est pair plus le nombre de fois où le compteur est impair, c'est donc au pire égal à deux fois le nombre de fois où compteur est pair, c'est à dire $2 * \log_2(\mbox{compteur})$ pour la valeur initiale de compteur.

Comme `compteur` vaut initialement `exposant`, le nombre de fois où l'on rentre dans la boucle est de l'ordre de $\mathcal{O}(\log_2(\mbox{exposant}))$ donc en $\mathcal{O}(\ln(\mbox{exposant}))$.

Comme les autres lignes sont en $\mathcal{O}(1)$ on a une complexité de l'algorithme en $\mathcal{O}(\ln(\mbox{exposant}))$.

Cette complexité est très faible ! Comparez par exemple : $2^{16} = 65536$ opérations et $\log_2(65536) = 16$ opérations.

Cette différence va aller exponentiellement lorsque compteur augmente, par exemple entre $2^{100} = 1267650600228229401496703205376$ et $100$ opérations

## conclusions

* la procédure utilisée pour l'étude de ces deux algorithmes est générale, vous pouvez (et devez) l'appliquer à l'étude de tout nouvel algorithme.
* il ne faut jamais penser que l'in ne peut pas faire mieux pour un algorithme. Si vous ne connaissiez pas l'exponentiation indienne, il vous aurez été difficile de penser que l'on peut fair mieux que l'algorithme naïf pour calculer une exponentielle
* un algorithmicien ferait beaucoup de sacrifices pour obtenir une complexité en $\mathcal{O}(\ln(n))$ tellement c'est efficace.

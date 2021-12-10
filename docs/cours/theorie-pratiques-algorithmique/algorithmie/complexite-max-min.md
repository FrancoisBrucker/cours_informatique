---
layout: page
title:  "Complexité max/min"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithmie]({% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}) / [complexité max/min]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-max-min.md %})
>
> prérequis :
>
>* [algorithmie/pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %})
{: .chemin}

Où l'on se donne des outils pour mesurer (théoriquement et en pratique) les performances d'un algorithmes

## mesures en $\mathcal{O}$

Mesurer les performances d'un algorithme se fera presque exclusivement en utilisant des $\mathcal{O}$ (*grand O*)

>Une fonction $f(N)$ est en $\mathcal{O}(f'(N))$ s'il existe 2 constantes $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot f'(N)$ pour tout $N > N_0$.
{: .note}

Cela permet :

* d'avoir un majorant de notre mesure lorsque $N$ devient grand
* de ne pas s'occuper des constantes puisque (on va le démontrer) une fonction en $\mathcal{O}(\mbox{constante})$ est également en $\mathcal{O}(1)$
* de ne pas s'occuper de la proportionnalité car (on va le démontrer) une fonction en $\mathcal{O}(\mbox{constante} \cdot f(N))$ est également en $\mathcal{O}(f(N))$

> Connaitre le comportement en $\mathcal{O}$ d'une mesure dépendant de $N$ nous donne un majorant de son comportement lorsque $N$ devient grand. Si le majorant n'est pas trop éloigné de la mesure originale, cela nous donne une **idée générale** de la valeur de la mesure lorsque $N$ devient grand.
{: .note}

Ceci est plutôt intéressant en algorithmie car l'on ne connait pas toujours exactement le nombre d'opérations élémentaires utilisées, mais on peut les majorer de façon assez précise. On utilisera ainsi les $\mathcal{O}$ pour mesurer :

* le nombre d'opérations élémentaires effectuée par l'algorithme avant de s'arrêter
* le temps mis par l'algorithme pour s'exécuter
* la taille de la mémoire utilisée pour par l'algorithme

Par rapport à la taille $N$ de l'entrée de l'algorithme.

### arithmétique des $\mathcal{O}$

Par abus de langage, on notera :

* $\mathcal{O}(f(N))$ plutôt que soit $f'(N)$ une fonction en $\mathcal{O}(f(N))$
* $f(N) = \mathcal{O}(g(N))$ plutôt que : "la fonction $f(N)$ est en $\mathcal{O}(g(N))$"
* $\mathcal{O}(f(N)) \Rightarrow \mathcal{O}(g(N))$ plutôt que "une fonction en $\mathcal{O}(f(N))$ est également en $\mathcal{O}(g(N))$"
* $\mathcal{O}(f(N)) \Leftrightarrow \mathcal{O}(g(N))$ plutôt que "une fonction en $\mathcal{O}(f(N))$ est également en $\mathcal{O}(g(N))$ et réciproquement"

> On a les règles suivantes :
>
> 1. $\mathcal{O}(A) \Leftrightarrow \mathcal{O}(1)$, avec $A$ une contante strictement positive
> 2. $\mathcal{O}(N^p) \Rightarrow \mathcal{O}(N^q)$ pour $q \geq p$
> 3. $f(N) = \mathcal{O}(g(N))$ implique $\mathcal{O}(f(N) + g(N) + h(N)) \Rightarrow \mathcal{O}(g(N) + h(N))$
> 4. $f(N) = \mathcal{O}(g(N))$ implique $\mathcal{O}(f(N) \cdot g(N) \cdot h(N) + h'(N)) \Rightarrow \mathcal{O}((g(N))^2 \cdot h(N)+ h'(N))$
>
> Et en combinant les $\mathcal{O}$ pour $f$ et $g$ deux fonction positives :
>
> * $\mathcal{O}(f(N)) + \mathcal{O}(g(N)) \Rightarrow \mathcal{O}(f(N) + g(N))$
> * $\mathcal{O}(f(N)) \cdot \mathcal{O}(g(N)) \Rightarrow \mathcal{O}(f(N) \cdot g(N))$
>
{: .note}

> Démontrez ces propriétés.
{: .a-faire}

{% details  Démonstration de $\mathcal{O}(A) \Leftrightarrow \mathcal{O}(1)$, avec $A$ une contante strictement positive %}

Soit $f(N) = \mathcal{O}(A)$. Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) < c_0 \cdot A$. En posant $c'_0 = c_0 \cdot A$, on a $f(N) < c'_0 \cdot 1$ pour tout $N > N_0$ donc $f(N) = \mathcal{O}(1)$.

Réciproquement, soit $f(N) = \mathcal{O}(1)$. Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) < c_0 \cdot 1$. En posant $c'_0 = c_0 / A$, on a $f(N) < c'_0 \cdot A$ pour tout $N > N_0$ donc $f(N) = \mathcal{O}(A)$.

{% enddetails %}

{% details  Démonstration de $\mathcal{O}(N^p) \Rightarrow \mathcal{O}(N^q)$ pour $q \geq p$ %}

Soit $f(N) = \mathcal{O}(N^p)$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot N^p$ pour $N > N_0$.
Comme $1 < 2 \cdot N^\alpha$ pour $\alpha \geq 0$ et $N> 1$, on a $N^p < c_0 \cdot N^q$ pour $c_0 = 2$, $N > 1 = N_0$  et $p \leq q$ : $N^p = \mathcal{O}(N^q)$ pour tout $p \leq q$

{% enddetails %}

{% details  Démonstration de $f(N) = \mathcal{O}(g(N))$ implique $\mathcal{O}(f(N) + g(N) + h(N)) \Rightarrow \mathcal{O}(g(N) + h(N))$ %}

Soit $f(N) = \mathcal{O}(g(N))$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot N^p$ pour $N > N_0$. Si $f'(N) = \mathcal{O}(f(N) + g(N) + h(N))$ il existe $c'_0$ et $N'_0$ tels que $f'(N) < c'_0(f(N) + g(N) + h(N))$ pour $N > N_0$.

De là, $f'(N) < c'_0 c_0 g(N) + c'_0 g(N) + c'_0 h(N)$ pour $N > \max \\{ N_0, N'_0 \\}$ ce qui implique $f'(N) < \max \\{ c'_0, c_0 \\}^2 (g(N) + h(N))$ pour $N > \max \\{ N_0, N'_0 \\}$ : $f'(N) = \mathcal{O}(g(N) + h(N))$

{% enddetails %}

{% details  Démonstration de $f(N) = \mathcal{O}(g(N))$ implique $\mathcal{O}(f(N) \cdot g(N) \cdot h(N) + h'(N)) \Rightarrow \mathcal{O}((g(N))^2 \cdot h(N)+ h'(N))$ %}

Soit $f(N) = \mathcal{O}(g(N))$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot N^p$ pour $N > N_0$. Si $f'(N) = \mathcal{O}(f(N)\cdot g(N) \cdot h(N) + h'(N))$ il existe $c'_0$ et $N'_0$ tels que $f'(N) < c'_0(f(N) \cdot g(N) \cdot h(N) + h'(N))$ pour $N > N_0$.

De là, $f'(N) < c'_0 (c_0 g(N) \cdot g(N) \cdot h(N) + h'(N)$ pour $N > \max \\{ N_0, N'_0 \\}$ ce qui implique $f'(N) < \max \\{ c'_0, c_0 \\}^2 (g(N)^2 \cdot  h(N) + h'(N))$ pour $N > \max \\{ N_0, N'_0 \\}$ : $f'(N) = \mathcal{O}((g(N))^2 \cdot h(N) + h'(N))$

{% enddetails %}

{% details  Démonstration de  $\mathcal{O}(f(N)) + \mathcal{O}(g(N)) \Rightarrow \mathcal{O}(f(N) + g(N))$ %}

Soient $f'(N) = \mathcal{O}(f(N))$ et $g' = \mathcal{O}(g(N))$, il existe donc $c_0$, $c'_0$, $N_0$ et $N'_0$ tels que $f'(N) < c_0 f(N)$ pour $N > N_0$ et $g'(N) < c'_0 g(N)$ pour $N > N'_0$.

On a alors $f'(N) + g'(N) < \max \\{c_0, c'_0\\} (f(N) + g(N))$ pour $N > \max \\{ N_0, N'_0\\}$ : $f'(N) + g'(N) = \mathcal{O}(f(N) + g(N))$.

{% enddetails %}

{% details  $\mathcal{O}(f(N)) \cdot \mathcal{O}(g(N)) \Rightarrow \mathcal{O}(f(N) \cdot g(N))$ %}

Soient $f'(N) = \mathcal{O}(f(N))$ et $g' = \mathcal{O}(g(N))$, il existe donc $c_0$, $c'_0$, $N_0$ et $N'_0$ tels que $f'(N) < c_0 f(N)$ pour $N > N_0$ et $g'(N) < c'_0 g(N)$ pour $N > N'_0$.

On a alors $f'(N) \cdot g'(N) < \max \\{c_0, c'_0, 1 \\}^2 (f(N) \cdot g(N))$ pour $N > \max \\{ N_0, N'_0\\}$ car $f$ et $g$ sont positives : $f'(N) \cdot g'(N) = \mathcal{O}(f(N) \cdot g(N))$.

{% enddetails %}

### conséquences algorithmique

La règle (1) montre qu'un nombre constant est toujours en $\mathcal{O}(1)$. Pour un algorithme, il est souvent compliqué de savoir exactement de combien d'[opérations basique] basique]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#instruction-basique) est constitué une opération, ou le temps exact qu'elle va prendre (pour un ordinateur, cela dépend du type de processeur par exemple. L'addition avec un x68 est faites [avec des registres](https://ensiwiki.ensimag.fr/index.php?title=Constructions_de_base_en_assembleur_x86) par exemple, et donc l'addition nécessite 2 opération du processeur). Mais on pourra toujours montrer qu'il y en a un nombre constant (ou borné par un nombre constant) :

> La complexité d'une opération basique nécessite $\mathcal{O}(1)$ opérations.
{: .note}

De là :

> un nombre constant d'opérations basiques nécessite $\mathcal{O}(1)$ opérations.
{: .note}

Les règles précédentes permettent plus généralement de montrer :

> $\mathcal{O}(A \cdot f(N)) \Leftrightarrow A \cdot \mathcal{O}(f(N)) \Leftrightarrow \mathcal{O}(f(N))$, avec $A$ une contante strictement positive et $f(N)$ une fonction strictement positive pour $N > N_0$
{: .note}

Ceci est pratique. En reprenant l'exemple de la partie [complexité des pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#complexité), car cela permet de ne pas compter toutes les opérations basiques précisément :

```text
x = 30
if ((x > 12) AND (y < 36)):
    z = x * "coucou"
```

1. on affecte un objet à x : 1 instruction, donc $\mathcal{O}(1)$ opérations.
2. un test avec 2 comparaisons et un `AND` : 3 instructions, donc $\mathcal{O}(3) = \mathcal{O}(1)$ opérations.
3. on affecte le résultat d'une opération élémentaire : 2 instructions, donc $\mathcal{O}(2) = \mathcal{O}(1)$ opérations.

Un nombre total d'instructions de $3 \mathcal{O}(1) = \mathcal{O}(1)$ opérations.

En revanche, faites attention, cela ne marque que pour les constantes !

> Si le nombre d'opérations élémentaires est variable on a : $n \mathcal{O}(1) = \mathcal{O}(n)$ !
{: .attention}

Enfin, comme en algorithmie on manipulera souvent des polynômes, on peut montrer facielement avec les règles précédentes que :

> \sum_{i=0}^na_i x^i = \mathcal{O}(x^n)
{: .note}

## complexité d'un algorithme

On l'a vu dans la partie [pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}#complexité), la complexité est le nombre d'opérations basiques effectuées par un algorithme. Le nombre d'opérations basiques effectué par un pseudo-code va être dépendant des entrées de celui-ci, même si les entrées ont la même taille (on verra des exemples de ça).

On distinguera trois types de complexités :

* nombre d'opérations basiques effectuées
* temps d'exécution d'un programme
* taille mémoire consommée pendant l'exécution

Les complexités vont toutes dépendre des entrées, plus précisément d'un paramètre rendant compte de leur **taille**, c'est à dire du nombre de cases mémoires nécessaires pour les stocker.

### nombre d'opérations basiques

> La **complexité** (aussi parfois appelée **complexité maximale**) d'un algorithme est le **nombre maximum d'opérations basiques** effectué par celui-ci pour des entrées **de taille totale donnée*. Elle sera donnée en $\mathcal{O}(f(N))$, où $N$ est une variable rendant compte de la taille des données.
{: .note}

La **taille** d'une entrée étant proportionnelle au nombre de cases mémoires que celle-ci nécessite.

Il arrive que certains algorithmes aient un comportement très différent selon les entrées. Parler seulement de la complexité (nombre maximum d'opérations) ne permet pas alors de le caractériser complètement. On pourra alors aussi parler de :

> La **complexité minimale** d'un algorithme est le **nombre minium d'opérations basiques** effectué par celui-ci pour des entrées **de taille totale donnée*. Elle sera donnée en $\mathcal{O}(f(N))$, où $N$ est une variable rendant compte de la taille des données.
{: .note}

Lorsque l'on calcule une complexité (maximale ou minimale) sous la forme d'un $\mathcal{O}(f(N))$, on tentera bien sur de trouver la fonction $f(N)$ la plus petite possible.

### temps d'exécution

Un moyen efficace de mesurer la complexité d'un algorithme écrit sous la forme d'un code exécutable est de mesurer le temps mis pour son exécution pour un jeu d'entrée donné.

> la **complexité en temps** d'un algorithme est le temps mis pour l'exécuter en utilisant un jeu de donné de taille donnée pour lequel la complexité est atteinte.
{: .note}

Le temps pris sera bien sur différent si l'on prend une machine plus puissante ou si l'on change le code de l'algorithme mais **complexité en temps sera proportionnelle à la complexité**. Pour le voir, il suffit de mesurer la durée d'exécution de chaque instruction basique et de la borner par le max.

> Si vous ne prenez pas un jeu de donné pour lequel la com^plexité de l'algorithme est atteinte, vous ne mesurez **pas** la complexité temporelle de l'algorithme...
{: .attention}

### taille mémoire

> la **complexité en espace** d'un algorithme est le nombre maximum de cases mémoires utilisées pour l'exécuter en utilisant un jeu de donné de taille donnée.
{: .note}

Comme la complexité, on la mesurera avec des $\mathcal{O}$.

Notez que la complexité en espace n'est pas forcément atteinte pour un jeu de donné donnant la complexité de l'algorithme, mais **complexité en espace sera toujours plus faible que la complexité** (puisque visiter une case mémoire nécessite une opération élémentaire).

### complexité de fonctions ou méthodes

> Toutes les autres opérations doivent être examinée, en particulier les méthodes d'objets qui peuvent prendre plus de temps.
{: .attention}

> Avec python si je dix t.max() pas en O(1)
{: .tbd}

### exemple 1 : quelle est la complexité de l'algorithme suivant


```python
total=0
de i=1 à n-1 faire :
    de j=1  à n faire :
		total=total+1
Rendre total
```

Cheminement de l'algorithme :

* ligne 1 : une affectation, donc en temps constant, donc $\mathcal{O}(1)$
* ligne 2 : une affectation (`i=1`) donc en $\mathcal{O}(1)$
* ligne 3:  une affectation (`j=1`) donc en $\mathcal{O}(1)$
* ligne 4 : une opération et une affectation, donc $\mathcal{O}(1) + \mathcal{O}(1)$
* ligne 3:  une affectation (`j=2`) donc en $\mathcal{O}(1)$
* ligne 4 : une opération et une affectation, donc $\mathcal{O}(1) + \mathcal{O}(1)$
* ...
* ligne 3:  une affectation (`j=n`) donc en $\mathcal{O}(1)$
* ligne 4 : une opération et une affectation, donc $\mathcal{O}(1) + \mathcal{O}(1)$
* ligne 2 : une affectation (`i=2`) donc en $\mathcal{O}(1)$
* ligne 3:  une affectation (`j=1`) donc en $\mathcal{O}(1)$
* ligne 4 : une opération et une affectation, donc $\mathcal{O}(1) + \mathcal{O}(1)$
* ... 
* ligne 3:  une affectation (`j=n`) donc en $\mathcal{O}(1)$
* ligne 4 : une opération et une affectation, donc $\mathcal{O}(1) + \mathcal{O}(1)$
* ...
* ligne 2 : une affectation (`i=n-1`) donc en $\mathcal{O}(1)$
* ligne 3:  une affectation (`j=1`) donc en $\mathcal{O}(1)$
* ligne 4 : une opération et une affectation, donc $\mathcal{O}(1) + \mathcal{O}(1)$
* ... 
* ligne 3:  une affectation (`j=n`) donc en $\mathcal{O}(1)$
* ligne 4 : une opération et une affectation, donc $\mathcal{O}(1) + \mathcal{O}(1)$
* linge 4 : une affectation $\mathcal{O}(1)$

On peut rassembler les boucles entres-elles :
Donc l'algorithme :

* ligne 1 : une affectation, donc en temps constant, donc $\mathcal{O}(1)$
* ligne 2 : une affectation (de la variable i) donc en $\mathcal{O}(1)$ et un début de bloc qui sera effectué $n-1$ fois, donc de l'ordre de $\mathcal{O}(n)$ fois.
* ligne 3:  une affectation (de la variable j) donc en $\mathcal{O}(1)$ et un début de bloc qui sera effectué $n-1$ fois, donc de l'ordre de $\mathcal{O}(n)$ fois.
* ligne 4 : une affectation, donc en temps constant, donc $\mathcal{O}(1)$
* ligne 5 : une affectation, donc en temps constant, donc $\mathcal{O}(1)$

on a donc une complexité de : 

$$\mathcal{O}(1) + \mathcal{O}(n) * (\mathcal{O}(1) + \mathcal{O}(n) * (\mathcal{O}(1) + \mathcal{O}(1))) + \mathcal{O}(1)$$

ceci vaut : 

$$\mathcal{O}(2) + \mathcal{O}(n) * (\mathcal{O}(1) + \mathcal{O}(n) * \mathcal{O}(2))$$

Comme $\mathcal{O}(2) = \mathcal{O}(1)$ on a : 
$$\mathcal{O}(1) + \mathcal{O}(n) * (\mathcal{O}(1) + \mathcal{O}(n) * \mathcal{O}(1))$$

donc comme $\mathcal{O}(n) * \mathcal{O}(1) = \mathcal{O}(1 * n) = \mathcal{O}(n)$ : 

$$\mathcal{O}(1) + \mathcal{O}(n) * (\mathcal{O}(1) + \mathcal{O}(n))$$

Donc : 
$$\mathcal{O}(1) + \mathcal{O}(n) + \mathcal{O}(n^2)$$

Comme $$\mathcal{O}(n^2 + n + 1) = \mathcal{O}(n^2)$$

La complexité finale de l'algorithme est en : $\mathcal{O}(n^2)$

**Règle de calcul simple :** 

* on multiplie le nombre de fois où on execute un bloc par la complexité du bloc.
* on peut die qu'une suite d'instruction en $\mathcal{O}(1)$ est également en $\mathcal{O}(1)$


### exemple 3 : quelle est la complexité de l'algorithme suivant

Attention à la deuxième boucle. Est-ce important pour le résultat ?

```
total=0
de i=1 à n-1 faire :
    de j=i+1 à n faire :
        total=total+1
Rendre total
```
On va utiliser une autre règle que l'on va montrer par la pratique : 

> Si une boucle s'exécute un nombre variable de fois, mais que cette variation est croissante (respectivement décroissante), on peut considérer pour le calcul de la complexité qu'elle s'exécute à chaque fois  de l'ordre du maximum de fois.

Ici, la boucle de la ligne 3 s'exécute un nombre variable de fois qui dépend de la valeur de $i$. Comme $i$ va croitre, le nombre de fois où cette boucle va s'exécuter va décroitre. Donc on peut dire qu'elle va s'exécuter de l'ordre de $\mathcal{O}(n)$ fois, exactement comme pour l'exemple 1. 

On peut donc estimer la complexité de l'algorithme à $\mathcal{O}(n^2)$ fois.

On peut faire un calcul exact de la complexité pour vérifier.

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

$$\mathcal{O}(1) + (\mathcal{O}(1) + (n-1) * (\mathcal{O}(1) + \mathcal{O}(1))) + 
(\mathcal{O}(1) + (n-2) * (\mathcal{O}(1) + \mathcal{O}(1))) + \dots
 + (\mathcal{O}(1) + (1) * (\mathcal{O}(1) + \mathcal{O}(1))) + \mathcal{O}(1)$$

comme $\mathcal{O}(1) + \mathcal{O}(1) = \mathcal{O}(1)$, on a : 

$$\mathcal{O}(1) + (\mathcal{O}(1) + (n-1) * (\mathcal{O}(1))) + 
(\mathcal{O}(1) + (n-2) * (\mathcal{O}(1))) + \dots
 + (\mathcal{O}(1) + (1) * (\mathcal{O}(1))) + \mathcal{O}(1)$$

$$\mathcal{O}(1) + ((n) * (\mathcal{O}(1))) + 
((n-1) * (\mathcal{O}(1))) + \dots
 + ((2) * (\mathcal{O}(1))) + \mathcal{O}(1)$$

et donc notre complexité vaut : 
$$\mathcal{O}(1) + \sum_{1\leq i \leq n} i * \mathcal{O}(1)$$

comme la somme des n premiers entiers vaut $(n+1)(n)/2$ notre complexité devient : 
$$\mathcal{O}(1) + (n+1)(n)/2 * \mathcal{O}(1)$$

Ce qui est de l'ordre de : 

$$\mathcal{O}((n+1)(n)/2) = \mathcal{O}((1/2) * (n^2 +n)) = \mathcal{O}((n^2 +n)) = \mathcal{O}(n^2)$$

On retrouve bien le résultat attendu.


### exemple 3 : plus grand élément d'un tableau de longueur $n$.

```python
def maximum(t, n):
    si n == 0
        return t[0]
    sinon:
        return max(t[n], maximum(t, n-1))
```

On vérifie bien que : 

1. l'algorithme converge bien
2. il rend bien le maximum d'un tableau

La complexité est définie par l'équation de récurrence $C(n) = \mathcal{O}(1) + C(n-1)$ et $C(0) =  \mathcal{O}(1)$

En bornant le temps constant par $K$, on a l'équation de récurrence suivante : $C(N) = K + C(N-1)$

$C(N) = K + K + C(N-2) = \dots = n * K + C(0) = (n+1) * K = \mathcal{O}(n)$

# comparaisons des complexités

Un mauvais choix d’algorithme peut entraîner une différence très importante (facteur 100, 1000, etc.) alors que l’optimisation du code ne fait gagner a priori qu’un facteur 10 au mieux. 

Il existe souvent plusieurs algorithme pour résoudre un problème. De temps en temps un algorithme est meilleurs que tous les autres, mais souvent cela dépend du type de données en entrée (on le verra). Il est donc important non seulement de connaître les complexités des algorithmes pour choisir le meilleurs mais également de connaitre son cas d'utilisation.


## Temps pour résoudre un problème de taille $n$

Exemple d'évolution du temps de calcul par rapport à la complexité. En supposant, que l'on ait un ordinateur qui résout des problèmes de complexité $n$ en 0.01 ms pour des données de taille 10, on peut remplir le tableau ci-après.

En colonnes le nombre $n$ de données, en lignes les complexités des algorithmes. 


 complexité  |     10     |   20    |    30   |      40     |     50     |       60
-------------|------------|---------|---------|-------------|------------|----------------          
    $n$      |    0.01 ms | 0.02 ms | 0.03 ms |  0.04 ms    | 0.05 ms    | 0.06 ms
    $n^2$    |    0.1 ms  | 0.4 ms  | 0.9 ms  |  1.6 ms     | 2.5 ms     | 3.6 ms
    $n^3$    |    1 ms    | 8 ms    | 27 ms   |  64 ms      | 125 ms     | 216 ms
    $n^5$    |    1s      | 3.2 s   | 24.3 s  |  1.7 min    | 5.2 min    | 13 min
    $2^n$    |    1 ms    | 1s      | 17.9 min|  12.7 jours | 35.7 ans   | 36600 ans
    $3^n$    |    59 ms   | 58 min  | 6.5 ans |  385500 ans | 2x1010 ans | 13x1016 siècles



L'évolution est dramatique plus la complexité augmente. Pour une complexité polynomiale, la croissance est encore maitrisée même s'il vaut mieux avoir une petite complexité pour traiter plus de données. Pour une complexité exponentielle ($2^n$ et $3^n$) la durée est tout simplement rédhibitoire.

## Nombre de problèmes résolu par heure

En colonne la rapidité de la machine, en ligne le nombre de problème d'une complexité donné réalisé en 1 heure.

 complexité | machine actuelle | 100x plus rapide | 1000x plus rapide
------------|------------------|------------------|--------------------      
    $n$     |         N1       |      100xN1      |      1000xN1
    $n^2$   |         N2       |      10xN2       |      31.6xN2     
    $n^3$   |         N3       |      4.64xN3     |      10xN3       
    $n^5$   |         N4       |      2.5xN4      |      3.98xN4     
    $2^n$   |         N5       |      N5+6.64     |      N5+9.97
    $3^n$   |         N6       |      N6+4.19     |      N6+6.29


La encore, l'évolution est dramatique plus la complexité augmente. Pour des complexité polynomiales le nombre de problème augmente d'un facteur multiplicatif lorsque la vitesse augment, mais ce n'est pas le cas pour des complexités exponentielles. Pour ces problèmes, augmenter la vitesse de la machine ne change pas fondamentalement le nombre de problèmes que l'on peut résoudre. 


## trouver un élément dans un tableau/chaîne de caractère.

On cherche toujours le cas le pire. Dans des algorithmes dont le nombre d'opérations dépend de l'entrée on choisira des entrées maximisant le nombre d'opérations.

```python
def est_dans_tableau(valeur, tableau):
    for x in tableau:
        if x == valeur:
            return True
	return False
```

Dans l'algorithme ci-dessous la complexité est maximale pour deux cas :

* l'élément recherché n'est pas dans le tableau
* l'élément recherché est le dernier élément du tableau

Car c'est là que l'on parcourt toute la boucle.

complexité : on parcourt tout le tableau et l'interieur de la boucle est en $\mathcal{O}(1)$. La complexité au pire est donc de $\mathcal{O}(len(\mbox{tableau}))$

On verra dans le cours sur les tris, qu'il existe encore d'autres notions de complexités : la *complexité minimale* et la *complexité en moyenne*.

## structures

>**TBD** Exemple du tableau en regardant comment fonctionne la mémoire. Et les complexité de maintien de la structure.

objet = place dans la mémoire


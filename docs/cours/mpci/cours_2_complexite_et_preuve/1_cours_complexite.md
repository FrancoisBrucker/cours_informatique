---
layout: page
title:  "Complexité"
category: cours
tags: informatique cours 
---

# Introduction 

On compte souvent (le nombre d'opération, la même prise, ...) en utilisant les *grand O* : $\mathcal{O}$ .

**Définition** :
Une fonction $g(N)$ est en $\mathcal{O}(f(N))$ s'il existe 2 constantes $c_0$ et $N_0$ tels que $g(N) < c_0 f(N)$ pour tout $N > N_0$.

Cela permet :

* d'avoir un majorant de notre comptage lorsque $N$ devient grand
* de ne pas s'occuper des constantes puisque $\mathcal{O}(\mbox{constante}) = \mathcal{O}(1)$
* de ne pas s'occuper de la proportionnalité $\mathcal{O}(\mbox{constante} * f(N)) = \mathcal{O}(f(N))$ 

Ce qui plutôt intéressant en informatique car :

* on veut voir l'évolution de la complexité par rapport à la taille des entrée
* la complexité d'un algorithme est nichée dans les boucles pas dans les opérations successives qui ne dépendent pas des données
	* comme les suites d'instructions constantes
	* ou une succession constante de boucles (seule la boucle est importante).

>**Remarque** : le nombre d'opérations d'un algorithme en grand O est proportionnel à sa durée 

## arithmétique des $\mathcal{O}$ (grand O)

Par abus de langage, on dira que :

* $f(N) = \mathcal{O}(g(N))$ plutôt que : "la fonction $f(N)$ est en $\mathcal{O}(g(N))$".
* $\mathcal{O}(f(N)) = \mathcal{O}(g(N))$ plutôt que "une fonction en $\mathcal{O}(f(N))$ est également en $\mathcal{O}(g(N))$".

On a alors les règles suivantes : 

* $N^p = \mathcal{O}(N^q)$ pour $q \geq p$
* $\mathcal{O}(1) = \mathcal{O}(2)$
* $\mathcal{O}(f(N)) + \mathcal{O}(g(N)) = \mathcal{O}(f(N) + g(N))$
* $\mathcal{O}(A*f(N)) = A * \mathcal{O}(f(N)) = \mathcal{O}(f(N))$
* $f(N) * \mathcal{O}(g(N)) = \mathcal{O}(f(N)*g(N))$

### exemple : quelle est la différence entre $\mathcal{O}(N^2 + N^3)$ et $\mathcal{O}(N^3)$

 On a
$\mathcal{O}(N^2 + N^3) = \mathcal{O}(N^2) + \mathcal{O}(N^3)$.
Comme $N^2$ est en $\mathcal{O}(N^3)$, $\mathcal{O}(N^2) + \mathcal{O}(N^3) = \mathcal{O}(N^3) + \mathcal{O}(N^3) = 2\mathcal{O}(N^3) = \mathcal{O}(N^3)$

## nombre d'opérations d'un algorithme


Pour un algorithme sa complexité désigne le **nombre maximum d'opérations** en notation $\mathcal{O}$ (grand O) par rapport aux **entrées**.

Cette complexité est proportionnelle à la durée max, si l'on connaît le temps max mis pour faire 1 opération

On peut aussi, compter le nombre de place mémoire maximum utilisée par l'algorithme par rapport aux entrées. On parle alors de **complexité en mémoire**


### Qu'est-ce qu'une opération ? 

C'est compliqué mais en gros c'est une *opération élémentaire* :

* un test 
* une affectation
* une opération arithmétique

En vrai : 

* tout est fait [avec des registres](https://ensiwiki.ensimag.fr/index.php?title=Constructions_de_base_en_assembleur_x86) et donc une somme deux deux entiers fait plus qu'une opération en assembleur
* personne ne sait vraiment combien de temps va prendre une opération à cause des optimisations du processeur


En revanche, ça prend un nombre maximum d'opérations qui est indépendant des données : c'est en $\mathcal{O}(1)$

>**Attention** : Toutes les autres opérations doivent être examinée, en particulier les méthodes d'objets qui peuvent prendre plus de temps. 

Exemple : 
```python

def imprime_majuscule(ma_chaine):
    ma_chaine_majuscule = ma_chaine.upper() # O(n) opérations où n est la longueur de la chaine
    print(ma_chaine_majuscule) # O(n) opérations
```

Attention cependant : dans l'exemple suivant, on manipule des constantes (la chaine est affectée et n'est pas un paramètre), tout est donc en $\mathcal{O}(1)$ :

```python
ma_chaine = "c'est vraiment très intéressant !"
print(ma_chaine)
```


### Qu'est-ce les paramètres d'une entrée ?

Ca dépend. Le but est juste de lier les entrées au nombre d'entrée. Cela peut être :

* un nombre passé en paramètre
* la taille d'un conteneur comme un tableau
* la place mémoire prise les entrées
* ...

Dans nos cas, cela sera toujours presque évident de savoir de quoi dépend la complexité.

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


### exemple 2 : quelle est la complexité de l'algorithme suivant

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

Complexité minimum : dans le meilleur des cas, le premier élément est la valeur et donc le nombre d'opération est $\mathcal{O}(1)$.


>**TBD** Calculer la complexité moyenne.


# structures

>**TBD** Exemple du tableau en regardant comment fonctionne la mémoire. Et les complexité de maintien de la structure.

objet = place dans la mémoire


---
layout: page
title:  "fonction de hash"
category: cours
---

Les fonctions de hashage. De la définition mathématique à son utilité en informatique.

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [théorie]({% link cours/algorithme-code-theorie/theorie/index.md %}) / [fonctions de hash]({% link cours/algorithme-code-theorie/theorie/fonctions-hash.md %})
>
> prérequis :
>
>* [fonctions]({% link cours/algorithme-code-theorie/theorie/fonctions.md %})
{: .chemin}

## définition

On peut définit dans toute sa généralité une [fonction de hashage](https://fr.wikipedia.org/wiki/Fonction_de_hachage) $f$ comme étant :

> Une **fonction de hashage** est une fonction $f$ :
>
> $$f: \mathbb{N} \rightarrow [0 \mathrel{ {.}\,{.} } m]$$
>
> où $m$  est un entier positif.
{: .note}

Une définition alternative, souvent utilisé en informatique, est :

> Une **fonction de hashage** est une fonction $f$ qui associe à tout mot de $\\{0, 1\\}^\star$ un mot de $\\{0, 1\\}^\star$ de longueur $m$.
>
> où $m$  est un entier positif.
{: .note}

Enfin, comme tout en informatique est codé comme une suite de 0 et de 1, une fonction de hashage peut être vue comme :

> Une **fonction de hashage** est une fonction qui associe un entier entre 0 et $m$ à tout objet.
>
> où $m$  est un entier positif.
{:.note}

En python par exemple, on peut utiliser la fonction [`hash`](https://docs.python.org/fr/3/library/functions.html?highlight=hash#hash) :

```python
>>> hash("du texte")
1183064373567153871
>>> hash(True)
1
>>> hash(1)
1
>>> hash(3.14)
322818021289917443
```

La principale raison de l'utilisation des fonctions de hashage est :

> Si $f$ est une fonction de hashage, alors :
>
> $$ f(a) \neq f(b) \rightarrow a \neq b$$
>
{:.note}

Une fonction de hashage permet de partitionner les entiers ({\em ie.} les objets) en $m+1$ classes. Pour que ce partitionnement soit utile, on demande à une *bonne* fonction de hashage d'avoir en plus les propriétés suivantes :

> Une fonction de hashage $f: \mathbb{N} \rightarrow [0\mathrel{ {.}\,{.} } m]$ utile doit avoir les 3 propriétés suivantes :
>
> 1. elle doit être {\bf équiprobable} : la probabilité que $f(a) = i $ doit être de $\frac{1}{m+1}$ pour tout $a\in \mathcal{N}$ et 0\eq i \leq m$
> 2. elle doit être facilement calculable
> 3. tout changement dans l'entrée doit produire un changement dans la sortie
>
{:.note}

## exemples

### une constante

facilement calculable.

Mais autrement peut d'intérêt.

### du modulo

équiprobable (même nombre d'éléments dans chaque classe)

facilement calculable : on peut couper par bloc

Mais : Si pas premier attention, pas forcément gros changements si les nombres changes exemple avec puissance de 10 (ou 2 ou quelconque pour la base)

## collisions

paradoxe des anniversaires

## utilisation

* résumé d'un objet (texte, commit dans github)
* dans des structure de données avancées : dictionnaire.

## hash cryptographique

### propriétés en plus

* doit changer (beaucoup) si on change un peu l'entrée (crypto)
* difficile de trouver 2 mots de même hash (crypto)
* trouver un mot qui a le même hash doit être compliqué (pour crypto)

il faut que de petit changement dans l'entrée produisentde gros changements dans la sortie.

### comment

sha-X

### exemple d'utilisation

* les mots de passes
* l'empreinte/vérification d'un texte/bibliothèque (hash sha)
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

* de N dans [0, k] déterministe

OK en info puisqu'on a vu que tout est un entier, donc une suite de 0 et de 1

* hash de 01* à O1m : déterministe

## exemple

### une constante

bof.

### du modulo

équiprobable (même nombre d'éléments dans chaque classe)

Mais : Si pas premier attention, pas forcément gros changements si les nombres changes exemple avec puissance de 10 (ou 2 ou quelconque pour la base)

## propriété voulues

* équiprobable (proba collision faible)
* calcul facile (implique calcul par bloc)
* doit dépendre de tout le mot : petit changement dans le mot doit produire de gros changement dans l'emprunte (pensez aux numéros de carte bleues)

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

### comment

sha-X

### exemple d'utilisation

* les mots de passes
* l'empreinte/vérification d'un texte/bibliothèque (hash sha)

>ici
{: .tbd}

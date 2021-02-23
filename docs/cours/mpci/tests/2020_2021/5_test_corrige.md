---
layout: page
title:  "corrigé Test 5 : modélisation"
category: cours
tags: informatique cours 
---

## introduction

Un code complet est [disponible](5_python.py).

## 1) créer le code python de la classe personnage en sachant qu'il doit pouvoir en plus exécuter le code suivant

La classe `Personnage` a tout ce qui est demandé par l'énoncé. On a implémenté la méthode `tape` pour qu'elle soit cohérente avec le code : l'assaillant enlève son attaque aux pv de l'assailli.

``` python
class Personnage:
    def __init__(self, pv=10, attaque=2):
        self.pv = pv
        self.attaque = attaque

    def get_pv(self):
        return self.pv

    def get_attaque(self):
        return self.attaque

    def set_attaque(self, attaque):
        self.attaque = attaque

    def tape(self, other):
        other.pv = other.pv - self.attaque
```

## 2) décrivez comment s'exécute la ligne balrog.tape(gandalf) du code précédent (en particulier les namespaces utilisés)

Lorsque la méthode s'éxécute, un *namespace* est crée pour elle.

1. dans ce *namespace* on place les paramètres de la méthode :
   * `self` : qui vaut l'objet à gauche du `.` donc `balrog`
   * `other` : qui vaut le 1er paramètre de l'appel donc `gandalf`
2. La ligne de code à exécuter est une affectation dnc :
   1. on cherche l'objet à droite du `=` : ici c'est une différence de :
      * l'objet de nom `attaque` dans le namespace de l'objet de nom `self` : c'est l'attaque de `balrog` qui est un entier valant 40.
      * l'objet de nom `pv` dans le namespace de l'objet de nom `other` : c'est les `pv` de `gandalf`  qui est un entier valant 4.
   2. le résultat de la soustraction est un entier valant -36
   3. on affecte cet entier au nom `pv` du namespace `other` : les `pv` de `gandalf` sont maintenant à -36.

Lorsque la méthode se finie, le *namespace* créé pour elle disparaît.

## 3) comment créer une méthode se_fait_taper_par(un_perso) en utilisant tape() ?

``` python
    def se_faire_taper_par(self, other):
        other.tape(self)
```

---
layout: page
title:  "sujet Test 5 : modélisation"
category: cours
tags: informatique cours 
---

## Introduction

Répondez aux questions dans l'ordre

On souhaite créer une classe Personnage dont les objets pourraient être créés :

* avec 2 paramètres :
  * le premier, les pv (points de vies), par défaut à 10
  * le second, l'attaque, par défaut à 2
* on doit pouvoir connaître les points de vie d'un personnage
* on doit pouvoir connaître et modifier l'attaque d'un personnage

## 1) créer le code python de la classe personnage en sachant qu'il doit pouvoir en plus exécuter le code suivant

```python
from personnage import Personnage

gandalf = Personnage(pv=4)
balrog = Personnage(20, 40)
balrog.tape(gandalf)

print("Le Balrog a donné", balrog.get_attaque(), "dégats à Gandalf")
print("il lui reste : ", gandalf.get_pv(), "pv (le pauvre)")
```

## 2) décrivez comment s'exécute la ligne balrog.tape(gandalf) du code précédent (en particulier les namespaces utilisés)

## 3) comment créer une méthode se_fait_taper_par(un_perso) en utilisant tape() ?

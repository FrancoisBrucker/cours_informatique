---
layout: page
title:  "MPCI S2 : Programmation 2"
category: cours
tags: informatique cours 
---

## Introduction

Cours de programmation 2 en S2 MPCI.

Est organisée en 3 types d'enseignements :

* séance de cours (**C,M**) : magistral.
  > pour acquérir  des connaissances de base
* séance tableau (**ST**) : exercices fait sans machine, accompagné d'un prof ou d'un corrigé
  > pour travailler/acquérir des connaissances théoriques
* séance machine (**SM**) : exercices fait avec votre machine, accompagné d'un prof ou d'un corrigé
  > pour travailler/acquérir des connaissances pratiques

Les divers contrôles intermédiaires seront à rendre directement sur [ametice](https://ametice.univ-amu.fr/course/view.php?id=70937).

## Séances

Chaque séance, à partir de la deuxième, commence par un test de 15min qui porte sur le cours précédent. Ce test sera à rendre sur [ametice](https://ametice.univ-amu.fr/course/view.php?id=70937).

* vendredi 4h : **C,M** suivi d'un **SM** : [pratiques de développement et développements pratique](#pratiques-de-développement-et-développements-pratique).
* mercredi 2h : **C,M** : [complexité et preuve](#complexité-et-preuve)
* vendredi 4h : **ST** suivi d'un **SM** : [exponentiation rapide](#exponentiation-rapide)

* mercredi 2h : **C,M** : [tris](#tris)
* vendredi 4h : **ST** suivi d'un **SM** : [tris](#tris)

* mercredi 2h : **DS** devoir surveillé
* vendredi 4h : **C,M** suivi d'un **SM** : [classes et objets](#classes-et-objets)

* mercredi 2h : **C,M** [algorithmes gloutons](#algorithmes-gloutons)
* vendredi 4h : **ST** [algorithmes gloutons](#algorithmes-gloutons)

* mercredi 2h : **DS** examen final

## Plan des cours

### pratiques de développement et développements pratique

1. [Algorithmie et code]({% link cours/mpci/cours_1_code/1_cours_algorithme_et_code.md %})
2. [pratiques de développement]({% link cours/mpci/cours_1_code/2_cours_pratiques_de_developpement.md %})
3. [développements pratiques]({% link cours/mpci/cours_1_code/3_cours_developpement_pratiques.md %})
4. [A vous]({% link cours/mpci/cours_1_code/4_a_vous_code.md %})

### complexité et preuve

1. [complexité]({% link cours/mpci/cours_2_complexite_et_preuve/1_cours_complexite.md %})
2. [preuve]({% link cours/mpci/cours_2_complexite_et_preuve/2_cours_preuve.md %})

### exponentiation rapide

1. [Algorithme de l'exponentiation rapide]({% link cours/mpci/cours_3_exponentiation_rapide/1_cours_exponentiation_rapide.md %})
2. [Code de l'exponentiation rapide]({% link cours/mpci/cours_3_exponentiation_rapide/2_code_exponentiation_rapide.md %})

### tris

1. [les tris]({% link cours/mpci/cours_4_tris/1_cours_tris.md %})
2. [session de code sur les tris]({% link cours/mpci/cours_4_tris/2_code_tris.md %})

### classes et objets

1. [le cours/ST]({% link cours/mpci/cours_5_classes_et_objets/1_cours_classes_et_objets.md %})
2. [séance tableau]({% link cours/mpci/cours_5_classes_et_objets/2_exercices_classes_et_objets.md %})
3. [le code]({% link cours/mpci/cours_5_classes_et_objets/3_code_classes_et_objets.md %})
4. bonus : [test driven development]({% link cours/mie/developpement_objet/tdd_et_test_pattern.md %}) pour vous entraîner à programmer par les tests en utilisant des classes.
5. si vous êtes chaud : [design patterns]({% link cours/mie/developpement_objet/design_patterns.md %}). Pour aller un peu plus loin dans le développement objet avec des design patterns.

### algorithmes gloutons

1. [cours]({% link cours/mpci/cours_6_gloutons/1_cours_gloutons.md %})
2. [le code]({% link cours/mpci/cours_6_gloutons/2_code_gloutons.md %})

## tests

1. code : [sujet]({% link cours/mpci/tests/2020_2021/1_test_sujet.md %}) et [corrigé]({% link cours/mpci/tests/2020_2021/1_test_corrige.md %})
2. complexité : [sujet]({% link cours/mpci/tests/2020_2021/2_test_sujet.md %}) et [corrigé]({% link cours/mpci/tests/2020_2021/2_test_corrige.md %})
3. preuve : [sujet]({% link cours/mpci/tests/2020_2021/3_test_sujet.md %}) et [corrigé]({% link cours/mpci/tests/2020_2021/3_test_corrige.md %})
4. [DS (sujet et corrigé)]({% link cours/mpci/tests/2020_2021/4_ds_corrige.md %})
5. modélisation : [sujet]({% link cours/mpci/tests/2020_2021/5_test_sujet.md %}) et [corrigé]({% link cours/mpci/tests/2020_2021/5_test_corrige.md %})
6. gloutons : [sujet]({% link cours/mpci/tests/2020_2021/6_test_sujet.md %}) et [corrigé]({% link cours/mpci/tests/2020_2021/6_test_corrige.md %})

## Misc

### tuto visual studio code

<https://code.visualstudio.com/docs/editor/codebasics>

### Tuto markdown

[Le format markdown]({% link cours/tuto/format_markdown.md %})

### tuto python

TBD

#### eval

#### import 

* `import truc` et pas `import truc.py`
* qu'est ce que *"__pycache__"* ?
* si on fait `from toto import toto` `toto`n'est plus le fichier *"toto.py"* mais le nom importé. SI ensuite on fait `from toto import tata` ça va planter.

#### tests

Si les tests ne sont pas révélé alors que vous avez des fichiers de tests. regardez les messages d'erreurs (où ?). SOuvent c'est du au fait qu'au moins un fichier de test ne peut être lu à cause d'erreurs (de syntaxe, d'import qui ne fonctionnent pas, ...)

#### bases de python

listes, variables etc.

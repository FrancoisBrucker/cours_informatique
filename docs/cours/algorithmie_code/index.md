---
layout: page
title:  "introduction au code et à l'algorithmie"
category: cours
---

## Introduction

> TBD : cours 2020/2021. Pas à jour.
{: .danger}

## Plan des cours

### pratiques de développement et développements pratique

1. [Algorithmie et code]({% link cours/algorithmie_code/cours_1_code/1_cours_algorithme_et_code.md %})
2. [pratiques de développement]({% link cours/algorithmie_code/cours_1_code/2_cours_pratiques_de_developpement.md %})
3. [développements pratiques]({% link cours/algorithmie_code/cours_1_code/3_cours_developpement_pratiques.md %})
4. [A vous]({% link cours/algorithmie_code/cours_1_code/4_a_vous_code.md %})

### complexité et preuve

1. [complexité]({% link cours/algorithmie_code/cours_2_complexite_et_preuve/1_cours_complexite.md %})
2. [preuve]({% link cours/algorithmie_code/cours_2_complexite_et_preuve/2_cours_preuve.md %})

### exponentiation rapide

1. [Algorithme de l'exponentiation rapide]({% link cours/algorithmie_code/cours_3_exponentiation_rapide/1_cours_exponentiation_rapide.md %})
2. [Code de l'exponentiation rapide]({% link cours/algorithmie_code/cours_3_exponentiation_rapide/2_code_exponentiation_rapide.md %})

### tris

1. [les tris]({% link cours/algorithmie_code/cours_4_tris/1_cours_tris.md %})
2. [session de code sur les tris]({% link cours/algorithmie_code/cours_4_tris/2_code_tris.md %})

### classes et objets

1. [le cours/ST]({% link cours/algorithmie_code/cours_5_classes_et_objets/1_cours_classes_et_objets.md %})
2. [séance tableau]({% link cours/algorithmie_code/cours_5_classes_et_objets/2_exercices_classes_et_objets.md %})
3. [le code]({% link cours/algorithmie_code/cours_5_classes_et_objets/3_code_classes_et_objets.md %})
4. bonus : [test driven development]({% link cours/developpement_objet/tdd_et_test_pattern.md %}) pour vous entraîner à programmer par les tests en utilisant des classes.
5. si vous êtes chaud : [design patterns]({% link cours/developpement_objet/design_patterns.md %}). Pour aller un peu plus loin dans le développement objet avec des design patterns.

### algorithmes gloutons

1. [cours]({% link cours/algorithmie_code/cours_6_gloutons/1_cours_gloutons.md %})
2. [le code]({% link cours/algorithmie_code/cours_6_gloutons/2_code_gloutons.md %})

## tests

1. code : [sujet]({% link cours/algorithmie_code/tests/2020_2021/1_test_sujet.md %}) et [corrigé]({% link cours/algorithmie_code/tests/2020_2021/1_test_corrige.md %})
2. complexité : [sujet]({% link cours/algorithmie_code/tests/2020_2021/2_test_sujet.md %}) et [corrigé]({% link cours/algorithmie_code/tests/2020_2021/2_test_corrige.md %})
3. preuve : [sujet]({% link cours/algorithmie_code/tests/2020_2021/3_test_sujet.md %}) et [corrigé]({% link cours/algorithmie_code/tests/2020_2021/3_test_corrige.md %})
4. [DS (sujet et corrigé)]({% link cours/algorithmie_code/tests/2020_2021/4_ds_corrige.md %})
5. modélisation : [sujet]({% link cours/algorithmie_code/tests/2020_2021/5_test_sujet.md %}) et [corrigé]({% link cours/algorithmie_code/tests/2020_2021/5_test_corrige.md %})
6. gloutons : [sujet]({% link cours/algorithmie_code/tests/2020_2021/6_test_sujet.md %}) et [corrigé]({% link cours/algorithmie_code/tests/2020_2021/6_test_corrige.md %})

## Misc

### tuto visual studio code

<https://code.visualstudio.com/docs/editor/codebasics>

### Tuto markdown

[Le format markdown]({% post_url tutos/2021-08-30-format-markdown %})

### tuto python

TBD

#### eval

#### import 

* `import truc` et pas `import truc.py`
* qu'est ce que *"__pycache__"* ?
* si on fait `from toto import toto` `toto`n'est plus le fichier *"toto.py"* mais le nom importé. SI ensuite on fait `from toto import tata` ça va planter.

#### tests

Si les tests ne sont pas révélé alors que vous avez des fichiers de tests. regardez les messages d'erreurs (où ?). Souvent c'est du au fait qu'au moins un fichier de test ne peut être lu à cause d'erreurs (de syntaxe, d'import qui ne fonctionnent pas, ...)

#### bases de python

listes, variables etc.

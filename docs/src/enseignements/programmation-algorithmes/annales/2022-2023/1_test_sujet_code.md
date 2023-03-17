---
layout: layout/post.njk

title:  "sujet Test 1 : code"
authors:
    - François Brucker
---

{% attention %}
Vous avez 15min pour faire le test.
{% endattention %}


Toute fonction écrite doit être testée :

{% note %}
Lorsque l'on vous demande d'***écrire une fonction***, cela **signifie** :

* écrire le code de la fonction
* écrire les tests qui vérifient son bon fonctionnement

{% endnote %}

Ce n'est pas grave si vous ne faites pas toutes les questions, mais si vous donnez une fonction sans ses tests ou qui ne fonctionne pas elle ne sera pas notée.

Enfin, faites aussi en sorte que votre code ait 0 défaut de style (le linter ne doit pas râler).

## But

On essaye d'écrire un programme qui joue au pendu.

## 1. fonction `est_une_lettre(lettre, mot)`{.language-}

On vous demande d'écrire la fonction `est_une_lettre(lettre, mot)`{.language-} telle que :

* **paramètres d'entrée** :
  1. `lettre`{.language-} un caractère
  2. `mot`{.language-} une chaîne de caractères
* **sortie** :
  * si au moins une des lettres de `mot`{.language-} et `lettre`{.language-}, la fonction rend `True`{.language-}
  * sinon, la fonction rend `False`{.language-}
* **exemples** :
  * `est_une_lettre("i", "victoire")`{.language-} doit rendre `True`{.language-}
  * `est_une_lettre("e", "la disparition")`{.language-} doit rendre `False`{.language-}

## 2. fonction `caractères(lettre, mot)`{.language-}

On vous demande d'écrire la fonction `caractères(lettre, mot)`{.language-} telle que :

* **paramètres d'entrée** :
  1. `lettre`{.language-} un caractère
  2. `mot`{.language-} une chaîne de caractères
* **sortie** :
  * une liste $L$ contenant tous les indices des caractères de `mot`{.language-} qui valent `lettre`{.language-}. Cette liste doit être triée par ordre croissant.
* **exemples** :
  * `caractères("i", "victoire")`{.language-} doit rendre `[1, 5]`{.language-}
  * `caractères("e", "la disparition")`{.language-} doit rendre `[]`{.language-}

## 3. fonction `découvre(mot_caché, lettre, positions)`{.language-}

On vous demande d'écrire la fonction `découvre(mot_caché, lettre, positions)`{.language-} telle que :

* **paramètres d'entrée** :
  1. `mot_caché`{.language-} une chaîne de caractères
  2. `lettre`{.language-} un caractère
  3. `positions`{.language-} une liste d'entiers rangés par ordre croissant
* **sortie** :
  * la chaîne de caractères `mot_caché`{.language-} où les indices correspondants aux entiers de `positions`{.language-} sont remplacés par `lettre`{.language-}
* **exemples** :
  * `découvre("......", "r", [1, 2, 5])`{.language-} doit rendre `".rr..r"`{.language-}
  * `découvre("erre.r", "u", [4])`{.language-} doit rendre `"erreur"`{.language-}
  * `découvre("erre.r", "u", [])`{.language-} doit rendre `"erre.r"`{.language-}

## 4. fonction `caché(mot)`{.language-}

On vous demande d'écrire la fonction `caché(mot)`{.language-} telle que :

* **paramètres d'entrée** :
  1. `mot`{.language-} une chaîne de caractères
* **sortie** :
  * une chaîne de caractères composée uniquement de `"."`{.language-} et de longueur égale à celle de `mot`{.language-}
* **exemples** :
  * `caché("anticonstitutionnellement")`{.language-} doit rendre `"........................."`{.language-}
  * `caché("")`{.language-} doit rendre `""`{.language-}

## 5. programme principal

Créez un programme principal permettant de jouer au pendu jusqu'à ce que le mot à trouver ne contienne plus de `"."`{.language-}

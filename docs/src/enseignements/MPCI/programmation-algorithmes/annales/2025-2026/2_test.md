---
layout: layout/post.njk

title:  "sujet Test 2 : programmation"
---

{% attention %}
Vous avez 15min pour faire le test.
{% endattention %}

## Rendu

On vous rappelle que toute fonction (hors du programme principal) doit être testée.

### Type de rendu

Vous devrez rendre le dossier d'un projet vscode (vous pouvez le compresser si nécessaire). Commencez donc par créer un projet dans un dossier que vous appellerez `test2`{.fichier}.

### Éléments de notation

1. 3 fichiers dans un projet :
    - le programme principal `main.py`{.fichier},
    - les fonctions utilisées `fonctions.py`{.fichier},
    - les tests des fonctions `test_fonctions.py`{.fichier}.
2. Du joli code : le code doit être passé par black.
1. Bons noms :
    - de fichiers,
    - de variables.
2. Tests unitaires : toute fonction doit être testée.

## Sujet

### 1 Entrée utilisateur

#### 1.1 Code

Créez une fonction de signature :

```pseudocode
parenthèses(s: chaîne) → chaîne  # la sortie est uniquement composée de parenthèses
```

Qui rend la restriction de la chaînes `s`{.language-} à ses parenthèses ouvrantes et fermantes.

Par exemples :

- `parenthèses("(1+2)-3")`{.language-} doit rendre la chaîne `"()"`{.language-}
- `parenthèses("coucou !")`{.language-} doit rendre la chaîne `""`{.language-}
- `parenthèses("coucou (toi) :)")`{.language-} doit rendre la chaîne `"())"`{.language-}

{% info %}
Vous pourrez utiliser le fait que `+`{.language-} est l'opérateur de concaténation pour deux chaines en python : `":" + ")`{.language-} valant `":)"`{.language-}
{% endinfo %}

#### 1.2 Programme principal

Demandez à l'utilisateur  de rentrer une chaîne de caractères puis affichez la restriction de la chaîne tapée à ses parenthèses. Par exemple :

```
Entrez une chaîne de caractères : coucou (toi) :)
La chaîne contient la suite de parenthèses : ())
```

### 2 Suite

#### 2.1 Code

Créez une fonction de signature :

```pseudocode
suite(s: chaîne) → [entier]  # l'entrée est uniquement composée de parenthèses
```

Qui rend à partir d'une chaîne de caractères `s`{.language-} uniquement constituée de parenthèses ouvrantes et fermantes un tableau d'entier `t`{.language-} de même longueur tel que `t[i] = 1`{.language-} si `s[i] = '('`{.language-} et `t[i] = -1`{.language-} si `s[i] = ')'`{.language-}

Par exemples :

- `suite("()")`{.language-} doit rendre la liste `[1, -1]`{.language-}
- `suite("")`{.language-} doit rendre la liste `[]`{.language-}
- `suite("())")`{.language-} doit rendre la liste `[1, -1, -1]`{.language-}

{% info %}
Vous pourrez utiliser la méthode `append`{.language-} des listes qui ajoute un élément en fin de liste.
{% endinfo %}

#### 2.2 Programme principal

Ajoutez à votre programme principal l'affichage de la suite.

Par exemple :

```
Entrez une chaîne de caractères : coucou (toi) :)
La chaîne contient la suite de parenthèses : ())
La suite associée est : [1, -1, -1]
```

### 3 Bon parenthésage

{% lien %}
<https://fr.wikipedia.org/wiki/Langage_de_Dyck>
{% endlien %}

La suite crée précédemment permet de déterminer si la chaîne initiale est un bon parenthésage. En effet, on peut montrer qu'une liste $t$ définie comme en 2 correspond à un bon parenthésage si et seulement si :

$\sum_{0 \leq i < m}t[i] \geq 0$ pour tout $0 \leq m < \text{len}(t)$

Une telle liste est appelée liste de Dyck.

#### 3.1 Code

Créez une fonction de signature :

```pseudocode
bon_parenthésage(l: [entier]) → booléen  # l'entrée est uniquement composée de 1 et de -1
```

Qui rend à partir d'une liste de 1 et de -1 :

- `Vrai` si la liste en entrée est une liste de Dyck
- `Faux` sinon

Par exemples :

- `bon_parenthésage([1, -1])`{.language-} doit rendre `True`{.language-}
- `bon_parenthésage([])`{.language-} doit rendre `True`{.language-}
- `parenthèses([1, -1, -1, 1])`{.language-} doit rendre `False`{.language-}

#### 3.2 Programme principal

Ajoutez à votre programme principal l'affichage de la suite.

Par exemple :

```
Entrez une chaîne de caractères : coucou (toi) :)
La chaîne contient la suite de parenthèses : ())
La suite associée est : [1, -1, -1]
La suite ne correspond pas à un bon parenthésage
```
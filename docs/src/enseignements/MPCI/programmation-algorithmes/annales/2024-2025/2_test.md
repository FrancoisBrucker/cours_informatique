---
layout: layout/post.njk

title:  "sujet Test 2 : code"
authors:
    - François Brucker
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
2. Du joli code :
    - 0 warning,
    - le code doit être passé par black.
3. Bons noms :
    - de fichiers,
    - de variables.
4. Tests unitaires : toute fonction non testée ne sera pas corrigée.

## Sujet

### 1 Suite alternante

#### 1.1 Code

Créez une fonction de signature :

```pseudocode
alternante(n: entier, a: caractère, b: caractère) → chaîne
```

Elle devra rendre une chaîne de caractères de longueur `n`{.language-} alternant les caractères `a`{.language-} et `b`{.language-} et en commençant par `a`{.language-}.

Par exemples :

- `alternante(4, "0", "1")`{.language-} doit rendre la chaîne `"0101"`{.language-}
- `alternante(7, "1", "z")`{.language-} doit rendre la chaîne `"1z1z1z1"`{.language-}

{% info %}
Vous pourrez utiliser le fait que `+`{.language-} est l'opérateur de concaténation pour deux chaines en python : `"0" + "1"`{.language-} valant `"01"`{.language-}
{% endinfo %}

#### 1.2 Programme principal

Demandez à l'utilisateur un entier $n$ (vous ne ferez aucun test de vérification) puis affichez une suite alternante de "0" et de "1" de longueur $n$ **par ligne de 5 caractères**. Par exemple si l'utilisateur donne $n = 12$ vous afficherez :

```
01010
10101
01
```

{% info %}
Vous pourrez utiliser le fait que `int(c)`{.language-} rendra un entier si `c`{.language-} est une chaîne de caractères représentant un entier.
{% endinfo %}

### 2 Suite croissante

#### 2.1 Code

Créez une fonction de signature :

```pseudocode
croissante_alternante(n: entier, c: chiffre) → chaîne
```

Qui devra rendre :

- `"567"`{.language-} pour `croissante_alternante(3, 5)`{.language-}
- `"4567891234567"`{.language-} pour `croissante_alternante(13, 4)`{.language-}
- `"1234567891234567891"`{.language-} pour `croissante_alternante(19, 1)`{.language-}

{% info %}
Vous pourrez utiliser le fait que `str(m)`{.language-} rendra une chaîne de caractère si `m`{.language-} est un entier.
{% endinfo %}

#### 2.2 Programme principal

Ajoutez à votre programme principal une suite croissante alternante de longueur $n$ commençant à partir de 1 **par ligne de 5 caractères**.

Par exemple si l'utilisateur donne $n = 12$ vous afficherez :

```
12345
67891
23
```

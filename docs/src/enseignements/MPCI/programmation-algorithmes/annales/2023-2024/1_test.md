---
layout: layout/post.njk

title:  "sujet Test 1 : code"
authors:
    - François Brucker
---

{% attention %}
Vous avez 15min pour faire le test.
{% endattention %}

## Rendu

On vous rappelle que toute fonction (hors du programme principal) doit être testée.

### Type de rendu

Vous devrez rendre le dossier d'un projet vscode (vous pouvez le compresser si nécessaire). Commencez donc par créer un projet dans un dossier que vous appellerez `test1`{.fichier}.

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

{% aller %}
[Le compte est bon](/cours/coder-et-développer/projet-codes/#compte-caractere){.interne}
{% endaller %}

## Barème

Une note sur 4 répartie comme suit :

- 1 point de note de style répartit en :
  - 1/4 point si trois fichiers utilisés : `main.py`{.language-} pour le programme principal, `fonctions.py`{.language-} pour le code des fonctions utilisées dans le programme principal et `test_fonctions.py`{.language-} pour les tests des fonctions de `fonctions.py`{.language-}
  - 1/4 point pour le choix de noms de variables explicites
  - 1/4 point si les tests passent et/ou sont cohérent avec le code
  - 1/4 point si black a été utilisé pour que le code soit agréable à lire
- 1 point pour la question 1 répartit en :
  - 1/3 point pour la gestion du `while`{.language-}
  - 1/3 point pour l'utilisation de la fonction `find`{.language-} ou du recodage de sa fonctionnalité
  - 1/3 point pour le reste (`input`{.language-}, ...)
- 1 point pour la question 2 répartit en :
  - 1/3 point pour le code de la fonction
  - 1/3 point pour les tests de la fonction
  - 1/3 point pour l'utilisation de la fonction dans le programme principal (ou à minima la fonctionnalité utilisée)
- 1 point pour la question 3 répartit en :
  - 1/3 point pour le code de la fonction
  - 1/3 point pour les tests de la fonction
  - 1/3 point pour l'utilisation de la fonction dans le programme principal (ou à minima la fonctionnalité utilisée)

La question 4 n'a été abordée par personne.

La note sur $20$ finale est obtenue en multipliant la note sur 4 par $5$

{% note "**Objectif du test**" %}

En 15 minutes :

- **un élève *normal*** doit parvenir à faire la première question sans le `while`{.language-} et le code/test de la deuxième question. Ce qui lui permet d'avoir 2.333333 points sur 4, soit 11.66666/20
- **un bon élève** doit parvenir à réussir les 2 premières questions. Ce qui lui permet d'avoir 3/4 et donc 15/20
- **un très bon élève** fait plus que les 2 premières questions.

{% endnote %}

La ventilation des notes est :

|note/4   | ≤1 | ]1, 1.5]   | ]1.5, 2]   | ]2, 2.25]    | ]2.25, 2.5] | ]2.5,2.75]  | ]2.75, 3] | ]3, 3.5]     | >3.5|
|note/20  |≤4.2| [5.2, 6.7] | [8.3, 10]  | [10.4, 11.3] | [11.7, 12.5]| [12.9, 13.8]| [14.2, 15]| [15.4, 17.1] | 18.3|
|---------|----|------------|------------|--------------|-------------|-------------|-----------|--------------|-----|
|nombre   | 4  |  3         |  8         |  6           |  9          | 6           | 4         |  4           |  1  |
|rang min | 42 | 39         | 31         | 25           | 16          | 10          | 6         |  2           |  1  |
| # <     |  0 |  4         |  7         | 15           | 21          | 30          | 36        | 40           |  44 |

- moyenne : 11.1/20 (2.22/4)
- écart-type : 3.57/20 (0.71/4)
- médiane : 11.67/20 (2.33/4)

Je suis globalement content de vous, vous avez globalement tous travaillé pour le test et la plupart des notes en dessous de 10 sont dues à un manque d'expérience. Quelques notes sont cependant préoccupantes et il faudra vraiment travailler sa production de code et comprendre comment tout ceci fonctionne ensemble.

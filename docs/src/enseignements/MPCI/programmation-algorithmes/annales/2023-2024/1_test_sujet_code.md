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

## 1. Création du programme principal

Créer le fichier `main.py`{.fichier} qui va contenir le programme principal. Celui-ci consistera à demander à l'utilisateur une chaine de caractères et un caractère et l'on cherchera à savoir combien de fois apparait le caractère dans la chaîne. Nous allons répondre à cette question en 3 questions.

{% faire %}
Créer dans le fichier `main.py`{.fichier} le code permettant d'exécuter les 4 étapes de l'algorithme suivant :

1. Demander à l'utilisateur une chaîne de caractères que l'on nommera `chaine_entrée`{.language-} (en utilisant [la fonction `input([prompt: str]) -> str`{.language-}](https://docs.python.org/fr/3/library/functions.html#input))
2. Demander à l'utilisateur un caractère que l'on nommera `caractère_entrée`{.language-} (vous ne ferez aucune vérification de type)
3. Afficher à l'écran le plus petit indice (ou -1) de `chaine_entrée`{.language-} valant `caractère_entrée`{.language-} (vous pourrez utiliser [la méthode `find`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.find) des chaines de caractères)
4. Retournez à l'étape 1. de cet algorithme à part si `chaîne_entrée`{.language-} valait `"sortie"`{.language-}

{% endfaire %}

## 2. Prochain indice

On veut savoir si le caractère `caractère_entrée`{.language-} apparait plusieurs fois dans la chaine `chaine_entrée`{.language-}. Comme on connait déjà le premier indice où il apparait, on cherche s'il apparait aussi plus tard.

### Fonction `donne_prochain_indice(chaine:str, indice:int) -> int`{.language-}

{% faire %}
Créer la fonction `donne_prochain_indice(chaine:str, indice:int) -> int`{.language-} qui rend :

- Le plus petit indice $j$ strictement plus grand que le paramètre `indice`{.language-} tel que `chaine[j] == chaine[indice]`{.language-},
- `None`{.language-} si cet indice n'existe pas.

{% endfaire %}

### Tests de `donne_prochain_indice(chaine:str, indice:int) -> int`{.language-}

Vous pourrez tester que :

- `donne_prochain_indice("bxaaxaaaxax", 4)`{.language-} rende 8
- `donne_prochain_indice("bxaaxaaaxax", 0)`{.language-} rende `None`{.language-}

### Ajout de question 2 au programme principal

On ajoute notre fonction au programme principal :

{% faire %}
Dans l'étape 3. de l'algorithme du programme principal, **utilisez la fonction que vous venez de coder** pour ajouter un affichage qui indique si `caractère_entrée`{.language-} apparait plusieurs fois dans `chaine_entrée`{.language-} ou pas.
{% endfaire %}
{% info %}
L'étape 3. du programme principal sera alors constitué de deux actions :

- Afficher à l'écran le plus petit indice (ou -1) de `chaine_entrée`{.language-} valant `caractère_entrée`{.language-} (vous pourrez utiliser [la méthode `find`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.find) des chaines de caractères) (***question 1***)
- Afficher si `caractère_entrée`{.language-} est présent plus d'une fois dans `chaine_entrée`{.language-} (***question 2***)
{% endinfo %}

## 3. Compte

On veut finalement savoir combien de fois apparaît `caractère_entrée`{.language-} dans la chaîne `chaine_entrée`{.language-}. Comme on connait sa première position grace à la question 1 et qu'on peut connaitre la suivante grace  à la question 2, on va terminer le boulot et compter combien de fois apparaît `caractère_entrée`{.language-} dans `chaine_entrée`{.language-}.

### Fonction `compte_caractère(chaine: str, indice: int) -> int`{.language-}

{% faire %}
Créer la fonction `compte_caractère(chaine: str, indice: int) -> int`{.language-} qui rend le nombre de fois où le caractère `chaine[indice]`{.language-} est présent dans le paramètre `chaine`{.language-}

{% endfaire %}

### Tests de `compte_caractère(chaine: str, indice: int) -> int`{.language-}

Vous pourrez tester avec :

- Un caractère non présent dans la chaine
- Un caractère présent plusieurs fois dans la chaine

### Ajout de question 3 au programme principal

{% faire %}
Dans l'étape 3. de l'algorithme du programme principal, **utilisez la fonction que vous venez de coder** pour ajouter un affichage qui indique le nombre de fois où  `caractère_entrée`{.language-} apparait dans `chaine_entrée`{.language-}.
{% endfaire %}
{% info %}
L'étape 3. du programme principal sera alors constitué de trois actions :

- Afficher à l'écran le plus petit indice (ou -1) de `chaine_entrée`{.language-} valant `caractère_entrée`{.language-} (vous pourrez utiliser [la méthode `find`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.find) des chaines de caractères) (***question 1***)
- Afficher à l'écran si `caractère_entrée`{.language-} est présent plus d'une fois dans `chaine_entrée`{.language-} (***question 2***)
- Afficher à l'écran le nombre de fois où  `caractère_entrée`{.language-} apparait dans `chaine_entrée`{.language-} (***question 3***)
{% endinfo %}

## 4. Maximum

Cerise sur le gateau, on cherche à savoir si `caractère_entrée`{.language-} est le caractère qui apparait le plus de fois dans `chaine_entrée`{.language-}.

### Fonction `donne_max_doublon(chaine: str) -> str`{.language-}

Créer la fonction  `donne_max_doublon(chaine: str) -> str`{.language-} qui rend le caractère de `chaine`{.language-} apparaissant le plus de fois.

{% faire %}
Créer la fonction  `donne_max_doublon(chaine: str) -> str`{.language-} qui rend le caractère de `chaine`{.language-} apparaissant le plus de fois.

{% endfaire %}

### Tests

Vous pourrez tester avec une chaine admettant plusieurs caractères répétés un nombre différent de fois.

### Ajout de question 4 au programme principal

{% faire %}
Dans l'étape 3. de l'algorithme du programme principal, **utilisez la fonction que vous venez de coder** pour  ajouter un affichage qui le nombre maximum de répétition d'un caractère, et affichez un message de victoire si `caractère_entrée`{.language-} réalise ce maximum.
{% endfaire %}
{% info %}
L'étape 3. du programme principal sera alors constitué de quatre actions :

- Afficher à l'écran le plus petit indice (ou -1) de `chaine_entrée`{.language-} valant `caractère_entrée`{.language-} (vous pourrez utiliser [la méthode `find`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.find) des chaines de caractères) (***question 1***)
- Afficher à l'écran si `caractère_entrée`{.language-} est présent plus d'une fois dans `chaine_entrée`{.language-} (***question 2***)
- Afficher à l'écran le nombre de fois où  `caractère_entrée`{.language-} apparait dans `chaine_entrée`{.language-} (***question 3***)
- Afficher à l'écran  le nombre maximum de répétition d'un caractère, et affichez un message de victoire si `caractère_entrée`{.language-} réalise ce maximum. (***question 4***)
{% endinfo %}

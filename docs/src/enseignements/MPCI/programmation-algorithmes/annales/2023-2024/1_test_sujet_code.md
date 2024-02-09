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

Créer le fichier `main.py`{.fichier} qui va contenir le programme principal. Celui-ci consistera à :

1. Demander à l'utilisateur une chaîne de caractères que l'on nommera `chaine_entrée`{.language-} (en utilisant [la fonction `input([prompt: str]) -> str`{.language-}](https://docs.python.org/fr/3/library/functions.html#input))
2. Demander à l'utilisateur un caractère que l'on nommera `caractère_entrée`{.language-} (vous ne ferez aucune vérification de type)
2. Afficher 
    1. Le plus petit indice (ou -1) de `chaine_entrée`{.language-} valant `caractère_entrée`{.language-} (vous pourrez utiliser [la méthode `find`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.find) des chaines de caractères)
3. Retour en 1., à part si `chaîne_entrée`{.language-} valait `"sortie"`{.language-}

## 2. Prochain indice

### Fonction `donne_prochain_indice(chaine:str, indice:int) -> int`{.language-}

Créer la fonction `donne_prochain_indice(chaine:str, indice:int) -> int`{.language-} qui rend :

- Le plus petit indice $j$ strictement plus grand que le paramètre `indice`{.language-} tel que `chaine[j] == chaine[indice]`{.language-},
- `None`{.language-} si cet indice n'existe pas.

### Tests de `donne_prochain_indice(chaine:str, indice:int) -> int`{.language-}

Vous pourrez tester que :

- `donne_prochain_indice("bxaaxaaaxax, 4)`{.language-} rende 8
- `donne_prochain_indice("bxaaxaaaxax, 0)`{.language-} rende `None`{.language-} 


### Programme principal

Ajouter à la partie afficher du programme principal :

2. Afficher
    2. Si `caractère_entrée`{.language-} est présent plus d'une fois dans `chaine_entrée`{.language-} 

## 3. Compte

### Fonction `compte_caractère(chaine: str, indice: int) -> int`{.language-}

Créer la fonction `compte_caractère(chaine: str, caractère: str) -> int`{.language-} qui rend le nombre de fois où le paramètre `caractère`{.language-} est présent dans le paramètre `chaine`{.language-}

### Tests de `compte_caractère(chaine: str, indice: int) -> int`{.language-}

Vous pourrez tester avec :

- Un caractère non présent dans la chaine
- Un caractère présent plusieurs fois dans la chaine

### Programme principal

Ajouter à la partie afficher du programme principal :

2. Afficher
    3. Le résultat de `compte_caractère(chaine_entrée, indice_caractère_entrée)`{.language-} si `caractère_entrée`{.language-} est dans `chaine_entrée`{.language-} (`indice_caractère_entrée`{.language-} est le premier indice où `caractère_entrée`{.language-} est dans `chaine_entrée`{.language-})

## 4. Maximum

### Fonction `donne_max_doublon(chaine: str) -> str`{.language-}

Créer la fonction  `donne_max_doublon(chaine: str) -> str`{.language-} qui rend le caractère de `chaine`{.language-} apparaissant le plus de fois.

### Tests

Vous pourrez tester avec une chaine admettant plusieurs caractères répétés un nombre différent de fois.

### Programme principal

Ajouter dans le programme principal :

2. Afficher
    4. Le résultat de `donne_max_doublon(chaine)`{.language-} pour la chaîne rentrée par l'utilisateur
    5. Afficher un message de victoire si `caractère_entrée`{.language-} réalise ce maximum.



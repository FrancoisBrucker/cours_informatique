---
layout: layout/post.njk

title: "Le compte est bon"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---




## 1. Création du programme principal

Créer le fichier `main.py`{.fichier} qui va contenir le programme principal. Celui-ci consistera à demander à l'utilisateur une chaîne de caractères et un caractère et l'on cherchera à savoir combien de fois apparaît le caractère dans la chaîne. Nous allons répondre à cette question en 3 questions.

{% faire %}
Créer dans le fichier `main.py`{.fichier} le code permettant d'exécuter les 4 étapes de l'algorithme suivant :

1. Demander à l'utilisateur une chaîne de caractères que l'on nommera `chaîne_entrée`{.language-} (en utilisant [la fonction `input([prompt: str]) -> str`{.language-}](https://docs.python.org/fr/3/library/functions.html#input))
2. Demander à l'utilisateur un caractère que l'on nommera `caractère_entrée`{.language-} (vous ne ferez aucune vérification de type)
3. Afficher à l'écran le plus petit indice (ou -1) de `chaîne_entrée`{.language-} valant `caractère_entrée`{.language-} (vous pourrez utiliser [la méthode `find`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.find) des chaînes de caractères)
4. Retournez à l'étape 1. de cet algorithme à part si `chaîne_entrée`{.language-} valait `"sortie"`{.language-}

{% endfaire %}

## 2. Prochain indice

On veut savoir si le caractère `caractère_entrée`{.language-} apparaît plusieurs fois dans la chaîne `chaîne_entrée`{.language-}. Comme on connaît déjà le premier indice où il apparaît, on cherche s'il apparaît aussi plus tard.

### Fonction `donne_prochain_indice(chaîne:str, indice:int) -> int`{.language-}

{% faire %}
Créer la fonction `donne_prochain_indice(chaîne:str, indice:int) -> int`{.language-} qui rend :

- Le plus petit indice $j$ strictement plus grand que le paramètre `indice`{.language-} tel que `chaîne[j] == chaîne[indice]`{.language-},
- `None`{.language-} si cet indice n'existe pas.

{% endfaire %}

### Ajout de question 2 au programme principal

On ajoute notre fonction au programme principal :

{% faire %}
Dans l'étape 3. de l'algorithme du programme principal, **utilisez la fonction que vous venez de coder** pour ajouter un affichage qui indique si `caractère_entrée`{.language-} apparaît plusieurs fois dans `chaîne_entrée`{.language-} ou pas.
{% endfaire %}
{% info %}
L'étape 3. du programme principal sera alors constitué de deux actions :

- Afficher à l'écran le plus petit indice (ou -1) de `chaîne_entrée`{.language-} valant `caractère_entrée`{.language-} (vous pourrez utiliser [la méthode `find`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.find) des chaînes de caractères) (***question 1***)
- Afficher si `caractère_entrée`{.language-} est présent plus d'une fois dans `chaîne_entrée`{.language-} (***question 2***)
{% endinfo %}

## 3. Compte

On veut finalement savoir combien de fois apparaît `caractère_entrée`{.language-} dans la chaîne `chaîne_entrée`{.language-}. Comme on connaît sa première position grace à la question 1 et qu'on peut connaître la suivante grace  à la question 2, on va terminer le boulot et compter combien de fois apparaît `caractère_entrée`{.language-} dans `chaîne_entrée`{.language-}.

### Fonction `compte_caractère(chaîne: str, indice: int) -> int`{.language-}

{% faire %}
Créer la fonction `compte_caractère(chaîne: str, indice: int) -> int`{.language-} qui rend le nombre de fois où le caractère `chaîne[indice]`{.language-} est présent dans le paramètre `chaîne`{.language-}

{% endfaire %}

### Ajout de question 3 au programme principal

{% faire %}
Dans l'étape 3. de l'algorithme du programme principal, **utilisez la fonction que vous venez de coder** pour ajouter un affichage qui indique le nombre de fois où  `caractère_entrée`{.language-} apparaît dans `chaîne_entrée`{.language-}.
{% endfaire %}
{% info %}
L'étape 3. du programme principal sera alors constitué de trois actions :

- Afficher à l'écran le plus petit indice (ou -1) de `chaîne_entrée`{.language-} valant `caractère_entrée`{.language-} (vous pourrez utiliser [la méthode `find`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.find) des chaînes de caractères) (***question 1***)
- Afficher à l'écran si `caractère_entrée`{.language-} est présent plus d'une fois dans `chaîne_entrée`{.language-} (***question 2***)
- Afficher à l'écran le nombre de fois où  `caractère_entrée`{.language-} apparaît dans `chaîne_entrée`{.language-} (***question 3***)
{% endinfo %}

## 4. Maximum

Cerise sur le gateau, on cherche à savoir si `caractère_entrée`{.language-} est le caractère qui apparaît le plus de fois dans `chaîne_entrée`{.language-}.

### Fonction `donne_max_doublon(chaîne: str) -> str`{.language-}

Créer la fonction  `donne_max_doublon(chaîne: str) -> str`{.language-} qui rend le caractère de `chaîne`{.language-} apparaissant le plus de fois.

{% faire %}
Créer la fonction  `donne_max_doublon(chaîne: str) -> str`{.language-} qui rend le caractère de `chaîne`{.language-} apparaissant le plus de fois.

{% endfaire %}

### Ajout de question 4 au programme principal

{% faire %}
Dans l'étape 3. de l'algorithme du programme principal, **utilisez la fonction que vous venez de coder** pour  ajouter un affichage qui le nombre maximum de répétition d'un caractère, et affichez un message de victoire si `caractère_entrée`{.language-} réalise ce maximum.
{% endfaire %}
{% info %}
L'étape 3. du programme principal sera alors constitué de quatre actions :

- Afficher à l'écran le plus petit indice (ou -1) de `chaîne_entrée`{.language-} valant `caractère_entrée`{.language-} (vous pourrez utiliser [la méthode `find`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.find) des chaînes de caractères) (***question 1***)
- Afficher à l'écran si `caractère_entrée`{.language-} est présent plus d'une fois dans `chaîne_entrée`{.language-} (***question 2***)
- Afficher à l'écran le nombre de fois où  `caractère_entrée`{.language-} apparaît dans `chaîne_entrée`{.language-} (***question 3***)
- Afficher à l'écran  le nombre maximum de répétition d'un caractère, et affichez un message de victoire si `caractère_entrée`{.language-} réalise ce maximum. (***question 4***)
{% endinfo %}

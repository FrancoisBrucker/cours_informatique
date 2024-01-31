---
layout: layout/post.njk

title:  "Palindromes : le code"
---


Nous allons ici mettre en oeuvre des algorithmes de reconnaissances de phrases palindromes. Vous serez certainement amené à coder quelques-uns des algorithmes que vous avez forgé dans [la partie algorithmie](../algorithmie) de ce projet.

{% attention %}
Pour le code python, il faudra impérativement :

- faire les tests unitaires de chaque fonction. Ils devront tous se lancer via la commande `python -m pytest`
- organisez votre code en autant de fichiers que nécessaire.
{% endattention %}

## Palindromes

### Algorithme palindrome

{% faire %}
Implémentez [l'algorithme  `palindrome(s: str) -> bool`{.language-} linéaire de la partie algorithmie](../algorithmie/#palindrome_linéaire){.language-}

{% endfaire %}

### Programme principal palindrome

{% faire %}
Créez un programme principal nommé `main-palindrome.py`{.fichier} qui demande à l'utilisateur de donner une chaîne de caractères et le programme répond "oui" si la chaîne est un palindrome et "non" sinon.
{% endfaire %}

### Bonus

En bonus. Ne sera pas noté car très dur à trouver sans google.

{% faire %}
Il y a un moyen en python de savoir si une chaîne de caractères est un palindrome en une instruction et un slice. Explicitez là si vous la trouvez.
{% endfaire %}

## Phrases palindromes

Pour traiter des phrases palindrome à partir d'un texte en français, il faut commencer par pré-traiter le texte pour qu'il ne contienne plus que des lettres non accentuées en majuscules.

### Prétraitement

{% faire %}

Créer une fonction `prétraitement(s: str) -> str` qui effectue le prétraitement d'une chaîne de caractères. Pour cela vous pourrez utiliser, dans l'ordre :

1. le module [`unidecode`{.language-}](https://pypi.org/project/Unidecode/) (qu'il vous faudra installer avec `pip`) qui permet de supprimer les accents des caractères
2. [la méthode `upper`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.upper) des chaînes de caractères qui majuscule les lettres
3. d'utiliser l'instruction `re.sub("[^A-Za-z]","",s)`{'.language-} (`sub`{.language-} est une fonction [du module `re`](https://docs.python.org/fr/3/library/re.html) de python) qui qui rend une chaîne ne possédant que les caractères alphabétique de `s`{.language-}.
{% endfaire %}
{% info %}
[le module `re`](https://docs.python.org/fr/3/library/re.html) de python permet de filtrer une chaîne de caractère selon [une expression régulière](https://fr.wikipedia.org/wiki/Expression_régulière). Ceci dépasse le cadre de ce cours d'algorithmie mais en deux mots `re.sub("[^A-Z]","",s)`{'.language-} va rendre une nouvelle chaîne de caractères en :

   1. regardant caractère par caractère le troisième paramètre (ici `s`{.language-}).
   2. elle ne conservera que les éléments décrits par le premier paramètre (ici `"[^A-Z]"`{.language-} qui signifie toutes les lettres en majuscules)
   3. les autres caractères étant remplacés par le second paramètre (ici `""`{.language-}, la chaîne vide)

{% endinfo %}

### Programme principal phrase palindrome

{% faire %}
Créez un programme principal nommé `main-phrase-palindrome.py`{.fichier} qui demande à l'utilisateur de donner une chaîne de caractères et le programme répond "oui" si la chaîne est une phrase palindrome et "non" sinon.
{% endfaire %}

### Fichier texte

On peut très facilement lire un fichier texte en python en utilisant l'instruction :

```python
s = open(nom_du_fichier).read()
```

Utilisez cette instruction pour vérifier que le texte contenu dans le fichier [`perec.txt`{.fichier}](../perec.txt){.fichier} (cliquez droit sur le lien et choisissez de le télécharger) est une phrase palindrome. On le doit à [Georges Perec](https://fr.wikipedia.org/wiki/Georges_Perec) écrivain et poète Français.

## Sous-palindrome

> TBD utiliser pytermgui pour colorier en rouge le max

### Algorithme

Implémentez l'algorithme le plus efficace que vous êtes arrivé à produire dans la partie algorithmie pour résoudre le problème du sous-palindrome

### Programme principal

> TBD expliciter tous les sous palindrome de taille >= k
> Utiliser la partie 2 pour l'appliquer aux textes avec espaces et accents
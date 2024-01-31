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

### Bonus

On peut très facilement lire un fichier texte en python en utilisant l'instruction :

```python
s = open(nom_du_fichier).read()
```

Utilisez cette instruction pour vérifier que le texte contenu dans le fichier [`perec.txt`{.fichier}](../perec.txt){.fichier} (cliquez droit sur le lien et choisissez de le télécharger) est une phrase palindrome. On le doit à [Georges Perec](https://fr.wikipedia.org/wiki/Georges_Perec) écrivain et poète Français.

## Sous-palindrome

> TBD utiliser pytermgui pour colorier en rouge le max

### Algorithme

Implémentez l'algorithme le plus efficace que vous êtes arrivé à produire dans la partie algorithmie pour résoudre le problème du sous-palindrome


## Fichiers

> TBD juste la base (on fera mieux, peut-être, plus tard)

### Palindromes

> charger fichier texte avec perec
>
### sous-Palindromes


> sous-palindrome faire l'algo en n3 et en n et vérifier la différence de temps complexité pour perec.
> 
> Tester avec d'autres fichiers en utf8 des fichier de l'internet. Dire comment lire (prendre en utf8).
> TBD

1. créez des mots aléatoires de taille $n$ à partir d'une chaîne alphabet $A$
2. texte :
   1. téléchargement et lecture (dossier courant)
   2. trick utf8
   3. uppercase et suppression espace
3. palindrome algo

4. télécharge fichier <https://www.gutenberg.org/ebooks/6099> Il faudra peut-être forcer le téléchargement, parfois chrome le bloque
5. charge fichier texte en python en entier et en une fois (pas plus)
6. <https://github.com/avian2/unidecode>
7. supprime espace (ou même garde que les caractères A-Z ?`"".join(filter(lambda x: x.isalpha(), string))`{.language-}. Liste vers chaîne sinon va être trop long. Peut être aussi d'abord voir avec un ensemble tous les caractères, puis les caractères non alphabet)
8. fonction

> <https://www.arretetonchar.fr/wp-content/uploads/2013/IMG/pdf_Georges_Perec_le_grand_palindrome.pdf>

> TBD expliciter tous les sous palindrome de taille >= k
>


### Création de palindromes


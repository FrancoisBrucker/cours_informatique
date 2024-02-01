---
layout: layout/post.njk

title:  "Palindromes : le code"
---


Nous allons ici mettre en oeuvre des algorithmes de reconnaissance de phrases palindromes. Vous serez certainement amené à coder quelques-uns des algorithmes que vous avez forgés dans [la partie algorithmie](../algorithmie) de ce projet.

{% attention %}
Pour le code python, il faudra impérativement :

- faire les tests unitaires de chaque fonction. Ils devront tous se lancer via la commande `python -m pytest`
- organiser votre code en autant de fichiers que nécessaire.
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

{% faire %}
Que fait la fonction mystère écrite ci-dessous :

```python
def mystère(s):
   return s == s[::-1]
```

{% endfaire %}

## Phrases palindromes

### Prétraitement

Pour traiter des phrases palindromes à partir d'un texte en français, il faut commencer par pré-traiter le texte pour qu'il ne contienne plus que des lettres non accentuées en majuscules.

{% faire %}

Créez une fonction `prétraitement(s: str) -> str` qui effectue le prétraitement d'une chaîne de caractères. Pour cela vous pourrez utiliser, dans l'ordre :

1. le module [`unidecode`{.language-}](https://pypi.org/project/Unidecode/) (qu'il vous faudra installer avec `pip`) qui permet de supprimer les accents des caractères
2. [la méthode `upper`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.upper) des chaînes de caractères qui majuscule les lettres
3. l'instruction `re.sub("[^A-Za-z]","",s)`{'.language-} (`sub`{.language-} est une fonction [du module `re`](https://docs.python.org/fr/3/library/re.html) de python) qui rend une chaîne ne possédant que les caractères alphabétiques de `s`{.language-}.
{% endfaire %}
{% info %}
[le module `re`](https://docs.python.org/fr/3/library/re.html) de python permet de filtrer une chaîne de caractères selon [une expression régulière](https://fr.wikipedia.org/wiki/Expression_régulière). Ceci dépasse le cadre de ce cours d'algorithmie mais en deux mots `re.sub("[^A-Z]","",s)`{'.language-} va rendre une nouvelle chaîne de caractères en :

   1. regardant caractère par caractère le troisième paramètre (ici `s`{.language-}).
   2. elle ne conservera que les éléments décrits par le premier paramètre (ici `"[^A-Z]"`{.language-} qui signifie toutes les lettres en majuscules)
   3. les autres caractères sont remplacés par le second paramètre (ici `""`{.language-}, la chaîne vide)

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

### Algorithme

{% faire %}

1. Implémentez l'algorithme le plus efficace que vous êtes arrivé à produire dans la partie algorithmie pour résoudre le problème du sous-palindrome.
2. Utilisez la question précédente pour créer une fonction `sous_palindrome(s: str) -> (int, int)`{.language-} qui rend l'indice de début et la longueur d'un plus grand sous-palindrome de `s`{.language-}

{% endfaire %}

### Programme principal

{% faire %}
Créez un programme principal nommé `main-sous-palindrome.py`{.fichier} qui demande à l'utilisateur de donner une chaîne de caractères et le programme : écrit la phrase entrée en écrivant en rouge le plus grand sous-palindrome.
{% endfaire %}
{% info %}
Pour changer de couleur dans un affichage à l'écran, il vous faudra utiliser un module que vous devrez installer. Vous pourrez utiliser [le module `pytermgui`{.language-}](https://pypi.org/project/PyTermGUI/) par exemple qui permet de faire plein de choses.

En lisant [la documentation de son sous-module tim](https://ptg.bczsalba.com/tim/) vous devriez comprendre comment faire pour colorer un affichage de plein de façons différentes.
{% endinfo %}

### Fichier texte

{% faire %}
Créez un programme principal nommé `main-sous-palindrome-fichier.py`{.fichier} qui demande à l'utilisateur le nom d'un fichier texte se trouvant dans le dossier courant. Le programme :

1. lit le fichier texte
2. transforme le texte en une chaîne utilisable par l'algorithme sous-palindrome en utilisant la fonction `prétraitement`{-language-}
3. trouve l'indice et la longueur d'un plus grand sous-palindrome
4. représente à l'écran le sous-palindrome retenu (écrit en rouge) entouré des 100 caractères le précédant et le succédant (écrits de façon normale).
{% endfaire %}

Vous pourrez utiliser comme textes des grands classiques de la littérature française prises sur le site <https://www.gutenberg.org/>. Choisissez toujours la version texte brute (*plain text*) en utf-8.

{% info %}
Pour les fleurs du mal de Baudelaire c'est là : <https://www.gutenberg.org/ebooks/6099>
{% endinfo %}

### Amélioration

Trouver des sous-phrases palindromes d'un texte peut être rigolo, mais sans caractères de ponctuation, il peut être difficile de s'y retrouver.

{% faire %}
Créez une fonction `correspondance(s12: str, s123:str) -> [int]`{.language-} qui prend deux paramètres :

- une chaîne `s12`{.language-} dont les lettres sont sans accents et en majuscules (résultat des étapes 1 et 2 du prétraitement pour une chaîne `s`{.language-})
- la chaîne `s123`{.language-} correspondant au prétraitement complet de `s12`{.language-} (`s12`{.language-} auquel on a fait l'étape 3 du prétraitement)

Cette fonction rend un tableau $t$ de correspondance où $t[i]$ correspond à l'indice dans `s12`{.language-} de l'indice `i`{.language-} dans `s123`{.language-}.
{% endfaire %}
{% info %}
On pourra remarquer que :

1. $t[0]$ correspond au plus petit indice $i$ tel que `s12[i] == s123[0]`{.language-}
2. $t[u]$ correspond au plus petit indice $i > t[u-1]$ tel que `s12[i] == s123[u]`{.language-}

{% endinfo %}

Par exemple, le résultat de `correspondance("OH LA  LA!", "OHLALA")`{.language-} sera le tableau : `[0, 1, 3, 4, 7, 8]`{.language-}

En remarquant qu'entre la chaîne initiale `s`{.language-} et la chaîne `s12`{.language-} seules les lettres ont été modifiées (`"ôh la  là!"`{.language-} et `"OH LA  LA!"`{.language-}) :

{% faire %}
Plutôt que d'afficher à l'écran le sous-palindrome de la chaîne après traitement, utilisez le texte initial en écrivant en rouge la portion de texte qui est le sous-palindrome.
{% endfaire %}

---
layout: layout/post.njk
title: "Fichiers texte"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Comment lire ou écrire des fichiers en python.

<!-- end résumé -->

{% lien %}
[Documentation python](https://docs.python.org/fr/3/tutorial/inputoutput.html#reading-and-writing-files)
{% endlien %}

Nous utiliserons dans cette partie le fichier exemple suivant :

```text
dans le vieil étang,
une grenouille saute,
un ploc dans l'eau.

Basho.
```

{% faire %}
Créez un fichier texte que vous nommerez `haiku.txt`{.fichier} et et copier/collez-y le texte précédent.
{% endfaire %}

La plupart des fichiers que vous créerez en python seront des fichiers textes.

## Objet fichier

En python, on utilise les fichiers _via_ un objet `file`{.language-}. On manipule les fichiers en 3 temps :

1. ouverture : `f = open("haiku.txt", "r", encoding="utf-8")`{.language-}
   Ces objets sont créés par la commande [`open`{.language-}](https://docs.python.org/fr/3/library/functions.html#open) qui ouvre un fichier. Elle a deux paramètres obligatoires :

   - le nom du fichier,
   - la façon dont on veut l'ouvrir :
     - `'r'`{.language-} : en lecture. La tête de lecture est placée au début du fichier
     - `'w'`{.language-} : en écriture. La tête d'écriture est placée au début du fichier. Donc **si le fichier contenait déjà des choses elles sont supprimées**
     - `'a'`{.language-} : en écriture à la fin du fichier. La tête d'écriture est placée à la fin du fichier. Donc si le fichier contenait déjà des choses elles ne sont **pas** supprimées

   L'objet renvoyé par `open` est une instance de la classe `file`.

   Par défaut, les fichiers sont considérés comme étant du texte écrit en [utf-8](/cours/algorithmie/structure-chaine-de-caractères/encodage/#utf8){.interne}. Si vous voulez ouvrir/écrire un fichier binaire, il faut ajouter `'b'`{.language-} au paramètre. Par exemple : `f = open("mon_image.jpg", "br")`{.language-} ouvre un fichier binaire en lecture.

2. On manipule ensuite le fichier grâce aux méthodes de la classe `file` :

   - en lecture avec les méthodes :
     - `read`{.language-} : `texte = f.read()`{.language-} qui lit tout le fichier sous la forme d'une chaîne de caractères
     - `readline`{.language-} qui lit la ligne suivante d'un fichier
   - en écriture avec `write`{.language-} :

3. enfin, on ferme le fichier : `f.close()`{.language-}

{% attention %}
Si vous ouvrez un fichier en écriture alors qu'il existait déjà, son contenu **disparaît immédiatement et pour toujours**. Il n'y a aucun moyen de récupérer son contenu.
{% endattention %}

## Lire un fichier

Pour lire un fichier, il faut commencer par l'ouvrir avec la commande `open`{.language} :

```python
f = open("haiku.txt", "r", encoding="utf-8")
```

Le résultat de cette instruction est la création d'un objet de type fichier de nom `f`{.language-}.

{% attention %}

Par défaut, python va lire le fichier au format de lecture `utf-8`, donc la commande suivante devrait suffire :

```python
f = open("haiku.txt", "r")
```

Mais certains ordinateurs sous windows nécessite de placer l'encodage explicitement, ce que nous ferons dans la suite.
{% endattention %}

### En entier

{% faire %}
Exécutez le code suivant pour lire le fichier qui doit être dans le même dossier que votre fichier python :
{% endfaire %}

```python
f = open("haiku.txt", "r", encoding="utf-8")  # ouverture d'un fichier texte en lecture  dans le même dossier que le fichier python
poème = f.read()
f.close()
print(poème)
```

Ne confondez pas le nom du fichier et son contenu. Le nom du fichier, ici `haiku.txt`{.fichier}, nous permet de l'ouvrir en lecture grâce à la commande `open`{.language-}. Son contenu est ensuite mis dans la variable `poème`{.language-} grâce à la méthode `read`{.language-}.

### Ligne à ligne

{% faire %}
Exécutez le code suivant pour lire le fichier ligne à ligne.
{% endfaire %}

```python
f = open("haiku.txt", "r", encoding="utf-8")
for ligne in f:  # boucle sur les lignes
    print(ligne)
f.close()
```

Notez la ligne vide entre deux affichages. Ceci est du au fait que chaque ligne du fichier contient déjà un retour à la ligne, auquel en est ajouté un automatiquement à la fin de l'instruction `print`.

Pour éviter cela, souvent on va stocker les lignes **sans** le retour à la ligne. Une façon simple de faire ceci est d'utiliser la méthode [`strip`{.language-} des chaines de caractères](https://docs.python.org/fr/3/library/stdtypes.html#str.strip) :

```python
f = open("haiku.txt", "r", encoding="utf-8")
for ligne in f:  # boucle sur les lignes
    print(ligne.strip())
f.close()
```

Le mieux étant encore de stocker directement le fichier dans une liste de lignes :

```python
f = open("haiku.txt", "r", encoding="utf-8")
lignes = []
for ligne in f:  # boucle sur les lignes
    lignes.append(ligne.strip())
f.close()

for ligne in lignes:
    print(ligne)
```

## Ajout de texte à un fichier

{% faire %}
Exécutez le code suivant pour ajouter quelque chose à la fin d'un fichier.
{% endfaire %}

```python
f = open("haiku.txt", "a", encoding="utf-8")
f.write("\n")
f.write("1644-1694")
f.close()
```

On ajoute un retour à la ligne, puis les dates de naissance et de mort de Basho.

Notez qu'aller à la ligne est un caractère comme un autre (il s'écrit `\n` et vaut U+0010). Il fait partie des [caractères de contrôles](https://fr.wikipedia.org/wiki/Caract%C3%A8re_de_contr%C3%B4le) comme la tabulation ou le bip (essayez par exemple `print(chr(0x7))`{.language-}).

{% attention %}
Lorsque vous écrivez des fichier, il faut s'assurer que le format d'écriture est en utf8, ceci se fait en ajoutant le paramètre `encoding="utf-8"`{.language-} à `open`{.language-}.
{% endattention %}

## Écriture d'un fichier

{% faire %}
Exécutez le code suivant pour remplacer le contenu du fichier.
{% endfaire %}

```python
f = open("haiku.txt", "w", encoding="utf-8")
f.write("Noël est aux portes\n")
f.write("les dindes et les pintades\n")
f.write("rentrent dans les fours")
f.write("\n")
f.write("Salim Bellen")
f.close()
```

{% attention %}
Une fois ouvert le fichier en écriture tout son contenu précédent est perdu.
{% endattention %}

## Utilisation de `with`{.language-}

Vous verrez parfois l'utilisation du mot clé python `with`{.language-} qui permet d'écrire :

```python
with open("haiku.txt", "a", encoding="utf-8") as f:
    f.write("\n")
    f.write("1644-1694")
```

- au début du bloc `with`{.language-} le résultat de l'ouverture du fichier est appelé `f`{.language-}
- A la fin du bloc `with`{.language-} on ferme `f`{.language-}
- s'il y a des erreurs, c'est également le bloc `with`{.language-} qui s'en occupe pour nous.

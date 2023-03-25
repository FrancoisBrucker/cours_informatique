---
layout: layout/post.njk 
title: "Projet : fichiers"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "../fichiers/"
---

<!-- début résumé -->

Utilisation des fichiers en python.

<!-- end résumé -->

Mise en place de votre projet :

{% faire %}

1. créez un dossier nommé `fichiers-donnees`{.fichier} où vous placerez vos fichiers
2. créez un projet vscode dans ce dossier

{% endfaire %}

## Jouons sur les mots

Utilisez python pour :

{% faire %}

1. télécharger le fichier présent à cette adresse : <https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words>
2. sauvegardez le dans un fichier nommé `words.txt`{.fichier}  dans le dossier de votre projet (`fichiers-donnees`{.fichier}).

{% endfaire %}

Le fichier contient une liste de mots, un mot par ligne.

{% faire %}

1. Combien de mots contient ce fichier ?
2. Quel est le 42ème mot du dictionnaire ?
3. Combien de mots finissent par 'g' ?

{% endfaire %}

Pour ne pas prendre en compte le caractère à la ligne, vous pourrez utiliser la méthode [strip](https://docs.python.org/fr/3/library/stdtypes.html#str.strip) des chaînes de caractères.

Enfin :

{% faire %}

1. Combien de mots du fichier contiennent la chaîne de caractères `prout` ? (`"b" in "abc"` rendra `True` en python)
2. Quels sont ces mots ?

{% endfaire %}

## Le compte de Monte-Cristo

Utilisez python pour :

{% faire %}

1. Télécharger le comte de Monte-Cristo avec python (<http://www.gutenberg.org/cache/epub/17989/pg17989.txt>),
2. Sauvegardez le dans un fichier sur votre ordinateur (toujours en utilisant python)

{% endfaire %}

Avec ce fichier :

{% faire %}

1. Comptez le nombre de caractères différents utilisés (vous pourrez mettre chaque caractère dans un [ensemble](https://docs.python.org/fr/3/tutorial/datastructures.html#sets)), et affichez les.
2. Remplacez tous les caractères qui ne sont pas des lettres (c'est à dire qui ne sont pas dans : `"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÇÉÊÎÔàâçèéêëîïôùû"`{.language-}) par des espaces (vous pourrez utiliser la méthode [replace](https://docs.python.org/fr/3/library/stdtypes.html#str.replace))
3. En déduire le nombre de mots utilisés (vous pourrez utiliser la méthode [split](https://docs.python.org/fr/3/library/stdtypes.html#str.split))
4. En déduire le nombre de mots **différents** utilisés (vous pourrez utiliser la méthode [split](https://docs.python.org/fr/3/library/stdtypes.html#str.split))

{% endfaire %}

Comptons en utilisant ce que l'on a fait précédemment :

{% faire %}

1. Combien de fois chaque mot est-il utilisé dans le texte (utilisez un dictionnaire où les mots seront les clés et la valeur le nombre de fois ou ce mot est vue)?
2. Est-il question de `Marseille` dans le texte ? Et si oui, combien de fois ?
3. Quelle est le mot qui revient le plus souvent ?
4. Quels sont les mots qui reviennent au moins $\frac{n}{2}$ fois où $n$ est le nombre de fois où apparaît le mot le plus fréquent.

{% endfaire %}

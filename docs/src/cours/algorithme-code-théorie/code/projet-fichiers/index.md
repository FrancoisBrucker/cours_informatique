---
layout: layout/post.njk 
title: "Projet : fichiers"

eleventyNavigation:
    order: 14
    prerequis:
        - "../fichiers/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
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

On vous demande d'utiliser python pour [télécharger directement un fichier](../fichiers/#fichiers-distants) puis de le traiter

### En Français

[Ce repo github](https://github.com/hbenbel/French-Dictionary/tree/master/dictionary) contient plusieurs fichiers csv contenant des mots français.

{% exercice %}

1. récupérez directement le fichier `dictionary.csv`{.fichier} à l'adresse : <https://raw.githubusercontent.com/hbenbel/French-Dictionary/master/dictionary/dictionary.csv>
2. sauvez le dans le dossier de votre projet (`fichiers-donnees`{.fichier}) sous le nom `mots.txt`{.fichier}
{% endexercice %}

Le fichier contient une liste de mots, un mot par ligne.

{% faire %}

1. Combien de mots contient ce fichier ?
2. Quel est le 42ème mot du dictionnaire ?
3. Combien de mots finissent par `g` ?
4. Combien de mots contiennent un `ç`

{% endfaire %}

Pour ne pas prendre en compte le caractère à la ligne, vous pourrez utiliser la méthode [strip](https://docs.python.org/fr/3/library/stdtypes.html#str.strip) des chaînes de caractères.

Enfin :

{% faire %}

Répondez à cette question existentielle : `nycthémères` est-il un mot français ?

{% endfaire %}

## Le compte de Monte-Cristo

Utilisez python pour :

{% faire %}

1. Télécharger [le comte de Monte-Cristo](http://www.gutenberg.org/cache/epub/17989/pg17989.txt) **directement** avec python
2. Sauvegardez le dans un fichier sur votre ordinateur (toujours en utilisant python)

{% endfaire %}

Avec ce fichier :

{% faire %}

1. Comptez le nombre de caractères différents utilisés (vous pourrez mettre chaque caractère dans un [ensemble](https://docs.python.org/fr/3/tutorial/datastructures.html#sets)), et affichez les.
2. Remplacez tous les caractères qui ne sont pas des lettres (c'est à dire qui ne sont pas dans : `"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÇÉÊÎÔàâçèéêëîïôùû"`{.language-}) par des espaces (vous pourrez utiliser la méthode [replace](https://docs.python.org/fr/3/library/stdtypes.html#str.replace))
3. En déduire le nombre de mots utilisés dans le texte (vous pourrez utiliser la méthode [split](https://docs.python.org/fr/3/library/stdtypes.html#str.split))
4. En déduire le nombre de mots **différents** utilisés dans le texte (vous pourrez utiliser la méthode [split](https://docs.python.org/fr/3/library/stdtypes.html#str.split))

{% endfaire %}

Comptons en utilisant ce que l'on a fait précédemment :

{% faire %}

1. Combien de fois chaque mot est-il utilisé dans le texte (utilisez un dictionnaire où les mots seront les clés et la valeur le nombre de fois ou ce mot est vue)?
2. Est-il question de `Marseille` dans le texte ? Et si oui, combien de fois ?
3. Quelle est le mot qui revient le plus souvent ?
4. Quels sont les mots qui reviennent au moins $\frac{n}{2}$ fois où $n$ est le nombre de fois où apparaît le mot le plus fréquent.

{% endfaire %}

Suites de mots :

{% faire %}

1. Créez un dictionnaire dont les clés snt les nots du texte et les valeurs une liste de tous les mots apparaissant juste après dans le texte.
2. En moyenne, combien de mots différents suivent u mot donné ?
3. En moyenne, combien de mots différents précèdent un mot donné ?
4. Créez des phrases aléatoires de 10 mots, où chaque paire de mot successive apparaît dans le texte.

{% endfaire %}

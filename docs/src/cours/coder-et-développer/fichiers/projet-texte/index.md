---
layout: layout/post.njk
title: "Projet : fichiers"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Mise en place de votre projet :

{% faire %}

1. créez un dossier nommé `fichiers-donnees`{.fichier} où vous placerez vos fichiers
2. créez un projet vscode dans ce dossier

{% endfaire %}

Dans tout ce projet on vous demande de coder le moins d'algorithmes possibles et d'utiliser au maximum les méthodes de listes de python :

{% lien %}
[Méthodes de chaînes de caractères](https://docs.python.org/fr/3/library/stdtypes.html#string-methods)
{% endlien %}

De plus, lorsque l'on utilise des fichiers, il faut lire les fichiers une seule fois en stockant le contenu utile dans une ou plusieurs variables puis ne plus utiliser le fichier car l'accès à un fichier sur le disque dur est beaucoup plus long que l'accès à des variables en mémoire.

## Jouons sur les mots

[Ce repo github](https://github.com/hbenbel/French-Dictionary/tree/master/dictionary) contient plusieurs fichiers csv contenant des mots français.

{% exercice %}

1. récupérez directement le fichier `dictionary.csv`{.fichier} à l'adresse : <https://raw.githubusercontent.com/hbenbel/French-Dictionary/master/dictionary/dictionary.csv> (cliquez droit sur le lien puis téléchargez le sur votre ordinateur)
2. sauvez le dans le dossier de votre projet (`fichiers-donnees`{.fichier}) sous le nom `mots.txt`{.fichier}
   {% endexercice %}

Le fichier contient une liste de mots, un mot par ligne.

### Lecture du fichier en une seule fois

{% faire %}

1. Récupérez tout le fichier dans une chaîne de caractères que vous appellerez `texte`{.language-}.
2. afficher la chaîne de caractères à l'écran.
3. Combien de caractères `"\n"`{.language-} possède ce fichier ?

{% endfaire %}
{% info %}
Les caractères `"\n"`{.language-} sont des [retour à la ligne](https://www.dynamic-mess.com/php/signification-retours/) et permettre de délimiter les lignes d'un fichier texte.

{% endinfo %}

### Lecture du fichier ligne à ligne

Notre fichier contient une donnée (un mot) par ligne. Il peut donc être utile de stocker chaque mot dans un tableau :

{% faire %}

1. En utilisant la lecture ligne à ligne d'un fichier. Construisez une liste `mots`{.language-} dont chaque élément est une ligne du fichier.
2. Affichez la 42ième ligne du texte (l'indice 41 de la liste).

{% endfaire %}

Vous avez du remarquer que l'affichage de la ligne 42 va 2 fois à la ligne. Ceci s'explique par le fait que :

1. la commande `print`{.language-} termine son affichage par un retour à la ligne
2. le mot lui même est une ligne du fichier et contient donc également le caractère `"\n"`{.language-}

Lorsque les données sont contenues dans chaque ligne d'un fichier texte, on a coutume de _nettoyer les données_, c'est à dire de supprimer les caractères de fin de ligne de la donnée ainsi que les caractères espaces `" "`{.language-} de début et de fin de ligne. Par exemple si la ligne contient `"   coucou  \n"`{.language-} on aura envie de ne conserver que la chaîne `"coucou"`{.language-}, c'est à dire la ligne sans le caractère de retour à la ligne (`"\n"`{.language-}) et sans les espaces au début et à la fin.

Pour faire cela automatiquement, python met à votre disposition [la méthode strip](https://docs.python.org/fr/3/library/stdtypes.html#str.strip) des chaînes de caractères. Donc :

{% faire %}
Modifier votre liste `mots`{.language-} pour que chaque élément contienne la version _stripée_ de la ligne.

{% endfaire %}
{% details "corrigé" %}

```python
mots = []
f = open("mots.txt", "r", encoding="utf-8")

for l in f:
    mots.append(l.strip())
f.close()
```

{% enddetails %}

Avec cette nouvelle liste il vous sera plus facile de répondre aux questions suivantes :

{% faire %}

1. Combien de mots contient ce fichier ?
2. Quel est le 42ème mot du dictionnaire ?
3. Combien de mots finissent par `g` ?
4. Combien de mots contiennent un `ç`

{% endfaire %}

Enfin :

{% faire %}

Répondez à cette question existentielle : `nycthémères` est-il un mot français ? Et si oui, quel est son numéro de ligne ? Et quel est la signification de ce mot ?

{% endfaire %}

## Le compte de Monte-Cristo

Utilisez python pour :

{% faire %}

Téléchargez [le comte de Monte-Cristo](http://www.gutenberg.org/cache/epub/17989/pg17989.txt) et sauvez le sur votre disque dur.

{% endfaire %}
{% attention %}
Les accès réseau sont toujours coûteux en temps, on a donc coutume de ne télécharger le fichier qu'une fois puis d'utiliser une copie locale pour tous les traitements.
{% endattention %}

Lisons ce fichier avec python. On veut le lire en une seule fois car c'est le texte en entier qui est important et pas une ligne particulière :

{% faire %}
Récupérez tout le fichier dans une chaîne de caractères que vous appellerez `monte_cristo`{.language-}.

{% endfaire %}

Avec cette chaîne de caractères :

{% faire %}

1. Comptez le nombre de caractères différents utilisés (vous pourrez mettre chaque caractère dans un [ensemble](https://docs.python.org/fr/3/tutorial/datastructures.html#sets)), et affichez-les.
2. Remplacez tous les caractères qui ne sont pas des lettres (c'est à dire qui ne sont pas dans : `"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÇÉÊÎÔàâçèéêëîïôùû"`{.language-}) par des espaces (vous pourrez utiliser la méthode [replace](https://docs.python.org/fr/3/library/stdtypes.html#str.replace))
3. En déduire le nombre de mots utilisés dans le texte
4. En déduire le nombre de mots **différents** utilisés dans le texte

{% endfaire %}
{% info %}

- Vous pourrez utiliser la méthode [split](https://docs.python.org/fr/3/library/stdtypes.html#str.split) des chaînes de caractères pour découper le texte. Il ne faudra **pas** donner explicitement de séparateur. Pourquoi ?
- Si vous voulez des mots différents, les ensembles sont fait pour ça.

{% endinfo %}
{% details "Nombres à trouver", "open" %}

- nombre de caractères : 105
- nombre de mots : 134712
- nombre de mots différents : 12244

{% enddetails %}

Comptons en utilisant ce que l'on a fait précédemment :

{% faire %}

1. Combien de fois chaque mot est-il utilisé dans le texte (utilisez un dictionnaire où les mots seront les clés et la valeur le nombre de fois ou ce mot est vue)?
2. Est-il question de `Marseille` dans le texte ? Et si oui, combien de fois ?
3. Quelle est le mot qui revient le plus souvent ?
4. Quels sont les mots qui reviennent au moins $\frac{n}{2}$ fois où $n$ est le nombre de fois où apparaît le mot le plus fréquent.
5. Quel est le mot le plus fréquent pour chaque longueur de mots ?

{% endfaire %}
{% details "Nombres à trouver", "open" %}

- Nombre de "Marseille" : 84
- Mot le plus fréquent :
  - (4790, 'de')
  - (2946, 'le')
  - (2940, 'et')
  - (2855, 'la')
  - (2731, 'à')
  - (2555, 'il')
- Mots de longueur différentes :
  - (4790, 'de')
  - (2731, 'à')
  - (1923, 'que')
  - (1543, 'vous')
  - (872, 'était')
  - (777, 'Dantès')
  - (291, 'monsieur')
  - (258, 'Villefort')
  - (219, 'Caderousse')
  - (161, 'Fernand')
  - (26, 'prisonniers')
  - (22, 'bonapartiste')
  - (20, 'contrebandiers')
  - (11, 'véritablement')
  - (10, 'malheureusement')
  - (3, 'particulièrement')
  - (1, 'révolutionnairement')
  - (1, 'imperceptiblement')

{% enddetails %}

Suites de mots :

{% faire %}

1. Créez un dictionnaire dont les clés sont les mots du texte et les valeurs une liste de tous les mots qui apparaissant juste après dans le texte.
2. En moyenne, combien de mots différents suivent un mot donné ?
3. En moyenne, combien de mots différents précèdent un mot donné ?
4. Créez des phrases aléatoires de 10 mots, où chaque paire de mot successive apparaît dans le texte.

{% endfaire %}

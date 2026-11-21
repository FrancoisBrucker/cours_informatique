---
layout: layout/post.njk
title: "Formats de données : csv"

eleventyNavigation:
  order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Les fichiers [csv](https://fr.wikipedia.org/wiki/Comma-separated_values) sont des fichiers textes permettant de stocker des données structurées comme une feuille excel.

<!-- fin résumé -->

Le format csv est utilisé pour stocker des données sous la forme d'une table. Par exemple :

```text
Prénom, nom, note
Harry, Cover, 12.5
Alain, Bessil, 7
Elvire, Sacuti, 15
Aimée, Nêms, 20
Gordon, Zola, 10
```

{% note %}
Un fichier csv :

- est un fichier texte
- chaque ligne du fichier est composée d'une **_donnée_**
- chaque donnée est composée de **_champs_** séparés par un **_délimiteur_**
- chaque donnée à :
  - le même nombre de champs
  - le même délimiteur

{% endnote %}

## Format csv

Le format csv peut sembler bien défini, mais il n'en est rien.

{% attention %}
Il est crucial de toujours soigneusement vérifier le format csv de vos données.
{% endattention %}

Par exemple :

- Le délimiteur est par défaut une `,`{.language-}, mais peut tout aussi bien être un `;` (par défaut lorsque l'on exporte un fichier au format csv depuis un excel en langue française), une tabulations, voir un espace.
- Pour pouvoir distinguer les chaines de caractères des nombres, par défaut une chaîne de caractères sera entourée de `"`. Mais ce n'est pas toujours le cas
- la [fin de ligne](https://fr.wikipedia.org/wiki/Retour_chariot#Informatique), qui est un caractère spécial est interprété différents sous unix (`\n`), sous windows (deux caractères `\r\n`) et sous les vieux systèmes mac avant Macos, donc vous n'en croiserez plus souvent (caractère `\r`).

Enfin :

- la première ligne est souvent spéciale car contenant le nom des différents attributs (colonnes)
- la première colonne peut contenir l'identifiant de la donnée

En python, tout ceci est bien sur paramétrable.

{% note %}
Utilisez un plugin vscode pour pouvoir visualiser clairement les fichiers csv.

Il en existe de nombreux. J'ai installé le tout simple [rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) pour rapidement connaître le format csv d'un fichier particulier.
{% endnote %}

## Python et fichier csv

{% lien %}
[Documentation csv python](https://docs.python.org/fr/3/library/csv.html)
{% endlien %}

Pour la suite, on supposera que l'on ait dans le dossier du projet courant le fichier `notes.csv`{.fichier} contenant :

```text
Prénom, nom, note
Harry, Cover, 12.5
Alain, Bessil, 7
Elvire, Sacuti, 15
Aimée, Nêms, 20
Gordon, Zola, 10
```

### Lecture d'un fichier

le code ci-après lit le fichier csv et le place dans une liste de listes si la ligne contient bien 3 champs. Puis on convertit le dernier élément en entier.

```python
import csv

donnees = []

f = open("notes.csv", newline='')
lecteur = csv.reader(f)
for ligne in lecteur:
    donnees.append(ligne)
```

{% attention %}
Par défaut, tout attribut sera considéré comme une chaîne de caractères. Il faut convertir chaque champ à son bon type. Si vous voulez traiter à part les chaînes de caractères, il faut les entourer de `"`.
{% endattention %}

1. `import csv`{.language-} pour pouvoir utiliser le module `csv`{.language-}
2. ouvrir le fichier à lire avec [`open`{.language-}](https://docs.python.org/fr/3/library/functions.html#open) avec une gestion de la fin de ligne.
3. placer ce fichier dans un `reader`{.language-} dont le but est de lire le fichier et de le structurer en utilisant ses paramètres.
4. lire le fichier ligne à ligne. A chaque utilisation vous obtiendrez une liste contenant les différents champs de la ligne lue.

Le _reader_ python permet de lire une chaîne de caractères et de l'interpréter selon le format csv. Il possède de [nombreuses options](https://docs.python.org/fr/3/library/csv.html#csv-fmt-params) permettant de gérer les multiples cas particuliers. Parmi les plus usités :

- `delimiter`{.language-}. Par défaut c'est des `','`, mais on verra souvent en France des csv dont le délimiteur est un `';'` (car les virgules sont déjà utilisés pour les nombres réels)
- `quotechar`{.language-} : pour savoir ce qui est une chaîne de caractères, souvent des `"`{.language-}.

### Séparer les noms de colonne des données

Pour lire une unique ligne, on peut utiliser la commande `next`{.language-}. Le code suivant lit la première ligne, qui contient les noms des différentes colonnes, puis lit les autres données en transformant le dernier champ (la note) en `float`{.language-}.

```python
import csv


donnees = []

f = open("notes.csv")
lecteur = csv.reader(f)
titres = next(lecteur)  # lit une unique ligne
for ligne in lecteur:    # continue la lecture
    ligne[2] = float(ligne[2])  # convertit la note en flottant
    donnees.append(ligne)
```

{% info %}
Le lecteur de csv fonctionne avec tout [itérateur](https://docs.python.org/fr/3.7/glossary.html#term-iterator). Il fonctionne donc aussi en remplaçant le fichier `f`{.language-} par une liste de chaînes de caractères par exemple.
{% endinfo %}

### Écrire des fichiers csv

Ajoutons la note de Mlle Debbie Scott qui a eu 13.5

{% attention %}
Il faut ouvrir le fichier en **ajout**. Si vous l'ouvrez juste en écriture tout votre fichier disparaît.
{% endattention %}

```python
import csv
with open('notes.csv', 'a', newline='') as f:
    écrivain = csv.writer(f)
    écrivain.writerow(['Debbie', 'Scott', 13.5])
```

## Exercices

### Codes postaux

{% faire %}
Téléchargez la base officielle des codes postaux au format csv à partir de [cette page](https://www.data.gouv.fr/fr/datasets/base-officielle-des-codes-postaux).
{%endfaire %}

En utilisant ce fichier csv :

{% faire %}

1. Quel est le format de ce fichier ?
2. Ouvrez ce fichier et déterminez :
   - A quel code postal est associé la charmante bourgade d'OTTERSWILLER ?
   - Combien de fois apparaît la ville de Marseille dans le fichier ? Et pourquoi ?

{% endfaire %}

### Prénoms

{% faire %}
En utilisant [cette page](https://www.insee.fr/fr/statistiques/7633685), récupérez le fichier des naissances en France (hors Mayotte) depuis 1900.
{% endfaire %}

En utilisant ce fichier :

{% faire %}

1. Quel le prénom le plus donné chez les garçons et chez les filles l'année de votre naissance ? Et en 2022 ?
2. Représentez graphiquement l'évolution au cours du temps (de l'année 1900 à 2022) de votre prénom (ou d'un prénom que vous aimez bien)

{% endfaire %}

Utilisez-maintenant le fichier des prénoms ventilés par département :

{% faire %}
Créez un dictionnaire dont les clés sont le numéro de département et la valeur, le nombre de fois où votre prénom a été donné dans ce département pour toutes les années.

Dans quel département votre prénom a-t-il été le plus donné ?
{% endfaire %}

---
layout: layout/post.njk

title: Exercices de scripting

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Quelques exercices de base de scripting shell.

## Téléchargements de fichiers

Le [projet Gutenberg](https://www.gutenberg.org/) contient de nombreux ouvrages libres de droits. Vous allez y récupérer des fichiers avec du scripting shell

### Récupération du fichier

Essayez de faire les différentes question de cette partie en une seule ligne de shell.

#### Url

{% lien %}
[Utiliser curl](https://www.youtube.com/watch?v=APtOavXTv5M&list=PLShDm2AZYnK1SdG3dufPdCqk08sOahUBP&index=9)
{% endlien %}

En utilisant la commande `curl` (au pire installez là), téléchargez [le 1er tome du Comte de Monte-Cristo](https://www.gutenberg.org/ebooks/search/?query=Le+comte+de+Monte-Cristo) au format utf-8 (récupérez son adresse sur le site) et affichez le résultat dans stdout.

#### Sauvegarde

Sauvegardez le contenu de l'url dans un fichier dont vous choisirez le nom en utilisant la redirection de stdout vers un fichier.

### Métrologie

Vous utiliserez le fichier de la question précédente pour faire cette partie. La encore, vous devriez pouvoir répondre à toutes les questions en une seule chaîne de commandes, mais ne vous forcez pas à y arriver si vous ne trouver la pas la solution.

#### Nombres

en Utilisant `wc`, rendez le nombre de lignes, de mots et de caractères de ce fichier.

#### Entête du Roman

1. A quelle ligne commence effectivement le Roman ?
2. . Quelle option de `grep` permet de donner la ligne contenant le pattern à chercher ?
3. Quel pattern utiliseriez vous avec grep pour trouver la fin de l'entête ajoutée par le site Gutenberg (on considère que la table des matière fait partie du roman) ?
4. Utilisez cette option pour trouver le numéro de ligne du début du roman
5. Combinez la recherche précédente avec la commande `cut` pour avoir **uniquement** le numéro de ligne
6. Comptez le nombre de lignes, de mots et de caractères de ce fichier à partir du début du roman

#### Marseille

1. Quelle est la différence entre `grep` et `grep -E` ?
2. En utilisant [la commande `grep -E`](https://www.redhat.com/sysadmin/find-text-files-using-grep), comptez le nombre de fois où l'on parle de Marseille ou de Marseillais dans ce Tome.

### Stockage

On vous demande de créer un script pour répondre aux questions suivantes

#### <span id="tout-le-comte"></span>Tout le comte

1. Créez un script qui crée sort sur stdout le contenu à la suite des 4 tomes du comte de monté Cristo
2. affinez le résultat en ne prenant pas les entêtes des 4 romans

Vous utiliserez une boucle for pour télécharger les 4 tomes à la suite des autres, à partir d'un tableau dans lequel vous aurez au préalable stocké les 4 urls.

#### Le comte est bon

Sauvez avec une redirection le contenu du roman dans un fichier. Utilisez ce fichier pour :

1. Refaire la partie métrologie pour le roman entier.
2. calculez le nombre moyen de mot par ligne (divisez le nombre de mots par rapport au nombre de lignes)

### Script final

Créez un script qui :

1. crée le fichier `comte-monte-cristo.txt`{.fichier} uniquement s'il n'existe pas déjà dans le dossier courant.
2. Si le fichier existe :
   1. le script  prévient l'utilisateur sur stderr
   2. rend un code de sortie de 1
3. si le fichier n'existe pas :
   1. il crée le fichier et y met les 4 tomes du cote de Monte-Cristo (partie ["Tout le comte"](./#tout-le-comte))
   2. affiche sur stderr, le nombre de ligne du fichier
   3. rend un code de sortie de 0

## Poubelle

La commande `rm` ne fait aucune sauvegarde d'un fichier avant de le supprimer. On vous demande de :

1. créer une commande `poubelle` qui prend un unique paramètre. Vous placerez cette commande dans `$HOME/.local/bin` et ferez en sorte que la commande soit accessible en changeant le PATH.
2. cette commande doit prendre un argument. SOn fonctionnement est le suivant :
   1. elle sauve le fichier argument dans le dossier `$POUBELLE`
   2. elle supprime le fichier argument
3. si la variable d'environnement `$POUBELLE` n'existe pas, elle sauve le fichier argument dans le dossier `$HOME/.config/poubelle`
4. si l'argument existe déjà dans `$POUBELLE` (ou dans `$HOME/.config/poubelle` si `$POUBELLE` n'est pas positionné), la commande doit :
   1. prévenir dans stderr que ce fichier est déjà sauvé
   2. si l'option -f n'est pas positionner, s'arrêter avec un code de sortie de 1.
   3. si l'option -f est positionner, elle doit remplacer le fichier par le nouveau et rendre un code de sortie de 0
5. si la commande est langée avec l'option `-r` et avec un argument : elle doit
   1. récupérer le fichier sauvé dans `$POUBELLE` (ou dans `$HOME/.config/poubelle` si `$POUBELLE` n'est pas positionné) s'il existe (sinon on prévient l'utilisateur dans stderr et on sort avec un code de 2)
   2. copier le fichier dans le dossier courant
   3. supprimer de `$POUBELLE` (ou dans `$HOME/.config/poubelle` si poubelle n'est pas positionné)
6. si la commande est lancée avec la commande `-l` et sans argument, elle doit lister les fichiers sauvés (ceux de `$POUBELLE` ou de `$HOME/.config/poubelle` si `$POUBELLE` n'est pas positionné)
7. la commande doit avoir une option `-h` (et `--help`) permettant de rendre son aide.
8. si la commande est lancée sans arguments, avec des arguments incompatibles ou incomplet, la commande doit s'arrêter avec un code de 3 et afficher l'aide de la commande.

{% lien %}

Vous pourrez lire [ce tuto](https://stackabuse.com/how-to-parse-command-line-arguments-in-bash/) pour gérer au mieux les options.

{% endlien %}

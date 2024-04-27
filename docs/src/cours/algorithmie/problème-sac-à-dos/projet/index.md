---
layout: layout/post.njk
title: Projet

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Séance de code pour tester le problème du sac à dos en condition (presque) réelle.


{% faire %}
Créez un projet vscode pour mettre toutes vos programmes.
{% endfaire %}

## Données

{% faire %}
Créez un fichier `données.py`{.fichier} où vous stockerez tout ce qui est relatif aux données.
{% endfaire %}
{% faire %}
Reprenez l'exemple du cours et placez la constante suivante dans le fichier `données.py`{.fichier}.

{% endfaire %}

Nous aurons besoin plus tard de connaitre le prix total d'une poudre, donc créons une fonction pour le calculer :

## Algorithmes gloutons

### Sac à dos fractionnel

{% faire %}
Créez un fichier `fractionnel.py`{.fichier} où vous écrirez le code de l'algorithme glouton trouvant le sac à dos fractionnel optimal.

Vous testerez votre code avec 2 produits.
{% endfaire %}


Une fois que vous êtes assuré du bon fonctionnement de votre algorithme :


{% faire %}
Exécutez l'algorithme glouton fractionnel avec l'`EXEMPLE`{.language-} du fichier `données.py`{.fichier}.
{% endfaire %}

Pour vérifier que le profit est bien celui attendu, créons une fonction :

{% faire %}
Ajoutez au fichier `fractionnel.py`{.fichier} une fonction `profit(sac_à_dos, produits)`{.language-} qui rend le profit réalisé pour le sac à dos en entrée.

Vous testerez votre code avec un sac à dos fictif puis, une fois le code testé vous l'utiliserez pour vérifier que l'`EXEMPLE`{.language-} du fichier `données.py`{.fichier} donne un résultat correct.

{% endfaire %}

### Sac à dos glouton

> TBD

## Expérimentation aléatoire

> TBD : création de données
> TBD : test sur gloutons.


## Pour conclure

Nous avons utilisé des dictinnaires et des fonctions annexes pour les gérer. On ne fait habituellement pas ça : seules les données brutes sont stockées sous la forme d'un dictionnaire (le plus souvent [un fichier JSON](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation) que l'on peut facilement importer en python) tout le reste est géré par des classes.

{% faire %}
Reprenez votre code et utilisez une classe `Produit`{.language-} permettant de gérer une poudre ou un aliment.
{% endfaire %}

## TBD

> <https://tarakc02.github.io/branch-and-bound/>
<https://informatique.ens-lyon.fr/concours-info/2011/sujet-jour5-2011.pdf>
> TBD : sac à dos multiple
> TBD : super croissant.
> TBD : quand est-ce que l'énumération est mieux que la programmation dynamique. Souvent prog dynamique chouette car pas beaucoup de choix pour K

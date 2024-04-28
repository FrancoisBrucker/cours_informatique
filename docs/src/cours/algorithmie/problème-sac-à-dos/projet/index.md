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
Créez un fichier `données.py`{.fichier} et placez y l'exemple du cours sous la forme d'une constante.
{% endfaire %}

## Algorithmes gloutons

### Sac à dos fractionnel

{% faire %}
Créez un fichier `fractionnel.py`{.fichier} où vous écrirez le code de l'algorithme glouton trouvant le sac à dos fractionnel optimal.

Vous testerez votre code dans le fichier `test_fractionnel.py`{.fichier}
{% endfaire %}


Une fois que vous êtes assuré du bon fonctionnement de votre algorithme :


{% faire %}
Exécutez l'algorithme glouton fractionnel avec l'`EXEMPLE`{.language-} du fichier `données.py`{.fichier}.
{% endfaire %}

Pour vérifier que le profit est bien celui attendu, créons une fonction :

{% faire %}
Ajoutez au fichier `données.py`{.fichier} une fonction `profit(sac_à_dos, produits)`{.language-} qui rend le profit réalisé pour le sac à dos et les produits en entrée.

Vous testerez cette fonction dans le fichier  `test_données.py`{.fichier}.

{% endfaire %}

Enfin :

{% faire %}
Faites en sorte que l'exécution du fichier `fractionnel.py`{.fichier} rende les données, le sac à dos et le profit pour l'exemple. Vous devez avoir quelque chose du genre en sortie :

```text
Données :
{'nom': 'poudre 1', 'kg': 15, 'prix': 135}
{'nom': 'poudre 2', 'kg': 2, 'prix': 30}
{'nom': 'poudre 3', 'kg': 4, 'prix': 32}
{'nom': 'poudre 4', 'kg': 1, 'prix': 6}
{'nom': 'poudre 5', 'kg': 6, 'prix': 18}
{'nom': 'poudre 6', 'kg': 80, 'prix': 800}

Sac à dos fractionnel optimal :
0 poudre 1
1 poudre 2
0 poudre 3
0 poudre 4
0 poudre 5
0.225 poudre 6

Profit : 210.0

```

{% endfaire %}

### Sac à dos glouton

{% faire %}
Créez un fichier `sac_a_dos.py`{.fichier} où vous écrirez le code de l'algorithme glouton trouvant le sac à dos.

Vous testerez votre code dans le fichier `test_sac_a_dos.py`{.fichier}
{% endfaire %}

Pour comparer les résultats par rapport au problème du sac à dos fractionnel :

{% faire %}
Faites en sorte que l'exécution du fichier `sac_a_dos.py`{.fichier} rende les données, le sac à dos et le profit pour l'exemple. Vous devez avoir quelque chose du genre en sortie :

```text
Données :
{'nom': 'poudre 1', 'kg': 15, 'prix': 135}
{'nom': 'poudre 2', 'kg': 2, 'prix': 30}
{'nom': 'poudre 3', 'kg': 4, 'prix': 32}
{'nom': 'poudre 4', 'kg': 1, 'prix': 6}
{'nom': 'poudre 5', 'kg': 6, 'prix': 18}
{'nom': 'poudre 6', 'kg': 80, 'prix': 800}

Sac à dos glouton :
1 poudre 1
1 poudre 2
0 poudre 3
1 poudre 4
0 poudre 5
0 poudre 6

Profit : 171
```

{% endfaire %}

## Énumération exhaustive

### Tous les sac à dos

{% faire %}
Dans le fichier `sac_a_dos.py`{.fichier} créez une fonction `énumèration(produits, masse_totale)` qui énumère tous les sac à dos possibles et rend le sac à dos maximum.

Vous testerez votre code dans le fichier `test_sac_a_dos.py`{.fichier}
{% endfaire %}

On peut maintenant comparer les résultats :

{% faire %}
Dans le fichier `sac_a_dos.py`{.fichier}, vérifiez que l'exemple donne bien le bon résultat.
{% endfaire %}

### Branch and Bound

{% faire %}
Dans un fichier `efficace.py`{.fichier} créez une fonction `branch_and_bound(produits, masse_totale)` qui utilise le _branch and bound_ pour trouver le sac à dos optimal. 

- Vous modifierez les algorithmes gloutons pour
{% endfaire %}

On peut maintenant comparer les résultats :

{% faire %}
Dans le fichier `sac_a_dos.py`{.fichier}, vérifiez que l'exemple donne bien le bon résultat.
{% endfaire %}
### Programmation dynamique

## Expérimentation aléatoire

> TBD : création de données
> TBD : test sur gloutons.
> TBD : temps


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

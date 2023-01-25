---
layout: layout/post.njk

title: "Style et couverture de code"
tags: ['tutoriel', 'python']
authors:
    - François Brucker

eleventyNavigation:
  key: "Style et couverture de code"
  parent: Tutoriels
---

<!-- début résumé -->

Style et couverture de code.

<!-- end résumé -->

## Style et black

Si vous avez pris l'habitude de faire du joli code en utilisant un linter, vous pouvez utiliser [black](https://black.readthedocs.io/en/stable/) pour le faire automatiquement.

{% faire %}
Suivez le [tuto]({{ "/tutoriels/vsc-python-modules-supplémentaires" | url}}#black) pour l'installer.
{% endfaire %}
{% faire %}
Jouez avec [black](https://black.readthedocs.io/en/stable/) sur le code du projet pour voir comment il est facile dre toujours avoir un code parfaitement stylé.

**Utilisez le toujours et souvent dans vos projets !**
{% endfaire %}

## Tests et couverture de code { #couverture-code }

Les tests sont obligatoires. On teste chaque fonction que l'on développe.

{% note %}
Lorsque l'on teste un objets et ses méthodes, on essaie dans la mesure du possible de ne pas avoir besoin des attributs. On ne vérifie que les résultats de la méthode, pas comment l'objet stocke ses informations.

On teste des **fonctionnalités** pas une **implémentation particulière de celles-ci**.
{% endnote %}

Les tests nous permette d'avoir confiance dans la qualité du code. Mais il est parfois compliqué d'être sur que nos tests vérifient bien tous les cas possibles (passent bien par tous les blocs `si/alors/sinon`{.language-} du code par exemple).

Un outil pour vérifier cela est la [couverture de code](https://fr.wikipedia.org/wiki/Couverture_de_code). On exécute les tests et on regarde, fichier par fichier quelles sont les lignes qui ont été vues pour ces tests.

{% faire %}

Installez l'outils de couverture de code en suivant le [tuto]({{ "/tutoriels/vsc-python-modules-supplémentaires" | url }}#code-coverage) vous montre comment l'installer.

{% endfaire %}

Son fonctionnement est le suivant :

1. on exécute les tests dans le terminal en ajoutant l'extension coverage  `python -m pytest --cov=.` (ou `python3` si vous êtes sous Mac ou Linux)
2. le résultat est donné dans le terminal.

En prenant [les 3 fichiers]({{ '/cours/algorithme-code-théorie/code/programmation-objet/composition-agrégation' | url}}#code-final) du cours programmation objet : composition et agrégation, on obtient :

```text
---------- coverage: platform darwin, python 3.9.9-final-0 -----------
Name             Stmts   Miss  Cover
------------------------------------
main.py             10     10     0%
panier.py           13      0   100%
test_panier.py      16      0   100%
------------------------------------
TOTAL               39     10    74%
```

{% faire %}

Vérifiez que vous avez la même chose pour votre projet.

{% endfaire %}

On voit que l'exécution des tests a eu besoin d'utiliser 100% du fichier `test_panier.py`{.fichier} (ce qui est normal) et 100% du fichier `panier.py`{.fichier}. Le fichier `main.py`{.fichier} n'a pas été utilisé du tout (aucune des 10 lignes n'a été vue), ce qui est normal.

{% note %}
Il faut tenter de passer par 100% du code utile dans nos tests.
{% endnote %}

Pour s'en rendre compte, on peut commenter un test et re-exécuter la couverture de code :

{% faire %}

Supprimez  le test `test_supprime_dans_panier`{.language-} et re-exécuter la couverture de code.

{% endfaire %}

Vous devriez obtenir :

```text
---------- coverage: platform darwin, python 3.9.9-final-0 -----------
Name             Stmts   Miss  Cover
------------------------------------
main.py             10     10     0%
panier.py           13      3    77%
test_panier.py      11      0   100%
------------------------------------
TOTAL               34     13    62%
```

3 lignes de `panier.py` n'ont pas été vue. Pour savoir exactement les quelles, la commande `python -m pytest --cov=. --cov-report term-missing` donne :

```text
---------- coverage: platform darwin, python 3.9.9-final-0 -----------
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
main.py             10     10     0%   1-17
panier.py           13      3    77%   15-18
test_panier.py      11      0   100%
----------------------------------------------
TOTAL               34     13    62%
```

C'est bien l'intérieur de la fonction `test_supprime_dans_panier`{.language-}.

{% info %}
Notez que la ligne contenant la définition de la fonction a été vue. En effet, lors de l'import du fichier `panier.py`{.fichier}, le ficher est lu, donc les noms des fonctions sont mises dans l'espace de nom du module.
{% endinfo %}

{% faire %}
Dans vos futurs projets, faites en sorte d'avoir toujours 100% de couverture de code.
{% endfaire %}

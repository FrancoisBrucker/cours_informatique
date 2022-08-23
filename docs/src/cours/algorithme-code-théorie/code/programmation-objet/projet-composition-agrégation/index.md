---
layout: layout/post.njk 
title: "Projet : composition et agrégation"
---

{% chemin %}
[Cours]({{ "../../.." }}) / [Algorithme, code et théorie]({{ "../.." }}) / [Code]({{ "../.." }}) / [Programmation Objet]({{ ".." }}) / [{{title}}]({{ "." }})
{% endchemin %}
{% prerequis "**Prérequis** :" %}

* [Composition et agrégation](../composition-agrégation)

{% endprerequis %}

<!-- début résumé -->

Classes et objets, le code !

<!-- end résumé -->

## Coder des objets

La programmation objet ressemble comme deux gouttes d'eau à la programmation classique d'algorithmes. Les principes y sont juste poussés à l'extrême.

Nous allons montrer ici comment avoir un code qui fonctionne.

### Code du projet

{% faire %}
Commencer par créer un nouveau projet vscode dans un dossier nommé `panier`{.fichier} et recopiez-y les trois fichiers de la [partie composition et agrégation](../composition-agr%égation#code-final).
{% endfaire %}

{% faire %}
Vérifiez que :

* tous les tests passent
* le programme principal fonctionne

{% endfaire %}

### Style et black

Maintenant que vous avez pris l'habitude de faire du joli code en utilisant un linter, vous pouvez utiliser [black](https://black.readthedocs.io/en/stable/) pour le faire automatiquement.

{% faire %}
Suivez le [tuto]({{ "/tutoriels/vsc-python-modules-supplémentaires" | url}}#black) pour l'installer.
{% endfaire %}
{% faire %}
Jouez avec [black](https://black.readthedocs.io/en/stable/) sur le code du projet pour voir comment il est facile dre toujours avoir un code parfaitement stylé.

**Utilisez le toujours et souvent dans vos projets !**
{% endfaire %}

### Tests et couverture de code {#couverture-code}

Les tests sont bien sur toujours obligatoires ! Vous testerez chaque fonction que vous développerez.

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

1. on exécute les tests dans le terminal en ajoutant l'extension coverage  `python -m pytest --cov=.` (ou `python3` si vous êtes sous mac ou linux)
2. le résultat est donné dans le terminal.

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
Dans la suite de ce projet, vous ferez en sorte d'avoir toujours 100% de couverture de code.
{% endfaire %}

## Un Dé

A vous ! Mettez en application tout ce que vous avez vu pour créer une classe `Dice`{.language-}. Elle doit être capable de :

* créer un objet sans paramètre (sa position est alors 1),
* créer un objet avec sa position initiale,
* connaître et donner la valeur du dé (avec les méthodes `get_position`{.language-} et `set_position`{.language-}),
* lancer un dé en utilisant une méthode nommée `roll()`{.language-} (la valeur du dé doit être modifiée aléatoirement).

{% note %}
Les *getter* let les *setter* sont deux méthodes permettant de rendre ou de modifier un attribut d'un objet sans avoir à le manipuler directement.

Cela permet d'abstraire un attribut de son implémentation.
{% endnote %}

Pour justifier de passer par des méthodes plutôt que d'accéder directement aux attributs, je vous conseille de lire ce [fil de stackoverflow](https://stackoverflow.com/questions/1568091/why-use-getters-and-setters-accessors?rq=1), bien que vieux il dit encore tout ce qu'il faut savoir.

{% faire %}
Créez un dossier `des-des`{.fichier} qui sera la racine de votre projet.
{% endfaire %}

### Modèle {#dice-modèle}

{% faire %}

1. Proposez une modélisation UML de la classe `Dice`{.language-}.
2. donnez des exemples de manipulation d'objets de cette classe, comme :
   * créer un objet
   * modifier la valeur de sa position
   * obtenir sa position
   * le lancer

{% endfaire %}

### code python {#dice-python}

{% faire %}
Créez le code python de la classe `Dice`{.language-} (fichier `dice.py`{.language-}).
{% endfaire %}

Pour être sûr que tout fonctionne comme prévu :

{% faire %}
Ajoutez les tests de chaque méthode de la classe `Dice`{.language-} (fichier test_dice`{.fichier}).

Il est impossible de tester le hasard, donc pour la méthode `roll`{.language-} vérifiez juste que la position du dé est cohérente (entre 1 et 6) après l'utilisation de la méthode.

Vérifiez que vous avez bien 100% de couverture de code.
{% endfaire %}

Pour jouer avec notre classe dice :

{% faire %}
Créez un fichier `main_dice.py`{.fichier} qui :

1. demande à l'utilisateur :
   * la position initiale du dé
   * la valeur pour laquelle arrêter les lancers
2. lance le dé jusqu'à tant que la valeur demandée par l’utilisateur soit trouvée.
3. le programme affiche le nombre de lancer nécessaire (cela peut être 0)

{% endfaire %}

## 5 dés

Méthode naïve pour manipuler 5 dés.

{% faire %}
Dans un fichier `main_5_des.py`{.fichier} Créez une liste avec 5 dés. Utilisez une boucle `for`{.language-} pour les lancer tous les 5, puis voir le résultat du lancer des 5 dés.
{% endfaire %}

Pour afficher la position d'un dé, il faut tout d'abord chercher sa position. Améliorons ça :

{% faire %}
Créez une méthode  `__str__`{.language-} pour la classe `Dice`{.language-} qui rende la position du dé (sous la forme d'une chaîne de caractère).

Ajoutez son test et utilisez là (de façon implicite) dans le fichier `main_5_des.py`{.fichier} en affichant directement les dés à l'écran plutôt que leurs positions.
{% endfaire %}

Une autre amélioration :

{% faire %}
Faites en sorte que l'on puisse écrire : `d.roll().roll()`{.language-} si l'on veut lancer deux fois de suite le dé `d`{.language-}.

Cela permettra aussi d'afficher `d`{.language-} directement après l'avoir lancé : `print(d.roll())`{.language-}.
{% endfaire %}

## Tapis vert

Nous allons créer une classe permettant de gérer nos 5 dès de façon plus pratique qu'avec notre liste.

Pour pouvoir jouer à des jeux de dés, implémentons une classe `TapisVert`{.language-}.

### Modèle {#tapis-vert-modèle}

{% faire %}

1. Proposez une modélisation UML de la classe `TapisVert`{.language-}.
2. donnez des exemples de manipulation d'objets de cette classe comme :
   * créer un objet
   * donner un tuple contenant ses 5 dés
   * lancer les dés qu'il contient avec une méthode `roll()`{.language-} (la méthode `roll`{.language-} ne doit pas avoir de paramètres)

{% endfaire %}

### Code python {#tapis-vert-python}

{% faire %}
Créez le code python de la classe `TapisVert`{.language-} (dans le fichier `dice.py`{.fichier})
{% endfaire %}

Pour ses tests vous pourrez :

{% faire %}

* Vérifier qu'après la création d'un objet `TapisVert`{.language-} on dispose bien de 5 dés positionnés sur 1.
* Vérifiez qu'après avoir lancé les dés, leurs positions sont toujours cohérentes avec le nombre de faces.
* Vérifiez que `TapisVert`{.language-} donne bien ses dés et non une copie de ceux-ci. Pour réaliser ceci vous pourrez implémenter le test suivant :
   1. demander les dés d'un objet de type `TapisVert`{.language-}
   2. modifier la position d'un dé
   3. redemander les dés de l'objet de type `TapisVert`{.language-} et vérifier que la position du dé est bien celle modifiée

{% endfaire %}

### Analyse du code

{% faire %}

1. Comment est-il possible d'avoir à la fois une méthode `roll`{.language-} pour `Dice`{.language-} et pour `TapisVert`{.language-} sans que python s'embrouille ?
2. Explicitez tous les namespaces utilisées (namespace de classe, d'objet, de fichier et de fonctions) lors de l'exécution de : `tapis_vert.roll()`{.language-}

{% endfaire %}

### Pour aller plus loin

{% faire %}

1. faites en sorte de pouvoir afficher joliment un objet `TapisVert`{.language-} (en affichant par exemple la valeurs de ses 5 dés)
2. Ajoutez des méthodes à `TapisVert`{.language-} permettant de savoir s'il a une paire, un brelan, un carré.
3. Ajoutez des méthodes à `TapisVert`{.language-} permettant de savoir s'il a une double-paire ou un full.

{% endfaire %}

### Pour aller encore plus loin

{% faire %}

Implémentez le jeu [poker d'as](https://fr.wikipedia.org/wiki/Poker_d%27as).

Notez qu'il faudra ajouter des méthodes permettant de bloquer un dé pour qu'il ne participe pas au lancer.

{% endfaire %}

---
layout: layout/post.njk 
title: "Projet : composition et agrégation"

eleventyNavigation:
  key: "Projet : composition et agrégation"
  parent: "Programmation Objet"

prerequis:
    - "../composition-agrégation/"
    - "../projet-objets-dés/"
    - "../projet-objets-cartes/"
---

<!-- début résumé -->

Classes et objets, la version 2.

<!-- end résumé -->

Dans les premiers projets objets, vous avez codé des classes toutes seules. Le but de ces projets introductifs étaient de vous montrer comment rassembler les différentes parties d'un concept en un tout appelé objet. Nous allons ici aller une étape plus loin en combinant des objets que l'on a créé dans d'autres objets.

## Tapis vert

Cette partie est la suite du projet dés. Donc si vous ne l'avez pas déjà fait, commencez par le faire :

{% aller %}
[Projet objets : dés](../projet-objets-dés/)
{% endaller %}

Pour les besoin de ce TD, nous allons présupposer que vous avez une classe `Dé`{.language-} qui fonctionne. La version minimale que nous allons utiliser ici est disponible ci-après. Mais ne vous sentez pas obliger de l'utiliser.

{% details "**une implémentation de la classe `Dé`{.language-}**" %}

fichier `dé.py`{.fichier} :

```python
class Dé:
   pass
```

fichier `test_dé.py`{.fichier} :

```python
class Dé:
   pass
```

{% enddetails %}

> dés, tapis vert (compose dés) et jeu (compose tapis vert + règles)
> cartes, bataille avec deck et jeu

### 5 dés

Méthode naïve pour manipuler 5 dés.

{% faire %}
Dans un fichier `main_5_des.py`{.fichier} Créez une liste avec 5 dés. Utilisez une boucle `for`{.language-} pour les lancer tous les 5, puis voir le résultat du lancer des 5 dés.
{% endfaire %}

### Composition

Nous allons créer une classe permettant de gérer nos 5 dès de façon plus pratique qu'avec notre liste.

Pour pouvoir jouer à des jeux de dés, implémentons une classe `TapisVert`{.language-}.

### Modèle du tapis vert

{% faire %}

1. Proposez une modélisation UML de la classe `TapisVert`{.language-}.
2. donnez des exemples de manipulation d'objets de cette classe comme :
   * créer un objet
   * donner un tuple contenant ses 5 dés
   * lancer les dés qu'il contient avec une méthode `roll()`{.language-} (la méthode `roll`{.language-} ne doit pas avoir de paramètres)

{% endfaire %}

### Code python du tapis vert

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

## Carte

> TBD jeux
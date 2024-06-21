---
layout: layout/post.njk
title: Complexité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La complexité d'un pseudo-code est une mesure associée au pseudo-code. Elle peut mesurer 2 grandeurs physique lors de l'exécution d'un algorithme :

- **_complexité en temps_** : le nombre d'instruction effectuées pendant son exécution
- **_complexité en espace_** : le nombre de cases mémoires maximales utilisées pendant son exécution.

Par défaut, la complexité utilisée est celle en temps :

{% note "**Définition**" %}
La complexité d'un pseudo-code est la complexité en temps de celui-ci.
{% endnote %}

Par exemple le pseudo-code suivant :

```text#
x = 30
if ((x > 12) AND (x < 36)):
    z = "entre 13 et 35"
```

1. Création de l'entier valant 30 : 1 instruction
2. on affecte l'entier à x : 1 instruction
3. Pour faire cette instruction il faut :
   - faire `x > 12`{.language-}. Pour cela :
     - on crée l'entier valant 12 : 1 instruction
     - on récupère la valeur de `x`{.language-} : 1 instruction
     - on effectue la comparaison : 1 instruction
   - faire `x < 36`{.language-}. Pour cela :
     - on crée l'entier valant 36 : 1 instruction
     - on récupère la valeur de `x`{.language-} : 1 instruction
     - on effectue la comparaison : 1 instruction
   - faire l'instruction `AND`{.language-} : 1 instruction
   - faire le `if`{.language-} : 1 instruction
4. on commence par récupérer la valeur de `x`{.language-} (1 instruction), on crée la chaîne (1 instruction) puis affecte le résultat d'une opération élémentaire (2 instructions) : donc un total de 4 instructions

Un nombre total d'instructions de 14.

## Complexité des appels de fonctions

Si l'on devait à chaque pseudo-code redéfinir tout les algorithmes qu'on utilise ce serait vraiment fastidieux. On utilise souvent des fonctions non basiques (comme l'affichage à l'écran qu'on a déjà vu) ou des structures plus élaborées (les listes par exemples qui sont des extensions des tableaux). Il faudra cependant toujours connaître les complexités de ce qu'on utilise.

{% attention %}
Lorsque l'on calcule la complexité d'un pseudo-code utilisant des fonctions, il faut compter le nombre d'instructions de l'exécution des fonctions !
{% endattention %}

Prenons par exemple le code suivant et comptons les instructions utilisées au cours de son exécution :

```python#
def recherche(t, x):
    for e in t:
        if e == x:
            return True
    return False

t = [1, 2, 6]
trouve = recherche(t, 6)
affiche à l'écran trouve
```

1. exécution de la ligne 7 : création d'un tableau et affectation à une variable : 2 instructions
2. exécution de la ligne 8 :
   1. exécution de la fonction recherche (ligne à ligne) :
      1. exécution de la ligne 1 : affectation des paramètres
         1. trouver les objets à mettre en paramètres :
            - pour le premier paramètre il faut trouver l'objet associé à t : 1 instruction
            - pour le second paramètre, l'objet est à créer : 1 instruction
         2. affecter les paramètres aux variables de la fonction :
            - affectation du premier paramètre à la variable locale t : 1 instruction
            - affectation du second paramètre à la variable locale e : 1 instruction
      2. exécution de la ligne 2 (3 fois): affecter `e` : 1 instruction
      3. exécution de la ligne 3 : un test
         - on trouve les objets associées à t et e : 2 instructions
         - on teste l'égalité : 1 instruction
         - on fait le `if`{.language-} : 1 instruction
      4. exécution de la ligne 4 : on arrive à cette ligne à la troisième itération : 1 instruction
   2. affection de la variable `trouve`{.language-}
3. afficher quelque chose à l'écran :
   - 1 instruction pour trouver l'objet à afficher
   - 1 instruction pour trouver l'afficher

Au total on eu besoin de $2+2+1+\underbracket{(1+1+1+1+3 \cdot (2+1+1) + 1)}_{\mbox{recherche(t, 6)}} + 1 + 1$
instructions c'est à dire $24$ instructions.

## Complexité des structures

> TBD re-écrire sous la forme de structures
> 
Si l'on devait à chaque pseudo-code redéfinir tout les algorithmes qu'on utilise ce serait vraiment fastidieux. On utilise souvent des fonctions non basiques (comme l'affichage à l'écran qu'on a déjà vu) ou des structures plus élaborées (les listes par exemples qui sont des extensions des tableaux). Il faudra cependant toujours connaître les complexités de ce qu'on utilise.

Par exemple pour les listes, qui sont des tableaux redimensionnables :

- complexité d'ajout d'un élément à la fin de la liste : coût de 1 instruction
- complexité de l'ajout d'un élément pas à la fin de la liste : coût de la taille de la liste instructions
- complexité de la suppression d'un élément à la fin de la liste : coût de 1 instruction
- complexité de la suppression d'un élément pas à la fin de la liste : coût de la taille de la liste instructions
- usage comme un tableau : 1 instruction

Si vous utilisez des méthodes d'objets comme vous avez l'habitude de le faire en python (comme une `ma_liste.index("?")`{.language-}, `x in ma_chaîne_de_caractères`{.language-}) ou des structures compliquées (télécharger un fichier d'internet) vous avez le droit mais vous **devez** en connaître le coût : la complexité, les cas d'usage (comme être connecté à internet), etc.

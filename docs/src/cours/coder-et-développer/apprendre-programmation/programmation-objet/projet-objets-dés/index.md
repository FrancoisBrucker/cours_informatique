---
layout: layout/post.njk 
title: "Projet : objets dés"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Projet sur le codage d'objets en python. Notre but est de pouvoir créer des dés virtuels pour pouvoir [jouer au 421](https://fr.wikipedia.org/wiki/421_(jeu)).

{% note "**Méthode de conception**" %}
Lorsque l'on crée un objet qui correspond à un objet réel, il faut faire en sorte que le code l'utilise comme on le ferait dans la réalité.
{% endnote %}

## Fonctionnalités d'un Dé

Si on veut pouvoir utiliser nos dés virtuels comme un vrai dé physique, la classe `Dé`{.language-} doit être capable de :

- créer un objet sans paramètre (sa position est alors 1),

- connaître et donner la position du dé,
- lancer un dé en utilisant une méthode nommée `lancer()`{.language-} qui ne rend **rien**, mais change la position du dé de façon aléatoire.

La position du dé doit être un entier entre 1 et 6.

### Modélisation UML

Des spécifications précédentes, on doit pouvoir en déterminer la modélisation UML.


{% faire %}

1. Proposez une modélisation UML de la classe `Dé`{.language-}.
2. Donnez des exemples de code qui manipulent des objets de cette classe, comme :
   - créer un objet
   - afficher sa position à l'écran
   - modifier sa position
   - lancer le dé

{% endfaire %}

### Code python (squelette)

{% attention2 "**À retenir : Conventions de nommage en python**" %}

En résumé :

- les noms de variables, de fonctions et de méthodes sont écrites :
  - tout en minuscules
  - utilisent le [_Snake case_](https://fr.wikipedia.org/wiki/Snake_case) où les mots sont séparés par des _underscores_ (`_`{.language-})
- les constantes sont écrites tout en majuscule
- le noms de classes sont écrites :
  - avec une majuscule
  - utilisent le [_Camel case_](https://fr.wikipedia.org/wiki/Camel_case) où les mots sont attachés les uns aux autres mais commencent par une majuscule
- les noms commençant par `__` et se finissant par `__` (comme `__name__`) ont des significations précises

{% endattention2 %}
{% lien %}
Toutes les [conventions de nommage de python](https://peps.python.org/pep-0008/#prescriptive-naming-conventions).
{% endlien %}

{% note "**Conventions**" %}

- les **noms** de classe commencent par une **majuscule**
- l'implémentation de la classe est placée dans un **fichier** de même nom mais avec une **minuscule**

{% endnote %}
{% info %}
En python, beaucoup de choses sont des [conventions](https://en.wikipedia.org/wiki/Convention_over_configuration) (variable privée, premier nom est self, ...) mais tout le monde s'y tient car la lecture du code en devient aisée. Il est facile de savoir de quel type est le nom rencontré en python si l'on utilise les façons de faire classiques, décrites dans la [PEP 8](https://peps.python.org/pep-0008/) de python.
{% endinfo %}

> commencer par mimer l'UML avec des méthodes pass.
On a utilisé l'instruction [`pass`{.language-}](https://www.docstring.fr/glossaire/pass/) qui ne fait rien. Nous l’utilisons ici car la définition d'une classe crée un bloc (il y a un `:`) et que tout bloc **doit** contenir une instruction.



Faites en particulier attention à la façon dont vous voulez lancer le dé.

## Projet vscode

{% faire %}
Créez un dossier `projet-dés`{.fichier} sur votre ordinateur et ouvrez-le avec visual studio code pour un faire votre projet.
{% endfaire %}

## User stories

{% note "Définition" %}
Une [user story](https://fr.wikipedia.org/wiki/R%C3%A9cit_utilisateur) est un récit qui nous permet de savoir comment et par qui va être utilisé notre code.
{% endnote %}

L'idée est d'écrire une succession d'actions faites par un utilisateur typique afin de réaliser une tâche précise avec notre programme. Par exemple :
{% note "**User story**" %}

- Nom : "Aléatoire ?"
- Utilisateur : un professeur.
- Story : On vérifie que le lancer de dé ressemble à de l'aléatoire.
- Actions :
  1. créer un dé sans paramètre
  2. afficher à l'écran sa position (ça doit être 1)
  3. lancer le dé 10 fois et affiche la position du dé après chaque lancer. Quelle est la probabilité que le dé ne change jamais ?.

{% endnote %}

Essayons de voir ce que donnerait cette user story si on devait la coder :

{% exercice %}

En utilisant la modélisation UML du Dé, codez la user story "Aléatoire" en python dans le fichier `story_aléatoire.py`{.fichier}.

{% endexercice %}
{% details "corrigé" %}
Il y a une probabilité de $\frac{1}{6^{10}} = 1.6 \cdot 10^{-8}$ que le dé ne change jamais de position en 10 lancers.

La user story donnerait en python :

```python
from dé import Dé

# 1. créer un dé sans paramètre
dé = Dé() 

# 2. afficher à l'écran sa position (ça doit être 1)
print(dé.position)

# 3. lancer le dé 10 fois et affiche la position du dé après chaque lancer
for i in range(10):
   dé.lancer()
   print(dé.position)
```

{% enddetails %}

Comme pour l'instant rien n'est codé :

{% faire %}
Commentez les codes python de la user story. A chaque fois que l'on codera une fonctionnalité, on dé-commentera ce qui marchera. A la fin de la session de code, votre user story devra être opérationnelle.
{% endfaire %}

La user story fait office de **test fonctionnel** qui permet de vérifier que le code correspond aux attentes des utilisateurs.

{% note %}
Un programme aura :

- **toujours** des [tests unitaires](https://fr.wikipedia.org/wiki/Test_unitaire) car ils garantissent que ce que vous avez codé est correct
- **très souvent** des [tests fonctionnels](https://en.wikipedia.org/wiki/Functional_testing) car ils garantissent que ce que vous avez codé pourra être utile

On exécutera la batterie de tests unitaires à chaque fois que l'on code ou que l'on modifie une fonction, les tests fonctionnels sont exécutés a chaque fois que l'on achève une fonctionnalité.

{% endnote %}
{% info %}
Les fonctionnalités développées doivent toutes faire parti d'au moins une user story, sinon c'est [YAGNI](../../développement/écrire-code/coder/#YAGNI){.interne}.
{% endinfo %}

## Code

### Classe vide

{% faire %}
Crée un ficher `dé.py`{.fichier} contenant une classe `Dé`{.language-} vide et testez avec la fonction de test `test_init()`{.language-} dans un fichier `test_dé.py`{.fichier} que l'on peut créer des objets de cette classe.
{% endfaire %}

{% faire %}
Dé-commentez la première partie de la user story et vérifiez qu'elle fonctionne.
{% endfaire %}

### Attribut `position`{.language-}

{% faire %}
Ajoutez l'attribut position au dé et assurez vous qu'il est bien initialisé à 1 dans un test nommé `test_position()`{.language-}.
{% endfaire %}

{% faire %}
Dé-commentez la seconde partie de la user story et vérifiez qu'elle fonctionne.
{% endfaire %}

Finalisons les différentes initialisations possible de l'attribut `position`{.language-} :

{% faire %}
Faites en sorte que l'on doive choisir la position initiale du dé dans le constructeur. Ajoutez un test correspondant dans le test `test_position()`{.language-}.
{% endfaire %}

### Méthode `Dé.lancer()`{.language-}

{% info %}
Dans la documentation et lorsque l'on décrit une méthode, som nom de la méthode est toujours accolé au nom de la classe qui la définit. Par exemple :  `Dé.lancer()`{.language-} signifie :

- la méthode `lancer`{.language-} de la classe `Dé`{.language-}
- cette méthode ne prend pas de paramètre.

{% endinfo %}
{% attention %}
Lorsque l'on décrit une méthode, on ne montre jamais `self`{.language-}. Ce n'est en effet pas un paramètre de la méthode à proprement parlé, c'est l'**objet** de la méthode : il est à gauche du `.`{.language-} lors de l'appel de la fonction.

On pourrait (mais on ne le fait pas parce que c'est moins clair) replacer le code suivant :

```python
>>> un_dé = Dé()
>>> un_dé.lancer()
```

Par le code ci-après qui est équivalent :

```python
>>> un_dé = Dé()
>>> Dé.lancer(un_dé)
```

{% endattention %}

Il ~~nous~~ vous reste à coder la méthode `Dé.lancer()`{.language-} :

{% faire %}
Codez la méthode `Dé.lancer()`{.language-} qui modifie aléatoirement la position du dé appelant par un entier allant de 1 à 6.
{% endfaire %}

Il est impossible de tester le hasard (on pourrait n'avoir pas de chance et lancer 10 fois le dé sans que la position ne change **sans** que ce soit mal codé), on ne va donc uniquement tester ici que le fait que la méthode lancer s'exécute sans soucis et le résultat reste cohérent :

{% faire %}
Ajouter un test nommé `test_lancer()`{.language-} qui vérifie que la position d'un dé après un lancer est toujours entre 1 et 6.
{% endfaire %}

Vous pouvez maintenant voir si la user story fonctionne :

{% faire %}
Dé-commentez la dernière partie de la user story et vérifiez qu'elle fonctionne.
{% endfaire %}

### Affichage

Pour l'instant, lorsque l'on tente d'afficher un dé on obtient le charabia suivant :

```python
>>> dé = Dé()
>>> print(dé)
<__main__.Dé object at 0x10a691010>
```

Ce qui n'est pas très informatif. On peut bien sur afficher sa position :

```python
>>> dé = Dé()
>>> print(dé.position)
1
```

Mais représenter un dé par un entier ce n'est pas très joli. Nous allons coder une méthode spécifique pour représenter notre objet sous la forme d'une chaîne de caractère : la méthode `Dé.texte()`{.language-}.
 
{% faire %}
Créez (et faites les tests) une méthode `Dé.texte()`{.language-} qui permette d'écrire :

```python
>>> d = Dé()
>>> print(d.texte())
⚀
>>> d.position = 4
>>> print(d.texte())
⚃
```

{% endfaire %}
{% info %}
Vous pourrez utiliser les caractères : `"⚀"`{.language-}, `"⚁"`{.language-}, `"⚂"`{.language-}, `"⚃"`{.language-}, `"⚄"`{.language-} et `"⚅"`{.language-} pour vos représentations.
{% endinfo %}

Vous pourrez maintenant utiliser cette méthode pour l'affichage de tous vos dés, en particulier pour les user stories !

## Programme principal

Avant de coder le programme principal :

{% faire %}

1. vérifiez que les tests unitaires fonctionnent
2. vérifiez que vos user stories sont toutes fonctionnelles

{% endfaire %}

Une fois tout ok, on peut commencer à créer le code du `main.py`{.fichier} :

{% faire %}

Créez un fichier `main.py`{.fichier} qui :

1. demande à l'utilisateur :
   - la position initiale du dé
   - la position pour laquelle arrêter les lancers
2. lance le dé jusqu'à tant que sa position est différente de la position demandée par l’utilisateur soit trouvée.
3. le programme affiche le nombre de lancer nécessaire (cela peut être 0)

{% endfaire %}

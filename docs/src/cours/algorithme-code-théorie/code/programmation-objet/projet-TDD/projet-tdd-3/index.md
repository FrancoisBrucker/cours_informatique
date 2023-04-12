---
layout: layout/post.njk 
title: "Partie 3 / 3"

eleventyNavigation:
    order: 3

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Troisième et dernière partie du projet TDD.

<!-- end résumé -->

## Todo list initiale

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`{.language-}
* [ ] `==`{.language-} avec autre chose qu'un `Dollar`{.language-}

On est arrivé à un point clé de notre projet. La classe `Monnaie`{.language-} permet de gérer plusieurs devises et de multiplier les montant par un entier.

On va encore épurer la todo list en supprimant les améliorations possibles de `==`{.language-} et la gestion des arrondis (que l'on vous laisse en exercice :-)) :

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5

## Déroulé

On va dans cette partie vous laisser plus libre et moins détailler les étapes. Ce sera à vous de modifier petit à petit votre code et à lancer les tests autant de de fois que nécessaire.

Nous allons ici faire en sorte que l'on puisse additionner des devises ensemble et gérer le taux de change. Cela va nécessiter l'utilisation de design patterns adaptés.

Rappelez vous (et forcez vous à le faire jusqu'à ce que ça devienne un automatisme) que l'on écrit **d'abord** le test, puis que l'on code **après** : on ne code que sur du **vert**, il n'y a **aucune** exception.

{% note "**Principe du TDD**" %}

1. **rouge** :
   * écrire *rapidement* un *petit* test
   * lancer les tests et les voir planter, voir même  ne correspondre à aucun code.
2. **vert** :
   * écrire le code *minimal* qui permet de faire passer le test
   * lancer les tests et les voir tous réussir
3. **code/refactor** :
   * élimine les duplications tout en conservant la validité des tests.

La partie refactor, qui est la partie réelle où l'on code ne se fait **que sur du vert** : on est assuré de ne pas casser le code puisque les tests passent.
{% endnote %}

## Addition 1/3

Avant de traiter l'addition de deux monnaies différentes, commençons par traiter le cas de 1 unique monnaie.

### <span id="todo-list-add-1-1"></span> Todo list

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* **[-] \\$5 + \\$2 = \\$7**

On s'assure dans le test qu'on ne somme pas deux fois la même chose pour éviter des effets de bord possible dans le code (c'est du code smell).

### <span id="faire-add-1-1"></span> Faire

{% exercice %}
Écrivez un test permettant de tester que \\$5 + \\$2 = \\$7 en :

* utilisant la méthode `plus`{.language-} de `Monnaie`{.language-} qui prend une autre monnaie en paramètre et rend une monnaie
* les objets de `Monnaie`{.language-} sont toujours non mutable

Une fois les tests écris, une *obvious implementation* devrait faire l'affaire.
{% endexercice %}
{% details "solution" %}

Fichier `test_monnaie.py`{.fichier} :

```python
# ...

def test_plus():
    assert monnaie.dollar(7) == monnaie.dollar(5).plus(monnaie.dollar(2))

# ...
```

Fichier `monnaie.py`{.fichier}

```python
# ...

class Monnaie:
    # ...

    def plus(self, other):
        return Monnaie(self.montant + other.montant, self.devise)

    # ...

# ...
```

{% enddetails %}

### <span id="faire-add-1-2"></span> Faire

Rendons les choses jolies en utilisant `__add__`{.language-} qui est le pendant pour l'addition de `__mul__`{.language-}

{% exercice %}
Remplacez la méthode `plus`{.language-} par `__add__`{.language-} dans `Monnaie`{.language-}.
{% endexercice %}
{% details "solution" %}

*easy peasy*, on remplace juste `plus`{.language-} par `+`{.language-}

Fichier `test_monnaie.py`{.fichier} :

```python
# ...

def test_plus():
    assert monnaie.dollar(7) == monnaie.dollar(5) + monnaie.dollar(2)

# ...
```

et  `plus`{.language-} par `__add__`{.language-}

Fichier `monnaie.py`{.fichier} :

```python
# ...

class Monnaie:
    # ...

    def __add__(self, other):
        return Monnaie(self.montant + other.montant, self.devise)

    # ...

# ...
```

{% enddetails %}

### <span id="todo-list-add-1-2"></span> Todo list

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [X] \\$5 + \\$2 = \\$7

## Addition 2/3

Notre implémentation de `+`{.language-} qui rend un objet de type `Monnaie`{.language-} ne sera pas tenable longtemps.

En effet `$5 + 2.5CHF` **ne peut pas être** un objet de type `Monnaie`{.language-}. Ce sont en effet deux devises différentes dont la valeur va dépendre d'un cours [qui change au cours du temps](https://fr.tradingview.com/symbols/USDCHF/). La somme `$5 + 2.5CHF` peut ainsi valoir `$10` en 2022 et `$7` en 2034.

Il faut donc résoudre deux problèmes :

* comment stocker une somme sous la forme de plusieurs devises ?
* comment convertir une monnaie ou un ensemble de monnaies en une autre ?

### <span id="todo-list-add-2-1"></span> Todo list

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* **[-] \\$5 + \\$2 = quelque chose qui correspond à $7**

### <span id="faire-add-2-1"></span> Faire

Pour imaginer cela rien de mieux qu'un test ! On va l'écrire à l'envers, en partant du résultat, car  on sait où on veut arriver : à $10 :

```python
### ...

def test_conversion_addition():
    # ...
    
    assert monnaie.dollar(7) == conversion

# ...
```

Ces $10 viennent d'une conversion en dollar d'une somme de deux monnaies, conversion qui -- d'un point de vue métier -- ne peut venir que d'une banque :

```python
### ...

def test_conversion_addition():
    # ...
    
    conversion = banque.conversion(somme, "USD")

    assert monnaie.dollar(7) == conversion

# ...
```

Banque qu'il faut créer :

```python
### ...

def test_conversion_addition():
    # ...
    
    banque = monnaie.Banque()
    conversion = banque.conversion(somme, "USD")

    assert monnaie.dollar(7) == conversion

# ...
```

Il ne reste plus qu'à fabriquer notre expression pur avoir notre test final :

```python
### ...

def test_conversion_addition():
    somme = monnaie.dollar(5) + monnaie.dollar(2)
    banque = monnaie.Banque()
    conversion = banque.conversion(somme, "USD")

    assert monnaie.dollar(7) == conversion

# ...
```

{% exercice %}
Ajoutez le test dans `test_monnaie.py`{.fichier} et *fakez* le tout dans `monnaie.py`{.fichier}  pour que le test passe.
{% endexercice %}
{% details "solution" %}

Fichier `monnaie.py`{.fichier} :

```python
# ...

class Banque:
    def conversion(self, expression, currency):
        return dollar(7)

# ...
```

{% enddetails %}

## Addition 3/3

L'implémentation réelle de tout ce qu'on a *faké* n'est pas si évidente que ça. On va donc devoir faire des choix restrictifs et ajouter à la todo list les généralisations à effectuer pour terminer le travail.

On va considérer que toute somme de deux monnaies est une nouvelle classe `Somme`{.language-} (on va cependant ajouter que la somme de 2 monnaies identiques devrait rendre une monnaie, comme pour la multiplication,  dans la todo list).

### <span id="todo-list-add-3-1"></span> Todo list

On change notre item de la todo list puisque \\$5 + \\$2 ne sera plus égal à \\$7, mais que ce serait bien qu'il soit :

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] \\$5 + \\$2 doit être égal à \\$7
* **[-] \\$5 + \\$2 = quelque chose qui correspond à $7**

### <span id="faire-add-3-1"></span> Faire

{% exercice %}

1. supprimez le test `test_plus`{.language-} qui vérifie que \\$5 + \\$2 = \\$7 ce qui n'est plus vrai
2. on ajoute un test pour montrer que la somme de deux monnaies est un objet contenant une partie gauche (la partie à gauche du `+`{.language-}) et une partie droite (la partie à droite du `+`{.language-})
3. on implémente le tout en une petite *obvious implementation*

{% endexercice %}
{% details "solution" %}

Fichier `test_monnaie.py`{.fichier} :

```python
# ...

def test_plus_est_une_Somme():
    somme = monnaie.dollar(5) + monnaie.dollar(2)

    assert somme.gauche == monnaie.dollar(5)
    assert somme.droite == monnaie.dollar(2)

# ...
```

Fichier `monnaie.py`{.fichier} :

```python
# ...

class Somme:
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

# ... 

class Monnaie:
    # ...

    def __add__(self, other):
        return Somme(self, other)

    # ...

# ...
```

{% enddetails %}

### <span id="todo-list-add-3-2"></span> Todo list

On a pas fini notre item.

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] \\$5 + \\$2 doit être égal à \\$7
* **[-] \\$5 + \\$2 = quelque chose qui correspond à $7**

Mais on a bien avancé puisque  \\$5 + \\$2 n'est plus une `Monnaie`{.language-}. Il nous reste à faire en sorte que ce quelque chose corresponde à \\$7.

## Conversion 1/3

Pour que \\$5 + \\$2 corresponde à quelque chose qui vaut à \\$7, on doit travailler sur la méthode `conversion`{.language-} de la `Banque`{.language-}. C'est elle qui doit pouvoir faire le change (pour l'instant c'est un *fake* qui rend \\$7).

### <span id="todo-list-conversion-1-2"></span> Todo list

Pour l'instant, `Banque.conversion`{.language-} prend pour une `Somme`{.language-} en paramètre. Nous n'allons pas ous en occuper tout de suite, mais il pourrait être intéressant qu'elle puisse aussi prendre une `Monnaie`{.language-} en paramètre pour faire le change :

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] \\$5 + \\$2 doit être égal à \\$7
* **[-] \\$5 + \\$2 = quelque chose qui correspond à $7**
* [ ] `Banque.conversion(Monnaie)`{.language-}

### <span id="faire-conversion-1-1"></span> Faire

Le test `test_conversion_addition`{.language-} affirme que `banque.conversion(monnaie.dollar(5) + monnaie.dollar(2), "USD")`{.language-} vaut  `monnaie.dollar(7)`{.language-}. Mais notre implémentation est encore un fake (il reste plein de duplications).

{% exercice %}
Supprimer les duplication de la méthode `Banque.conversion`{.language-} en :

* supposant que les parties `gauche`{.language-} et `droite`{.language-} de la somme sont des `Monnaie`{.language-}
* que le taux de change est toujours de 1 pour 1

{% endexercice %}
{% details "solution" %}

Fichier `monnaie.py`{.fichier} :

```python
# ...

class Banque:
    def conversion(self, expression, devise):
        return Monnaie(expression.gauche.montant + expression.droite.montant, devise)

# ...
```

{% enddetails %}

C'est un début. Il nous reste à gérer :

* lorsque les deux parties de la `Somme`{.language-} ne sont pas des `Monnaie`{.language-}
* le taux de change

## Conversion 2/3

L'implémentation actuelle de la méthode `Banque.conversion`{.language-} — même si incomplète — pose déjà des soucis. En particulier : la banque doit connaître l'implémentation de `Monnaie`{.language-} pour avoir accès à l'attribut `montant`{.language-}.

Lorsque l'on fait du développement objet, on aime pas trop que tous les objets connaissent les attributs de tout le monde. Cela couple les objets entre eux et le code en devient moins maniable (en changeant une classe, il faut changer toutes les autres...)

{% note "**Principe de développement objet :** [loi de Déméter](https://fr.wikipedia.org/wiki/Loi_de_D%C3%A9m%C3%A9ter)" %}

Toute méthode `m`{.language-} d'un objet `o`{.language-} de classe `C`{.language-} ne peut invoquer que :

* les paramètres de `m`{.language-}
* les objets créés par `m`{.language-}
* lui-même
* les méthodes de `C`{.language-}

Un bon programme utilise des objets qui interagissent entre eux mais qui ne connaissent pas l'implémentation des autres classes. Les objets doivent être le plus découplé possible.
{% endnote %}

En particulier, la loi de Déméter demande d'éviter d'appeler les méthodes d'un attribut d'un objet ce qui est exactement ce que l'on fait.

### <span id="faire-conversion-2-1"></span> Faire

Pour éviter cette double indirection :

{% exercice %}
Remontez d'un cran le code de `Banque.conversion`{.language-} en le plaçant dans une méthode `Somme.conversion(devise)`{.language-}. Pour l'instant on suppose toujours que le taux de conversion est de 1 pour 1 quelque soient les monnaies et que les parties gauche et droite des `Somme`{.language-} sont des `Monnaies`{.language-}.
{% endexercice %}
{% details "solution" %}

Fichier `monnaie.py`{.fichier} :

```python
# ...

class Banque:
    def conversion(self, expression, devise):
        return expression.conversion(devise)

# ...

class Somme:
    # ... 

    def conversion(self, devise):
        return Monnaie(self.gauche.montant + self.droite.montant, devise)

    # ... 

# ...
```

{% enddetails %}

### <span id="todo-list-conversion-2-1"></span> Todo list

On a fini un item, mais avec plein de restrictions. Ajoutons les à la la todo list.

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] \\$5 + \\$2 doit être égal à \\$7
* [X] \\$5 + \\$2 = quelque chose qui correspond à $7
* [ ] `Banque.conversion(Monnaie)`{.language-}
* [ ] `Somme.conversion(devise)`{.language-} doit vraiment faire des conversions

## Conversion 3/3

L'étape précédente a permis de baisser le niveau de connaissance de la banque des objets qui l'entourent. C'est une bonne chose car cela suit la loi de Déméter.

Monter la méthode `conversion`{.language-} de la `Banque`{.language-} à la `Somme`{.language-} nous permet également de traiter le cas où `Banque.conversion`{.language-} a une  `Monnaie`{.language-} comme paramètre : il suffit de rajouter une méthode `Monnaie.conversion`{.language-} !

### <span id="todo-list-conversion-3-1"></span> Todo list

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] \\$5 + \\$2 doit être égal à \\$7
* [X] \\$5 + \\$2 = quelque chose qui correspond à $7
* **[-] `Banque.conversion(Monnaie)`{.language-}**
* [ ] `Somme.conversion(devise)`{.language-} doit vraiment faire des conversions

### <span id="faire-conversion-3-1"></span> Faire

{% exercice %}

1. créez un test où l'argument de `Banque.conversion`{.language-} est un objet de type `Monnaie`{.language-}
2. implémentez le code correspondant

De même que précédemment, on va considérer que le seul paramètre de la méthode `Monnaie.conversion`{.language-} la devise d'arrivée et que — pour l'instant — le taux de change est de 1 pour 1
{% endexercice %}
{% details "solution" %}

Fichier `test_monnaie.py`{.fichier} :

```python
# ...

def test_banque_conversion_monnaie_identique():
    banque = monnaie.Banque()
    assert monnaie.dollar(1) == banque.conversion(monnaie.dollar(1), "USD")

# ...
```

Fichier `monnaie.py`{.fichier} :

```python
# ...

class Monnaie:
    # ...

    def conversion(self, devise):
        return Monnaie(self.montant, devise)

    # ...

# ...
```

{% enddetails %}

### <span id="todo-list-conversion-3-2"></span> Todo list

On a fini un item, mais avec plein de restrictions. Ajoutons les à la la todo list :

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] \\$5 + \\$2 doit être égal à \\$7
* [X] \\$5 + \\$2 = quelque chose qui correspond à $7
* [X] `Banque.conversion(Monnaie)`{.language-}
* [ ] `Somme.conversion(devise)`{.language-} doit vraiment faire des conversions
* [ ] `Monnaie.conversion(devise)`{.language-} doit vraiment faire des conversions

## Taux de change 1/2

On va maintenant s'attaquer à la conversion. Commençons simple avec les objets de type `Monnaie`{.language-}

### <span id="todo-list-change-1-1"></span> Todo list

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] \\$5 + \\$2 doit être égal à \\$7
* [X] \\$5 + \\$2 = quelque chose qui correspond à $7
* [X] `Banque.conversion(Monnaie)`{.language-}
* [ ] `Somme.conversion(devise)`{.language-} doit vraiment faire des conversions
* **[-] `Monnaie.conversion(devise)`{.language-} doit vraiment faire des conversions**

### <span id="faire-change-1-1"></span> Faire

{% exercice %}
On veut que `Banque.conversion(monnaie.dollar(2), "CHF")`{.language-} donne 1. On doit pour cela utilisez un taux de change donné par `Banque.change`{.language-} qui prend 2 devises en paramètres, celle de départ et celle d'arrivée.

1. créez un test qui vérifie que `Banque.change`{.language-} fonctionne pour deux devises identiques et utilisez cette méthode dans `Banque.conversion`{.language-}.
2. créez un test qui vérifie que `Banque.change`{.language-} fonctionne pour convertir des dollar en CHF avec un taux de 2 dollars pour 1 CHF.
3. créez un test qui vérifie que `Banque.conversion(monnaie.dollar(2), "CHF")`{.language-} donne 1
4. utilisez la banque pour faire la conversion dans `Monnaie.conversion`{.language-} (il faudra ajouter la banque comme paramètre)

{% endexercice %}
{% details "solution" %}

Fichier `test_monnaie.py`{.fichier} :

```python
# ...

def test_banque_change_identique():
    assert 1 == monnaie.Banque().change("USD", "USD")


def test_banque_change_CHF_dollar():
    assert 2 == monnaie.Banque().change("CHF", "USD")
    assert 0.5 == approx(monnaie.Banque().change("USD", "CHF"))

# ...

def test_banque_conversion_monnaie_differente():
    banque = monnaie.Banque()
    assert monnaie.franc(1) == banque.conversion(monnaie.dollar(2), "CHF")

# ...
```

Fichier `monnaie.py`{.fichier} :

```python
# ...

class Banque:
    def conversion(self, expression, devise):
        return expression.conversion(self, devise)

    def change(self, devise_depart, devise_arrivée):
        if devise_depart == devise_arrivée:
            return 1
        elif devise_depart == "USD":
            return .5
        else:
            return 2

# ... 

class Somme:
    # ...

    def conversion(self, banque, devise):
        return Monnaie(self.gauche.montant + self.droite.montant, devise)

    # ...

# ...

class Monnaie:
    # ...

    def conversion(self, banque, devise):
        return Monnaie(self.montant * banque.change(self.devise, devise), devise)

    # ...

# ...
```

Remarquez qu'on a du également modifier `Somme.conversion`{.language-} pour que les tests continuent de passer.

{% enddetails %}

### <span id="todo-list-change-1-2"></span> Todo list

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] \\$5 + \\$2 doit être égal à \\$7
* [X] \\$5 + \\$2 = quelque chose qui correspond à $7
* [X] `Banque.conversion(Monnaie)`{.language-}
* [ ] `Somme.conversion(devise)`{.language-} doit vraiment faire des conversions
* [X] `Monnaie.conversion(devise)`{.language-} doit vraiment faire des conversions

### Taux de change 2/2

Pour l'instant notre conversion pour les sommes ne considère que les mêmes devises. On va travailler maintenant sur des devises différentes.

### <span id="todo-list-change-2-1"></span> Todo list

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] \\$5 + \\$2 doit être égal à \\$7
* [X] \\$5 + \\$2 = quelque chose qui correspond à $7
* [X] `Banque.conversion(Monnaie)`{.language-}
* **[-] `Somme.conversion(devise)`{.language-} doit vraiment faire des conversions**
* [X] `Monnaie.conversion(devise)`{.language-} doit vraiment faire des conversions

### <span id="faire-change-2-1"></span> Faire

Commençons simplement :

{% exercice %}
Faire un test qui convertit la somme de \\$2 et 1CHF en franc suisse et implémentez le tout.
{% endexercice %}
{% details "solution" %}

Fichier `test_monnaie.py`{.fichier} :

```python
# ...

def test_somme_conversion_deux_monnaies():
    assert monnaie.franc(2) == monnaie.Banque().conversion(monnaie.dollar(2) + monnaie.franc(1), "CHF")

# ...
```

Fichier `monnaie.py`{.fichier} :

```python
# ...

class Somme:
    # ...

    def conversion(self, banque, devise):
        gauche = banque.conversion(self.gauche, devise)
        droite = banque.conversion(self.droite, devise)
        return Monnaie(gauche.montant + droite.montant, devise)

    # ...

# ...

class Monnaie:
    # ...

    def conversion(self, banque, devise):
        return Monnaie(self.montant * banque.change(self.devise, devise), devise)

    # ...

# ...
```

Remarquez qu'on a du également modifier `Somme.conversion`{.language-} pour que les tests continuent de passer.

{% enddetails %}

### <span id="todo-list-change-2-2"></span> Todo list

* [X] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] \\$5 + \\$2 doit être égal à \\$7
* [X] \\$5 + \\$2 = quelque chose qui correspond à $7
* [X] `Banque.conversion(Monnaie)`{.language-}
* [X] `Somme.conversion(devise)`{.language-} doit vraiment faire des conversions**
* [X] `Monnaie.conversion(devise)`{.language-} doit vraiment faire des conversions

## Expressions

Pour finir, il nous reste à généraliser le tout. C'est à dire que l'on aimerait bien pouvoir multiplier une `Somme`{.language-} par un entier par exemple ou additionner des `Somme`{.language-} entre elles.

Le design pattern utilisé pour cela est :

{% note "**Design pattern :** [composite](https://refactoring.guru/fr/design-patterns/composite)" %}

Son but est de pouvoir traiter un groupe d'individu comme un seul. Il utilise une structuration récursive pour cela.
{% endnote %}

Le diagramme de classe du pattern composite peut -être vu comme ça :

![composite](composite.png)

Un nœud va être composé d'autre nœud ou de feuilles, les deux classes ayant une méthode `opération`{.language-}. La méthode `opération`{.language-} de la classe nœud consistant uniquement à successivement appeler la méthode `opérations`{.language-} pour chacun de ses enfants. La terminaison intervenant lorsqu'est appelé la méthode opération d'une feuille.

L'intérêt principal de ce design pattern est que la façon d'appeler la méthode `opération`{.language-} est identique pour un ensemble ou un unique élément.

### <span id="faire-exp-1"></span> Faire

A priori, une partie de la somme de sommes est déjà implémentée. Regardez comment `Somme`{.language-} est construite, en particulier la méthode `__add__`{.language-}.

Par exemple, le test suivant doit passer :

Fichier `test_monnaie.py`{.fichier} :

```python
# ...

def test_somme_de_somme():
    banque = monnaie.Banque()
    expression = monnaie.dollar(1) + (monnaie.franc(2) + monnaie.dollar(1))
    assert monnaie.franc(3) == banque.conversion(expression, "CHF")

# ...
```

{% exercice %}
Pourquoi ?
{% endexercice %}
{% details "solution" %}

La méthode conversion est récursive dans `Somme`{.language-}. Les terminaison se faisant lorsque une partie de la somme est une `Monnaie`{.language-}.

{% enddetails %}

En revanche, ce test ne passe pas encore :

Fichier `test_monnaie.py`{.fichier} :

```python
# ...

def test_somme_de_somme_2():
    banque = monnaie.Banque()
    expression = (monnaie.dollar(1) + monnaie.franc(2)) + monnaie.dollar(1)
    assert monnaie.franc(3) == banque.conversion(expression, "CHF")

# ...
```

{% exercice %}
Pourquoi ?
{% endexercice %}
{% details "solution" %}

Le résultat des tests donne :

```text

    def test_somme_de_somme_2():
        banque = monnaie.Banque()
>       expression = (monnaie.dollar(1) + monnaie.franc(2)) + monnaie.dollar(1)
E       TypeError: unsupported operand type(s) for +: 'Somme' and 'Monnaie'
```

Nous n'avons pas implémenté de méthode `__add__`{.language-} pour les `Somme`{.language-}.
{% enddetails %}

{% exercice %}
Faite passer les tests.
{% endexercice %}
{% details "solution" %}

Fichier `monnaie.py`{.fichier} :

```python
# ...

class Somme:
    # ...

    def __add__(self, other):
        return Somme(self, other)

    # ...

# ...
```

{% enddetails %}

### <span id="faire-exp-2"></span> Faire

Il ne reste plus qu'à tester la multiplication pour finir.

Fichier `test_monnaie.py`{.fichier} :

```python
def test_mult_de_somme():
    banque = monnaie.Banque()

    expression = (monnaie.franc(2) + monnaie.dollar(1)) * 4
    assert monnaie.franc(10) == banque.conversion(expression, "CHF")
```

{% exercice %}
Faite passer le test ci-dessus
{% endexercice %}
{% details "solution" %}
Fichier `monnaie.py`{.fichier} :

```python
# ...

class Somme:
    # ...

    def __mul__(self, multiplier):
        return Somme(self.gauche * multiplier, self.droite * multiplier)
    
    # ...

# ...
```

{% enddetails %}

{% exercice %}
Pourquoi nous sera-t-il impossible d'écrire : `4 * (monnaie.franc(2) + monnaie.dollar(1))`{.language-} ?
{% endexercice %}
{% details "solution" %}

Parce qu'il faudrait modifier la méthode `__mul__`{.language-} des entiers de python, ce qui est impossible.

{% enddetails %}

## Bilan

Vous avez suivi tout un projet de développement par les tests. J'espère vous avoir convaincu que cette méthode permet de développer rapidement et proprement du code (*"clean code that works"*).

### code

#### `test_monnaie.py`{.fichier}

```python
from pytest import approx
import monnaie


def test_multiplication():
    cinq = monnaie.dollar(5)

    assert monnaie.dollar(10) == cinq * 2
    assert monnaie.dollar(15) == cinq * 3


def test_egalite():
    assert monnaie.dollar(5) == monnaie.dollar(5)


def test_non_egalite_dollar():
    assert monnaie.dollar(5) != monnaie.dollar(6)


def test_franc_dollar():
    assert monnaie.franc(1) != monnaie.dollar(1)


def test_devise():
    assert "USD" == monnaie.dollar(1).devise
    assert "CHF" == monnaie.franc(1).devise


def test_plus_est_une_Somme():
    somme = monnaie.dollar(5) + monnaie.dollar(2)

    assert somme.gauche == monnaie.dollar(5)
    assert somme.droite == monnaie.dollar(2)


def test_conversion_addition():
    somme = monnaie.dollar(5) + monnaie.dollar(2)
    banque = monnaie.Banque()
    conversion = banque.conversion(somme, "USD")

    assert monnaie.dollar(7) == conversion


def test_banque_conversion_monnaie_identique():
    banque = monnaie.Banque()
    assert monnaie.dollar(1) == banque.conversion(monnaie.dollar(1), "USD")


def test_banque_conversion_monnaie_differente():
    banque = monnaie.Banque()
    assert monnaie.franc(1) == banque.conversion(monnaie.dollar(2), "CHF")


def test_banque_change_identique():
    assert 1 == monnaie.Banque().change("USD", "USD")


def test_banque_change_CHF_dollar():
    assert 2 == monnaie.Banque().change("CHF", "USD")
    assert 0.5 == approx(monnaie.Banque().change("USD", "CHF"))


def test_somme_conversion_deux_monnaies():
    assert monnaie.franc(2) == monnaie.Banque().conversion(
        monnaie.dollar(2) + monnaie.franc(1), "CHF"
    )


def test_somme_de_somme():
    banque = monnaie.Banque()
    expression = monnaie.dollar(1) + (monnaie.franc(2) + monnaie.dollar(1))
    assert monnaie.franc(3) == banque.conversion(expression, "CHF")


def test_somme_de_somme_2():
    banque = monnaie.Banque()
    expression = (monnaie.dollar(1) + monnaie.franc(2)) + monnaie.dollar(1)
    assert monnaie.franc(3) == banque.conversion(expression, "CHF")


def test_mult_de_somme():
    banque = monnaie.Banque()

    expression = (monnaie.franc(2) + monnaie.dollar(1)) * 4
    assert monnaie.franc(10) == banque.conversion(expression, "CHF")

```

#### `monnaie.py`{.fichier}

```python
def dollar(montant):
    return Monnaie(montant, "USD")


def franc(montant):
    return Monnaie(montant, "CHF")


class Monnaie:
    def __init__(self, montant, devise):
        self.montant = montant
        self.devise = devise

    def __eq__(self, other):
        return self.devise == other.devise and self.montant == other.montant

    def __mul__(self, multiplicateur):
        return Monnaie(self.montant * multiplicateur, self.devise)

    def __add__(self, other):
        return Somme(self, other)

    def conversion(self, banque, devise):
        return Monnaie(self.montant * banque.change(self.devise, devise), devise)


class Banque:
    def conversion(self, expression, devise):
        return expression.conversion(self, devise)

    def change(self, devise_depart, devise_arrivée):
        if devise_depart == devise_arrivée:
            return 1
        elif devise_depart == "USD":
            return 0.5
        else:
            return 2


class Somme:
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

    def conversion(self, banque, devise):
        gauche = banque.conversion(self.gauche, devise)
        droite = banque.conversion(self.droite, devise)
        return Monnaie(gauche.montant + droite.montant, devise)

    def __add__(self, other):
        return Somme(self, other)

    def __mul__(self, multiplier):
        return Somme(self.gauche * multiplier, self.droite * multiplier)

```

---
layout: layout/post.njk

title:  "sujet Test 6 : Le retour de la programmation orientée objet (et elle est pas contente)"
---

{% attention %}
Vous avez 30min pour faire le test.
{% endattention %}

## Rendu

On vous rappelle que toute fonction (hors du programme principal) doit être testée.

### Type de rendu

Vous devrez rendre le dossier d'un projet vscode (vous pouvez le compresser si nécessaire). Commencez donc par créer un projet dans un dossier que vous appellerez `la-POO-C-bo`{.fichier}.

### Éléments de notation

1. 3 fichiers dans un projet :
    - le programme principal `main.py`{.fichier},
    - les fonctions utilisées `fractran.py`{.fichier},
    - les tests des fonctions `test_fractran.py`{.fichier}.
2. Du joli code : le code doit être passé par black.
1. Bons noms :
    - de fichiers,
    - de variables.
2. Tests unitaires : toute fonction doit être testée.

## Sujet

Le but du sujet est de construire un ordinateur !

On utilisera pour cela [le FRACTRAN](https://fr.wikipedia.org/wiki/FRACTRAN) qui est un langage de programmation inventé par John Conway (à qui l'on doit aussi le célèbre [jeu de la vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie)).

Nous allons y aller pas à pas, il suffit de suivre les différentes étapes.

### Fractions

{% faire %}

Implémentez la classe la classe `Fraction`{.language-} dans le fichier `fractran.py`{.fichier}.

{% endfaire %}
{% info %}
Vous pourrez utiliser le fait qu'en python :
- `a // b`{.language-} rend la division entière de `a`{.language-} par `b`{.language-},
- `a % b`{.language-} rend le reste de la division entière  de `a`{.language-} par `b`{.language-}.
{% endinfo %}

La classe doit satisfaire le diagramme UML est le suivant :

![](./fractions.png)

- La méthode `Fraction.est_entier(n)`{.language-} rend un booléen qui est :
  - `True`{.language-} si le dénominateur de la fraction divise `n`{.language-}
  - `True`{.language-} si le dénominateur de la fraction ne divise pas `n`{.language-}
- La méthode `Fraction.valeur(n)`{.language-} rend l'entier résultant de la multiplication du numérateur et de la division entière entre `n`{.language-} et le dénominateur

Les tests suivant explicitent ce fonctionnement (écrits dans `test_fractran.py`{.fichier}) :

```python
from fractran import Fraction


def test_Fraction_init():
    assert Fraction(1, 2).numérateur == 1
    assert Fraction(1, 2).dénominateur == 2


def test_Fraction_est_entier():
    assert Fraction(1, 2).est_entier(2)
    assert not Fraction(1, 3).est_entier(2)


def test_Fraction_valeur():
    assert Fraction(3, 2).valeur(4) == 3 * (4 // 2)


```

### Facteurs

Le langage FRACTAN s'utilise en utilisant la décomposition en facteurs premiers des nombres. 

{% faire %}
Implémentez la classe `Facteur`{.language-} dans le fichier `fractran.py`{.fichier}.

{% endfaire %}
{% info %}
Vous pourrez utiliser le fait qu'en python  `a ** b`{.language-} rend $a^b$.
{% endinfo %}

La classe doit satisfaire le diagramme UML est le suivant :

![](./facteur.png)

- La méthode `Facteur.nombre(L)`{.language-} rend un entier qui vaut le produits des $\text{facteur}[i]^{L[i]}$ pour $0 \leq i < \text{len}(L)$

- La méthode `Fraction.décomposition(n)`{.language-} rend la liste $L$ telle que $n$ soit divisible par $\text{facteur}[i]^{L[i]}$ mais pas par $\text{facteur}[i]^{L[i] + 1}$ pour tout $0 \leq i < \text{len}(\text{facteur})$

Les tests suivant explicitent ce fonctionnement (écrits dans `test_fractran.py`{.fichier}) :

```python
from fractran import Facteur


def test_Facteur_init():
    assert Facteur([2, 3, 7]).facteurs == [2, 3, 7]


def test_Facteur_nombre():
    assert Facteur([2, 3, 7]).nombre([1, 2]) == (2 ** 1) * (3 ** 2)
    assert Facteur([2, 3, 7]).nombre([1, 2, 3]) == (2 ** 1) * (3 ** 2) * (7 ** 3)


def test_Facteur_décomposition():
    assert Facteur([2, 3, 7]).décomposition(1) == [0, 0, 0]
    assert Facteur([2, 3, 7]).décomposition((2**3) * (3**2) * (7)) == [3, 2, 1]

```

### Fractran

Le Fractran est un langage de programmation où un programme est une liste finie de fractions :

<div>
$$
P = [\frac{p_0}{q_0}, \cdots, \frac{p_i}{q_i}, \cdots, \frac{p_{l-1}}{q_{l-1}} ]
$$
</div>

L'exécution du programme $P$ nécessite un paramètre d'entrée $n$ et se déroule comme suit :

1. Tant qu'il existe $i$ tel que $q_i$ divise $n$, on pose $n \leftarrow n \cdot \frac{p_{i^\star}}{p_{i^\star}}$ avec $i^\star$ le plus petit indice $i$ tel que $q_i$ divise $n$.
2. Lorsqu'il n'existe plus d'indice $i$ tel que $q_i$ divise $n$, le programme s'arrête et rend $n$.

Par exemple si $P = [\frac{3}{10}, \frac{4}{3}]$ alors $P(14) = 14$ (aucun dénominateur ne divise 14) et $P(15) = 8$ (3 divise 15 ; 10 divise 20 ; 3 divise 6 ; aucune fraction ne divise 8).

Le code suivant (écrit dans `fractran.py`{.fichier}) implémente cette idée :

```python
class Fractran:
    def __init__(self, fractions):
        self.programme = fractions

    def run(self, n):
        i = 0
        while i < len(self.programme):
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                i = 0
            else:
                i += 1
        return n
    
```

Et est basé sur l'uml suivant :

![](./fractran.png)

{% faire %}

Testez cette classe dans le fichier `test_fractran.py`{.fichier}.

{% endfaire %}

## Programme Principal

Montrons un peu que le Fractran est un vrai langage de programmation en exhibant les programmes qui permettent de calculer la somme et le produit de deux entiers.

{% faire %}
Créez un fichier `main.py`{.fichier} où vous :

1. copierez le code suivant,
2. ajouterez des commentaires explicitant son fonctionnement.

{% endfaire %}

```python
from fractran import Fractran, Fraction, Facteur

facteurs = Facteur([2, 3, 5])

print("Somme :")
somme = [Fraction(3, 2)]
for i in range(10):
    for j in range(10):
        retour = Fractran(somme).run(facteurs.nombre([i, j]))
        décomposition = facteurs.décomposition(retour)
        print(i, "+", j, "=", décomposition[1], "(retour =", retour, "; décomposition =", décomposition,")")


print("Produit :")
produit = [Fraction(455, 33), Fraction(11, 13), Fraction(1, 11), Fraction(3, 7), Fraction(11, 2), Fraction(1, 3)]
for i in range(10):
    for j in range(10):
        retour = Fractran(produit).run(facteurs.nombre([i, j]))
        décomposition = facteurs.décomposition(retour)
        print(i, "*", j, "=", décomposition[2], "(retour =", retour, "décomposition =", décomposition, ")")
```

<!-- 

Ajouter la méthode suite.
## Pour ne pas finir
 -->

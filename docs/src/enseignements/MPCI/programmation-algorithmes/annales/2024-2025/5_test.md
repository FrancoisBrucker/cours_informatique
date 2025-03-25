---
layout: layout/post.njk

title: "Sujet Test 5 : objets"
---

{% attention %}
Vous avez 15min pour faire le test.
{% endattention %}

## Rendu

### Type de rendu

Rendu sur feuille.

### Éléments de notation

Les principales questions sont les quatre premières (une bonne note si vous y répondez bien).

## Sujet

On souhaite créer une classe `Polynome`{.language-} pour manipuler des polynômes avec les fonctionnalités suivantes:

- un polynôme est représenté par la séquence des coefficients de ses monômes par ordre croissant de degré. Par exemple, $P(X) = 3 \cdot X^3 -0.5\cdot  X + 1$ est représenté par $(1, -0.5, 0, 3)$.
- le constructeur prend en argument la séquence de coefficients.
- si `p`{.language-} est une instance de `Polynome`{.language-}
  - `p.calcule_degré()`{.language-} renvoie le degré du polynôme
  - `p.evalue(x)`{.language-} renvoie la valeur du polynôme en `x`{.language-} (un flottant).
  - `str(p)`{.language-} renvoie une chaîne de caractères du style `3 X ** 3 -0.5 X + 1`{.language-}.
  - `p.derive()`{.language-} renvoie un nouveau polynôme correspondant à la dérivée de `p`{.language-}.
  - `p + q`{.language-} renvoie un nouveau polynôme correspondant à la somme de `p`{.language-} et d'une autre instance `q`{.language-} de `Polynome`{.language-}.
  - `p * q`{.language-} renvoie un nouveau polynôme correspondant au produit de `p`{.language-} et d'une autre instance `q`{.language-} de `Polynome`{.language-}.

On aimerait aussi créer une classe `FractionRationnelle`{.language-} représentant des bestioles de la forme $R(X) = \frac{P(X)}{Q(X)}$ où $P$ et $Q$ sont deux polynômes ($Q\neq 0$).

### Question 1

Faites un diagramme UML avec les classes `Polynome`{.language-} et `FractionRationnelle`{.language-}, et la relation entre ces classes. Pour `FractionRationnelle`{.language-}, vous ferez apparaître deux méthodes issues de votre imagination (inutile de donner des explications, le diagramme UML est suffisamment explicite).

### Question 2

Pourquoi vaut-il mieux utiliser un tuple plutôt qu'une liste pour stocker les coefficients d'un polynôme ?

### Question 3

Donnez le code de la classe `Polynome`{.language-} avec uniquement le constructeur et les méthodes `calcule_degré`{.language-}, `evalue`{.language-}.

### Question 4

Donnez le code d'une fonction de test pour chacune des méthodes précédentes.

### Question 5

Donnez le code de la classe `FractionRationnelle`{.language-} avec uniquement son constructeur.

### Question 6

Donnez le code des méthodes pour calculer la dérivée, la somme, le produit et la conversion en chaîne de caractères de polynômes.

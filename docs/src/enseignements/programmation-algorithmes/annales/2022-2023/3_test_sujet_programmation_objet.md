---
layout: layout/post.njk

title:  "sujet Test 3 : programmation objet"
authors:
    - Valentin Emiya
    - François Brucker
---

Vous allez écrire une classe `Fraction`{.language-} utilisant les *méthodes spéciales* vues en cours.

{% info %}
Vous devez rendre un fichier markdown, mais rien ne vous empêche de coder en python dans un fichier annexe pour vérifier que votre code est juste.
{% endinfo %}

Les objets de la classe `Fraction`{.language-} possèdent deux attributs : `numérateur`{.language-} et `dénominateur`{.language-} et représentent la fraction `numérateur / dénominateur`{.language-}.

## Question 1

Écrivez en python la classe `Fraction`{.language-} comprenant uniquement les deux attributs et un constructeur.

## Question 2

Ajoutez une méthode `Fraction.valeur()`{.language-} qui rend une approximation réelle de la valeur de la fraction (la division du `numérateur`{.language-} par le `dénominateur`{.language-}).

## Question 3

Ajoutez une méthode `réduit`{.language-} qui renvoie une fraction irréductible égale à la fraction. Pour cela, on pourra utiliser la fonction `math.gcd(a,b)`{.language-} qui renvoie le plus grand diviseur commun de a et b.

## Question 4

Écrivez le modèle UML de la classe `Fraction`{.language-}.

## Question 5

Afin de pouvoir utiliser nos fraction sans approximation, il serait pratique de pouvoir tester l'égalité de deux fractions. Redéfinissez la méthode `__eq__`{.language-} (l'égalité doit utiliser la méthode `Fraction.réduit()`{.language-}).

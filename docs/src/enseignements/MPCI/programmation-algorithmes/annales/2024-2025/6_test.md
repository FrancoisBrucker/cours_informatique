---
layout: layout/post.njk

title: "Sujet Test 6 : modélisation"
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

Vous devez modéliser un système de gestion des employés dans une entreprise, où chaque employé possède un nom, un poste et un salaire. Certains employés sont des managers qui supervisent une équipe constituée d'autres employés, ses subordonnés.

La classe de base est `Employé`{.language-}, et la classe `Manager`{.language-} hérite de cette classe. Les actions possibles sur un employé sont de retourner une description indiquant le le nom, le poste et le salaire (`__str__`{.language-}) et d'augmenter le salaire d'un certain pourcentage (`augmenter_salaire(pourcentage)`{.language-}). Avec un manager, il est possible d'ajouter un subordonné à son équipe (`ajouter_subordonné(un_employé)`{.language-}) et la description doit mentionner également le nombre de membres dans son équipe.

### Question 1

Faites un diagramme UML avec les classes `Employé`{.language-} et `Manager`{.language-}, et les relations entre ces classes.

### Question 2

Écrivez le code de ces classes, en veillant à bien utiliser `super()`{.language-}.

### Question 3

Écrivez une fonction `créer_employés()`{.language-} qui :

- crée d'un objet `Employé`{.language-} nommé "Paul", avec le poste "Développeur" et un salaire de 3000 euros;
- crée d'objet `Manager`{.language-} nommé "Marie", avec le poste "Chef de projet" et un salaire de 5000 euros;
- ajoute "Paul" comme subordonné de "Marie";
- affiche une description de chaque objet;
- renvoie les deux objets.

### Question 4

Écrivez les fonctions de tests suivant, qui appellent `créer_employés()`{.language-} dans un premier temps :

- une fonction qui teste si chaque objet est de la bonne classe ;
- une fonction qui teste les chaînes de caractères renvoyées par `__str__`{.language-} ;
- une fonction qui teste la taille de l'équipe de Marie, crée et ajoute un subordonné et teste à nouveau la taille de l'équipe ;
- une fonction qui augmente le salaire de chaque personne et vérifie le résultat.

### Question 5

Ajoutez une méthode qui vérifie qu'il n'y a pas de boucle dans le système hiérarchique: il suffira de vérifier qu'un manager ne peut pas se superviser lui-même, même avec plusieurs niveaux hiérarchiques de distance (on suppose que cette méthode sera ensuite appelée sur chaque manager).

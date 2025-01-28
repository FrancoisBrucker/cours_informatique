---
layout: layout/post.njk

title: "sujet Test 1 : code"
authors:
  - François Brucker
---

{% attention %}
Vous avez 15min pour faire le test.
{% endattention %}

Toute fonction écrite doit être testée :

{% note %}
Lorsque l'on vous demande d'**_écrire une fonction_**, cela **signifie** :

- écrire le code de la fonction
- écrire les tests qui vérifient son bon fonctionnement

{% endnote %}

Ce n'est pas grave si vous ne faites pas toutes les questions, mais si vous donnez une fonction sans ses tests ou qui ne fonctionne pas elle ne sera pas notée.

Enfin, faites aussi en sorte que votre code ait 0 défaut de style (le linter ne doit pas râler).

## Sujet

{% aller %}
[Pendu](/cours/coder-et-développer/projet-codes/#pendu){.interne}
{% endaller %}

## Barème

Une note sur 5 répartie comme suit :

1. sur 1 point (.5 pour le code et .5 pour les tests)
2. sur 1 point (.5 pour le code et .5 pour les tests)
3. sur 1 point (.5 pour le code et .5 pour les tests)
4. sur 1 point (.5 pour le code et .5 pour les tests)
5. sur 1 point

La note sur $20$ finale est obtenue en multipliant la note sur 5 par $6$

{% note "**Objectif du test**" %}

En 15 minutes :

- **un élève _normal_** doit parvenir à faire parfaitement les 2 premières questions. Ce qui lui permet d'avoir 2/5, soit 12/20
- **un bon élève** doit parvenir à réussir les 3 premières questions. Ce qui lui permet d'avoir 3/5 et donc 18/20
- **un très bon élève** fait plus que les 3 premières questions.
  {% endnote %}

La ventilation des notes est :

|note/5 | 0 | 0.5 | 1 | 1.25| 1.5 | 1.75 | 2 | 2.25 | 2.5 | 2.75 | 3 | 3.5 | 4 | 5 |
|note/20| 0 | 3 | 6 | 7.5 | 9 | 10.5 | 12| 13.5 | 15 | 16.5 | 18| 21 | 24| 30|
|-------|---|------|-----|-----|-----|------|---|------|-----|------|---|-----|---|---|
|nombre | 3 | 5 | 10 | 1 | 1 | 1 | 12| 1 | 1 | 1 | 4 | 1 | 1 | 1 |
|rang | 41| 36 | 26 | 25 | 24 | 23 | 11| 10 | 9 | 8 | 4 | 3 | 2 | 1 |
| # < | 0| 3 | 8 | 18 | 19 |20 | 21| 33 | 34 | 35 | 36| 40 | 41| 42|

- moyenne : 10.2/20 (1.7/5)
- écart-type : 6.57/20 (1.09/5)
- médiane : 12/20 (2/5)

{% attention %}
Beaucoup d'entres vous sont venus sans réelle préparation au test. Cela se ressent dans les notes (la moité des élèves ont moins de dix et un quart moins de six) !
{% endattention %}

Vous **devez** préparer chaque test pour obtenir une note correcte (12 ou plus). Le cours est en ligne, il y a des annales et les profs — très sympas — répondent à vos questions en direct ou par mail.

Outre le manque de préparation, j'ai vu beaucoup de code ou de tests qui ne s'exécutent manifestement pas. Votre code **doit** être exécutable sinon le correcteur peut penser que vous tentez de l'enfumer et ça le force à modifier votre code pour le faire fonctionner, en particulier pour lancer les tests (ce qui le rend irritable et moins enclin à être bienveillant).

Enfin, cela masque les fonctions ou les tests qui sont corrects !

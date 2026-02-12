---
layout: layout/post.njk

title: "sujet Test 3 : complexité"
authors:
  - François Brucker
---

## Barème

J'ai adopté la notation GEI pour les QCM lorsqu'il y a avait plusieurs réponses possibles : 

- chaque réponse fausse non cochée : 1pt/nombre de réponses possibles
- chaque réponse vraie cochée : 1pt/nombre de réponses possibles

C'est très gentil, voir trop gentil. Il est possible que cette notation ne soit pas conservée.

### Ventilation des points

La note du test est sur 6 points, 1pt par question.

La note sur $20$ finale est obtenue en multipliant la note sur 6 par $4$

{% note "**Objectif du test**" %}

En 15 minutes :

- **un élève moyen** fait les 3 premières question plus ou moins parfaitement, ce qui assure le 10
- **un bon élève** a écrit en plus un algorithme de dichotomie plus ou moins correct, ce qui fait monter la note à 14
- **un très bon élève** fait les 3 premières questions parfaitement et écrit un algorithme de dichotomie exacte.

{% endnote %}

### Ventilation des notes

|note/20  | < 10 | [10, 12]  | ]12, 14]  | ]14, 16] | ]16, 20[ |  20 |
|---------|------|---------|-------------|----------|----------|-----|
|nombre   |   1  |    15   |     7       |    11    |    6     | 1   |
|rang min |  42  |    38   |    24       |    16    |    6     | 1   | 

- moyenne : 13.1/20 (3.27/6)
- écart-type : 4.01/20 (1.01/6)
- médiane : 13.17/20 (3.29/6)

{% info %}
Seul 1 élève a en dessous de la moyenne pour absence non justifiée au test.
{% endinfo %}

Autrement, je suis encore une fois globalement satisfait de votre travail. Attention cependant aux définitions de la complexité, il y a quand même globalement quelques flottements... atténués par la notation très généreuse. Révisez donc tout de même cette partie car même si la base est apprise les fondations ne sont pas encore bien solide et [les chateaux fait de sable s'écroulent fatalement dans l'eau](https://www.youtube.com/watch?v=MpbBc30DbQw&list=PLNPGM2D7aODeeRDxgwwtnwZTAApuJznnu&index=9).

## Erreurs fréquemment rencontrées

### Complexité

Peut de personnes ont tous juste sur les 2 premières questions. Reprenez le cours pour comprendre où vous vous êtes trompés.

### Algorithme de la dichotomie

- Attention, si l'on peut supposer que $f(a)$ et $f(b)$ sont de signe contraire, rien ne dit que $f(a) <0$. Un test possible est de regarder le signe de $f(a) \cdot f((b-a)/2)$.
- Comme on rend le milieu de l'intervalle : le véritable zéro est au maximum différent de $(b-a)2^{n+1}$ de celui rendu.
- le $\epsilon$ correspond à l'erreur sur $x$, pas sa valeur $f(x)$ par rapport à 0. 

## Corrigé

{% lien %}
[corrigé](../3_test_corrigé.pdf){.interne}
{% endlien %}
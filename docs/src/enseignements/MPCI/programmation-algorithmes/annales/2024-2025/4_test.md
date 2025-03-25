---
layout: layout/post.njk

title: "sujet Test 4 : tris"
---

{% attention %}
Vous avez 15min pour faire le test.
{% endattention %}

## Rendu

### Type de rendu

Rendu sur feuille.

### Éléments de notation

1. Écriture sous la forme d'un pseudo-code correct
2. Lorsque l'on vous demande de donner un algorithme il faudra toujours, en plus de son pseudo-code, prouver :
   - sa finitude
   - son exactitude

Ne tartinez pas des pages et des pages de démonstration. Allez directement au fait et si c'est évident, dites le.

## Sujet

### 1 Complexités

#### 1.1

Quelle est la complexité du problème du tri ? Vous justifierez votre réponse en :

- donnant un minorant de cette complexité
- donnant un majorant de cette complexité (avec un nom d'algorithme du cours ayant cette complexité)

#### 1.2

Donnez une définition (rapide) de la complexité en moyenne d'un algorithme. Pour quels sorte d'algorithme est-elle utile et comment la calculer en pratique ?

### 2 Algorithme

```pseudocode
algorithme tri(T: [entier]):
   i ← 1
   tant que i < T.longueur:
      si T[i - 1] ≤ T[i]:
         i ← i + 1
      sinon:
         T[i], T[i - 1] ← T[i - 1], T[i]
         i ← max(1, i - 1)
```

#### 2.1

Démontrez que l'algorithme précédent est un algorithme de tri.

#### 2.2

##### 2.2.1

Donnez (et justifiez) la complexité de l'algorithme ?

##### 2.2.2

Donnez (et justifiez) la complexité minimale de l'algorithme ?

##### 2.2.3

Donnez (et justifiez) la complexité en moyenne de l'algorithme ? N'oubliez pas de donner le modèle de données utilisé pour calculer votre réponse.

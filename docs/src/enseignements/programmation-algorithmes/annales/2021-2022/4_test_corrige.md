---
layout: layout/post.njk

title:  "Corrigé Test 4 : classes et objets"
authors:
    - François Brucker
---

## 1

```text
-------------------------
|  Morceau              |
-------------------------
| titre: str            |
| durée: float          |
-------------------------
| __init__(titre, durée)|
-------------------------
```

Sans informations complémentaires, la classe n'a besoin que d'un constructeur qui va placer les attributs.

## 2

```python
fatal_picart = Morceau("cure toujours", 2.52)
```

{% attention %}
Votre déclaration doit être conforme à votre UML.
{% endattention %}

## 3

```text
-----------------------------------
| Playlist                        |
-----------------------------------
| morceaux : list de Morceau      |
-----------------------------------
| __init__(liste: list de Morceau)|
-----------------------------------
```

Les `Morceau`{.language-} étant donné à la construction de l'objet, c'est un lien d'**agrégation** (la `Playlist`{.language-} ne crée pas les `Morceau`{.language-})

## 4

Une playlist devrait pouvoir lire un morceau aléatoire et ajouter/supprimer un morceau de la playlist

## 5

```text
-----------------------------------
| Playlist                        |
-----------------------------------
| morceaux : list de Morceau      |
| piste_lecture                   |
-----------------------------------
| __init__(liste: list de Morceau)|
| lire_aléatoire()                |
| ajout_morceau(Morceau)           |
| supprime_morceau(Morceau)        |
-----------------------------------
```

## 6

* on crée une liste initialement vite, on ajoute un morceau et on vérifie qu'il est présent
* on crée une liste avec un morceau, on le supprime et on vérifie qu'il n'y est plus
* on crée une liste avec un morceau, on demande de lire u morceau aléatoire, et on vérifie que c'est lui.
Proposez des tests unitaires permettant de vérifier qu'une des fonctionnalités que vous avez ajoutées est correcte.

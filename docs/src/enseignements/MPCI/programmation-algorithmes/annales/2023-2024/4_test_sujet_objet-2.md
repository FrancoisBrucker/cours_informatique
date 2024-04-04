---
layout: layout/post.njk

title: "sujet Test 4 : Programmation objet 2"
---


## 1.

Écrivez dans un fichier undo.py la classe `UndoRedo`{.language-} telle que :
l'initialisation prend deux paramètres : une liste `l`{.language-} et un objet `x`{.language-}.
la classe contient deux méthodes :
`supprime()`{.language-} qui ne prend pas de paramètre et supprime le dernier élément de `l`{.language-} s'il vaut `x`{.language-}
 `remet()`{.language-} qui ne prend pas de paramètre et place `x`{.language-} comme dernier élément de la liste.
Vous pourrez utiliser le fait que si `l` est une liste en python :
`l.pop()`{.language-} supprime le dernier élément de `l`{.language-} et le rend.
`l[-1]`{.language-} rend le dernier élément de la liste `l`{.language-}.

## 2.

En sachant que `randint(1, 10)`{.language-} rend un entier aléatoire entre 1 et 10 détaillez avec des commentaires ce que fait le code suivant, que vous placerez dans un fichier `main.py`{.fichier} :

```python

from random import randint

l = []
for x in range(10):
   l.append(randint(1, 10))
print(l)

sauve = []
while len(l) > 0:
   undo_redo = UndoRedo(l, l[-1])
   undo_redo.supprime()
   sauve.append(undo_redo)

print(l)

while len(sauve) > 0:
   undo_redo = sauve.pop()
   undo_redo.remet()

print(l)

```

## 3.


Faites dans le fichier `undo.py`{.language-} un héritage de la classe `list `{.language-} de python qui possède, outre toutes les méthodes de listes, la méthode `depop()`{.language-} qui permet d’annuler la dernière méthode `pop`{.language-} utilisée.


---
layout: layout/post.njk

title: "Corrigé Test 4 : Programmation objet 2"
---


## 1.

```python
class UndoRedo:
    def __init__(self, l, x):
        self.l = l
        self.x = x

    def supprime(self):
        if self.l[-1] == self.x:
            self.l.pop()

    def remet(self):
        self.l.append(self.x)
```

## 2.

> TBD

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

```python
class MaListe(list):
    def __init__(self):
        super().__init__()
        self.stock = None

    def pop(self):
        self.stock = UndoRedo(self, self[-1])
        return super().pop()

    def depop(self):
        if self.stock is not None:
            self.stock.remet()
            self.stock = None

l = MaListe()

l.append(42)
print(l)
l.pop()
print(l)
l.depop()
print(l)
```

Ce n'est pas parfait car si on fait deux `pop`{.language-} de suite cela ne marche plus, mais c'est un début.


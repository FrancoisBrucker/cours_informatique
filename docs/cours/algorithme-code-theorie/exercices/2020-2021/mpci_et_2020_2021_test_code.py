class UndoRedo:
    def __init__(self, l, x):
        self.l = l
        self.x = x
    def supprime(self):
        if self.l[-1] == self.x:
            self.l.pop()
    def remet(self):
        self.l.append(self.x)

from random import randint

l = [] 
for x in range(10):
  l.append(randint(1, 10))

sauve = []

print(l)

while len(l) > 0:
  undo_redo = UndoRedo(l, l[-1])
  undo_redo.supprime()
  sauve.append(undo_redo)

print(l)

while len(sauve) > 0:
  undo_redo = sauve.pop()
  undo_redo.remet()

print(l)
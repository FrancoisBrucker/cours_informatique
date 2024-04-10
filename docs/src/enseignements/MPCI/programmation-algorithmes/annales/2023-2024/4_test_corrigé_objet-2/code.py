class UndoRedo:
    def __init__(self, l, x):
        self.l = l
        self.x = x

    def supprime(self):
        if self.l[-1] == self.x:
            self.l.pop()

    def remet(self):
        self.l.append(self.x)


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

from dé import Dé, MementoDé

dé = Dé()
print(dé)
memento = MementoDé(dé)
dé.lancer()
print(dé)
memento.restore()
print(dé)

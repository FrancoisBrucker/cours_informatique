from dé import TapisVert, MementoTapisVert

tapis = TapisVert()
memento_liste = []

print("0 :", tapis)
for i in range(1, 10):
    memento_liste.append(MementoTapisVert(tapis))
    tapis.lancer()
    print(i, ":", tapis)

for _ in range(len(memento_liste)):
    memento_liste.pop().restore()
    print(len(memento_liste), ":", tapis)

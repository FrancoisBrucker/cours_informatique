from dé import TapisVert

tapis_vert = TapisVert()

tapis_vert.lancer()

for dé in tapis_vert.dés:
    print(dé.position)
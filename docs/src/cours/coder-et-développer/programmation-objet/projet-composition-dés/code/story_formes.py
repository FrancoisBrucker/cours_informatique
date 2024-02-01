from dé import TapisVert

tapis_vert = TapisVert()

while True:

    tapis_vert.lancer()
    print(tapis_vert)
    if tapis_vert.possède_paire():
        print("  A une paire")
    if tapis_vert.possède_brelan():
        print("  A un brelan")
    if tapis_vert.possède_carré():
        print("  A un carré")

    entrée = input("Appuyez sur la touche <entrée> pour recommencer")

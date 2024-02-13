from fonctions import donne_prochain_indice, compte_caractère, donne_max_doublon

chaine_entrée = ""

while chaine_entrée != "sortie":
    chaine_entrée = input("Entre une chaine de caractères : ")
    caractère_entrée = input("Entre un caractère : ")

    index_caractère = chaine_entrée.find(caractère_entrée)
    print("Premier index du caractère :", index_caractère)

    if index_caractère == -1:
        print("Il n'apparait pas")
    elif donne_prochain_indice(chaine_entrée, index_caractère) != None:
        print("Il apparait plusieurs fois")
    else:
        print("Il apparait une fois")

    if index_caractère > -1:
        print("caractère apparait", compte_caractère(chaine_entrée, index_caractère), "fois.")

        if index_caractère == donne_max_doublon(chaine_entrée):
            print("c'est le max !")


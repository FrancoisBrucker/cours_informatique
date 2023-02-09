from pendu import caché, est_une_lettre, découvre, caractères


mot_à_trouver = "table"
mot_caché = caché(mot_à_trouver)


print("mot à trouver :", mot_caché)
nombre_essai = 0

while est_une_lettre(".", mot_caché):
    lettre = input("Donnez une lettre : ")
    mot_caché = découvre(mot_caché, lettre, caractères(lettre, mot_à_trouver))
    print("mot à trouver :", mot_caché)

    nombre_essai += 1

print("Victoire !, vous avez gagné en", nombre_essai, "essais.")

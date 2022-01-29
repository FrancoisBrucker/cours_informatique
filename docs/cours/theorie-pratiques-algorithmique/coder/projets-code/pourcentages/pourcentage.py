def pourcent(chaîne_de_caractères):
    nombre_de_0 = 0

    for c in chaîne_de_caractères:
        if c == "0":
            nombre_de_0 += 1

    return 100 * (nombre_de_0 / len(chaîne_de_caractères))

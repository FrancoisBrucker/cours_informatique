def pourcent(chaîne_de_caractères):
    nombre_de_0 = chaîne_de_caractères.count('0')

    if len(chaîne_de_caractères):
        return nombre_de_0 / len(chaîne_de_caractères)
    else:
        return 0


def non_lue():
    pass

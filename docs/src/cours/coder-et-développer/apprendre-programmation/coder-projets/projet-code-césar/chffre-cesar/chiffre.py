ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def césar_chiffre(texte_clair, cle):

    décalage = ALPHABET.index(cle)
    texteCesar = ""
    for x in texte_clair:
        if x in ALPHABET:
            texteCesar += ALPHABET[(ALPHABET.index(x) + décalage) % 26]
        else:
            texteCesar += x

    return texteCesar


def césar_déchiffre(texte_chiffré, cle):

    décalage = ALPHABET.index(cle)
    texteCesar = ""
    for x in texte_chiffré:
        if x in ALPHABET:
            texteCesar += ALPHABET[(ALPHABET.index(x) - décalage) % 26]
        else:
            texteCesar += x

    return texteCesar

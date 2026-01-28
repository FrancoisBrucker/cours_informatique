ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def césar_chiffre(texte, cle):

    décalage = ALPHABET.index(cle)
    texteCesar = ""
    for x in texte:
        if x in ALPHABET:
            texteCesar += ALPHABET[(ALPHABET.index(x) + décalage) % 26]
        else:
            texteCesar += x

    return texteCesar


def césar_déchiffre(texte, cle):

    décalage = ALPHABET.index(cle)
    texteCesar = ""
    for x in texte:
        if x in ALPHABET:
            texteCesar += ALPHABET[(ALPHABET.index(x) - décalage) % 26]
        else:
            texteCesar += x

    return texteCesar
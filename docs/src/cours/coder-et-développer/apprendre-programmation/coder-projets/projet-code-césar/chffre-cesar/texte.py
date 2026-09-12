import unicodedata


def conversion(texte_avec_accent):
    liste_glyphes_unicode = list(unicodedata.normalize("NFKD", texte_avec_accent))

    liste_caractères = []
    for c in liste_glyphes_unicode:
        if not unicodedata.combining(c):
            liste_caractères.append(c)
    
    chaîne_sans_accent = "".join(liste_caractères)
    texte_en_majuscule = chaîne_sans_accent.upper()

    return texte_en_majuscule

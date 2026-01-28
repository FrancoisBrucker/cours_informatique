import unicodedata

def conversion(texte_avec_accent):
    liste_caractères_unicode = list(unicodedata.normalize('NFKD', texte_avec_accent))
    
    liste_caractères_simple = []
    for c in liste_caractères_unicode:
        if not unicodedata.combining(c):
            liste_caractères_simple.append(c)
        
    chaîne_sans_accent = ''.join(liste_caractères_simple)
    texte_en_majuscule = chaîne_sans_accent.upper()
    
    return texte_en_majuscule

def nombre(chaîne):
    somme = 0
    for s in chaîne:
        somme += ord(s)
    return somme


def somme_digit(nombre):
    somme = 0
    for c in str(nombre):
        somme += int(c)

    return somme


def chiffre_associe(chaîne):
    chiffre = nombre(chaîne)
    
    while (chiffre > 9):
        chiffre = somme_digit(chiffre)

    return chiffre

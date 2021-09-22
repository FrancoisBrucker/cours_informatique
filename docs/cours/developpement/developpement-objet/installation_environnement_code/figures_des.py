def contient_une_paire(cinq_des):
    return len(set(cinq_des)) < len(cinq_des)


def compte_valeur(cinq_des):
    compte = dict()

    for valeur_de in cinq_des:
        if valeur_de not in compte:
            compte[valeur_de] = 0
        compte[valeur_de] += 1

    return compte


def contient_un_brelan(cinq_des):
    compte = compte_valeur(cinq_des)

    nombre_brelan = 0
    for nombre in compte.values():
        if nombre > 2:
            nombre_brelan += 1
    return nombre_brelan > 0


def contient_un_carre(cinq_des):
    compte = compte_valeur(cinq_des)

    nombre_carre = 0
    for nombre in compte.values():
        if nombre > 3:
            nombre_carre += 1
    return nombre_carre > 0


def contient_une_double_paire(cinq_des):
    compte = compte_valeur(cinq_des)

    nombre_paires = 0
    for nombre in compte.values():
        if nombre > 1:
            nombre_paires += 1
    return nombre_paires > 1


def contient_un_full(cinq_des):
    compte = compte_valeur(cinq_des)

    nombre_paires = 0
    nombre_brelan = 0
    for nombre in compte.values():
        if nombre > 2:
            nombre_brelan += 1
        elif nombre > 1:
            nombre_paires += 1

    return (nombre_paires >= 1 and nombre_brelan >= 1) or (nombre_brelan > 1)

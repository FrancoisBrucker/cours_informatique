def est_une_lettre(lettre, mot):
    return lettre in mot


def test_est_une_lettre_oui():
    assert est_une_lettre("i", "victoire")


def test_est_une_lettre_non():
    assert not est_une_lettre("e", "la disparition")


def caractères(lettre, mot):
    position = []

    for i in range(len(mot)):
        if mot[i] == lettre:
            position.append(i)

    return position


def test_caractères_des_positions():
    assert [1, 5] == caractères("i", "victoire")


def test_caractères_des_positions_pas_de_position():
    assert [] == caractères("e", "la disparition")


def découvre(mot_caché, lettre, positions):
    mot = ""

    if len(positions) == 0:
        return mot_caché

    pos = 0
    for i in range(len(mot_caché)):
        if i == positions[pos]:
            mot += lettre
            pos = min(pos + 1, len(positions) - 1)
        else:
            mot += mot_caché[i]

    return mot

def test_découvre():
    assert ".rr..r" == découvre("......", "r", [1, 2, 5])
    assert "erreur" == découvre("erre.r", "u", [4])
    assert "erre.r" == découvre("erre.r", "u", [])

def découvre_alternatif(mot_caché, lettre, positions):
    """ de complexité un peu moins bonne que découvre, mais plus facile 
        à écrire.
    """
    mot = ""

    if len(positions) == 0:
        return mot_caché

    for i in range(len(mot_caché)):

        if i in positions:
            mot += lettre
        else:
            mot += mot_caché[i]

    return mot


def test_découvre_alternatif():
    assert ".rr..r" == découvre_alternatif("......", "r", [1, 2, 5])
    assert "erreur" == découvre_alternatif("erre.r", "u", [4])
    assert "erre.r" == découvre_alternatif("erre.r", "u", [])


def caché(mot):
    return "." * len(mot)


def test_caché_rien():
    assert "" == caché("")


def test_caché_des_lettres():
    assert "........................." == caché("anticonstitutionnellement")


if __name__ == "__main__":
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

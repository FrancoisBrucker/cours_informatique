from math import factorial

from voyageur import pays, europe, draw, draw_chemin, glouton, fonction_objectif, d, passe_globale


def dessine_pays():
    draw(pays)
    draw(europe, size=10)


def dessine_glouton(pays, size=20):
    chemin = glouton(pays)
    draw_chemin(pays, chemin, size)
    print(chemin)
    print("distance :", fonction_objectif(chemin))


def iteration_glouton(pays, nombre_essai=20):
    chemin = glouton(pays)
    nb_amélioration = 0
    for essai in range(nombre_essai):
        chemin_possible = glouton(pays)

        if fonction_objectif(chemin_possible) < fonction_objectif(chemin):
            print(
                "Iteration :",
                essai + 1,
                "^",
                fonction_objectif(chemin),
                ">",
                fonction_objectif(chemin_possible),
            )
            chemin = chemin_possible
            nb_amélioration += 1
        else:
            print(
                "Iteration :",
                essai + 1,
                "v",
                fonction_objectif(chemin),
                "≤",
                fonction_objectif(chemin_possible),
            )

    print("Nombre d'améliorations :", nb_amélioration)


def deux_opt_final(chemin):
    opt = True
    while opt:
        opt = False
        f = fonction_objectif(chemin)
        chemin = passe_globale(chemin)

        if f > fonction_objectif(chemin):
            opt = True

    return chemin


if __name__ == "__main__":

    print(
        "Nombre de possibilités de voyages pour",
        len(pays),
        "pays :",
        factorial(len(pays) - 1) // 2,
    )

    print(
        "Nombre de possibilités de voyages pour",
        len(pays),
        "pays :",
        factorial(len(pays) - 1) // 2,
    )

    list_pays = list(pays)
    dist_pays = []
    for i in range(len(list_pays)):
        for j in range(i + 1, len(list_pays)):
            dist_pays.append(d(list_pays[i], list_pays[j]))

    print("min : ", min(dist_pays))
    print("max : ", max(dist_pays))
    print("moyenne : ", sum(dist_pays) / len(dist_pays))

    dessine_pays()
    dessine_glouton(pays)
    dessine_glouton(europe, 13)

    iteration_glouton(europe)

    chemin = glouton(europe)
    draw_chemin(europe, chemin, 13)
    print("fonction objectif avant 2-opt final :", fonction_objectif(chemin))

    chemin = deux_opt_final(chemin)
    draw_chemin(europe, chemin, 13)
    print("fonction objectif après 2-opt final :", fonction_objectif(chemin))

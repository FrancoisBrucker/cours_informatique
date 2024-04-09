def rendu(R, pieces=(1, 2, 5)):
    pieces = list(pieces)
    pieces.sort()
    pieces.reverse()

    rendu = []
    for v in pieces:
        p = R // v        
        R -= p * v

        rendu.append((v, p))
    
    return rendu

def test_rendu():
    assert [(5, 2), (2, 1), (1, 1)] == rendu(13, (1, 2, 5))


def nombre_films_maximal(films):

    films.sort(key=lambda x: x[1])

    films_a_voir = [films[0]]
    for film in films:
        fin_dernier_film = films_a_voir[-1][1]
        début_nouveau_film = film[0]
        if fin_dernier_film <= début_nouveau_film:
            films_a_voir.append(film)

    return films_a_voir

def nombre_salles(films):
    films.sort(key=lambda x: x[0])

    salles = [[films[0]]]
    for film in films[1:]:
        nouvelle_salle = True
        for salle in salles:
            dernier_film = salle[-1]
            if film[0] >= dernier_film[1]:
                salle.append(film)
                nouvelle_salle = False
                break
        if nouvelle_salle:
            salles.append([film])

    return salles

def test_nombre_salles():
    assert [[(1, 3), (4, 6)], [(2, 5)]] == nombre_salles([(1, 3), (4,6), (2, 5)])


def produits_est_compatible(liste_produit):
    liste_produit.sort(key=lambda x: x[0])

    for date, produit in enumerate(liste_produit):
        if date + 1 > produit[0]:
            return False
    return True

def produits_maximum_profit(liste_produit):
    liste_produit.sort(key=lambda x : x[1])
    liste_produit.reverse()

    ensemble_max = []
    for produit in liste_produit:
        test = ensemble_max + [produit]

        if produits_est_compatible(test):
            ensemble_max.append(produit)
    
    return ensemble_max


def test_produits_est_compatible():
    assert produits_est_compatible([[1, 10]])
    assert produits_est_compatible([[5, 10], [1, 12]])
    assert produits_est_compatible([[1, 10], [1, 2]]) == False
    assert produits_est_compatible([[1, 10], [2, 12], [4, 2], [5, 2], [5, 2]])
    assert produits_est_compatible([[1, 10], [2, 12], [3, 3], [4, 2], [5, 2], [5, 2]]) == False


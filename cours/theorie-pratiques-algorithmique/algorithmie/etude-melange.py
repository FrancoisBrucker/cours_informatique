from random import randint
import matplotlib.pyplot as plt


def permutations(elements):
    if len(elements) == 0:
        return [[]]

    les_permutations = []
    for i in range(len(elements)):
        premier = elements[i]
        elements_sans_premier = elements[:i] + elements[i + 1:]
        permutations_sans_premier = permutations(elements_sans_premier)
        for une_fin_de_permutation in permutations_sans_premier:
            permutation = [premier] + une_fin_de_permutation
            les_permutations.append(permutation)
    return les_permutations


def test_permutation_vide():
    assert [[]] == permutations([])


def test_permutation_singleton():
    assert [[1]] == permutations([1])


def test_permutation_trois():
    assert [[1, 3, 2], [1, 2, 3], [3, 1, 2], [3, 2, 1], [2, 1, 3], [2, 3, 1]] == permutations([1, 3, 2])


def melange(elements):
    P = permutations(elements)
    i = randint(0, len(P) - 1)
    return P[i]


def melange_knuth(elements):
    copie_elements = list(elements)
    for i in range(len(copie_elements) - 1, -1, -1):
        j = randint(0, i)
        copie_elements[i], copie_elements[j] = copie_elements[j], copie_elements[i]
    return copie_elements


def melange_transposition(elements):
    copie_elements = list(elements)
    for k in range(len(copie_elements) - 1):
        i = randint(0, len(copie_elements) - 1)
        j = randint(0, len(copie_elements) - 1)

        copie_elements[i], copie_elements[j] = copie_elements[j], copie_elements[i]
    return copie_elements


def draw():
    NOMBRE_ITERATION = 100000
    TABLEAU = [1, 2, 3, 4, 5, 6]
    PERMUTATIONS = [x for x in permutations(TABLEAU)]

    compte = [0] * len(PERMUTATIONS)

    for k in range(NOMBRE_ITERATION):
        # res = melange_knuth(TABLEAU)
        res = melange_transposition(TABLEAU)

        for i in range(len(PERMUTATIONS)):
            if PERMUTATIONS[i] == res:
                compte[i] += 1
                break

    fig, ax = plt.subplots(figsize=(20, 5))

    ax.set_xlim(-1, len(PERMUTATIONS) - 1)

    ax.plot(compte, label="knuth")
    ax.axhline(y=NOMBRE_ITERATION / len(PERMUTATIONS), color="red", label="théorique")

    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_title("nombre de permutations")

    plt.show()

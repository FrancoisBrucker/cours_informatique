def insertion(tableau):
    for i in range(1, len(tableau)):
        courant = tableau[i]
        j = i
        while (j > 0) and (courant < tableau[j - 1]):
            tableau[j] = tableau[j - 1]
            j -= 1
        tableau[j] = courant


def selection(tableau):
    for i in range(len(tableau) - 1):
        min_index = i
        for j in range(i + 1, len(tableau)):
            if tableau[j] < tableau[min_index]:
                min_index = j
        tableau[i], tableau[min_index] = tableau[min_index], tableau[i]


def colle(tab1, tab2):
    i1 = i2 = 0
    tab_colle = []
    while i1 < len(tab1) or i2 < len(tab2):
        if i2 == len(tab2):
            tab_colle.append(tab1[i1])
            i1 += 1
        elif i1 == len(tab1):
            tab_colle.append(tab2[i2])
            i2 += 1
        elif tab1[i1] < tab2[i2]:
            tab_colle.append(tab1[i1])
            i1 += 1
        else:
            tab_colle.append(tab2[i2])
            i2 += 1
    return tab_colle


def fusion(tableau):
    if len(tableau) < 2:
        return tableau
    else:
        milieu = len(tableau) // 2
    return colle(fusion(tableau[:milieu]), fusion(tableau[milieu:]))


def rapide(tableau):
    if len(tableau) <= 1:
        return tableau

    pivot = tableau[0]

    tab_gauche = [tableau[i] for i in range(1, len(tableau)) if tableau[i] <= pivot]
    tab_droite = [tableau[i] for i in range(1, len(tableau)) if tableau[i] > pivot]

    return rapide(tab_gauche) + [pivot] + rapide(tab_droite)

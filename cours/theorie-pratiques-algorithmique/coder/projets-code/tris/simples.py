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


t = [1, 3, 2, 6, 4, 5, 0]
selection(t)
print(t)


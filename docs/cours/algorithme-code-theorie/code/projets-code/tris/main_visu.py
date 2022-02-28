import random

import matplotlib.pyplot as plt


def draw_tab(tab):
    ax.cla()  # on efface le dessin
    ax.plot(tab, 'ro')
    plt.pause(0.1)  # on pause le dessin


def insertion(tableau):
    for i in range(1, len(tableau)):
        courant = tableau[i]
        j = i
        while (j > 0) and (courant < tableau[j - 1]):
            tableau[j] = tableau[j - 1]
            tableau[j - 1] = courant
            j -= 1

            draw_tab(tab)  # on affiche le tableau


def selection(tableau):
    for i in range(len(tableau) - 1):
        min_index = i
        for j in range(i + 1, len(tableau)):
            if tableau[j] < tableau[min_index]:
                min_index = j
        tableau[i], tableau[min_index] = tableau[min_index], tableau[i]
        draw_tab(tab)  # on affiche le tableau


def bulles(tableau):
    on_continue = True
    n = len(tableau)
    while on_continue:
        on_continue = False
        for i in range(1, n):
            if tableau[i - 1] > tableau[i]:
                on_continue = True
                tableau[i - 1], tableau[i] = tableau[i], tableau[i - 1]
                draw_tab(tab)


fig, ax = plt.subplots(figsize=(20, 5))

tab = list(range(30))
random.shuffle(tab)

print(tab)

ax.plot(tab, 'ro')
insertion(tab)

print(tab)

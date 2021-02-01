import random

import matplotlib.pyplot as plt


def draw_tab(tab):
    plt.plot(tab, 'ro')
    plt.pause(0.1)
    plt.cla()


def selection(tab):
    for i in range(len(tab) - 1):
        min_index = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[min_index]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]
        draw_tab(tab)


def insertion(tab):
    for i in range(1, len(tab)):
        actu = tab[i]
        j = i
        while j > 0 and tab[j - 1] > actu:
            tab[j] = tab[j - 1]
            draw_tab(tab)
            j -= 1
        tab[j] = actu
        draw_tab(tab)


tab = list(range(30))
random.shuffle(tab)

print(tab)
plt.plot(tab, 'ro')
# selection(tab)
insertion(tab)
plt.show()

print(tab)

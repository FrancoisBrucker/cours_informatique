import random

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()


def draw_tab(tab):
    ax.cla()  # on efface le dessin
    ax.plot(tab, 'ro')
    plt.pause(0.1)  # on pause le dessin


def insertion_visu(T):
    for i in range(1, len(T)):
        courant = T[i]
        j = i
        while (j > 0) and (courant < T[j - 1]):
            T[j] = T[j - 1]
            draw_tab(T)  # on affiche le tableau

            j -= 1
        T[j] = courant
        draw_tab(T)
    draw_tab(tab)


def sélection_visu(T):
    for i in range(len(T) - 1):
        min_index = i
        for j in range(i + 1, len(T)):
            if T[j] < T[min_index]:
                min_index = j
        T[i], T[min_index] = T[min_index], T[i]
        draw_tab(T)
    draw_tab(tab)

def bulles_visu(T):
    for i in range(len(T) - 1, 0, -1):
        trié = True
        for j in range(i):
            if T[j + 1] < T[j]:
                T[j + 1], T[j] = T[j], T[j + 1]
                trié = False

                draw_tab(T)
        if trié:
            return
    draw_tab(tab)

fig, ax = plt.subplots(figsize=(20, 5))

tab = list(range(30))
random.shuffle(tab)

print(tab)  

ax.plot(tab, 'ro')

insertion_visu(list(tab))
sélection_visu(list(tab))
bulles_visu(list(tab))

draw_tab(tab)

print(tab)
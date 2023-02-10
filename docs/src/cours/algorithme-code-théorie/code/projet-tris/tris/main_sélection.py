import time
import matplotlib.pyplot as plt


def sélection(T):
    for i in range(len(T) - 1):
        min_index = i
        for j in range(i + 1, len(T)):
            if T[j] < T[min_index]:
                min_index = j
        T[i], T[min_index] = T[min_index], T[i]


def temps_sélection(T):
    t1 = time.perf_counter()
    sélection(T)
    t2 = time.perf_counter()

    delta = t2 - t1

    return delta


def tableau_max_sélection(n):
    return list(range(n))


def temps_max_sélection(d):
    n = 1
    T = tableau_max_sélection(n)
    delta = temps_sélection(T)

    while delta < d:
        n = 2 * n
        T = tableau_max_sélection(n)
        delta = temps_sélection(T)

    return n


d = 1
n = temps_max_sélection(d)
x = list(range(1, n, n // 20))

print("n =", n, " pour d =", d, " seconde ; len(x) =", len(x))

t1 = time.perf_counter()
y = [temps_sélection(tableau_max_sélection(i)) for i in x]
t2 = time.perf_counter()
print("temps total de calcul : ", t2 - t1, " secondes.")

fig, ax = plt.subplots(figsize=(20, 5))
ax.set_title("complexité du tri par selection")

ax.plot(x, y)

plt.show()

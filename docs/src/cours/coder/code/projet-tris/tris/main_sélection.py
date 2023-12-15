import time
import matplotlib.pyplot as plt

from tris import sélection
from mesure import temps_sélection


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
tailles = list(range(1, n, n // 20))

print("n =", n, " pour d =", d, " seconde ; len(x) =", len(tailles))

t1 = time.perf_counter()
temps_max = [temps_sélection(tableau_max_sélection(i)) for i in tailles]
t2 = time.perf_counter()
print("temps total de calcul : ", t2 - t1, " secondes.")

fig, ax = plt.subplots(figsize=(20, 5))
ax.set_title("complexité du tri par selection")

ax.plot(tailles, temps_max)

plt.show()

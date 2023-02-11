import time
import matplotlib.pyplot as plt

from tris import insertion
from mesure import temps_insertion, temps_insertion_moyen


def tableau_min_insertion(n):
    return list(range(n))


def tableau_max_insertion(n):
    return list(reversed(range(n)))


n = 8192  # identique tri par sélection
tailles = list(range(1, n, n // 20))


t1 = time.perf_counter()
temps_max = [temps_insertion(tableau_max_insertion(i)) for i in tailles]
t2 = time.perf_counter()

print("temps total de calcul max : ", t2 - t1, " secondes.")

t1 = time.perf_counter()
temps_min = [temps_insertion(tableau_min_insertion(i)) for i in tailles]
t2 = time.perf_counter()

print("temps total de calcul min : ", t2 - t1, " secondes.")

t1 = time.perf_counter()
temps_moyen = [temps_insertion_moyen(i) for i in tailles]
t2 = time.perf_counter()

print("temps total de calcul moyen : ", t2 - t1, " secondes.")

fig, ax = plt.subplots(figsize=(20, 5))
ax.set_title("complexité du tri par insertion")

ax.plot(tailles, temps_max)
ax.plot(tailles, temps_min)
ax.plot(tailles, temps_moyen)

ax.set_xlim(800, 1200)
ax.set_ylim(0, 0.04)

plt.show()
# plt.savefig("graphique.pdf", format="pdf", bbox_inches='tight')
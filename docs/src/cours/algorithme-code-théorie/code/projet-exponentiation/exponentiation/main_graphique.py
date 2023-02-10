import time
import matplotlib.pyplot as plt
from exponentiation import puissance_naif, puissance_rapide


NOMBRE = 3
MAX = 100000
PAS = 1000

exposant = []
temps_naif = []
temps_rapide = []

for x in range(0, MAX, PAS):
    exposant.append(x)

    t1 = time.perf_counter()
    puissance_naif(NOMBRE, x)
    t2 = time.perf_counter()
    delta = t2 - t1
    temps_naif.append(delta)

    t1 = time.perf_counter()
    puissance_rapide(NOMBRE, x)
    t2 = time.perf_counter()
    delta = t2 - t1
    temps_rapide.append(delta)

fig, ax = plt.subplots(figsize=(20, 5))

ax.set_xlim(0, MAX)
ax.set_ylim(0, max(temps_rapide[-1], temps_naif[-1]))

ax.set_title("complexités temporelles")


ax.plot(exposant, temps_naif)
ax.plot(exposant, temps_rapide)

plt.show()

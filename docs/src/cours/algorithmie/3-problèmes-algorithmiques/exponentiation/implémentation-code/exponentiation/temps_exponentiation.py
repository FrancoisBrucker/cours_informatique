import time

import matplotlib.pyplot as plt

from exponentiation import puissance_naif, puissance_rapide

temps = 1


exposant = []
temps_naif = []
temps_rapide = []


y = 1

t1 = time.perf_counter()
puissance_naif(3, y)
t2 = time.perf_counter()
delta = t2 - t1

exposant.append(y)
temps_naif.append(delta)

t1 = time.perf_counter()
puissance_rapide(3, y)
t2 = time.perf_counter()

temps_rapide.append(t2 - t1)

while delta < temps:
    y *= 2

    t1 = time.perf_counter()
    puissance_naif(3, y)
    t2 = time.perf_counter()

    delta = t2 - t1

    exposant.append(y)
    temps_naif.append(delta)

    t1 = time.perf_counter()
    puissance_rapide(3, y)
    t2 = time.perf_counter()

    temps_rapide.append(t2 - t1)

for i in range(len(exposant)):
    print(exposant[i], temps_naif[i] / temps_rapide[i])


fig, ax = plt.subplots(figsize=(20, 5))

ax.set_title("complexités temporelles")
ax.set_xlabel('y')
ax.set_ylabel('temps')

ax.plot(exposant, temps_naif, 'o-')

ax2 = ax.twinx()
ax2.plot(exposant, temps_rapide, 'ro-')

plt.xscale('log')

plt.show()
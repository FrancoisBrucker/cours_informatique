import json
import random
from algos import ford_et_fulkerson

with open("../../projet-chemins-min/villes_10000_habitants.json") as entree:
    villes = json.load(entree)

france = {clé: set(valeur["voisins"]) for clé, valeur in villes.items()}

LA_MARNE = "Reims"

NOMBRE_TAXI = 20
T = 5
TAXI_DÉPART = random.sample(list(france), T)

K = 20

MAX_TAXI_ROUTE = 20
ct = dict()

for u in france:
    for v in france[u]:
        if (v, u) not in ct:
            ct[(u, v)] = random.randint(1, MAX_TAXI_ROUTE)
        else:
            ct[(u, v)] = ct[(v, u)]


MAX_PARKING = 50

population_villes = [nom for nom in france]
population_villes.sort(key=lambda x: villes[x]["population"])
population_villes.reverse()

p = dict()
pas = 0
for i in range(len(population_villes)):
    u = population_villes[i]
    if i / len(population_villes) >= pas / MAX_PARKING:
        pas += 1

    p[u] = pas
    p[u] = random.randint(1, MAX_PARKING)


def d_GPS(uv):
    v, v2 = uv
    return (villes[v]["longitude"] - villes[v2]["longitude"]) ** 2 + (
        villes[v]["latitude"] - villes[v2]["latitude"]
    ) ** 2


distances_villes = [(u, v) for u in france for v in france[u] if u < v]
distances_villes.sort(key=d_GPS)

MAX_DIST = 5

tv = dict()
pas = 0
for i in range(len(distances_villes)):
    u, v = distances_villes[i]
    # if i / len(distances_villes) >= pas / MAX_DIST:
    #     pas += 1

    tv[(u, v)] = tv[(v, u)] = int(MAX_DIST * i / len(distances_villes))


for u in france:
    print(u, p[u])
    for v in france[u]:
        print("    ", v, tv[(u, v)], ct[(u, v)])

K = 20

G = dict()
c = dict()
LA_MARNE = "Reims"

print("modélisation")
# sommets
print("sommets")
for v in france:
    for k in range(K + 1):
        G[(v, k)] = set()

# parking
print("parking")
for (v, k) in G:
    if k == K:
        continue
    G[(v, k)].add((v, k + 1))
    c[((v, k), (v, k + 1))] = p[v]


# routes
print("routes")
for (v, k) in G:
    for v2 in france[v]:
        if k > K - tv[(v, v2)]:
            continue

        G[(v, k)].add((v2, k + tv[(v, v2)]))
        c[((v, k), (v2, k + tv[(v, v2)]))] = ct[(v, v2)]

# Source
print("source")
G["s"] = set()

for v in TAXI_DÉPART:
    G["s"].add((v, 0))
    c[("s", (v, 0))] = NOMBRE_TAXI


# puits
print("puits")
G["p"] = set()
G[(LA_MARNE, K)].add("p")
c[((LA_MARNE, K), "p")] = NOMBRE_TAXI * T


print("f&f")
f = {uv: 0 for uv in c}

ford_et_fulkerson(G, c, "s", "p", f)

print(NOMBRE_TAXI * T, f[((LA_MARNE, K), "p")])


# reverse graph.
G_prim = {x: set() for x in G}
for u in G:
    for v in G[u]:
        G_prim[v].add(u)


def taxi_dans_ville_a_t(v, t):
    nb_taxi = 0
    for v in G_prim[(u, t)]:
        nb_taxi += f[(v, (u, t))]

    return nb_taxi


def taxi_entre_villes_a_t(u, v, t, k):
    if (temps - k < 0) or (temps - tv[(u, v)] + k < 0):
        return 0

    if (temps + k > K) or (temps - k + tv[(u, v)] > K):
        return 0

    return (
        f[(u, temps - k), (v, temps - k + tv[(u, v)])]
        + f[(v, temps - tv[(u, v)] + k), (u, temps + k)]
    )


print(">>>", TAXI_DÉPART)
for v in G["s"]:
    print(v[0], f[("s", v)], c[("s", v)])

print("=====")
for v in G_prim["p"]:
    print(v[0], f[(v, "p")], c[(v, "p")])

import matplotlib.pyplot as plt
import matplotlib.lines as mlines


print(">>>", TAXI_DÉPART)

fig, ax = plt.subplots(figsize=(10, 10))


for u in france:
    ax.text(villes[u]["longitude"], villes[u]["latitude"], u)
    for v in france[u]:
        if v > u:  # évite de tracer 2 fois le même arc
            continue

        ax.add_line(
            mlines.Line2D(
                (villes[u]["longitude"], villes[v]["longitude"]),
                (villes[u]["latitude"], villes[v]["latitude"]),
            )
        )

ax.plot(
    [villes[x]["longitude"] for x in france],
    [villes[x]["latitude"] for x in france],
    "o",
    color="black",
    markersize=2,
)
ax.plot(
    [villes[LA_MARNE]["longitude"]],
    [villes[LA_MARNE]["latitude"]],
    "*",
    color="red",
    markersize=20,
)
ax.plot(
    [villes[x]["longitude"] for x in TAXI_DÉPART],
    [villes[x]["latitude"] for x in TAXI_DÉPART],
    "o",
    color="red",
    markersize=10,
)

for temps in range(K + 1):
    [p.remove() for p in reversed(ax.patches)]

    for u in france:
        nb_taxi = taxi_dans_ville_a_t(u, temps)

        if nb_taxi > 0:
            circle = plt.Circle(
                (villes[u]["longitude"], villes[u]["latitude"]),
                0.2 * (1 + nb_taxi / (NOMBRE_TAXI * T)),
                color="g",
            )
            ax.add_patch(circle)

        for v in france[u]:
            if v > u:
                continue

            for k in range(1, tv[(u, v)]):
                nb_taxi = taxi_entre_villes_a_t(u, v, temps, k)

                if nb_taxi > 0:

                    circle = plt.Circle(
                        (
                            villes[u]["longitude"]
                            + k
                            * (villes[v]["longitude"] - villes[u]["longitude"])
                            / tv[(u, v)],
                            villes[u]["latitude"]
                            + k
                            * (villes[v]["latitude"] - villes[u]["latitude"])
                            / tv[(u, v)],
                        ),
                        0.2 * (1 + nb_taxi / (NOMBRE_TAXI * T)),
                        color="g",
                    )
                    ax.add_patch(circle)

    plt.pause(1)
plt.show()

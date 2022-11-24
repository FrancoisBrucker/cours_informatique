import geopandas as gpd
import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("../villes_france_30000.csv", skipinitialspace=True)


def lecture():
    print(df)
    # print(df.to_string())

    print(df.columns)
    print(df.dtypes)

    print(df["nom"])
    # print(df["nom"].to_string())  # convertit toute la colonne en string

    print(df["nom"] == "Marseille")
    print(df[df["nom"] == "Marseille"])


# lecture()


villes = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))
villes.set_crs("EPSG:4326")

# print(villes)

POPULATION = 50000
POPULATION = 10000

def plot_1():
    fig, ax = plt.subplots(figsize=(10, 5))

    # villes.plot(ax=ax)
    villes[villes["population"] > POPULATION].plot(ax=ax)

    plt.show()

    print(len(villes[villes["population"] > POPULATION]))


# plot_1()

import shapely.geometry

île_de_France = shapely.geometry.box(2.02, 48.7, 2.72, 48.98)

# v2 = villes[villes["geometry"].within(île_de_France)]
# print(v2[v2["population"] > POPULATION])
# print(len(v2[v2["population"] > POPULATION]))

# print(villes[villes["geometry"].within(île_de_France) & (villes["population"] > POPULATION)])

v2 = villes[(~villes.geometry.within(île_de_France)) | (villes["nom"] == "Paris")]
grandes_villes = v2[v2["population"] > POPULATION]

# print(grandes_villes)
# print(len(grandes_villes))


def plot_2():
    fig, ax = plt.subplots(figsize=(10, 5))

    grandes_villes.plot(ax=ax)

    plt.show()


# plot_2()

# print(grandes_villes["geometry"].apply(lambda g: grandes_villes.distance(g)))


marseille_df = villes[villes["nom"] == "Marseille"]


def marseille():
    # marseille = marseille_df.loc[1]
    marseille = marseille_df.iloc[0]
    print(marseille_df.index.tolist())

    print(grandes_villes.iloc[0]["geometry"].distance(marseille["geometry"]))

    print(grandes_villes["geometry"].distance(marseille["geometry"]))


marseille()

d = grandes_villes["geometry"].apply(lambda x: grandes_villes["geometry"].distance(x))
print(d)

i, j = 2, 91
print(d.loc[i, j])

i = grandes_villes[grandes_villes["nom"] == "Marseille"].index[0]
j = grandes_villes[grandes_villes["nom"] == "Rennes"].index[0]

print(d.loc[i, j])

MAX_DIST = 1
G = {}
f = {}
for i in grandes_villes.index:
    nom_i = grandes_villes.loc[i]["nom"]
    G[nom_i] = set()
    for j in grandes_villes.index:
        if d.loc[i, j] <= MAX_DIST:
            nom_j = grandes_villes.loc[j]["nom"]
            G[nom_i].add(nom_j)
            f[(nom_i, nom_j)] = d.loc[i, j]

# print(G)
# print(f)


def plot_3():
    import matplotlib.lines as mlines

    fig, ax = plt.subplots(figsize=(10, 5))

    grandes_villes.plot(ax=ax)

    for u in G:
        i = grandes_villes[grandes_villes["nom"] == u].index[0]
        point_i = grandes_villes.loc[i]["geometry"]
        for v in G[u]:
            j = grandes_villes[grandes_villes["nom"] == v].index[0]
            point_j = grandes_villes.loc[j]["geometry"]
            ax.add_line(mlines.Line2D((point_i.x, point_j.x), (point_i.y, point_j.y)))
    plt.show()


# plot_3()


print(grandes_villes["nom"].to_string())


from algos import les_composantes

for x in les_composantes(G):
    print(x)


print(d[i].sort_values())
print(">>>", d[i].sort_values().index[1])
print(grandes_villes.loc[4])


i = grandes_villes[grandes_villes["nom"] == "Ajaccio"].index[0]
proche = d[i].sort_values().index[1]

G["Ajaccio"].update({"Nice"})
G["Nice"].update({"Ajaccio"})

f[("Ajaccio", "Nice")] = d.loc[i, proche]
f[("Nice", "Ajaccio")] = d.loc[i, proche]

# plot_3()

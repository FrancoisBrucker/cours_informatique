import geopandas as gpd
import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("../villes_france_30000.csv", skipinitialspace=True)

print(df)
# print(df.to_string())

print(df.columns)
print(df.dtypes)

print(df["nom"])
# print(df["nom"].to_string())  # convertit toute la colonne en string

print(df["nom"] == "Marseille")
print(df[df["nom"] == "Marseille"])

villes = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))
villes.set_crs("EPSG:4326")

print(villes)



# fig, ax = plt.subplots(figsize=(10, 5))

# # villes.plot(ax=ax)
# villes[villes["population"] > 50000].plot(ax=ax)

# plt.show()

# print(len(villes[villes["population"] > 50000]))

import shapely.geometry

île_de_France = shapely.geometry.box(2.02, 48.7, 2.72, 48.98)

# v2 = villes[villes["geometry"].within(île_de_France)]
# print(v2[v2["population"] > 50000])
# print(len(v2[v2["population"] > 50000]))

# print(villes[villes["geometry"].within(île_de_France) & (villes["population"] > 50000)])

v2 = villes[(~villes.geometry.within(île_de_France)) | (villes["nom"] == "Paris")]
grandes_villes = v2[v2["population"] > 50000]
print(grandes_villes)
# print(len(grandes_villes))


# fig, ax = plt.subplots(figsize=(10, 5))

# grandes_villes.plot(ax=ax)

# plt.show()

# print(grandes_villes["geometry"].apply(lambda g: grandes_villes.distance(g)))

marseille = villes[villes["nom"] == "Marseille"].iloc[-1]



d = grandes_villes["geometry"].apply(lambda x: grandes_villes["geometry"].distance(x))
print(d)
print(d.loc[91])

print(d.loc[91][91])

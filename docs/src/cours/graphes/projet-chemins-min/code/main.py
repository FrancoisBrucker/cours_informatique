import geopandas as gpd
import pandas as pd


df = pd.read_csv("../villes_france_30000.csv")

print(df)
# print(df.to_string())

print(df.columns)
print(df.dtypes)

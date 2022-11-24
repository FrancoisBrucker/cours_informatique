import json

with open("../villes_10000_habitants.json") as entree:
    villes = json.load(entree)

print(villes)
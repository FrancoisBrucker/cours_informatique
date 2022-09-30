import csv
import json

pays = {}
with open('gps-pays-autres.csv', newline='') as csvfile:
    for row in csv.reader(csvfile, quotechar='"', quoting=csv.QUOTE_NONNUMERIC):
        pays[row[3]] = {
            "long": row[2],
            "lat": row[1],
        }

with open("voisins-pays.json", "r") as read_file:
    voisins = json.load(read_file)

print(len(voisins.keys()))
print(len(pays.keys()))
for x in sorted(list(set(pays.keys()) - set(voisins.keys()))):
    print(x)
print("----")
for x in sorted(list(set(voisins.keys()) - set(pays.keys()))):
    print(x)
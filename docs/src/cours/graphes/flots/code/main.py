from algos import marquage, chaîne_augmentante, augmentation_flot, ford_et_fulkerson, graphe_écart_valuation

G = {
    's': {'a', 'b'},
    'a': {'b', 'd'},
    'b': {'c', 'e'},
    'c': {'a', 'd', 'e'},
    'd': {'e', 'p'},
    'e': {'p'},
    'p': set()
}

c = {
    ('s', 'a'): 2,
    ('s', 'b'): 3,
    ('a', 'b'): 1,
    ('a', 'd'): 2,
    ('b', 'c'): 1,
    ('b', 'e'): 2,
    ('c', 'a'): 2,
    ('c', 'd'): 1,
    ('c', 'e'): 1,
    ('d', 'e'): 1,
    ('d', 'p'): 2,
    ('e', 'p'): 1
}

f = {
    ('s', 'a'): 1,
    ('s', 'b'): 0,
    ('a', 'b'): 1,
    ('a', 'd'): 1,
    ('b', 'c'): 1,
    ('b', 'e'): 0,
    ('c', 'a'): 1,
    ('c', 'd'): 0,
    ('c', 'e'): 0,
    ('d', 'e'): 0,
    ('d', 'p'): 1,
    ('e', 'p'): 0
}

f1 = dict(f)

marques = marquage(G, c, 's', 'p', f1)

for x, y in marques.items():
    print(x, y)

chaîne = chaîne_augmentante('s', 'p', marques)

print(chaîne)

augmentation_flot('s', 'p', marques, chaîne, f1)

print("après 1 chaîne")
for x, y in f1.items():
    print(x, y)

f1 = dict(f)
ford_et_fulkerson(G, c, 's', 'p', f1)

print("tout l'algorithme")

for x, y in f1.items():
    print(x, y)


print("marque avec flot maximum")

f1 = {
    ('s', 'a'): 2,
    ('s', 'b'): 1,
    ('a', 'b'): 1,
    ('a', 'd'): 2,
    ('b', 'c'): 1,
    ('b', 'e'): 1,
    ('c', 'a'): 1,
    ('c', 'd'): 0,
    ('c', 'e'): 0,
    ('d', 'e'): 0,
    ('d', 'p'): 2,
    ('e', 'p'): 1
}

marques = marquage(G, c, 's', 'p', f1)

for x, y in marques.items():
    print(x, y)


print("graphe d'écart :")

graphe, vf = graphe_écart_valuation(G, c, f, {uv: 1 for uv in c})

for x in graphe:
    print(x, graphe[x], [vf[(x, y)] for y in graphe[x]])

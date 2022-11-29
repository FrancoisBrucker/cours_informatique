G1 = {
    's': {'a', 'b'},
    'a': {'b', 'd'},
    'b': {'c', 'e'},
    'c': {'a', 'd', 'e'},
    'd': {'e', 'p'},
    'e': {'p'},
    'p': set()
}

c1 = {
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

f1 = {
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


from algos import marquage, chaîne_augmentante, augmentation_flot

marques = marquage(G1, c1, 's', 'p', f1)

for x, y in marques.items():
    print(x, y)

chaîne = chaîne_augmentante('s', 'p', marques)

print(chaîne)

augmentation_flot('s', 'p', marques, chaîne, f1)

for x, y in f1.items():
    print(x, y)
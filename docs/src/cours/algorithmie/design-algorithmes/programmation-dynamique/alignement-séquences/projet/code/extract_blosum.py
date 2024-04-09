# https://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt

PROTEINS = [
    "A",
    "R",
    "N",
    "D",
    "C",
    "Q",
    "E",
    "G",
    "H",
    "I",
    "L",
    "K",
    "M",
    "F",
    "P",
    "S",
    "T",
    "W",
    "Y",
    "V",
    "B",
    "Z",
    "X",
]

blosum = []
for l in open("blosum.txt").readlines():
    if l[0] not in PROTEINS:
        continue

    blosum.append([int(x) for x in l[1:].split()][:-1])

for l in blosum:
    print(l)


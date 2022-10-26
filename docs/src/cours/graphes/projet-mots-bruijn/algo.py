def mots(alphabet, p):
    compteur = [0] * p

    mots = [alphabet[0] * p]
    while compteur != [len(alphabet) - 1] * p:
        i = p - 1

        while compteur[i] == len(alphabet) - 1:
            i -= 1
        compteur[i] += 1
        for j in range(i + 1, p):
            compteur[j] = 0
        mots.append("".join(alphabet[x] for x in compteur))

    return mots


for mot in mots("01", 4):
    print(mot)

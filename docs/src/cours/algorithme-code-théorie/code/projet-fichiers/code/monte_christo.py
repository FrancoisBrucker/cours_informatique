import requests


def sauve():
    page = requests.get("http://www.gutenberg.org/cache/epub/17989/pg17989.txt")

    texte = page.text

    f = open("monte-cristo.txt", "w")
    f.write(texte)
    f.close()


# sauve()

monte = open("monte-cristo.txt").read()
carateres = set(monte)
print("nombre de caractères : ", len(carateres))

lettres = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÇÉÊÎÔàâçèéêëîïôùû")

for c in carateres - lettres:
    monte = monte.replace(c, " ")

mots = set(monte.split())

print("nombre de mots : ", len(monte.split()))
print("nombre de mots différents : ", len(set(mots)))

compte_mots = dict()
for mot in mots:
    compte_mots[mot] = 0

for mot in monte.split():
    compte_mots[mot] += 1

print('Nombre de "Marseille" :', compte_mots['Marseille'])

liste_mots = [(compte_mots[m], m) for m in compte_mots]
liste_mots.sort()
liste_mots.reverse()

nb_max = liste_mots[0][0]
i = 0
while liste_mots[i][0] >= nb_max / 2:
    print(liste_mots[i])
    i += 1



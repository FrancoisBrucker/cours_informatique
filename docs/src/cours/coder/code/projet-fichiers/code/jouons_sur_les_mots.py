import requests


def sauve():
    page = requests.get("https://raw.githubusercontent.com/hbenbel/French-Dictionary/master/dictionary/dictionary.csv")

    texte = page.text

    f = open("words.txt", "w")
    f.write(texte)
    f.close()


sauve()
exit()

mots = []
f = open("words.txt")
for mot in f:
    mots.append(mot.strip())

print("nombre de mots :", len(mots))
print("42ème mot :", mots[41])

compte = 0
for mot in mots:
    if mot[-1] == 'g':
        compte += 1
print("nombre de mots finissant par 'g' :", compte)

nombre_de_prout = 0
for mot in mots:
    if "prout" in mot:
        print(mot)
        nombre_de_prout += 1
print("nombre de prout :", nombre_de_prout)

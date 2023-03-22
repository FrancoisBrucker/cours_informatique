import requests


def sauve():
    page = requests.get("https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words")

    texte = page.text

    f = open("words.txt", "w")
    f.write(texte)
    f.close()


# sauve()

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

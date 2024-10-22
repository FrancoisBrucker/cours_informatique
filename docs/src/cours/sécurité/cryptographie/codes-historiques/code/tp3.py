import random


def majuscule(texte):
    """rend la chaine texte en majusucle

    Convertit les accent en majuscule non accentuees
    """

    alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZAAEEEEIIOUUUYC"
    alphabet2 = "abcdefghijklmnopqrstuvwxyzâàéèêëïîôùûüÿç"
    texteMaj = ""
    for l in texte:
        if l in alphabet2:
            texteMaj += alphabet1[alphabet2.index(l)]
        else:
            texteMaj += l
    return texteMaj


def texteSansEspaces(texte):
    """rend le texte sans espaces"""
    txt2 = ""
    for x in texte:
        if x == " ":
            continue
        txt2 += x
    return txt2


def frequences(texte, decalage=1):
    """rend les frequences des differents caracteres d'un texte
    texte ne doit contenir que des lettres (pas d'espaces)
    pour un decalage donne

    les lettres prisent en compte sont ceux d'indice 0+k*decalage (0<=k)
    """
    frequences = {}
    total = 0
    pos = 0
    while pos < len(texte):
        total += 1
        lettre = texte[pos]
        if lettre in frequences:
            frequences[lettre] += 1
        else:
            frequences[lettre] = 1
        pos += decalage

    for x in frequences:
        frequences[x] = 1.0 * frequences[x] / total
    return frequences


def ordreFrequences(texte, decalage=1):
    """rend un tableau contenant l'ordre d'appartition des lettres
    par ordre decroissant

    texte doit etre ecrit en majuscule et sans espaces
    """
    freq = frequences(texte, decalage)
    tab = []
    for x in freq:
        tab.append((freq[x], x))
    tab.sort()
    tab.reverse()
    tab2 = []
    for x in tab:
        tab2.append((x[1], x[0]))
    return tab2


def prems(nbmax):
    """rend un tableau contenant tous les nombres premiers inferieurs a nbMax"""
    # crible
    a = [True] * nbmax
    i = 2
    while i <= nbmax:
        suivant = nbmax + 1
        for j in range(i + 1, nbmax + 1):
            if j % i == 0:
                a[j - 1] = False
            elif (a[j - 1] == True) and (suivant == nbmax + 1):
                suivant = j
        i = suivant
    prems = []
    for i, x in enumerate(a):
        if x == True:
            prems.append(i + 1)
    return prems


def expomodulo(nombre, N, p):
    res = nombre % N
    if p == 0:
        return 1 % N
    for i in range(p - 1):
        res = (res * nombre) % N
    return res


def IC(texte, decalage=1):
    """calcul l'indice de coincidence mutuel d'un texte

    texte ne doit etre compose que de lettres de l'alphabet en majuscule
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    IC = 0
    nbetape = decalage
    for i in range(decalage):
        pos = i
        nbLettres = [0] * 26
        total = 0
        while pos < len(texte):
            nbLettres[alphabet.index(texte[pos])] += 1
            total += 1
            pos += decalage

        IClocal = 0
        for k in range(26):
            IClocal += nbLettres[k] * (nbLettres[k] - 1)
        if total > 1:
            IClocal = 1.0 * IClocal / (total * (total - 1))
        else:
            nbetape -= 1

        IC += IClocal
    if nbetape > 0:
        IC = IC / nbetape
    else:
        IC = 0
    return IC


def printIC(texte, decalageMax):
    """imprime le coefficient IC pour tous les decalages de 1 a decalageMax
    trie par ordre croissant

    texte doit etre ecrit en majuscule et sans espace
    """

    theTab = []
    for i in range(decalageMax):
        possible = IC(texte, i + 1)
        theTab.append((possible, i + 1))
    theTab.sort()
    print("Valeurs des IC triees :")
    for x in theTab:
        print("IC = %f decalage = %d " % (x[0], x[1]))


def printFrequences(texte, decalage):
    """imprime les frequences des lettres

    texte doit etre en majuscule et sans espaces
    """
    for dec in range(decalage):
        mesfreq = ordreFrequences(texte[dec:], decalage)
        print("lettres en pos", dec, "+ k * ", decalage, " : ")
        for x in mesfreq:
            print(
                x,
            )
        print("")


def ajouteEspaces(texte1, texte2):
    """rend texte1 ou l'on a ajoute les espaces aux positions de texte2
    texte 1 et texte2 doivent posseder le meme nombre de caracteres non espaces
    """
    texteSortie = ""
    pos = 0
    for x in texte2:
        if x != " ":
            texteSortie = texteSortie + texte1[pos]
            pos += 1
        else:
            texteSortie = texteSortie + " "
    return texteSortie


def cesarEncode(texte, cle):
    """encode un texte selon le code de Cesar

    cle : une lettre de l'alphabet en majucule : La lettre A devient cle
    texte : un texte ne comportant que des lettres de l'alphabet en majuscule
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(cle) != 1 or cle not in alphabet:
        raise (ValueError, "La cle doit etre une lettre de l'alphabet")

    decalage = alphabet.index(cle)
    texteCesar = ""
    for x in texte:
        texteCesar += alphabet[(alphabet.index(x) + decalage) % 26]

    return texteCesar


def cesarDecode(texte, cle):
    """Decode un texte encode selon le code de Cesar

    cle : une lettre de l'alphabet en majucule : La lettre A devient cle
    texte : un texte ne comportant que des lettres de l'alphabet en majuscule
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(cle) != 1 or cle not in alphabet:
        raise (ValueError, "La cle doit etre une lettre de l'alphabet")

    decalage = alphabet.index(cle)
    texteCesar = ""
    for x in texte:
        texteCesar += alphabet[(alphabet.index(x) - decalage) % 26]

    return texteCesar


def vigenereEncode(texte, motCle):
    """encode un texte selon le code de Vigenere

    cle : un mot de l'alphabet en majuscule
    texte : un texte ne comportant que des lettres de l'alphabet en majuscule.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    texteVigenere = ""
    pos = 0
    for x in texte:
        texteVigenere += alphabet[
            (alphabet.index(x) + alphabet.index(motCle[pos])) % 26
        ]
        pos = (pos + 1) % len(motCle)
    return texteVigenere


def vigenereDecode(texte, motCle):
    """Decode un texte encode selon le code de Vigenere

    cle : un mot de l'alphabet en majuscule
    texte : un texte ne comportant que des lettres de l'alphabet en majuscule.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    texteVigenere = ""
    pos = 0
    for x in texte:
        texteVigenere += alphabet[
            (alphabet.index(x) - alphabet.index(motCle[pos])) % 26
        ]
        pos = (pos + 1) % len(motCle)
    return texteVigenere


def RSAClef(nbmax):
    """retourne des clefs RSA de inferieures a nbMax

    retourne un triplet (N,p,s)
    """
    premiers = prems(nbmax)
    tab = random.sample(premiers[1:], 3)  # enleve 1
    s = max(tab)
    del tab[tab.index(s)]
    x = tab.pop()
    y = tab.pop()
    print(x, y, s)
    p = 1
    while p * s % ((x - 1) * (y - 1)) != 1:
        p += 1

    return (x * y, p, s)


def RSAEncode(texte, N, p):
    """Encode le texte facon RSA.
    le texte ne doit etre compose que de lettres et d'espaces

    si len(texte) n'est pas un multiple de N, des espaces sont rajoutes a la
    fin du texte
    """
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    N2 = N
    nbcar = 1  # nombre de chiffres necessaire pour N
    while N2 / 10 > 0:
        N2 = N2 / 10
        nbcar += 1
    if nbcar % 2 == 1:
        nbcar += 1
    nbcar = nbcar / 2  # nombre de caractere par encodage
    texteCode = ""
    i = 0
    while i < len(texte):
        nombre = 0
        for j in range(nbcar):
            if i + j < len(texte):
                nombre = (nombre * 100 + alphabet.index(majuscule(texte[i + j]))) % N
            else:
                nombre = (nombre * 100 + 0) % N  # espace en fin de chaine
        nombre = expomodulo(nombre, N, p)
        nombreChaine = str(nombre)
        nombreChaine = "0" * (2 * nbcar - len(nombreChaine)) + nombreChaine
        texteCode = texteCode + nombreChaine
        i += nbcar
    return texteCode


def RSADecode(texte, N, s):
    """Dencode le texte facon RSA.
    le texte ne doit etre compose que de lettres et d'espaces

    le nombre de caractere du texte non crypte doit etre un multiple de
    len(str(N)).
    """
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    N2 = N
    nbcar = 1  # nombre de chiffres necessaire pour N
    nbcar = len(str(N)) + len(str(N)) % 2

    texteDecode = ""
    i = 0
    while i < len(texte):
        nombre = 0
        if i + nbcar < len(texte):
            txt = texte[i : i + nbcar]
        else:
            txt = texte[i:]
        nombre = expomodulo(int(txt), N, s)

        boutTexte = ""
        for j in range(nbcar / 2):
            boutTexte = alphabet[nombre % 100] + boutTexte
            nombre = nombre / 100
        texteDecode = texteDecode + boutTexte
        i += nbcar

    return texteDecode


def codedecodeVigenere(texte, maFonction=vigenereEncode):
    """Crypte un texte encode selon vigenere
    texte doit etre compose de lettres de l'alphabet et d'espaces
    mafonction est soit egal a vigenereEncode, soit a vigenereDecode
    """
    entree = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    texte = majuscule(texte)
    texteNu = texteSansEspaces(texte)
    print("")
    print("Texte de depart : ")
    print(texte)

    entree = ""
    while entree not in ["_"]:
        entree = raw_input("cle ('_' pour quitter) : ")
        if entree in ["", "_"]:
            continue
        cle = majuscule(entree)
        texteCrypteNu = maFonction(texteNu, cle)
        texteCrypte = ajouteEspaces(texteCrypteNu, texte)
        print("Texte de depart : ")
        print(texte)
        print("Cle :")
        print(cle)
        print("Texte code : ")
        print(texteCrypte)
        print("IC :")
        printIC(texteNu, 10)
        print("Frequences : ")
        printFrequences(texteNu, len(cle))


# for x in ordreFrequences(majuscule(texteSansEspaces("Longtemps je me suis couche de bonne heure"))):
#     print(x)

print(vigenereEncode(majuscule(texteSansEspaces("Longtemps je me suis couche de bonne heure")), "PROUST"))
print(vigenereDecode("AFBALXBGGDWFTJICKVDLQBWWTSCHFXWVILW", "PROUST"))


printIC("AFBALXBGGDWFTJICKVDLQBWWTSCHFXWVILW", 10)

for i in range(6):
  print(i)
  for x in ordreFrequences("AFBALXBGGDWFTJICKVDLQBWWTSCHFXWVILW"[i:] +"AFBALXBGGDWFTJICKVDLQBWWTSCHFXWVILW"[:i], 6):
      print(x)
  print("---------")

print(vigenereDecode("AFBALXBGGDWFTJICKVDLQBWWTSCHFXWVILW", "PVELST"))

# print(vigenereEncode(majuscule(texteSansEspaces("Longtemps je me suis couche de bonne heure")), majuscule(texteSansEspaces("ALarecherc he du temp sperdu de marcel pro"))))
# print(vigenereDecode("LZNXXGTTJLLQHMNMERGJGYHXHFANEGLPJIS", majuscule(texteSansEspaces("ALarecherc he du temp sperdu de marcel pro"))))